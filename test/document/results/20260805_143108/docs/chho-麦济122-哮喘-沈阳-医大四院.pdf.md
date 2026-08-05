# 基准结果：chho-麦济122-哮喘-沈阳-医大四院.pdf

## 基本信息

- 文件：`chho-麦济122-哮喘-沈阳-医大四院.pdf`
- 大小：8763.4 KB
- PDF 总页数：13
- doc_id：`a747105e908311f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:09  完成时间：2026-08-05T14:31:10  耗时：1.0s
- progress_msg：`04:15:33 Indexing done (0.09s). Task done (253.39s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 35998448 | 1 | 1-1 | 2/4 沈阳市第四人民医院 THE FOURTH PEOPLE'S HOSPIT |
| 2 | 76c8c28e | 1 | 2-2 | 报告时间: 2025-01-02 \multicolumn{7}{c}{报告单} |
| 3 | 3e3dd467 | 1 | 3-3 | 报告时间: 2025-09-02 预计 实测 % (实/预) Date 25-9 |
| 4 | 7bbd8a36 | 1 | 6-6 | 辽宁崇文厚德医院 门诊病历 科室：呼吸内一科门诊 姓名： 职业： 就诊日期：20 |
| 5 | 4fd1babf | 1 | 7-7 | 新药特药大药房总店 流水单号 10020045213 结账时间 2025-11- |
| 6 | dbda5d0e | 1 | 8-8 | 2/4 25/09/02 14:58 普通 科 室:呼吸与危重症一门诊 诊断:( |
| 7 | 18f5901d | 2 | 8-9 | 2025/09/19 18:04 新药特药大药房总店 流水单号 10020044 |
| 8 | c233502f | 1 | 10-10 | 1/1 NO:25004949727 4号窗口 25/11/03 16:39 普 |
| 9 | 0016ca93 | 2 | 10-11 | 2025/11/05 14:51 沈阳市第四人民医院 处方笺 医疗类别:市医保  |
| 10 | ce1148c8 | 1 | 12-12 | 新药特药大药房总店 流水单号 10020046503 结账时间 2026-01- |
| 11 | 9d6a2063 | 1 | 13-13 | 沈阳市第四人民医院 处方笺 医疗类别:市医保 NO:26000513029 3号 |
| 12 | 24ee5966 | 2 | 4-5 | <table><tr><td>白细胞</td><td>None</td><td> |

- chunks 总数：12
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`
- 覆盖页数：13 / 13；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 3 | 3 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 4 | 4 | 4 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 2 | 2 | 2 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 2, "ExaminationReport": 2, "LabReport": 1, "MedicationRecord": 3, "PrescriptionRecord": 4}`
- ChunkMerger：`{"found": true, "merged": 12, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 3, "Extractor:Prescription": 4, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 2}, "filtered_noise": 3}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 04:15:31,418 INFO     29 [ChunkMerger] Merged 12 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 04:10:57,339 INFO     29 handle_task begin for task {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 04:10:57,579 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-05 04:10:57,633 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 04:10:57,670 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 04:10:57,670 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 04:10:57,678 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 04:10:57,678 INFO     29 ============================================================
2026-08-05 04:10:57,678 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 04:10:57,678 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 04:10:57,678 INFO     29 ============================================================
2026-08-05 04:10:57,678 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 04:10:57,679 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 04:10:57,680 INFO     29 No torch found.
2026-08-05 04:10:57,980 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-06"
}
```
2026-08-05 04:10:57,981 INFO     29 [qwen-vl-parser] page=45 classify=table report_date=2026-01-06
2026-08-05 04:10:57,987 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1364813, prompt_len=756
2026-08-05 04:10:59,569 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=13
2026-08-05 04:10:59,770 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931963, prompt_len=644
2026-08-05 04:11:01,865 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-08-23"}
```
2026-08-05 04:11:01,865 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2024-08-23
2026-08-05 04:11:01,876 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=931963, prompt_len=401
2026-08-05 04:11:04,592 INFO     29 [qwen-vl-parser] table API response (len=1104):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[颜色]颜色 & & 黄色 & & 清 & & [尿酸结晶]尿酸结晶 & & 0 & & 0~15 & 个/ul \\
[浊度]浊度 & & 清亮 & & 清 & & [草酸钙结晶]草酸钙结晶 & & 0 & & 0~30 & 个/ul \\
[GLU]葡萄糖 & & - & & 阴性 & & [上皮细胞]上皮细胞 & & 14 & & 0~20 & 个/ul \\
[BLD]潜血 & & - & & 阴性 & & [粘液丝]粘液丝 & & 5 & & 0~20 & 个/ul \\
[LEU]白细胞 & & 2+ & & 阴性 & & [酵母菌]酵母菌 & & 6 & $\uparrow$ & 0~0 & 个/ul \\
[PRO]蛋白质 & & - & & 阴性 & & [透明管型]透明管型 & & 0 & & 0~1 & 个/ul \\
[NIT]亚硝酸盐 & & + & & 阴性 & & [颗粒管型]颗粒管型 & & 0 & & 0~0 & 个/ul \\
[URO]尿胆素原 & & - & & 阴性 & & [小圆上皮]小圆上皮 & & 0 & & 0~3 & 个/ul \\
[BIL]胆红素 & & - & & 阴性 & & [其他管型]其他管型 & & 0 & & 0~0 & 个/ul \\
[KET]酮体 & & - & & 阴性 & & [其他上皮]其他上皮 & & 0 & & 0~10 & 个/ul \\
[Vc]维生素C & & - & & - & & [异常红细胞]异常红细胞 & & 0 & & 0~5 & 个/ul \\
[pH]酸碱性 & & 6.0 & & 5.0~8.5 & & [细菌]细菌 & & 1072 & $\uparrow$ & 0~50 & 个/ul \\
[SG]比重 & & 1.020 & & 1.010~ & & [尿沉渣镜检]尿沉渣镜检 & & : & & & \\
[红细胞]红细胞 & & 0 & & 0~5 & 个/ul & [白细胞]白细胞 & & +++/HP & & $\le$5/HP & \\
[白细胞]白细胞 & & 218 & $\uparrow$ & 0~7 & 个/ul & [红细胞]红细胞 & & 未查见 & & $\le$3/HP & \\
\hline
\end{tabular}
2026-08-05 04:11:04,592 INFO     29 [qwen-vl-parser] page=45 table: 22 LaTeX lines (bbox 1621-1642)
2026-08-05 04:11:04,592 INFO     29 [qwen-vl-parser] page=45 table: 22 sections
2026-08-05 04:11:04,710 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=644
2026-08-05 04:11:04,818 INFO     29 [qwen-vl-parser] text API response (len=484):
["2/4", "沈阳市第四人民医院", "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "门诊病历", "业：现住址：辽宁省沈阳市皇姑区延河街", "就诊科别：呼吸与危重症医学科门诊", "就诊时间：2024-08-23 16:00", "书写时间：2024-08-23 16:59", "供史者：患者本人", "主诉：支气管哮喘开药", "现病史：患者支气管哮喘，继续巩固治疗：", "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "孟鲁司特钠片", "10mg*5片，共10片", "每次10mg，QD", "睡前口服", "查体/专科查体：", "辅助检查：", "诊断：", "支气管哮喘", "处理意见：", "建议患者定期复查肺功能，肺部CT.", "我科随诊。", "建议休息天数：0天。", "患者下转：", "签名：杨昕", "患者签名：", "门诊病历专用章", "(1)", "vivo X80 此份", "ZEISS 书同等效力。", "2024/08/23 16:29"]
2026-08-05 04:11:04,818 INFO     29 [qwen-vl-parser] page=1 text: 32 lines (bbox 0-31)
2026-08-05 04:11:04,818 INFO     29 [qwen-vl-parser] page=1 text: 32 sections
2026-08-05 04:11:06,033 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1353736, prompt_len=644
2026-08-05 04:11:08,827 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:11:08,828 INFO     29 [qwen-vl-parser] page=46 classify=table report_date=2026-01-15
2026-08-05 04:11:08,834 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871040, prompt_len=756
2026-08-05 04:11:10,005 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-01-02"
}
```
2026-08-05 04:11:10,005 INFO     29 [qwen-vl-parser] page=2 classify=table report_date=2025-01-02
2026-08-05 04:11:10,012 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1353736, prompt_len=756
2026-08-05 04:11:11,742 INFO     29 [qwen-vl-parser] table API response (len=377):
\begin{tabular}{ccccccl}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\
{[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\
{[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \% \\
{[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\
{[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\
{[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\
\hline
\end{tabular}
2026-08-05 04:11:11,743 INFO     29 [qwen-vl-parser] page=46 table: 13 LaTeX lines (bbox 1643-1655)
2026-08-05 04:11:11,743 INFO     29 [qwen-vl-parser] page=46 table: 13 sections
2026-08-05 04:11:11,898 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=644
2026-08-05 04:11:13,418 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:11:13,419 INFO     29 [qwen-vl-parser] page=47 classify=table report_date=2026-01-15
2026-08-05 04:11:13,432 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1420685, prompt_len=756
2026-08-05 04:11:16,333 INFO     29 [qwen-vl-parser] table API response (len=1062):
\begin{tabular}{lcccccc}
\hline
\multicolumn{7}{c}{\textbf{报告单}} \\
\hline
出生日期: & 1983-6-17 & 性别: & 女 & & & \\
住院号: & 890730 & 年龄: & 42 Years & & & \\
身高: & 163 cm & 测试号: & 2025011002 & & & \\
& & 体重: & 70 kg & & & \\
\hline
\multicolumn{1}{c}{Time} & \multicolumn{1}{c}{预计} & \multicolumn{2}{c}{实1\%(实1/预)} & \multicolumn{2}{c}{实2\%(实2/预)} & \multicolumn{1}{c}{变异率} \\
\multicolumn{1}{c}{} & \multicolumn{1}{c}{} & \multicolumn{2}{c}{14:07:} & \multicolumn{2}{c}{14:26:} & \multicolumn{1}{c}{} \\
\hline
FVC & [L] & 3.24 & 3.05 & 94.1 & 3.34 & 103.1 & 9.6 \\
FEV 1 & [L] & 2.79 & 2.12 & 76.1 & 2.48 & 89.0 & 16.9 \\
FEV 1 \% FVC & [\%] & & 69.69 & & 74.33 & & 6.7 \\
FEV 1 \% VC MAX & [\%] & 81.12 & 63.16 & 77.9 & 72.42 & 89.3 & 14.7 \\
PEF & [L/s] & 6.59 & 6.83 & 103.5 & 6.59 & 99.9 & -3.5 \\
MEF 75 & [L/s] & 5.80 & 3.41 & 58.8 & 4.72 & 81.4 & 38.4 \\
MEF 50 & [L/s] & 4.10 & 2.30 & 56.2 & 2.16 & 52.7 & -6.2 \\
MEF 25 & [L/s] & 1.77 & 0.45 & 25.4 & 0.82 & 46.2 & 82.0 \\
MMEF 75/25 & [L/s] & 3.53 & 0.95 & 26.9 & 1.74 & 49.2 & 83.1 \\
\hline
\end{tabular}
2026-08-05 04:11:16,334 INFO     29 [qwen-vl-parser] page=2 table: 24 LaTeX lines (bbox 32-55)
2026-08-05 04:11:16,335 INFO     29 [qwen-vl-parser] page=2 table: 24 sections
2026-08-05 04:11:16,602 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645938, prompt_len=644
2026-08-05 04:11:18,666 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-09-02"
}
```
2026-08-05 04:11:18,666 INFO     29 [qwen-vl-parser] page=3 classify=table report_date=2025-09-02
2026-08-05 04:11:18,672 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1645938, prompt_len=756
2026-08-05 04:11:21,928 INFO     29 [qwen-vl-parser] table API response (len=1412):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
{[}WBC{]}白细胞数目 & & 4.20 & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & & 38.3 & & 35~45 & \% \\
{[}Lym\%{]}淋巴细胞百分比 & & 28.6 & & 20~50 & \% & {[}MCV{]}平均红细胞体积 & & 81.3 & $\downarrow$ & 82~100 & fL \\
{[}Mon\%{]}单核细胞百分比 & & 5.0 & & 3~10 & \% & {[}MCH{]}平均红细胞血红蛋白含量 & & 25.6 & $\downarrow$ & 27~34 & pg \\
{[}Neu\%{]}中性粒细胞百分比 & & 64.5 & & 40~75 & \% & {[}MCHC{]}平均红细胞血红蛋白浓度 & & 313 & $\downarrow$ & 316~354 & g/L \\
{[}Eos\%{]}嗜酸性细胞百分比 & & 1.7 & & 0.4~8 & \% & {[}RDW-CV{]}红细胞分布宽度变异系数 & & 14.9 & & 11~16 & \% \\
{[}Bas\%{]}嗜碱性细胞百分比 & & 0.2 & & 0.0~1.0 & \% & {[}RDW-SD{]}红细胞分布宽度标准差 & & 43.2 & & 35.0~56.0 & fL \\
{[}Lym\# {]}淋巴细胞数目 & & 1.20 & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & & 288 & & 125~350 & 10^9/L \\
{[}Mon\# {]}单核细胞数目 & & 0.21 & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & & 9.0 & & 6.5~12 & fL \\
{[}Neu\# {]}中性粒细胞数目 & & 2.71 & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & & 15.6 & & 9~17 & fL \\
{[}Eos\# {]}嗜酸性细胞数目 & & 0.07 & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & & 0.258 & & 0.108~ & \% \\
{[}Bas\# {]}嗜碱性细胞数目 & & 0.01 & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & & 19.3 & & 11~45 & \% \\
{[}RBC{]}红细胞数目 & & 4.71 & & 3.8~5.1 & 10^12/L & {[}IG\%{]}未成熟粒细胞百分比 & & 0.1 & & 0.0~0.6 & \% \\
{[}HGB{]}血红蛋白 & & 120 & & 115~150 & g/L & {[}IG\# {]}未成熟粒细胞计数 & & 0.00 & & 0.00~0.06 & 10^9/L \\
\hline
\end{tabular}
2026-08-05 04:11:21,929 INFO     29 [qwen-vl-parser] page=47 table: 20 LaTeX lines (bbox 1656-1675)
2026-08-05 04:11:21,929 INFO     29 [qwen-vl-parser] page=47 table: 20 sections
2026-08-05 04:11:22,085 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=644
2026-08-05 04:11:22,152 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:11:22.151+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:11:23,698 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:11:23,699 INFO     29 [qwen-vl-parser] page=48 classify=table report_date=2026-01-15
2026-08-05 04:11:23,712 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1427726, prompt_len=756
2026-08-05 04:11:24,628 INFO     29 [qwen-vl-parser] table API response (len=987):
\begin{tabular}{l c c c c}
\hline
& & 预计 & 实测 & \% (实/预) \\
\hline
Date & & & 25-9-02 & \\
Time & & & 14:07:38 & \\
\hline
VT & [L] & 0.50 & & \\
BF & [1/min] & 20.00 & & \\
MV & [L/min] & 10.00 & & \\
ERV & [L] & 1.07 & & \\
VC MAX & [L] & 3.31 & 3.36 & 101.6 \\
\hline
FVC & [L] & 3.24 & 3.05 & 94.1 \\
FEV 1 & [L] & 2.79 & 2.12 & 76.1 \\
FEV 1 \% FVC & [\%] & & 69.69 & \\
FEV 1 \% VC MAX & [\%] & 81.12 & 63.16 & 77.9 \\
PEF & [L/s] & 6.59 & 6.83 & 103.5 \\
MEF 75 & [L/s] & 5.80 & 3.41 & 58.8 \\
MEF 50 & [L/s] & 4.10 & 2.30 & 56.2 \\
MEF 25 & [L/s] & 1.77 & 0.45 & 25.4 \\
MMEF 75/25 & [L/s] & 3.53 & 0.95 & 26.9 \\
\hline
MVV & [L/min] & 103.77 & & \\
FEV 1*30 & [L/min] & 103.77 & 63.70 & 61.4 \\
\hline
RV-SB & [L] & 1.62 & 2.06 & 127.2 \\
RV\%TLC-SB & [\%] & 33.24 & 40.20 & 120.9 \\
TLC-SB & [L] & 4.97 & 5.13 & 103.3 \\
FRC-SB & [L] & 2.69 & 2.97 & 110.3 \\
FRC\%TLC-SB & [\%] & 51.82 & 57.88 & 111.7 \\
DLCO SB & [mmol/min/kPa] & 8.54 & 5.51 & (64.6) \\
\hline
\end{tabular}
2026-08-05 04:11:24,628 INFO     29 [qwen-vl-parser] page=3 table: 35 LaTeX lines (bbox 56-90)
2026-08-05 04:11:24,628 INFO     29 [qwen-vl-parser] page=3 table: 35 sections
2026-08-05 04:11:24,730 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=662622, prompt_len=644
2026-08-05 04:11:26,180 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2025-09-02"
}
```
2026-08-05 04:11:26,181 INFO     29 [qwen-vl-parser] page=4 classify=table report_date=2025-09-02
2026-08-05 04:11:26,187 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=662622, prompt_len=756
2026-08-05 04:11:29,128 INFO     29 [qwen-vl-parser] table API response (len=497):
\begin{tabular}{lrrrr}
\hline
检查项目 & 结果 & 单位 & 参考值 \\
\hline
白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\
红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\
血红蛋白 & 138 & g/L & 115--150 \\
血小板 & 300 & 10^9/L & 125--350 \\
红细胞压积 & 41.30 & \% & 35--45 \\
红细胞平均体积 & 83.60 & fL & 82--100 \\
平均血红蛋白量 & 28.00 & pg & 27--34 \\
平均血红蛋白浓 & 334 & g/L & 316--354 \\
度 & & & \\
中性粒细胞比率 & 54.20 & \% & 40--75 \\
淋巴细胞比率 & 36.10 & \% & 20--50 \\
单核细胞比率 & 3.70 & \% & 3--10 \\
嗜酸性粒细胞比 & 5.50 & \% & 0.4--8.0 \\
率 & & & \\
\hline
\end{tabular}
2026-08-05 04:11:29,130 INFO     29 [qwen-vl-parser] page=4 table: 21 LaTeX lines (bbox 91-111)
2026-08-05 04:11:29,130 INFO     29 [qwen-vl-parser] page=4 table: 21 sections
2026-08-05 04:11:29,254 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871197, prompt_len=644
2026-08-05 04:11:30,918 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-05 04:11:30,918 INFO     29 [qwen-vl-parser] page=5 classify=table report_date=None
2026-08-05 04:11:30,931 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=871197, prompt_len=756
2026-08-05 04:11:36,577 INFO     29 [qwen-vl-parser] table API response (len=957):
\begin{tabular}{cccccc}
\hline
& & & & & \\
红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\
血红蛋白 & 138 & g/L & 115--150 & & \\
血小板 & 300 & 10^9/L & 125--350 & & \\
红细胞压积 & 41.30 & \% & 35--45 & & \\
红细胞平均体积 & 83.60 & fL & 82--100 & & \\
平均血红蛋白量 & 28.00 & pg & 27--34 & & \\
平均血红蛋白浓 & 334 & g/L & 316--354 & & \\
度 & & & & & \\
中性粒细胞比率 & 54.20 & \% & 40--75 & & \\
淋巴细胞比率 & 36.10 & \% & 20--50 & & \\
单核细胞比率 & 3.70 & \% & 3--10 & & \\
嗜酸性粒细胞比 & 5.50 & \% & 0.4--8.0 & & \\
率 & & & & & \\
嗜碱性粒细胞比 & 0.50 & \% & 0--1 & & \\
率 & & & & & \\
中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\
淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\
单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\
嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\
嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\
红细胞分布宽度 & 12.9 & \% & 11.0--16.0 & & \\
变异系数 & & & & & \\
血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\
平均血小板体积 & 10.2 & fL & 9--13 & & \\
血小板压积 & 0.31 & \% & 0.10--0.28 & & \\
C反应蛋白 & 7.92 & mg/L & 0--6 & & \\
\hline
\end{tabular}
2026-08-05 04:11:36,578 INFO     29 [qwen-vl-parser] page=5 table: 31 LaTeX lines (bbox 112-142)
2026-08-05 04:11:36,578 INFO     29 [qwen-vl-parser] page=5 table: 31 sections
2026-08-05 04:11:37,029 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2251643, prompt_len=644
2026-08-05 04:11:42,754 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:11:42,754 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 04:11:42,763 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2251643, prompt_len=401
2026-08-05 04:11:45,947 INFO     29 [qwen-vl-parser] text API response (len=452):
["辽宁崇文厚德医院", "门诊病历", "科室：呼吸内一科门诊", "姓名：", "职业：", "就诊日期：2025/11/08 10:11:23", "主诉：反复喘息2年，加重1周", "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "既往史：否认。", "过敏史：{无}", "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "性。", "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "初步诊断：1、支气管哮喘 急性发作期", "处理：", "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "2.1周后复诊，病情变化随诊。", "医生签名：王春", "王春", "白", "第 1 页"]
2026-08-05 04:11:45,947 INFO     29 [qwen-vl-parser] page=6 text: 23 lines (bbox 143-165)
2026-08-05 04:11:45,947 INFO     29 [qwen-vl-parser] page=6 text: 23 sections
2026-08-05 04:11:46,375 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194363, prompt_len=644
2026-08-05 04:11:47,696 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:11:47,697 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-05 04:11:47,709 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2194363, prompt_len=401
2026-08-05 04:11:49,833 INFO     29 [qwen-vl-parser] text API response (len=263):
["新药特药大药房总店", "流水单号 10020045213", "结账时间 2025-11-08 15:22:19", "编号 数量 单价 金额 营业员", "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "Sr1/库存2", "0310145 2 盒 34.00 68.00", "合计 68.00", "优惠：0.00 微信：0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据，药品为特殊、", "商品，售出概不退还！"]
2026-08-05 04:11:49,833 INFO     29 [qwen-vl-parser] page=7 text: 16 lines (bbox 166-181)
2026-08-05 04:11:49,834 INFO     29 [qwen-vl-parser] page=7 text: 16 sections
2026-08-05 04:11:50,011 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=770597, prompt_len=644
2026-08-05 04:11:51,454 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-09-19"}
```
2026-08-05 04:11:51,455 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-09-19
2026-08-05 04:11:51,463 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=770597, prompt_len=401
2026-08-05 04:11:53,866 INFO     29 [qwen-vl-parser] text API response (len=342):
["2/4", "25/09/02 14:58", "普通", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "孟鲁司特钠片【舒宁安】乙", "超量说明:", "【10mg*5片】", "(4.96元/盒)", "3盒", "用法用量:每次10mg,睡前口服,每天一次", "医师:杨沂发药:修泉涌配药:沈瑶", "vivo X80 · ZEISS", "计:208.48/208.48", "第1页/共1页", "2025/09/19 18:04"]
2026-08-05 04:11:53,866 INFO     29 [qwen-vl-parser] page=8 text: 22 lines (bbox 182-203)
2026-08-05 04:11:53,866 INFO     29 [qwen-vl-parser] page=8 text: 22 sections
2026-08-05 04:11:53,994 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=952454, prompt_len=644
2026-08-05 04:11:54,757 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:11:54.756+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:11:55,362 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 04:11:55,362 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-05 04:11:55,378 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=952454, prompt_len=401
2026-08-05 04:11:57,451 INFO     29 [qwen-vl-parser] text API response (len=274):
["新药特药大药房总店", "流水单号 10020044912", "结账时间 2025-10-14 08:34:01", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]
2026-08-05 04:11:57,451 INFO     29 [qwen-vl-parser] page=9 text: 16 lines (bbox 204-219)
2026-08-05 04:11:57,451 INFO     29 [qwen-vl-parser] page=9 text: 16 sections
2026-08-05 04:11:57,620 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=758856, prompt_len=644
2026-08-05 04:11:58,893 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:11:58,893 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-05 04:11:58,902 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=758856, prompt_len=401
2026-08-05 04:12:01,153 INFO     29 [qwen-vl-parser] text API response (len=303):
["1/1", "NO:25004949727", "4号窗口", "25/11/03 16:39", "普通", "病志号:55161248", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【500g:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:沈瑶配药:巴艺洁", "vivo X80 · ZEISS", "金额合计:193.6/193.6", "第1页/共1页", "2025/11/05 14:51"]
2026-08-05 04:12:01,155 INFO     29 [qwen-vl-parser] page=10 text: 19 lines (bbox 220-238)
2026-08-05 04:12:01,155 INFO     29 [qwen-vl-parser] page=10 text: 19 sections
2026-08-05 04:12:01,431 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1190809, prompt_len=644
2026-08-05 04:12:02,857 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:12:02,857 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-05 04:12:02,863 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1190809, prompt_len=401
2026-08-05 04:12:05,122 INFO     29 [qwen-vl-parser] text API response (len=304):
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:25005558582", "4号窗口", "25/12/08 14:00", "普通", "病志号:55161248", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "vivo X80 · ZEISS", "医师:杨昕发药:李琳配药:巴艺洁", "2025/12/31 18:28金额合计:193.6/193.6", "第1页/共1页"]
2026-08-05 04:12:05,122 INFO     29 [qwen-vl-parser] page=11 text: 18 lines (bbox 239-256)
2026-08-05 04:12:05,123 INFO     29 [qwen-vl-parser] page=11 text: 18 sections
2026-08-05 04:12:05,496 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1881057, prompt_len=644
2026-08-05 04:12:06,686 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:12:06,686 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-05 04:12:06,694 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1881057, prompt_len=401
2026-08-05 04:12:09,014 INFO     29 [qwen-vl-parser] text API response (len=314):
["新药特药大药房总店", "流水单号", "10020046503", "结账时间", "2026-01-02 18:12:29", "编号", "数量", "单价", "金额", "营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "泡/葛兰素史克(集团)/库存1", "0200127", "1", "盒", "199.00", "199.00", "合计", "199.00", "优惠:0.00", "微信:0.00", "收银", "1002", "银台", "会员", "本次积分", "0.00", "累计积分", "0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]
2026-08-05 04:12:09,015 INFO     29 [qwen-vl-parser] page=12 text: 31 lines (bbox 257-287)
2026-08-05 04:12:09,015 INFO     29 [qwen-vl-parser] page=12 text: 31 sections
2026-08-05 04:12:09,318 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1396520, prompt_len=644
2026-08-05 04:12:13,358 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:12:13,358 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=None
2026-08-05 04:12:13,365 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1396520, prompt_len=401
2026-08-05 04:12:15,479 INFO     29 [qwen-vl-parser] text API response (len=267):
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:26000513029", "3号窗口", "26/01/30 13:26", "普通", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "【50ug:250ug/泡*60泡/(193.60元/盒) 1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:李琳 配药:乔军", "金额合计:193.6/193.6", "第1页/共1页"]
2026-08-05 04:12:15,480 INFO     29 [qwen-vl-parser] page=13 text: 16 lines (bbox 288-303)
2026-08-05 04:12:15,480 INFO     29 [qwen-vl-parser] page=13 text: 16 sections
2026-08-05 04:12:15,480 INFO     29 [qwen-vl-parser] parse_pdf done: 304 sections from 13 pages.
2026-08-05 04:12:15,486 INFO     29 Close text detector.
2026-08-05 04:12:15,842 INFO     29 Close text recognizer.
2026-08-05 04:12:16,199 INFO     29 Close recognizer.
2026-08-05 04:12:16,578 INFO     29 Close recognizer.
2026-08-05 04:12:17,061 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 04:12:17,061 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Parser:MedLink | outputs={"html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "json"}
2026-08-05 04:12:17,061 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 04:12:17,084 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:12:17,085 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2/4\n[BBOX-1] 沈阳市第四人民医院\n[BBOX-2] THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG\n[BBOX-3] 门诊病历\n[BBOX-4] 业：现住址：辽宁省沈阳市皇姑区延河街\n[BBOX-5] 就诊科别：呼吸与危重症医学科门诊\n[BBOX-6] 就诊时间：2024-08-23 16:00\n[BBOX-7] 书写时间：2024-08-23 16:59\n[BBOX-8] 供史者：患者本人\n[BBOX-9] 主诉：支气管哮喘开药\n[BBOX-10] 现病史：患者支气管哮喘，继续巩固治疗：\n[BBOX-11] 沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒\n[BBOX-12] 孟鲁司特钠片\n[BBOX-13] 10mg*5片，共10片\n[BBOX-14] 每次10mg，QD\n[BBOX-15] 睡前口服\n[BBOX-16] 查体/专科查体：\n[BBOX-17] 辅助检查：\n[BBOX-18] 诊断：\n[BBOX-19] 支气管哮喘\n[BBOX-20] 处理意见：\n[BBOX-21] 建议患者定期复查肺功能，肺部CT.\n[BBOX-22] 我科随诊。\n[BBOX-23] 建议休息天数：0天。\n[BBOX-24] 患者下转：\n[BBOX-25] 签名：杨昕\n[BBOX-26] 患者签名：\n[BBOX-27] 门诊病历专用章\n[BBOX-28] (1)\n[BBOX-29] vivo X80 此份\n[BBOX-30] ZEISS 书同等效力。\n[BBOX-31] 2024/08/23 16:29\n[BBOX-32] \\begin{tabular}{lcccccc}\n[BBOX-33] 报告时间: 2025-01-02\n[BBOX-34] \\hline\n[BBOX-35] \\multicolumn{7}{c}{\\textbf{报告单}} \\\\\n[BBOX-36] \\hline\n[BBOX-37] 出生日期: & 1983-6-17 & 性别: & 女 & & & \\\\\n[BBOX-38] 住院号: & 890730 & 年龄: & 42 Years & & & \\\\\n[BBOX-39] 身高: & 163 cm & 测试号: & 2025011002 & & & \\\\\n[BBOX-40] & & 体重: & 70 kg & & & \\\\\n[BBOX-41] \\hline\n[BBOX-42] \\multicolumn{1}{c}{Time} & \\multicolumn{1}{c}{预计} & \\multicolumn{2}{c}{实1\\%(实1/预)} & \\multicolumn{2}{c}{实2\\%(实2/预)} & \\multicolumn{1}{c}{变异率} \\\\\n[BBOX-43] \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{} & \\multicolumn{2}{c}{14:07:} & \\multicolumn{2}{c}{14:26:} & \\multicolumn{1}{c}{} \\\\\n[BBOX-44] \\hline\n[BBOX-45] FVC & [L] & 3.24 & 3.05 & 94.1 & 3.34 & 103.1 & 9.6 \\\\\n[BBOX-46] FEV 1 & [L] & 2.79 & 2.12 & 76.1 & 2.48 & 89.0 & 16.9 \\\\\n[BBOX-47] FEV 1 \\% FVC & [\\%] & & 69.69 & & 74.33 & & 6.7 \\\\\n[BBOX-48] FEV 1 \\% VC MAX & [\\%] & 81.12 & 63.16 & 77.9 & 72.42 & 89.3 & 14.7 \\\\\n[BBOX-49] PEF & [L/s] & 6.59 & 6.83 & 103.5 & 6.59 & 99.9 & -3.5 \\\\\n[BBOX-50] MEF 75 & [L/s] & 5.80 & 3.41 & 58.8 & 4.72 & 81.4 & 38.4 \\\\\n[BBOX-51] MEF 50 & [L/s] & 4.10 & 2.30 & 56.2 & 2.16 & 52.7 & -6.2 \\\\\n[BBOX-52] MEF 25 & [L/s] & 1.77 & 0.45 & 25.4 & 0.82 & 46.2 & 82.0 \\\\\n[BBOX-53] MMEF 75/25 & [L/s] & 3.53 & 0.95 & 26.9 & 1.74 & 49.2 & 83.1 \\\\\n[BBOX-54] \\hline\n[BBOX-55] \\end{tabular}\n[BBOX-56] \\begin{tabular}{l c c c c}\n[BBOX-57] 报告时间: 2025-09-02\n[BBOX-58] \\hline\n[BBOX-59] & & 预计 & 实测 & \\% (实/预) \\\\\n[BBOX-60] \\hline\n[BBOX-61] Date & & & 25-9-02 & \\\\\n[BBOX-62] Time & & & 14:07:38 & \\\\\n[BBOX-63] \\hline\n[BBOX-64] VT & [L] & 0.50 & & \\\\\n[BBOX-65] BF & [1/min] & 20.00 & & \\\\\n[BBOX-66] MV & [L/min] & 10.00 & & \\\\\n[BBOX-67] ERV & [L] & 1.07 & & \\\\\n[BBOX-68] VC MAX & [L] & 3.31 & 3.36 & 101.6 \\\\\n[BBOX-69] \\hline\n[BBOX-70] FVC & [L] & 3.24 & 3.05 & 94.1 \\\\\n[BBOX-71] FEV 1 & [L] & 2.79 & 2.12 & 76.1 \\\\\n[BBOX-72] FEV 1 \\% FVC & [\\%] & & 69.69 & \\\\\n[BBOX-73] FEV 1 \\% VC MAX & [\\%] & 81.12 & 63.16 & 77.9 \\\\\n[BBOX-74] PEF & [L/s] & 6.59 & 6.83 & 103.5 \\\\\n[BBOX-75] MEF 75 & [L/s] & 5.80 & 3.41 & 58.8 \\\\\n[BBOX-76] MEF 50 & [L/s] & 4.10 & 2.30 & 56.2 \\\\\n[BBOX-77] MEF 25 & [L/s] & 1.77 & 0.45 & 25.4 \\\\\n[BBOX-78] MMEF 75/25 & [L/s] & 3.53 & 0.95 & 26.9 \\\\\n[BBOX-79] \\hline\n[BBOX-80] MVV & [L/min] & 103.77 & & \\\\\n[BBOX-81] FEV 1*30 & [L/min] & 103.77 & 63.70 & 61.4 \\\\\n[BBOX-82] \\hline\n[BBOX-83] RV-SB & [L] & 1.62 & 2.06 & 127.2 \\\\\n[BBOX-84] RV\\%TLC-SB & [\\%] & 33.24 & 40.20 & 120.9 \\\\\n[BBOX-85] TLC-SB & [L] & 4.97 & 5.13 & 103.3 \\\\\n[BBOX-86] FRC-SB & [L] & 2.69 & 2.97 & 110.3 \\\\\n[BBOX-87] FRC\\%TLC-SB & [\\%] & 51.82 & 57.88 & 111.7 \\\\\n[BBOX-88] DLCO SB & [mmol/min/kPa] & 8.54 & 5.51 & (64.6) \\\\\n[BBOX-89] \\hline\n[BBOX-90] \\end{tabular}\n[BBOX-91] \\begin{tabular}{lrrrr}\n[BBOX-92] 报告时间: 2025-09-02\n[BBOX-93] \\hline\n[BBOX-94] 检查项目 & 结果 & 单位 & 参考值 \\\\\n[BBOX-95] \\hline\n[BBOX-96] 白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\\\\n[BBOX-97] 红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\\\\n[BBOX-98] 血红蛋白 & 138 & g/L & 115--150 \\\\\n[BBOX-99] 血小板 & 300 & 10^9/L & 125--350 \\\\\n[BBOX-100] 红细胞压积 & 41.30 & \\% & 35--45 \\\\\n[BBOX-101] 红细胞平均体积 & 83.60 & fL & 82--100 \\\\\n[BBOX-102] 平均血红蛋白量 & 28.00 & pg & 27--34 \\\\\n[BBOX-103] 平均血红蛋白浓 & 334 & g/L & 316--354 \\\\\n[BBOX-104] 度 & & & \\\\\n[BBOX-105] 中性粒细胞比率 & 54.20 & \\% & 40--75 \\\\\n[BBOX-106] 淋巴细胞比率 & 36.10 & \\% & 20--50 \\\\\n[BBOX-107] 单核细胞比率 & 3.70 & \\% & 3--10 \\\\\n[BBOX-108] 嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 \\\\\n[BBOX-109] 率 & & & \\\\\n[BBOX-110] \\hline\n[BBOX-111] \\end{tabular}\n[BBOX-112] \\begin{tabular}{cccccc}\n[BBOX-113] \\hline\n[BBOX-114] & & & & & \\\\\n[BBOX-115] 红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\\\\n[BBOX-116] 血红蛋白 & 138 & g/L & 115--150 & & \\\\\n[BBOX-117] 血小板 & 300 & 10^9/L & 125--350 & & \\\\\n[BBOX-118] 红细胞压积 & 41.30 & \\% & 35--45 & & \\\\\n[BBOX-119] 红细胞平均体积 & 83.60 & fL & 82--100 & & \\\\\n[BBOX-120] 平均血红蛋白量 & 28.00 & pg & 27--34 & & \\\\\n[BBOX-121] 平均血红蛋白浓 & 334 & g/L & 316--354 & & \\\\\n[BBOX-122] 度 & & & & & \\\\\n[BBOX-123] 中性粒细胞比率 & 54.20 & \\% & 40--75 & & \\\\\n[BBOX-124] 淋巴细胞比率 & 36.10 & \\% & 20--50 & & \\\\\n[BBOX-125] 单核细胞比率 & 3.70 & \\% & 3--10 & & \\\\\n[BBOX-126] 嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 & & \\\\\n[BBOX-127] 率 & & & & & \\\\\n[BBOX-128] 嗜碱性粒细胞比 & 0.50 & \\% & 0--1 & & \\\\\n[BBOX-129] 率 & & & & & \\\\\n[BBOX-130] 中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\\\\n[BBOX-131] 淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\\\\n[BBOX-132] 单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\\\\n[BBOX-133] 嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\\\\n[BBOX-134] 嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\\\\n[BBOX-135] 红细胞分布宽度 & 12.9 & \\% & 11.0--16.0 & & \\\\\n[BBOX-136] 变异系数 & & & & & \\\\\n[BBOX-137] 血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\\\\n[BBOX-138] 平均血小板体积 & 10.2 & fL & 9--13 & & \\\\\n[BBOX-139] 血小板压积 & 0.31 & \\% & 0.10--0.28 & & \\\\\n[BBOX-140] C反应蛋白 & 7.92 & mg/L & 0--6 & & \\\\\n[BBOX-141] \\hline\n[BBOX-142] \\end{tabular}\n[BBOX-143] 辽宁崇文厚德医院\n[BBOX-144] 门诊病历\n[BBOX-145] 科室：呼吸内一科门诊\n[BBOX-146] 姓名：\n[BBOX-147] 职业：\n[BBOX-148] 就诊日期：2025/11/08 10:11:23\n[BBOX-149] 主诉：反复喘息2年，加重1周\n[BBOX-150] 现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万\n[BBOX-151] 林”治疗，症状稍有改善，为求进一步诊治来我院就诊。\n[BBOX-152] 既往史：否认。\n[BBOX-153] 过敏史：{无}\n[BBOX-154] 体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。\n[BBOX-155] 辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试\n[BBOX-156] 性。\n[BBOX-157] 抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.\n[BBOX-158] 初步诊断：1、支气管哮喘 急性发作期\n[BBOX-159] 处理：\n[BBOX-160] 1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。\n[BBOX-161] 2.1周后复诊，病情变化随诊。\n[BBOX-162] 医生签名：王春\n[BBOX-163] 王春\n[BBOX-164] 白\n[BBOX-165] 第 1 页\n[BBOX-166] 新药特药大药房总店\n[BBOX-167] 流水单号 10020045213\n[BBOX-168] 结账时间 2025-11-08 15:22:19\n[BBOX-169] 编号 数量 单价 金额 营业员\n[BBOX-170] 甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It\n[BBOX-171] Sr1/库存2\n[BBOX-172] 0310145 2 盒 34.00 68.00\n[BBOX-173] 合计 68.00\n[BBOX-174] 优惠：0.00 微信：0.00\n[BBOX-175] 收银 1002\n[BBOX-176] 银台\n[BBOX-177] 会员\n[BBOX-178] 本次积分 0.00\n[BBOX-179] 累计积分 0.00\n[BBOX-180] 此票为开发票依据，药品为特殊、\n[BBOX-181] 商品，售出概不退还！\n[BBOX-182] 2/4\n[BBOX-183] 25/09/02 14:58\n[BBOX-184] 普通\n[BBOX-185] 科\n[BBOX-186] 室:呼吸与危重症一门诊\n[BBOX-187] 诊断:(J45.900x001)支气管哮喘\n[BBOX-188] Rp\n[BBOX-189] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-190] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-191] 1盒\n[BBOX-192] 用法用量:每次300ug,吸入,每天二次\n[BBOX-193] 孟鲁司特钠片【舒宁安】乙\n[BBOX-194] 超量说明:\n[BBOX-195] 【10mg*5片】\n[BBOX-196] (4.96元/盒)\n[BBOX-197] 3盒\n[BBOX-198] 用法用量:每次10mg,睡前口服,每天一次\n[BBOX-199] 医师:杨沂发药:修泉涌配药:沈瑶\n[BBOX-200] vivo X80 · ZEISS\n[BBOX-201] 计:208.48/208.48\n[BBOX-202] 第1页/共1页\n[BBOX-203] 2025/09/19 18:04\n[BBOX-204] 新药特药大药房总店\n[BBOX-205] 流水单号 10020044912\n[BBOX-206] 结账时间 2025-10-14 08:34:01\n[BBOX-207] 编号 数量 单价 金额 营业员\n[BBOX-208] 沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug\n[BBOX-209] 泡/葛兰素史克(集团)/库存1\n[BBOX-210] 0200127 1 盒 199.00 199.00\n[BBOX-211] 合计 199.00\n[BBOX-212] 优惠:0.00 微信:0.00\n[BBOX-213] 收银 1002\n[BBOX-214] 银台\n[BBOX-215] 会员\n[BBOX-216] 本次积分 0.00\n[BBOX-217] 累计积分 0.00\n[BBOX-218] 此票为开发票依据,药品为特殊、\n[BBOX-219] 商品,售出概不退还!\n[BBOX-220] 1/1\n[BBOX-221] NO:25004949727\n[BBOX-222] 4号窗口\n[BBOX-223] 25/11/03 16:39\n[BBOX-224] 普通\n[BBOX-225] 病志号:55161248\n[BBOX-226] 科\n[BBOX-227] 室:呼吸与危重症一门诊\n[BBOX-228] 诊断:(J45.900x001)支气管哮喘\n[BBOX-229] Rp\n[BBOX-230] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-231] 【500g:250ug/泡*60泡/(193.60元/盒)\n[BBOX-232] 1盒\n[BBOX-233] 用法用量:每次300ug,吸入,每天二次\n[BBOX-234] 医师:杨昕发药:沈瑶配药:巴艺洁\n[BBOX-235] vivo X80 · ZEISS\n[BBOX-236] 金额合计:193.6/193.6\n[BBOX-237] 第1页/共1页\n[BBOX-238] 2025/11/05 14:51\n[BBOX-239] 沈阳市第四人民医院\n[BBOX-240] 处方笺\n[BBOX-241] 医疗类别:市医保\n[BBOX-242] NO:25005558582\n[BBOX-243] 4号窗口\n[BBOX-244] 25/12/08 14:00\n[BBOX-245] 普通\n[BBOX-246] 病志号:55161248\n[BBOX-247] 诊断:(J45.900x001)支气管哮喘\n[BBOX-248] Rp\n[BBOX-249] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n[BBOX-250] 【50ug:250ug/泡*60泡/(193.60元/盒)\n[BBOX-251] 1盒\n[BBOX-252] 用法用量:每次300ug,吸入,每天二次\n[BBOX-253] vivo X80 · ZEISS\n[BBOX-254] 医师:杨昕发药:李琳配药:巴艺洁\n[BBOX-255] 2025/12/31 18:28金额合计:193.6/193.6\n[BBOX-256] 第1页/共1页\n[BBOX-257] 新药特药大药房总店\n[BBOX-258] 流水单号\n[BBOX-259] 10020046503\n[BBOX-260] 结账时间\n[BBOX-261] 2026-01-02 18:12:29\n[BBOX-262] 编号\n[BBOX-263] 数量\n[BBOX-264] 单价\n[BBOX-265] 金额\n[BBOX-266] 营业员\n[BBOX-267] 沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:\n[BBOX-268] 泡/葛兰素史克(集团)/库存1\n[BBOX-269] 0200127\n[BBOX-270] 1\n[BBOX-271] 盒\n[BBOX-272] 199.00\n[BBOX-273] 199.00\n[BBOX-274] 合计\n[BBOX-275] 199.00\n[BBOX-276] 优惠:0.00\n[BBOX-277] 微信:0.00\n[BBOX-278] 收银\n[BBOX-279] 1002\n[BBOX-280] 银台\n[BBOX-281] 会员\n[BBOX-282] 本次积分\n[BBOX-283] 0.00\n[BBOX-284] 累计积分\n[BBOX-285] 0.00\n[BBOX-286] 此票为开发票依据,药品为特殊、\n[BBOX-287] 商品,售出概不退还!\n[BBOX-288] 沈阳市第四人民医院\n[BBOX-289] 处方笺\n[BBOX-290] 医疗类别:市医保\n[BBOX-291] NO:26000513029\n[BBOX-292] 3号窗口\n[BBOX-293] 26/01/30 13:26\n[BBOX-294] 普通\n[BBOX-295] 科 室:呼吸与危重症一门诊\n[BBOX-296] 诊断:(J45.900x001)支气管哮喘\n[BBOX-297] Rp\n[BBOX-298] 沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙\n[BBOX-299] 【50ug:250ug/泡*60泡/(193.60元/盒) 1盒\n[BBOX-300] 用法用量:每次300ug,吸入,每天二次\n[BBOX-301] 医师:杨昕发药:李琳 配药:乔军\n[BBOX-302] 金额合计:193.6/193.6\n[BBOX-303] 第1页/共1页"
  }
]
2026-08-05 04:12:27,468 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:12:27.468+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:12:28,009 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:12:28,025 INFO     29 [SmartSplitter] SmartSplitter done: 12 chunks from 12 LLM segments (all bbox_id). Types: {'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}
2026-08-05 04:12:28,033 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 04:12:28,033 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}"}
2026-08-05 04:12:28,033 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 04:12:28,034 INFO     29 [ChunkRouter] Routed 12 chunks into 5 groups: {'chunks_Clinical': 2, 'chunks_Examination': 2, 'chunks_LabExam': 1, 'chunks_Medication': 3, 'chunks_Prescription': 4}
2026-08-05 04:12:28,041 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 04:12:28,041 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | ChunkRouter:Router | outputs={"html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks": "12 items, types={'OutpatientRecord': 2, 'ExaminationReport': 2, 'LabReport': 1, 'MedicationRecord': 3, 'PrescriptionRecord': 4}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:12:28,041 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 04:12:28,045 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:12:28,046 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[3, 4]
2026-08-05 04:12:28,046 INFO     29 [qwen-vl-table] positions ： [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:12:28,235 INFO     29 [qwen-vl-table] page=3, rect=595x843, img=(1654x2342)
2026-08-05 04:12:28,440 INFO     29 [qwen-vl-table] page=4, rect=595x843, img=(1654x2342)
2026-08-05 04:12:28,441 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:12:28,441 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 91, \"bbox_end\": 142, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{lrrrr}\n报告时间: 2025-09-02\n\\hline\n检查项目 & 结果 & 单位 & 参考值 \\\\\n\\hline\n白细胞 & 8.40 & 10^9/L & 3.5--9.5 \\\\\n红细胞 & 4.94 & 10^12/L & 3.8--5.1 \\\\\n血红蛋白 & 138 & g/L & 115--150 \\\\\n血小板 & 300 & 10^9/L & 125--350 \\\\\n红细胞压积 & 41.30 & \\% & 35--45 \\\\\n红细胞平均体积 & 83.60 & fL & 82--100 \\\\\n平均血红蛋白量 & 28.00 & pg & 27--34 \\\\\n平均血红蛋白浓 & 334 & g/L & 316--354 \\\\\n度 & & & \\\\\n中性粒细胞比率 & 54.20 & \\% & 40--75 \\\\\n淋巴细胞比率 & 36.10 & \\% & 20--50 \\\\\n单核细胞比率 & 3.70 & \\% & 3--10 \\\\\n嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 \\\\\n率 & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{cccccc}\n\\hline\n& & & & & \\\\\n红细胞 & 4.94 & 10^12/L & 3.8--5.1 & & \\\\\n血红蛋白 & 138 & g/L & 115--150 & & \\\\",
    "role": "user"
  }
]
[92m04:12:28 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:12:28,442 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:12:35,570 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:12:35,570 INFO     29 [qwen-vl-table] page=3 LLM output (len=2037):
{
  "report_date": "2025-09-02",
  "items": [
    {
      "name": "白细胞",
      "item_code": null,
      "value": "8.40",
      "unit": "10^9/L",
      "reference_range": "3.5--9.5",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": null,
      "value": "4.94",
      "unit": "10^12/L",
      "reference_range": "3.8--5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": null,
      "value": "138",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": null,
      "value": "300",
      "unit": "10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "41.30",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": null,
      "value": "83.60",
      "unit": "fL",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "28.00",
      "unit": "pg",
      "reference_range": "27--34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "334",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": null,
      "value": "54.20",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": null,
      "value": "36.10",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": null,
      "value": "3.70",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": null,
      "value": "5.50",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    }
  ]
}
2026-08-05 04:12:35,571 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:12:35,571 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 91, \"bbox_end\": 142, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "血小板 & 300 & 10^9/L & 125--350 & & \\\\\n红细胞压积 & 41.30 & \\% & 35--45 & & \\\\\n红细胞平均体积 & 83.60 & fL & 82--100 & & \\\\\n平均血红蛋白量 & 28.00 & pg & 27--34 & & \\\\\n平均血红蛋白浓 & 334 & g/L & 316--354 & & \\\\\n度 & & & & & \\\\\n中性粒细胞比率 & 54.20 & \\% & 40--75 & & \\\\\n淋巴细胞比率 & 36.10 & \\% & 20--50 & & \\\\\n单核细胞比率 & 3.70 & \\% & 3--10 & & \\\\\n嗜酸性粒细胞比 & 5.50 & \\% & 0.4--8.0 & & \\\\\n率 & & & & & \\\\\n嗜碱性粒细胞比 & 0.50 & \\% & 0--1 & & \\\\\n率 & & & & & \\\\\n中性粒细胞数 & 4.56 & 10^9/L & 1.8--6.3 & & \\\\\n淋巴细胞数 & 3.03 & 10^9/L & 1.1--3.2 & & \\\\\n单核细胞数 & 0.31 & 10^9/L & 0.10--0.60 & & \\\\\n嗜酸性粒细胞 & 0.46 & 10^9/L & 0.02--0.52 & & \\\\\n嗜碱性粒细胞 & 0.04 & 10^9/L & 0--0.06 & & \\\\\n红细胞分布宽度 & 12.9 & \\% & 11.0--16.0 & & \\\\\n变异系数 & & & & & \\\\\n血小板分布宽度 & 16.5 & fL & 8.0--18.1 & & \\\\\n平均血小板体积 & 10.2 & fL & 9--13 & & \\\\\n血小板压积 & 0.31 & \\% & 0.10--0.28 & & \\\\\nC反应蛋白 & 7.92 & mg/L & 0--6 & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
[92m04:12:35 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:12:35,572 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:12:50,489 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:12:50,489 INFO     29 [qwen-vl-table] page=4 LLM output (len=3383):
{
  "report_date": "2025-09-02",
  "items": [
    {
      "name": "血小板",
      "item_code": null,
      "value": "300",
      "unit": "10^9/L",
      "reference_range": "125--350",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": null,
      "value": "41.30",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "红细胞平均体积",
      "item_code": null,
      "value": "83.60",
      "unit": "fL",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白量",
      "item_code": null,
      "value": "28.00",
      "unit": "pg",
      "reference_range": "27--34",
      "abnormal": false
    },
    {
      "name": "平均血红蛋白浓度",
      "item_code": null,
      "value": "334",
      "unit": "g/L",
      "reference_range": "316--354",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": null,
      "value": "54.20",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": null,
      "value": "36.10",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": null,
      "value": "3.70",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": null,
      "value": "5.50",
      "unit": "%",
      "reference_range": "0.4--8.0",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞比率",
      "item_code": null,
      "value": "0.50",
      "unit": "%",
      "reference_range": "0--1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞数",
      "item_code": null,
      "value": "4.56",
      "unit": "10^9/L",
      "reference_range": "1.8--6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞数",
      "item_code": null,
      "value": "3.03",
      "unit": "10^9/L",
      "reference_range": "1.1--3.2",
      "abnormal": false
    },
    {
      "name": "单核细胞数",
      "item_code": null,
      "value": "0.31",
      "unit": "10^9/L",
      "reference_range": "0.10--0.60",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞",
      "item_code": null,
      "value": "0.46",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞",
      "item_code": null,
      "value": "0.04",
      "unit": "10^9/L",
      "reference_range": "0--0.06",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度变异系数",
      "item_code": null,
      "value": "12.9",
      "unit": "%",
      "reference_range": "11.0--16.0",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": null,
      "value": "16.5",
      "unit": "fL",
      "reference_range": "8.0--18.1",
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": null,
      "value": "10.2",
      "unit": "fL",
      "reference_range": "9--13",
      "abnormal": false
    },
    {
      "name": "血小板压积",
      "item_code": null,
      "value": "0.31",
      "unit": "%",
      "reference_range": "0.10--0.28",
      "abnormal": true
    },
    {
      "name": "C反应蛋白",
      "item_code": null,
      "value": "7.92",
      "unit": "mg/L",
      "reference_range": "0--6",
      "abnormal": true
    }
  ]
}
2026-08-05 04:12:50,490 INFO     29 [qwen-vl-table] coord grouping: {3: 24, 4: 8}
2026-08-05 04:12:50,491 INFO     29 [qwen-vl-table] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=706909, prompt_len=679
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、红细胞、血红蛋白、血小板、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、中性粒细胞比率、淋巴细胞比率、单核细胞比率、嗜酸性粒细胞比率、血小板、红细胞压积、红细胞平均体积、平均血红蛋白量、平均血红蛋白浓度、中性粒细胞比率、淋巴细胞比率、单核细胞比率、嗜酸性粒细胞比率、嗜碱性粒细胞比率、嗜酸性粒细胞、红细胞分布宽度变异系数

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
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord API raw response (len=1231):
[
	{"text": "白细胞", "bbox": [199, 457, 281, 479]},
	{"text": "红细胞", "bbox": [199, 497, 281, 518]},
	{"text": "血红蛋白", "bbox": [199, 536, 307, 558]},
	{"text": "血小板", "bbox": [199, 576, 281, 598]},
	{"text": "红细胞压积", "bbox": [199, 616, 337, 638]},
	{"text": "红细胞平均体积", "bbox": [199, 656, 391, 678]},
	{"text": "平均血红蛋白量", "bbox": [199, 695, 391, 717]},
	{"text": "平均血红蛋白浓度", "bbox": [199, 735, 391, 757]},
	{"text": "中性粒细胞比率", "bbox": [199, 805, 391, 827]},
	{"text": "淋巴细胞比率", "bbox": [199, 845, 364, 867]},
	{"text": "单核细胞比率", "bbox": [199, 884, 364, 906]},
	{"text": "嗜酸性粒细胞比率", "bbox": [199, 924, 391, 946]},
	{"text": "血小板", "bbox": [199, 576, 281, 598]},
	{"text": "红细胞压积", "bbox": [199, 616, 337, 638]},
	{"text": "红细胞平均体积", "bbox": [199, 656, 391, 678]},
	{"text": "平均血红蛋白量", "bbox": [199, 695, 391, 717]},
	{"text": "平均血红蛋白浓度", "bbox": [199, 735, 391, 757]},
	{"text": "中性粒细胞比率", "bbox": [199, 805, 391, 827]},
	{"text": "淋巴细胞比率", "bbox": [199, 845, 364, 867]},
	{"text": "单核细胞比率", "bbox": [199, 884, 364, 906]},
	{"text": "嗜酸性粒细胞比率", "bbox": [199, 924, 391, 946]},
	{"text": "嗜碱性粒细胞比率", "bbox": [199, 964, 391, 986]},
	{"text": "嗜酸性粒细胞", "bbox": [199, 964, 391, 986]},
	{"text": "红细胞分布宽度变异系数", "bbox": [199, 964, 391, 986]}
]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord API: raw_items=24, valid_items=24, elapsed=8.0s
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[199, 457, 281, 479]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[1]: text=红细胞, bbox=[199, 497, 281, 518]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[2]: text=血红蛋白, bbox=[199, 536, 307, 558]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[3]: text=血小板, bbox=[199, 576, 281, 598]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[4]: text=红细胞压积, bbox=[199, 616, 337, 638]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[5]: text=红细胞平均体积, bbox=[199, 656, 391, 678]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[6]: text=平均血红蛋白量, bbox=[199, 695, 391, 717]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[7]: text=平均血红蛋白浓度, bbox=[199, 735, 391, 757]
2026-08-05 04:12:58,454 INFO     29 [qwen-vl-table] coord item[8]: text=中性粒细胞比率, bbox=[199, 805, 391, 827]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[9]: text=淋巴细胞比率, bbox=[199, 845, 364, 867]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[10]: text=单核细胞比率, bbox=[199, 884, 364, 906]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[11]: text=嗜酸性粒细胞比率, bbox=[199, 924, 391, 946]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[12]: text=血小板, bbox=[199, 576, 281, 598]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[199, 616, 337, 638]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞平均体积, bbox=[199, 656, 391, 678]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[15]: text=平均血红蛋白量, bbox=[199, 695, 391, 717]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[16]: text=平均血红蛋白浓度, bbox=[199, 735, 391, 757]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[17]: text=中性粒细胞比率, bbox=[199, 805, 391, 827]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[18]: text=淋巴细胞比率, bbox=[199, 845, 364, 867]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[19]: text=单核细胞比率, bbox=[199, 884, 364, 906]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[20]: text=嗜酸性粒细胞比率, bbox=[199, 924, 391, 946]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[21]: text=嗜碱性粒细胞比率, bbox=[199, 964, 391, 986]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[22]: text=嗜酸性粒细胞, bbox=[199, 964, 391, 986]
2026-08-05 04:12:58,455 INFO     29 [qwen-vl-table] coord item[23]: text=红细胞分布宽度变异系数, bbox=[199, 964, 391, 986]
2026-08-05 04:12:58,456 INFO     29 [qwen-vl-table] page=3 coord: matched 24/24, time=8.0s
2026-08-05 04:12:58,458 INFO     29 [qwen-vl-table] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=922700, prompt_len=560
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
中性粒细胞数、淋巴细胞数、单核细胞数、嗜碱性粒细胞、血小板分布宽度、平均血小板体积、血小板压积、C反应蛋白

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
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord API raw response (len=408):
[
	{"text": "中性粒细胞数", "bbox": [198, 583, 363, 605]},
	{"text": "淋巴细胞数", "bbox": [198, 623, 336, 645]},
	{"text": "单核细胞数", "bbox": [198, 663, 336, 685]},
	{"text": "嗜碱性粒细胞", "bbox": [198, 742, 363, 764]},
	{"text": "血小板分布宽度", "bbox": [198, 851, 391, 873]},
	{"text": "平均血小板体积", "bbox": [198, 890, 391, 912]},
	{"text": "血小板压积", "bbox": [198, 930, 336, 952]},
	{"text": "C反应蛋白", "bbox": [198, 970, 324, 992]}
]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord API: raw_items=8, valid_items=8, elapsed=3.5s
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[0]: text=中性粒细胞数, bbox=[198, 583, 363, 605]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[1]: text=淋巴细胞数, bbox=[198, 623, 336, 645]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[2]: text=单核细胞数, bbox=[198, 663, 336, 685]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[3]: text=嗜碱性粒细胞, bbox=[198, 742, 363, 764]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[4]: text=血小板分布宽度, bbox=[198, 851, 391, 873]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[5]: text=平均血小板体积, bbox=[198, 890, 391, 912]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[6]: text=血小板压积, bbox=[198, 930, 336, 952]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] coord item[7]: text=C反应蛋白, bbox=[198, 970, 324, 992]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] page=4 coord: matched 8/8, time=3.5s
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] new_positions (32):
[[4, 118.46072583007812, 167.27368823242188, 385.2647233886719, 403.8113840332031], [4, 118.46072583007812, 167.27368823242188, 418.9859245605469, 436.68955517578127], [4, 118.46072583007812, 182.7509689941406, 451.864095703125, 470.4107563476562], [4, 118.46072583007812, 167.27368823242188, 485.585296875, 504.1319575195312], [4, 118.46072583007812, 200.60936987304686, 519.3064980468749, 537.8531586914063], [4, 118.46072583007812, 232.7544914550781, 553.02769921875, 571.5743598632812], [4, 118.46072583007812, 232.7544914550781, 585.9058703613281, 604.4525310058593], [4, 118.46072583007812, 232.7544914550781, 619.6270715332031, 638.1737321777343], [4, 118.46072583007812, 232.7544914550781, 678.6391735839844, 697.1858342285157], [4, 118.46072583007812, 216.6819306640625, 712.3603747558593, 730.9070354003906], [4, 118.46072583007812, 216.6819306640625, 745.2385458984375, 763.7852065429687], [4, 118.46072583007812, 232.7544914550781, 778.9597470703125, 797.5064077148437], [4, 118.46072583007812, 167.27368823242188, 485.585296875, 504.1319575195312], [4, 118.46072583007812, 200.60936987304686, 519.3064980468749, 537.8531586914063], [4, 118.46072583007812, 232.7544914550781, 553.02769921875, 571.5743598632812], [4, 118.46072583007812, 232.7544914550781, 585.9058703613281, 604.4525310058593], [4, 118.46072583007812, 232.7544914550781, 619.6270715332031, 638.1737321777343], [4, 118.46072583007812, 232.7544914550781, 678.6391735839844, 697.1858342285157], [4, 118.46072583007812, 216.6819306640625, 712.3603747558593, 730.9070354003906], [4, 118.46072583007812, 216.6819306640625, 745.2385458984375, 763.7852065429687], [4, 118.46072583007812, 232.7544914550781, 778.9597470703125, 797.5064077148437], [4, 118.46072583007812, 232.7544914550781, 812.6809482421875, 831.2276088867187], [4, 118.46072583007812, 232.7544914550781, 812.6809482421875, 831.2276088867187], [4, 118.46072583007812, 232.7544914550781, 812.6809482421875, 831.2276088867187], [5, 117.86544580078125, 216.08665063476562, 491.4865070800781, 510.03316772460937], [5, 117.86544580078125, 200.01408984374999, 525.2077082519531, 543.7543688964844], [5, 117.86544580078125, 200.01408984374999, 558.9289094238281, 577.4755700683594], [5, 117.86544580078125, 216.08665063476562, 625.5282817382813, 644.0749423828125], [5, 117.86544580078125, 232.7544914550781, 717.4185549316406, 735.9652155761719], [5, 117.86544580078125, 232.7544914550781, 750.2967260742188, 768.84338671875], [5, 117.86544580078125, 200.01408984374999, 784.0179272460938, 802.564587890625], [5, 117.86544580078125, 192.87072949218748, 817.7391284179687, 836.2857890624999]]
2026-08-05 04:13:01,960 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=32, matched=32, pages=2, time=33.9s
2026-08-05 04:13:01,972 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 04:13:01,972 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:13:01,972 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 04:13:01,972 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:13:01.972+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:13:01,978 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:01,978 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:13:01 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:01,979 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:03,161 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:03,169 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 04:13:03,169 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:13:03,169 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 04:13:03,174 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:13:03,174 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:13:03,174 INFO     29 [qwen-vl-text] positions(28): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:13:03,174 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [28]
2026-08-05 04:13:03,438 INFO     29 [qwen-vl-text] page=0, rect=595x1290, img=(1654x3583), dpi=200
2026-08-05 04:13:03,439 INFO     29 [qwen-vl-text] LLM extraction start, text_len=341
2026-08-05 04:13:03,439 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:03,440 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 27, \"encounter_dates\": [\"2024-08-23\"], \"department\": \"呼吸与危重症医学科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "2/4\n沈阳市第四人民医院\nTHE FOURTH PEOPLE'S HOSPITAL OF SHENYANG\n门诊病历\n业：现住址：辽宁省沈阳市皇姑区延河街\n就诊科别：呼吸与危重症医学科门诊\n就诊时间：2024-08-23 16:00\n书写时间：2024-08-23 16:59\n供史者：患者本人\n主诉：支气管哮喘开药\n现病史：患者支气管哮喘，继续巩固治疗：\n沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒\n孟鲁司特钠片\n10mg*5片，共10片\n每次10mg，QD\n睡前口服\n查体/专科查体：\n辅助检查：\n诊断：\n支气管哮喘\n处理意见：\n建议患者定期复查肺功能，肺部CT.\n我科随诊。\n建议休息天数：0天。\n患者下转：\n签名：杨昕\n患者签名：\n门诊病历专用章",
    "role": "user"
  }
]
[92m04:13:03 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:03,441 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:05,885 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:05,885 INFO     29 [qwen-vl-text] LLM output (len=369):
{
  "encounter_date": "2024-08-23",
  "chief_complaint": "支气管哮喘开药",
  "present_illness": "患者支气管哮喘，继续巩固治疗：沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒；孟鲁司特钠片10mg*5片，共10片，每次10mg，QD，睡前口服",
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒",
    "孟鲁司特钠片10mg*5片，共10片，每次10mg，QD，睡前口服",
    "建议患者定期复查肺功能，肺部CT",
    "我科随诊"
  ]
}
2026-08-05 04:13:05,885 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-08-23]
2026-08-05 04:13:05,888 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1369676, prompt_len=1038
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["2/4", "沈阳市第四人民医院", "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "门诊病历", "业：现住址：辽宁省沈阳市皇姑区延河街", "就诊科别：呼吸与危重症医学科门诊", "就诊时间：2024-08-23 16:00", "书写时间：2024-08-23 16:59", "供史者：患者本人", "主诉：支气管哮喘开药", "现病史：患者支气管哮喘，继续巩固治疗：", "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "孟鲁司特钠片", "10mg*5片，共10片", "每次10mg，QD", "睡前口服", "查体/专科查体：", "辅助检查：", "诊断：", "支气管哮喘", "处理意见：", "建议患者定期复查肺功能，肺部CT.", "我科随诊。", "建议休息天数：0天。", "患者下转：", "签名：杨昕", "患者签名：", "门诊病历专用章"]

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
2026-08-05 04:13:18,214 INFO     29 [qwen-vl-text] coord API raw response (len=1621):
[
	{"text": "2/4", "bbox": [78, 118, 138, 135]},
	{"text": "沈阳市第四人民医院", "bbox": [395, 183, 708, 202]},
	{"text": "THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG", "bbox": [395, 202, 708, 209]},
	{"text": "门诊病历", "bbox": [454, 212, 595, 230]},
	{"text": "业：现住址：辽宁省沈阳市皇姑区延河街", "bbox": [538, 237, 842, 247]},
	{"text": "就诊科别：呼吸与危重症医学科门诊", "bbox": [157, 281, 430, 291]},
	{"text": "就诊时间：2024-08-23 16:00", "bbox": [157, 295, 379, 304],
	"text": "书写时间：2024-08-23 16:59", "bbox": [157, 308, 379, 317]},
	{"text": "供史者：患者本人", "bbox": [157, 321, 288, 330]},
	{"text": "主诉：支气管哮喘开药", "bbox": [157, 339, 333, 349]},
	{"text": "现病史：患者支气管哮喘，继续巩固治疗：", "bbox": [157, 366, 480, 376]},
	{"text": "沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒", "bbox": [157, 388, 614, 398]},
	{"text": "孟鲁司特钠片", "bbox": [157, 399, 260, 408]},
	{"text": "10mg*5片，共10片", "bbox": [315, 400, 446, 409]},
	{"text": "每次10mg，QD", "bbox": [552, 400, 650, 409]},
	{"text": "睡前口服", "bbox": [725, 400, 794, 409]},
	{"text": "查体/专科查体：", "bbox": [157, 427, 277, 437]},
	{"text": "辅助检查：", "bbox": [157, 467, 234, 476]},
	{"text": "诊断：", "bbox": [157, 517, 197, 526]},
	{"text": "支气管哮喘", "bbox": [157, 528, 243, 537]},
	{"text": "处理意见：", "bbox": [157, 557, 234, 566]},
	{"text": "建议患者定期复查肺功能，肺部CT.", "bbox": [157, 568, 427, 577]},
	{"text": "我科随诊。", "bbox": [157, 579, 234, 588]},
	{"text": "建议休息天数：0天。", "bbox": [157, 590, 321, 600]},
	{"text": "患者下转：", "bbox": [157, 602, 234, 611]},
	{"text": "签名：杨昕", "bbox": [517, 628, 643, 650]},
	{"text": "患者签名：", "bbox": [164, 641, 241, 651]},
	{"text": "门诊病历专用章", "bbox": [669, 785, 778, 799]},
	{"text": "(1)", "bbox": [708, 800, 740, 810]}
]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=12.3s
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[0]: text=2/4, bbox=[78, 118, 138, 135]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[1]: text=沈阳市第四人民医院, bbox=[395, 183, 708, 202]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[2]: text=THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG, bbox=[395, 202, 708, 209]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[3]: text=门诊病历, bbox=[454, 212, 595, 230]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[4]: text=业：现住址：辽宁省沈阳市皇姑区延河街, bbox=[538, 237, 842, 247]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[5]: text=就诊科别：呼吸与危重症医学科门诊, bbox=[157, 281, 430, 291]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[6]: text=书写时间：2024-08-23 16:59, bbox=[157, 308, 379, 317]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[7]: text=供史者：患者本人, bbox=[157, 321, 288, 330]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[8]: text=主诉：支气管哮喘开药, bbox=[157, 339, 333, 349]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[9]: text=现病史：患者支气管哮喘，继续巩固治疗：, bbox=[157, 366, 480, 376]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒, bbox=[157, 388, 614, 398]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[11]: text=孟鲁司特钠片, bbox=[157, 399, 260, 408]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[12]: text=10mg*5片，共10片, bbox=[315, 400, 446, 409]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[13]: text=每次10mg，QD, bbox=[552, 400, 650, 409]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[14]: text=睡前口服, bbox=[725, 400, 794, 409]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[15]: text=查体/专科查体：, bbox=[157, 427, 277, 437]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：, bbox=[157, 467, 234, 476]
2026-08-05 04:13:18,215 INFO     29 [qwen-vl-text] coord item[17]: text=诊断：, bbox=[157, 517, 197, 526]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[18]: text=支气管哮喘, bbox=[157, 528, 243, 537]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[19]: text=处理意见：, bbox=[157, 557, 234, 566]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[20]: text=建议患者定期复查肺功能，肺部CT., bbox=[157, 568, 427, 577]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[21]: text=我科随诊。, bbox=[157, 579, 234, 588]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[22]: text=建议休息天数：0天。, bbox=[157, 590, 321, 600]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[23]: text=患者下转：, bbox=[157, 602, 234, 611]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[24]: text=签名：杨昕, bbox=[517, 628, 643, 650]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[25]: text=患者签名：, bbox=[164, 641, 241, 651]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[26]: text=门诊病历专用章, bbox=[669, 785, 778, 799]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] coord item[27]: text=(1), bbox=[708, 800, 740, 810]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] page=0 — 28/28 coords, api_time=12.3s
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] new_positions (28):
[[0, 46.43184228515625, 82.14864404296874, 152.19168115234376, 174.11760131835936], [0, 235.13561157226562, 421.45826074218746, 236.02608178710938, 260.53152197265626], [0, 235.13561157226562, 421.45826074218746, 260.53152197265626, 269.5598420410156], [0, 270.2571333007812, 354.1916174316406, 273.4291220703125, 296.6448022460938], [0, 320.26065576171874, 501.2257846679687, 305.6731223144531, 318.5707224121094], [0, 93.45896459960937, 255.97041259765624, 362.42256274414063, 375.3201628417969], [0, 93.45896459960937, 225.61113110351562, 397.2460830078125, 408.8539230957031], [0, 93.45896459960937, 171.4406484375, 414.01296313476564, 425.62080322265626], [0, 93.45896459960937, 198.22824975585937, 437.2286433105469, 450.1262434082031], [0, 93.45896459960937, 285.7344140625, 472.05216357421875, 484.949763671875], [0, 93.45896459960937, 365.5019379882812, 500.4268837890625, 513.3244838867188], [0, 93.45896459960937, 154.77280761718748, 514.6142438964844, 526.222083984375], [0, 187.51320922851562, 265.49489306640623, 515.90400390625, 527.5118439941406], [0, 328.59457617187496, 386.9320190429687, 515.90400390625, 527.5118439941406], [0, 431.57802124023436, 472.6523432617187, 515.90400390625, 527.5118439941406], [0, 93.45896459960937, 164.89256811523435, 550.7275241699218, 563.6251242675781], [0, 93.45896459960937, 139.29552685546875, 602.3179245605469, 613.9257646484375], [0, 93.45896459960937, 117.27016577148437, 666.8059250488282, 678.4137651367188], [0, 93.45896459960937, 144.6530471191406, 680.99328515625, 692.6011252441406], [0, 93.45896459960937, 139.29552685546875, 718.3963254394531, 730.0041655273437], [0, 93.45896459960937, 254.18457250976562, 732.583685546875, 744.1915256347656], [0, 93.45896459960937, 139.29552685546875, 746.7710456542969, 758.3788857421875], [0, 93.45896459960937, 191.08488940429686, 760.9584057617187, 773.856005859375], [0, 93.45896459960937, 139.29552685546875, 776.4355258789062, 788.0433659667968], [0, 307.75977514648434, 382.7650588378906, 809.9692861328125, 838.3440063476562], [0, 97.62592480468749, 143.46248706054686, 826.7361662597656, 839.6337663574219], [0, 398.24233959960935, 463.1278627929687, 1012.4616076660157, 1030.5182478027343], [0, 421.45826074218746, 440.50722167968746, 1031.8080078125, 1044.7056079101562]]
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=15.0s
2026-08-05 04:13:18,216 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:13:18,216 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 04:13:18,217 INFO     29 [qwen-vl-text] positions(23): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:13:18,217 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [23]
2026-08-05 04:13:18,690 INFO     29 [qwen-vl-text] page=5, rect=595x1010, img=(1654x2805), dpi=200
2026-08-05 04:13:18,691 INFO     29 [qwen-vl-text] LLM extraction start, text_len=382
2026-08-05 04:13:18,692 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:18,692 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 143, \"bbox_end\": 165, \"encounter_dates\": [\"2025-11-08\"], \"department\": \"呼吸内一科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "辽宁崇文厚德医院\n门诊病历\n科室：呼吸内一科门诊\n姓名：\n职业：\n就诊日期：2025/11/08 10:11:23\n主诉：反复喘息2年，加重1周\n现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万\n林”治疗，症状稍有改善，为求进一步诊治来我院就诊。\n既往史：否认。\n过敏史：{无}\n体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。\n辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试\n性。\n抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.\n初步诊断：1、支气管哮喘 急性发作期\n处理：\n1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。\n2.1周后复诊，病情变化随诊。\n医生签名：王春\n王春\n白\n第 1 页",
    "role": "user"
  }
]
[92m04:13:18 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:18,694 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:21,191 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:21,192 INFO     29 [qwen-vl-text] LLM output (len=300):
{
  "encounter_date": "2025-11-08",
  "chief_complaint": "反复喘息2年，加重1周",
  "present_illness": "3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万林”治疗，症状稍有改善，为求进一步诊治来我院就诊。",
  "past_history": "否认。过敏史：无",
  "diagnosis": "支气管哮喘 急性发作期",
  "treatment_plan": "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。2.1周后复诊，病情变化随诊。"
}
2026-08-05 04:13:21,192 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-08]
2026-08-05 04:13:21,199 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2857232, prompt_len=1064
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["辽宁崇文厚德医院", "门诊病历", "科室：呼吸内一科门诊", "姓名：", "职业：", "就诊日期：2025/11/08 10:11:23", "主诉：反复喘息2年，加重1周", "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "既往史：否认。", "过敏史：{无}", "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "性。", "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "初步诊断：1、支气管哮喘 急性发作期", "处理：", "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "2.1周后复诊，病情变化随诊。", "医生签名：王春", "王春", "白", "第 1 页"]

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
2026-08-05 04:13:30,897 INFO     29 [qwen-vl-text] coord API raw response (len=1365):
[
	{"text": "辽宁崇文厚德医院", "bbox": [357, 39, 667, 63]},
	{"text": "门诊病历", "bbox": [437, 72, 588, 95]},
	{"text": "科室：呼吸内一科门诊", "bbox": [36, 105, 280, 120]},
	{"text": "姓名：", "bbox": [31, 161, 89, 176]},
	{"text": "职业：", "bbox": [29, 187, 87, 202]},
	{"text": "就诊日期：2025/11/08 10:11:23", "bbox": [28, 214, 390, 230]},
	{"text": "主诉：反复喘息2年，加重1周", "bbox": [26, 243, 350, 259]},
	{"text": "现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万", "bbox": [23, 270, 997, 288]},
	{"text": "林”治疗，症状稍有改善，为求进一步诊治来我院就诊。", "bbox": [7, 300, 630, 317]},
	{"text": "既往史：否认。", "bbox": [18, 334, 178, 350]},
	{"text": "过敏史：{无}", "bbox": [14, 365, 160, 381]},
	{"text": "体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。", "bbox": [12, 393, 955, 411]},
	{"text": "辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试", "bbox": [9, 422, 995, 440]},
	{"text": "性。", "bbox": [7, 455, 44, 471]},
	{"text": "抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.", "bbox": [7, 489, 620, 505]},
	{"text": "初步诊断：1、支气管哮喘 急性发作期", "bbox": [29, 518, 462, 535]},
	{"text": "处理：", "bbox": [4, 548, 65, 564]},
	{"text": "1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。", "bbox": [4, 575, 980, 592]},
	{"text": "2.1周后复诊，病情变化随诊。", "bbox": [4, 605, 311, 621]},
	{"text": "医生签名：王春", "bbox": [535, 724, 719, 740]},
	{"text": "王春", "bbox": [778, 670, 927, 727]},
	{"text": "白", "bbox": [880, 713, 905, 737]},
	{"text": "第 1 页", "bbox": [429, 930, 580, 945]}
]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.7s
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[0]: text=辽宁崇文厚德医院, bbox=[357, 39, 667, 63]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[1]: text=门诊病历, bbox=[437, 72, 588, 95]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[2]: text=科室：呼吸内一科门诊, bbox=[36, 105, 280, 120]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[31, 161, 89, 176]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[4]: text=职业：, bbox=[29, 187, 87, 202]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[5]: text=就诊日期：2025/11/08 10:11:23, bbox=[28, 214, 390, 230]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[6]: text=主诉：反复喘息2年，加重1周, bbox=[26, 243, 350, 259]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[7]: text=现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万, bbox=[23, 270, 997, 288]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[8]: text=林”治疗，症状稍有改善，为求进一步诊治来我院就诊。, bbox=[7, 300, 630, 317]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[9]: text=既往史：否认。, bbox=[18, 334, 178, 350]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[10]: text=过敏史：{无}, bbox=[14, 365, 160, 381]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[11]: text=体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。, bbox=[12, 393, 955, 411]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[12]: text=辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试, bbox=[9, 422, 995, 440]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[13]: text=性。, bbox=[7, 455, 44, 471]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[14]: text=抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%., bbox=[7, 489, 620, 505]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断：1、支气管哮喘 急性发作期, bbox=[29, 518, 462, 535]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[16]: text=处理：, bbox=[4, 548, 65, 564]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[17]: text=1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。, bbox=[4, 575, 980, 592]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[18]: text=2.1周后复诊，病情变化随诊。, bbox=[4, 605, 311, 621]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[19]: text=医生签名：王春, bbox=[535, 724, 719, 740]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[20]: text=王春, bbox=[778, 670, 927, 727]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[21]: text=白, bbox=[880, 713, 905, 737]
2026-08-05 04:13:30,898 INFO     29 [qwen-vl-text] coord item[22]: text=第 1 页, bbox=[429, 930, 580, 945]
2026-08-05 04:13:30,899 INFO     29 [qwen-vl-text] page=5 — 23/23 coords, api_time=9.7s
2026-08-05 04:13:30,899 INFO     29 [qwen-vl-text] new_positions (23):
[[5, 212.51497045898435, 397.0517795410156, 39.38142114257813, 63.616141845703126], [5, 260.1373728027344, 350.02465722656245, 72.704162109375, 95.92910278320313], [5, 21.4300810546875, 166.678408203125, 106.02690307617188, 121.173603515625], [5, 18.453680908203125, 52.97992260742187, 162.5745847167969, 177.72128515625002], [5, 17.263120849609372, 51.78936254882812, 188.82886547851564, 203.97556591796877], [5, 16.6678408203125, 232.15921142578122, 216.09292626953126, 232.24940673828127], [5, 15.477280761718749, 208.34801025390624, 245.37654711914064, 261.5330275878906], [5, 13.691440673828124, 593.4941892089844, 272.6406079101563, 290.8166484375], [5, 4.166960205078125, 375.02641845703124, 302.9340087890625, 320.10026928710937], [5, 10.71504052734375, 105.95984521484374, 337.26652978515625, 353.4230102539063], [5, 8.33392041015625, 95.2448046875, 368.5697106933594, 384.7261911621094], [5, 7.1433603515624995, 568.4924279785156, 396.8435515136719, 415.01959204101564], [5, 5.357520263671875, 592.3036291503906, 426.12717236328126, 444.30321289062505], [5, 4.166960205078125, 26.192321289062498, 459.4499133300782, 475.60639379882815], [5, 4.166960205078125, 369.07361816406245, 493.7824343261719, 509.9389147949219], [5, 17.263120849609372, 275.0193735351562, 523.0660551757812, 540.2323156738281], [5, 2.3811201171875, 38.69320190429687, 553.3594560546875, 569.5159365234375], [5, 2.3811201171875, 583.3744287109374, 580.6235168457032, 597.7897773437501], [5, 2.3811201171875, 185.1320891113281, 610.9169177246094, 627.0733981933594], [5, 318.4748156738281, 428.00634106445307, 731.0807412109375, 747.2372216796875], [5, 463.1278627929687, 551.824587158203, 676.5526196289063, 734.1100812988282], [5, 523.84642578125, 538.7284265136718, 719.9731608886719, 744.2078815917969], [5, 255.37513256835936, 345.26241699218747, 939.0954272460938, 954.242127685547]]
2026-08-05 04:13:30,899 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=12.7s
2026-08-05 04:13:30,904 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 04:13:30,904 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:13:30,904 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 04:13:30,908 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:13:30,908 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 04:13:30,908 INFO     29 [qwen-vl-text] positions(16): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:13:30,908 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [16]
2026-08-05 04:13:31,242 INFO     29 [qwen-vl-text] page=6, rect=544x842, img=(1511x2339), dpi=200
2026-08-05 04:13:31,242 INFO     29 [qwen-vl-text] LLM extraction start, text_len=214
2026-08-05 04:13:31,242 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:31,242 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 166, \"bbox_end\": 181, \"encounter_dates\": [\"2025-11-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "新药特药大药房总店\n流水单号 10020045213\n结账时间 2025-11-08 15:22:19\n编号 数量 单价 金额 营业员\n甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It\nSr1/库存2\n0310145 2 盒 34.00 68.00\n合计 68.00\n优惠：0.00 微信：0.00\n收银 1002\n银台\n会员\n本次积分 0.00\n累计积分 0.00\n此票为开发票依据，药品为特殊、\n商品，售出概不退还！",
    "role": "user"
  }
]
[92m04:13:31 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:31,244 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:35,854 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:13:35.852+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:13:36,751 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:36,752 INFO     29 [qwen-vl-text] LLM output (len=422):
{
  "encounter_date": "2025-11-08",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "甲泼尼龙片（美卓乐）",
      "specification": "4mg*30片",
      "dosage": null,
      "quantity": 2,
      "unit_price": 34.00,
      "total_price": 68.00,
      "frequency": null,
      "route": null,
      "manufacturer": "Pfizer It",
      "approval_number": null
    }
  ],
  "payment_total": 68.00,
  "payment_method": null
}
2026-08-05 04:13:36,752 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-08]
2026-08-05 04:13:36,757 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3269868, prompt_len=875
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["新药特药大药房总店", "流水单号 10020045213", "结账时间 2025-11-08 15:22:19", "编号 数量 单价 金额 营业员", "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "Sr1/库存2", "0310145 2 盒 34.00 68.00", "合计 68.00", "优惠：0.00 微信：0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据，药品为特殊、", "商品，售出概不退还！"]

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
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord API raw response (len=903):
[
	{"text": "新药特药大药房总店", "bbox": [153, 134, 722, 178]},
	{"text": "流水单号 10020045213", "bbox": [15, 193, 719, 226]},
	{"text": "结账时间 2025-11-08 15:22:19", "bbox": [14, 245, 719, 280]},
	{"text": "编号 数量 单价 金额 营业员", "bbox": [11, 297, 860, 339]},
	{"text": "甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It", "bbox": [14, 350, 995, 392]},
	{"text": "Sr1/库存2", "bbox": [7, 405, 243, 439]},
	{"text": "0310145 2 盒 34.00 68.00", "bbox": [7, 460, 909, 496]},
	{"text": "合计 68.00", "bbox": [10, 511, 280, 544]},
	{"text": "优惠：0.00 微信：0.00", "bbox": [10, 566, 660, 600]},
	{"text": "收银 1002", "bbox": [7, 617, 255, 650]},
	{"text": "银台", "bbox": [7, 670, 100, 701]},
	{"text": "会员", "bbox": [7, 723, 100, 754]},
	{"text": "本次积分 0.00", "bbox": [10, 775, 351, 807]},
	{"text": "累计积分 0.00", "bbox": [14, 827, 467, 858]},
	{"text": "此票为开发票依据，药品为特殊、", "bbox": [210, 874, 870, 905]},
	{"text": "商品，售出概不退还！", "bbox": [353, 920, 776, 950]}
]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=6.7s
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[153, 134, 722, 178]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号 10020045213, bbox=[15, 193, 719, 226]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[2]: text=结账时间 2025-11-08 15:22:19, bbox=[14, 245, 719, 280]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[3]: text=编号 数量 单价 金额 营业员, bbox=[11, 297, 860, 339]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[4]: text=甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It, bbox=[14, 350, 995, 392]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[5]: text=Sr1/库存2, bbox=[7, 405, 243, 439]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[6]: text=0310145 2 盒 34.00 68.00, bbox=[7, 460, 909, 496]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[7]: text=合计 68.00, bbox=[10, 511, 280, 544]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[8]: text=优惠：0.00 微信：0.00, bbox=[10, 566, 660, 600]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[9]: text=收银 1002, bbox=[7, 617, 255, 650]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[10]: text=银台, bbox=[7, 670, 100, 701]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[11]: text=会员, bbox=[7, 723, 100, 754]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分 0.00, bbox=[10, 775, 351, 807]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[13]: text=累计积分 0.00, bbox=[14, 827, 467, 858]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[14]: text=此票为开发票依据，药品为特殊、, bbox=[210, 874, 870, 905]
2026-08-05 04:13:43,445 INFO     29 [qwen-vl-text] coord item[15]: text=商品，售出概不退还！, bbox=[353, 920, 776, 950]
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] page=6 — 16/16 coords, api_time=6.7s
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] new_positions (16):
[[6, 83.21057775878907, 392.66690942382814, 112.81326196289062, 149.85642260742188], [6, 8.157899780273437, 391.03532946777347, 162.48477282714845, 190.26714331054689], [6, 7.614039794921876, 391.03532946777347, 206.2630535888672, 235.7292041015625], [6, 5.982459838867188, 467.7195874023438, 250.04133435058594, 285.4007149658203], [6, 7.614039794921876, 541.1406854248047, 294.6615051269531, 330.0208857421875], [6, 3.807019897460938, 132.1579764404297, 340.9654559326172, 369.58971643066405], [6, 3.807019897460938, 494.36872668457033, 387.26940673828125, 417.577447265625], [6, 5.438599853515625, 152.2807958984375, 430.2057974853516, 457.98816796875], [6, 5.438599853515625, 358.94759033203127, 476.5097482910156, 505.1340087890625], [6, 3.807019897460938, 138.68429626464845, 519.4461390380859, 547.2285095214844], [6, 3.807019897460938, 54.385998535156254, 564.0663098144531, 590.1649002685547], [6, 3.807019897460938, 54.385998535156254, 608.6864805908203, 634.7850710449219], [6, 5.438599853515625, 190.89485485839845, 652.4647613525391, 679.4052418212891], [6, 7.614039794921876, 253.98261315917972, 696.2430421142578, 722.3416325683594], [6, 114.21059692382813, 473.1581872558594, 735.8118728027343, 761.9104632568359], [6, 191.98257482910157, 422.03534863281254, 774.5388134765625, 799.7955139160156]]
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=12.5s
2026-08-05 04:13:43,446 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] positions(17): [[7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:13:43,446 INFO     29 [qwen-vl-text] page grouping: [7, 8], lines per page: [1, 16]
2026-08-05 04:13:43,654 INFO     29 [qwen-vl-text] page=7, rect=595x843, img=(1654x2342), dpi=200
2026-08-05 04:13:43,866 INFO     29 [qwen-vl-text] page=8, rect=595x843, img=(1654x2342), dpi=200
2026-08-05 04:13:43,867 INFO     29 [qwen-vl-text] LLM extraction start, text_len=242
2026-08-05 04:13:43,867 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:43,867 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 203, \"bbox_end\": 219, \"encounter_dates\": [\"2025-10-14\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "2025/09/19 18:04\n新药特药大药房总店\n流水单号 10020044912\n结账时间 2025-10-14 08:34:01\n编号 数量 单价 金额 营业员\n沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug\n泡/葛兰素史克(集团)/库存1\n0200127 1 盒 199.00 199.00\n合计 199.00\n优惠:0.00 微信:0.00\n收银 1002\n银台\n会员\n本次积分 0.00\n累计积分 0.00\n此票为开发票依据,药品为特殊、\n商品,售出概不退还!",
    "role": "user"
  }
]
[92m04:13:43 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:43,868 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:47,262 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:47,262 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2025-10-14",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂(舒利迭)",
      "specification": "50ug:250ug",
      "dosage": null,
      "quantity": 1,
      "unit_price": 199.00,
      "total_price": 199.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克(集团)",
      "approval_number": null
    }
  ],
  "payment_total": 199.00,
  "payment_method": null
}
2026-08-05 04:13:47,263 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-14]
2026-08-05 04:13:47,266 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055779, prompt_len=631
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2025/09/19 18:04"]

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
2026-08-05 04:13:48,849 INFO     29 [qwen-vl-text] coord API raw response (len=75):
```json
[
	{"text": "2025/09/19 18:04", "bbox": [199, 790, 346, 803]}
]
```
2026-08-05 04:13:48,849 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.6s
2026-08-05 04:13:48,849 INFO     29 [qwen-vl-text] coord item[0]: text=2025/09/19 18:04, bbox=[199, 790, 346, 803]
2026-08-05 04:13:48,850 INFO     29 [qwen-vl-text] page=7 — 1/1 coords, api_time=1.6s
2026-08-05 04:13:48,851 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=938473, prompt_len=886
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["新药特药大药房总店", "流水单号 10020044912", "结账时间 2025-10-14 08:34:01", "编号 数量 单价 金额 营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "泡/葛兰素史克(集团)/库存1", "0200127 1 盒 199.00 199.00", "合计 199.00", "优惠:0.00 微信:0.00", "收银 1002", "银台", "会员", "本次积分 0.00", "累计积分 0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]

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
2026-08-05 04:13:52,210 INFO     29 [qwen-vl-parser] table API response (len=43277):
\begin{tabular}{ccccccccc}
\hline
\textbf{英文} & \textbf{项目名称} & \textbf{结果} & \textbf{提示} & \textbf{参考范围} & \textbf{单位} & \textbf{英文} & \textbf{项目名称} & \textbf{结果} & \textbf{提示} & \textbf{参考范围} & \textbf{单位} \\
\hline
{[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\
{[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\
{[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\
{[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\
{[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\
{[AST/ALT]}谷草/谷丙 & 2.14 & \textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\textup{\text
2026-08-05 04:13:52,212 INFO     29 [qwen-vl-parser] page=48 table: 11 LaTeX lines (bbox 1676-1686)
2026-08-05 04:13:52,212 INFO     29 [qwen-vl-parser] page=48 table: 11 sections
2026-08-05 04:13:52,375 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=644
2026-08-05 04:13:53,959 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:13:53,959 INFO     29 [qwen-vl-parser] page=49 classify=table report_date=2026-01-15
2026-08-05 04:13:53,966 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1378163, prompt_len=756
2026-08-05 04:13:56,693 INFO     29 [qwen-vl-text] coord API raw response (len=919):
[
	{"text": "新药特药大药房总店", "bbox": [165, 162, 642, 199]},
	{"text": "流水单号 10020044912", "bbox": [48, 210, 642, 243]},
	{"text": "结账时间 2025-10-14 08:34:01", "bbox": [48, 262, 642, 292]},
	{"text": "编号 数量 单价 金额 营业员", "bbox": [48, 310, 764, 347]},
	{"text": "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug", "bbox": [48, 360, 946, 395]},
	{"text": "泡/葛兰素史克(集团)/库存1", "bbox": [48, 409, 613, 440]},
	{"text": "0200127 1 盒 199.00 199.00", "bbox": [48, 460, 860, 490]},
	{"text": "合计 199.00", "bbox": [48, 508, 293, 537]},
	{"text": "优惠:0.00 微信:0.00", "bbox": [48, 558, 607, 590]},
	{"text": "收银 1002", "bbox": [48, 608, 252, 638]},
	{"text": "银台", "bbox": [48, 660, 123, 690]},
	{"text": "会员", "bbox": [48, 710, 123, 741]},
	{"text": "本次积分 0.00", "bbox": [48, 762, 339, 792]},
	{"text": "累计积分 0.00", "bbox": [48, 813, 448, 844]},
	{"text": "此票为开发票依据,药品为特殊、", "bbox": [220, 863, 817, 895]},
	{"text": "商品,售出概不退还!", "bbox": [350, 913, 730, 942]}
]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=7.8s
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[165, 162, 642, 199]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号 10020044912, bbox=[48, 210, 642, 243]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[2]: text=结账时间 2025-10-14 08:34:01, bbox=[48, 262, 642, 292]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[3]: text=编号 数量 单价 金额 营业员, bbox=[48, 310, 764, 347]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[4]: text=沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug, bbox=[48, 360, 946, 395]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[5]: text=泡/葛兰素史克(集团)/库存1, bbox=[48, 409, 613, 440]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[6]: text=0200127 1 盒 199.00 199.00, bbox=[48, 460, 860, 490]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[7]: text=合计 199.00, bbox=[48, 508, 293, 537]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[8]: text=优惠:0.00 微信:0.00, bbox=[48, 558, 607, 590]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[9]: text=收银 1002, bbox=[48, 608, 252, 638]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[10]: text=银台, bbox=[48, 660, 123, 690]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[11]: text=会员, bbox=[48, 710, 123, 741]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[12]: text=本次积分 0.00, bbox=[48, 762, 339, 792]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[13]: text=累计积分 0.00, bbox=[48, 813, 448, 844]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[14]: text=此票为开发票依据,药品为特殊、, bbox=[220, 863, 817, 895]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] coord item[15]: text=商品,售出概不退还!, bbox=[350, 913, 730, 942]
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] page=8 — 16/16 coords, api_time=7.8s
2026-08-05 04:13:56,694 INFO     29 [qwen-vl-text] new_positions (17):
[[7, 118.46072583007812, 205.96689013671875, 665.9937231445313, 676.9531135253906], [8, 98.22120483398437, 382.1697788085937, 136.57086474609375, 167.76297583007812], [8, 28.573441406249998, 382.1697788085937, 177.03630615234374, 204.85629711914063], [8, 28.573441406249998, 382.1697788085937, 220.87386767578124, 246.1647685546875], [8, 28.573441406249998, 454.7939423828125, 261.33930908203126, 292.5314201660156], [8, 28.573441406249998, 563.1349077148437, 303.49081054687497, 332.99686157226563], [8, 28.573441406249998, 364.90665795898434, 344.79928198242186, 370.933212890625], [8, 28.573441406249998, 511.94082519531247, 387.7938134765625, 413.08471435546875], [8, 28.573441406249998, 174.41704858398435, 428.2592548828125, 452.70712573242184], [8, 28.573441406249998, 361.3349777832031, 470.4107563476562, 497.3877172851562], [8, 28.573441406249998, 150.0105673828125, 512.5622578125, 537.8531586914063], [8, 28.573441406249998, 73.21944360351561, 556.3998193359375, 581.6907202148437], [8, 28.573441406249998, 73.21944360351561, 598.5513208007812, 624.6852517089843], [8, 28.573441406249998, 201.7999299316406, 642.3888823242187, 667.679783203125], [8, 28.573441406249998, 266.685453125, 685.3834138183594, 711.5173447265624], [8, 130.9616064453125, 486.34378393554687, 727.5349152832031, 754.5118762207031], [8, 208.34801025390624, 434.55442138671873, 769.6864167480469, 794.1342875976562]]
2026-08-05 04:13:56,695 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=2, time=13.2s
2026-08-05 04:13:56,695 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:13:56,695 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 04:13:56,695 INFO     29 [qwen-vl-text] positions(31): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:13:56,695 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [31]
2026-08-05 04:13:57,000 INFO     29 [qwen-vl-text] page=11, rect=466x842, img=(1294x2339), dpi=200
2026-08-05 04:13:57,001 INFO     29 [qwen-vl-text] LLM extraction start, text_len=220
2026-08-05 04:13:57,001 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:13:57,002 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 257, \"bbox_end\": 287, \"encounter_dates\": [\"2026-01-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "新药特药大药房总店\n流水单号\n10020046503\n结账时间\n2026-01-02 18:12:29\n编号\n数量\n单价\n金额\n营业员\n沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:\n泡/葛兰素史克(集团)/库存1\n0200127\n1\n盒\n199.00\n199.00\n合计\n199.00\n优惠:0.00\n微信:0.00\n收银\n1002\n银台\n会员\n本次积分\n0.00\n累计积分\n0.00\n此票为开发票依据,药品为特殊、\n商品,售出概不退还!",
    "role": "user"
  }
]
[92m04:13:57 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:57,003 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:13:57,555 INFO     29 [qwen-vl-parser] table API response (len=659):
\begin{tabular}{ccccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\
\hline
[颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\
[浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\
[GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\
[NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\
[LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\
[PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\
[NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\
[URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\
[BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\
[KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\
[pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\
\hline
\end{tabular}
2026-08-05 04:13:57,556 INFO     29 [qwen-vl-parser] page=49 table: 18 LaTeX lines (bbox 1687-1704)
2026-08-05 04:13:57,556 INFO     29 [qwen-vl-parser] page=49 table: 18 sections
2026-08-05 04:13:57,677 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=644
2026-08-05 04:13:59,078 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:13:59,078 INFO     29 [qwen-vl-parser] page=50 classify=table report_date=2026-01-15
2026-08-05 04:13:59,086 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=814682, prompt_len=756
2026-08-05 04:13:59,661 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:13:59,661 INFO     29 [qwen-vl-text] LLM output (len=431):
{
  "encounter_date": "2026-01-02",
  "pharmacy": "新药特药大药房总店",
  "medications": [
    {
      "name": "沙美特罗替卡松吸入粉雾剂(舒利迭)",
      "specification": "50ug/泡",
      "dosage": null,
      "quantity": 1,
      "unit_price": 199.00,
      "total_price": 199.00,
      "frequency": null,
      "route": null,
      "manufacturer": "葛兰素史克(集团)",
      "approval_number": null
    }
  ],
  "payment_total": 199.00,
  "payment_method": null
}
2026-08-05 04:13:59,661 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-02]
2026-08-05 04:13:59,666 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2692129, prompt_len=926
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["新药特药大药房总店", "流水单号", "10020046503", "结账时间", "2026-01-02 18:12:29", "编号", "数量", "单价", "金额", "营业员", "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "泡/葛兰素史克(集团)/库存1", "0200127", "1", "盒", "199.00", "199.00", "合计", "199.00", "优惠:0.00", "微信:0.00", "收银", "1002", "银台", "会员", "本次积分", "0.00", "累计积分", "0.00", "此票为开发票依据,药品为特殊、", "商品,售出概不退还!"]

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
2026-08-05 04:14:00,889 INFO     29 [qwen-vl-parser] table API response (len=245):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\
\hline
[FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\
[FR T4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\
[fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\
\hline
\end{tabular}
2026-08-05 04:14:00,890 INFO     29 [qwen-vl-parser] page=50 table: 10 LaTeX lines (bbox 1705-1714)
2026-08-05 04:14:00,890 INFO     29 [qwen-vl-parser] page=50 table: 10 sections
2026-08-05 04:14:01,023 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=644
2026-08-05 04:14:02,493 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-15"
}
```
2026-08-05 04:14:02,493 INFO     29 [qwen-vl-parser] page=51 classify=table report_date=2026-01-15
2026-08-05 04:14:02,503 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1044406, prompt_len=756
2026-08-05 04:14:04,463 INFO     29 [qwen-vl-parser] table API response (len=318):
\begin{tabular}{ccccccc}
\hline
英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\
\hline
{[}HBsAg{]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co & & \\
{[}抗-HCV{]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co & & \\
{[}抗-HIV{]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co & & \\
{[}TP-Ab{]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co & & \\
\hline
\end{tabular}
2026-08-05 04:14:04,464 INFO     29 [qwen-vl-parser] page=51 table: 11 LaTeX lines (bbox 1715-1725)
2026-08-05 04:14:04,464 INFO     29 [qwen-vl-parser] page=51 table: 11 sections
2026-08-05 04:14:04,650 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=644
2026-08-05 04:14:07,335 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 04:14:07,335 INFO     29 [qwen-vl-parser] page=52 classify=text report_date=None
2026-08-05 04:14:07,349 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1042924, prompt_len=401
2026-08-05 04:14:08,794 INFO     29 [qwen-vl-parser] text API response (len=171):
["处方笺", "4970401", "姓名：", "性别：□男 □女 年龄：60岁", "科别： 费别： 电话/住址：", "过敏史：无 开具日期：2021年2月16日", "临床诊断：支气管哮喘", "Rp", "复方丙酸倍氯米松气雾剂 20g", "用法：二天喷一次，3.", "审核： 调配： 医师：", "核对： 发药： 金额："]
2026-08-05 04:14:08,795 INFO     29 [qwen-vl-parser] page=52 text: 12 lines (bbox 1726-1737)
2026-08-05 04:14:08,795 INFO     29 [qwen-vl-parser] page=52 text: 12 sections
2026-08-05 04:14:08,795 INFO     29 [qwen-vl-parser] parse_pdf done: 1738 sections from 52 pages.
2026-08-05 04:14:08,805 INFO     29 Close text detector.
2026-08-05 04:14:09,124 INFO     29 Close text recognizer.
2026-08-05 04:14:09,453 INFO     29 Close recognizer.
2026-08-05 04:14:09,760 INFO     29 Close recognizer.
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord API raw response (len=1574):
[
	{"text": "新药特药大药房总店", "bbox": [181, 124, 755, 161]},
	{"text": "流水单号", "bbox": [50, 176, 233, 205]},
	{"text": "10020046503", "bbox": [487, 177, 752, 202]},
	{"text": "结账时间", "bbox": [48, 223, 233, 252]},
	{"text": "2026-01-02 18:12:29", "bbox": [285, 224, 752, 250]},
	{"text": "编号", "bbox": [45, 270, 136, 302]},
	{"text": "数量", "bbox": [238, 268, 335, 300]},
	{"text": "单价", "bbox": [410, 269, 503, 302]},
	{"text": "金额", "bbox": [580, 270, 678, 302]},
	{"text": "营业员", "bbox": [752, 270, 895, 303]},
	{"text": "沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:", "bbox": [45, 317, 972, 348]},
	{"text": "泡/葛兰素史克(集团)/库存1", "bbox": [45, 364, 713, 394]},
	{"text": "0200127", "bbox": [48, 413, 216, 438]},
	{"text": "1", "bbox": [318, 413, 335, 438]},
	{"text": "盒", "bbox": [460, 412, 508, 441]},
	{"text": "199.00", "bbox": [608, 414, 755, 439]},
	{"text": "199.00", "bbox": [854, 414, 998, 439]},
	{"text": "合计", "bbox": [48, 458, 138, 485]},
	{"text": "199.00", "bbox": [190, 460, 339, 484]},
	{"text": "优惠:0.00", "bbox": [45, 505, 288, 532]},
	{"text": "微信:0.00", "bbox": [458, 507, 700, 533]},
	{"text": "收银", "bbox": [42, 549, 134, 577]},
	{"text": "1002", "bbox": [188, 553, 285, 576]},
	{"text": "银台", "bbox": [42, 595, 130, 623]},
	{"text": "会员", "bbox": [42, 642, 130, 670]},
	{"text": "本次积分", "bbox": [42, 687, 228, 714]},
	{"text": "0.00", "bbox": [282, 690, 380, 713]},
	{"text": "累计积分", "bbox": [48, 730, 228, 756]},
	{"text": "0.00", "bbox": [402, 734, 503, 757]},
	{"text": "此票为开发票依据,药品为特殊、", "bbox": [243, 773, 915, 800]},
	{"text": "商品,售出概不退还!", "bbox": [387, 811, 819, 835]}
]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=10.4s
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[0]: text=新药特药大药房总店, bbox=[181, 124, 755, 161]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[1]: text=流水单号, bbox=[50, 176, 233, 205]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[2]: text=10020046503, bbox=[487, 177, 752, 202]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[3]: text=结账时间, bbox=[48, 223, 233, 252]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[4]: text=2026-01-02 18:12:29, bbox=[285, 224, 752, 250]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[5]: text=编号, bbox=[45, 270, 136, 302]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[6]: text=数量, bbox=[238, 268, 335, 300]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[7]: text=单价, bbox=[410, 269, 503, 302]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[8]: text=金额, bbox=[580, 270, 678, 302]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[9]: text=营业员, bbox=[752, 270, 895, 303]
2026-08-05 04:14:10,084 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:, bbox=[45, 317, 972, 348]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[11]: text=泡/葛兰素史克(集团)/库存1, bbox=[45, 364, 713, 394]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[12]: text=0200127, bbox=[48, 413, 216, 438]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[13]: text=1, bbox=[318, 413, 335, 438]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[14]: text=盒, bbox=[460, 412, 508, 441]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[15]: text=199.00, bbox=[608, 414, 755, 439]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[16]: text=199.00, bbox=[854, 414, 998, 439]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[17]: text=合计, bbox=[48, 458, 138, 485]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[18]: text=199.00, bbox=[190, 460, 339, 484]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[19]: text=优惠:0.00, bbox=[45, 505, 288, 532]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[20]: text=微信:0.00, bbox=[458, 507, 700, 533]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[21]: text=收银, bbox=[42, 549, 134, 577]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[22]: text=1002, bbox=[188, 553, 285, 576]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[23]: text=银台, bbox=[42, 595, 130, 623]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[24]: text=会员, bbox=[42, 642, 130, 670]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[25]: text=本次积分, bbox=[42, 687, 228, 714]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[26]: text=0.00, bbox=[282, 690, 380, 713]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[27]: text=累计积分, bbox=[48, 730, 228, 756]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[28]: text=0.00, bbox=[402, 734, 503, 757]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[29]: text=此票为开发票依据,药品为特殊、, bbox=[243, 773, 915, 800]
2026-08-05 04:14:10,085 INFO     29 [qwen-vl-text] coord item[30]: text=商品,售出概不退还!, bbox=[387, 811, 819, 835]
2026-08-05 04:14:10,086 INFO     29 [qwen-vl-text] page=11 — 31/31 coords, api_time=10.4s
2026-08-05 04:14:10,086 INFO     29 [qwen-vl-text] new_positions (31):
[[11, 84.25731176757813, 351.4600573730469, 104.39436181640625, 135.54429235839842], [11, 23.27550048828125, 108.46383227539063, 148.172642578125, 172.5874530029297], [11, 226.7033747558594, 350.06352734375, 149.01453259277343, 170.06178295898437], [11, 22.34448046875, 108.46383227539063, 187.74147326660156, 212.15628369140626], [11, 132.67035278320313, 350.06352734375, 188.58336328125, 210.47250366210938], [11, 20.947950439453127, 63.309361328125, 227.31030395507813, 254.25078442382812], [11, 110.79138232421876, 155.94585327148437, 225.62652392578124, 252.56700439453124], [11, 190.85910400390625, 234.15153491210938, 226.46841394042968, 254.25078442382812], [11, 269.9958056640625, 315.6157866210938, 227.31030395507813, 254.25078442382812], [11, 350.06352734375, 416.6314587402344, 227.31030395507813, 255.09267443847656], [11, 20.947950439453127, 452.4757294921875, 266.87913464355466, 292.9777250976562], [11, 20.947950439453127, 331.9086369628906, 306.44796533203123, 331.7046657714844], [11, 22.34448046875, 100.55016210937501, 347.7005760498047, 368.74782641601564], [11, 148.03218310546876, 155.94585327148437, 347.7005760498047, 368.74782641601564], [11, 214.1346044921875, 236.4790849609375, 346.85868603515627, 371.27349645996094], [11, 283.0300859375, 351.4600573730469, 348.5424660644531, 369.58971643066405], [11, 397.5455483398438, 464.5789897460938, 348.5424660644531, 369.58971643066405], [11, 22.34448046875, 64.24038134765625, 385.58562670898436, 408.3166571044922], [11, 88.44690185546875, 157.8078933105469, 387.26940673828125, 407.47476708984374], [11, 20.947950439453127, 134.0668828125, 425.15445739746093, 447.8854877929687], [11, 213.20358447265625, 325.8570068359375, 426.8382374267578, 448.7273778076172], [11, 19.55142041015625, 62.378341308593754, 462.1976180419922, 485.77053845214846], [11, 87.5158818359375, 132.67035278320313, 465.5651781005859, 484.9286484375], [11, 19.55142041015625, 60.516301269531255, 500.9245587158203, 524.4974791259766], [11, 19.55142041015625, 60.516301269531255, 540.4933894042969, 564.0663098144531], [11, 19.55142041015625, 106.1362822265625, 578.3784400634765, 601.1094704589843], [11, 131.27382275390624, 176.8938037109375, 580.9041101074218, 600.267580444336], [11, 22.34448046875, 106.1362822265625, 614.5797106933594, 636.4688510742187], [11, 187.13502392578124, 234.15153491210938, 617.9472707519532, 637.3107410888672], [11, 113.11893237304687, 425.9416589355469, 650.7809813232421, 673.51201171875], [11, 180.15237377929688, 381.25269799804687, 682.7728018798828, 702.9781622314453]]
2026-08-05 04:14:10,086 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=13.4s
2026-08-05 04:14:10,125 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 04:14:10,125 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:14:10,126 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 04:14:10,126 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:14:10.126+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:14:10,135 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:14:10,136 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:14:10,136 INFO     29 [qwen-vl-text] positions(21): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:14:10,136 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [21]
2026-08-05 04:14:10,339 INFO     29 [qwen-vl-text] page=7, rect=595x843, img=(1654x2342), dpi=200
2026-08-05 04:14:10,340 INFO     29 [qwen-vl-text] LLM extraction start, text_len=258
2026-08-05 04:14:10,340 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:10,340 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 182, \"bbox_end\": 202, \"encounter_dates\": [\"2025-09-02\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "2/4\n25/09/02 14:58\n普通\n科\n室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\n孟鲁司特钠片【舒宁安】乙\n超量说明:\n【10mg*5片】\n(4.96元/盒)\n3盒\n用法用量:每次10mg,睡前口服,每天一次\n医师:杨沂发药:修泉涌配药:沈瑶\nvivo X80 · ZEISS\n计:208.48/208.48\n第1页/共1页",
    "role": "user"
  }
]
[92m04:14:10 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:10,342 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:10,876 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 04:14:10,876 INFO     29 [Trace] task=6bc9a31c | doc=DAXI-哮喘.pdf | Parser:MedLink | outputs={"html": "", "json": "1738 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "json"}
2026-08-05 04:14:10,876 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 04:14:10,911 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:14:10,912 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] \\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c\n[BBOX-1] 报告时间: 2026-01-29\n[BBOX-2] \\begin{tabular}{lcccccc}\n[BBOX-3] 报告时间: 2026-01-15\n[BBOX-4] \\hline\n[BBOX-5] & 预计值 & Bst \\% (Bst/ & A1 & A2 & A3 \\\\\n[BBOX-6] \\hline\n[BBOX-7] FVC & [L] & 3.13 & 3.15 & 100.54 & 3.15 & 3.08 & 3.07 \\\\\n[BBOX-8] FEV 1 & [L] & 2.70 & 1.99 & 73.90 & 1.99 & 1.85 & 1.96 \\\\\n[BBOX-9] FEV6 & [L] & & 3.13 & & 3.13 & & 3.05 \\\\\n[BBOX-10] FEV 1 \\% FVC & [\\%] & 83.98 & 63.25 & 75.31 & 63.25 & 60.02 & 63.82 \\\\\n[BBOX-11] FEV 1 \\% VC MAX & [\\%] & 81.31 & 63.25 & 77.78 & 63.25 & 58.74 & 62.12 \\\\\n[BBOX-12] FIF 50 & [L/s] & & 5.84 & & 5.77 & 5.84 & 5.48 \\\\\n[BBOX-13] FEV3 \\% FVC & [\\%] & & 89.30 & & 89.30 & 87.11 & 88.97 \\\\\n[BBOX-14] VC MAX & [L] & 3.19 & 3.15 & 98.65 & 2.99 & & \\\\\n[BBOX-15] PEF & [L/s] & 6.46 & 6.33 & 97.97 & 6.33 & 5.90 & 5.95 \\\\\n[BBOX-16] MMEF 75/25 & [L/s] & 3.53 & 1.06 & 30.03 & 1.06 & 0.89 & 0.99 \\\\\n[BBOX-17] MEF 25 & [L/s] & 1.77 & 0.46 & 26.28 & 0.46 & 0.38 & 0.40 \\\\\n[BBOX-18] MEF 50 & [L/s] & 4.06 & 1.25 & 30.90 & 1.25 & 1.13 & 1.24 \\\\\n[BBOX-19] MEF 75 & [L/s] & 5.73 & 3.01 & 52.56 & 3.01 & 2.22 & 2.68 \\\\\n[BBOX-20] V backextrapolation [B] & & & 0.06 & & 0.06 & 0.05 & 0.06 \\\\\n[BBOX-21] V backextrapol. \\% FVC & & & 1.86 & & 1.86 & 1.52 & 1.82 \\\\\n[BBOX-22] FET & [s] & & 8.73 & & 8.73 & 5.99 & 6.71 \\\\\n[BBOX-23] FEF 200-1200 & [L/s] & & 3.07 & & 3.07 & 2.51 & 2.98 \\\\\n[BBOX-24] FVC IN & [L] & 3.19 & 2.99 & 93.64 & 2.26 & 2.99 & 2.94 \\\\\n[BBOX-25] FIV1 & [L] & & 2.96 & & 2.24 & 2.96 & 2.92 \\\\\n[BBOX-26] FIV1 \\% FVC & [\\%] & & 99.14 & & 99.32 & 99.14 & 99.48 \\\\\n[BBOX-27] FEF50 \\% FIF50 & [\\%] & & 21.46 & & 21.72 & 19.34 & 22.60 \\\\\n[BBOX-28] PIF & [L/s] & & 6.10 & & 5.87 & 6.10 & 5.50 \\\\\n[BBOX-29] MVV & [L/min] & 101.9 & 91.45 & 89.73 & 91.45 & & \\\\\n[BBOX-30] BF MVV & [1/min] & & 75.65 & & 75.65 & & \\\\\n[BBOX-31] \\hline\n[BBOX-32] \\end{tabular}\n[BBOX-33] \\begin{tabular}{lcccccc}\n[BBOX-34] 报告时间: 2015-01-26\n[BBOX-35] \\hline\n[BBOX-36] \\multicolumn{7}{c}{\\textbf{肺功能报告单}} \\\\\n[BBOX-37] \\hline\n[BBOX-38] 姓名： & & & & & & \\\\\n[BBOX-39] 出生日期： & 1984/11/02 & & & & & \\\\\n[BBOX-40] 住院号： & & & & & & \\\\\n[BBOX-41] 身高： & 160 cm & & & & & \\\\\n[BBOX-42] 身份证号： & & & & & & \\\\\n[BBOX-43] 性别： & 女 & & & & & \\\\\n[BBOX-44] 年龄： & 41 岁 & & & & & \\\\\n[BBOX-45] 测试号： & & & & & & \\\\\n[BBOX-46] 体重： & 48 kg & & & & & \\\\\n[BBOX-47] \\hline\n[BBOX-48] \\multicolumn{1}{l}{测试日期} & \\multicolumn{1}{c}{预计} & \\multicolumn{2}{c}{实1 \\% (实1/预)} & \\multicolumn{2}{c}{实2 \\% (实2/预)} & \\multicolumn{1}{c}{变异率} \\\\\n[BBOX-49] \\multicolumn{1}{l}{测试时间} & & \\multicolumn{1}{c}{26/1/15} & & \\multicolumn{1}{c}{26/1/15} & & \\\\\n[BBOX-50] \\multicolumn{1}{l}{} & & \\multicolumn{1}{c}{9:51:00上午} & & \\multicolumn{1}{c}{10:14:56上午} & & \\\\\n[BBOX-51] \\hline\n[BBOX-52] FVC & [L] & 3.13 & 3.15 & 100.5 & 3.25 & 103.9 & 3.3 \\\\\n[BBOX-53] FEV 1 & [L] & 2.70 & 1.99 & 73.9 & 2.26 & 83.8 & 13.4 \\\\\n[BBOX-54] FEV 1 \\% FVC & [\\%] & 83.98 & 63.25 & 75.3 & 69.40 & 82.6 & 9.7 \\\\\n[BBOX-55] FEV 1 \\% VC MAX & [\\%] & 81.31 & 63.25 & 77.8 & 69.40 & 85.4 & 9.7 \\\\\n[BBOX-56] PEF & [L/s] & 6.46 & 6.33 & 98.0 & 7.25 & 112.2 & 14.5 \\\\\n[BBOX-57] MEF 75 & [L/s] & 5.73 & 3.01 & 52.6 & 3.73 & 65.1 & 23.8 \\\\\n[BBOX-58] MEF 50 & [L/s] & 4.06 & 1.25 & 30.9 & 1.67 & 41.2 & 33.3 \\\\\n[BBOX-59] MEF 25 & [L/s] & 1.77 & 0.46 & 26.3 & 0.59 & 33.6 & 27.7 \\\\\n[BBOX-60] MMEF 75/25 & [L/s] & 3.53 & 1.06 & 30.0 & 1.46 & 41.3 & 37.6 \\\\\n[BBOX-61] FET & [s] & & 8.73 & & 4.94 & & -43.4 \\\\\n[BBOX-62] V backextrapolation ex [L] & & & 0.06 & & 0.07 & & 20.1 \\\\\n[BBOX-63] V backextrapol. \\% FVC [\\%] & & & 1.86 & & 2.17 & & 16.3 \\\\\n[BBOX-64] \\hline\n[BBOX-65] \\end{tabular}\n[BBOX-66] \\begin{tabular}{l c c c c c c}\n[BBOX-67] 报告时间: 2025-04-11\n[BBOX-68] \\hline\n[BBOX-69] \\multicolumn{7}{c}{\\textbf{肺功能报告单}} \\\\\n[BBOX-70] \\hline\n[BBOX-71] \\textbf{姓名:} & & & & & & \\\\\n[BBOX-72] \\textbf{出生日期:} & 1984/4/02 & & & & & \\\\\n[BBOX-73] \\textbf{门诊/住院/体检:} & & & & & & \\\\\n[BBOX-74] \\textbf{身高:} & 160 cm & & & & & \\\\\n[BBOX-75] \\textbf{身份证号:} & & & & & & \\\\\n[BBOX-76] \\textbf{性别:} & & & & & & 女 \\\\\n[BBOX-77] \\textbf{年龄:} & & & & & & 41 岁 \\\\\n[BBOX-78] \\textbf{测试号:} & & & & & & \\\\\n[BBOX-79] \\textbf{体重:} & & & & & & 50 kg \\\\\n[BBOX-80] \\hline\n[BBOX-81] \\textbf{测试日期} & \\textbf{预计} & \\textbf{实测} & \\textbf{\\% (实/预)} & & & \\\\\n[BBOX-82] \\textbf{测试时间} & & & & & & \\\\\n[BBOX-83] \\hline\n[BBOX-84] & & & & & & \\\\\n[BBOX-85] VT & [L] & 0.36 & 0.41 & 114.9 & & \\\\\n[BBOX-86] BF & [1/min] & 20.00 & 20.79 & 104.0 & & \\\\\n[BBOX-87] MV & [L/min] & 7.14 & 8.54 & 119.5 & & \\\\\n[BBOX-88] ERV & [L] & 1.07 & 1.07 & 99.4 & & \\\\\n[BBOX-89] VC MAX & [L] & 3.19 & 2.84 & 88.9 & & \\\\\n[BBOX-90] \\hline\n[BBOX-91] FVC & [L] & 3.13 & 2.84 & 90.6 & & \\\\\n[BBOX-92] FEV 1 & [L] & 2.70 & 1.53 & 56.9 & & \\\\\n[BBOX-93] FEV 1 \\% FVC & [\\%] & 83.98 & 54.07 & 64.4 & & \\\\\n[BBOX-94] FEV 1 \\% VC MAX & [\\%] & 81.31 & 54.07 & 66.5 & & \\\\\n[BBOX-95] PEF & [L/s] & 6.46 & 4.56 & 70.7 & & \\\\\n[BBOX-96] MEF 75 & [L/s] & 5.73 & 1.84 & 32.1 & & \\\\\n[BBOX-97] MEF 50 & [L/s] & 4.06 & 0.84 & 20.7 & & \\\\\n[BBOX-98] MEF 25 & [L/s] & 1.77 & 0.28 & 15.6 & & \\\\\n[BBOX-99] MMEF 75/25 & [L/s] & 3.53 & 0.65 & 18.3 & & \\\\\n[BBOX-100] FET & [s] & & 8.46 & & & \\\\\n[BBOX-101] V backextrapolation ex & [L] & & 0.03 & & & \\\\\n[BBOX-102] V backextrapol. \\% FVC & [\\%] & & 1.23 & & & \\\\\n[BBOX-103] \\hline\n[BBOX-104] MVV & [L/min] & 101.93 & 75.75 & 74.3 & & \\\\\n[BBOX-105] FEV 1*30 & [L/min] & 101.93 & 46.03 & 45.2 & & \\\\\n[BBOX-106] \\hline\n[BBOX-107] RV-SB & [L] & 1.55 & 2.56 & 164.9 & & \\\\\n[BBOX-108] RV\\%TLC-SB & [\\%] & 32.90 & 47.52 & 144.4 & & \\\\\n[BBOX-109] TLC-SB & [L] & 4.77 & 5.39 & 112.9 & & \\\\\n[BBOX-110] FRC-SB & [L] & 2.63 & 3.31 & 126.0 & & \\\\\n[BBOX-111] FRC\\%TLC-SB & [\\%] & 51.66 & 61.42 & 118.9 & & \\\\\n[BBOX-112] DLCOc SB & [mmol/min/kPa] & 8.34 & 6.95 & 83.4 & & \\\\\n[BBOX-113] DLCO SB & [mmol/min/kPa] & 8.34 & 6.95 & 83.4 & & \\\\\n[BBOX-114] \\hline\n[BBOX-115] \\end{tabular}\n[BBOX-116] \\begin{tabular}{lcccccc}\n[BBOX-117] 报告时间: 2025-04-11\n[BBOX-118] \\hline\n[BBOX-119] \\multicolumn{7}{c}{肺功能报告单} \\\\\n[BBOX-120] 姓名: & & & & & & \\\\\n[BBOX-121] 出生日期: & 1984/4/02 & & 性别: & 女 & & \\\\\n[BBOX-122] 门诊/住院/体检: & & & 年龄: & 41 岁 & & \\\\\n[BBOX-123] 身高: & 160 cm & & 测试号: & & & \\\\\n[BBOX-124] 身份证号: & & & 体重: & 50 kg & & \\\\\n[BBOX-125] \\hline\n[BBOX-126] \\multicolumn{1}{c}{} & \\multicolumn{1}{c}{预计} & \\multicolumn{2}{c}{实1 \\% (实1/预)} & \\multicolumn{2}{c}{实2 \\% (实2/预)} & \\multicolumn{1}{c}{变异率} \\\\\n[BBOX-127] \\multicolumn{1}{c}{测试日期} & & & & & & \\\\\n[BBOX-128] \\multicolumn{1}{c}{测试时间} & & & & & & \\\\\n[BBOX-129] \\hline\n[BBOX-130] & & & & & & \\\\\n[BBOX-131] FVC & [L] & 3.13 & 2.84 & 90.6 & 3.05 & 7.5 \\\\\n[BBOX-132] FEV 1 & [L] & 2.70 & 1.53 & 56.9 & 1.91 & 24.7 \\\\\n[BBOX-133] FEV 1 \\% FVC & [\\%] & 83.98 & 54.07 & 64.4 & 62.70 & 16.0 \\\\\n[BBOX-134] FEV 1 \\% VC MAX & [\\%] & 81.31 & 54.07 & 66.5 & 62.70 & 16.0 \\\\\n[BBOX-135] PEF & [L/s] & 6.46 & 4.56 & 70.7 & 5.64 & 23.6 \\\\\n[BBOX-136] MEF 75 & [L/s] & 5.73 & 1.84 & 32.1 & 2.65 & 44.3 \\\\\n[BBOX-137] MEF 50 & [L/s] & 4.06 & 0.84 & 20.7 & 1.23 & 47.0 \\\\\n[BBOX-138] MEF 25 & [L/s] & 1.77 & 0.28 & 15.6 & 0.44 & 60.2 \\\\\n[BBOX-139] MMEF 75/25 & [L/s] & 3.53 & 0.65 & 18.3 & 1.02 & 58.8 \\\\\n[BBOX-140] FET & [s] & & 8.46 & & 6.41 & -24.2 \\\\\n[BBOX-141] V backextrapolation ex [L] & & & 0.03 & & 0.06 & 71.7 \\\\\n[BBOX-142] V backextrapol. \\% FVC [\\%] & & & 1.23 & & 1.96 & 59.6 \\\\\n[BBOX-143] \\hline\n[BBOX-144] \\end{tabular}\n[BBOX-145] 院\n[BBOX-146] 入院记录\n[BBOX-147] 姓名：\n[BBOX-148] 科室：产科二区\n[BBOX-149] 床号：\n[BBOX-150] 科室：产科二区\n[BBOX-151] 第(1)次入院记录\n[BBOX-152] 过敏史：无\n[BBOX-153] 姓名：\n[BBOX-154] 性别：女\n[BBOX-155] 年龄：36岁\n[BBOX-156] 身份证号\n[BBOX-157] 职业：\n[BBOX-158] 婚姻：已婚\n[BBOX-159] 民族：汉族\n[BBOX-160] 出生地：\n[BBOX-161] 现住址：\n[BBOX-162] 入院日期：2020-07-08 08:36:09\n[BBOX-163] 邮编\n[BBOX-164] 病史采集时间：2020-07-08 08:36:09\n[BBOX-165] 联系人：\n[BBOX-166] 与病人关系：夫妻\n[BBOX-167] 病史叙述者：本人\n[BBOX-168] 联系人地址：同上地址\n[BBOX-169] 电话.\n[BBOX-170] 可靠程度：可靠\n[BBOX-171] 主诉：停经39周，要求住院待产。\n[BBOX-172] 现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产\n[BBOX-173] 期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合\n[BBOX-174] 孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接\n[BBOX-175] 触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA\n[BBOX-176] 结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛\n[BBOX-177] 查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰\n[BBOX-178] 痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子\n[BBOX-179] 宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。\n[BBOX-180] 既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有\n[BBOX-181] “肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血\n[BBOX-182] 史，有献血史，否认食物及药物过敏史。预防接种随社会进行。\n[BBOX-183] 个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住\n[BBOX-184] 史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。\n[BBOX-185] 婚育史：31岁结婚，爱人\n[BBOX-186] 现年37岁，职员，工作于三门峡市党校，身体健康，无吸\n[BBOX-187] 烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男\n[BBOX-188] 婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。\n[BBOX-189] 月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳\n[BBOX-190] 历），量中等，色暗红，偶有血块，无痛经。\n[BBOX-191] 页\n[BBOX-192] 书写者签名：\n[BBOX-193] 总第 页\n[BBOX-194] 院\n[BBOX-195] 入院记录\n[BBOX-196] 姓名:\n[BBOX-197] 科室:产科二区\n[BBOX-198] 床号:\n[BBOX-199] 生.\n[BBOX-200] 家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。\n[BBOX-201] 体格检查\n[BBOX-202] 体温:36.5℃\n[BBOX-203] 脉搏:78次/分\n[BBOX-204] 呼吸:18次/分\n[BBOX-205] 血压:98/64mmHg\n[BBOX-206] 身高160cm\n[BBOX-207] 体重:60Kg\n[BBOX-208] 一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言\n[BBOX-209] 语状态流利;检查时能合作等。\n[BBOX-210] 皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创\n[BBOX-211] 伤、溃疡、结节。\n[BBOX-212] 淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。\n[BBOX-213] 头部:\n[BBOX-214] 头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。\n[BBOX-215] 眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,\n[BBOX-216] 间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。\n[BBOX-217] 耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。\n[BBOX-218] 鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。\n[BBOX-219] 口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异\n[BBOX-220] 常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿\n[BBOX-221] 大、分泌物;咽部无充血、分泌物。\n[BBOX-222] 颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居\n[BBOX-223] 中,甲状腺无肿大。\n[BBOX-224] 胸部\n[BBOX-225] 胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉\n[BBOX-226] 曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。\n[BBOX-227] 肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。\n[BBOX-228] 触诊:语音震颤两侧相等,无摩擦感。\n[BBOX-229] 叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,\n[BBOX-230] 听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、\n[BBOX-231] 第页\n[BBOX-232] 书写者签名:\n[BBOX-233] 总第页\n[BBOX-234] 院\n[BBOX-235] 入院记录\n[BBOX-236] 姓名：\n[BBOX-237] 科室：产科二区\n[BBOX-238] 床号\n[BBOX-239] 病号：\n[BBOX-240] 干啰音、湿啰音。\n[BBOX-241] 心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前\n[BBOX-242] 区无异常搏动、局限性膨隆。\n[BBOX-243] 触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、\n[BBOX-244] 震颤、摩擦感。\n[BBOX-245] 叩诊：左右心界线以每肋间距胸骨中线的cm数记载。\n[BBOX-246] 右cm\n[BBOX-247] 肋间\n[BBOX-248] 左cm\n[BBOX-249] 2\n[BBOX-250] Ⅱ\n[BBOX-251] 2.5\n[BBOX-252] 2\n[BBOX-253] Ⅲ\n[BBOX-254] 4\n[BBOX-255] 3\n[BBOX-256] Ⅳ\n[BBOX-257] 5.5\n[BBOX-258] V\n[BBOX-259] 8\n[BBOX-260] 左锁骨中线至前正中线的距离9cm。\n[BBOX-261] 听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分\n[BBOX-262] 裂，P2<A2。\n[BBOX-263] 血管：桡动脉搏动正常，血管壁硬度正常。\n[BBOX-264] 周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。\n[BBOX-265] 腹部：\n[BBOX-266] 视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆\n[BBOX-267] 起，下腹可见一长约15cm横行手术疤痕。\n[BBOX-268] 触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未\n[BBOX-269] 触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。\n[BBOX-270] 叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度\n[BBOX-271] 鼓音，移动性浊音阴性。\n[BBOX-272] 听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血\n[BBOX-273] 管杂音。\n[BBOX-274] 外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱\n[BBOX-275] 肛、湿疣等。\n[BBOX-276] 脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。\n[BBOX-277] 四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎\n[BBOX-278] 院\n[BBOX-279] 入院记录\n[BBOX-280] 姓名.\n[BBOX-281] 科室:产科二区\n[BBOX-282] 床号\n[BBOX-283] 住院号.\n[BBOX-284] 缩;关节无红肿、畸形、运动障碍,双下肢水肿。\n[BBOX-285] 神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、\n[BBOX-286] 腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。\n[BBOX-287] 专科情况\n[BBOX-288] 宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无\n[BBOX-289] 宫缩,未见红,未破水,骨盆外测量及内诊:未做。\n[BBOX-290] 辅助检查\n[BBOX-291] B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指\n[BBOX-292] 数8.5cm),胎盘成熟度II°.\n[BBOX-293] 初步诊断:\n[BBOX-294] 1.妊娠合并子宫瘢痕;\n[BBOX-295] 3.孕2产,宫内孕39周头位待产。\n[BBOX-296] 主治医师:\n[BBOX-297] 孙小丹\n[BBOX-298] 副主任医师:\n[BBOX-299] 彭琼玉\n[BBOX-300] 2020.07.08\n[BBOX-301] CS 扫描全能王\n[BBOX-302] 3亿人都在用的扫描App\n[BBOX-303] 姓名：\n[BBOX-304] 科室：产科二区\n[BBOX-305] 床号\n[BBOX-306] 住院号.\n[BBOX-307] 2020年07月08日 09时22分\n[BBOX-308] 首次病程记录\n[BBOX-309] 患\n[BBOX-310] 女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于\n[BBOX-311] 2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥\n[BBOX-312] 感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日\n[BBOX-313] (阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单\n[BBOX-314] 活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正\n[BBOX-315] 常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正\n[BBOX-316] 常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求\n[BBOX-317] 住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，\n[BBOX-318] 精神好，全身皮肤粘膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、\n[BBOX-319] 专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律\n[BBOX-320] 齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02\n[BBOX-321] 本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度\n[BBOX-322] II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位\n[BBOX-323] 待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，\n[BBOX-324] 末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎\n[BBOX-325] 动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎\n[BBOX-326] 位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。3、\n[BBOX-327] 辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm\n[BBOX-328] 羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊\n[BBOX-329] 断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检\n[BBOX-330] 查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相\n[BBOX-331] 关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、\n[BBOX-332] 患者要求明日剖宫产，纳入剖宫产临床路径。\n[BBOX-333] 主治医师：孙州\n[BBOX-334] 2020年07月08日 10时22分\n[BBOX-335] 科主任宋瑞香主治医师查房记录\n[BBOX-336] 第页\n[BBOX-337] 总第页\n[BBOX-338] 姓名：\n[BBOX-339] 科室：产科二区\n[BBOX-340] 床号：\n[BBOX-341] 住院号\n[BBOX-342] 今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破\n[BBOX-343] 水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范\n[BBOX-344] 围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依\n[BBOX-345] 据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿\n[BBOX-346] 体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及\n[BBOX-347] 内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径\n[BBOX-348] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：\n[BBOX-349] 患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者\n[BBOX-350] 及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心\n[BBOX-351] 变化。以上医嘱已执行。\n[BBOX-352] 主治医师：主治医师：\n[BBOX-353] 孙丹\n[BBOX-354] 2020年07月08日 10：20\n[BBOX-355] 术前小结\n[BBOX-356] 姓名：\n[BBOX-357] 性别：女，年龄：36岁；\n[BBOX-358] 病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感\n[BBOX-359] 染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾\n[BBOX-360] 肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，\n[BBOX-361] 腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未\n[BBOX-362] 破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎\n[BBOX-363] 头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止\n[BBOX-364] 妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同\n[BBOX-365] 意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准\n[BBOX-366] 备。\n[BBOX-367] 术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。\n[BBOX-368] 手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：\n[BBOX-369] 拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；\n[BBOX-370] 拟施麻醉：椎管内麻醉；\n[BBOX-371] 第 页\n[BBOX-372] 总第 页\n[BBOX-373] 姓名：\n[BBOX-374] 科室：产科二区\n[BBOX-375] 床号：\n[BBOX-376] 注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好\n[BBOX-377] 新生儿复苏工作。\n[BBOX-378] 主治医师：孙丹丹\n[BBOX-379] 第 页\n[BBOX-380] 总第 页\n[BBOX-381] 院\n[BBOX-382] 姓名：\n[BBOX-383] 科室：产科二区\n[BBOX-384] 床：\n[BBOX-385] 住院号：\n[BBOX-386] 2020年07月09日 09时47分\n[BBOX-387] 术后首次病程记录\n[BBOX-388] 患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫\n[BBOX-389] 下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子\n[BBOX-390] 宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸\n[BBOX-391] 净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球\n[BBOX-392] 擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝\n[BBOX-393] 合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正\n[BBOX-394] 常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不\n[BBOX-395] 多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周\n[BBOX-396] 头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头\n[BBOX-397] 孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下\n[BBOX-398] 肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。\n[BBOX-399] 住院医师：冯雪云\n[BBOX-400] 2020年07月10日 09时00分\n[BBOX-401] 彭琼玉副主任医师查房记录\n[BBOX-402] 今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师\n[BBOX-403] 查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合\n[BBOX-404] 好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量\n[BBOX-405] 正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病\n[BBOX-406] 情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连\n[BBOX-407] 及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫\n[BBOX-408] 恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活\n[BBOX-409] 动，注意监测血糖情况，上述指示已执行。\n[BBOX-410] 副主任医师：马\n[BBOX-411] 住院医师：冯雪云\n[BBOX-412] 2020年07月11日 08时06分\n[BBOX-413] 术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊\n[BBOX-414] 第 页\n[BBOX-415] 总第 页\n[BBOX-416] 出院\n[BBOX-417] 姓名：\n[BBOX-418] 科室：产科二区\n[BBOX-419] 床号\n[BBOX-420] 住院\n[BBOX-421] 未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血\n[BBOX-422] 不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双\n[BBOX-423] 下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切\n[BBOX-424] 口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加\n[BBOX-425] 益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。\n[BBOX-426] 主治医师：孙丹丹\n[BBOX-427] 2020年07月12日 10时00分\n[BBOX-428] 彭琼玉副主任医师查房记录\n[BBOX-429] 今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生\n[BBOX-430] 命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异\n[BBOX-431] 常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性\n[BBOX-432] 粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，\n[BBOX-433] 切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任\n[BBOX-434] 医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫\n[BBOX-435] 产临床路径管理，今日办理出院。指示已执行。\n[BBOX-436] 副主任医师：彭琼玉\n[BBOX-437] 主治医师：孙丹丹\n[BBOX-438] 出院记录\n[BBOX-439] 姓名\n[BBOX-440] 科室：产科二区\n[BBOX-441] 床号.\n[BBOX-442] 住院号.\n[BBOX-443] 2020年07月12日\n[BBOX-444] 出院记录\n[BBOX-445] 患者.\n[BBOX-446] 36岁\n[BBOX-447] 住院号：\n[BBOX-448] 入院日期：2020-07-08 08:36:09\n[BBOX-449] 出院日期：2020年07月12日\n[BBOX-450] 住院天数：4天\n[BBOX-451] 入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺\n[BBOX-452] 听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估\n[BBOX-453] 计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外\n[BBOX-454] 测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径\n[BBOX-455] 9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。\n[BBOX-456] 入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。\n[BBOX-457] 诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在\n[BBOX-458] 腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢\n[BBOX-459] 痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，\n[BBOX-460] 切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘\n[BBOX-461] 胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝\n[BBOX-462] 合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫\n[BBOX-463] 切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗\n[BBOX-464] 感染、加强宫缩支持及对症治疗。\n[BBOX-465] 出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：\n[BBOX-466] 出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显\n[BBOX-467] 异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩\n[BBOX-468] 好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳\n[BBOX-469] 泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划\n[BBOX-470] 性剖宫产临床路径。\n[BBOX-471] 出院医嘱：1.注意休息，合理营养；\n[BBOX-472] 2.禁性生活、盆浴及重体力劳动2个月；\n[BBOX-473] 3.坚持纯母乳喂养大于4-6月；\n[BBOX-474] 第 页\n[BBOX-475] 总第 页\n[BBOX-476] 医院\n[BBOX-477] 出院记录\n[BBOX-478] 姓名：\n[BBOX-479] 科室：产科二区\n[BBOX-480] 床号：\n[BBOX-481] 住院号：2\n[BBOX-482] 4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理\n[BBOX-483] 状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经\n[BBOX-484] 量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）\n[BBOX-485] 5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：\n[BBOX-486] 6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂\n[BBOX-487] 1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或\n[BBOX-488] 出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；\n[BBOX-489] 7.咨询电话产科：\n[BBOX-490] ，新生儿科：0398-3118382。母乳咨询电话：\n[BBOX-491] 0398-3118618.\n[BBOX-492] 主治医师：\n[BBOX-493] 孙州\n[BBOX-494] 临床数据中心-患者360视图\n[BBOX-495] 返回患者查询\n[BBOX-496] ���者姓名\n[BBOX-497] 女 出生日\n[BBOX-498] 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-499] 就诊时间轴\n[BBOX-500] 门诊号\n[BBOX-501] 诊时间：2023-08-14 15:29:02 接诊科室：普通儿科三组（门） 接诊医生：谭真真\n[BBOX-502] 全部\n[BBOX-503] 近一月\n[BBOX-504] 近三月\n[BBOX-505] 近半年\n[BBOX-506] 近一年\n[BBOX-507] 近五年\n[BBOX-508] 门诊39 住院1\n[BBOX-509] 总览\n[BBOX-510] 就诊列表\n[BBOX-511] 2024-04-24 普通儿科一组（...\n[BBOX-512] 2024-04-19 普通儿科一组（...\n[BBOX-513] 2024-04-08 妇科门诊\n[BBOX-514] 2024-04-08 妇科一病区(门)\n[BBOX-515] 2024-01-05 妇科一病区(门)\n[BBOX-516] 2023-08-14 普通儿科三组（...\n[BBOX-517] 2023-07-06 普通儿科三组（...\n[BBOX-518] 2023-06-26 普通儿科三组（...\n[BBOX-519] 2023-05-08 普通儿科三组（...\n[BBOX-520] 2023-05-08 普通儿科一组（...\n[BBOX-521] 2023-04-18 普通儿科三组（...\n[BBOX-522] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-523] 1.\n[BBOX-524] 门诊号.\n[BBOX-525] 姓名：\n[BBOX-526] 性别：女\n[BBOX-527] 年龄：39岁\n[BBOX-528] 民族：汉族\n[BBOX-529] 身份证\n[BBOX-530] 现住址：\n[BBOX-531] 就诊类型：初诊\n[BBOX-532] 就诊科室：普通儿科三组（门）\n[BBOX-533] 就诊日期：2023-08-14 15:29\n[BBOX-534] 联系电\n[BBOX-535] 主诉：咽峡炎购药\n[BBOX-536] 现病史：咽峡炎购药\n[BBOX-537] 既往史：平素体健，无肝炎、结核类传染病史\n[BBOX-538] 过敏史：无\n[BBOX-539] 体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充\n[BBOX-540] 血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛\n[BBOX-541] 辅助检查：\n[BBOX-542] 初步印象：急性咽峡炎\n[BBOX-543] 处理意见：门诊\n[BBOX-544] 备注：\n[BBOX-545] 医师签名：谭真真\n[BBOX-546] 第1页\n[BBOX-547] 门诊病历\n[BBOX-548] 门诊号：\n[BBOX-549] 姓名\n[BBOX-550] 性别：女\n[BBOX-551] 年龄：39岁\n[BBOX-552] 民族：汉族\n[BBOX-553] 身份证号\n[BBOX-554] 现住址：\n[BBOX-555] 就诊类型：急诊\n[BBOX-556] 就诊科室：妇科一病区(门)\n[BBOX-557] 就诊日期：2024-01-05 10:32\n[BBOX-558] 联系电话\n[BBOX-559] 主诉：下腹痛2小时\n[BBOX-560] 现病史：患者月经第二天，无明显诱因出现下腹持续疼痛\n[BBOX-561] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-562] 婚育史：\n[BBOX-563] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-564] 过敏史：无\n[BBOX-565] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。\n[BBOX-566] 辅助检查：\n[BBOX-567] 初步印象：女性盆腔炎性疾病\n[BBOX-568] 处理意见：门诊治疗\n[BBOX-569] 备注：\n[BBOX-570] 医师签名：汪会芳\n[BBOX-571] 第1页\n[BBOX-572] 三门峡市中心医院门户-患者360 ×\n[BBOX-573] ← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-574] 临床数据中心-患者360视图\n[BBOX-575] 返回患者查询\n[BBOX-576] 患者姓名:\n[BBOX-577] 女 出\n[BBOX-578] 期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-579] 就诊时间轴\n[BBOX-580] 门诊号\n[BBOX-581] 就诊时间: 2024-04-08 09 44 02 接诊科室: 妇科一病区(门) 接诊医生: 权丽丽\n[BBOX-582] 全部\n[BBOX-583] 近一月\n[BBOX-584] 近三月\n[BBOX-585] 近半年\n[BBOX-586] 近一年\n[BBOX-587] 近五年\n[BBOX-588] 门诊 39 住院1\n[BBOX-589] 总览\n[BBOX-590] 就诊列表\n[BBOX-591] 2025-04-11 哮喘危重—病达(I J)\n[BBOX-592] 2025-01-06 普通儿科三组 (...\n[BBOX-593] 2024-12-30 普通儿科三组 (...\n[BBOX-594] 2024-07-05 普通儿科一组 (...\n[BBOX-595] 2024-04-24 普通儿科一组 (...\n[BBOX-596] 2024-04-19 普通儿科一组 (...\n[BBOX-597] 2024-04-08 妇科门诊\n[BBOX-598] 2024-04-08 妇科一病区(门)\n[BBOX-599] 2024-01-05 妇科一病区(门)\n[BBOX-600] 2023-08-14 普通儿科三组 (...\n[BBOX-601] 2023-07-06 普通儿科三组 (...\n[BBOX-602] 集放视图\n[BBOX-603] 诊断\n[BBOX-604] 病历文书\n[BBOX-605] 处方\n[BBOX-606] 检验\n[BBOX-607] 检查\n[BBOX-608] 处置\n[BBOX-609] 肺功能检查\n[BBOX-610] 单机报告\n[BBOX-611] 检验报告\n[BBOX-612] 门诊号:\n[BBOX-613] 姓名\n[BBOX-614] 性别: 女\n[BBOX-615] 年龄:40岁\n[BBOX-616] 民族: 汉族\n[BBOX-617] 身份证号\n[BBOX-618] 现住址:\n[BBOX-619] 就诊类型:初诊\n[BBOX-620] 就诊科室:妇科一病区(门)\n[BBOX-621] 就诊日期: 2024-04-08 09:44\n[BBOX-622] 联系电话\n[BBOX-623] 主诉: 月经期下腹间断疼痛2个月\n[BBOX-624] 现病史: 2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经\n[BBOX-625] 第3天下腹疼痛但是疼痛程度较前减轻,\n[BBOX-626] 既往史: 平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史\n[BBOX-627] 婚育史:\n[BBOX-628] 月经史: 患者平素月经规律,量中等,色正常,无痛经。\n[BBOX-629] 过敏史: 无\n[BBOX-630] 专科检查: 外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小\n[BBOX-631] 正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。\n[BBOX-632] 辅助检查:\n[BBOX-633] 初步印象: 女性盆腔炎性疾病\n[BBOX-634] 处理意见: 门诊检查\n[BBOX-635] 备注:\n[BBOX-636] 医师签名: 权丽丽\n[BBOX-637] 第1页\n[BBOX-638] 三门峡市中心医院门户-患者360 ×\n[BBOX-639] 临床数据中心-患者360视图\n[BBOX-640] 返回患者查询\n[BBOX-641] 患者姓\n[BBOX-642] 出生\n[BBOX-643] 期：2020-07-08\n[BBOX-644] 最近诊疗日期：2026-02-12\n[BBOX-645] 当前在院状态：出院\n[BBOX-646] 过敏：无\n[BBOX-647] 详情>>\n[BBOX-648] 就诊时间抽\n[BBOX-649] 1门诊号：\n[BBOX-650] 就诊时间：2024-04-08 11:32:46\n[BBOX-651] 接诊科室：妇科门诊\n[BBOX-652] 接诊医生：曲丽霞\n[BBOX-653] 全部\n[BBOX-654] 近一月\n[BBOX-655] 近三月\n[BBOX-656] 近半年\n[BBOX-657] 近一年\n[BBOX-658] 近五年\n[BBOX-659] 门诊诊39\n[BBOX-660] 住院1\n[BBOX-661] 总览\n[BBOX-662] 就诊列表\n[BBOX-663] 2025-04-11 守收厄重_病区(1)\n[BBOX-664] 2025-01-06 普通儿科三组(...\n[BBOX-665] 2024-12-30 普通儿科三组(...\n[BBOX-666] 2024-07-05 普通儿科一组(...\n[BBOX-667] 2024-04-24 普通儿科一组(...\n[BBOX-668] 2024-04-19 普通儿科一组(...\n[BBOX-669] 2024-04-08 妇科门诊\n[BBOX-670] 2024-04-08 妇科一病区(门)\n[BBOX-671] 2024-01-05 妇科一病区(门)\n[BBOX-672] 2023-08-14 普通儿科三组(...\n[BBOX-673] 2023-07-06 普通儿科三组(...\n[BBOX-674] 集成视图\n[BBOX-675] 诊断\n[BBOX-676] 病历文书\n[BBOX-677] 处方\n[BBOX-678] 检验\n[BBOX-679] 检查\n[BBOX-680] 处置\n[BBOX-681] 肺功能检查\n[BBOX-682] 单机报告\n[BBOX-683] 体检报告\n[BBOX-684] 门诊号\n[BBOX-685] 姓名\n[BBOX-686] 性别：女\n[BBOX-687] 年龄：40岁\n[BBOX-688] 民族：汉族\n[BBOX-689] 身份证号\n[BBOX-690] 现住址：\n[BBOX-691] 就诊类型：初诊\n[BBOX-692] 就诊科室：妇科门诊\n[BBOX-693] 就诊日期：2024-04-08 11:32\n[BBOX-694] 联系电话\n[BBOX-695] 主诉：月经期下腹间断疼痛2个月\n[BBOX-696] 现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经\n[BBOX-697] 第3天下腹疼痛但是疼痛程度较前减轻，\n[BBOX-698] 既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史\n[BBOX-699] 婚育史：\n[BBOX-700] 月经史：患者平素月经规律，量中等，色正常，无痛经。\n[BBOX-701] 过敏史：无\n[BBOX-702] 专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小\n[BBOX-703] 正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。\n[BBOX-704] 辅助检查：\n[BBOX-705] 初步印象：女性盆腔炎性疾病\n[BBOX-706] 处理意见：门诊检查\n[BBOX-707] 备注：\n[BBOX-708] 医师签名：\n[BBOX-709] 第1页\n[BBOX-710] <\n[BBOX-711] →\n[BBOX-712] C\n[BBOX-713] ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-714] 临床数据中心-患者360视图\n[BBOX-715] 返回患者查询\n[BBOX-716] 患者姓\n[BBOX-717] 女\n[BBOX-718] 出生日期\n[BBOX-719] 首诊日期：2020-07-08\n[BBOX-720] 最近诊疗日期：2026-02-12\n[BBOX-721] 当前在院状态：出院\n[BBOX-722] 过敏：无\n[BBOX-723] 详情>>\n[BBOX-724] 就诊时间抽\n[BBOX-725] 门诊号\n[BBOX-726] 就诊时间：2024-04-19 08.07.40\n[BBOX-727] 接诊科室：普通儿科一组(门)\n[BBOX-728] 接诊医生：李婉莹\n[BBOX-729] 全部\n[BBOX-730] 近一月\n[BBOX-731] 近三月\n[BBOX-732] 近半年\n[BBOX-733] 近一年\n[BBOX-734] 近五年\n[BBOX-735] ■ 门诊诊39\n[BBOX-736] 住院1\n[BBOX-737] 总览\n[BBOX-738] 就诊列表\n[BBOX-739] 2025-04-11 宁议危重—病区(IJ)\n[BBOX-740] 2025-01-06 普通儿科三组(...\n[BBOX-741] 2024-12-30 普通儿科三组(...\n[BBOX-742] 2024-07-05 普通儿科一组(...\n[BBOX-743] 2024-04-24 普通儿科一组(...\n[BBOX-744] 2024-04-19 普通儿科一组(...\n[BBOX-745] 2024-04-08 妇科门诊\n[BBOX-746] 2024-04-08 妇科一病区(门)\n[BBOX-747] 2024-01-05 妇科一病区(门)\n[BBOX-748] 2023-08-14 普通儿科三组(...\n[BBOX-749] 2023-07-06 普通儿科三组(...\n[BBOX-750] 集成视图\n[BBOX-751] 诊断\n[BBOX-752] 病历文书\n[BBOX-753] 处方\n[BBOX-754] 检验\n[BBOX-755] 检查\n[BBOX-756] 处置\n[BBOX-757] 肺功能检查\n[BBOX-758] 单机报告\n[BBOX-759] 体检报告\n[BBOX-760] 门诊号\n[BBOX-761] 姓\n[BBOX-762] 性别：女\n[BBOX-763] 年龄：40岁\n[BBOX-764] 民族：汉族\n[BBOX-765] 身份证号：\n[BBOX-766] 现住址：\n[BBOX-767] 就诊类型：急诊\n[BBOX-768] 就诊科室：普通儿科一组(门)\n[BBOX-769] 就诊日期：2024-04-19 08:07\n[BBOX-770] 联系电话\n[BBOX-771] 主诉：因呼吸道感染）不适要求开药\n[BBOX-772] 现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。\n[BBOX-773] 既往史：既往体质一般\n[BBOX-774] 过敏史：无\n[BBOX-775] 体格检查：神志清晰，精神一般，自主体位，查体合作\n[BBOX-776] 辅助检查：\n[BBOX-777] 初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症\n[BBOX-778] 处理意见：开立药品\n[BBOX-779] 备注：\n[BBOX-780] 医师签名：李婉莹\n[BBOX-781] 第1页\n[BBOX-782] CS 扫描全能王\n[BBOX-783] 3亿人都在用的扫描App\n[BBOX-784] 患者姓名：女\n[BBOX-785] 出生日期：\n[BBOX-786] 就诊日期：2020-07-08\n[BBOX-787] 最近诊疗日期：2026-02-12\n[BBOX-788] 当前在院状态：出院\n[BBOX-789] 过敏：无\n[BBOX-790] 详情>>\n[BBOX-791] 就诊时间：2025-04-11 14:47:07\n[BBOX-792] 接诊科室：呼吸危重二病区(门)\n[BBOX-793] 接诊医生：段竹云\n[BBOX-794] 全部\n[BBOX-795] 近一月\n[BBOX-796] 近三月\n[BBOX-797] 近半年\n[BBOX-798] 近一年\n[BBOX-799] 近五年\n[BBOX-800] 门诊39\n[BBOX-801] 住院1\n[BBOX-802] 总览\n[BBOX-803] 就诊列表\n[BBOX-804] 2025-06-23 普通儿科三组 (...\n[BBOX-805] 2025-05-09 呼吸危重二病区(门)\n[BBOX-806] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-807] 2025-04-11 呼吸危重二病区(门)\n[BBOX-808] 2025-01-06 普通儿科三组 (...\n[BBOX-809] 2024-12-30 普通儿科三组 (...\n[BBOX-810] 2024-07-05 普通儿科一组 (...\n[BBOX-811] 2024-04-24 普通儿科一组 (...\n[BBOX-812] 2024-04-19 普通儿科一组 (...\n[BBOX-813] 2024-04-08 妇科门诊\n[BBOX-814] 2024-04-08 妇科一病区(门)\n[BBOX-815] 集成视图\n[BBOX-816] 诊断\n[BBOX-817] 病历文书\n[BBOX-818] 处方\n[BBOX-819] 检验\n[BBOX-820] 检查\n[BBOX-821] 处置\n[BBOX-822] 肺功能检查\n[BBOX-823] 单机报告\n[BBOX-824] 透析治疗\n[BBOX-825] 费用\n[BBOX-826] 体检报告\n[BBOX-827] （总）诊病历\n[BBOX-828] 门诊号：\n[BBOX-829] 姓\n[BBOX-830] 性别：女\n[BBOX-831] 年龄：41岁\n[BBOX-832] 民族：汉族\n[BBOX-833] 婚姻状况：已婚\n[BBOX-834] 身份证\n[BBOX-835] 职业：专业技术人员\n[BBOX-836] 现住址：\n[BBOX-837] 就诊类型：初诊\n[BBOX-838] 就诊科室：呼吸危重二病区(门)\n[BBOX-839] 就诊日期：2025-04-11\n[BBOX-840] 14:47\n[BBOX-841] 联系电话：\n[BBOX-842] 主诉：咳嗽憋气一周\n[BBOX-843] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-844] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-845] 个人史：无吸烟史\n[BBOX-846] 过敏史：无\n[BBOX-847] 体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-848] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-849] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-850] 处理意见：坚持门诊治疗，定期复查\n[BBOX-851] 备注：\n[BBOX-852] 医师签名：段竹云\n[BBOX-853] 第1页\n[BBOX-854] 临床数据中心-患者360视图\n[BBOX-855] 返回患者查询\n[BBOX-856] 就诊时间抽\n[BBOX-857] 近五年\n[BBOX-858] 门诊39 住院1\n[BBOX-859] 就诊列表\n[BBOX-860] 2025-06-23 普通儿科三组 (...\n[BBOX-861] 2025-05-09 呼吸危重二病区(门)\n[BBOX-862] 2025-04-11 耳鼻咽喉头颈外\n[BBOX-863] 2025-04-11 呼吸危重二病区(门)\n[BBOX-864] 2025-01-06 普通儿科三组 (...\n[BBOX-865] 2024-12-30 普通儿科三组 (...\n[BBOX-866] 2024-07-05 普通儿科一组 (...\n[BBOX-867] 2024-04-24 普通儿科一组 (...\n[BBOX-868] 2024-04-19 普通儿科一组 (...\n[BBOX-869] 2024-04-08 妇科门诊\n[BBOX-870] 2024-04-08 妇科一病区(门)\n[BBOX-871] ]: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-872] 就诊时间: 2025-04-11 15:43:29 接诊科室: 耳鼻咽喉头颈外科(门) 接诊医生: 刘秀层\n[BBOX-873] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 报告\n[BBOX-874] 门诊病历\n[BBOX-875] 门诊号\n[BBOX-876] 姓名\n[BBOX-877] 性别: 女\n[BBOX-878] 年龄:41岁\n[BBOX-879] 民族: 汉族\n[BBOX-880] 婚姻状况: 已婚\n[BBOX-881] 身份证号\n[BBOX-882] 职业: 职员\n[BBOX-883] 现住址:\n[BBOX-884] 就诊类型: 初诊\n[BBOX-885] 就诊科室:耳鼻咽喉头颈外科\n[BBOX-886] 就诊日期: 2025-04-11 15:43\n[BBOX-887] 联系电\n[BBOX-888] 主诉:鼻塞流涕,咳嗽憋气1周\n[BBOX-889] 现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊\n[BBOX-890] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-891] 家族史:无家族遗传病史\n[BBOX-892] 过敏史:无\n[BBOX-893] 体格检查:鼻腔粘膜充血,水肿,水样分泌物附着\n[BBOX-894] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-895] 初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]\n[BBOX-896] 处理意见:坚持门诊治疗,定期复查\n[BBOX-897] 备注:\n[BBOX-898] 医师签名:刘秀层\n[BBOX-899] 第1页\n[BBOX-900] 三门峡市中心医院门户-患者360 ×\n[BBOX-901] ← → C ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-902] 临床数据中心-患者360视图\n[BBOX-903] 返回患者查询 患者姓名 : 女 出生日期\n[BBOX-904] 日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-905] 就诊时间轴\n[BBOX-906] 门诊号\n[BBOX-907] 就诊时间: 2025-05-09 17 00 57 接诊科室: 呼吸危重二病区(门) 接诊医生: 段竹云\n[BBOX-908] 全部 近一月 近三月 近半年 近一年\n[BBOX-909] 近五年\n[BBOX-910] ■ 门急诊39 住院1\n[BBOX-911] 总览 就诊列表\n[BBOX-912] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 体检报告\n[BBOX-913] 门诊号:\n[BBOX-914] 11(急)诊病历\n[BBOX-915] 2025-11-27 普通儿科二区(...\n[BBOX-916] 2025-11-24 普通儿科二区(...\n[BBOX-917] 2025-09-18 普通儿科二区(...\n[BBOX-918] 2025-07-11 普通儿科一组(...\n[BBOX-919] 2025-06-23 普通儿科三组(...\n[BBOX-920] 2025-05-09 呼吸危重二病区(门)\n[BBOX-921] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-922] 2025-04-11 呼吸危重二病区(门)\n[BBOX-923] 2025-01-06 普通儿科三组(...\n[BBOX-924] 2024-12-30 普通儿科三组(...\n[BBOX-925] 2024-07-05 普通儿科一组(...\n[BBOX-926] 姓名\n[BBOX-927] 性别:女\n[BBOX-928] 年龄:41岁\n[BBOX-929] 民族:汉族\n[BBOX-930] 婚姻状况:已婚\n[BBOX-931] 身份证\n[BBOX-932] 业:专业技术人员\n[BBOX-933] 现住址:\n[BBOX-934] 就诊类型:复诊\n[BBOX-935] 就诊科室:呼吸危重二病区(门)\n[BBOX-936] 就诊日期:2025-05-09\n[BBOX-937] 17:00\n[BBOX-938] 联系电话\n[BBOX-939] 主诉:咳嗽憋气一周\n[BBOX-940] 现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊\n[BBOX-941] 既往史:平素体健,无高血压、冠心病、糖尿病病史\n[BBOX-942] 个人史:无吸烟史\n[BBOX-943] 过敏史:无\n[BBOX-944] 体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音\n[BBOX-945] 辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。\n[BBOX-946] 初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]\n[BBOX-947] 处理意见:坚持门诊治疗,定期复查\n[BBOX-948] 备注:\n[BBOX-949] 医师签名:段竹云\n[BBOX-950] 第1页\n[BBOX-951] 三门峡市中心医院门户-惠睿360 ×\n[BBOX-952] ← → ① 不安全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-953] 临床数据中心-患者360视图\n[BBOX-954] 返回患者查询 患者姓名:\n[BBOX-955] 出生日期:\n[BBOX-956] 日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-957] 就诊时间轴\n[BBOX-958] 门诊号:\n[BBOX-959] 就诊时间: 2025-06-23 10:49:50 接诊科室: 普通儿科三组(门) 接诊医生: 谭真真\n[BBOX-960] 全部 近一月 近三月 近半年 近一年\n[BBOX-961] 近五年\n[BBOX-962] 门诊诊39 住院1\n[BBOX-963] 总览 就诊列表\n[BBOX-964] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-965] 2025-11-27 普通儿科二区(...\n[BBOX-966] 2025-11-24 普通儿科二区(...\n[BBOX-967] 2025-09-18 普通儿科二区(...\n[BBOX-968] 2025-07-11 普通儿科一组(...\n[BBOX-969] 2025-06-23 普通儿科三组(\n[BBOX-970] 2025-05-09 呼吸危重二病区(门)\n[BBOX-971] 2025-04-11 耳鼻咽喉头颈外\n[BBOX-972] 2025-04-11 呼吸危重二病区(门)\n[BBOX-973] 2025-01-06 普通儿科三组(...\n[BBOX-974] 2024-12-30 普通儿科三组(...\n[BBOX-975] 2024-07-05 普通儿科一组(...\n[BBOX-976] 门诊号:\n[BBOX-977] 姓名\n[BBOX-978] 性别: 女\n[BBOX-979] 年龄:41岁\n[BBOX-980] 民族: 汉族\n[BBOX-981] 婚姻状况: 小组\n[BBOX-982] 身份证号:\n[BBOX-983] 职业: 专业技术人员\n[BBOX-984] 现住址:\n[BBOX-985] 就诊类型:初诊\n[BBOX-986] 就诊科室:普通儿科三组(门)\n[BBOX-987] 就诊日期: 2025-06-23 10:49\n[BBOX-988] 联系电话\n[BBOX-989] 主诉: 呼吸道感染购药\n[BBOX-990] 现病史: 呼吸道感染购药\n[BBOX-991] 既往史: 平素体健, 无肝炎、结核类传染病史\n[BBOX-992] 过敏史: 无\n[BBOX-993] 体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充\n[BBOX-994] 血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛\n[BBOX-995] 辅助检查:\n[BBOX-996] 初步印象: 上呼吸道感染\n[BBOX-997] 处理意见: 门诊药物治疗\n[BBOX-998] 备注:\n[BBOX-999] 医师签名: 谭真真\n[BBOX-1000] 第1页\n[BBOX-1001] <->C ①不安全|192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1002] 临床数据中心-患者360视图\n[BBOX-1003] 返回患者查询 患者姓 出生日期\n[BBOX-1004] 就诊日期:2020-07-08 最近诊疗日期:2026-02-12 当前在院状态:出院 过敏:无 详情>>\n[BBOX-1005] 就诊时间始 门诊号\n[BBOX-1006] 就诊时间:2025-07-1110:02:50 接诊科室:普通儿科一组(门) 接诊医生:赵艳\n[BBOX-1007] 全部 近一月 近三月 近半年 近一年\n[BBOX-1008] 近五年\n[BBOX-1009] ■ 门急诊39 住院1\n[BBOX-1010] 总览 就诊列表\n[BBOX-1011] 2025-11-27普通儿科二区(...\n[BBOX-1012] 2025-11-24普通儿科二区(...\n[BBOX-1013] 2025-09-18普通儿科二区(...\n[BBOX-1014] 2025-07-11普通儿科一组(...\n[BBOX-1015] 2025-06-23普通儿科三组(...\n[BBOX-1016] 2025-05-09呼吸危重二病区(门)\n[BBOX-1017] 2025-04-11耳鼻咽喉头颈外...\n[BBOX-1018] 2025-04-11呼吸危重二病区(门)\n[BBOX-1019] 2025-01-06普通儿科三组(...\n[BBOX-1020] 2024-12-30普通儿科三组(...\n[BBOX-1021] 2024-07-05普通儿科一组(...\n[BBOX-1022] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 体检报告\n[BBOX-1023] 一\n[BBOX-1024] 1.\n[BBOX-1025] 病历\n[BBOX-1026] 门诊号\n[BBOX-1027] 姓名\n[BBOX-1028] 性别:女\n[BBOX-1029] 年龄:41岁\n[BBOX-1030] 民族:汉族\n[BBOX-1031] 婚姻状况:未婚\n[BBOX-1032] 身份证\n[BBOX-1033] 职业:专业技术人员\n[BBOX-1034] 现住址:\n[BBOX-1035] 就诊类型:初诊\n[BBOX-1036] 就诊科室:普通儿科一组(门)\n[BBOX-1037] 就诊日期:2025-07-1110:02\n[BBOX-1038] 联系电话\n[BBOX-1039] 主诉:呼吸道感染购药\n[BBOX-1040] 现病史:呼吸道感染购药\n[BBOX-1041] 既往史:平素体健,无肝炎、结核类传染病史\n[BBOX-1042] 过敏史:无\n[BBOX-1043] 体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充\n[BBOX-1044] 血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛\n[BBOX-1045] 辅助检查:\n[BBOX-1046] 初步印象:支气管炎\n[BBOX-1047] 处理意见:门诊药物治疗\n[BBOX-1048] 备注:\n[BBOX-1049] 医师签名:赵艳\n[BBOX-1050] 第1页\n[BBOX-1051] CS 扫描全能王\n[BBOX-1052] 3亿人都在用的扫描App\n[BBOX-1053] 临床数据中心-患者360视图\n[BBOX-1054] 返回患者查询\n[BBOX-1055] 患者姓名:\n[BBOX-1056] ：女 出生日期:\n[BBOX-1057] 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1058] 就诊时间抽\n[BBOX-1059] 门诊号:\n[BBOX-1060] 就诊时间：2025-09-18 15:22:06 接诊科室：普通儿科二区（门） 接诊医生：赵艳\n[BBOX-1061] 全部 近一月 近三月 近半年 近一年\n[BBOX-1062] 近五年\n[BBOX-1063] ■ 门诊诊39 住院1\n[BBOX-1064] 总览 就诊列表\n[BBOX-1065] 2025-12-09 普通儿科二区（...\n[BBOX-1066] 2025-12-07 普通儿科二区（...\n[BBOX-1067] 2025-12-01 普通儿科二区（...\n[BBOX-1068] 2025-11-27 普通儿科二区（...\n[BBOX-1069] 2025-11-24 普通儿科二区（...\n[BBOX-1070] 2025-09-18 普通儿科二区（...\n[BBOX-1071] 2025-07-11 普通儿科一组（...\n[BBOX-1072] 2025-06-23 普通儿科三组（...\n[BBOX-1073] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1074] 2025-04-11 耳鼻咽喉头颈外...\n[BBOX-1075] 2025-04-11 呼吸危重二病区(门)\n[BBOX-1076] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 请价治疗 费用 体检报告\n[BBOX-1077] 门诊病历\n[BBOX-1078] 门诊\n[BBOX-1079] 姓名:\n[BBOX-1080] 性别:女\n[BBOX-1081] 年龄:41岁\n[BBOX-1082] 民族:汉族\n[BBOX-1083] 婚姻状况:未婚\n[BBOX-1084] 身份证\n[BBOX-1085] 职业:职员\n[BBOX-1086] 现住址:\n[BBOX-1087] 就诊类型:初诊\n[BBOX-1088] 就诊科室:普通儿科二区(门)\n[BBOX-1089] 就诊日期:2025-09-18 15:22\n[BBOX-1090] 联系电话\n[BBOX-1091] 主诉:咽部疼痛伴眼部不适4天\n[BBOX-1092] 现病史:4天前无明显诱因出现咽部疼痛,伴鼻塞,伴眼部不适,无发热、呕吐、腹泻、皮疹等不适,病后精神、食欲欠佳,大小便正常。\n[BBOX-1093] 既往史:无特殊。\n[BBOX-1094] 过敏史:无\n[BBOX-1095] 体格检查:发育正常,营养良好,精神一般,呼吸平稳,双眼睑结膜充血,口唇红润,咽腔充血,无疱疹,双侧扁桃体I°,充血,无分泌物,双肺呼吸音清,未闻及干湿性啰音,听诊心律齐,无杂音,腹平软,无压痛、反跳痛,未触及包块,肠鸣音活跃,神经系统未见阳性体征。\n[BBOX-1096] 辅助检查:无\n[BBOX-1097] 初步印象:1.急性咽峡炎.2.急性变应性结膜炎\n[BBOX-1098] 处理意见:门诊治疗,动态观察病情变化,不适及时随诊。\n[BBOX-1099] 备注:\n[BBOX-1100] 医师签名:赵艳\n[BBOX-1101] 第1页\n[BBOX-1102] Le coo\n[BBOX-1103] 全 | 192.168.13.101/app/app/360/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1104] 临床数据中心\n[BBOX-1105] 0视图\n[BBOX-1106] 返回患者查询\n[BBOX-1107] 患者\n[BBOX-1108] 女 出生F\n[BBOX-1109] 就诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1110] 就诊时间轴\n[BBOX-1111] 门诊\n[BBOX-1112] 诊时间: 2025-12-01 15:28:03 接诊科室: 普通儿科二区(门) 接诊医生: 赵海国\n[BBOX-1113] 全季\n[BBOX-1114] 近一月\n[BBOX-1115] 近三月\n[BBOX-1116] 近半年\n[BBOX-1117] 近一年\n[BBOX-1118] 近五年\n[BBOX-1119] 门诊急诊39 住院1\n[BBOX-1120] 总览\n[BBOX-1121] 就诊列表\n[BBOX-1122] 集成视图\n[BBOX-1123] 诊断\n[BBOX-1124] 病历文书\n[BBOX-1125] 处方\n[BBOX-1126] 检验\n[BBOX-1127] 检查\n[BBOX-1128] 处置\n[BBOX-1129] 肺功能检查\n[BBOX-1130] 单机报告\n[BBOX-1131] 透析治疗\n[BBOX-1132] 费用\n[BBOX-1133] 体检报告\n[BBOX-1134] 1.1、心/诊病历\n[BBOX-1135] 门诊\n[BBOX-1136] 2026-01-15 呼吸危重三病区(门)\n[BBOX-1137] 2026-01-06 妇科一病区(门)\n[BBOX-1138] 2025-12-09 普通儿科二区(...\n[BBOX-1139] 2025-12-07 普通儿科二区(...\n[BBOX-1140] 2025-12-01 普通儿科二区(...\n[BBOX-1141] 2025-11-27 普通儿科二区(...\n[BBOX-1142] 2025-11-24 普通儿科二区(...\n[BBOX-1143] 2025-09-18 普通儿科二区(...\n[BBOX-1144] 2025-07-11 普通儿科一组(...\n[BBOX-1145] 2025-06-23 普通儿科三组(...\n[BBOX-1146] 2025-05-09 呼吸危重二病区(门)\n[BBOX-1147] 姓名:\n[BBOX-1148] 性别: 女\n[BBOX-1149] 年龄:41岁\n[BBOX-1150] 民族: 汉族\n[BBOX-1151] 婚姻状况: 未...\n[BBOX-1152] 身份证:\n[BBOX-1153] 职业: 专业技术人员\n[BBOX-1154] 现住址:\n[BBOX-1155] 就诊类型:初诊\n[BBOX-1156] 就诊科室:普通儿科二区(门)\n[BBOX-1157] 就诊日期: 2025-12-01 15:28\n[BBOX-1158] 联系电\n[BBOX-1159] 主诉: 发热半天。\n[BBOX-1160] 现病史: 半天前出现发热,最高体温38.0℃,口服药物治疗1次,无咳嗽,无喘息,无呼吸困难,无咯血,无腹泻、呕吐等。精神食欲一般,大小便正常。\n[BBOX-1161] 既往史: 无。\n[BBOX-1162] 过敏史: 无\n[BBOX-1163] 体格检查: 神志清,精神一般,呼吸浅快,咽充血,扁桃体二度大,充血,无疱疹,无脓点,双肺呼吸音清,\n[BBOX-1164] 心音有力,律齐,腹软。\n[BBOX-1165] 辅助检查:\n[BBOX-1166] 初步印象: 急性上呼吸道感染\n[BBOX-1167] 处理意见: 口服药物,动态观察,不适随诊。\n[BBOX-1168] 备注:\n[BBOX-1169] 医师签名: 赵海国\n[BBOX-1170] 第1页\n[BBOX-1171] 姓名：\n[BBOX-1172] 性别：女\n[BBOX-1173] 年龄：41岁\n[BBOX-1174] 民族：汉族\n[BBOX-1175] 婚姻状况：已婚\n[BBOX-1176] 身份证号\n[BBOX-1177] 职业：专业技术人员\n[BBOX-1178] 现住址\n[BBOX-1179] 就诊类型：初诊\n[BBOX-1180] 就诊科室：妇科一病区(门)\n[BBOX-1181] 就诊日期：2026-01-06 08:36\n[BBOX-1182] 联系电话.\n[BBOX-1183] 主诉：左下腹间断疼痛1年左右来诊\n[BBOX-1184] 现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，\n[BBOX-1185] 慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。\n[BBOX-1186] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/\n[BBOX-1187] 非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性\n[BBOX-1188] 盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状\n[BBOX-1189] 者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括\n[BBOX-1190] 药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；\n[BBOX-1191] 获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否\n[BBOX-1192] 认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊\n[BBOX-1193] 娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1194] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1195] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1196] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-\n[BBOX-1197] 28天，经期5天，经量较前不变\n[BBOX-1198] 过敏史：无\n[BBOX-1199] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：\n[BBOX-1200] 98/76mmHg\n[BBOX-1201] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究\n[BBOX-1202] 疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1203] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件\n[BBOX-1204] 区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1205] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C&-\n[BBOX-1206] 125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1207] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便\n[BBOX-1208] 黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎\n[BBOX-1209] 性疾病后遗症，慢性盆腔痛\n[BBOX-1210] 处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患\n[BBOX-1211] 绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临\n[BBOX-1212] 床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出\n[BBOX-1213] 门\n[BBOX-1214] CS 扫描全能王\n[BBOX-1215] 3亿人都在用的扫描App\n[BBOX-1216] 既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。\n[BBOX-1217] 婚育史：已婚已育，孕2产2，有性生活史\n[BBOX-1218] 手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术\n[BBOX-1219] 月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-28天，经期5天，经量较前不变\n[BBOX-1220] 过敏史：无\n[BBOX-1221] 生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：98/76mmHg\n[BBOX-1222] 体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。\n[BBOX-1223] 专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。\n[BBOX-1224] 辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。\n[BBOX-1225] 初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎性疾病后遗症，慢性盆腔痛\n[BBOX-1226] 从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患者“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选期相关检查。\n[BBOX-1227] 1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。\n[BBOX-1228] 2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。\n[BBOX-1229] 3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，筛选失败，告知受试者转为门诊常规诊疗。\n[BBOX-1230] 备注：\n[BBOX-1231] 医师签名：\n[BBOX-1232] 临床数据中心-患者360视图\n[BBOX-1233] 返回患者查询\n[BBOX-1234] 患者\n[BBOX-1235] 日期：2020-07-08\n[BBOX-1236] 最近诊疗日期：2026-02-12\n[BBOX-1237] 当前在院状态：出院\n[BBOX-1238] 过敏：无\n[BBOX-1239] 详情>>\n[BBOX-1240] 就诊时间轴\n[BBOX-1241] 门诊号\n[BBOX-1242] 时间：2026-01-15 10:56:28\n[BBOX-1243] 接诊科室：呼吸危重三病区(门)\n[BBOX-1244] 接诊医生：王辉\n[BBOX-1245] 全部\n[BBOX-1246] 近一月\n[BBOX-1247] 近三月\n[BBOX-1248] 近半年\n[BBOX-1249] 近一年\n[BBOX-1250] 近五年\n[BBOX-1251] 门诊39-住院1\n[BBOX-1252] 总览\n[BBOX-1253] 就诊列表\n[BBOX-1254] 集成视图\n[BBOX-1255] 诊断\n[BBOX-1256] 病历文书\n[BBOX-1257] 处方\n[BBOX-1258] 检验\n[BBOX-1259] 检查\n[BBOX-1260] 处置\n[BBOX-1261] 肺功能检查\n[BBOX-1262] 单机报告\n[BBOX-1263] 透析治疗\n[BBOX-1264] 费用\n[BBOX-1265] 体检报告\n[BBOX-1266] 2026-02-12 呼吸危重三病区(门)\n[BBOX-1267] 2026-01-15 呼吸危重三病区(门)\n[BBOX-1268] 2026-01-06 妇科一病区(门)\n[BBOX-1269] 2025-12-09 普通儿科二区(...\n[BBOX-1270] 2025-12-07 普通儿科二区(...\n[BBOX-1271] 2025-12-01 普通儿科二区(...\n[BBOX-1272] 2025-11-27 普通儿科二区(...\n[BBOX-1273] 2025-11-24 普通儿科二区(...\n[BBOX-1274] 2025-09-18 普通儿科二区(...\n[BBOX-1275] 2025-07-11 普通儿科一组(...\n[BBOX-1276] 2025-06-23 普通儿科三组(...\n[BBOX-1277] 门诊\n[BBOX-1278] 姓名\n[BBOX-1279] 性别：女\n[BBOX-1280] 年龄：41岁\n[BBOX-1281] 民族：汉族\n[BBOX-1282] 婚姻状况：已婚\n[BBOX-1283] 身份证号\n[BBOX-1284] 职业：其他\n[BBOX-1285] 现住址\n[BBOX-1286] 就诊类型：复诊\n[BBOX-1287] 就诊科室：呼吸危重三病区(门)\n[BBOX-1288] 就诊日期：2026-01-15\n[BBOX-1289] 10:56\n[BBOX-1290] 联系电话\n[BBOX-1291] 主诉：咳嗽憋气一周\n[BBOX-1292] 现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊\n[BBOX-1293] 既往史：平素体健，无高血压、冠心病、糖尿病病史\n[BBOX-1294] 个人史：无吸烟史\n[BBOX-1295] 过敏史：无\n[BBOX-1296] 体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音\n[BBOX-1297] 辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。\n[BBOX-1298] 初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]\n[BBOX-1299] 处理意见：坚持门诊治疗，定期复查\n[BBOX-1300] 备注\n[BBOX-1301] 医师签名：王辉\n[BBOX-1302] 第1页\n[BBOX-1303] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1304] 返回概览视图\n[BBOX-1305] 门诊号：2\n[BBOX-1306] 时间：2026-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1307] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1308] 请输入药品内容，按回车键检索\n[BBOX-1309] 查询全部\n[BBOX-1310] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1311] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国\n[BBOX-1312] 药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真\n[BBOX-1313] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真\n[BBOX-1314] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1315] 药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟\n[BBOX-1316] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟\n[BBOX-1317] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽\n[BBOX-1318] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳\n[BBOX-1319] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳\n[BBOX-1320] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳\n[BBOX-1321] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳\n[BBOX-1322] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真\n[BBOX-1323] 药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云\n[BBOX-1324] 共10页 20页\n[BBOX-1325] 1 2 3 4 > 前往 1 页\n[BBOX-1326] CS 扫描全能王\n[BBOX-1327] 3 亿人都在用的扫描App\n[BBOX-1328] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1329] 984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1330] 时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1331] 返回概览视图\n[BBOX-1332] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1333] 请输入药品内容，按回车键检索\n[BBOX-1334] 查询全部\n[BBOX-1335] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1336] 药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽\n[BBOX-1337] 药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳\n[BBOX-1338] 药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳\n[BBOX-1339] 药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳\n[BBOX-1340] 药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳\n[BBOX-1341] 药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真\n[BBOX-1342] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云\n[BBOX-1343] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云\n[BBOX-1344] 药品 醋酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层\n[BBOX-1345] 药品 鼻炎康莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1346] 药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云\n[BBOX-1347] 药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云\n[BBOX-1348] 药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真\n[BBOX-1349] 药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真\n[BBOX-1350] 共70条 20条/页 < 1 2 3 4 > 前往 1\n[BBOX-1351] /patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1352] 84-04-02\n[BBOX-1353] 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1354] 返回概览视图\n[BBOX-1355] 门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1356] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1357] 请输入药品内容, 按回车键检索\n[BBOX-1358] 查询全部\n[BBOX-1359] 类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1360] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹\n[BBOX-1361] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹\n[BBOX-1362] 药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳\n[BBOX-1363] 药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1364] 药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹\n[BBOX-1365] 药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹\n[BBOX-1366] 药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹\n[BBOX-1367] 药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1368] 药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1369] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1370] 药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1371] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1372] 共70条 20条/页 < 1 2 3 4 > 前往 2 页\n[BBOX-1373] CS 扫描全能王\n[BBOX-1374] 3亿人都在用的扫描App\n[BBOX-1375] 50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView\n[BBOX-1376] 984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>\n[BBOX-1377] 门诊\n[BBOX-1378] 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1379] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1380] 请输入药品内容,按回车键检索\n[BBOX-1381] 查询全部\n[BBOX-1382] 类型 组 药品名称[规格]\n[BBOX-1383] 药品 替硝唑氯化钠注射液\n[BBOX-1384] 药品 左氧氟沙星氯化钠注射液(选)\n[BBOX-1385] 药品 蒲地蓝消炎口服液\n[BBOX-1386] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-1387] 药品 蒲地蓝消炎口服液\n[BBOX-1388] 药品 (小儿)双黄连口服液(选)\n[BBOX-1389] 药品 地塞米松磷酸钠注射液(选)\n[BBOX-1390] 药品 5ml灭菌注射用水\n[BBOX-1391] 药品 (扑尔敏针)马来酸氯苯那敏注射液\n[BBOX-1392] 药品 消旋山莨菪碱注射液\n[BBOX-1393] 药品 头孢克肟颗粒(选)\n[BBOX-1394] 药品 (天晴速畅)吸入用布地奈德混悬液(选)\n[BBOX-1395] 药品 (大伊可新)维生素AD滴剂\n[BBOX-1396] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1397] 入\n[BBOX-1398] 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳\n[BBOX-1399] 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳\n[BBOX-1400] 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真\n[BBOX-1401] 口服 tid 12g 2 2023-07-06 20:00:14 谭真真\n[BBOX-1402] 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1403] 口服 tid 20ml 2 2023-07-06 20:00:14 谭真真\n[BBOX-1404] 外用 bid 10mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1405] 外用 bid 5ml 4 2023-06-26 15:19:59 谭真真\n[BBOX-1406] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1407] 外用 bid 20mg 2 2023-06-26 15:19:59 谭真真\n[BBOX-1408] 口服 bid 100mg 30 2023-05-08 19:56:47 陈音\n[BBOX-1409] 压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞\n[BBOX-1410] 口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞\n[BBOX-1411] 共70条 20条/页 < 1 2 3 4 > 前往 2 页\n[BBOX-1412] 返回概览视图\n[BBOX-1413] 11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森\n[BBOX-1414] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1415] 请输入药品内容,按回车键检索\n[BBOX-1416] 查询全部\n[BBOX-1417] 类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1418] 药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音\n[BBOX-1419] 药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音\n[BBOX-1420] 药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音\n[BBOX-1421] 药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音\n[BBOX-1422] 药��� 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音\n[BBOX-1423] 药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶\n[BBOX-1424] 药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国\n[BBOX-1425] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国\n[BBOX-1426] 药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚\n[BBOX-1427] 药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-1428] 药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-1429] 药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚\n[BBOX-1430] 药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚\n[BBOX-1431] 药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-1432] 药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚\n[BBOX-1433] 共70条 20条/页 < 1 2 3 4 > 前往 3 页\n[BBOX-1434] CS 扫描全能王\n[BBOX-1435] 3亿人都在用的扫描App\n[BBOX-1436] \\begin{tabular}{lllllllllll}\n[BBOX-1437] \\hline\n[BBOX-1438] 类型 & 组 & 药品名称/规格 & 用法 & 频率 & 实际用量 & 总量 & 开立时间 & 开立医师 & \\\\\n[BBOX-1439] \\hline\n[BBOX-1440] 药品 & & 乙1)盐酸氨溴索口服溶液(基) & 口服 & bid & 5ml & 1 & 2022-05-09 19.49.32 & 赵海国 & \\\\\n[BBOX-1441] 药品 & & 赖氨肌醇维B12口服溶液 & 口服 & bid & 10ml & 3 & 2022-05-09 19.49.32 & 赵海国 & \\\\\n[BBOX-1442] 药品 & & 乙0)5ml灭菌注射用水 & 外用 & bid & 20ml & 4 & 2022-05-05 09.58.24 & 李凌蔚 & \\\\\n[BBOX-1443] 药品 & & 乙1)(扑尔敏针)马来酸氯苯那敏注射液 & 外用 & bid & 20mg & 2 & 2022-05-05 09.58.24 & 李凌蔚 & \\\\\n[BBOX-1444] 药品 & & 甲)地塞米松磷酸钠注射液(基) & 外用 & bid & 10mg & 2 & 2022-05-05 09.58.24 & 李凌蔚 & \\\\\n[BBOX-1445] 药品 & & 乙1)消旋山莨菪碱注射液(基) & 外用 & bid & 20mg & 2 & 2022-05-05 09.58.24 & 李凌蔚 & \\\\\n[BBOX-1446] 药品 & & 赖氨肌醇维B12口服溶液 & 口服 & bid & 10ml & 1 & 2022-05-05 09.57.04 & 李凌蔚 & \\\\\n[BBOX-1447] 药品 & & 乙1)复合维生素B片 & 口服 & tid & 1片 & 100 & 2022-05-05 09.56.29 & 李凌蔚 & \\\\\n[BBOX-1448] 药品 & & 甲)维生素B2片(基) & 口服 & tid & 5mg & 100 & 2022-05-05 09.56.29 & 李凌蔚 & \\\\\n[BBOX-1449] 药品 & & 乙1)头孢克肟颗粒 & 口服 & bid & 50mg & 2 & 2022-05-05 09.54.38 & 李凌蔚 & \\\\\n[BBOX-1450] 药品 & & 乙1)金振口服液(基) & 口服 & bid & 10ml & 1 & 2022-05-05 09.54.38 & 李凌蔚 & \\\\\n[BBOX-1451] 药品 & & (盖克)小儿氨酚黄那敏颗粒 & 口服 & tid & 3g & 2 & 2022-04-19 16.05.18 & 陈媛 & \\\\\n[BBOX-1452] 药品 & & 乙1)美敏伪麻口服溶液 & 口服 & tid & 4ml & 1 & 2022-04-19 16.05.18 & 陈媛 & \\\\\n[BBOX-1453] 药品 & & 复方氨酚甲麻口服液 & 口服 & qid & 5ml & 1 & 2022-04-19 16.05.18 & 陈媛 & \\\\\n[BBOX-1454] \\hline\n[BBOX-1455] \\end{tabular}\n[BBOX-1456] 184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n[BBOX-1457] 返回概览视图\n[BBOX-1458] 2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n[BBOX-1459] 集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n[BBOX-1460] 请输入药品内容,按回车键检索\n[BBOX-1461] 查询全部\n[BBOX-1462] 类型 组 药品名称(规格)\n[BBOX-1463] 药品 甲)(小儿)双黄连口服液(基)\n[BBOX-1464] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-1465] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)\n[BBOX-1466] 药品 蒲地蓝消炎口服液\n[BBOX-1467] 药品 复方氨酚甲麻口服液\n[BBOX-1468] 药品 (盖克)小儿氨酚黄那敏颗粒\n[BBOX-1469] 药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)\n[BBOX-1470] 药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)\n[BBOX-1471] 药品 右旋糖酐铁颗粒\n[BBOX-1472] 药品 盐酸氨卓斯丁滴眼液\n[BBOX-1473] 用法 频率 实际用量 总量 开立时间 开立医师\n[BBOX-1474] 口服 tid 10ml 1 2022-03-26 19:51:46 谭真真\n[BBOX-1475] 口服 tid 6g 2 2022-03-26 19:51:18 谭真真\n[BBOX-1476] 口服(继续 用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真\n[BBOX-1477] 口服 bid 10ml 1 2022-03-26 19:51:18 谭真真\n[BBOX-1478] 口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-1479] 口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-1480] 口服(继续 用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴\n[BBOX-1481] 压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅\n[BBOX-1482] 口服 tid 1袋 80 2021-09-28 15:12:34 党建华\n[BBOX-1483] 滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳\n[BBOX-1484] 共70条 20条/页 < 1 2 3 4 > 前往 4 页\n[BBOX-1485] \\begin{tabular}{llllllllll}\n[BBOX-1486] 报告时间: 2026-01-06\n[BBOX-1487] \\hline\n[BBOX-1488] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 \\\\\n[BBOX-1489] \\hline\n[BBOX-1490] [WBC]白细胞数目 & & 4.28 & & 3.5~9.5 & 10^9/L & [HCT]红细胞压积 & & 37.8 & \\\\\n[BBOX-1491] [Lym\\%]淋巴细胞百分比 & & 28.4 & & 20~50 & \\% & [MCV]平均红细胞体积 & & 80.4 & $\\downarrow$ \\\\\n[BBOX-1492] [Mon\\%]单核细胞百分比 & & 4.7 & & 3~10 & \\% & [MCH]平均红细胞血红蛋白含量 & & 26.0 & $\\downarrow$ \\\\\n[BBOX-1493] [Neu\\%]中性粒细胞百分比 & & 64.4 & & 40~75 & \\% & [MCHC]平均红细胞血红蛋白浓度 & & 323 & \\\\\n[BBOX-1494] [Eos\\%]嗜酸性细胞百分比 & & 2.4 & & 0.4~8 & \\% & [RDW-CV]红细胞分布宽度变异系数 & & 15.2 & \\\\\n[BBOX-1495] [Bas\\%]嗜碱性细胞百分比 & & 0.1 & & 0.0~1.0 & \\% & [RDW-SD]红细胞分布宽度标准差 & & 43.0 & \\\\\n[BBOX-1496] [Lym\\#]淋巴细胞数目 & & 1.22 & & 1.1~3.2 & 10^9/L & [PLT]血小板数目 & & 224 & \\\\\n[BBOX-1497] [Mon\\#]单核细胞数目 & & 0.20 & & 0.1~0.6 & 10^9/L & [MPV]平均血小板体积 & & 8.0 & \\\\\n[BBOX-1498] [Neu\\#]中性粒细胞数目 & & 2.76 & & 1.8~6.3 & 10^9/L & [PDW]血小板分布宽度 & & 16.0 & \\\\\n[BBOX-1499] [Eos\\#]嗜酸性细胞数目 & & 0.10 & & 0.02~0.52 & 10^9/L & [PCT]血小板压积 & & 0.180 & \\\\\n[BBOX-1500] [Bas\\#]嗜碱性细胞数目 & & 0.00 & & 0.00~0.06 & 10^9/L & [P-LCR]大型血小板比率 & & 15.8 & \\\\\n[BBOX-1501] [RBC]红细胞数目 & & 4.70 & & 3.8~5.1 & 10^12/L & [IG\\%]未成熟粒细胞百分比 & & 0.4 & \\\\\n[BBOX-1502] [HGB]血红蛋白 & & 122 & & 115~150 & g/L & [IG\\#]未成熟粒细胞计数 & & 0.02 & \\\\\n[BBOX-1503] \\hline\n[BBOX-1504] \\end{tabular}\n[BBOX-1505] \\begin{tabular}{ccccccc}\n[BBOX-1506] 报告时间: 2026-01-06\n[BBOX-1507] \\hline\n[BBOX-1508] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1509] \\hline\n[BBOX-1510] {[}ESR{]}血沉 & & 7 & & 0~20 & mm/h \\\\\n[BBOX-1511] \\hline\n[BBOX-1512] \\end{tabular}\n[BBOX-1513] \\begin{tabular}{l l c c c c}\n[BBOX-1514] 报告时间: 2026-01-06\n[BBOX-1515] \\hline\n[BBOX-1516] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1517] \\hline\n[BBOX-1518] [TBIL]总胆红素 & & 8.5 & & 0.0~21.0 & $\\mu$mol/L \\\\\n[BBOX-1519] [DBIL]直接胆红素 & & 2.3 & & 0.0~8.0 & $\\mu$mol/L \\\\\n[BBOX-1520] [IBIL]间接胆红素 & & 6.2 & & 0.0~13.0 & $\\mu$mol/L \\\\\n[BBOX-1521] [ALT]谷丙转氨酶 & & 12.2 & & 7~40 & U/L \\\\\n[BBOX-1522] [AST]谷草转氨酶 & & 18 & & 13~35 & U/L \\\\\n[BBOX-1523] [AST/ALT]谷草/谷丙 & & 1.48 & & 0.8~1.5 & \\\\\n[BBOX-1524] [TP]总蛋白 & & 73.6 & & 65.0~85.0 & g/L \\\\\n[BBOX-1525] [ALB]白蛋白 & & 46.0 & & 40.0~55.0 & g/L \\\\\n[BBOX-1526] [GLB]球蛋白 & & 27.6 & & 20.0~40.0 & g/L \\\\\n[BBOX-1527] [A/G]白球比值 & & 1.67 & & 1.20~2.4 & \\\\\n[BBOX-1528] [GGT]谷氨酰转肽酶 & & 9.0 & & 7~45 & U/L \\\\\n[BBOX-1529] [ALP]碱性磷酸酶 & & 66 & & 40~150 & U/L \\\\\n[BBOX-1530] [Urea]尿素 & & 4.27 & & 2.6~7.5 & mmol/L \\\\\n[BBOX-1531] [CRE]肌酐 & & 49.9 & & 41~73 & $\\mu$mol/L \\\\\n[BBOX-1532] \\hline\n[BBOX-1533] \\end{tabular}\n[BBOX-1534] \\begin{tabular}{lllll}\n[BBOX-1535] 报告时间: 2026-01-06\n[BBOX-1536] \\hline\n[BBOX-1537] \\multicolumn{2}{l}{瑞图RT-F600} & \\multicolumn{3}{c}{\\textbf{医学检验科检验报告单}} \\\\\n[BBOX-1538] \\multicolumn{2}{l}{\\textbf{白带分析仪}} & & & \\\\\n[BBOX-1539] \\multicolumn{2}{l}{姓名:} & 送检科室: 妇科一病区(门) & 床号: & 样本类型: 阴道分泌物 \\\\\n[BBOX-1540] \\multicolumn{2}{l}{住院(门诊)号:} & 性别: 女 & 年龄: 41岁 & 样本状态: 正常 \\\\\n[BBOX-1541] \\multicolumn{2}{l}{检验项目: 妇科微生态} & & & \\\\\n[BBOX-1542] \\multicolumn{2}{l}{疾病诊断: 慢性盆腔痛} & & & \\\\\n[BBOX-1543] \\hline\n[BBOX-1544] \\multicolumn{5}{l}{形态学检测项目:} \\\\\n[BBOX-1545] \\multicolumn{2}{l}{细胞情况} & 结果 & 正常值范围 & 镜下所见: \\\\\n[BBOX-1546] \\multicolumn{2}{l}{清洁度} & Ⅱ & ~ ≤Ⅱ & \\\\\n[BBOX-1547] \\multicolumn{2}{l}{白细胞} & 5-15 & ≤15/HP & \\\\\n[BBOX-1548] \\multicolumn{2}{l}{红细胞} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1549] \\multicolumn{2}{l}{线索细胞} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1550] \\multicolumn{2}{l}{上皮细胞} & 10-15 & ~ 满视野 & \\\\\n[BBOX-1551] \\multicolumn{2}{l}{} & & & \\\\\n[BBOX-1552] \\multicolumn{2}{l}{病原体情况:} & & & \\\\\n[BBOX-1553] \\multicolumn{2}{l}{滴虫} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1554] \\multicolumn{2}{l}{菌丝} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1555] \\multicolumn{2}{l}{孢子} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1556] \\multicolumn{2}{l}{芽生孢子} & 未检出 & ~ 未检出 & \\\\\n[BBOX-1557] \\multicolumn{2}{l}{} & & & \\\\\n[BBOX-1558] \\multicolumn{2}{l}{菌群情况:} & & & \\\\\n[BBOX-1559] \\multicolumn{2}{l}{菌群密集度} & ++ & ~ ++ & \\\\\n[BBOX-1560] \\multicolumn{2}{l}{多样性} & + & ~ ++ & \\\\\n[BBOX-1561] \\multicolumn{2}{l}{优势菌} & G+杆菌 & ~ G阳性杆菌 & \\\\\n[BBOX-1562] \\multicolumn{2}{l}{$\\beta$-N-乙酰氨基葡萄糖苷酶(NAG)} & - & ~ - & \\\\\n[BBOX-1563] \\multicolumn{2}{l}{} & & & \\\\\n[BBOX-1564] \\multicolumn{2}{l}{功能学分析:} & & & \\\\\n[BBOX-1565] \\multicolumn{2}{l}{唾液酸苷酶} & - & ~ - & \\\\\n[BBOX-1566] \\multicolumn{2}{l}{白细胞酯酶} & - & ~ - & \\\\\n[BBOX-1567] \\multicolumn{2}{l}{胺试验} & - & ~ - & \\\\\n[BBOX-1568] \\multicolumn{2}{l}{脯氨酸氨基肽酶PIP} & - & ~ - & \\\\\n[BBOX-1569] \\multicolumn{2}{l}{过氧化氢(H2O2)} & + & ~ - & \\\\\n[BBOX-1570] \\multicolumn{2}{l}{pH值} & 3.8 & 3.8 ~ 4.5 & \\\\\n[BBOX-1571] \\multicolumn{2}{l}{Nugent评分2} & AV评分1 & & \\\\\n[BBOX-1572] \\hline\n[BBOX-1573] \\multicolumn{5}{l}{※ 备注:阴道微生态未见明显异常!} \\\\\n[BBOX-1574] \\hline\n[BBOX-1575] \\multicolumn{2}{l}{采集时间: 2026-01-06} & \\multicolumn{2}{l}{接收时间: 2026-01-06} & \\multicolumn{2}{l}{审核时间: 2026-01-06} & \\multicolumn{2}{l}{打印时间: 2026/2/26 下午} \\\\\n[BBOX-1576] \\multicolumn{2}{l}{09:15} & \\multicolumn{2}{l}{09:22} & \\multicolumn{2}{l}{10:59} & \\multicolumn{2}{l}{3:59:58} \\\\\n[BBOX-1577] \\multicolumn{2}{l}{送检医生: 权丽丽} & \\multicolumn{2}{l}{检验者: 伊原原} & \\multicolumn{2}{l}{审核者: 介倩倩} & \\multicolumn{2}{l}{打印者: 网页打印} \\\\\n[BBOX-1578] \\multicolumn{8}{l}{※本报告检查结果实行互认制度,如有疑问,请在三天内和我们联系,电} \\\\\n[BBOX-1579] \\hline\n[BBOX-1580] \\end{tabular}\n[BBOX-1581] \\begin{tabular}{cccccc}\n[BBOX-1582] 报告时间: 2026-01-06\n[BBOX-1583] \\hline\n[BBOX-1584] 英文 & 项目名称 & 结果 & 参考范围 & 单位 & \\\\\n[BBOX-1585] \\hline\n[BBOX-1586] \\multicolumn{6}{c}{[β-HCG]人绒毛膜促性腺激素 0.40} \\\\\n[BBOX-1587] \\hline\n[BBOX-1588] \\multicolumn{6}{c}{非孕期 0~2.9} \\\\\n[BBOX-1589] \\multicolumn{6}{c}{0.2-1周 5~50} \\\\\n[BBOX-1590] \\multicolumn{6}{c}{1-2周 50~500} \\\\\n[BBOX-1591] \\multicolumn{6}{c}{2-3周 100~5000} \\\\\n[BBOX-1592] \\multicolumn{6}{c}{3-4周 500~10000} \\\\\n[BBOX-1593] \\multicolumn{6}{c}{4-5周 1000~50000} \\\\\n[BBOX-1594] \\multicolumn{6}{c}{5-6周 10000~100000} \\\\\n[BBOX-1595] \\multicolumn{6}{c}{6-8周 15000~200000} \\\\\n[BBOX-1596] \\hline\n[BBOX-1597] \\end{tabular}\n[BBOX-1598] \\begin{tabular}{llllll}\n[BBOX-1599] 报告时间: 2026-01-06\n[BBOX-1600] \\hline\n[BBOX-1601] 采集时间: & 2026-01-06 & 接收时间: & 2026-01-06 & 审核时间: & 2026-01-06 \\\\\n[BBOX-1602] & 09:15 & & 10:03 & & 11:06 \\\\\n[BBOX-1603] 送检医生: 权丽丽 & & 检验者: & & 审核者: & \\\\\n[BBOX-1604] \\hline\n[BBOX-1605] \\end{tabular}\n[BBOX-1606] \\begin{tabular}{llllll}\n[BBOX-1607] 报告时间: 2026-01-06\n[BBOX-1608] \\hline\n[BBOX-1609] 打印时间: & 2026/2/26 下午 & 打印者: & 网页打印 & & \\\\\n[BBOX-1610] & 4:00:10 & & & & \\\\\n[BBOX-1611] \\hline\n[BBOX-1612] \\end{tabular}\n[BBOX-1613] \\begin{tabular}{ccccccc}\n[BBOX-1614] 报告时间: 2026-01-06\n[BBOX-1615] \\hline\n[BBOX-1616] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1617] \\hline\n[BBOX-1618] [OV125Ag]CA-125 & & 59.70 & $\\uparrow$ & 0.00~35.00 & U/ml \\\\\n[BBOX-1619] \\hline\n[BBOX-1620] \\end{tabular}\n[BBOX-1621] \\begin{tabular}{ccccccccc}\n[BBOX-1622] 报告时间: 2026-01-06\n[BBOX-1623] \\hline\n[BBOX-1624] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1625] \\hline\n[BBOX-1626] [颜色]颜色 & & 黄色 & & 清 & & [尿酸结晶]尿酸结晶 & & 0 & & 0~15 & 个/ul \\\\\n[BBOX-1627] [浊度]浊度 & & 清亮 & & 清 & & [草酸钙结晶]草酸钙结晶 & & 0 & & 0~30 & 个/ul \\\\\n[BBOX-1628] [GLU]葡萄糖 & & - & & 阴性 & & [上皮细胞]上皮细胞 & & 14 & & 0~20 & 个/ul \\\\\n[BBOX-1629] [BLD]潜血 & & - & & 阴性 & & [粘液丝]粘液丝 & & 5 & & 0~20 & 个/ul \\\\\n[BBOX-1630] [LEU]白细胞 & & 2+ & & 阴性 & & [酵母菌]酵母菌 & & 6 & $\\uparrow$ & 0~0 & 个/ul \\\\\n[BBOX-1631] [PRO]蛋白质 & & - & & 阴性 & & [透明管型]透明管型 & & 0 & & 0~1 & 个/ul \\\\\n[BBOX-1632] [NIT]亚硝酸盐 & & + & & 阴性 & & [颗粒管型]颗粒管型 & & 0 & & 0~0 & 个/ul \\\\\n[BBOX-1633] [URO]尿胆素原 & & - & & 阴性 & & [小圆上皮]小圆上皮 & & 0 & & 0~3 & 个/ul \\\\\n[BBOX-1634] [BIL]胆红素 & & - & & 阴性 & & [其他管型]其他管型 & & 0 & & 0~0 & 个/ul \\\\\n[BBOX-1635] [KET]酮体 & & - & & 阴性 & & [其他上皮]其他上皮 & & 0 & & 0~10 & 个/ul \\\\\n[BBOX-1636] [Vc]维生素C & & - & & - & & [异常红细胞]异常红细胞 & & 0 & & 0~5 & 个/ul \\\\\n[BBOX-1637] [pH]酸碱性 & & 6.0 & & 5.0~8.5 & & [细菌]细菌 & & 1072 & $\\uparrow$ & 0~50 & 个/ul \\\\\n[BBOX-1638] [SG]比重 & & 1.020 & & 1.010~ & & [尿沉渣镜检]尿沉渣镜检 & & : & & & \\\\\n[BBOX-1639] [红细胞]红细胞 & & 0 & & 0~5 & 个/ul & [白细胞]白细胞 & & +++/HP & & $\\le$5/HP & \\\\\n[BBOX-1640] [白细胞]白细胞 & & 218 & $\\uparrow$ & 0~7 & 个/ul & [红细胞]红细胞 & & 未查见 & & $\\le$3/HP & \\\\\n[BBOX-1641] \\hline\n[BBOX-1642] \\end{tabular}\n[BBOX-1643] \\begin{tabular}{ccccccl}\n[BBOX-1644] 报告时间: 2026-01-15\n[BBOX-1645] \\hline\n[BBOX-1646] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1647] \\hline\n[BBOX-1648] {[}PT{]}凝血酶原时间 & & 11.0 & & 9.4~12.5 & s \\\\\n[BBOX-1649] {[}INR{]}国际标准化比例 & & 0.98 & & 0.8~1.2 & INR \\\\\n[BBOX-1650] {[}HDD{]}凝血酶原活动度 & & 103.00 & & 70~130 & \\% \\\\\n[BBOX-1651] {[}APTT{]}部分凝血活酶时间(胶质硅) & & 33.7 & & 25.1~36.5 & s \\\\\n[BBOX-1652] {[}Fib{]}纤维蛋白原 & & 2.65 & & 2.00~4.00 & g/L \\\\\n[BBOX-1653] {[}TT{]}凝血酶时间 & & 15.1 & & 10.3~16.6 & s \\\\\n[BBOX-1654] \\hline\n[BBOX-1655] \\end{tabular}\n[BBOX-1656] \\begin{tabular}{ccccccccc}\n[BBOX-1657] 报告时间: 2026-01-15\n[BBOX-1658] \\hline\n[BBOX-1659] 英文 & 项���名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1660] \\hline\n[BBOX-1661] {[}WBC{]}白细胞数目 & & 4.20 & & 3.5~9.5 & 10^9/L & {[}HCT{]}红细胞压积 & & 38.3 & & 35~45 & \\% \\\\\n[BBOX-1662] {[}Lym\\%{]}淋巴细胞百分比 & & 28.6 & & 20~50 & \\% & {[}MCV{]}平均红细胞体积 & & 81.3 & $\\downarrow$ & 82~100 & fL \\\\\n[BBOX-1663] {[}Mon\\%{]}单核细胞百分比 & & 5.0 & & 3~10 & \\% & {[}MCH{]}平均红细胞血红蛋白含量 & & 25.6 & $\\downarrow$ & 27~34 & pg \\\\\n[BBOX-1664] {[}Neu\\%{]}中性粒细胞百分比 & & 64.5 & & 40~75 & \\% & {[}MCHC{]}平均红细胞血红蛋白浓度 & & 313 & $\\downarrow$ & 316~354 & g/L \\\\\n[BBOX-1665] {[}Eos\\%{]}嗜酸性细胞百分比 & & 1.7 & & 0.4~8 & \\% & {[}RDW-CV{]}红细胞分布宽度变异系数 & & 14.9 & & 11~16 & \\% \\\\\n[BBOX-1666] {[}Bas\\%{]}嗜碱性细胞百分比 & & 0.2 & & 0.0~1.0 & \\% & {[}RDW-SD{]}红细胞分布宽度标准差 & & 43.2 & & 35.0~56.0 & fL \\\\\n[BBOX-1667] {[}Lym\\# {]}淋巴细胞数目 & & 1.20 & & 1.1~3.2 & 10^9/L & {[}PLT{]}血小板数目 & & 288 & & 125~350 & 10^9/L \\\\\n[BBOX-1668] {[}Mon\\# {]}单核细胞数目 & & 0.21 & & 0.1~0.6 & 10^9/L & {[}MPV{]}平均血小板体积 & & 9.0 & & 6.5~12 & fL \\\\\n[BBOX-1669] {[}Neu\\# {]}中性粒细胞数目 & & 2.71 & & 1.8~6.3 & 10^9/L & {[}PDW{]}血小板分布宽度 & & 15.6 & & 9~17 & fL \\\\\n[BBOX-1670] {[}Eos\\# {]}嗜酸性细胞数目 & & 0.07 & & 0.02~0.52 & 10^9/L & {[}PCT{]}血小板压积 & & 0.258 & & 0.108~ & \\% \\\\\n[BBOX-1671] {[}Bas\\# {]}嗜碱性细胞数目 & & 0.01 & & 0.00~0.06 & 10^9/L & {[}P-LCR{]}大型血小板比率 & & 19.3 & & 11~45 & \\% \\\\\n[BBOX-1672] {[}RBC{]}红细胞数目 & & 4.71 & & 3.8~5.1 & 10^12/L & {[}IG\\%{]}未成熟粒细胞百分比 & & 0.1 & & 0.0~0.6 & \\% \\\\\n[BBOX-1673] {[}HGB{]}血红蛋白 & & 120 & & 115~150 & g/L & {[}IG\\# {]}未成熟粒细胞计数 & & 0.00 & & 0.00~0.06 & 10^9/L \\\\\n[BBOX-1674] \\hline\n[BBOX-1675] \\end{tabular}\n[BBOX-1676] \\begin{tabular}{ccccccccc}\n[BBOX-1677] 报告时间: 2026-01-15\n[BBOX-1678] \\hline\n[BBOX-1679] \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} & \\textbf{英文} & \\textbf{项目名称} & \\textbf{结果} & \\textbf{提示} & \\textbf{参考范围} & \\textbf{单位} \\\\\n[BBOX-1680] \\hline\n[BBOX-1681] {[TBIL]}总胆红素 & & 8.7 & & 0.0~21.0 & \\textmu mol/L & {[Cl]}氯 & & 105 & & 99~110 & mmol/L \\\\\n[BBOX-1682] {[DBIL]}直接胆红素 & & 3.5 & & 0.0~8.0 & \\textmu mol/L & {[Ca]}钙 & & 2.38 & & 2.11~2.52 & mmol/L \\\\\n[BBOX-1683] {[IBIL]}间接胆红素 & & 5.2 & & 0.0~13.0 & \\textmu mol/L & {[CO2cp]}二氧化碳结合力 & & 27.6 & & 21.0~31.0 & mmol/L \\\\\n[BBOX-1684] {[ALT]}谷丙转氨酶 & & 7.0 & & 7~40 & U/L & {[m-AST]}谷草转氨酶线粒体同工酶 & & 2.0 & & 0~18 & U/L \\\\\n[BBOX-1685] {[AST]}谷草转氨酶 & & 15 & & 13~35 & U/L & {[CK]}肌酸激酶 & & 37 & & 24~200 & U/L \\\\\n[BBOX-1686] {[AST/ALT]}谷草/谷丙 & 2.14 & \\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\textup{\\text\n[BBOX-1687] \\begin{tabular}{ccccccccc}\n[BBOX-1688] 报告时间: 2026-01-15\n[BBOX-1689] \\hline\n[BBOX-1690] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 & 英文 & 项目名称 & 结果 \\\\\n[BBOX-1691] \\hline\n[BBOX-1692] [颜色]颜色 & 黄色 & & & 黄、淡黄 & & [SG]尿比重 & 1.020 & 1.003~ \\\\\n[BBOX-1693] [浊度]浊度 & 清亮 & & & 清 & & [VC]维生素C & 0.0 & - \\\\\n[BBOX-1694] [GLU]葡萄糖 & - & & & - & & [WBC]白细胞 & 28.00 & 0~28 \\\\\n[BBOX-1695] [NQX]尿潜血 & - & & & - & mg/l & [RBC]红细胞 & 6.00 & 0~17 \\\\\n[BBOX-1696] [LEU]白细胞 & - & & & - & & [粘液丝]粘液丝 & 11 & 0~28 \\\\\n[BBOX-1697] [PRO]尿蛋白 & - & & & - & & [结晶]结晶 & 0.0 & 0~28 \\\\\n[BBOX-1698] [NIT]亚硝酸盐 & + & & & - & & [管型]管型 & 0 & 0~2 \\\\\n[BBOX-1699] [URO]尿胆原 & - & & & - & & [EC]上皮细胞 & 39.00 & 0~34 \\\\\n[BBOX-1700] [BIL]胆红素 & - & & & - & & [BACT细菌]细菌 & 163.00 & 0~7 \\\\\n[BBOX-1701] [KET]尿酮体 & - & & & - & & [BYST真菌]真菌 & 0 & 0~1 \\\\\n[BBOX-1702] [pH]pH值 & 6.0 & & & 4.5~8.0 & & & & \\\\\n[BBOX-1703] \\hline\n[BBOX-1704] \\end{tabular}\n[BBOX-1705] \\begin{tabular}{ccccccc}\n[BBOX-1706] 报告时间: 2026-01-15\n[BBOX-1707] \\hline\n[BBOX-1708] 英文 & 项目名称 & 结果 & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1709] \\hline\n[BBOX-1710] [FT3]游离三碘甲状腺原氨酸 & & 3.11 & & 2.14~4.21 & pg/mL \\\\\n[BBOX-1711] [FR T4]游离甲状腺素 & & 0.76 & & 0.61~1.12 & ng/dL \\\\\n[BBOX-1712] [fTSH3]超敏促甲状腺素 & & 1.350 & & 0.560~5.910 & uIU/ml \\\\\n[BBOX-1713] \\hline\n[BBOX-1714] \\end{tabular}\n[BBOX-1715] \\begin{tabular}{ccccccc}\n[BBOX-1716] 报告时间: 2026-01-15\n[BBOX-1717] \\hline\n[BBOX-1718] 英文 & 项目名称 & 结果 & SCO & 提示 & 参考范围 & 单位 \\\\\n[BBOX-1719] \\hline\n[BBOX-1720] {[}HBsAg{]}乙肝表面抗原(酶免法) & 阴性 & 0.04 & 阴性 & s/co & & \\\\\n[BBOX-1721] {[}抗-HCV{]}丙肝抗体(酶免法) & 阴性 & 0.15 & 阴性 & s/co & & \\\\\n[BBOX-1722] {[}抗-HIV{]}人免疫缺陷病毒抗体(酶免法) & 阴性 & 0.06 & 阴性 & s/co & & \\\\\n[BBOX-1723] {[}TP-Ab{]}梅毒螺旋体抗体(酶免法) & 阴性 & 0.07 & 阴性 & s/co & & \\\\\n[BBOX-1724] \\hline\n[BBOX-1725] \\end{tabular}\n[BBOX-1726] 处方笺\n[BBOX-1727] 4970401\n[BBOX-1728] 姓名：\n[BBOX-1729] 性别：□男 □女 年龄：60岁\n[BBOX-1730] 科别： 费别： 电话/住址：\n[BBOX-1731] 过敏史：无 开具日期：2021年2月16日\n[BBOX-1732] 临床诊断：支气管哮喘\n[BBOX-1733] Rp\n[BBOX-1734] 复方丙酸倍氯米松气雾剂 20g\n[BBOX-1735] 用法：二天喷一次，3.\n[BBOX-1736] 审核： 调配： 医师：\n[BBOX-1737] 核对： 发药： 金额："
  }
]
2026-08-05 04:14:14,121 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:14:14,121 INFO     29 [qwen-vl-text] LLM output (len=680):
{
  "encounter_date": "2025-09-02",
  "prescription_type": "门诊处方",
  "prescriber": "杨沂",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": "舒宁安",
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "每天一次",
      "route": "口服",
      "duration_days": null,
      "quantity": "3盒",
      "notes": "睡前口服"
    }
  ]
}
2026-08-05 04:14:14,121 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-02]
2026-08-05 04:14:14,123 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1055779, prompt_len=934
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共21行）
["2/4", "25/09/02 14:58", "普通", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "孟鲁司特钠片【舒宁安】乙", "超量说明:", "【10mg*5片】", "(4.96元/盒)", "3盒", "用法用量:每次10mg,睡前口服,每天一次", "医师:杨沂发药:修泉涌配药:沈瑶", "vivo X80 · ZEISS", "计:208.48/208.48", "第1页/共1页"]

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
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord API raw response (len=1183):
[
	{"text": "2/4", "bbox": [471, 62, 525, 77]},
	{"text": "25/09/02 14:58", "bbox": [307, 350, 418, 359]},
	{"text": "普通", "bbox": [458, 350, 489, 359]},
	{"text": "科", "bbox": [314, 447, 330, 459]},
	{"text": "室:呼吸与危重症一门诊", "bbox": [360, 447, 519, 459]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [309, 464, 469, 473]},
	{"text": "Rp", "bbox": [306, 479, 323, 489]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [307, 502, 594, 513]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [326, 518, 552, 528]},
	{"text": "1盒", "bbox": [594, 518, 614, 528]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [328, 532, 540, 543]},
	{"text": "孟鲁司特钠片【舒宁安】乙", "bbox": [307, 547, 476, 558]},
	{"text": "超量说明:", "bbox": [514, 547, 572, 558]},
	{"text": "【10mg*5片】", "bbox": [326, 563, 397, 573]},
	{"text": "(4.96元/盒)", "bbox": [468, 563, 538, 573]},
	{"text": "3盒", "bbox": [592, 563, 612, 573]},
	{"text": "用法用量:每次10mg,睡前口服,每天一次", "bbox": [328, 577, 560, 588]},
	{"text": "医师:杨沂发药:修泉涌配药:沈瑶", "bbox": [315, 757, 511, 768]},
	{"text": "vivo X80 · ZEISS", "bbox": [199, 769, 361, 781]},
	{"text": "计:208.48/208.48", "bbox": [360, 775, 460, 784]},
	{"text": "第1页/共1页", "bbox": [482, 775, 553, 785]}
]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord API: raw_items=21, valid_items=21, elapsed=6.1s
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[0]: text=2/4, bbox=[471, 62, 525, 77]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[1]: text=25/09/02 14:58, bbox=[307, 350, 418, 359]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[2]: text=普通, bbox=[458, 350, 489, 359]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[3]: text=科, bbox=[314, 447, 330, 459]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[4]: text=室:呼吸与危重症一门诊, bbox=[360, 447, 519, 459]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[5]: text=诊断:(J45.900x001)支气管哮喘, bbox=[309, 464, 469, 473]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[6]: text=Rp, bbox=[306, 479, 323, 489]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[7]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[307, 502, 594, 513]
2026-08-05 04:14:20,189 INFO     29 [qwen-vl-text] coord item[8]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[326, 518, 552, 528]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[9]: text=1盒, bbox=[594, 518, 614, 528]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[10]: text=用法用量:每次300ug,吸入,每天二次, bbox=[328, 532, 540, 543]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[11]: text=孟鲁司特钠片【舒宁安】乙, bbox=[307, 547, 476, 558]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[12]: text=超量说明:, bbox=[514, 547, 572, 558]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[13]: text=【10mg*5片】, bbox=[326, 563, 397, 573]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[14]: text=(4.96元/盒), bbox=[468, 563, 538, 573]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[15]: text=3盒, bbox=[592, 563, 612, 573]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[16]: text=用法用量:每次10mg,睡前口服,每天一次, bbox=[328, 577, 560, 588]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[17]: text=医师:杨沂发药:修泉涌配药:沈瑶, bbox=[315, 757, 511, 768]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[18]: text=vivo X80 · ZEISS, bbox=[199, 769, 361, 781]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[19]: text=计:208.48/208.48, bbox=[360, 775, 460, 784]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] coord item[20]: text=第1页/共1页, bbox=[482, 775, 553, 785]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] page=7 — 21/21 coords, api_time=6.1s
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] new_positions (21):
[[7, 280.3768937988281, 312.52201538085933, 52.267861816406246, 64.91331225585937], [7, 182.7509689941406, 248.82705224609373, 295.0605102539062, 302.6477805175781], [7, 272.6382534179687, 291.09193432617184, 295.0605102539062, 302.6477805175781], [7, 186.91792919921875, 196.44240966796875, 376.83442309570313, 386.9507834472656], [7, 214.30081054687497, 308.9503352050781, 376.83442309570313, 386.9507834472656], [7, 183.94152905273435, 279.1863337402344, 391.16593359374997, 398.75320385742185], [7, 182.15568896484373, 192.2754494628906, 403.8113840332031, 412.2416843261719], [7, 182.7509689941406, 353.59633740234375, 423.20107470703124, 432.47440502929686], [7, 194.06128955078123, 328.59457617187496, 436.68955517578127, 445.11985546875], [7, 353.59633740234375, 365.5019379882812, 436.68955517578127, 445.11985546875], [7, 195.25184960937497, 321.4512158203125, 448.4919755859375, 457.7653059082031], [7, 182.7509689941406, 283.3532939453125, 461.1374260253906, 470.4107563476562], [7, 305.9739350585937, 340.5001767578125, 461.1374260253906, 470.4107563476562], [7, 194.06128955078123, 236.32617163085936, 474.6259064941406, 483.0562067871094], [7, 278.5910537109375, 320.26065576171874, 474.6259064941406, 483.0562067871094], [7, 352.40577734374995, 364.31137792968747, 474.6259064941406, 483.0562067871094], [7, 195.25184960937497, 333.35681640625, 486.42832690429685, 495.7016572265625], [7, 187.51320922851562, 304.1880949707031, 638.1737321777343, 647.4470625], [7, 118.46072583007812, 214.89609057617187, 648.2900925292969, 658.4064528808593], [7, 214.30081054687497, 273.82881347656246, 653.3482727050781, 660.93554296875], [7, 286.9249741210937, 329.18985620117184, 653.3482727050781, 661.7785729980469]]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=1, time=10.1s
2026-08-05 04:14:20,190 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] positions(18): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:14:20,190 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [18]
2026-08-05 04:14:20,409 INFO     29 [qwen-vl-text] page=9, rect=595x843, img=(1654x2342), dpi=200
2026-08-05 04:14:20,410 INFO     29 [qwen-vl-text] LLM extraction start, text_len=228
2026-08-05 04:14:20,410 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:20,410 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 220, \"bbox_end\": 237, \"encounter_dates\": [\"2025-11-03\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "1/1\nNO:25004949727\n4号窗口\n25/11/03 16:39\n普通\n病志号:55161248\n科\n室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【500g:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\n医师:杨昕发药:沈瑶配药:巴艺洁\nvivo X80 · ZEISS\n金额合计:193.6/193.6\n第1页/共1页",
    "role": "user"
  }
]
[92m04:14:20 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:20,411 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:25,905 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:14:25,906 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2025-11-03",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "(J45.900x001)支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-05 04:14:25,906 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-03]
2026-08-05 04:14:25,908 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1081835, prompt_len=895
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["1/1", "NO:25004949727", "4号窗口", "25/11/03 16:39", "普通", "病志号:55161248", "科", "室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【500g:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:沈瑶配药:巴艺洁", "vivo X80 · ZEISS", "金额合计:193.6/193.6", "第1页/共1页"]

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
2026-08-05 04:14:31,893 INFO     29 [qwen-vl-text] coord API raw response (len=1021):
[
	{"text": "1/1", "bbox": [476, 62, 520, 77]},
	{"text": "NO:25004949727", "bbox": [294, 295, 417, 308]},
	{"text": "4号窗口", "bbox": [462, 296, 524, 308]},
	{"text": "25/11/03 16:39", "bbox": [290, 316, 413, 328]},
	{"text": "普通", "bbox": [461, 316, 496, 328]},
	{"text": "病志号:55161248", "bbox": [290, 340, 444, 352]},
	{"text": "科", "bbox": [301, 429, 319, 442]},
	{"text": "室:呼吸与危重症一门诊", "bbox": [353, 429, 528, 442]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [297, 448, 473, 458]},
	{"text": "Rp", "bbox": [296, 465, 314, 476]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [300, 489, 607, 500]},
	{"text": "【500g:250ug/泡*60泡/(193.60元/盒)", "bbox": [323, 505, 562, 515]},
	{"text": "1盒", "bbox": [607, 505, 628, 515]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [324, 520, 550, 530]},
	{"text": "医师:杨昕发药:沈瑶配药:巴艺洁", "bbox": [309, 761, 521, 773]},
	{"text": "vivo X80 · ZEISS", "bbox": [200, 770, 361, 782]},
	{"text": "金额合计:193.6/193.6", "bbox": [310, 783, 451, 793]},
	{"text": "第1页/共1页", "bbox": [492, 781, 568, 792]}
]
2026-08-05 04:14:31,893 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.0s
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[0]: text=1/1, bbox=[476, 62, 520, 77]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[1]: text=NO:25004949727, bbox=[294, 295, 417, 308]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[2]: text=4号窗口, bbox=[462, 296, 524, 308]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[3]: text=25/11/03 16:39, bbox=[290, 316, 413, 328]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[4]: text=普通, bbox=[461, 316, 496, 328]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[5]: text=病志号:55161248, bbox=[290, 340, 444, 352]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[6]: text=科, bbox=[301, 429, 319, 442]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[7]: text=室:呼吸与危重症一门诊, bbox=[353, 429, 528, 442]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[8]: text=诊断:(J45.900x001)支气管哮喘, bbox=[297, 448, 473, 458]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[9]: text=Rp, bbox=[296, 465, 314, 476]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[300, 489, 607, 500]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[11]: text=【500g:250ug/泡*60泡/(193.60元/盒), bbox=[323, 505, 562, 515]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[12]: text=1盒, bbox=[607, 505, 628, 515]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[13]: text=用法用量:每次300ug,吸入,每天二次, bbox=[324, 520, 550, 530]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[14]: text=医师:杨昕发药:沈瑶配药:巴艺洁, bbox=[309, 761, 521, 773]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[15]: text=vivo X80 · ZEISS, bbox=[200, 770, 361, 782]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[16]: text=金额合计:193.6/193.6, bbox=[310, 783, 451, 793]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] coord item[17]: text=第1页/共1页, bbox=[492, 781, 568, 792]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] page=9 — 18/18 coords, api_time=6.0s
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] new_positions (18):
[[9, 283.3532939453125, 309.54561523437496, 52.267861816406246, 64.91331225585937], [9, 175.01232861328123, 248.23177221679686, 248.6938586425781, 259.65324902343747], [9, 275.0193735351562, 311.92673535156246, 249.536888671875, 259.65324902343747], [9, 172.63120849609373, 245.85065209960936, 266.3974892578125, 276.513849609375], [9, 274.42409350585933, 295.25889453125, 266.3974892578125, 276.513849609375], [9, 172.63120849609373, 264.3043330078125, 286.6302099609375, 296.7465703125], [9, 179.17928881835937, 189.8943293457031, 361.65988256835936, 372.6192729492187], [9, 210.13385034179686, 314.30785546874995, 361.65988256835936, 372.6192729492187], [9, 176.79816870117187, 281.56745385742187, 377.677453125, 386.10775341796875], [9, 176.20288867187497, 186.91792919921875, 392.0089636230469, 401.2822939453125], [9, 178.5840087890625, 361.3349777832031, 412.2416843261719, 421.5150146484375], [9, 192.2754494628906, 334.54737646484375, 425.73016479492185, 434.1604650878906], [9, 361.3349777832031, 373.8358583984375, 425.73016479492185, 434.1604650878906], [9, 192.87072949218748, 327.4040161132812, 438.375615234375, 446.80591552734376], [9, 183.94152905273435, 310.14089526367184, 641.5458522949218, 651.6622126464844], [9, 119.05600585937499, 214.89609057617187, 649.1331225585938, 659.2494829101562], [9, 184.53680908203123, 268.4712932128906, 660.0925129394531, 668.5228132324219], [9, 292.87777441406246, 338.119056640625, 658.4064528808593, 667.679783203125]]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] ═══ DONE ═══ 18 positions, pages=1, time=11.7s
2026-08-05 04:14:31,894 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] positions(19): [[9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:14:31,894 INFO     29 [qwen-vl-text] page grouping: [9, 10], lines per page: [1, 18]
2026-08-05 04:14:32,099 INFO     29 [qwen-vl-text] page=9, rect=595x843, img=(1654x2342), dpi=200
2026-08-05 04:14:32,296 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1654x2340), dpi=200
2026-08-05 04:14:32,297 INFO     29 [qwen-vl-text] LLM extraction start, text_len=266
2026-08-05 04:14:32,297 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:32,297 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 238, \"bbox_end\": 256, \"encounter_dates\": [\"2025-12-08\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "2025/11/05 14:51\n沈阳市第四人民医院\n处方笺\n医疗类别:市医保\nNO:25005558582\n4号窗口\n25/12/08 14:00\n普通\n病志号:55161248\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙\n【50ug:250ug/泡*60泡/(193.60元/盒)\n1盒\n用法用量:每次300ug,吸入,每天二次\nvivo X80 · ZEISS\n医师:杨昕发药:李琳配药:巴艺洁\n2025/12/31 18:28金额合计:193.6/193.6\n第1页/共1页",
    "role": "user"
  }
]
[92m04:14:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:32,298 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:35,060 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:14:35,061 INFO     29 [qwen-vl-text] LLM output (len=422):
{
  "encounter_date": "2025-12-08",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-05 04:14:35,061 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-08]
2026-08-05 04:14:35,062 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1081835, prompt_len=631
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["2025/11/05 14:51"]

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
2026-08-05 04:14:35,810 INFO     29 [qwen-vl-text] coord API raw response (len=75):
```json
[
	{"text": "2025/11/05 14:51", "bbox": [199, 790, 345, 803]}
]
```
2026-08-05 04:14:35,810 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-05 04:14:35,810 INFO     29 [qwen-vl-text] coord item[0]: text=2025/11/05 14:51, bbox=[199, 790, 345, 803]
2026-08-05 04:14:35,810 INFO     29 [qwen-vl-text] page=9 — 1/1 coords, api_time=0.7s
2026-08-05 04:14:35,813 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1719940, prompt_len=916
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:25005558582", "4号窗口", "25/12/08 14:00", "普通", "病志号:55161248", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "【50ug:250ug/泡*60泡/(193.60元/盒)", "1盒", "用法用量:每次300ug,吸入,每天二次", "vivo X80 · ZEISS", "医师:杨昕发药:李琳配药:巴艺洁", "2025/12/31 18:28金额合计:193.6/193.6", "第1页/共1页"]

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
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord API raw response (len=1042):
[
	{"text": "沈阳市第四人民医院", "bbox": [362, 190, 628, 220]},
	{"text": "处方笺", "bbox": [454, 217, 543, 241]},
	{"text": "医疗类别:市医保", "bbox": [383, 241, 552, 263]},
	{"text": "NO:25005558582", "bbox": [268, 264, 430, 285]},
	{"text": "4号窗口", "bbox": [487, 270, 567, 290]},
	{"text": "25/12/08 14:00", "bbox": [263, 294, 424, 314]},
	{"text": "普通", "bbox": [485, 298, 530, 317]},
	{"text": "病志号:55161248", "bbox": [268, 327, 463, 348]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [259, 467, 495, 483]},
	{"text": "Rp", "bbox": [254, 490, 277, 505]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙", "bbox": [255, 523, 675, 543]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒)", "bbox": [284, 546, 614, 565]},
	{"text": "1盒", "bbox": [675, 550, 704, 565]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [285, 568, 597, 587]},
	{"text": "vivo X80 · ZEISS", "bbox": [31, 892, 282, 913]},
	{"text": "医师:杨昕发药:李琳配药:巴艺洁", "bbox": [255, 900, 545, 917]},
	{"text": "2025/12/31 18:28金额合计:193.6/193.6", "bbox": [31, 927, 449, 945]},
	{"text": "第1页/共1页", "bbox": [504, 925, 605, 940]}
]
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=6.1s
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord item[0]: text=沈阳市第四人民医院, bbox=[362, 190, 628, 220]
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[454, 217, 543, 241]
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord item[2]: text=医疗类别:市医保, bbox=[383, 241, 552, 263]
2026-08-05 04:14:41,868 INFO     29 [qwen-vl-text] coord item[3]: text=NO:25005558582, bbox=[268, 264, 430, 285]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[4]: text=4号窗口, bbox=[487, 270, 567, 290]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[5]: text=25/12/08 14:00, bbox=[263, 294, 424, 314]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[6]: text=普通, bbox=[485, 298, 530, 317]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[7]: text=病志号:55161248, bbox=[268, 327, 463, 348]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[8]: text=诊断:(J45.900x001)支气管哮喘, bbox=[259, 467, 495, 483]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[9]: text=Rp, bbox=[254, 490, 277, 505]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[10]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙, bbox=[255, 523, 675, 543]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[11]: text=【50ug:250ug/泡*60泡/(193.60元/盒), bbox=[284, 546, 614, 565]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[12]: text=1盒, bbox=[675, 550, 704, 565]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[13]: text=用法用量:每次300ug,吸入,每天二次, bbox=[285, 568, 597, 587]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[14]: text=vivo X80 · ZEISS, bbox=[31, 892, 282, 913]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[15]: text=医师:杨昕发药:李琳配药:巴艺洁, bbox=[255, 900, 545, 917]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[16]: text=2025/12/31 18:28金额合计:193.6/193.6, bbox=[31, 927, 449, 945]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] coord item[17]: text=第1页/共1页, bbox=[504, 925, 605, 940]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] page=10 — 18/18 coords, api_time=6.1s
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] new_positions (19):
[[9, 118.46072583007812, 205.37161010742187, 665.9937231445313, 676.9531135253906], [10, 215.49137060546875, 373.8358583984375, 160.05410278320312, 185.32580322265625], [10, 270.2571333007812, 323.2370559082031, 182.79863317871096, 203.01599353027345], [10, 227.9922512207031, 328.59457617187496, 203.01599353027345, 221.54857385253908], [10, 159.5350478515625, 255.97041259765624, 222.3909638671875, 240.0811541748047], [10, 289.9013742675781, 337.5237766113281, 227.44530395507815, 244.2931042480469], [10, 156.5586477050781, 252.39873242187497, 247.66266430664064, 264.5104645996094], [10, 288.71081420898435, 315.49841552734375, 251.03222436523438, 267.0376346435547], [10, 159.5350478515625, 275.6146535644531, 275.4615347900391, 293.15172509765625], [10, 154.1775275878906, 294.6636145019531, 393.39613684082036, 406.87437707519535], [10, 151.20112744140624, 164.89256811523435, 412.7711071777344, 425.406957397461], [10, 151.79640747070312, 401.8140197753906, 440.56997766113284, 457.4177779541016], [10, 169.0595283203125, 365.5019379882812, 459.9449479980469, 475.95035827636724], [10, 401.8140197753906, 419.07714062499997, 463.31450805664065, 475.95035827636724], [10, 169.65480834960937, 355.38217749023437, 478.4775283203125, 494.4829385986328], [10, 18.453680908203125, 167.86896826171875, 751.4118930664063, 769.1020833740234], [10, 151.79640747070312, 324.42761596679685, 758.1510131835938, 772.4716434326173], [10, 18.453680908203125, 267.28073315429685, 780.8955435791016, 796.0585638427735], [10, 300.021134765625, 360.14441772460935, 779.2107635498047, 791.8466137695312]]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] ═══ DONE ═══ 19 positions, pages=2, time=10.0s
2026-08-05 04:14:41,869 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] positions(16): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:14:41,869 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [16]
2026-08-05 04:14:42,089 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1654x2340), dpi=200
2026-08-05 04:14:42,090 INFO     29 [qwen-vl-text] LLM extraction start, text_len=218
2026-08-05 04:14:42,090 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:42,090 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 288, \"bbox_end\": 303, \"encounter_dates\": [\"2026-01-30\"], \"department\": \"呼吸与危重症一门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "沈阳市第四人民医院\n处方笺\n医疗类别:市医保\nNO:26000513029\n3号窗口\n26/01/30 13:26\n普通\n科 室:呼吸与危重症一门诊\n诊断:(J45.900x001)支气管哮喘\nRp\n沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙\n【50ug:250ug/泡*60泡/(193.60元/盒) 1盒\n用法用量:每次300ug,吸入,每天二次\n医师:杨昕发药:李琳 配药:乔军\n金额合计:193.6/193.6\n第1页/共1页",
    "role": "user"
  }
]
[92m04:14:42 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:42,092 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:42,840 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:14:42.836+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:14:44,783 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:14:44,783 INFO     29 [qwen-vl-text] LLM output (len=435):
{
  "encounter_date": "2026-01-30",
  "prescription_type": "门诊处方",
  "prescriber": "杨昕",
  "department": "呼吸与危重症一门诊",
  "diagnosis": "(J45.900x001)支气管哮喘",
  "items": [
    {
      "drug_generic_name": "沙美特罗替卡松吸入粉雾剂",
      "drug_trade_name": "舒利迭",
      "drug_category": "西药",
      "dosage": "300ug",
      "frequency": "每天二次",
      "route": "吸入",
      "duration_days": null,
      "quantity": "1盒",
      "notes": null
    }
  ]
}
2026-08-05 04:14:44,784 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-30]
2026-08-05 04:14:44,787 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2163548, prompt_len=879
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["沈阳市第四人民医院", "处方笺", "医疗类别:市医保", "NO:26000513029", "3号窗口", "26/01/30 13:26", "普通", "科 室:呼吸与危重症一门诊", "诊断:(J45.900x001)支气管哮喘", "Rp", "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "【50ug:250ug/泡*60泡/(193.60元/盒) 1盒", "用法用量:每次300ug,吸入,每天二次", "医师:杨昕发药:李琳 配药:乔军", "金额合计:193.6/193.6", "第1页/共1页"]

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
2026-08-05 04:14:50,475 INFO     29 [qwen-vl-text] coord API raw response (len=923):
[
	{"text": "沈阳市第四人民医院", "bbox": [333, 101, 614, 128]},
	{"text": "处方笺", "bbox": [430, 124, 524, 147]},
	{"text": "医疗类别:市医保", "bbox": [356, 148, 535, 171],
	"text": "NO:26000513029", "bbox": [230, 171, 405, 192]},
	{"text": "3号窗口", "bbox": [467, 179, 552, 198]},
	{"text": "26/01/30 13:26", "bbox": [224, 202, 400, 223]},
	{"text": "普通", "bbox": [465, 208, 514, 227]},
	{"text": "科 室:呼吸与危重症一门诊", "bbox": [227, 362, 554, 389]},
	{"text": "诊断:(J45.900x001)支气管哮喘", "bbox": [220, 390, 477, 409]},
	{"text": "Rp", "bbox": [216, 415, 242, 432]},
	{"text": "沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙", "bbox": [219, 452, 667, 472]},
	{"text": "【50ug:250ug/泡*60泡/(193.60元/盒) 1盒", "bbox": [251, 477, 698, 497]},
	{"text": "用法用量:每次300ug,吸入,每天二次", "bbox": [253, 500, 584, 519]},
	{"text": "医师:杨昕发药:李琳 配药:乔军", "bbox": [215, 870, 515, 891]},
	{"text": "金额合计:193.6/193.6", "bbox": [217, 904, 428, 924]},
	{"text": "第1页/共1页", "bbox": [490, 905, 608, 924]}
]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord API: raw_items=15, valid_items=15, elapsed=5.7s
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[0]: text=沈阳市第四人民医院, bbox=[333, 101, 614, 128]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[1]: text=处方笺, bbox=[430, 124, 524, 147]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[2]: text=NO:26000513029, bbox=[230, 171, 405, 192]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[3]: text=3号窗口, bbox=[467, 179, 552, 198]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[4]: text=26/01/30 13:26, bbox=[224, 202, 400, 223]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[5]: text=普通, bbox=[465, 208, 514, 227]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[6]: text=科 室:呼吸与危重症一门诊, bbox=[227, 362, 554, 389]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[7]: text=诊断:(J45.900x001)支气管哮喘, bbox=[220, 390, 477, 409]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[8]: text=Rp, bbox=[216, 415, 242, 432]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[9]: text=沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙, bbox=[219, 452, 667, 472]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[10]: text=【50ug:250ug/泡*60泡/(193.60元/盒) 1盒, bbox=[251, 477, 698, 497]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[11]: text=用法用量:每次300ug,吸入,每天二次, bbox=[253, 500, 584, 519]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[12]: text=医师:杨昕发药:李琳 配药:乔军, bbox=[215, 870, 515, 891]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[13]: text=金额合计:193.6/193.6, bbox=[217, 904, 428, 924]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] coord item[14]: text=第1页/共1页, bbox=[490, 905, 608, 924]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] page=12 — 16/16 coords, api_time=5.7s
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] new_positions (16):
[[12, 198.22824975585937, 365.5019379882812, 85.0813914794922, 107.825921875], [12, 255.97041259765624, 311.92673535156246, 104.45636181640626, 123.83133215332032], [12, 136.91440673828123, 241.08841186523435, 144.0486925048828, 161.7388828125], [12, 277.9957736816406, 328.59457617187496, 150.78781262207033, 166.79322290039065], [12, 133.3427265625, 238.11201171874998, 170.1627829589844, 187.85297326660157], [12, 276.8052136230469, 305.9739350585937, 175.217123046875, 191.22253332519531], [12, 135.1285666503906, 329.7851362304687, 304.9451853027344, 327.6897156982422], [12, 130.9616064453125, 283.94857397460936, 328.53210571289065, 344.53751599121097], [12, 128.580486328125, 144.05776708984374, 349.5918560791016, 363.912486328125], [12, 130.36632641601562, 397.0517795410156, 380.76028662109377, 397.60808691406254], [12, 149.41528735351562, 415.50546044921873, 401.8200369873047, 418.6678372802735], [12, 150.60584741210937, 347.64353710937496, 421.19500732421875, 437.20041760253906], [12, 127.98520629882812, 306.5692150878906, 732.8793127441406, 750.5695030517578], [12, 129.17576635742188, 254.7798525390625, 761.5205732421875, 778.3683735351563], [12, 291.6872143554687, 361.9302578125, 762.362963256836, 778.3683735351563], [12, 291.6872143554687, 361.9302578125, 762.362963256836, 778.3683735351563]]
2026-08-05 04:14:50,476 INFO     29 [qwen-vl-text] ═══ DONE ═══ 16 positions, pages=1, time=8.6s
2026-08-05 04:14:50,485 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 04:14:50,485 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Prescription | outputs={"chunks": "4 items, types={'PrescriptionRecord': 4}", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:14:50,485 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 04:14:50,492 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:50,492 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m04:14:50 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:50,494 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:56,631 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:14:56,636 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 04:14:56,636 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:14:56,637 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 04:14:56,642 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:14:56,642 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 04:14:57,174 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 04:14:57,181 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 04:14:57,181 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:14:57,181 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 04:14:57,186 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:14:57,186 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 04:14:57,187 INFO     29 [qwen-vl-text] positions(24): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:14:57,187 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [17]
2026-08-05 04:14:57,482 INFO     29 [qwen-vl-text] page=1, rect=595x1290, img=(1654x3583), dpi=200
2026-08-05 04:14:57,483 INFO     29 [qwen-vl-text] LLM extraction start, text_len=752
2026-08-05 04:14:57,483 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:14:57,483 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 32, \"bbox_end\": 55, \"encounter_dates\": [\"2025-01-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2025-01-02\n\\multicolumn{7}{c}{报告单}\n出生日期: 1983-6-17 性别: 女\n住院号: 890730 年龄: 42 Years\n身高: 163 cm 测试号: 2025011002\n体重: 70 kg\n\\multicolumn{1}{c}{Time} \\multicolumn{1}{c}{预计} \\multicolumn{2}{c}{实1%(实1/预)} \\multicolumn{2}{c}{实2%(实2/预)} \\multicolumn{1}{c}{变异率}\n\\multicolumn{1}{c}{} \\multicolumn{1}{c}{} \\multicolumn{2}{c}{14:07:} \\multicolumn{2}{c}{14:26:} \\multicolumn{1}{c}{}\nFVC [L] 3.24 3.05 94.1 3.34 103.1 9.6\nFEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9\nFEV 1 % FVC [%] 69.69 74.33 6.7\nFEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7\nPEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5\nMEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4\nMEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 -6.2\nMEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0\nMMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1",
    "role": "user"
  }
]
[92m04:14:57 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:14:57,484 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:15:03,523 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:15:03,523 INFO     29 [qwen-vl-text] LLM output (len=919):
{
  "exam_date": "2025-01-02",
  "report_date": "2025-01-02",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "| Time | 预计 | 实1%(实1/预) 14:07: | 实2%(实2/预) 14:26: | 变异率 |\n|---|---|---|---|---|\n| FVC [L] | 3.24 | 3.05 (94.1) | 3.34 (103.1) | 9.6 |\n| FEV 1 [L] | 2.79 | 2.12 (76.1) | 2.48 (89.0) | 16.9 |\n| FEV 1 % FVC [%] | 69.69 | 74.33 | - | 6.7 |\n| FEV 1 % VC MAX [%] | 81.12 | 63.16 (77.9) | 72.42 (89.3) | 14.7 |\n| PEF [L/s] | 6.59 | 6.83 (103.5) | 6.59 (99.9) | -3.5 |\n| MEF 75 [L/s] | 5.80 | 3.41 (58.8) | 4.72 (81.4) | 38.4 |\n| MEF 50 [L/s] | 4.10 | 2.30 (56.2) | 2.16 (52.7) | -6.2 |\n| MEF 25 [L/s] | 1.77 | 0.45 (25.4) | 0.82 (46.2) | 82.0 |\n| MMEF 75/25 [L/s] | 3.53 | 0.95 (26.9) | 1.74 (49.2) | 83.1 |",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 04:15:03,527 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1927411, prompt_len=1427
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["报告时间: 2025-01-02", "\\multicolumn{7}{c}{报告单}", "出生日期: 1983-6-17 性别: 女", "住院号: 890730 年龄: 42 Years", "身高: 163 cm 测试号: 2025011002", "体重: 70 kg", "\\multicolumn{1}{c}{Time} \\multicolumn{1}{c}{预计} \\multicolumn{2}{c}{实1%(实1/预)} \\multicolumn{2}{c}{实2%(实2/预)} \\multicolumn{1}{c}{变异率}", "\\multicolumn{1}{c}{} \\multicolumn{1}{c}{} \\multicolumn{2}{c}{14:07:} \\multicolumn{2}{c}{14:26:} \\multicolumn{1}{c}{}", "FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6", "FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9", "FEV 1 % FVC [%] 69.69 74.33 6.7", "FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7", "PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5", "MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4", "MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 -6.2", "MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0", "MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1"]

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
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord API raw response (len=1504):
[
	{"text": "报告时间: 2025-01-02", "bbox": [488, 274, 574, 290]},
	{"text": "\\multicolumn{7}{c}{报告单}", "bbox": [488, 274, 574, 290]},
	{"text": "出生日期: 1983-6-17 性别: 女", "bbox": [488, 290, 728, 305]},
	{"text": "住院号: 890730 年龄: 42 Years", "bbox": [488, 303, 802, 316]},
	{"text": "身高: 163 cm 测试号: 2025011002", "bbox": [488, 314, 825, 327]},
	{"text": "体重: 70 kg", "bbox": [488, 325, 765, 338]},
	{"text": "\\multicolumn{1}{c}{Time} \\multicolumn{1}{c}{预计} \\multicolumn{2}{c}{实1%(实1/预)} \\multicolumn{2}{c}{实2%(实2/预)} \\multicolumn{1}{c}{变异率}", "bbox": [57, 343, 894, 364]},
	{"text": "\\multicolumn{1}{c}{} \\multicolumn{1}{c}{} \\multicolumn{2}{c}{14:07:} \\multicolumn{2}{c}{14:26:} \\multicolumn{1}{c}{}", "bbox": [426, 357, 675, 369]},
	{"text": "FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6", "bbox": [57, 384, 894, 398]},
	{"text": "FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9", "bbox": [57, 398, 894, 411]},
	{"text": "FEV 1 % FVC [%] 69.69 74.33 6.7", "bbox": [57, 411, 894, 424]},
	{"text": "FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7", "bbox": [57, 424, 894, 438]},
	{"text": "PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5", "bbox": [57, 438, 894, 451]},
	{"text": "MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4", "bbox": [57, 451, 894, 465]},
	{"text": "MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 -6.2", "bbox": [57, 465, 894, 478]},
	{"text": "MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0", "bbox": [57, 478, 894, 491]},
	{"text": "MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1", "bbox": [57, 491, 894, 505]}
]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=8.9s
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2025-01-02, bbox=[488, 274, 574, 290]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[1]: text=\multicolumn{7}{c}{报告单}, bbox=[488, 274, 574, 290]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[2]: text=出生日期: 1983-6-17 性别: 女, bbox=[488, 290, 728, 305]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[3]: text=住院号: 890730 年龄: 42 Years, bbox=[488, 303, 802, 316]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[4]: text=身高: 163 cm 测试号: 2025011002, bbox=[488, 314, 825, 327]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[5]: text=体重: 70 kg, bbox=[488, 325, 765, 338]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[6]: text=\multicolumn{1}{c}{Time} \multicolumn{1}{c}{预计} \multicolumn{2}{c}{实1%(实1/预)} \multicolumn{2}{c}{实2%(实2/预)} \multicolumn{1}{c}{变异率}, bbox=[57, 343, 894, 364]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[7]: text=\multicolumn{1}{c}{} \multicolumn{1}{c}{} \multicolumn{2}{c}{14:07:} \multicolumn{2}{c}{14:26:} \multicolumn{1}{c}{}, bbox=[426, 357, 675, 369]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[8]: text=FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6, bbox=[57, 384, 894, 398]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[9]: text=FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9, bbox=[57, 398, 894, 411]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[10]: text=FEV 1 % FVC [%] 69.69 74.33 6.7, bbox=[57, 411, 894, 424]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[11]: text=FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7, bbox=[57, 424, 894, 438]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[12]: text=PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5, bbox=[57, 438, 894, 451]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[13]: text=MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4, bbox=[57, 451, 894, 465]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[14]: text=MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 -6.2, bbox=[57, 465, 894, 478]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[15]: text=MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0, bbox=[57, 478, 894, 491]
2026-08-05 04:15:12,446 INFO     29 [qwen-vl-text] coord item[16]: text=MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1, bbox=[57, 491, 894, 505]
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] page=1 — 17/17 coords, api_time=8.9s
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] new_positions (17):
[[1, 290.49665429687496, 341.69073681640623, 353.39424267578124, 374.03040283203126], [1, 290.49665429687496, 341.69073681640623, 353.39424267578124, 374.03040283203126], [1, 290.49665429687496, 433.363861328125, 374.03040283203126, 393.3768029785156], [1, 290.49665429687496, 477.4145834960937, 390.7972829589844, 407.5641630859375], [1, 290.49665429687496, 491.10602416992185, 404.98464306640625, 421.7515231933594], [1, 290.49665429687496, 455.38922241210935, 419.1720031738281, 435.93888330078124], [1, 33.93096166992187, 532.1803461914062, 442.38768334960935, 469.4726435546875], [1, 253.58929248046874, 401.8140197753906, 460.44432348632813, 475.9214436035156], [1, 33.93096166992187, 532.1803461914062, 495.26784375, 513.3244838867188], [1, 33.93096166992187, 532.1803461914062, 513.3244838867188, 530.0913640136719], [1, 33.93096166992187, 532.1803461914062, 530.0913640136719, 546.858244140625], [1, 33.93096166992187, 532.1803461914062, 546.858244140625, 564.9148842773437], [1, 33.93096166992187, 532.1803461914062, 564.9148842773437, 581.6817644042969], [1, 33.93096166992187, 532.1803461914062, 581.6817644042969, 599.7384045410156], [1, 33.93096166992187, 532.1803461914062, 599.7384045410156, 616.5052846679688], [1, 33.93096166992187, 532.1803461914062, 616.5052846679688, 633.2721647949219], [1, 33.93096166992187, 532.1803461914062, 633.2721647949219, 651.3288049316407]]
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] ═══ DONE ═══ 17 positions, pages=1, time=15.3s
2026-08-05 04:15:12,447 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] positions(35): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 04:15:12,447 INFO     29 [qwen-vl-text] page grouping: [2], lines per page: [26]
2026-08-05 04:15:12,791 INFO     29 [qwen-vl-text] page=2, rect=595x1290, img=(1654x3583), dpi=200
2026-08-05 04:15:12,792 INFO     29 [qwen-vl-text] LLM extraction start, text_len=630
2026-08-05 04:15:12,793 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 04:15:12,793 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 56, \"bbox_end\": 90, \"encounter_dates\": [\"2025-09-02\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "报告时间: 2025-09-02\n预计 实测 % (实/预)\nDate 25-9-02\nTime 14:07:38\nVT [L] 0.50\nBF [1/min] 20.00\nMV [L/min] 10.00\nERV [L] 1.07\nVC MAX [L] 3.31 3.36 101.6\nFVC [L] 3.24 3.05 94.1\nFEV 1 [L] 2.79 2.12 76.1\nFEV 1 % FVC [%] 69.69\nFEV 1 % VC MAX [%] 81.12 63.16 77.9\nPEF [L/s] 6.59 6.83 103.5\nMEF 75 [L/s] 5.80 3.41 58.8\nMEF 50 [L/s] 4.10 2.30 56.2\nMEF 25 [L/s] 1.77 0.45 25.4\nMMEF 75/25 [L/s] 3.53 0.95 26.9\nMVV [L/min] 103.77\nFEV 1*30 [L/min] 103.77 63.70 61.4\nRV-SB [L] 1.62 2.06 127.2\nRV%TLC-SB [%] 33.24 40.20 120.9\nTLC-SB [L] 4.97 5.13 103.3\nFRC-SB [L] 2.69 2.97 110.3\nFRC%TLC-SB [%] 51.82 57.88 111.7\nDLCO SB [mmol/min/kPa] 8.54 5.51 (64.6)",
    "role": "user"
  }
]
[92m04:15:12 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:15:12,795 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 04:15:15,488 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T04:15:15.487+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 8, "lag": 0, "done": 7, "failed": 0, "current": {"6bc9a31c908211f1a3da71efcdd7cc1f": {"id": "6bc9a31c908211f1a3da71efcdd7cc1f", "doc_id": "6b8d7c20908211f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392060, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785902525374, "task_type": "dataflow", "root_trace_id": "3b3a602d2a7547bea54c2c5f4a7101b6", "root_traceparent": "00-3b3a602d2a7547bea54c2c5f4a7101b6-1163386773efdba0-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "a82d80a2908311f1a3da71efcdd7cc1f": {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 04:15:19,724 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 04:15:19,724 INFO     29 [qwen-vl-text] LLM output (len=947):
{
  "exam_date": "2025-09-02",
  "report_date": "2025-09-02",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": null,
  "department": null,
  "bed_number": null,
  "findings": "预计 实测 % (实/预)\nDate 25-9-02\nTime 14:07:38\nVT [L] 0.50\nBF [1/min] 20.00\nMV [L/min] 10.00\nERV [L] 1.07\nVC MAX [L] 3.31 3.36 101.6\nFVC [L] 3.24 3.05 94.1\nFEV 1 [L] 2.79 2.12 76.1\nFEV 1 % FVC [%] 69.69\nFEV 1 % VC MAX [%] 81.12 63.16 77.9\nPEF [L/s] 6.59 6.83 103.5\nMEF 75 [L/s] 5.80 3.41 58.8\nMEF 50 [L/s] 4.10 2.30 56.2\nMEF 25 [L/s] 1.77 0.45 25.4\nMMEF 75/25 [L/s] 3.53 0.95 26.9\nMVV [L/min] 103.77\nFEV 1*30 [L/min] 103.77 63.70 61.4\nRV-SB [L] 1.62 2.06 127.2\nRV%TLC-SB [%] 33.24 40.20 120.9\nTLC-SB [L] 4.97 5.13 103.3\nFRC-SB [L] 2.69 2.97 110.3\nFRC%TLC-SB [%] 51.82 57.88 111.7\nDLCO SB [mmol/min/kPa] 8.54 5.51 (64.6)",
  "conclusion": null,
  "physician": null,
  "reviewer": null
}
2026-08-05 04:15:19,727 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2329839, prompt_len=1321
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共26行）
["报告时间: 2025-09-02", "预计 实测 % (实/预)", "Date 25-9-02", "Time 14:07:38", "VT [L] 0.50", "BF [1/min] 20.00", "MV [L/min] 10.00", "ERV [L] 1.07", "VC MAX [L] 3.31 3.36 101.6", "FVC [L] 3.24 3.05 94.1", "FEV 1 [L] 2.79 2.12 76.1", "FEV 1 % FVC [%] 69.69", "FEV 1 % VC MAX [%] 81.12 63.16 77.9", "PEF [L/s] 6.59 6.83 103.5", "MEF 75 [L/s] 5.80 3.41 58.8", "MEF 50 [L/s] 4.10 2.30 56.2", "MEF 25 [L/s] 1.77 0.45 25.4", "MMEF 75/25 [L/s] 3.53 0.95 26.9", "MVV [L/min] 103.77", "FEV 1*30 [L/min] 103.77 63.70 61.4", "RV-SB [L] 1.62 2.06 127.2", "RV%TLC-SB [%] 33.24 40.20 120.9", "TLC-SB [L] 4.97 5.13 103.3", "FRC-SB [L] 2.69 2.97 110.3", "FRC%TLC-SB [%] 51.82 57.88 111.7", "DLCO SB [mmol/min/kPa] 8.54 5.51 (64.6)"]

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
2026-08-05 04:15:31,407 INFO     29 [qwen-vl-text] coord API raw response (len=1753):
[
	{"text": "报告时间: 2025-09-02", "bbox": [483, 326, 561, 337]},
	{"text": "预计 实测 % (实/预)", "bbox": [418, 313, 663, 326]},
	{"text": "Date 25-9-02", "bbox": [68, 326, 561, 337]},
	{"text": "Time 14:07:38", "bbox": [68, 337, 561, 349]},
	{"text": "VT [L] 0.50", "bbox": [68, 360, 465, 373]},
	{"text": "BF [1/min] 20.00", "bbox": [68, 373, 465, 385]},
	{"text": "MV [L/min] 10.00", "bbox": [68, 385, 465, 397]},
	{"text": "ERV [L] 1.07", "bbox": [68, 397, 465, 409]},
	{"text": "VC MAX [L] 3.31 3.36 101.6", "bbox": [68, 409, 667, 421]},
	{"text": "FVC [L] 3.24 3.05 94.1", "bbox": [68, 431, 667, 443]},
	{"text": "FEV 1 [L] 2.79 2.12 76.1", "bbox": [68, 443, 667, 455]},
	{"text": "FEV 1 % FVC [%] 69.69", "bbox": [68, 455, 559, 467]},
	{"text": "FEV 1 % VC MAX [%] 81.12 63.16 77.9", "bbox": [68, 467, 667, 479]},
	{"text": "PEF [L/s] 6.59 6.83 103.5", "bbox": [68, 479, 667, 491]},
	{"text": "MEF 75 [L/s] 5.80 3.41 58.8", "bbox": [68, 491, 667, 503]},
	{"text": "MEF 50 [L/s] 4.10 2.30 56.2", "bbox": [68, 503, 667, 515]},
	{"text": "MEF 25 [L/s] 1.77 0.45 25.4", "bbox": [68, 515, 667, 527]},
	{"text": "MMEF 75/25 [L/s] 3.53 0.95 26.9", "bbox": [68, 527, 667, 539]},
	{"text": "MVV [L/min] 103.77", "bbox": [68, 545, 465, 557]},
	{"text": "FEV 1*30 [L/min] 103.77 63.70 61.4", "bbox": [68, 557, 667, 569]},
	{"text": "RV-SB [L] 1.62 2.06 127.2", "bbox": [68, 580, 667, 592]},
	{"text": "RV%TLC-SB [%] 33.24 40.20 120.9", "bbox": [68, 592, 667, 604]},
	{"text": "TLC-SB [L] 4.97 5.13 103.3", "bbox": [68, 604, 667, 616]},
	{"text": "FRC-SB [L] 2.69 2.97 110.3", "bbox": [68, 616, 667, 628]},
	{"text": "FRC%TLC-SB [%] 51.82 57.88 111.7", "bbox": [68, 628, 667, 640]},
	{"text": "DLCO SB [mmol/min/kPa] 8.54 5.51 (64.6)", "bbox": [68, 640, 667, 652]}
]
2026-08-05 04:15:31,407 INFO     29 [qwen-vl-text] coord API: raw_items=26, valid_items=26, elapsed=11.7s
2026-08-05 04:15:31,407 INFO     29 [qwen-vl-text] coord item[0]: text=报告时间: 2025-09-02, bbox=[483, 326, 561, 337]
2026-08-05 04:15:31,407 INFO     29 [qwen-vl-text] coord item[1]: text=预计 实测 % (实/预), bbox=[418, 313, 663, 326]
2026-08-05 04:15:31,407 INFO     29 [qwen-vl-text] coord item[2]: text=Date 25-9-02, bbox=[68, 326, 561, 337]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[3]: text=Time 14:07:38, bbox=[68, 337, 561, 349]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[4]: text=VT [L] 0.50, bbox=[68, 360, 465, 373]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[5]: text=BF [1/min] 20.00, bbox=[68, 373, 465, 385]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[6]: text=MV [L/min] 10.00, bbox=[68, 385, 465, 397]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[7]: text=ERV [L] 1.07, bbox=[68, 397, 465, 409]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[8]: text=VC MAX [L] 3.31 3.36 101.6, bbox=[68, 409, 667, 421]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[9]: text=FVC [L] 3.24 3.05 94.1, bbox=[68, 431, 667, 443]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[10]: text=FEV 1 [L] 2.79 2.12 76.1, bbox=[68, 443, 667, 455]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[11]: text=FEV 1 % FVC [%] 69.69, bbox=[68, 455, 559, 467]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[12]: text=FEV 1 % VC MAX [%] 81.12 63.16 77.9, bbox=[68, 467, 667, 479]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[13]: text=PEF [L/s] 6.59 6.83 103.5, bbox=[68, 479, 667, 491]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[14]: text=MEF 75 [L/s] 5.80 3.41 58.8, bbox=[68, 491, 667, 503]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[15]: text=MEF 50 [L/s] 4.10 2.30 56.2, bbox=[68, 503, 667, 515]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[16]: text=MEF 25 [L/s] 1.77 0.45 25.4, bbox=[68, 515, 667, 527]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[17]: text=MMEF 75/25 [L/s] 3.53 0.95 26.9, bbox=[68, 527, 667, 539]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[18]: text=MVV [L/min] 103.77, bbox=[68, 545, 465, 557]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[19]: text=FEV 1*30 [L/min] 103.77 63.70 61.4, bbox=[68, 557, 667, 569]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[20]: text=RV-SB [L] 1.62 2.06 127.2, bbox=[68, 580, 667, 592]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[21]: text=RV%TLC-SB [%] 33.24 40.20 120.9, bbox=[68, 592, 667, 604]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[22]: text=TLC-SB [L] 4.97 5.13 103.3, bbox=[68, 604, 667, 616]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[23]: text=FRC-SB [L] 2.69 2.97 110.3, bbox=[68, 616, 667, 628]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[24]: text=FRC%TLC-SB [%] 51.82 57.88 111.7, bbox=[68, 628, 667, 640]
2026-08-05 04:15:31,408 INFO     29 [qwen-vl-text] coord item[25]: text=DLCO SB [mmol/min/kPa] 8.54 5.51 (64.6), bbox=[68, 640, 667, 652]
2026-08-05 04:15:31,409 INFO     29 [qwen-vl-text] page=2 — 26/26 coords, api_time=11.7s
2026-08-05 04:15:31,409 INFO     29 [qwen-vl-text] new_positions (26):
[[2, 287.5202541503906, 333.9520964355469, 420.46176318359375, 434.6491232910156], [2, 248.82705224609373, 394.6706594238281, 403.6948830566406, 420.46176318359375], [2, 40.4790419921875, 333.9520964355469, 420.46176318359375, 434.6491232910156], [2, 40.4790419921875, 333.9520964355469, 434.6491232910156, 450.1262434082031], [2, 40.4790419921875, 276.8052136230469, 464.313603515625, 481.08048364257814], [2, 40.4790419921875, 276.8052136230469, 481.08048364257814, 496.55760375976564], [2, 40.4790419921875, 276.8052136230469, 496.55760375976564, 512.0347238769531], [2, 40.4790419921875, 276.8052136230469, 512.0347238769531, 527.5118439941406], [2, 40.4790419921875, 397.0517795410156, 527.5118439941406, 542.9889641113281], [2, 40.4790419921875, 397.0517795410156, 555.8865642089844, 571.3636843261719], [2, 40.4790419921875, 397.0517795410156, 571.3636843261719, 586.8408044433594], [2, 40.4790419921875, 332.7615363769531, 586.8408044433594, 602.3179245605469], [2, 40.4790419921875, 397.0517795410156, 602.3179245605469, 617.7950446777344], [2, 40.4790419921875, 397.0517795410156, 617.7950446777344, 633.2721647949219], [2, 40.4790419921875, 397.0517795410156, 633.2721647949219, 648.7492849121094], [2, 40.4790419921875, 397.0517795410156, 648.7492849121094, 664.2264050292969], [2, 40.4790419921875, 397.0517795410156, 664.2264050292969, 679.7035251464844], [2, 40.4790419921875, 397.0517795410156, 679.7035251464844, 695.1806452636719], [2, 40.4790419921875, 276.8052136230469, 702.9192053222656, 718.3963254394531], [2, 40.4790419921875, 397.0517795410156, 718.3963254394531, 733.8734455566406], [2, 40.4790419921875, 397.0517795410156, 748.0608056640625, 763.53792578125], [2, 40.4790419921875, 397.0517795410156, 763.53792578125, 779.0150458984375], [2, 40.4790419921875, 397.0517795410156, 779.0150458984375, 794.492166015625], [2, 40.4790419921875, 397.0517795410156, 794.492166015625, 809.9692861328125], [2, 40.4790419921875, 397.0517795410156, 809.9692861328125, 825.44640625], [2, 40.4790419921875, 397.0517795410156, 825.44640625, 840.9235263671875]]
2026-08-05 04:15:31,409 INFO     29 [qwen-vl-text] ═══ DONE ═══ 26 positions, pages=1, time=19.0s
2026-08-05 04:15:31,417 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 04:15:31,417 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Extractor:ExaminationReport | outputs={"chunks": "2 items, types={'ExaminationReport': 2}", "html": "", "json": "304 items", "markdown": "", "text": "", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "output_format": "chunks", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "chunks_Examination": "2 items, types={'ExaminationReport': 2}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Prescription": "4 items, types={'PrescriptionRecord': 4}", "route_summary": "{\"chunks_Clinical\": 2, \"chunks_Examination\": 2, \"chunks_LabExam\": 1, \"chunks_Medication\": 3, \"chunks_Prescription\": 4}"}
2026-08-05 04:15:31,417 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 04:15:31,418 INFO     29 [ChunkMerger] Merged 12 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 4, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 2} (filtered 3 noise chunks)
2026-08-05 04:15:31,991 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 04:15:31,991 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 4, 'ExaminationReport': 2}", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf"}
2026-08-05 04:15:31,992 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 04:15:32,076 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785903057576, 'update_date': datetime.datetime(2026, 8, 5, 4, 10, 57), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 132299, 'status': '1'}
2026-08-05 04:15:32,293 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞  None  8.40  10^9/L  3.5--9.5  False    红细胞  None  4.94  10^12/L  3.8--5.1  False    血红蛋白  None  138  g/L  115--150  False    血小板  None  300  10^9/L  125--350  False    红细胞压积  None  41.30  %  35--45  False    红细胞平均体积  None  83.60  fL  82--100  False    平均血红蛋白量  None  28.00  pg  27--34  False    平均血红蛋白浓度  None  334  g/L  316--354  False    中性粒细胞比率  None  54.20  %  40--75  False    淋巴细胞比率  None  36.10  %  20--50  False    单核细胞比率  None  3.70  %  3--10  False    嗜酸性粒细胞比率  None  5.50  %  0.4--8.0  False    血小板  None  300  10^9/L  125--350  False    红细胞压积  None  41.30  %  35--45  False    红细胞平均体积  None  83.60  fL  82--100  False    平均血红蛋白量  None  28.00  pg  27--34  False    平均血红蛋白浓度  None  334  g/L  316--354  False    中性粒细胞比率  None  54.20  %  40--75  False    淋巴细胞比率  None  36.10  %  20--50  False    单核细胞比率  None  3.70  %  3--10  False    嗜酸性粒细胞比率  None  5.50  %  0.4--8.0  False    嗜碱性粒细胞比率  None  0.50  %  0--1  False    中性粒细胞数  None  4.56  10^9/L  1.8--6.3  False    淋巴细胞数  None  3.03  10^9/L  1.1--3.2  False    单核细胞数  None  0.31  10^9/L  0.10--0.60  False    嗜酸性粒细胞  None  0.46  10^9/L  0.02--0.52  False    嗜碱性粒细胞  None  0.04  10^9/L  0--0.06  False    红细胞分布宽度变异系数  None  12.9  %  11.0--16.0  False    血小板分布宽度  None  16.5  fL  8.0--18.1  False    平均血小板体积  None  10.2  fL  9--13  False    血小板压积  None  0.31  %  0.10--0.28  True    C反应蛋白  None  7.92  mg/L  0--6  True   
---
2/4
沈阳市第四人民医院
THE FOURTH PEOPLE'S HOSPITAL OF SHENYANG
门诊病历
业：现住址：辽宁省沈阳市皇姑区延河街
就诊科别：呼吸与危重症医学科门诊
就诊时间：2024-08-23 16:00
书写时间：2024-08-23 16:59
供史者：患者本人
主诉：支气管哮喘开药
现病史：患者支气管哮喘，继续巩固治疗：
沙美特罗替卡松吸入粉雾剂50ug：250ug/泡*60泡/盒，共1盒
孟鲁司特钠片
10mg*5片，共10片
每次10mg，QD
睡前口服
查体/专科查体：
辅助检查：
诊断：
支气管哮喘
处理意见：
建议患者定期复查肺功能，肺部CT.
我科随诊。
建议休息天数：0天。
患者下转：
签名：杨昕
患者签名：
门诊病历专用章
---
辽宁崇文厚德医院
门诊病历
科室：呼吸内一科门诊
姓名：
职业：
就诊日期：2025/11/08 10:11:23
主诉：反复喘息2年，加重1周
现病史：3年前开始出现反复喘息，1周前受凉后诱发喘息加重，活动后明显，自用“万
林”治疗，症状稍有改善，为求进一步诊治来我院就诊。
既往史：否认。
过敏史：{无}
体格检查：血压：128/73mmHg 两肺呼吸音粗，良妃少许喘鸣音，心音有力，律齐。
辅助检查：肺功能：中度阻塞通气功能障碍；小气道功能障碍；用药后支气管舒张试
性。
抽血回报：血常规：白细胞计数:9.13*10^9/L;中性粒细胞:48.90%.
初步诊断：1、支气管哮喘 急性发作期
处理：
1.建议舒利迭250ug日二次，规律吸入，甲泼尼龙20mg连续口服5天，建议检查肺CT。
2.1周后复诊，病情变化随诊。
医生签名：王春
王春
白
第 1 页
---
新药特药大药房总店
流水单号 10020045213
结账时间 2025-11-08 15:22:19
编号 数量 单价 金额 营业员
甲泼尼龙片（美卓乐）/4mg*30片/Pfizer It
Sr1/库存2
0310145 2 盒 34.00 68.00
合计 68.00
优惠：0.00 微信：0.00
收银 1002
银台
会员
本次积分 0.00
累计积分 0.00
此票为开发票依据，药品为特殊、
商品，售出概不退还！
---
2025/09/19 18:04
新药特药大药房总店
流水单号 10020044912
结账时间 2025-10-14 08:34:01
编号 数量 单价 金额 营业员
沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:250ug
泡/葛兰素史克(集团)/库存1
0200127 1 盒 199.00 199.00
合计 199.00
优惠:0.00 微信:0.00
收银 1002
银台
会员
本次积分 0.00
累计积分 0.00
此票为开发票依据,药品为特殊、
商品,售出概不退还!
---
新药特药大药房总店
流水单号
10020046503
结账时间
2026-01-02 18:12:29
编号
数量
单价
金额
营业员
沙美特罗替卡松吸入粉雾剂(舒利迭)/50ug:
泡/葛兰素史克(集团)/库存1
0200127
1
盒
199.00
199.00
合计
199.00
优惠:0.00
微信:0.00
收银
1002
银台
会员
本次积分
0.00
累计积分
0.00
此票为开发票依据,药品为特殊、
商品,售出概不退还!
---
2/4
25/09/02 14:58
普通
科
室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
孟鲁司特钠片【舒宁安】乙
超量说明:
【10mg*5片】
(4.96元/盒)
3盒
用法用量:每次10mg,睡前口服,每天一次
医师:杨沂发药:修泉涌配药:沈瑶
vivo X80 · ZEISS
计:208.48/208.48
第1页/共1页
---
1/1
NO:25004949727
4号窗口
25/11/03 16:39
普通
病志号:55161248
科
室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【500g:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
医师:杨昕发药:沈瑶配药:巴艺洁
vivo X80 · ZEISS
金额合计:193.6/193.6
第1页/共1页
---
2025/11/05 14:51
沈阳市第四人民医院
处方笺
医疗类别:市医保
NO:25005558582
4号窗口
25/12/08 14:00
普通
病志号:55161248
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】乙
【50ug:250ug/泡*60泡/(193.60元/盒)
1盒
用法用量:每次300ug,吸入,每天二次
vivo X80 · ZEISS
医师:杨昕发药:李琳配药:巴艺洁
2025/12/31 18:28金额合计:193.6/193.6
第1页/共1页
---
沈阳市第四人民医院
处方笺
医疗类别:市医保
NO:26000513029
3号窗口
26/01/30 13:26
普通
科 室:呼吸与危重症一门诊
诊断:(J45.900x001)支气管哮喘
Rp
沙美特罗替卡松吸入粉雾剂【(小)舒利迭】 乙
【50ug:250ug/泡*60泡/(193.60元/盒) 1盒
用法用量:每次300ug,吸入,每天二次
医师:杨昕发药:李琳 配药:乔军
金额合计:193.6/193.6
第1页/共1页
---
报告时间: 2025-01-02
\multicolumn{7}{c}{报告单}
出生日期: 1983-6-17 性别: 女
住院号: 890730 年龄: 42 Years
身高: 163 cm 测试号: 2025011002
体重: 70 kg
\multicolumn{1}{c}{Time} \multicolumn{1}{c}{预计} \multicolumn{2}{c}{实1%(实1/预)} \multicolumn{2}{c}{实2%(实2/预)} \multicolumn{1}{c}{变异率}
\multicolumn{1}{c}{} \multicolumn{1}{c}{} \multicolumn{2}{c}{14:07:} \multicolumn{2}{c}{14:26:} \multicolumn{1}{c}{}
FVC [L] 3.24 3.05 94.1 3.34 103.1 9.6
FEV 1 [L] 2.79 2.12 76.1 2.48 89.0 16.9
FEV 1 % FVC [%] 69.69 74.33 6.7
FEV 1 % VC MAX [%] 81.12 63.16 77.9 72.42 89.3 14.7
PEF [L/s] 6.59 6.83 103.5 6.59 99.9 -3.5
MEF 75 [L/s] 5.80 3.41 58.8 4.72 81.4 38.4
MEF 50 [L/s] 4.10 2.30 56.2 2.16 52.7 -6.2
MEF 25 [L/s] 1.77 0.45 25.4 0.82 46.2 82.0
MMEF 75/25 [L/s] 3.53 0.95 26.9 1.74 49.2 83.1
---
报告时间: 2025-09-02
预计 实测 % (实/预)
Date 25-9-02
Time 14:07:38
VT [L] 0.50
BF [1/min] 20.00
MV [L/min] 10.00
ERV [L] 1.07
VC MAX [L] 3.31 3.36 101.6
FVC [L] 3.24 3.05 94.1
FEV 1 [L] 2.79 2.12 76.1
FEV 1 % FVC [%] 69.69
FEV 1 % VC MAX [%] 81.12 63.16 77.9
PEF [L/s] 6.59 6.83 103.5
MEF 75 [L/s] 5.80 3.41 58.8
MEF 50 [L/s] 4.10 2.30 56.2
MEF 25 [L/s] 1.77 0.45 25.4
MMEF 75/25 [L/s] 3.53 0.95 26.9
MVV [L/min] 103.77
FEV 1*30 [L/min] 103.77 63.70 61.4
RV-SB [L] 1.62 2.06 127.2
RV%TLC-SB [%] 33.24 40.20 120.9
TLC-SB [L] 4.97 5.13 103.3
FRC-SB [L] 2.69 2.97 110.3
FRC%TLC-SB [%] 51.82 57.88 111.7
DLCO SB [mmol/min/kPa] 8.54 5.51 (64.6)
2026-08-05 04:15:32,818 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 04:15:32,818 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "12 items, types={'LabReport': 1, 'OutpatientRecord': 2, 'MedicationRecord': 3, 'PrescriptionRecord': 4, 'ExaminationReport': 2}", "name": "chho-麦济122-哮喘-沈阳-医大四院.pdf", "embedding_token_consumption": 4026}
2026-08-05 04:15:32,818 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 04:15:33,068 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 04:15:33,068 INFO     29 [Trace] task=a82d80a2 | doc=chho-麦济122-哮喘-沈阳-医大四院.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":12,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(4, 118, 167, 385, 403) row[-1]=(5, 117, 192, 817, 836)
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,074 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 04:15:33,079 INFO     29 set_progress(a82d80a2908311f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 04:15:33 [DOC Engine]:
Start to index...
2026-08-05 04:15:33,104 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-05 04:15:33,109 INFO     29 set_progress(a82d80a2908311f1a3da71efcdd7cc1f), progress: 0.8083333333333333, progress_msg: 
2026-08-05 04:15:33,140 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.020s]
2026-08-05 04:15:33,165 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-05 04:15:33,172 INFO     29 set_progress(a82d80a2908311f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 04:15:33 Indexing done (0.09s). Task done (253.39s)
2026-08-05 04:15:33,175 INFO     29 [Done], chunks(12), token(4026), elapsed:253.39
2026-08-05 04:15:33,307 INFO     29 handle_task done for task {"id": "a82d80a2908311f1a3da71efcdd7cc1f", "doc_id": "a747105e908311f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "type": "pdf", "location": "chho-\u9ea6\u6d4e122-\u54ee\u5598-\u6c88\u9633-\u533b\u5927\u56db\u9662.pdf", "size": 6983197, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785903056189, "task_type": "dataflow", "root_trace_id": "2fa47143ee23406b855067cf9d192c22", "root_traceparent": "00-2fa47143ee23406b855067cf9d192c22-36e716608aadf755-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
