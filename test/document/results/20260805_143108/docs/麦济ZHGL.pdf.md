# 基准结果：麦济ZHGL.pdf

## 基本信息

- 文件：`麦济ZHGL.pdf`
- 大小：4723.3 KB
- PDF 总页数：6
- doc_id：`2d7d9c50909411f1a3da71efcdd7cc1f`
- 上传方式：existing
- 状态：run=None (code=None)  progress=None
- 开始时间：2026-08-05T14:31:24  完成时间：2026-08-05T14:31:25  耗时：0.9s
- progress_msg：`06:11:40 Indexing done (0.05s). Task done (135.07s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | dd0fa5a9 | 1 | 1-1 | 电子发票(普通发票) 国家税务总局 内蒙古自治区税务局 发票号码：2515200 |
| 2 | 5fdfbf74 | 1 | 2-2 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：51岁 诊疗号：001107274 |
| 3 | 27da176a | 2 | 3-4 | 内蒙古医科大学附属医院门诊病历 姓名： 年龄：51岁 诊疗号：001107274 |
| 4 | f9364319 | 1 | 5-5 | 欣源药业 NO:2026011900323 商品名称 单价 数量 小计 布地奈德 |
| 5 | fc274305 | 1 | 6-6 | 内蒙古医科大学附属医院 门诊缴费凭证 诊疗号: 0011072747 姓名: 收 |

- chunks 总数：5
- 各 chunk 页数合计（含跨页重复）：6
- 页码并集：`[1, 2, 3, 4, 5, 6]`
- 覆盖页数：6 / 6；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 2 | 0 | 2 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 3 | 3 | 3 | encounter_date, pharmacy, payment_total | **OK** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 0 | 0 | 0 | report_time, report_category, report_name | **-** |

- SmartSplitter Types 统计：`{"MedicationRecord": 3, "OutpatientRecord": 2}`
- ChunkMerger：`{"found": true, "merged": 5, "sources": 8, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 2, "Extractor:Medication": 3, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1}, "filtered_noise": 6}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-05 06:11:39,463 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-05 06:09:13,984 INFO     29 handle_task begin for task {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-05 06:09:14,180 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-05 06:09:14,230 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-05 06:09:14,243 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-05 06:09:14,243 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-05 06:09:14,251 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-05 06:09:14,252 INFO     29 ============================================================
2026-08-05 06:09:14,252 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-05 06:09:14,252 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-05 06:09:14,252 INFO     29 ============================================================
2026-08-05 06:09:14,252 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-05 06:09:14,252 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-05 06:09:14,253 INFO     29 No torch found.
2026-08-05 06:09:15,041 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=6
2026-08-05 06:09:15,202 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=956086, prompt_len=644
2026-08-05 06:09:16,777 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:09:16,777 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-05 06:09:16,786 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=956086, prompt_len=401
2026-08-05 06:09:19,412 INFO     29 [qwen-vl-parser] text API response (len=451):
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：25152000000077385777", "开票日期：2025年12月24日", "购买方信息", "统一社会信用代码/纳税人识别号", "名称：国药控股国大药房内蒙古有限公司第三百七十三分公司", "统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46", "销售方信息", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "320ug:9ug*60吸", "盒", "1", "306.930693069307", "306.93", "1%", "3.07", "福莫特罗吸入粉雾剂", "合计", "￥306.93", "￥3.07", "价税合计(大写)", "叁佰壹拾圆整", "(小写)￥310.00", "收款人:马利亚;", "复核人:梁会荣", "备注", "开票人:梁会荣"]
2026-08-05 06:09:19,413 INFO     29 [qwen-vl-parser] page=1 text: 37 lines (bbox 0-36)
2026-08-05 06:09:19,413 INFO     29 [qwen-vl-parser] page=1 text: 37 sections
2026-08-05 06:09:19,821 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2046923, prompt_len=644
2026-08-05 06:09:22,674 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2020-02-13"}
```
2026-08-05 06:09:22,674 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=2020-02-13
2026-08-05 06:09:22,685 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2046923, prompt_len=401
2026-08-05 06:09:26,333 INFO     29 [qwen-vl-parser] text API response (len=546):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：51岁", "诊疗号：0011072747", "民族：汉族", "性别：女性", "内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2020-02-13 09:12", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近几日咳嗽、胸闷气短症状加重", "现病史：哮喘史，近几日咳嗽、胸闷气短症状加重", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "布地奈德福莫特罗吸入粉雾剂", "用量：1.000吸/次", "(II)<(320μg/9μg)/吸*60>", "用法：吸入，二次/日，30天", "签名："]
2026-08-05 06:09:26,333 INFO     29 [qwen-vl-parser] page=2 text: 33 lines (bbox 37-69)
2026-08-05 06:09:26,333 INFO     29 [qwen-vl-parser] page=2 text: 33 sections
2026-08-05 06:09:26,691 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2126284, prompt_len=644
2026-08-05 06:09:28,620 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-05 06:09:28,621 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-05 06:09:28,636 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2126284, prompt_len=401
2026-08-05 06:09:38,071 INFO     29 [qwen-vl-parser] text API response (len=1107):
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：51岁", "诊疗号：0011072747", "民族：汉族", "性别：女性", "呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-09 07:39", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：本次为V16访视", "现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮", "喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非", "药物治疗。检查并回收发放的日记卡1本，版本号/版本日期", "(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，", "指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂", "(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘", "记携带，嘱患者从今日起停用，择期尽快送回。", "既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂", "<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别", "ICS+LABA。", "既往病史：", "1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治", "疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评", "判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围", "内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与", "筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复", "查肝功。", "2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症", "状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞", "计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常", "有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，", "嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。", "此外无持续跟进AE。", "体格检查：", "辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至", "少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检", "查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照", "要求处理储存并寄送。", "过敏史："]
2026-08-05 06:09:38,071 INFO     29 [qwen-vl-parser] page=3 text: 44 lines (bbox 70-113)
2026-08-05 06:09:38,072 INFO     29 [qwen-vl-parser] page=3 text: 44 sections
2026-08-05 06:09:38,406 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1354067, prompt_len=644
2026-08-05 06:09:39,072 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:09:39.071+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"2de9b1b0909411f1a3da71efcdd7cc1f": {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:09:40,142 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:09:40,142 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-05 06:09:40,172 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1354067, prompt_len=401
2026-08-05 06:09:41,974 INFO     29 [qwen-vl-parser] text API response (len=176):
["初步诊断（西医）：1.支气管哮喘", "初步诊断（中医）：", "治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂", "(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/", "日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。", "签名："]
2026-08-05 06:09:41,975 INFO     29 [qwen-vl-parser] page=4 text: 6 lines (bbox 114-119)
2026-08-05 06:09:41,975 INFO     29 [qwen-vl-parser] page=4 text: 6 sections
2026-08-05 06:09:42,311 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1863898, prompt_len=644
2026-08-05 06:09:45,978 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:09:45,978 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-05 06:09:45,990 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1863898, prompt_len=401
2026-08-05 06:09:48,263 INFO     29 [qwen-vl-parser] text API response (len=275):
["欣源药业", "NO:2026011900323", "商品名称", "单价", "数量", "小计", "布地奈德福莫特罗吸入粉雾剂320ug:", "9ug*60吸/盒", "309.00", "2", "618.00", "阿斯利康", "批号: PKGF", "效期:2027-03 规格:1支/盒", "总计:", "2.00", "618.00", "会员卡号:800310", "会员姓名:", "本次积分:618.00", "累计积分:2518.10", "收银员004营业员004", "日期26-01-1910:53:22"]
2026-08-05 06:09:48,264 INFO     29 [qwen-vl-parser] page=5 text: 23 lines (bbox 120-142)
2026-08-05 06:09:48,264 INFO     29 [qwen-vl-parser] page=5 text: 23 sections
2026-08-05 06:09:48,523 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1199420, prompt_len=644
2026-08-05 06:09:50,113 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-05 06:09:50,113 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=None
2026-08-05 06:09:50,120 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1199420, prompt_len=401
2026-08-05 06:09:52,221 INFO     29 [qwen-vl-parser] text API response (len=305):
["内蒙古医科大学附属医院", "门诊缴费凭证", "诊疗号: 0011072747", "姓名:", "收费项目", "西药", "总额(元)", "301.53", "(取药窗口: 门诊二楼西药房3号窗口)", "开单科室: 呼吸内科门诊", "结算类型: 自费", "总金额: 301.53元", "实付金额: 301.53元", "机器编号: zzj217", "缴费时间: 2026-02-13 10:13:31", "支付方式: 微信", "交易订单号: 39N6260213101311FYAzzj217D4230", "温馨提示:", "如需发票, 请关注我院微信公众号获取", "电子发票"]
2026-08-05 06:09:52,221 INFO     29 [qwen-vl-parser] page=6 text: 20 lines (bbox 143-162)
2026-08-05 06:09:52,221 INFO     29 [qwen-vl-parser] page=6 text: 20 sections
2026-08-05 06:09:52,221 INFO     29 [qwen-vl-parser] parse_pdf done: 163 sections from 6 pages.
2026-08-05 06:09:52,231 INFO     29 Close text detector.
2026-08-05 06:09:52,696 INFO     29 Close text recognizer.
2026-08-05 06:09:53,130 INFO     29 Close recognizer.
2026-08-05 06:09:53,544 INFO     29 Close recognizer.
2026-08-05 06:09:54,096 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-05 06:09:54,096 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Parser:MedLink | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "json"}
2026-08-05 06:09:54,096 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-05 06:09:54,126 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:09:54,127 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。只有主诉，病史的也属于OutpatientRecord（门诊病历）\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n6. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n7. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 电子发票(普通发票)\n[BBOX-1] 国家税务总局\n[BBOX-2] 内蒙古自治区税务局\n[BBOX-3] 发票号码：25152000000077385777\n[BBOX-4] 开票日期：2025年12月24日\n[BBOX-5] 购买方信息\n[BBOX-6] 统一社会信用代码/纳税人识别号\n[BBOX-7] 名称：国药控股国大药房内蒙古有限公司第三百七十三分公司\n[BBOX-8] 统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46\n[BBOX-9] 销售方信息\n[BBOX-10] 项目名称\n[BBOX-11] 规格型号\n[BBOX-12] 单位\n[BBOX-13] 数量\n[BBOX-14] 单价\n[BBOX-15] 金额\n[BBOX-16] 税率/征收率\n[BBOX-17] 税额\n[BBOX-18] *化学药品制剂*布地奈德\n[BBOX-19] 320ug:9ug*60吸\n[BBOX-20] 盒\n[BBOX-21] 1\n[BBOX-22] 306.930693069307\n[BBOX-23] 306.93\n[BBOX-24] 1%\n[BBOX-25] 3.07\n[BBOX-26] 福莫特罗吸入粉雾剂\n[BBOX-27] 合计\n[BBOX-28] ￥306.93\n[BBOX-29] ￥3.07\n[BBOX-30] 价税合计(大写)\n[BBOX-31] 叁佰壹拾圆整\n[BBOX-32] (小写)￥310.00\n[BBOX-33] 收款人:马利亚;\n[BBOX-34] 复核人:梁会荣\n[BBOX-35] 备注\n[BBOX-36] 开票人:梁会荣\n[BBOX-37] 内蒙古医科大学附属医院门诊病历\n[BBOX-38] 姓名：\n[BBOX-39] 年龄：51岁\n[BBOX-40] 诊疗号：0011072747\n[BBOX-41] 民族：汉族\n[BBOX-42] 性别：女性\n[BBOX-43] 内科门诊\n[BBOX-44] 联系电话：\n[BBOX-45] 身份证：\n[BBOX-46] 病情：\n[BBOX-47] 就诊状态：\n[BBOX-48] 就诊时间：2020-02-13 09:12\n[BBOX-49] 生命体征（需要时）：\n[BBOX-50] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-51] 主诉：哮喘史，近几日咳嗽、胸闷气短症状加重\n[BBOX-52] 现病史：哮喘史，近几日咳嗽、胸闷气短症状加重\n[BBOX-53] 既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n[BBOX-54] 无，吸烟史无，无过敏史。\n[BBOX-55] 体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰\n[BBOX-56] 音，双下肢无水肿，体重kg。\n[BBOX-57] 辅助检查：心肺\n[BBOX-58] 过敏史：不详\n[BBOX-59] 初步诊断（西医）：1.支气管哮喘(急性发作期)\n[BBOX-60] 初步诊断（中医）：\n[BBOX-61] 治疗方案：随诊\n[BBOX-62] 醋酸泼尼松片<5mg>\n[BBOX-63] 用量：3.000片/次\n[BBOX-64] 用法：口服，一次/日，5天\n[BBOX-65] 布地奈德福莫特罗吸入粉雾剂\n[BBOX-66] 用量：1.000吸/次\n[BBOX-67] (II)<(320μg/9μg)/吸*60>\n[BBOX-68] 用法：吸入，二次/日，30天\n[BBOX-69] 签名：\n[BBOX-70] 内蒙古医科大学附属医院门诊病历\n[BBOX-71] 姓名：\n[BBOX-72] 年龄：51岁\n[BBOX-73] 诊疗号：0011072747\n[BBOX-74] 民族：汉族\n[BBOX-75] 性别：女性\n[BBOX-76] 呼吸内科门诊\n[BBOX-77] 联系电话：\n[BBOX-78] 身份证：\n[BBOX-79] 病情：\n[BBOX-80] 就诊状态：\n[BBOX-81] 就诊时间：2026-02-09 07:39\n[BBOX-82] 生命体征（需要时）：\n[BBOX-83] 体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n[BBOX-84] 主诉：本次为V16访视\n[BBOX-85] 现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮\n[BBOX-86] 喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非\n[BBOX-87] 药物治疗。检查并回收发放的日记卡1本，版本号/版本日期\n[BBOX-88] (V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，\n[BBOX-89] 指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂\n[BBOX-90] (万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘\n[BBOX-91] 记携带，嘱患者从今日起停用，择期尽快送回。\n[BBOX-92] 既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂\n[BBOX-93] <(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别\n[BBOX-94] ICS+LABA。\n[BBOX-95] 既往病史：\n[BBOX-96] 1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治\n[BBOX-97] 疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评\n[BBOX-98] 判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围\n[BBOX-99] 内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与\n[BBOX-100] 筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复\n[BBOX-101] 查肝功。\n[BBOX-102] 2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症\n[BBOX-103] 状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞\n[BBOX-104] 计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常\n[BBOX-105] 有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，\n[BBOX-106] 嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。\n[BBOX-107] 此外无持续跟进AE。\n[BBOX-108] 体格检查：\n[BBOX-109] 辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至\n[BBOX-110] 少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检\n[BBOX-111] 查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照\n[BBOX-112] 要求处理储存并寄送。\n[BBOX-113] 过敏史：\n[BBOX-114] 初步诊断（西医）：1.支气管哮喘\n[BBOX-115] 初步诊断（中医）：\n[BBOX-116] 治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂\n[BBOX-117] (II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/\n[BBOX-118] 日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。\n[BBOX-119] 签名：\n[BBOX-120] 欣源药业\n[BBOX-121] NO:2026011900323\n[BBOX-122] 商品名称\n[BBOX-123] 单价\n[BBOX-124] 数量\n[BBOX-125] 小计\n[BBOX-126] 布地奈德福莫特罗吸入粉雾剂320ug:\n[BBOX-127] 9ug*60吸/盒\n[BBOX-128] 309.00\n[BBOX-129] 2\n[BBOX-130] 618.00\n[BBOX-131] 阿斯利康\n[BBOX-132] 批号: PKGF\n[BBOX-133] 效期:2027-03 规格:1支/盒\n[BBOX-134] 总计:\n[BBOX-135] 2.00\n[BBOX-136] 618.00\n[BBOX-137] 会员卡号:800310\n[BBOX-138] 会员姓名:\n[BBOX-139] 本次积分:618.00\n[BBOX-140] 累计积分:2518.10\n[BBOX-141] 收银员004营业员004\n[BBOX-142] 日期26-01-1910:53:22\n[BBOX-143] 内蒙古医科大学附属医院\n[BBOX-144] 门诊缴费凭证\n[BBOX-145] 诊疗号: 0011072747\n[BBOX-146] 姓名:\n[BBOX-147] 收费项目\n[BBOX-148] 西药\n[BBOX-149] 总额(元)\n[BBOX-150] 301.53\n[BBOX-151] (取药窗口: 门诊二楼西药房3号窗口)\n[BBOX-152] 开单科室: 呼吸内科门诊\n[BBOX-153] 结算类型: 自费\n[BBOX-154] 总金额: 301.53元\n[BBOX-155] 实付金额: 301.53元\n[BBOX-156] 机器编号: zzj217\n[BBOX-157] 缴费时间: 2026-02-13 10:13:31\n[BBOX-158] 支付方式: 微信\n[BBOX-159] 交易订单号: 39N6260213101311FYAzzj217D4230\n[BBOX-160] 温馨提示:\n[BBOX-161] 如需发票, 请关注我院微信公众号获取\n[BBOX-162] 电子发票"
  }
]
2026-08-05 06:09:58,931 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:09:58,943 INFO     29 [SmartSplitter] SmartSplitter done: 5 chunks from 5 LLM segments (all bbox_id). Types: {'MedicationRecord': 3, 'OutpatientRecord': 2}
2026-08-05 06:09:58,951 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-05 06:09:58,951 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks": "5 items, types={'MedicationRecord': 3, 'OutpatientRecord': 2}"}
2026-08-05 06:09:58,951 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-05 06:09:58,951 INFO     29 [ChunkRouter] Routed 5 chunks into 2 groups: {'chunks_Medication': 3, 'chunks_Clinical': 2}
2026-08-05 06:09:58,958 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-05 06:09:58,959 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | ChunkRouter:Router | outputs={"html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks": "5 items, types={'MedicationRecord': 3, 'OutpatientRecord': 2}", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:09:58,959 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-05 06:09:58,963 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:09:58,963 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:09:58 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:09:58,964 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:09:59,696 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:09:59,702 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-05 06:09:59,702 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:LabExam | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:09:59,702 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-05 06:09:59,708 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:09:59,709 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:09:59 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:09:59,710 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:00,720 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:10:00,725 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-05 06:10:00,725 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:10:00,725 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-05 06:10:00,730 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:10:00,730 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:10:00,730 INFO     29 [qwen-vl-text] positions(33): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:10:00,730 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [33]
2026-08-05 06:10:01,170 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:10:01,171 INFO     29 [qwen-vl-text] LLM extraction start, text_len=446
2026-08-05 06:10:01,171 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:10:01,171 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 37, \"bbox_end\": 69, \"encounter_dates\": [\"2020-02-13\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：51岁\n诊疗号：0011072747\n民族：汉族\n性别：女性\n内科门诊\n联系电话：\n身份证：\n病情：\n就诊状态：\n就诊时间：2020-02-13 09:12\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：哮喘史，近几日咳嗽、胸闷气短症状加重\n现病史：哮喘史，近几日咳嗽、胸闷气短症状加重\n既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎\n无，吸烟史无，无过敏史。\n体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰\n音，双下肢无水肿，体重kg。\n辅助检查：心肺\n过敏史：不详\n初步诊断（西医）：1.支气管哮喘(急性发作期)\n初步诊断（中医）：\n治疗方案：随诊\n醋酸泼尼松片<5mg>\n用量：3.000片/次\n用法：口服，一次/日，5天\n布地奈德福莫特罗吸入粉雾剂\n用量：1.000吸/次\n(II)<(320μg/9μg)/吸*60>\n用法：吸入，二次/日，30天\n签名：",
    "role": "user"
  }
]
[92m06:10:01 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:01,172 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:04,095 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:10:04,095 INFO     29 [qwen-vl-text] LLM output (len=382):
{
  "encounter_date": "2020-02-13",
  "chief_complaint": "哮喘史，近几日咳嗽、胸闷气短症状加重",
  "present_illness": "哮喘史，近几日咳嗽、胸闷气短症状加重",
  "past_history": "患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎无，吸烟史无，无过敏史。",
  "diagnosis": "西医：1.支气管哮喘(急性发作期) 中医：null",
  "treatment_plan": [
    "随诊",
    "醋酸泼尼松片<5mg> 用量：3.000片/次 用法：口服，一次/日，5天",
    "布地奈德福莫特罗吸入粉雾剂(II)<(320μg/9μg)/吸*60> 用量：1.000吸/次 用法：吸入，二次/日，30天"
  ]
}
2026-08-05 06:10:04,096 INFO     29 [qwen-vl-text] Updated encounter_dates=[2020-02-13]
2026-08-05 06:10:04,100 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2424420, prompt_len=1158
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：51岁", "诊疗号：0011072747", "民族：汉族", "性别：女性", "内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2020-02-13 09:12", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：哮喘史，近几日咳嗽、胸闷气短症状加重", "现病史：哮喘史，近几日咳嗽、胸闷气短症状加重", "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "无，吸烟史无，无过敏史。", "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "音，双下肢无水肿，体重kg。", "辅助检查：心肺", "过敏史：不详", "初步诊断（西医）：1.支气管哮喘(急性发作期)", "初步诊断（中医）：", "治疗方案：随诊", "醋酸泼尼松片<5mg>", "用量：3.000片/次", "用法：口服，一次/日，5天", "布地奈德福莫特罗吸入粉雾剂", "用量：1.000吸/次", "(II)<(320μg/9μg)/吸*60>", "用法：吸入，二次/日，30天", "签名："]

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
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord API raw response (len=1899):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [285, 93, 814, 118]},
	{"text": "姓名：", "bbox": [109, 120, 167, 139]},
	{"text": "年龄：51岁", "bbox": [373, 123, 505, 142]},
	{"text": "诊疗号：0011072747", "bbox": [630, 125, 855, 143]},
	{"text": "民族：汉族", "bbox": [109, 145, 238, 163]},
	{"text": "性别：女性", "bbox": [400, 148, 501, 166]},
	{"text": "内科门诊", "bbox": [758, 148, 858, 166]},
	{"text": "联系电话：", "bbox": [108, 168, 219, 187]},
	{"text": "身份证：", "bbox": [419, 170, 502, 188]},
	{"text": "病情：", "bbox": [798, 170, 857, 189]},
	{"text": "就诊状态：", "bbox": [108, 191, 219, 209]},
	{"text": "就诊时间：2020-02-13 09:12", "bbox": [354, 193, 695, 211]},
	{"text": "生命体征（需要时）：", "bbox": [108, 214, 346, 233]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [108, 238, 614, 258]},
	{"text": "主诉：哮喘史，近几日咳嗽、胸闷气短症状加重", "bbox": [106, 262, 668, 282]},
	{"text": "现病史：哮喘史，近几日咳嗽、胸闷气短症状加重", "bbox": [106, 287, 668, 306]},
	{"text": "既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎", "bbox": [104, 311, 976, 332]},
	{"text": "无，吸烟史无，无过敏史。", "bbox": [213, 336, 504, 356]},
	{"text": "体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰", "bbox": [104, 360, 944, 380]},
	{"text": "音，双下肢无水肿，体重kg。", "bbox": [240, 385, 561, 405]},
	{"text": "辅助检查：心肺", "bbox": [102, 410, 305, 429]},
	{"text": "过敏史：不详", "bbox": [102, 434, 288, 453]},
	{"text": "初步诊断（西医）：1.支气管哮喘(急性发作期)", "bbox": [102, 458, 634, 478]},
	{"text": "初步诊断（中医）：", "bbox": [102, 482, 316, 502]},
	{"text": "治疗方案：随诊", "bbox": [102, 507, 288, 526]},
	{"text": "醋酸泼尼松片<5mg>", "bbox": [99, 566, 313, 585]},
	{"text": "用量：3.000片/次", "bbox": [608, 565, 810, 584]},
	{"text": "用法：口服，一次/日，5天", "bbox": [139, 591, 444, 610]},
	{"text": "布地奈德福莫特罗吸入粉雾剂", "bbox": [100, 617, 426, 636]},
	{"text": "用量：1.000吸/次", "bbox": [607, 616, 808, 635]},
	{"text": "(II)<(320μg/9μg)/吸*60>", "bbox": [100, 654, 414, 673]},
	{"text": "用法：吸入，二次/日，30天", "bbox": [137, 677, 454, 696]},
	{"text": "签名：", "bbox": [574, 770, 632, 790]}
]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=13.7s
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[285, 93, 814, 118]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[109, 120, 167, 139]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：51岁, bbox=[373, 123, 505, 142]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0011072747, bbox=[630, 125, 855, 143]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[109, 145, 238, 163]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女性, bbox=[400, 148, 501, 166]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[6]: text=内科门诊, bbox=[758, 148, 858, 166]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[108, 168, 219, 187]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[8]: text=身份证：, bbox=[419, 170, 502, 188]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[9]: text=病情：, bbox=[798, 170, 857, 189]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[10]: text=就诊状态：, bbox=[108, 191, 219, 209]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[11]: text=就诊时间：2020-02-13 09:12, bbox=[354, 193, 695, 211]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[12]: text=生命体征（需要时）：, bbox=[108, 214, 346, 233]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[13]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[108, 238, 614, 258]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：哮喘史，近几日咳嗽、胸闷气短症状加重, bbox=[106, 262, 668, 282]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：哮喘史，近几日咳嗽、胸闷气短症状加重, bbox=[106, 287, 668, 306]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[16]: text=既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎, bbox=[104, 311, 976, 332]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[17]: text=无，吸烟史无，无过敏史。, bbox=[213, 336, 504, 356]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[18]: text=体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰, bbox=[104, 360, 944, 380]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[19]: text=音，双下肢无水肿，体重kg。, bbox=[240, 385, 561, 405]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[20]: text=辅助检查：心肺, bbox=[102, 410, 305, 429]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[21]: text=过敏史：不详, bbox=[102, 434, 288, 453]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[22]: text=初步诊断（西医）：1.支气管哮喘(急性发作期), bbox=[102, 458, 634, 478]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[23]: text=初步诊断（中医）：, bbox=[102, 482, 316, 502]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[24]: text=治疗方案：随诊, bbox=[102, 507, 288, 526]
2026-08-05 06:10:17,808 INFO     29 [qwen-vl-text] coord item[25]: text=醋酸泼尼松片<5mg>, bbox=[99, 566, 313, 585]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[26]: text=用量：3.000片/次, bbox=[608, 565, 810, 584]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[27]: text=用法：口服，一次/日，5天, bbox=[139, 591, 444, 610]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[28]: text=布地奈德福莫特罗吸入粉雾剂, bbox=[100, 617, 426, 636]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[29]: text=用量：1.000吸/次, bbox=[607, 616, 808, 635]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[30]: text=(II)<(320μg/9μg)/吸*60>, bbox=[100, 654, 414, 673]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[31]: text=用法：吸入，二次/日，30天, bbox=[137, 677, 454, 696]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] coord item[32]: text=签名：, bbox=[574, 770, 632, 790]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] page=1 — 33/33 coords, api_time=13.7s
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] new_positions (33):
[[1, 169.575, 484.33, 78.306, 99.356], [1, 64.855, 99.365, 101.03999999999999, 117.038], [1, 221.935, 300.47499999999997, 103.566, 119.564], [1, 374.84999999999997, 508.72499999999997, 105.25, 120.40599999999999], [1, 64.855, 141.60999999999999, 122.08999999999999, 137.246], [1, 238.0, 298.09499999999997, 124.616, 139.772], [1, 451.01, 510.51, 124.616, 139.772], [1, 64.25999999999999, 130.305, 141.456, 157.454], [1, 249.30499999999998, 298.69, 143.14, 158.296], [1, 474.81, 509.91499999999996, 143.14, 159.138], [1, 64.25999999999999, 130.305, 160.822, 175.97799999999998], [1, 210.63, 413.525, 162.506, 177.662], [1, 64.25999999999999, 205.87, 180.188, 196.186], [1, 64.25999999999999, 365.33, 200.396, 217.236], [1, 63.07, 397.46, 220.60399999999998, 237.444], [1, 63.07, 397.46, 241.654, 257.652], [1, 61.879999999999995, 580.72, 261.86199999999997, 279.544], [1, 126.735, 299.88, 282.912, 299.752], [1, 61.879999999999995, 561.68, 303.12, 319.96], [1, 142.79999999999998, 333.79499999999996, 324.17, 341.01], [1, 60.69, 181.475, 345.21999999999997, 361.21799999999996], [1, 60.69, 171.35999999999999, 365.428, 381.426], [1, 60.69, 377.22999999999996, 385.63599999999997, 402.476], [1, 60.69, 188.01999999999998, 405.844, 422.68399999999997], [1, 60.69, 171.35999999999999, 426.894, 442.892], [1, 58.904999999999994, 186.23499999999999, 476.572, 492.57], [1, 361.76, 481.95, 475.72999999999996, 491.728], [1, 82.705, 264.18, 497.62199999999996, 513.62], [1, 59.5, 253.47, 519.514, 535.512], [1, 361.16499999999996, 480.76, 518.672, 534.67], [1, 59.5, 246.32999999999998, 550.668, 566.6659999999999], [1, 81.515, 270.13, 570.034, 586.0319999999999], [1, 341.53, 376.03999999999996, 648.34, 665.18]]
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=17.1s
2026-08-05 06:10:17,809 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-05 06:10:17,809 INFO     29 [qwen-vl-text] positions(50): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:10:17,810 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [44, 6]
2026-08-05 06:10:18,178 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:10:18,576 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:10:18,576 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1132
2026-08-05 06:10:18,576 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:10:18,576 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 70, \"bbox_end\": 119, \"encounter_dates\": [\"2026-02-09\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "内蒙古医科大学附属医院门诊病历\n姓名：\n年龄：51岁\n诊疗号：0011072747\n民族：汉族\n性别：女性\n呼吸内科门诊\n联系电话：\n身份证：\n病情：\n就诊状态：\n就诊时间：2026-02-09 07:39\n生命体征（需要时）：\n体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg\n主诉：本次为V16访视\n现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮\n喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非\n药物治疗。检查并回收发放的日记卡1本，版本号/版本日期\n(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，\n指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂\n(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘\n记携带，嘱患者从今日起停用，择期尽快送回。\n既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂\n<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别\nICS+LABA。\n既往病史：\n1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治\n疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评\n判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围\n内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与\n筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复\n查肝功。\n2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症\n状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞\n计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常\n有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，\n嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。\n此外无持续跟进AE。\n体格检查：\n辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至\n少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检\n查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照\n要求处理储存并寄送。\n过敏史：\n初步诊断（西医）：1.支气管哮喘\n初步诊断（中医）：\n治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂\n(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/\n日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。\n签名：",
    "role": "user"
  }
]
[92m06:10:18 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:18,577 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:18,579 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:10:18.577+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"2de9b1b0909411f1a3da71efcdd7cc1f": {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:10:25,979 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:10:25,980 INFO     29 [qwen-vl-text] LLM output (len=953):
{
  "encounter_date": "2026-02-09",
  "chief_complaint": "本次为V16访视",
  "present_illness": "今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非药物治疗。检查并回收发放的日记卡1本，版本号/版本日期(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘记携带，嘱患者从今日起停用，择期尽快送回。",
  "past_history": "背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别ICS+LABA。既往病史：1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复查肝功。2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。此外无持续跟进AE。",
  "diagnosis": "西医：1.支气管哮喘 中医：",
  "treatment_plan": "随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。"
}
2026-08-05 06:10:25,980 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-09]
2026-08-05 06:10:25,989 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2561010, prompt_len=1719
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["内蒙古医科大学附属医院门诊病历", "姓名：", "年龄：51岁", "诊疗号：0011072747", "民族：汉族", "性别：女性", "呼吸内科门诊", "联系电话：", "身份证：", "病情：", "就诊状态：", "就诊时间：2026-02-09 07:39", "生命体征（需要时）：", "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "主诉：本次为V16访视", "现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮", "喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非", "药物治疗。检查并回收发放的日记卡1本，版本号/版本日期", "(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，", "指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂", "(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘", "记携带，嘱患者从今日起停用，择期尽快送回。", "既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂", "<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别", "ICS+LABA。", "既往病史：", "1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治", "疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评", "判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围", "内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与", "筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复", "查肝功。", "2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症", "状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞", "计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常", "有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，", "嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。", "此外无持续跟进AE。", "体格检查：", "辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至", "少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检", "查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照", "要求处理储存并寄送。", "过敏史："]

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
2026-08-05 06:10:44,418 INFO     29 [qwen-vl-text] coord API raw response (len=2912):
[
	{"text": "内蒙古医科大学附属医院门诊病历", "bbox": [278, 78, 785, 106]},
	{"text": "姓名：", "bbox": [117, 110, 173, 128]},
	{"text": "年龄：51岁", "bbox": [364, 110, 490, 128]},
	{"text": "诊疗号：0011072747", "bbox": [608, 109, 825, 127]},
	{"text": "民族：汉族", "bbox": [117, 133, 241, 150]},
	{"text": "性别：女性", "bbox": [364, 133, 488, 150]},
	{"text": "呼吸内科门诊", "bbox": [690, 132, 829, 150]},
	{"text": "联系电话：", "bbox": [117, 156, 221, 173]},
	{"text": "身份证：", "bbox": [410, 156, 490, 173]},
	{"text": "病情：", "bbox": [770, 155, 829, 172]},
	{"text": "就诊状态：", "bbox": [117, 178, 221, 195]},
	{"text": "就诊时间：2026-02-09 07:39", "bbox": [350, 178, 673, 195]},
	{"text": "生命体征（需要时）：", "bbox": [117, 200, 344, 218]},
	{"text": "体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg", "bbox": [117, 223, 598, 241]},
	{"text": "主诉：本次为V16访视", "bbox": [117, 247, 386, 265]},
	{"text": "现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮", "bbox": [117, 269, 949, 288]},
	{"text": "喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非", "bbox": [219, 292, 949, 311]},
	{"text": "药物治疗。检查并回收发放的日记卡1本，版本号/版本日期", "bbox": [220, 316, 952, 335]},
	{"text": "(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，", "bbox": [231, 340, 937, 359]},
	{"text": "指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂", "bbox": [219, 364, 952, 383]},
	{"text": "(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘", "bbox": [231, 387, 952, 406]},
	{"text": "记携带，嘱患者从今日起停用，择期尽快送回。", "bbox": [219, 411, 718, 430]},
	{"text": "既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂", "bbox": [117, 435, 952, 454]},
	{"text": "<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别", "bbox": [220, 458, 952, 477]},
	{"text": "ICS+LABA。", "bbox": [221, 484, 341, 501]},
	{"text": "既往病史：", "bbox": [221, 508, 328, 525]},
	{"text": "1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治", "bbox": [221, 530, 954, 549]},
	{"text": "疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评", "bbox": [221, 554, 957, 573]},
	{"text": "判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围", "bbox": [221, 577, 957, 596]},
	{"text": "内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与", "bbox": [221, 601, 955, 620]},
	{"text": "筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复", "bbox": [221, 625, 955, 644]},
	{"text": "查肝功。", "bbox": [221, 650, 305, 668]},
	{"text": "2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症", "bbox": [221, 673, 955, 692]},
	{"text": "状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞", "bbox": [221, 697, 957, 716]},
	{"text": "计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常", "bbox": [221, 720, 955, 739]},
	{"text": "有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，", "bbox": [223, 744, 943, 763]},
	{"text": "嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。", "bbox": [223, 768, 909, 787]},
	{"text": "此外无持续跟进AE。", "bbox": [223, 792, 433, 811]},
	{"text": "体格检查：", "bbox": [120, 818, 225, 836]},
	{"text": "辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至", "bbox": [120, 842, 955, 861]},
	{"text": "少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检", "bbox": [250, 865, 955, 885]},
	{"text": "查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照", "bbox": [250, 889, 955, 908]},
	{"text": "要求处理储存并寄送。", "bbox": [250, 913, 478, 932]},
	{"text": "过敏史：", "bbox": [117, 937, 200, 955]}
]
2026-08-05 06:10:44,418 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=18.4s
2026-08-05 06:10:44,418 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院门诊病历, bbox=[278, 78, 785, 106]
2026-08-05 06:10:44,418 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[117, 110, 173, 128]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[2]: text=年龄：51岁, bbox=[364, 110, 490, 128]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗号：0011072747, bbox=[608, 109, 825, 127]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[117, 133, 241, 150]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女性, bbox=[364, 133, 488, 150]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[6]: text=呼吸内科门诊, bbox=[690, 132, 829, 150]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[7]: text=联系电话：, bbox=[117, 156, 221, 173]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[8]: text=身份证：, bbox=[410, 156, 490, 173]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[9]: text=病情：, bbox=[770, 155, 829, 172]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[10]: text=就诊状态：, bbox=[117, 178, 221, 195]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[11]: text=就诊时间：2026-02-09 07:39, bbox=[350, 178, 673, 195]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[12]: text=生命体征（需要时）：, bbox=[117, 200, 344, 218]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[13]: text=体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg, bbox=[117, 223, 598, 241]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[14]: text=主诉：本次为V16访视, bbox=[117, 247, 386, 265]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[15]: text=现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮, bbox=[117, 269, 949, 288]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[16]: text=喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非, bbox=[219, 292, 949, 311]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[17]: text=药物治疗。检查并回收发放的日记卡1本，版本号/版本日期, bbox=[220, 316, 952, 335]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[18]: text=(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，, bbox=[231, 340, 937, 359]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[19]: text=指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂, bbox=[219, 364, 952, 383]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[20]: text=(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘, bbox=[231, 387, 952, 406]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[21]: text=记携带，嘱患者从今日起停用，择期尽快送回。, bbox=[219, 411, 718, 430]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[22]: text=既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂, bbox=[117, 435, 952, 454]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[23]: text=<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别, bbox=[220, 458, 952, 477]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[24]: text=ICS+LABA。, bbox=[221, 484, 341, 501]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[25]: text=既往病史：, bbox=[221, 508, 328, 525]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[26]: text=1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治, bbox=[221, 530, 954, 549]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[27]: text=疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评, bbox=[221, 554, 957, 573]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[28]: text=判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围, bbox=[221, 577, 957, 596]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[29]: text=内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与, bbox=[221, 601, 955, 620]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[30]: text=筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复, bbox=[221, 625, 955, 644]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[31]: text=查肝功。, bbox=[221, 650, 305, 668]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[32]: text=2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症, bbox=[221, 673, 955, 692]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[33]: text=状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞, bbox=[221, 697, 957, 716]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[34]: text=计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常, bbox=[221, 720, 955, 739]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[35]: text=有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，, bbox=[223, 744, 943, 763]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[36]: text=嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。, bbox=[223, 768, 909, 787]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[37]: text=此外无持续跟进AE。, bbox=[223, 792, 433, 811]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[38]: text=体格检查：, bbox=[120, 818, 225, 836]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[39]: text=辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至, bbox=[120, 842, 955, 861]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[40]: text=少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检, bbox=[250, 865, 955, 885]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[41]: text=查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照, bbox=[250, 889, 955, 908]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[42]: text=要求处理储存并寄送。, bbox=[250, 913, 478, 932]
2026-08-05 06:10:44,419 INFO     29 [qwen-vl-text] coord item[43]: text=过敏史：, bbox=[117, 937, 200, 955]
2026-08-05 06:10:44,420 INFO     29 [qwen-vl-text] page=2 — 44/44 coords, api_time=18.4s
2026-08-05 06:10:44,422 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1630373, prompt_len=787
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共6行）
["初步诊断（西医）：1.支气管哮喘", "初步诊断（中医）：", "治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂", "(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/", "日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。", "签名："]

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
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord API raw response (len=423):
[
	{"text": "初步诊断（西医）：1.支气管哮喘", "bbox": [115, 82, 484, 102]},
	{"text": "初步诊断（中医）：", "bbox": [116, 107, 321, 126]},
	{"text": "治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂", "bbox": [248, 131, 868, 150]},
	{"text": "(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/", "bbox": [250, 155, 920, 174]},
	{"text": "日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。", "bbox": [250, 178, 933, 219]},
	{"text": "签名：", "bbox": [580, 255, 731, 275]}
]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord API: raw_items=6, valid_items=6, elapsed=3.7s
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[0]: text=初步诊断（西医）：1.支气管哮喘, bbox=[115, 82, 484, 102]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[1]: text=初步诊断（中医）：, bbox=[116, 107, 321, 126]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[2]: text=治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂, bbox=[248, 131, 868, 150]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[3]: text=(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/, bbox=[250, 155, 920, 174]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[4]: text=日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。, bbox=[250, 178, 933, 219]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] coord item[5]: text=签名：, bbox=[580, 255, 731, 275]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] page=3 — 6/6 coords, api_time=3.7s
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] new_positions (50):
[[2, 165.41, 467.075, 65.676, 89.252], [2, 69.615, 102.935, 92.61999999999999, 107.776], [2, 216.57999999999998, 291.55, 92.61999999999999, 107.776], [2, 361.76, 490.875, 91.77799999999999, 106.934], [2, 69.615, 143.39499999999998, 111.98599999999999, 126.3], [2, 216.57999999999998, 290.36, 111.98599999999999, 126.3], [2, 410.54999999999995, 493.255, 111.14399999999999, 126.3], [2, 69.615, 131.495, 131.352, 145.666], [2, 243.95, 291.55, 131.352, 145.666], [2, 458.15, 493.255, 130.51, 144.82399999999998], [2, 69.615, 131.495, 149.876, 164.19], [2, 208.25, 400.435, 149.876, 164.19], [2, 69.615, 204.67999999999998, 168.4, 183.55599999999998], [2, 69.615, 355.81, 187.766, 202.922], [2, 69.615, 229.67, 207.974, 223.13], [2, 69.615, 564.655, 226.498, 242.49599999999998], [2, 130.305, 564.655, 245.864, 261.86199999999997], [2, 130.9, 566.4399999999999, 266.072, 282.07], [2, 137.445, 557.515, 286.28, 302.27799999999996], [2, 130.305, 566.4399999999999, 306.488, 322.486], [2, 137.445, 566.4399999999999, 325.854, 341.852], [2, 130.305, 427.21, 346.062, 362.06], [2, 69.615, 566.4399999999999, 366.27, 382.268], [2, 130.9, 566.4399999999999, 385.63599999999997, 401.63399999999996], [2, 131.495, 202.89499999999998, 407.52799999999996, 421.842], [2, 131.495, 195.16, 427.736, 442.05], [2, 131.495, 567.63, 446.26, 462.258], [2, 131.495, 569.415, 466.46799999999996, 482.466], [2, 131.495, 569.415, 485.834, 501.832], [2, 131.495, 568.225, 506.042, 522.04], [2, 131.495, 568.225, 526.25, 542.2479999999999], [2, 131.495, 181.475, 547.3, 562.456], [2, 131.495, 568.225, 566.6659999999999, 582.664], [2, 131.495, 569.415, 586.874, 602.872], [2, 131.495, 568.225, 606.24, 622.2379999999999], [2, 132.685, 561.0849999999999, 626.448, 642.446], [2, 132.685, 540.855, 646.656, 662.654], [2, 132.685, 257.635, 666.864, 682.862], [2, 71.39999999999999, 133.875, 688.756, 703.9119999999999], [2, 71.39999999999999, 568.225, 708.9639999999999, 724.962], [2, 148.75, 568.225, 728.3299999999999, 745.17], [2, 148.75, 568.225, 748.538, 764.536], [2, 148.75, 284.40999999999997, 768.746, 784.744], [2, 69.615, 119.0, 788.954, 804.11], [3, 68.425, 287.97999999999996, 69.044, 85.884], [3, 69.02, 190.995, 90.094, 106.092], [3, 147.56, 516.4599999999999, 110.30199999999999, 126.3], [3, 148.75, 547.4, 130.51, 146.50799999999998], [3, 148.75, 555.135, 149.876, 184.398], [3, 345.09999999999997, 434.945, 214.70999999999998, 231.54999999999998]]
2026-08-05 06:10:48,145 INFO     29 [qwen-vl-text] ═══ DONE ═══ 50 positions, pages=2, time=30.3s
2026-08-05 06:10:48,161 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-05 06:10:48,161 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Clinical | outputs={"chunks": "2 items, types={'OutpatientRecord': 2}", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:10:48,161 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-05 06:10:48,168 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:10:48,169 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:10:48,169 INFO     29 [qwen-vl-text] positions(37): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:10:48,169 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [37]
2026-08-05 06:10:48,399 INFO     29 [qwen-vl-text] page=0, rect=842x595, img=(2339x1653), dpi=200
2026-08-05 06:10:48,400 INFO     29 [qwen-vl-text] LLM extraction start, text_len=339
2026-08-05 06:10:48,400 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:10:48,400 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 0, \"bbox_end\": 36, \"encounter_dates\": [\"2025-12-24\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "电子发票(普通发票)\n国家税务总局\n内蒙古自治区税务局\n发票号码：25152000000077385777\n开票日期：2025年12月24日\n购买方信息\n统一社会信用代码/纳税人识别号\n名称：国药控股国大药房内蒙古有限公司第三百七十三分公司\n统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46\n销售方信息\n项目名称\n规格型号\n单位\n数量\n单价\n金额\n税率/征收率\n税额\n*化学药品制剂*布地奈德\n320ug:9ug*60吸\n盒\n1\n306.930693069307\n306.93\n1%\n3.07\n福莫特罗吸入粉雾剂\n合计\n￥306.93\n￥3.07\n价税合计(大写)\n叁佰壹拾圆整\n(小写)￥310.00\n收款人:马利亚;\n复核人:梁会荣\n备注\n开票人:梁会荣",
    "role": "user"
  }
]
[92m06:10:48 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:48,401 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:10:51,408 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:10:51.407+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"2de9b1b0909411f1a3da71efcdd7cc1f": {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:10:51,505 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:10:51,505 INFO     29 [qwen-vl-text] LLM output (len=442):
{
  "encounter_date": "2025-12-24",
  "pharmacy": "国药控股国大药房内蒙古有限公司第三百七十三分公司",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸",
      "dosage": null,
      "quantity": 1,
      "unit_price": 306.93,
      "total_price": 306.93,
      "frequency": null,
      "route": null,
      "manufacturer": null,
      "approval_number": null
    }
  ],
  "payment_total": 310.00,
  "payment_method": null
}
2026-08-05 06:10:51,505 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-24]
2026-08-05 06:10:51,506 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1352692, prompt_len=1063
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共37行）
["电子发票(普通发票)", "国家税务总局", "内蒙古自治区税务局", "发票号码：25152000000077385777", "开票日期：2025年12月24日", "购买方信息", "统一社会信用代码/纳税人识别号", "名称：国药控股国大药房内蒙古有限公司第三百七十三分公司", "统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46", "销售方信息", "项目名称", "规格型号", "单位", "数量", "单价", "金额", "税率/征收率", "税额", "*化学药品制剂*布地奈德", "320ug:9ug*60吸", "盒", "1", "306.930693069307", "306.93", "1%", "3.07", "福莫特罗吸入粉雾剂", "合计", "￥306.93", "￥3.07", "价税合计(大写)", "叁佰壹拾圆整", "(小写)￥310.00", "收款人:马利亚;", "复核人:梁会荣", "备注", "开票人:梁会荣"]

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
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord API raw response (len=3248):
[
	{"text": "电子发票(普通发票)", "bbox": [328, 80, 645, 129], "bbox_2d": [328, 80, 645, 129]},
	{"text": "国家税务总局", "bbox": [465, 143, 536, 158], "bbox_2d": [465, 143, 536, 158]},
	{"text": "内蒙古自治区税务局", "bbox": [448, 170, 553, 210], "bbox_2d": [448, 170, 553, 210]},
	{"text": "发票号码：25152000000077385777", "bbox": [738, 103, 965, 125], "bbox_2d": [738, 103, 965, 125]},
	{"text": "开票日期：2025年12月24日", "bbox": [738, 146, 918, 168], "bbox_2d": [738, 146, 918, 168]},
	{"text": "购买方信息", "bbox": [32, 256, 45, 378], "bbox_2d": [32, 256, 45, 378]},
	{"text": "统一社会信用代码/纳税人识别号", "bbox": [58, 340, 251, 360], "bbox_2d": [58, 340, 251, 360]},
	{"text": "名称：国药控股国大药房内蒙古有限公司第三百七十三分公司", "bbox": [536, 265, 937, 288], "bbox_2d": [536, 265, 937, 288]},
	{"text": "统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46", "bbox": [535, 340, 956, 363], "bbox_2d": [535, 340, 956, 363]},
	{"text": "销售方信息", "bbox": [510, 257, 523, 379], "bbox_2d": [510, 257, 523, 379]},
	{"text": "项目名称", "bbox": [80, 403, 140, 423], "bbox_2d": [80, 403, 140, 423]},
	{"text": "规格型号", "bbox": [202, 404, 262, 424], "bbox_2d": [202, 404, 262, 424]},
	{"text": "单位", "bbox": [322, 404, 367, 424], "bbox_2d": [322, 404, 367, 424]},
	{"text": "数量", "bbox": [445, 405, 491, 425], "bbox_2d": [445, 405, 491, 425]},
	{"text": "单价", "bbox": [565, 405, 609, 425], "bbox_2d": [565, 405, 609, 425]},
	{"text": "金额", "bbox": [687, 406, 731, 426], "bbox_2d": [687, 406, 731, 426]},
	{"text": "税率/征收率", "bbox": [752, 406, 837, 426], "bbox_2d": [752, 406, 837, 426]},
	{"text": "税额", "bbox": [929, 406, 975, 426], "bbox_2d": [929, 406, 975, 426]},
	{"text": "*化学药品制剂*布地奈德", "bbox": [25, 424, 190, 447], "bbox_2d": [25, 424, 190, 447]},
	{"text": "320ug:9ug*60吸", "bbox": [201, 428, 309, 450], "bbox_2d": [201, 428, 309, 450]},
	{"text": "盒", "bbox": [335, 428, 352, 450], "bbox_2d": [335, 428, 352, 450]},
	{"text": "1", "bbox": [482, 430, 491, 449], "bbox_2d": [482, 430, 491, 449]},
	{"text": "306.930693069307", "bbox": [502, 430, 609, 449], "bbox_2d": [502, 430, 609, 449]},
	{"text": "306.93", "bbox": [686, 430, 731, 450], "bbox_2d": [686, 430, 731, 450]},
	{"text": "1%", "bbox": [789, 432, 804, 450], "bbox_2d": [789, 432, 804, 450]},
	{"text": "3.07", "bbox": [951, 432, 982, 451], "bbox_2d": [951, 432, 982, 451]},
	{"text": "福莫特罗吸入粉雾剂", "bbox": [25, 457, 160, 479], "bbox_2d": [25, 457, 160, 479]},
	{"text": "合计", "bbox": [105, 678, 118, 696], "bbox_2d": [105, 678, 118, 696]},
	{"text": "计", "bbox": [178, 678, 192, 697], "bbox_2d": [178, 678, 192, 697]},
	{"text": "￥306.93", "bbox": [677, 684, 733, 704], "bbox_2d": [677, 684, 733, 704]},
	{"text": "￥3.07", "bbox": [940, 685, 982, 706], "bbox_2d": [940, 685, 982, 706]},
	{"text": "价税合计(大写)", "bbox": [88, 721, 198, 743], "bbox_2d": [88, 721, 198, 743]},
	{"text": "叁佰壹拾圆整", "bbox": [303, 720, 393, 743], "bbox_2d": [303, 720, 393, 743]},
	{"text": "(小写)￥310.00", "bbox": [692, 727, 808, 752], "bbox_2d": [692, 727, 808, 752]},
	{"text": "收款人:马利亚;", "bbox": [60, 760, 163, 782], "bbox_2d": [60, 760, 163, 782]},
	{"text": "复核人:梁会荣", "bbox": [193, 763, 291, 785], "bbox_2d": [193, 763, 291, 785]},
	{"text": "备注", "bbox": [38, 793, 51, 812], "bbox_2d": [38, 793, 51, 812]},
	{"text": "开票人:梁会荣", "bbox": [100, 932, 200, 956], "bbox_2d": [100, 932, 200, 956]}
]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=17.1s
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[0]: text=电子发票(普通发票), bbox=[328, 80, 645, 129]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[1]: text=国家税务总局, bbox=[465, 143, 536, 158]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[2]: text=内蒙古自治区税务局, bbox=[448, 170, 553, 210]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[3]: text=发票号码：25152000000077385777, bbox=[738, 103, 965, 125]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[4]: text=开票日期：2025年12月24日, bbox=[738, 146, 918, 168]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[5]: text=购买方信息, bbox=[32, 256, 45, 378]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[6]: text=统一社会信用代码/纳税人识别号, bbox=[58, 340, 251, 360]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[7]: text=名称：国药控股国大药房内蒙古有限公司第三百七十三分公司, bbox=[536, 265, 937, 288]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[8]: text=统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46, bbox=[535, 340, 956, 363]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[9]: text=销售方信息, bbox=[510, 257, 523, 379]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[10]: text=项目名称, bbox=[80, 403, 140, 423]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[11]: text=规格型号, bbox=[202, 404, 262, 424]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[12]: text=单位, bbox=[322, 404, 367, 424]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[13]: text=数量, bbox=[445, 405, 491, 425]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[14]: text=单价, bbox=[565, 405, 609, 425]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[15]: text=金额, bbox=[687, 406, 731, 426]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[16]: text=税率/征收率, bbox=[752, 406, 837, 426]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[17]: text=税额, bbox=[929, 406, 975, 426]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[18]: text=*化学药品制剂*布地奈德, bbox=[25, 424, 190, 447]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[19]: text=320ug:9ug*60吸, bbox=[201, 428, 309, 450]
2026-08-05 06:11:08,643 INFO     29 [qwen-vl-text] coord item[20]: text=盒, bbox=[335, 428, 352, 450]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[21]: text=1, bbox=[482, 430, 491, 449]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[22]: text=306.930693069307, bbox=[502, 430, 609, 449]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[23]: text=306.93, bbox=[686, 430, 731, 450]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[24]: text=1%, bbox=[789, 432, 804, 450]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[25]: text=3.07, bbox=[951, 432, 982, 451]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[26]: text=福莫特罗吸入粉雾剂, bbox=[25, 457, 160, 479]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[27]: text=合计, bbox=[105, 678, 118, 696]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[28]: text=计, bbox=[178, 678, 192, 697]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[29]: text=￥306.93, bbox=[677, 684, 733, 704]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[30]: text=￥3.07, bbox=[940, 685, 982, 706]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[31]: text=价税合计(大写), bbox=[88, 721, 198, 743]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[32]: text=叁佰壹拾圆整, bbox=[303, 720, 393, 743]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[33]: text=(小写)￥310.00, bbox=[692, 727, 808, 752]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[34]: text=收款人:马利亚;, bbox=[60, 760, 163, 782]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[35]: text=复核人:梁会荣, bbox=[193, 763, 291, 785]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[36]: text=备注, bbox=[38, 793, 51, 812]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] coord item[37]: text=开票人:梁会荣, bbox=[100, 932, 200, 956]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] page=0 — 37/37 coords, api_time=17.1s
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] new_positions (37):
[[0, 276.176, 543.09, 47.599999999999994, 76.755], [0, 391.53, 451.312, 85.085, 94.00999999999999], [0, 377.216, 465.626, 101.14999999999999, 124.94999999999999], [0, 621.396, 812.53, 61.285, 74.375], [0, 621.396, 772.956, 86.86999999999999, 99.96], [0, 26.944, 37.89, 152.32, 224.91], [0, 48.836, 211.34199999999998, 202.29999999999998, 214.2], [0, 451.312, 788.954, 157.67499999999998, 171.35999999999999], [0, 450.46999999999997, 804.952, 202.29999999999998, 215.98499999999999], [0, 429.41999999999996, 440.366, 152.915, 225.505], [0, 67.36, 117.88, 239.785, 251.685], [0, 170.084, 220.60399999999998, 240.38, 252.28], [0, 271.12399999999997, 309.014, 240.38, 252.28], [0, 374.69, 413.42199999999997, 240.975, 252.875], [0, 475.72999999999996, 512.778, 240.975, 252.875], [0, 578.454, 615.502, 241.57, 253.47], [0, 633.184, 704.754, 241.57, 253.47], [0, 782.218, 820.9499999999999, 241.57, 253.47], [0, 21.05, 159.98, 252.28, 265.965], [0, 169.242, 260.178, 254.66, 267.75], [0, 282.07, 296.384, 254.66, 267.75], [0, 405.844, 413.42199999999997, 255.85, 267.155], [0, 422.68399999999997, 512.778, 255.85, 267.155], [0, 577.612, 615.502, 255.85, 267.75], [0, 664.338, 676.968, 257.03999999999996, 267.75], [0, 800.742, 826.8439999999999, 257.03999999999996, 268.34499999999997], [0, 21.05, 134.72, 271.91499999999996, 285.005], [0, 88.41, 99.356, 403.40999999999997, 414.12], [0, 149.876, 161.664, 403.40999999999997, 414.715], [0, 570.034, 617.1859999999999, 406.97999999999996, 418.88], [0, 791.48, 826.8439999999999, 407.575, 420.07], [0, 74.096, 166.716, 428.995, 442.085], [0, 255.126, 330.906, 428.4, 442.085], [0, 582.664, 680.336, 432.565, 447.44], [0, 50.519999999999996, 137.246, 452.2, 465.28999999999996], [0, 162.506, 245.022, 453.98499999999996, 467.075], [0, 31.996, 42.942, 471.835, 483.14]]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] ═══ DONE ═══ 37 positions, pages=1, time=20.5s
2026-08-05 06:11:08,644 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:11:08,644 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-05 06:11:08,958 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:11:08,958 INFO     29 [qwen-vl-text] LLM extraction start, text_len=205
2026-08-05 06:11:08,959 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:11:08,959 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 120, \"bbox_end\": 142, \"encounter_dates\": [\"2026-01-19\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "欣源药业\nNO:2026011900323\n商品名称\n单价\n数量\n小计\n布地奈德福莫特罗吸入粉雾剂320ug:\n9ug*60吸/盒\n309.00\n2\n618.00\n阿斯利康\n批号: PKGF\n效期:2027-03 规格:1支/盒\n总计:\n2.00\n618.00\n会员卡号:800310\n会员姓名:\n本次积分:618.00\n累计积分:2518.10\n收银员004营业员004\n日期26-01-1910:53:22",
    "role": "user"
  }
]
[92m06:11:08 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:08,960 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:15,716 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:11:15,716 INFO     29 [qwen-vl-text] LLM output (len=426):
{
  "encounter_date": "2026-01-19",
  "pharmacy": "欣源药业",
  "medications": [
    {
      "name": "布地奈德福莫特罗吸入粉雾剂",
      "specification": "320ug:9ug*60吸/盒",
      "dosage": null,
      "quantity": 2,
      "unit_price": 309.00,
      "total_price": 618.00,
      "frequency": null,
      "route": null,
      "manufacturer": "阿斯利康",
      "approval_number": null
    }
  ],
  "payment_total": 618.00,
  "payment_method": null
}
2026-08-05 06:11:15,716 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-19]
2026-08-05 06:11:15,728 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2602355, prompt_len=887
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["欣源药业", "NO:2026011900323", "商品名称", "单价", "数量", "小计", "布地奈德福莫特罗吸入粉雾剂320ug:", "9ug*60吸/盒", "309.00", "2", "618.00", "阿斯利康", "批号: PKGF", "效期:2027-03 规格:1支/盒", "总计:", "2.00", "618.00", "会员卡号:800310", "会员姓名:", "本次积分:618.00", "累计积分:2518.10", "收银员004营业员004", "日期26-01-1910:53:22"]

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
2026-08-05 06:11:23,541 INFO     29 [qwen-vl-text] coord API raw response (len=1204):
[
	{"text": "欣源药业", "bbox": [408, 207, 636, 252]},
	{"text": "NO:2026011900323", "bbox": [148, 296, 502, 330]},
	{"text": "商品名称", "bbox": [148, 335, 327, 370],
	"bbox": [464, 340, 550, 374]},
	{"text": "单价", "bbox": [594, 341, 683, 374]},
	{"text": "小计", "bbox": [752, 341, 843, 374]},
	{"text": "布地奈德福莫特罗吸入粉雾剂320ug:", "bbox": [148, 417, 868, 454]},
	{"text": "9ug*60吸/盒", "bbox": [144, 460, 422, 494]},
	{"text": "309.00", "bbox": [485, 464, 621, 491]},
	{"text": "2", "bbox": [659, 464, 685, 491]},
	{"text": "618.00", "bbox": [752, 464, 895, 491]},
	{"text": "阿斯利康", "bbox": [144, 500, 324, 534]},
	{"text": "批号: PKGF", "bbox": [440, 501, 664, 533]},
	{"text": "效期:2027-03 规格:1支/盒", "bbox": [144, 540, 706, 574]},
	{"text": "总计:", "bbox": [144, 624, 247, 658]},
	{"text": "2.00", "bbox": [461, 626, 553, 654]},
	{"text": "618.00", "bbox": [672, 627, 811, 656]},
	{"text": "会员卡号:800310", "bbox": [144, 665, 498, 698]},
	{"text": "会员姓名:", "bbox": [144, 704, 338, 738]},
	{"text": "本次积分:618.00", "bbox": [142, 784, 498, 819]},
	{"text": "累计积分:2518.10", "bbox": [144, 827, 521, 861]},
	{"text": "收银员004营业员004", "bbox": [142, 865, 586, 900]},
	{"text": "日期26-01-1910:53:22", "bbox": [144, 907, 631, 938]}
]
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=7.8s
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord item[0]: text=欣源药业, bbox=[408, 207, 636, 252]
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord item[1]: text=NO:2026011900323, bbox=[148, 296, 502, 330]
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord item[2]: text=商品名称, bbox=[464, 340, 550, 374]
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord item[3]: text=单价, bbox=[594, 341, 683, 374]
2026-08-05 06:11:23,542 INFO     29 [qwen-vl-text] coord item[4]: text=小计, bbox=[752, 341, 843, 374]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[5]: text=布地奈德福莫特罗吸入粉雾剂320ug:, bbox=[148, 417, 868, 454]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[6]: text=9ug*60吸/盒, bbox=[144, 460, 422, 494]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[7]: text=309.00, bbox=[485, 464, 621, 491]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[8]: text=2, bbox=[659, 464, 685, 491]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[9]: text=618.00, bbox=[752, 464, 895, 491]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[10]: text=阿斯利康, bbox=[144, 500, 324, 534]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[11]: text=批号: PKGF, bbox=[440, 501, 664, 533]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[12]: text=效期:2027-03 规格:1支/盒, bbox=[144, 540, 706, 574]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[13]: text=总计:, bbox=[144, 624, 247, 658]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[14]: text=2.00, bbox=[461, 626, 553, 654]
2026-08-05 06:11:23,543 INFO     29 [qwen-vl-text] coord item[15]: text=618.00, bbox=[672, 627, 811, 656]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[16]: text=会员卡号:800310, bbox=[144, 665, 498, 698]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[17]: text=会员姓名:, bbox=[144, 704, 338, 738]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[18]: text=本次积分:618.00, bbox=[142, 784, 498, 819]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[19]: text=累计积分:2518.10, bbox=[144, 827, 521, 861]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[20]: text=收银员004营业员004, bbox=[142, 865, 586, 900]
2026-08-05 06:11:23,544 INFO     29 [qwen-vl-text] coord item[21]: text=日期26-01-1910:53:22, bbox=[144, 907, 631, 938]
2026-08-05 06:11:23,545 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=7.8s
2026-08-05 06:11:23,545 INFO     29 [qwen-vl-text] new_positions (23):
[[4, 242.76, 378.41999999999996, 174.29399999999998, 212.184], [4, 88.06, 298.69, 249.232, 277.86], [4, 276.08, 327.25, 286.28, 314.908], [4, 353.43, 406.385, 287.122, 314.908], [4, 447.44, 501.585, 287.122, 314.908], [4, 88.06, 516.4599999999999, 351.114, 382.268], [4, 85.67999999999999, 251.08999999999997, 387.32, 415.948], [4, 288.575, 369.495, 390.688, 413.42199999999997], [4, 392.10499999999996, 407.575, 390.688, 413.42199999999997], [4, 447.44, 532.525, 390.688, 413.42199999999997], [4, 85.67999999999999, 192.78, 421.0, 449.628], [4, 261.8, 395.08, 421.842, 448.786], [4, 85.67999999999999, 420.07, 454.68, 483.308], [4, 85.67999999999999, 146.965, 525.408, 554.036], [4, 274.295, 329.03499999999997, 527.092, 550.668], [4, 399.84, 482.54499999999996, 527.934, 552.352], [4, 85.67999999999999, 296.31, 559.93, 587.716], [4, 85.67999999999999, 201.10999999999999, 592.768, 621.396], [4, 84.49, 296.31, 660.1279999999999, 689.598], [4, 85.67999999999999, 309.995, 696.334, 724.962], [4, 84.49, 348.66999999999996, 728.3299999999999, 757.8], [4, 85.67999999999999, 375.445, 763.694, 789.7959999999999], [4, 85.67999999999999, 375.445, 763.694, 789.7959999999999]]
2026-08-05 06:11:23,545 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=14.9s
2026-08-05 06:11:23,546 INFO     29 extractor ocr_parser=qwen-vl, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-05 06:11:23,546 INFO     29 [qwen-vl-text] ═══ START ═══ type=MedicationRecord, doc_id=None
2026-08-05 06:11:23,547 INFO     29 [qwen-vl-text] positions(20): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-05 06:11:23,547 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [20]
2026-08-05 06:11:23,809 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-05 06:11:23,810 INFO     29 [qwen-vl-text] LLM extraction start, text_len=244
2026-08-05 06:11:23,810 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:11:23,810 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"MedicationRecord\", \"bbox_start\": 143, \"bbox_end\": 162, \"encounter_dates\": [\"2026-02-13\"], \"department\": \"呼吸内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的收款日期标识）：输出 JSON 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "内蒙古医科大学附属医院\n门诊缴费凭证\n诊疗号: 0011072747\n姓名:\n收费项目\n西药\n总额(元)\n301.53\n(取药窗口: 门诊二楼西药房3号窗口)\n开单科室: 呼吸内科门诊\n结算类型: 自费\n总金额: 301.53元\n实付金额: 301.53元\n机器编号: zzj217\n缴费时间: 2026-02-13 10:13:31\n支付方式: 微信\n交易订单号: 39N6260213101311FYAzzj217D4230\n温馨提示:\n如需发票, 请关注我院微信公众号获取\n电子发票",
    "role": "user"
  }
]
[92m06:11:23 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:23,811 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:24,608 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-05T06:11:24.607+00:00", "boot_at": "2026-08-05T03:06:58.931+00:00", "pending": 7, "lag": 0, "done": 24, "failed": 0, "current": {"2de9b1b0909411f1a3da71efcdd7cc1f": {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-05 06:11:25,708 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:11:25,708 INFO     29 [qwen-vl-text] LLM output (len=139):
{
  "encounter_date": "2026-02-13",
  "pharmacy": "门诊二楼西药房3号窗口",
  "medications": [],
  "payment_total": 301.53,
  "payment_method": "微信"
}
2026-08-05 06:11:25,708 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-13]
2026-08-05 06:11:25,711 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1773307, prompt_len=917
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["内蒙古医科大学附属医院", "门诊缴费凭证", "诊疗号: 0011072747", "姓名:", "收费项目", "西药", "总额(元)", "301.53", "(取药窗口: 门诊二楼西药房3号窗口)", "开单科室: 呼吸内科门诊", "结算类型: 自费", "总金额: 301.53元", "实付金额: 301.53元", "机器编号: zzj217", "缴费时间: 2026-02-13 10:13:31", "支付方式: 微信", "交易订单号: 39N6260213101311FYAzzj217D4230", "温馨提示:", "如需发票, 请关注我院微信公众号获取", "电子发票"]

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
2026-08-05 06:11:32,556 INFO     29 [qwen-vl-text] coord API raw response (len=1123):
[
	{"text": "内蒙古医科大学附属医院", "bbox": [292, 14, 808, 47]},
	{"text": "门诊缴费凭证", "bbox": [402, 43, 626, 67]},
	{"text": "诊疗号: 0011072747", "bbox": [252, 280, 554, 311]},
	{"text": "姓名:", "bbox": [255, 327, 360, 361]},
	{"text": "收费项目", "bbox": [255, 388, 391, 417]},
	{"text": "西药", "bbox": [255, 428, 317, 454]},
	{"text": "总额(元)", "bbox": [691, 385, 812, 417]},
	{"text": "301.53", "bbox": [688, 430, 782, 452]},
	{"text": "(取药窗口: 门诊二楼西药房3号窗口)", "bbox": [268, 457, 808, 485]},
	{"text": "开单科室: 呼吸内科门诊", "bbox": [255, 496, 620, 522]},
	{"text": "结算类型: 自费", "bbox": [255, 557, 500, 584]},
	{"text": "总金额: 301.53元", "bbox": [255, 596, 551, 622]},
	{"text": "实付金额: 301.53元", "bbox": [255, 635, 551, 661]},
	{"text": "机器编号: zzj217", "bbox": [255, 687, 515, 715]},
	{"text": "缴费时间: 2026-02-13 10:13:31", "bbox": [255, 719, 698, 743]},
	{"text": "支付方式: 微信", "bbox": [255, 747, 491, 774]},
	{"text": "交易订单号: 39N6260213101311FYAzzj217D4230", "bbox": [255, 778, 741, 798]},
	{"text": "温馨提示:", "bbox": [255, 833, 394, 859]},
	{"text": "如需发票, 请关注我院微信公众号获取", "bbox": [255, 871, 790, 898]},
	{"text": "电子发票", "bbox": [255, 909, 381, 933]}
]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=6.8s
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[0]: text=内蒙古医科大学附属医院, bbox=[292, 14, 808, 47]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[1]: text=门诊缴费凭证, bbox=[402, 43, 626, 67]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗号: 0011072747, bbox=[252, 280, 554, 311]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[255, 327, 360, 361]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[4]: text=收费项目, bbox=[255, 388, 391, 417]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[5]: text=西药, bbox=[255, 428, 317, 454]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[6]: text=总额(元), bbox=[691, 385, 812, 417]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[7]: text=301.53, bbox=[688, 430, 782, 452]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[8]: text=(取药窗口: 门诊二楼西药房3号窗口), bbox=[268, 457, 808, 485]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[9]: text=开单科室: 呼吸内科门诊, bbox=[255, 496, 620, 522]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[10]: text=结算类型: 自费, bbox=[255, 557, 500, 584]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[11]: text=总金额: 301.53元, bbox=[255, 596, 551, 622]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[12]: text=实付金额: 301.53元, bbox=[255, 635, 551, 661]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[13]: text=机器编号: zzj217, bbox=[255, 687, 515, 715]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[14]: text=缴费时间: 2026-02-13 10:13:31, bbox=[255, 719, 698, 743]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[15]: text=支付方式: 微信, bbox=[255, 747, 491, 774]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[16]: text=交易订单号: 39N6260213101311FYAzzj217D4230, bbox=[255, 778, 741, 798]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[17]: text=温馨提示:, bbox=[255, 833, 394, 859]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[18]: text=如需发票, 请关注我院微信公众号获取, bbox=[255, 871, 790, 898]
2026-08-05 06:11:32,557 INFO     29 [qwen-vl-text] coord item[19]: text=电子发票, bbox=[255, 909, 381, 933]
2026-08-05 06:11:32,558 INFO     29 [qwen-vl-text] page=5 — 20/20 coords, api_time=6.8s
2026-08-05 06:11:32,558 INFO     29 [qwen-vl-text] new_positions (20):
[[5, 173.73999999999998, 480.76, 11.788, 39.574], [5, 239.19, 372.46999999999997, 36.205999999999996, 56.414], [5, 149.94, 329.63, 235.76, 261.86199999999997], [5, 151.725, 214.2, 275.334, 303.962], [5, 151.725, 232.64499999999998, 326.69599999999997, 351.114], [5, 151.725, 188.61499999999998, 360.376, 382.268], [5, 411.145, 483.14, 324.17, 351.114], [5, 409.35999999999996, 465.28999999999996, 362.06, 380.584], [5, 159.45999999999998, 480.76, 384.794, 408.37], [5, 151.725, 368.9, 417.632, 439.524], [5, 151.725, 297.5, 468.99399999999997, 491.728], [5, 151.725, 327.84499999999997, 501.832, 523.7239999999999], [5, 151.725, 327.84499999999997, 534.67, 556.562], [5, 151.725, 306.425, 578.454, 602.03], [5, 151.725, 415.31, 605.398, 625.606], [5, 151.725, 292.145, 628.9739999999999, 651.708], [5, 151.725, 440.895, 655.076, 671.9159999999999], [5, 151.725, 234.42999999999998, 701.386, 723.278], [5, 151.725, 470.04999999999995, 733.382, 756.116], [5, 151.725, 226.695, 765.3779999999999, 785.586]]
2026-08-05 06:11:32,558 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=9.0s
2026-08-05 06:11:32,568 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-05 06:11:32,569 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Medication | outputs={"chunks": "3 items, types={'MedicationRecord': 3}", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:11:32,569 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-05 06:11:32,573 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:11:32,573 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条处方：输出单个 JSON 对象\n- 如果原文包含多条处方（由不同的处方日期标识）：输出 JSON 数组\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:11:32 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:32,575 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:34,060 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:11:34,069 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-05 06:11:34,069 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:11:34,069 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-05 06:11:34,074 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:11:34,074 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:11:34 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:34,075 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:37,251 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:11:37,262 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-05 06:11:37,262 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:11:37,262 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-05 06:11:37,270 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:11:37,271 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-05 06:11:37,867 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-05 06:11:37,875 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-05 06:11:37,875 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:11:37,876 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-05 06:11:37,882 INFO     29 [LLM] Extractor call: llm_id=qwen3.7-max
2026-08-05 06:11:37,882 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
[92m06:11:37 - LiteLLM:INFO[0m: utils.py:3895 - 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:37,883 INFO     29 
LiteLLM completion() model= qwen3.7-max; provider = dashscope
2026-08-05 06:11:39,451 INFO     29 [LLM] Extractor response: llm_id=qwen3.7-max
2026-08-05 06:11:39,461 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-05 06:11:39,462 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "163 items", "markdown": "", "text": "", "name": "麦济ZHGL.pdf", "output_format": "chunks", "chunks_Medication": "3 items, types={'MedicationRecord': 3}", "chunks_Clinical": "2 items, types={'OutpatientRecord': 2}", "route_summary": "{\"chunks_Medication\": 3, \"chunks_Clinical\": 2}"}
2026-08-05 06:11:39,462 INFO     29 [Pipeline] Executing component [12]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-05 06:11:39,463 INFO     29 [ChunkMerger] Merged 5 chunks from 8 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 2, 'Extractor:Medication': 3, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1} (filtered 6 noise chunks)
2026-08-05 06:11:39,480 INFO     29 [Pipeline] Component [12]: ChunkMerger:Merger finished. error=None
2026-08-05 06:11:39,480 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3}", "name": "麦济ZHGL.pdf"}
2026-08-05 06:11:39,480 INFO     29 [Pipeline] Executing component [13]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-05 06:11:39,558 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1785910154176, 'update_date': datetime.datetime(2026, 8, 5, 6, 9, 14), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 247698, 'status': '1'}
2026-08-05 06:11:39,790 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=内蒙古医科大学附属医院门诊病历
姓名：
年龄：51岁
诊疗号：0011072747
民族：汉族
性别：女性
内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2020-02-13 09:12
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：哮喘史，近几日咳嗽、胸闷气短症状加重
现病史：哮喘史，近几日咳嗽、胸闷气短症状加重
既往史：患者平素身体健康，高血压无，糖尿病无，心脏病无，肺结核无，鼻炎
无，吸烟史无，无过敏史。
体格检查：发育正常，营养良好，体型正力，双肺呼吸音清，双肺未闻及啰
音，双下肢无水肿，体重kg。
辅助检查：心肺
过敏史：不详
初步诊断（西医）：1.支气管哮喘(急性发作期)
初步诊断（中医）：
治疗方案：随诊
醋酸泼尼松片<5mg>
用量：3.000片/次
用法：口服，一次/日，5天
布地奈德福莫特罗吸入粉雾剂
用量：1.000吸/次
(II)<(320μg/9μg)/吸*60>
用法：吸入，二次/日，30天
签名：
---
内蒙古医科大学附属医院门诊病历
姓名：
年龄：51岁
诊疗号：0011072747
民族：汉族
性别：女性
呼吸内科门诊
联系电话：
身份证：
病情：
就诊状态：
就诊时间：2026-02-09 07:39
生命体征（需要时）：
体温：℃ 脉搏：次/分 呼吸：次/分 血压：/mmHg
主诉：本次为V16访视
现病史：今患者按约回院，受试者自上次访视至今，哮喘症状控制平稳，无哮
喘急性恶化，无哮喘急性发作，无AE，无SAE，无新增合并用药或非
药物治疗。检查并回收发放的日记卡1本，版本号/版本日期
(V2.0/20250916)，受试者日记卡填写正确，发放新的日记卡1本，
指导受试者填写。患者诉自上次访视至今未使用硫酸沙丁胺醇气雾剂
(万托林)，既往发放批号：6J7C，有效期2026-7患者今日出门忘
记携带，嘱患者从今日起停用，择期尽快送回。
既往史：背景用药：2022.12.4-至今规律吸入布地奈德福莫特罗吸入粉雾剂
<(320μg/9μg)用量：1.000吸/次用法：吸入，二次/日 类别
ICS+LABA。
既往病史：
1.肝功能异常：开始时间：2024.12.05，筛选时持续，筛选时接受治
疗，查看今日血生化结果：ALT:46.9U/L，正常值范围：7-40 U/L 评
判结果：NCS；SAT：27.7 U/L，正常值范围：27.7 U/L在正常值范围
内；AST/ALT 0.6 正常值范围：0.8-2 评判结果NCS；以上异常结果与
筛选期结果比较，无恶化，持续状态，故不继续跟进。嘱患者定期复
查肝功。
2.尿路感染：开始时间：2024.12.05，筛选时持续，因患者无不适症
状，未行药物或非药物与治疗。今日查看结果：白细胞：3+，白细胞
计数：169.70；上皮细胞：31.00；管型：1.53 评判结果均CS异常
有临床意义，以上异常结果与筛选期结果比较，无恶化，持续状态，
嘱患者必要时会诊，行药物或非药物治疗，建议4周后回院复查。
此外无持续跟进AE。
体格检查：
辅助检查：8:35休息至少5min完成生命体征检查，结果详见生命体征表；至
少空腹8h，8:36空腹采集血生化、凝血检查，8:56留尿常规检
查，8:30按照中心实验室要求，采集血常规、ADA/Nab检查，按照
要求处理储存并寄送。
过敏史：
初步诊断（西医）：1.支气管哮喘
初步诊断（中医）：
治疗方案：随诊告知受试者继续规律吸入布地奈德福莫特罗吸入粉雾剂
(II)<(320μg/9μg)/吸*60>用量:1.000吸/次用法:吸入,二次/
日。告知患者今日出组。4周后会回院复测尿常规。患者表示无症状，未给予明确答复是否回院，4周后电话联系。
签名：
---
电子发票(普通发票)
国家税务总局
内蒙古自治区税务局
发票号码：25152000000077385777
开票日期：2025年12月24日
购买方信息
统一社会信用代码/纳税人识别号
名称：国药控股国大药房内蒙古有限公司第三百七十三分公司
统一社会信用代码/纳税人识别号：91150121MACGJJ2Q46
销售方信息
项目名称
规格型号
单位
数量
单价
金额
税率/征收率
税额
*化学药品制剂*布地奈德
320ug:9ug*60吸
盒
1
306.930693069307
306.93
1%
3.07
福莫特罗吸入粉雾剂
合计
￥306.93
￥3.07
价税合计(大写)
叁佰壹拾圆整
(小写)￥310.00
收款人:马利亚;
复核人:梁会荣
备注
开票人:梁会荣
---
欣源药业
NO:2026011900323
商品名称
单价
数量
小计
布地奈德福莫特罗吸入粉雾剂320ug:
9ug*60吸/盒
309.00
2
618.00
阿斯利康
批号: PKGF
效期:2027-03 规格:1支/盒
总计:
2.00
618.00
会员卡号:800310
会员姓名:
本次积分:618.00
累计积分:2518.10
收银员004营业员004
日期26-01-1910:53:22
---
内蒙古医科大学附属医院
门诊缴费凭证
诊疗号: 0011072747
姓名:
收费项目
西药
总额(元)
301.53
(取药窗口: 门诊二楼西药房3号窗口)
开单科室: 呼吸内科门诊
结算类型: 自费
总金额: 301.53元
实付金额: 301.53元
机器编号: zzj217
缴费时间: 2026-02-13 10:13:31
支付方式: 微信
交易订单号: 39N6260213101311FYAzzj217D4230
温馨提示:
如需发票, 请关注我院微信公众号获取
电子发票
2026-08-05 06:11:40,121 INFO     29 [Pipeline] Component [13]: Tokenizer:MedEmbed finished. error=None
2026-08-05 06:11:40,121 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "5 items, types={'OutpatientRecord': 2, 'MedicationRecord': 3}", "name": "麦济ZHGL.pdf", "embedding_token_consumption": 1849}
2026-08-05 06:11:40,121 INFO     29 [Pipeline] Executing component [14]: Invoke:SyncChunks (type=Invoke)
2026-08-05 06:11:40,706 INFO     29 [Pipeline] Component [14]: Invoke:SyncChunks finished. error=None
2026-08-05 06:11:40,707 INFO     29 [Trace] task=2de9b1b0 | doc=麦济ZHGL.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":5,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-05 06:11:40,714 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:11:40,714 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:11:40,714 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:11:40,714 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:11:40,714 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-05 06:11:40,721 INFO     29 set_progress(2de9b1b0909411f1a3da71efcdd7cc1f), progress: 0.82, progress_msg: 06:11:40 [DOC Engine]:
Start to index...
2026-08-05 06:11:40,747 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-05 06:11:40,750 INFO     29 set_progress(2de9b1b0909411f1a3da71efcdd7cc1f), progress: 0.8200000000000001, progress_msg: 
2026-08-05 06:11:40,760 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.006s]
2026-08-05 06:11:40,766 INFO     29 set_progress(2de9b1b0909411f1a3da71efcdd7cc1f), progress: 1.0, progress_msg: 06:11:40 Indexing done (0.05s). Task done (135.07s)
2026-08-05 06:11:40,769 INFO     29 [Done], chunks(5), token(1849), elapsed:135.07
2026-08-05 06:11:40,841 INFO     29 handle_task done for task {"id": "2de9b1b0909411f1a3da71efcdd7cc1f", "doc_id": "2d7d9c50909411f1a3da71efcdd7cc1f", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u9ea6\u6d4eZHGL.pdf", "type": "pdf", "location": "\u9ea6\u6d4eZHGL.pdf", "size": 4836707, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1785910152508, "task_type": "dataflow", "root_trace_id": "5b27b624452947d18730334830c3c912", "root_traceparent": "00-5b27b624452947d18730334830c3c912-4d04900f1004560c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
