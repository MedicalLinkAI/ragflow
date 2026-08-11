# 基准结果：HXJ 哮喘 广三.pdf

## 基本信息

- 文件：`HXJ 哮喘 广三.pdf`
- 大小：8215.2 KB
- PDF 总页数：17
- doc_id：`4e37d76a94ab11f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T19:04:48  完成时间：2026-08-10T19:16:03  耗时：675.1s
- progress_msg：`11:16:02 Indexing done (0.11s). Task done (645.30s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | e4ad7964 | 1 | 1-1 | 门(急)诊病历信息 就诊卡 流水 病历编号: 姓 别:男 年 龄:64岁 就诊科 |
| 2 | d4d71231 | 1 | 2-2 | 门(急)诊病历信息 就诊卡号: 流水号: 病历编号: 性别:男 年 龄:65岁  |
| 3 | a7cb693b | 2 | 3-4 | 门(急)诊病历信息 就诊卡号 流水 姓名 性别:男 年 龄:65岁 就诊科室:内 |
| 4 | d9e7bf15 | 1 | 5-5 | 门(急)诊处方 就诊时间:2025-09-15 就诊科室:内科门诊 主诊医 姓名 |
| 5 | 5f5af593 | 1 | 6-6 | 门(急)诊处方 就诊时间:2025-08-18 就诊科室:内科门诊 主诊 姓名: |
| 6 | 51ecfc7f | 1 | 7-7 | 门(急)诊处方 就诊时间:2025-05-30 就诊科室:内科门诊 主 姓名 性 |
| 7 | e363a5d2 | 1 | 8-8 | 门(急)诊处方 就诊时间:2025-03-05 就诊科室:内科门诊 主诊医 姓名 |
| 8 | 865edfa6 | 1 | 9-9 | 门(急)诊处方 就诊时间:2025-03-05 就诊科室:内科门诊 主诊 姓名  |
| 9 | 7de345a7 | 1 | 10-10 | 门(急)诊处方 就诊时间:2025-02-08 就诊科室:内科门诊 主诊 姓名: |
| 10 | df179c16 | 1 | 11-11 | 门(急)诊处方 就诊时间:2025-01-10 就诊科室:内科门诊 主诊 性别: |
| 11 | f6055ae9 | 1 | 12-12 | 门(急)诊处方 就诊时间:2024-12-11 就诊科室:内科门诊 主诊 姓名: |
| 12 | e857aff1 | 1 | 13-13 | 门(急)诊处方 就诊时间:2024-11-18 就诊科室:内科门诊 主诊 姓名  |
| 13 | f85a75c0 | 1 | 15-15 | 处方笺 普通 诊疗 患者姓 男 年龄：65岁 费别： 科室： 2026-01-0 |
| 14 | b0b979f9 | 1 | 16-16 | 处方笺 普通 诊断 患者 年龄：65岁 费别 科室 6-01-06 11:31: |
| 15 | 5068fefb | 1 | 17-17 | 病历编号： 姓名： 性别：男 年龄：65岁 就诊科室：内科门诊（基础） 医生：  |
| 16 | 3c6f76f8 | 1 | 14-14 | <table><tr><td>白细胞</td><td>WBC</td><td>9 |

- chunks 总数：16
- 各 chunk 页数合计（含跨页重复）：17
- 页码并集：`[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]`
- 覆盖页数：17 / 17；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：✅ 完全覆盖：chunk 页码并集 = PDF 总页数**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 4 | 0 | 4 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 0 | 1 | 0 | admission_date, discharge_date, department, outcome | **-** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 11 | 11 | 11 | encounter_date, prescriber, diagnosis | **OK** |
| ExaminationReport | 检查报告 | 0 | 1 | 0 | exam_date, report_date, exam_name, body_part, department | **-** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"OutpatientRecord": 4, "PrescriptionRecord": 11, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 16, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 4, "Extractor:Medication": 1, "Extractor:Prescription": 11, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 1, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：2 条
  - `[no_text_noise] 2026-08-10 11:15:16,498 INFO     29 [ChunkMerger] Merged 46 chunks from 9 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 14, 'Extractor:Medication': 1, 'Extractor:Pre`
  - `[no_text_noise] 2026-08-10 11:16:01,164 INFO     29 [ChunkMerger] Merged 16 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Presc`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 11:04:53,829 INFO     29 handle_task begin for task {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:04:54,085 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 11:04:54,215 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 11:04:54,536 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:04:54,536 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 11:04:54,537 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 11:04:54,543 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 11:04:54,543 INFO     29 ============================================================
2026-08-10 11:04:54,544 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 11:04:54,544 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 11:04:54,544 INFO     29 ============================================================
2026-08-10 11:04:54,544 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 11:04:54,544 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 11:04:54,546 INFO     29 No torch found.
2026-08-10 11:04:56,371 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=17
2026-08-10 11:04:56,893 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2726825, prompt_len=764
2026-08-10 11:04:58,363 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:04:58,364 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 11:04:58,373 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2726825, prompt_len=401
2026-08-10 11:05:02,076 INFO     29 [qwen-vl-parser] text API response (len=467):
["门(急)诊病历信息", "就诊卡", "流水", "病历编号:", "姓", "别:男", "年", "龄:64岁", "就诊科室:内科门诊(荔湾)", "医", "诊时间:2025-10-21 16:24:23", "主", "诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "支气管哮喘", "单病种:", "发病时间:", "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:建议在住地附近社区医疗机构随诊。", "病情评估:", "病情分级:", "是否抢救病例:否", "是否抢救成功:", "是否为绿色通道患者:否", "病人去向:", "病人来源:自行来院", "是否曾就诊于其他医疗机构:"]
2026-08-10 11:05:02,077 INFO     29 [qwen-vl-parser] page=1 text: 41 lines (bbox 0-40)
2026-08-10 11:05:02,077 INFO     29 [qwen-vl-parser] page=1 text: 41 sections
2026-08-10 11:05:02,325 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384260, prompt_len=764
2026-08-10 11:05:03,671 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:03,672 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 11:05:03,683 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1384260, prompt_len=401
2026-08-10 11:05:05,599 INFO     29 [qwen-vl-parser] text API response (len=314):
["门(急)诊病历信息", "就诊卡号:", "流水号:", "病历编号:", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "医生:", "就诊时间:2025-11-19 11:33:52", "主诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:"]
2026-08-10 11:05:05,599 INFO     29 [qwen-vl-parser] page=2 text: 29 lines (bbox 41-69)
2026-08-10 11:05:05,599 INFO     29 [qwen-vl-parser] page=2 text: 29 sections
2026-08-10 11:05:05,924 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2469560, prompt_len=764
2026-08-10 11:05:06,145 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:06,145 INFO     29 [qwen-vl-text] LLM output (len=3733):
{
  "encounter_date": "2022-05-09",
  "prescription_type": "门诊处方",
  "prescriber": "赵海国",
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
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "复方氨酚甲麻口服液",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": null,
      "frequency": "qid",
      "route": "口服",
      "duration_days": null,
      "quantity": null,
      "notes": null
    }
  ]
}
2026-08-10 11:05:06,146 INFO     29 [qwen-vl-text] Updated encounter_dates=[2022-05-09]
2026-08-10 11:05:06,147 INFO     29 [qwen-vl-text] coord API call start, page=36, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1030200, prompt_len=1776
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共25行）
["50/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView", "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "门.", "J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容，按回车键检索", "查询全部", "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚", "药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚", "药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛", "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "药品 乙1)美敏伪麻口服溶液 口服 tid 5ml 1 2022-04-19 16.05.18 陈媛", "药品 复方氨酚甲麻口服液 口服 qid 20条/页 < 1 2 3 4 > 前往 3 页", "共70条"]

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
2026-08-10 11:05:08,027 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:08,027 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 11:05:08,045 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2469560, prompt_len=401
2026-08-10 11:05:15,725 INFO     29 [qwen-vl-parser] text API response (len=1087):
["门(急)诊病历信息", "就诊卡号", "流水", "姓名", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "病历编号:", "就诊时间:2025-12-12 09:26:46", "主诉:BAIYUN V8", "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "完成下流操作:", "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "5、休息至少10分钟后,行12导联ECG检查。", "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:05:15,726 INFO     29 [qwen-vl-parser] page=3 text: 22 lines (bbox 70-91)
2026-08-10 11:05:15,726 INFO     29 [qwen-vl-parser] page=3 text: 22 sections
2026-08-10 11:05:16,093 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1994294, prompt_len=764
2026-08-10 11:05:17,684 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:17,684 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 11:05:17,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1994294, prompt_len=401
2026-08-10 11:05:21,324 INFO     29 [qwen-vl-text] coord API raw response (len=2163):
[
	{"text": "50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView", "bbox": [3, 43, 357, 60]},
	{"text": "984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "bbox": [5, 92, 426, 107]},
	{"text": "返回概览视图", "bbox": [918, 92, 976, 107]},
	{"text": "门.", "bbox": [8, 120, 20, 135]},
	{"text": "J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "bbox": [157, 120, 432, 135]},
	{"text": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "bbox": [21, 150, 585, 165]},
	{"text": "请输入药品内容，按回车键检索", "bbox": [19, 193, 134, 208]},
	{"text": "查询全部", "bbox": [214, 193, 262, 208]},
	{"text": "类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师", "bbox": [18, 226, 967, 244]},
	{"text": "药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国", "bbox": [18, 263, 967, 281]},
	{"text": "药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国", "bbox": [18, 281, 967, 300]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚", "bbox": [18, 300, 967, 319]},
	{"text": "药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [18, 319, 967, 338]},
	{"text": "药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [18, 338, 967, 357]},
	{"text": "药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚", "bbox": [18, 357, 967, 376]},
	{"text": "药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚", "bbox": [18, 376, 967, 395]},
	{"text": "药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚", "bbox": [18, 395, 967, 414]},
	{"text": "药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚", "bbox": [18, 414, 967, 433]},
	{"text": "药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚", "bbox": [18, 433, 967, 452]},
	{"text": "药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚", "bbox": [18, 452, 967, 471]},
	{"text": "药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛", "bbox": [18, 471, 967, 490]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛", "bbox": [18, 490, 967, 509]},
	{"text": "药品 乙1)美敏伪麻口服溶液 口服 tid 5ml 1 2022-04-19 16.05.18 陈媛", "bbox": [18, 509, 967, 528]},
	{"text": "药品 复方氨酚甲麻口服液 口服 qid 20条/页 < 1 2 3 4 > 前往 3 页", "bbox": [18, 528, 967, 547]},
	{"text": "共70条", "bbox": [719, 623, 749, 636]}
]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord API: raw_items=25, valid_items=25, elapsed=15.2s
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[0]: text=50/patientsMainPage.html?parentPageJump=1&&showTable=true#/patientView, bbox=[3, 43, 357, 60]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[1]: text=984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>, bbox=[5, 92, 426, 107]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[2]: text=返回概览视图, bbox=[918, 92, 976, 107]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[3]: text=门., bbox=[8, 120, 20, 135]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[4]: text=J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森, bbox=[157, 120, 432, 135]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[5]: text=集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告, bbox=[21, 150, 585, 165]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[6]: text=请输入药品内容，按回车键检索, bbox=[19, 193, 134, 208]
2026-08-10 11:05:21,325 INFO     29 [qwen-vl-text] coord item[7]: text=查询全部, bbox=[214, 193, 262, 208]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[8]: text=类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师, bbox=[18, 226, 967, 244]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[9]: text=药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国, bbox=[18, 263, 967, 281]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[10]: text=药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国, bbox=[18, 281, 967, 300]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[11]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚, bbox=[18, 300, 967, 319]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[12]: text=药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[18, 319, 967, 338]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[13]: text=药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[18, 338, 967, 357]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[14]: text=药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚, bbox=[18, 357, 967, 376]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[15]: text=药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚, bbox=[18, 376, 967, 395]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[16]: text=药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚, bbox=[18, 395, 967, 414]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[17]: text=药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚, bbox=[18, 414, 967, 433]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[18]: text=药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚, bbox=[18, 433, 967, 452]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[19]: text=药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚, bbox=[18, 452, 967, 471]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[20]: text=药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛, bbox=[18, 471, 967, 490]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[21]: text=药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛, bbox=[18, 490, 967, 509]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[22]: text=药品 乙1)美敏伪麻口服溶液 口服 tid 5ml 1 2022-04-19 16.05.18 陈媛, bbox=[18, 509, 967, 528]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[23]: text=药品 复方氨酚甲麻口服液 口服 qid 20条/页 < 1 2 3 4 > 前往 3 页, bbox=[18, 528, 967, 547]
2026-08-10 11:05:21,326 INFO     29 [qwen-vl-text] coord item[24]: text=共70条, bbox=[719, 623, 749, 636]
2026-08-10 11:05:21,327 INFO     29 [qwen-vl-text] page=36 — 25/25 coords, api_time=15.2s
2026-08-10 11:05:21,327 INFO     29 [qwen-vl-text] new_positions (25):
[[36, 2.526, 300.594, 25.584999999999997, 35.699999999999996], [36, 4.21, 358.692, 54.739999999999995, 63.665], [36, 772.956, 821.7919999999999, 54.739999999999995, 63.665], [36, 6.736, 16.84, 71.39999999999999, 80.325], [36, 132.194, 363.74399999999997, 71.39999999999999, 80.325], [36, 17.682, 492.57, 89.25, 98.175], [36, 15.998, 112.828, 114.835, 123.75999999999999], [36, 180.188, 220.60399999999998, 114.835, 123.75999999999999], [36, 15.155999999999999, 814.2139999999999, 134.47, 145.18], [36, 15.155999999999999, 814.2139999999999, 156.48499999999999, 167.195], [36, 15.155999999999999, 814.2139999999999, 167.195, 178.5], [36, 15.155999999999999, 814.2139999999999, 178.5, 189.80499999999998], [36, 15.155999999999999, 814.2139999999999, 189.80499999999998, 201.10999999999999], [36, 15.155999999999999, 814.2139999999999, 201.10999999999999, 212.415], [36, 15.155999999999999, 814.2139999999999, 212.415, 223.72], [36, 15.155999999999999, 814.2139999999999, 223.72, 235.02499999999998], [36, 15.155999999999999, 814.2139999999999, 235.02499999999998, 246.32999999999998], [36, 15.155999999999999, 814.2139999999999, 246.32999999999998, 257.635], [36, 15.155999999999999, 814.2139999999999, 257.635, 268.94], [36, 15.155999999999999, 814.2139999999999, 268.94, 280.245], [36, 15.155999999999999, 814.2139999999999, 280.245, 291.55], [36, 15.155999999999999, 814.2139999999999, 291.55, 302.85499999999996], [36, 15.155999999999999, 814.2139999999999, 302.85499999999996, 314.15999999999997], [36, 15.155999999999999, 814.2139999999999, 314.15999999999997, 325.465], [36, 605.398, 630.658, 370.685, 378.41999999999996]]
2026-08-10 11:05:21,327 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=1, time=27.8s
2026-08-10 11:05:21,327 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:05:21,329 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:05:21,330 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:05:21,330 INFO     29 [qwen-vl-text] positions(29): [[37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0], [37, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:05:21,330 INFO     29 [qwen-vl-text] page grouping: [37], lines per page: [29]
2026-08-10 11:05:21,531 INFO     29 [qwen-vl-text] page=37, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:05:21,533 INFO     29 [qwen-vl-text] LLM extraction start, text_len=832
2026-08-10 11:05:21,533 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:21,533 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 2030, \"bbox_end\": 2058, \"encounter_dates\": [\"2026-02-12\"], \"department\": \"呼吸危重三病区(门)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>\n返回概览视图\n2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森\n集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告\n请输入药品内容,按回车键检索\n查询全部\n类型 组 药品名称(规格)\n药品 甲)(小儿)双黄连口服液(基)\n药品 (盖克)小儿氨酚黄那敏颗粒\n药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)\n药品 蒲地蓝消炎口服液\n药品 复方氨酚甲麻口服液\n药品 (盖克)小儿氨酚黄那敏颗粒\n药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)\n药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)\n药品 右旋糖酐铁颗粒\n药品 盐酸氨卓斯丁滴眼液\n用法 频率 实际用量 总量 开立时间 开立医师\n口服 tid 10ml 1 2022-03-26 19:51:46 谭真真\n口服 tid 6g 2 2022-03-26 19:51:18 谭真真\n口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真\n口服 bid 10ml 1 2022-03-26 19:51:18 谭真真\n口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴\n口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴\n口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴\n压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅\n口服 tid 1袋 80 2021-09-28 15:12:34 党建华\n滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳\n共70条 20条/页 < 1 2 3 4 > 前往 4 页",
    "role": "user"
  }
]
2026-08-10 11:05:23,150 INFO     29 [qwen-vl-parser] text API response (len=834):
["门诊病历", "25/10/21 16时 门诊病历", "25/11/19 11时 门诊病历（GCP专用）", "25/12/12 09时 门诊病历（GCP专用）", "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试", "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "跟踪合并用药", "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏", "性鼻炎。", "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。", "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "入 qd 治疗急性支气管炎。", "预约下次安全性电话随访时间。", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "心电图(心电图室做)", "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "备注:", "医生:", ""]
2026-08-10 11:05:23,150 INFO     29 [qwen-vl-parser] page=4 text: 34 lines (bbox 92-125)
2026-08-10 11:05:23,150 INFO     29 [qwen-vl-parser] page=4 text: 34 sections
2026-08-10 11:05:23,546 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2243639, prompt_len=764
2026-08-10 11:05:24,825 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:05:24.822+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:05:25,026 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:25,026 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 11:05:25,041 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2243639, prompt_len=401
2026-08-10 11:05:27,755 INFO     29 [qwen-vl-parser] text API response (len=466):
["门(急)诊处方", "就诊时间:2025-09-15", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:4", "患者", "医疗证号:", "处方号", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "倍氯米松福莫特罗吸入气雾剂◆", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天", "医师", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "打印时间:2025-12-19", "为了您的用药安全,药物处方当天有效 第 1 页共 1 页", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:05:27,757 INFO     29 [qwen-vl-parser] page=5 text: 45 lines (bbox 126-170)
2026-08-10 11:05:27,757 INFO     29 [qwen-vl-parser] page=5 text: 45 sections
2026-08-10 11:05:27,922 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137495, prompt_len=764
2026-08-10 11:05:29,306 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-08-18"}
```
2026-08-10 11:05:29,307 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-08-18
2026-08-10 11:05:29,320 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1137495, prompt_len=401
2026-08-10 11:05:29,948 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:29,948 INFO     29 [qwen-vl-text] LLM output (len=2741):
{
  "encounter_date": "2026-02-12",
  "prescription_type": "住院处方",
  "prescriber": "孙帅森",
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
2026-08-10 11:05:29,949 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-12]
2026-08-10 11:05:29,952 INFO     29 [qwen-vl-text] coord API call start, page=37, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=772217, prompt_len=1532
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "返回概览视图", "2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "请输入药品内容,按回车键检索", "查询全部", "类型 组 药品名称(规格)", "药品 甲)(小儿)双黄连口服液(基)", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "药品 蒲地蓝消炎口服液", "药品 复方氨酚甲麻口服液", "药品 (盖克)小儿氨酚黄那敏颗粒", "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "药品 右旋糖酐铁颗粒", "药品 盐酸氨卓斯丁滴眼液", "用法 频率 实际用量 总量 开立时间 开立医师", "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "共70条 20条/页 < 1 2 3 4 > 前往 4 页"]

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
2026-08-10 11:05:33,003 INFO     29 [qwen-vl-parser] text API response (len=342):
["门(急)诊处方", "就诊时间:2025-08-18", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "28片", "1.05", "29.43", "Sig", "10mg/次,口服,qn*28天", "倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天"]
2026-08-10 11:05:33,004 INFO     29 [qwen-vl-parser] page=6 text: 34 lines (bbox 171-204)
2026-08-10 11:05:33,004 INFO     29 [qwen-vl-parser] page=6 text: 34 sections
2026-08-10 11:05:33,163 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1097037, prompt_len=764
2026-08-10 11:05:34,520 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:34,521 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=None
2026-08-10 11:05:34,533 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1097037, prompt_len=401
2026-08-10 11:05:36,783 INFO     29 [qwen-vl-parser] text API response (len=336):
["门(急)诊处方", "就诊时间:2025-05-30", "就诊科室:内科门诊", "主", "姓名", "性别:男", "年龄:64岁", "卡", "患者类型:GCP支付", "医疗证号:", "处", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*5/盒", "90片", "2.56", "230.58", "Sig", "10mg/次,口服,qn*90天", "倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶", "221.61", "664.83", "Sig", "2揿/次,吸入,bid*90天"]
2026-08-10 11:05:36,784 INFO     29 [qwen-vl-parser] page=7 text: 34 lines (bbox 205-238)
2026-08-10 11:05:36,784 INFO     29 [qwen-vl-parser] page=7 text: 34 sections
2026-08-10 11:05:36,975 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1235285, prompt_len=764
2026-08-10 11:05:38,488 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-03-05"}
```
2026-08-10 11:05:38,489 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-03-05
2026-08-10 11:05:38,510 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1235285, prompt_len=401
2026-08-10 11:05:40,794 INFO     29 [qwen-vl-parser] text API response (len=341):
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "221.61 443.22", "Sig", "2揿/次,吸入,bid*60天", "孟鲁司特钠片", "10mg*30/瓶", "60片", "1.05", "63.06", "Sig", "10mg/次,口服,qn*60天"]
2026-08-10 11:05:40,795 INFO     29 [qwen-vl-parser] page=8 text: 33 lines (bbox 239-271)
2026-08-10 11:05:40,795 INFO     29 [qwen-vl-parser] page=8 text: 33 sections
2026-08-10 11:05:40,967 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061616, prompt_len=764
2026-08-10 11:05:42,443 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:42,444 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 11:05:42,462 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1061616, prompt_len=401
2026-08-10 11:05:44,902 INFO     29 [qwen-vl-parser] text API response (len=366):
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:05:44,903 INFO     29 [qwen-vl-parser] page=9 text: 35 lines (bbox 272-306)
2026-08-10 11:05:44,903 INFO     29 [qwen-vl-parser] page=9 text: 35 sections
2026-08-10 11:05:45,111 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1455567, prompt_len=764
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord API raw response (len=2096):
[
	{"text": "184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>", "bbox": [6, 139, 427, 155]},
	{"text": "返回概览视图", "bbox": [923, 140, 980, 155]},
	{"text": "2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森", "bbox": [150, 169, 433, 184]},
	{"text": "集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告", "bbox": [19, 196, 587, 214]},
	{"text": "请输入药品内容,按回车键检索", "bbox": [19, 239, 134, 255]},
	{"text": "查询全部", "bbox": [212, 240, 262, 254]},
	{"text": "类型 组 药品名称(规格)", "bbox": [17, 271, 163, 289]},
	{"text": "药品 甲)(小儿)双黄连口服液(基)", "bbox": [17, 296, 204, 313]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒", "bbox": [17, 321, 204, 338]},
	{"text": "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)", "bbox": [17, 353, 271, 370]},
	{"text": "药品 蒲地蓝消炎口服液", "bbox": [17, 386, 175, 403]},
	{"text": "药品 复方氨酚甲麻口服液", "bbox": [17, 410, 183, 427]},
	{"text": "药品 (盖克)小儿氨酚黄那敏颗粒", "bbox": [17, 435, 205, 452]},
	{"text": "药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)", "bbox": [17, 467, 280, 484]},
	{"text": "药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)", "bbox": [17, 499, 277, 516]},
	{"text": "药品 右旋糖酐铁颗粒", "bbox": [17, 524, 167, 541]},
	{"text": "药品 盐酸氨卓斯丁滴眼液", "bbox": [17, 549, 184, 566]},
	{"text": "用法 频率 实际用量 总量 开立时间 开立医师", "bbox": [643, 271, 977, 289]},
	{"text": "口服 tid 10ml 1 2022-03-26 19:51:46 谭真真", "bbox": [643, 296, 968, 313]},
	{"text": "口服 tid 6g 2 2022-03-26 19:51:18 谭真真", "bbox": [643, 321, 968, 338]},
	{"text": "口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真", "bbox": [643, 345, 968, 370]},
	{"text": "口服 bid 10ml 1 2022-03-26 19:51:18 谭真真", "bbox": [643, 386, 968, 403]},
	{"text": "口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 410, 968, 427]},
	{"text": "口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 435, 968, 452]},
	{"text": "口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴", "bbox": [643, 467, 968, 484]},
	{"text": "压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅", "bbox": [643, 499, 968, 516]},
	{"text": "口服 tid 1袋 80 2021-09-28 15:12:34 党建华", "bbox": [643, 524, 968, 541]},
	{"text": "滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳", "bbox": [643, 549, 968, 566]},
	{"text": "共70条 20条/页 < 1 2 3 4 > 前往 4 页", "bbox": [723, 583, 985, 599]}
]
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=15.7s
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord item[0]: text=184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>, bbox=[6, 139, 427, 155]
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord item[1]: text=返回概览视图, bbox=[923, 140, 980, 155]
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord item[2]: text=2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森, bbox=[150, 169, 433, 184]
2026-08-10 11:05:45,673 INFO     29 [qwen-vl-text] coord item[3]: text=集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告, bbox=[19, 196, 587, 214]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[4]: text=请输入药品内容,按回车键检索, bbox=[19, 239, 134, 255]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[5]: text=查询全部, bbox=[212, 240, 262, 254]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[6]: text=类型 组 药品名称(规格), bbox=[17, 271, 163, 289]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[7]: text=药品 甲)(小儿)双黄连口服液(基), bbox=[17, 296, 204, 313]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[8]: text=药品 (盖克)小儿氨酚黄那敏颗粒, bbox=[17, 321, 204, 338]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[9]: text=药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基), bbox=[17, 353, 271, 370]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[10]: text=药品 蒲地蓝消炎口服液, bbox=[17, 386, 175, 403]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[11]: text=药品 复方氨酚甲麻口服液, bbox=[17, 410, 183, 427]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[12]: text=药品 (盖克)小儿氨酚黄那敏颗粒, bbox=[17, 435, 205, 452]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[13]: text=药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基), bbox=[17, 467, 280, 484]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[14]: text=药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基), bbox=[17, 499, 277, 516]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[15]: text=药品 右旋糖酐铁颗粒, bbox=[17, 524, 167, 541]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[16]: text=药品 盐酸氨卓斯丁滴眼液, bbox=[17, 549, 184, 566]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[17]: text=用法 频率 实际用量 总量 开立时间 开立医师, bbox=[643, 271, 977, 289]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[18]: text=口服 tid 10ml 1 2022-03-26 19:51:46 谭真真, bbox=[643, 296, 968, 313]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[19]: text=口服 tid 6g 2 2022-03-26 19:51:18 谭真真, bbox=[643, 321, 968, 338]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[20]: text=口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真, bbox=[643, 345, 968, 370]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[21]: text=口服 bid 10ml 1 2022-03-26 19:51:18 谭真真, bbox=[643, 386, 968, 403]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[22]: text=口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 410, 968, 427]
2026-08-10 11:05:45,674 INFO     29 [qwen-vl-text] coord item[23]: text=口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 435, 968, 452]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] coord item[24]: text=口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴, bbox=[643, 467, 968, 484]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] coord item[25]: text=压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅, bbox=[643, 499, 968, 516]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] coord item[26]: text=口服 tid 1袋 80 2021-09-28 15:12:34 党建华, bbox=[643, 524, 968, 541]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] coord item[27]: text=滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳, bbox=[643, 549, 968, 566]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] coord item[28]: text=共70条 20条/页 < 1 2 3 4 > 前往 4 页, bbox=[723, 583, 985, 599]
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] page=37 — 29/29 coords, api_time=15.7s
2026-08-10 11:05:45,675 INFO     29 [qwen-vl-text] new_positions (29):
[[37, 5.052, 359.534, 82.705, 92.225], [37, 777.1659999999999, 825.16, 83.3, 92.225], [37, 126.3, 364.586, 100.55499999999999, 109.47999999999999], [37, 15.998, 494.25399999999996, 116.61999999999999, 127.33], [37, 15.998, 112.828, 142.20499999999998, 151.725], [37, 178.504, 220.60399999999998, 142.79999999999998, 151.13], [37, 14.314, 137.246, 161.245, 171.95499999999998], [37, 14.314, 171.768, 176.12, 186.23499999999999], [37, 14.314, 171.768, 190.995, 201.10999999999999], [37, 14.314, 228.182, 210.035, 220.14999999999998], [37, 14.314, 147.35, 229.67, 239.785], [37, 14.314, 154.08599999999998, 243.95, 254.065], [37, 14.314, 172.60999999999999, 258.825, 268.94], [37, 14.314, 235.76, 277.865, 287.97999999999996], [37, 14.314, 233.23399999999998, 296.905, 307.02], [37, 14.314, 140.614, 311.78, 321.895], [37, 14.314, 154.928, 326.655, 336.77], [37, 541.406, 822.634, 161.245, 171.95499999999998], [37, 541.406, 815.0559999999999, 176.12, 186.23499999999999], [37, 541.406, 815.0559999999999, 190.995, 201.10999999999999], [37, 541.406, 815.0559999999999, 205.27499999999998, 220.14999999999998], [37, 541.406, 815.0559999999999, 229.67, 239.785], [37, 541.406, 815.0559999999999, 243.95, 254.065], [37, 541.406, 815.0559999999999, 258.825, 268.94], [37, 541.406, 815.0559999999999, 277.865, 287.97999999999996], [37, 541.406, 815.0559999999999, 296.905, 307.02], [37, 541.406, 815.0559999999999, 311.78, 321.895], [37, 541.406, 815.0559999999999, 326.655, 336.77], [37, 608.766, 829.37, 346.885, 356.405]]
2026-08-10 11:05:45,676 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=24.3s
2026-08-10 11:05:45,676 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:05:45,678 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:05:45,678 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:05:45,678 INFO     29 [qwen-vl-text] positions(12): [[51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0], [51, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:05:45,678 INFO     29 [qwen-vl-text] page grouping: [51], lines per page: [12]
2026-08-10 11:05:45,937 INFO     29 [qwen-vl-text] page=51, rect=842x1193, img=(2339x3313), dpi=200
2026-08-10 11:05:45,939 INFO     29 [qwen-vl-text] LLM extraction start, text_len=132
2026-08-10 11:05:45,940 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:45,940 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 2314, \"bbox_end\": 2325, \"encounter_dates\": [\"2021-02-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n4970401\n姓名：\n性别：□男 □女 年龄：60岁\n科别： 费别： 电话/住址：\n过敏史：无 开具日期：2021年2月16日\n临床诊断：支气管哮喘\nRp\n孟鲁司特钠片 10mg 2板\n用法：二天一次 1片\n审核： 调配： 医师：\n核对： 发药： 金额：",
    "role": "user"
  }
]
2026-08-10 11:05:46,620 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-02-08"}
```
2026-08-10 11:05:46,621 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2025-02-08
2026-08-10 11:05:46,635 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1455567, prompt_len=401
2026-08-10 11:05:48,196 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:48,196 INFO     29 [qwen-vl-text] LLM output (len=407):
{
  "encounter_date": "2021-02-16",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": null,
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "二天一次",
      "route": null,
      "duration_days": null,
      "quantity": "2板",
      "notes": "1片"
    }
  ]
}
2026-08-10 11:05:48,196 INFO     29 [qwen-vl-text] Updated encounter_dates=[2021-02-16]
2026-08-10 11:05:48,199 INFO     29 [qwen-vl-text] coord API call start, page=51, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1496199, prompt_len=781
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共12行）
["处方笺", "4970401", "姓名：", "性别：□男 □女 年龄：60岁", "科别： 费别： 电话/住址：", "过敏史：无 开具日期：2021年2月16日", "临床诊断：支气管哮喘", "Rp", "孟鲁司特钠片 10mg 2板", "用法：二天一次 1片", "审核： 调配： 医师：", "核对： 发药： 金额："]

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
2026-08-10 11:05:48,873 INFO     29 [qwen-vl-parser] text API response (len=370):
["门(急)诊处方", "就诊时间:2025-02-08", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号:", "患者类型:001 支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:05:48,874 INFO     29 [qwen-vl-parser] page=10 text: 35 lines (bbox 307-341)
2026-08-10 11:05:48,874 INFO     29 [qwen-vl-parser] page=10 text: 35 sections
2026-08-10 11:05:49,062 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1263830, prompt_len=764
2026-08-10 11:05:51,501 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:05:51,501 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 11:05:51,515 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1263830, prompt_len=401
2026-08-10 11:05:53,783 INFO     29 [qwen-vl-parser] text API response (len=328):
["门(急)诊处方", "就诊时间:2025-01-10", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:64岁", "卡号", "患者类型:G", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]
2026-08-10 11:05:53,783 INFO     29 [qwen-vl-parser] page=11 text: 32 lines (bbox 342-373)
2026-08-10 11:05:53,784 INFO     29 [qwen-vl-parser] page=11 text: 32 sections
2026-08-10 11:05:53,939 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1073703, prompt_len=764
2026-08-10 11:05:55,446 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-12-11"}
```
2026-08-10 11:05:55,448 INFO     29 [qwen-vl-text] coord API raw response (len=654):
[
	{"text": "处方笺", "bbox": [393, 68, 627, 108]},
	{"text": "4970401", "bbox": [695, 94, 895, 122]},
	{"text": "姓名：", "bbox": [68, 147, 195, 171]},
	{"text": "性别：□男 □女 年龄：60岁", "bbox": [457, 145, 944, 170]},
	{"text": "科别： 费别： 电话/住址：", "bbox": [68, 180, 692, 204]},
	{"text": "过敏史：无 开具日期：2021年2月16日", "bbox": [70, 211, 943, 245]},
	{"text": "临床诊断：支气管哮喘", "bbox": [70, 244, 480, 291]},
	{"text": "Rp", "bbox": [70, 295, 145, 348]},
	{"text": "孟鲁司特钠片 10mg 2板", "bbox": [180, 398, 874, 508]},
	{"text": "用法：二天一次 1片", "bbox": [375, 555, 887, 680]},
	{"text": "审核： 调配： 医师：", "bbox": [68, 880, 914, 934]},
	{"text": "核对： 发药： 金额：", "bbox": [68, 944, 725, 971]}
]
2026-08-10 11:05:55,448 INFO     29 [qwen-vl-text] coord API: raw_items=12, valid_items=12, elapsed=7.2s
2026-08-10 11:05:55,449 INFO     29 [qwen-vl-text] coord item[0]: text=处方笺, bbox=[393, 68, 627, 108]
2026-08-10 11:05:55,449 INFO     29 [qwen-vl-text] coord item[1]: text=4970401, bbox=[695, 94, 895, 122]
2026-08-10 11:05:55,449 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=2024-12-11
2026-08-10 11:05:55,450 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[68, 147, 195, 171]
2026-08-10 11:05:55,450 INFO     29 [qwen-vl-text] coord item[3]: text=性别：□男 □女 年龄：60岁, bbox=[457, 145, 944, 170]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[4]: text=科别： 费别： 电话/住址：, bbox=[68, 180, 692, 204]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[5]: text=过敏史：无 开具日期：2021年2月16日, bbox=[70, 211, 943, 245]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[6]: text=临床诊断：支气管哮喘, bbox=[70, 244, 480, 291]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[7]: text=Rp, bbox=[70, 295, 145, 348]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[8]: text=孟鲁司特钠片 10mg 2板, bbox=[180, 398, 874, 508]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[9]: text=用法：二天一次 1片, bbox=[375, 555, 887, 680]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[10]: text=审核： 调配： 医师：, bbox=[68, 880, 914, 934]
2026-08-10 11:05:55,451 INFO     29 [qwen-vl-text] coord item[11]: text=核对： 发药： 金额：, bbox=[68, 944, 725, 971]
2026-08-10 11:05:55,452 INFO     29 [qwen-vl-text] page=51 — 12/12 coords, api_time=7.2s
2026-08-10 11:05:55,452 INFO     29 [qwen-vl-text] new_positions (12):
[[51, 330.906, 527.934, 81.0991474609375, 128.8045283203125], [51, 585.1899999999999, 753.5899999999999, 112.10764501953125, 145.50141162109375], [51, 57.256, 164.19, 175.31727465820313, 203.94050317382812], [51, 384.794, 794.848, 172.93200561523437, 202.74786865234375], [51, 57.256, 582.664, 214.6742138671875, 243.2974423828125], [51, 58.94, 794.006, 251.64588403320312, 292.19545776367187], [51, 58.94, 404.15999999999997, 291.0028232421875, 347.0566457519531], [51, 58.94, 122.08999999999999, 351.82718383789063, 415.0368134765625], [51, 151.56, 735.908, 474.66853955078125, 605.8583369140625], [51, 315.75, 746.8539999999999, 661.9121594238281, 810.991474609375], [51, 57.256, 769.588, 1049.51837890625, 1113.9206430664062], [51, 57.256, 610.4499999999999, 1125.8469882812499, 1158.048120361328]]
2026-08-10 11:05:55,452 INFO     29 [qwen-vl-text] ═══ DONE ═══ 12 positions, pages=1, time=9.8s
2026-08-10 11:05:55,478 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1073703, prompt_len=401
2026-08-10 11:05:55,488 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:05:55,488 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Extractor:Prescription | outputs={"chunks": "5 items, types={'PrescriptionRecord': 5}", "html": "", "json": "2326 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Progress": "7 items, types={'ProgressNote': 7}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "5 items, types={'PrescriptionRecord': 5}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Progress\": 7, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 5, \"chunks_LabExam\": 13}"}
2026-08-10 11:05:55,488 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:05:55,496 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:05:55,498 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:05:55,498 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 11:05:55,498 INFO     29 [qwen-vl-text] positions(56): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:05:55,498 INFO     29 [qwen-vl-text] page grouping: [14, 15], lines per page: [38, 18]
2026-08-10 11:05:55,736 INFO     29 [qwen-vl-text] page=14, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:05:55,902 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:05:55,904 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1307
2026-08-10 11:05:55,904 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:05:55,905 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 1008, \"bbox_end\": 1063, \"encounter_dates\": [\"2020-07-12\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "出院记录\n姓名\n科室：产科二区\n床号.\n住院号.\n2020年07月12日\n出院记录\n患者.\n36岁\n住院号：\n入院日期：2020-07-08 08:36:09\n出院日期：2020年07月12日\n住院天数：4天\n入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺\n听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估\n计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外\n测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径\n9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。\n入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。\n诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在\n腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢\n痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，\n切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘\n胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝\n合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫\n切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗\n感染、加强宫缩支持及对症治疗。\n出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：\n出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显\n异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩\n好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳\n泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划\n性剖宫产临床路径。\n出院医嘱：1.注意休息，合理营养；\n2.禁性生活、盆浴及重体力劳动2个月；\n3.坚持纯母乳喂养大于4-6月；\n第 页\n总第 页\n医院\n出院记录\n姓名：\n科室：产科二区\n床号：\n住院号：2\n4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理\n状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经\n量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）\n5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：\n6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂\n1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或\n出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；\n7.咨询电话产科：\n，新生儿科：0398-3118382。母乳咨询电话：\n0398-3118618.\n主治医师：\n孙州",
    "role": "user"
  }
]
2026-08-10 11:05:56,386 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:05:56.385+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:05:57,690 INFO     29 [qwen-vl-parser] text API response (len=368):
["门(急)诊处方", "就诊时间:2024-12-11", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:05:57,690 INFO     29 [qwen-vl-parser] page=12 text: 35 lines (bbox 374-408)
2026-08-10 11:05:57,690 INFO     29 [qwen-vl-parser] page=12 text: 35 sections
2026-08-10 11:05:57,849 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1135113, prompt_len=764
2026-08-10 11:05:59,230 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2024-11-18"}
```
2026-08-10 11:05:59,230 INFO     29 [qwen-vl-parser] page=13 classify=text report_date=2024-11-18
2026-08-10 11:05:59,238 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1135113, prompt_len=401
2026-08-10 11:06:02,018 INFO     29 [qwen-vl-parser] text API response (len=371):
["门(急)诊处方", "就诊时间:2024-11-18", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:63岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘,非危重", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "CS 扫描全能王", "3亿人都在用的扫描App"]
2026-08-10 11:06:02,018 INFO     29 [qwen-vl-parser] page=13 text: 35 lines (bbox 409-443)
2026-08-10 11:06:02,018 INFO     29 [qwen-vl-parser] page=13 text: 35 sections
2026-08-10 11:06:02,155 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1009899, prompt_len=764
2026-08-10 11:06:04,205 INFO     29 [qwen-vl-parser] classify API response (len=50):
```json
{"type": "table", "report_date": null}
```
2026-08-10 11:06:04,205 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=None
2026-08-10 11:06:04,216 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1009899, prompt_len=756
2026-08-10 11:06:09,027 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:09,027 INFO     29 [qwen-vl-text] LLM output (len=2431):
{
  "encounter_date": "2020-07-12",
  "admission_date": "2020-07-08",
  "discharge_date": "2020-07-12",
  "hospital_days": 4,
  "department": "产科二区",
  "bed_number": null,
  "admission_condition": "以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "admission_diagnoses": [
    {
      "name": "妊娠合并子宫瘢痕",
      "diagnosis_type": "西医"
    },
    {
      "name": "孕产：宫内孕39周头位待产",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗感染、加强宫缩支持及对症治疗。",
  "auxiliary_exams": null,
  "imaging_findings": "B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "discharge_diagnoses": [
    {
      "name": "妊娠合并子宫瘢痕",
      "diagnosis_type": "西医"
    },
    {
      "name": "孕产：宫内孕39+周头位剖宫产",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划性剖宫产临床路径。",
  "outcome": "治愈",
  "discharge_orders": "1.注意休息，合理营养；2.禁性生活、盆浴及重体力劳动2个月；3.坚持纯母乳喂养大于4-6月；4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；7.咨询电话产科：，新生儿科：0398-3118382。母乳咨询电话：0398-3118618.",
  "do_medications": [
    "维生素AD滴剂 1粒/次 一次/日 至2岁"
  ],
  "do_follow_up": "产后42天门诊复查",
  "do_precautions": [
    "注意休息，合理营养",
    "禁性生活、盆浴及重体力劳动2个月",
    "坚持纯母乳喂养大于4-6月",
    "如出院后出现任何异常情况请立即就诊，注意产妇心理状态，必要时心理咨询门诊就诊",
    "若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经量、腹痛、发热等，及时就诊",
    "严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠",
    "出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊"
  ],
  "next_treatment_date": null,
  "attending_physician": "孙州",
  "pe_ecog_score": null,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 11:06:09,027 INFO     29 [qwen-vl-text] Updated encounter_dates=[2020-07-12]
2026-08-10 11:06:09,029 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1337725, prompt_len=1676
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["出院记录", "姓名", "科室：产科二区", "床号.", "住院号.", "2020年07月12日", "出院记录", "患者.", "36岁", "住院号：", "入院日期：2020-07-08 08:36:09", "出院日期：2020年07月12日", "住院天数：4天", "入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺", "听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估", "计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外", "测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。", "入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。", "诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在", "腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢", "痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，", "切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘", "胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝", "合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫", "切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗", "感染、加强宫缩支持及对症治疗。", "出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：", "出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显", "异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩", "好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳", "泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划", "性剖宫产临床路径。", "出院医嘱：1.注意休息，合理营养；", "2.禁性生活、盆浴及重体力劳动2个月；", "3.坚持纯母乳喂养大于4-6月；", "第 页", "总第 页"]

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
2026-08-10 11:06:14,335 INFO     29 [qwen-vl-parser] table API response (len=1805):
\begin{tabular}{ccccccl}
\hline
序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\
\hline
1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\
2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\
3 & 中性粒细胞百分数(NEUN) & 62.30 & & \% & 40 -- 75 & \\
4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\
5 & 淋巴细胞百分数(LYN) & 28.60 & & \% & 20 -- 50 & \\
6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\
7 & 单核细胞百分数(MON%) & 5.10 & & \% & 3 -- 10 & \\
8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\
9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \% & 0.4 -- 8 & \\
10 & 嗜碱性粒细胞总数(BASO) & 0.03 & & 10^9/L & 0 -- 0.06 & \\
11 & 嗜碱性粒细胞百分比(BASO%) & 0.30 & & \% & 0 -- 1 & \\
12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\
13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\
14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \% & 40 -- 50 & \\
15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\
16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\
17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\
18 & 红细胞分布宽度(RDW) & 12.40 & & \% & 11.6 -- 14.8 & \\
19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\
20 & 血小板(PLT) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\
21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\
22 & 平均血小板比容(Pct) & 0.21 & & \% & 0.10 -- 0.29 & \\
23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\
24 & 大血小板(P-LCR) & 30.90 & & \% & & \\
25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\
26 & 网织红细胞百分数(RETR) & 1.64 & & \% & & \\
27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\downarrow$ & \% & 89.9 -- 98.4 & \\
28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\uparrow$ & \% & 1.6 -- 9.5 & \\
29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\uparrow$ & \% & 0 -- 1.7 & \\
30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\uparrow$ & \% & 1.6 -- 10.5 & \\
31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\
32 & 有核红细胞百分比(NRBC%) & 0 & & \% & & \\
\hline
\end{tabular}
2026-08-10 11:06:14,336 INFO     29 [qwen-vl-parser] page=14 table: 38 LaTeX lines (bbox 444-481)
2026-08-10 11:06:14,336 INFO     29 [qwen-vl-parser] page=14 table: 38 sections
2026-08-10 11:06:14,462 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716459, prompt_len=764
2026-08-10 11:06:15,900 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:06:15,900 INFO     29 [qwen-vl-parser] page=15 classify=text report_date=None
2026-08-10 11:06:15,907 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=716459, prompt_len=401
2026-08-10 11:06:18,481 INFO     29 [qwen-vl-parser] text API response (len=361):
["处方笺", "普通", "诊疗", "患者姓", "男", "年龄：65岁", "费别：", "科室：", "2026-01-06 11:28:26", "处方号", "地址：", "联系电", "身份号", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "R", "P:", "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "1瓶", "剂量：每次2揿 （1/60 瓶）", "用法：吸入用药", "bid 01-06", "孟鲁司特钠片(省采)◆", "10mg*5/盒", "30片", "剂量：每次10mg （1 片）", "用法：口服", "qd 01-06", "处方金额：298.47元", "取药药房：门诊西药房（荔湾）", ""]
2026-08-10 11:06:18,482 INFO     29 [qwen-vl-parser] page=15 text: 29 lines (bbox 482-510)
2026-08-10 11:06:18,482 INFO     29 [qwen-vl-parser] page=15 text: 29 sections
2026-08-10 11:06:18,670 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049439, prompt_len=764
2026-08-10 11:06:20,077 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 11:06:20,077 INFO     29 [qwen-vl-parser] page=16 classify=text report_date=None
2026-08-10 11:06:20,087 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1049439, prompt_len=401
2026-08-10 11:06:23,144 INFO     29 [qwen-vl-parser] text API response (len=437):
["处方笺", "普通", "诊断", "患者", "年龄：65岁", "费别", "科室", "6-01-06 11:31:02", "处方", "地址", "联系", "身份", "诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎", "Rp:", "左氧氟沙星片(省采)●⑥", "0.5g*28片/盒", "3片", "剂量：每次0.5g", "(1 片)", "用法：口服", "qd", "01-06", "醋酸泼尼松片●②⑥", "5mg*100/瓶", "6片", "剂量：每次10mg", "(2 片)", "用法：口服", "qm", "01-06", "盐酸氨溴索分散片(省采)●⑥", "30mg*50/盒", "15片", "剂量：每次30mg", "(1 片)", "用法：餐后口服", "tid", "01-06", "处方金额：3.47元", "取药药房：门诊西药房（荔湾）", "医师手签：", ""]
2026-08-10 11:06:23,144 INFO     29 [qwen-vl-parser] page=16 text: 41 lines (bbox 511-551)
2026-08-10 11:06:23,145 INFO     29 [qwen-vl-parser] page=16 text: 41 sections
2026-08-10 11:06:23,524 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2373698, prompt_len=764
2026-08-10 11:06:25,131 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-02-04"}
```
2026-08-10 11:06:25,132 INFO     29 [qwen-vl-parser] page=17 classify=text report_date=2026-02-04
2026-08-10 11:06:25,144 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2373698, prompt_len=401
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord API raw response (len=2623):
[
	{"text": "出院记录", "bbox": [438, 89, 571, 108]},
	{"text": "姓名", "bbox": [130, 117, 167, 133]},
	{"text": "科室：产科二区", "bbox": [310, 117, 440, 132]},
	{"text": "床号.", "bbox": [506, 117, 548, 132]},
	{"text": "住院号.", "bbox": [676, 117, 784, 133]},
	{"text": "2020年07月12日", "bbox": [122, 141, 250, 156]},
	{"text": "出院记录", "bbox": [454, 141, 527, 156]},
	{"text": "患者.", "bbox": [159, 167, 203, 182]},
	{"text": "36岁", "bbox": [287, 167, 324, 182]},
	{"text": "住院号：", "bbox": [480, 167, 561, 182]},
	{"text": "入院日期：2020-07-08 08:36:09", "bbox": [159, 192, 426, 207]},
	{"text": "出院日期：2020年07月12日", "bbox": [509, 192, 727, 207]},
	{"text": "住院天数：4天", "bbox": [159, 219, 279, 234]},
	{"text": "入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺", "bbox": [122, 245, 876, 261]},
	{"text": "听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估", "bbox": [122, 271, 867, 287]},
	{"text": "计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外", "bbox": [122, 298, 867, 314]},
	{"text": "测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径", "bbox": [122, 325, 858, 340]},
	{"text": "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。", "bbox": [122, 351, 579, 367]},
	{"text": "入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。", "bbox": [159, 378, 708, 394]},
	{"text": "诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在", "bbox": [122, 404, 870, 420]},
	{"text": "腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢", "bbox": [122, 430, 876, 446]},
	{"text": "痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，", "bbox": [122, 457, 863, 473]},
	{"text": "切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘", "bbox": [122, 483, 866, 499]},
	{"text": "胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝", "bbox": [122, 509, 876, 525]},
	{"text": "合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫", "bbox": [122, 535, 874, 551]},
	{"text": "切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗", "bbox": [122, 561, 876, 577]},
	{"text": "感染、加强宫缩支持及对症治疗。", "bbox": [122, 587, 388, 603]},
	{"text": "出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：", "bbox": [159, 613, 726, 629]},
	{"text": "出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显", "bbox": [159, 639, 874, 655]},
	{"text": "异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩", "bbox": [122, 666, 874, 682]},
	{"text": "好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳", "bbox": [122, 692, 874, 708]},
	{"text": "泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划", "bbox": [122, 718, 874, 734]},
	{"text": "性剖宫产临床路径。", "bbox": [122, 744, 275, 760]},
	{"text": "出院医嘱：1.注意休息，合理营养；", "bbox": [159, 770, 440, 786]},
	{"text": "2.禁性生活、盆浴及重体力劳动2个月；", "bbox": [248, 796, 558, 812]},
	{"text": "3.坚持纯母乳喂养大于4-6月；", "bbox": [248, 823, 485, 839]},
	{"text": "第 页", "bbox": [503, 880, 549, 894]},
	{"text": "总第 页", "bbox": [818, 880, 882, 894]}
]
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=17.6s
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord item[0]: text=出院记录, bbox=[438, 89, 571, 108]
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[130, 117, 167, 133]
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord item[2]: text=科室：产科二区, bbox=[310, 117, 440, 132]
2026-08-10 11:06:26,618 INFO     29 [qwen-vl-text] coord item[3]: text=床号., bbox=[506, 117, 548, 132]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[4]: text=住院号., bbox=[676, 117, 784, 133]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[5]: text=2020年07月12日, bbox=[122, 141, 250, 156]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[6]: text=出院记录, bbox=[454, 141, 527, 156]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[7]: text=患者., bbox=[159, 167, 203, 182]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[8]: text=36岁, bbox=[287, 167, 324, 182]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[9]: text=住院号：, bbox=[480, 167, 561, 182]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[10]: text=入院日期：2020-07-08 08:36:09, bbox=[159, 192, 426, 207]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[11]: text=出院日期：2020年07月12日, bbox=[509, 192, 727, 207]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[12]: text=住院天数：4天, bbox=[159, 219, 279, 234]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[13]: text=入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺, bbox=[122, 245, 876, 261]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[14]: text=听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估, bbox=[122, 271, 867, 287]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[15]: text=计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外, bbox=[122, 298, 867, 314]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[16]: text=测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径, bbox=[122, 325, 858, 340]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[17]: text=9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。, bbox=[122, 351, 579, 367]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[18]: text=入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。, bbox=[159, 378, 708, 394]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[19]: text=诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在, bbox=[122, 404, 870, 420]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[20]: text=腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢, bbox=[122, 430, 876, 446]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[21]: text=痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，, bbox=[122, 457, 863, 473]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[22]: text=切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘, bbox=[122, 483, 866, 499]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[23]: text=胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝, bbox=[122, 509, 876, 525]
2026-08-10 11:06:26,619 INFO     29 [qwen-vl-text] coord item[24]: text=合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫, bbox=[122, 535, 874, 551]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[25]: text=切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗, bbox=[122, 561, 876, 577]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[26]: text=感染、加强宫缩支持及对症治疗。, bbox=[122, 587, 388, 603]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[27]: text=出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：, bbox=[159, 613, 726, 629]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[28]: text=出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显, bbox=[159, 639, 874, 655]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[29]: text=异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩, bbox=[122, 666, 874, 682]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[30]: text=好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳, bbox=[122, 692, 874, 708]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[31]: text=泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划, bbox=[122, 718, 874, 734]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[32]: text=性剖宫产临床路径。, bbox=[122, 744, 275, 760]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[33]: text=出院医嘱：1.注意休息，合理营养；, bbox=[159, 770, 440, 786]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[34]: text=2.禁性生活、盆浴及重体力劳动2个月；, bbox=[248, 796, 558, 812]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[35]: text=3.坚持纯母乳喂养大于4-6月；, bbox=[248, 823, 485, 839]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[36]: text=第 页, bbox=[503, 880, 549, 894]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] coord item[37]: text=总第 页, bbox=[818, 880, 882, 894]
2026-08-10 11:06:26,620 INFO     29 [qwen-vl-text] page=14 — 38/38 coords, api_time=17.6s
2026-08-10 11:06:26,622 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=582406, prompt_len=1024
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["医院", "出院记录", "姓名：", "科室：产科二区", "床号：", "住院号：2", "4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理", "状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经", "量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）", "5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：", "6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂", "1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或", "出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；", "7.咨询电话产科：", "，新生儿科：0398-3118382。母乳咨询电话：", "0398-3118618.", "主治医师：", "孙州"]

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
2026-08-10 11:06:32,036 INFO     29 [qwen-vl-parser] text API response (len=940):
["病历编号：", "姓名：", "性别：男", "年龄：65岁", "就诊科室：内科门诊（基础）", "医生：", "就诊时间：2026-02-04 11:23:30", "主诉：支气管哮喘治疗后复诊", "现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "既往史：鼻炎病史，有糖尿病史", "过敏史：未发现", "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "专科情况：", "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "备注：建议在停药附近社区医疗机构随访。"]
2026-08-10 11:06:32,036 INFO     29 [qwen-vl-parser] page=17 text: 30 lines (bbox 552-581)
2026-08-10 11:06:32,036 INFO     29 [qwen-vl-parser] page=17 text: 30 sections
2026-08-10 11:06:32,036 INFO     29 [qwen-vl-parser] parse_pdf done: 582 sections from 17 pages.
2026-08-10 11:06:32,049 INFO     29 Close text detector.
2026-08-10 11:06:32,453 INFO     29 Close text recognizer.
2026-08-10 11:06:33,942 INFO     29 Close recognizer.
2026-08-10 11:06:34,366 INFO     29 Close recognizer.
2026-08-10 11:06:34,866 INFO     29 [qwen-vl-text] coord API raw response (len=1150):
[
	{"text": "医院", "bbox": [557, 63, 615, 84]},
	{"text": "出院记录", "bbox": [435, 101, 575, 120]},
	{"text": "姓名：", "bbox": [109, 129, 157, 145]},
	{"text": "科室：产科二区", "bbox": [300, 129, 438, 145]},
	{"text": "床号：", "bbox": [507, 129, 553, 145]},
	{"text": "住院号：2", "bbox": [686, 129, 771, 145]},
	{"text": "4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理", "bbox": [237, 153, 899, 170]},
	{"text": "状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经", "bbox": [100, 180, 870, 197]},
	{"text": "量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）", "bbox": [100, 207, 784, 224]},
	{"text": "5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：", "bbox": [237, 237, 800, 254]},
	{"text": "6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂", "bbox": [237, 264, 902, 281]},
	{"text": "1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或", "bbox": [100, 291, 902, 308]},
	{"text": "出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；", "bbox": [102, 320, 773, 337]},
	{"text": "7.咨询电话产科：", "bbox": [227, 347, 371, 364]},
	{"text": "，新生儿科：0398-3118382。母乳咨询电话：", "bbox": [444, 349, 882, 365]},
	{"text": "0398-3118618.", "bbox": [100, 375, 226, 390]},
	{"text": "主治医师：", "bbox": [647, 430, 733, 446]},
	{"text": "孙州", "bbox": [753, 409, 837, 437]}
]
2026-08-10 11:06:34,866 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=8.2s
2026-08-10 11:06:34,866 INFO     29 [qwen-vl-text] coord item[0]: text=医院, bbox=[557, 63, 615, 84]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[1]: text=出院记录, bbox=[435, 101, 575, 120]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[109, 129, 157, 145]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[3]: text=科室：产科二区, bbox=[300, 129, 438, 145]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[4]: text=床号：, bbox=[507, 129, 553, 145]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[5]: text=住院号：2, bbox=[686, 129, 771, 145]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[6]: text=4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理, bbox=[237, 153, 899, 170]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[7]: text=状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经, bbox=[100, 180, 870, 197]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[8]: text=量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）, bbox=[100, 207, 784, 224]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[9]: text=5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：, bbox=[237, 237, 800, 254]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[10]: text=6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂, bbox=[237, 264, 902, 281]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[11]: text=1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或, bbox=[100, 291, 902, 308]
2026-08-10 11:06:34,867 INFO     29 [qwen-vl-text] coord item[12]: text=出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；, bbox=[102, 320, 773, 337]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] coord item[13]: text=7.咨询电话产科：, bbox=[227, 347, 371, 364]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] coord item[14]: text=，新生儿科：0398-3118382。母乳咨询电话：, bbox=[444, 349, 882, 365]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] coord item[15]: text=0398-3118618., bbox=[100, 375, 226, 390]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] coord item[16]: text=主治医师：, bbox=[647, 430, 733, 446]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] coord item[17]: text=孙州, bbox=[753, 409, 837, 437]
2026-08-10 11:06:34,868 INFO     29 [qwen-vl-text] page=15 — 18/18 coords, api_time=8.2s
2026-08-10 11:06:34,869 INFO     29 [qwen-vl-text] new_positions (56):
[[14, 260.61, 339.745, 74.938, 90.93599999999999], [14, 77.35, 99.365, 98.514, 111.98599999999999], [14, 184.45, 261.8, 98.514, 111.14399999999999], [14, 301.07, 326.06, 98.514, 111.14399999999999], [14, 402.21999999999997, 466.47999999999996, 98.514, 111.98599999999999], [14, 72.59, 148.75, 118.722, 131.352], [14, 270.13, 313.565, 118.722, 131.352], [14, 94.60499999999999, 120.785, 140.614, 153.244], [14, 170.765, 192.78, 140.614, 153.244], [14, 285.59999999999997, 333.79499999999996, 140.614, 153.244], [14, 94.60499999999999, 253.47, 161.664, 174.29399999999998], [14, 302.85499999999996, 432.565, 161.664, 174.29399999999998], [14, 94.60499999999999, 166.005, 184.398, 197.028], [14, 72.59, 521.22, 206.29, 219.762], [14, 72.59, 515.865, 228.182, 241.654], [14, 72.59, 515.865, 250.916, 264.388], [14, 72.59, 510.51, 273.65, 286.28], [14, 72.59, 344.505, 295.542, 309.014], [14, 94.60499999999999, 421.26, 318.276, 331.748], [14, 72.59, 517.65, 340.168, 353.64], [14, 72.59, 521.22, 362.06, 375.532], [14, 72.59, 513.485, 384.794, 398.26599999999996], [14, 72.59, 515.27, 406.686, 420.15799999999996], [14, 72.59, 521.22, 428.578, 442.05], [14, 72.59, 520.03, 450.46999999999997, 463.942], [14, 72.59, 521.22, 472.36199999999997, 485.834], [14, 72.59, 230.85999999999999, 494.25399999999996, 507.726], [14, 94.60499999999999, 431.96999999999997, 516.146, 529.6179999999999], [14, 94.60499999999999, 520.03, 538.038, 551.51], [14, 72.59, 520.03, 560.7719999999999, 574.244], [14, 72.59, 520.03, 582.664, 596.136], [14, 72.59, 520.03, 604.5559999999999, 618.028], [14, 72.59, 163.625, 626.448, 639.92], [14, 94.60499999999999, 261.8, 648.34, 661.812], [14, 147.56, 332.01, 670.232, 683.704], [14, 147.56, 288.575, 692.966, 706.438], [14, 299.28499999999997, 326.655, 740.9599999999999, 752.7479999999999], [14, 486.71, 524.79, 740.9599999999999, 752.7479999999999], [15, 331.41499999999996, 365.925, 53.046, 70.728], [15, 258.825, 342.125, 85.042, 101.03999999999999], [15, 64.855, 93.41499999999999, 108.618, 122.08999999999999], [15, 178.5, 260.61, 108.618, 122.08999999999999], [15, 301.66499999999996, 329.03499999999997, 108.618, 122.08999999999999], [15, 408.16999999999996, 458.745, 108.618, 122.08999999999999], [15, 141.015, 534.905, 128.826, 143.14], [15, 59.5, 517.65, 151.56, 165.874], [15, 59.5, 466.47999999999996, 174.29399999999998, 188.608], [15, 141.015, 476.0, 199.554, 213.868], [15, 141.015, 536.6899999999999, 222.28799999999998, 236.602], [15, 59.5, 536.6899999999999, 245.022, 259.336], [15, 60.69, 459.935, 269.44, 283.75399999999996], [15, 135.065, 220.74499999999998, 292.174, 306.488], [15, 264.18, 524.79, 293.858, 307.33], [15, 59.5, 134.47, 315.75, 328.38], [15, 384.965, 436.135, 362.06, 375.532], [15, 448.03499999999997, 498.015, 344.378, 367.954]]
2026-08-10 11:06:34,869 INFO     29 [qwen-vl-text] ═══ DONE ═══ 56 positions, pages=2, time=39.4s
2026-08-10 11:06:34,883 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:06:34,884 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "2326 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Progress": "7 items, types={'ProgressNote': 7}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "5 items, types={'PrescriptionRecord': 5}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Progress\": 7, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 5, \"chunks_LabExam\": 13}"}
2026-08-10 11:06:34,884 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:06:34,884 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:06:34.884+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:06:34,897 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:06:34,899 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:06:34,899 INFO     29 [qwen-vl-text] ═══ START ═══ type=AdmissionRecord, doc_id=None
2026-08-10 11:06:34,899 INFO     29 [qwen-vl-text] positions(156): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:06:34,899 INFO     29 [qwen-vl-text] page grouping: [5, 6, 7, 8], lines per page: [49, 40, 44, 23]
2026-08-10 11:06:35,134 INFO     29 [qwen-vl-text] page=5, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:06:35,362 INFO     29 [qwen-vl-text] page=6, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:06:35,594 INFO     29 [qwen-vl-text] page=7, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:06:35,774 INFO     29 [qwen-vl-text] page=8, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:06:35,776 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2765
2026-08-10 11:06:35,776 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:35,776 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"AdmissionRecord\", \"bbox_start\": 711, \"bbox_end\": 866, \"encounter_dates\": [\"2020-07-08\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "院\n入院记录\n姓名：\n科室：产科二区\n床号：\n科室：产科二区\n第(1)次入院记录\n过敏史：无\n姓名：\n性别：女\n年龄：36岁\n身份证号\n职业：\n婚姻：已婚\n民族：汉族\n出生地：\n现住址：\n入院日期：2020-07-08 08:36:09\n邮编\n病史采集时间：2020-07-08 08:36:09\n联系人：\n与病人关系：夫妻\n病史叙述者：本人\n联系人地址：同上地址\n电话.\n可靠程度：可靠\n主诉：停经39周，要求住院待产。\n现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产\n期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合\n孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接\n触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA\n结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛\n查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰\n痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子\n宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。\n既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有\n“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血\n史，有献血史，否认食物及药物过敏史。预防接种随社会进行。\n个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住\n史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。\n婚育史：31岁结婚，爱人\n现年37岁，职员，工作于三门峡市党校，身体健康，无吸\n烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男\n婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。\n月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳\n历），量中等，色暗红，偶有血块，无痛经。\n页\n书写者签名：\n总第 页\n院\n入院记录\n姓名:\n科室:产科二区\n床号:\n生.\n家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。\n体格检查\n体温:36.5℃\n脉搏:78次/分\n呼吸:18次/分\n血压:98/64mmHg\n身高160cm\n体重:60Kg\n一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言\n语状态流利;检查时能合作等。\n皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创\n伤、溃疡、结节。\n淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。\n头部:\n头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。\n眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,\n间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。\n耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。\n鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。\n口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异\n常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿\n大、分泌物;咽部无充血、分泌物。\n颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居\n中,甲状腺无肿大。\n胸部\n胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉\n曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。\n肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。\n触诊:语音震颤两侧相等,无摩擦感。\n叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,\n听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、\n第页\n书写者签名:\n总第页\n院\n入院记录\n姓名：\n科室：产科二区\n床号\n病号：\n干啰音、湿啰音。\n心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前\n区无异常搏动、局限性膨隆。\n触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、\n震颤、摩擦感。\n叩诊：左右心界线以每肋间距胸骨中线的cm数记载。\n右cm\n肋间\n左cm\n2\nⅡ\n2.5\n2\nⅢ\n4\n3\nⅣ\n5.5\nV\n8\n左锁骨中线至前正中线的距离9cm。\n听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分\n裂，P2<A2。\n血管：桡动脉搏动正常，血管壁硬度正常。\n周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。\n腹部：\n视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆\n起，下腹可见一长约15cm横行手术疤痕。\n触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未\n触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。\n叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度\n鼓音，移动性浊音阴性。\n听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血\n管杂音。\n外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱\n肛、湿疣等。\n脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。\n四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎\n院\n入院记录\n姓名.\n科室:产科二区\n床号\n住院号.\n缩;关节无红肿、畸形、运动障碍,双下肢水肿。\n神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、\n腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。\n专科情况\n宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无\n宫缩,未见红,未破水,骨盆外测量及内诊:未做。\n辅助检查\nB超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指\n数8.5cm),胎盘成熟度II°.\n初步诊断:\n1.妊娠合并子宫瘢痕;\n3.孕2产,宫内孕39周头位待产。\n主治医师:\n孙小丹\n副主任医师:\n彭琼玉\n2020.07.08",
    "role": "user"
  }
]
2026-08-10 11:06:36,400 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 11:06:36,400 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Parser:MedLink | outputs={"html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "json"}
2026-08-10 11:06:36,400 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 11:06:36,440 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:36,441 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 门(急)诊病历信息\n[BBOX-1] 就诊卡\n[BBOX-2] 流水\n[BBOX-3] 病历编号:\n[BBOX-4] 姓\n[BBOX-5] 别:男\n[BBOX-6] 年\n[BBOX-7] 龄:64岁\n[BBOX-8] 就诊科室:内科门诊(荔湾)\n[BBOX-9] 医\n[BBOX-10] 诊时间:2025-10-21 16:24:23\n[BBOX-11] 主\n[BBOX-12] 诉:取药\n[BBOX-13] 现病史:\n[BBOX-14] 既往史:\n[BBOX-15] 过敏史:\n[BBOX-16] 个人史:\n[BBOX-17] 体格检查:\n[BBOX-18] 专科情况:\n[BBOX-19] 辅助检查:\n[BBOX-20] 治疗项目:\n[BBOX-21] 门诊诊断:\n[BBOX-22] 支气管哮喘\n[BBOX-23] 单病种:\n[BBOX-24] 发病时间:\n[BBOX-25] 处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n[BBOX-26] 1孟鲁司特钠片(省采)◆\n[BBOX-27] 1瓶10.0mg,口服,每晚1次\n[BBOX-28] 30天\n[BBOX-29] 2倍氯米松福莫特罗吸入气雾剂◆①\n[BBOX-30] 1瓶2.0揿,吸入用药,一天2次\n[BBOX-31] 30天\n[BBOX-32] 备注:建议在住地附近社区医疗机构随诊。\n[BBOX-33] 病情评估:\n[BBOX-34] 病情分级:\n[BBOX-35] 是否抢救病例:否\n[BBOX-36] 是否抢救成功:\n[BBOX-37] 是否为绿色通道患者:否\n[BBOX-38] 病人去向:\n[BBOX-39] 病人来源:自行来院\n[BBOX-40] 是否曾就诊于其他医疗机构:\n[BBOX-41] 门(急)诊病历信息\n[BBOX-42] 就诊卡号:\n[BBOX-43] 流水号:\n[BBOX-44] 病历编号:\n[BBOX-45] 性别:男\n[BBOX-46] 年\n[BBOX-47] 龄:65岁\n[BBOX-48] 就诊科室:内科门诊(荔湾)\n[BBOX-49] 医生:\n[BBOX-50] 就诊时间:2025-11-19 11:33:52\n[BBOX-51] 主诉:取药\n[BBOX-52] 现病史:\n[BBOX-53] 既往史:\n[BBOX-54] 过敏史:\n[BBOX-55] 个人史:\n[BBOX-56] 体格检查:\n[BBOX-57] 专科情况:\n[BBOX-58] 辅助检查:\n[BBOX-59] 治疗项目:\n[BBOX-60] 门诊诊断:\n[BBOX-61] 1、支气管哮喘\n[BBOX-62] 处置:\n[BBOX-63] 1孟鲁司特钠片(省采)◆\n[BBOX-64] 1瓶10.0mg,口服,每晚1次\n[BBOX-65] 30天\n[BBOX-66] 2倍氯米松福莫特罗吸入气雾剂◆①\n[BBOX-67] 1瓶2.0揿,吸入用药,一天2次\n[BBOX-68] 30天\n[BBOX-69] 备注:\n[BBOX-70] 门(急)诊病历信息\n[BBOX-71] 就诊卡号\n[BBOX-72] 流水\n[BBOX-73] 姓名\n[BBOX-74] 性别:男\n[BBOX-75] 年\n[BBOX-76] 龄:65岁\n[BBOX-77] 就诊科室:内科门诊(荔湾)\n[BBOX-78] 病历编号:\n[BBOX-79] 就诊时间:2025-12-12 09:26:46\n[BBOX-80] 主诉:BAIYUN V8\n[BBOX-81] 现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。\n[BBOX-82] 完成下流操作:\n[BBOX-83] 1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;\n[BBOX-84] 2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。\n[BBOX-85] 3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。\n[BBOX-86] 4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。\n[BBOX-87] 5、休息至少10分钟后,行12导联ECG检查。\n[BBOX-88] 6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。\n[BBOX-89] 7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。\n[BBOX-90] CS 扫描全能王\n[BBOX-91] 3亿人都在用的扫描App\n[BBOX-92] 门诊病历\n[BBOX-93] 25/10/21 16时 门诊病历\n[BBOX-94] 25/11/19 11时 门诊病历（GCP专用）\n[BBOX-95] 25/12/12 09时 门诊病历（GCP专用）\n[BBOX-96] 1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验\n[BBOX-97] 药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。\n[BBOX-98] 2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无\n[BBOX-99] 关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。\n[BBOX-100] 病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。\n[BBOX-101] 3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试\n[BBOX-102] 验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。\n[BBOX-103] 跟踪合并用药\n[BBOX-104] 1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏\n[BBOX-105] 性鼻炎。\n[BBOX-106] 2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。\n[BBOX-107] 3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。\n[BBOX-108] 补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸\n[BBOX-109] 入 qd 治疗急性支气管炎。\n[BBOX-110] 预约下次安全性电话随访时间。\n[BBOX-111] 既往史:\n[BBOX-112] 过敏史:\n[BBOX-113] 个人史:\n[BBOX-114] 体格检查:\n[BBOX-115] 专科情况:\n[BBOX-116] 辅助检查:\n[BBOX-117] 治疗项目:\n[BBOX-118] 门诊诊断:\n[BBOX-119] 1、支气管哮喘\n[BBOX-120] 处置:\n[BBOX-121] 心电图(心电图室做)\n[BBOX-122] 伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天\n[BBOX-123] 孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天\n[BBOX-124] 备注:\n[BBOX-125] 医生:\n[BBOX-126] 门(急)诊处方\n[BBOX-127] 就诊时间:2025-09-15\n[BBOX-128] 就诊科室:内科门诊\n[BBOX-129] 主诊医\n[BBOX-130] 姓名\n[BBOX-131] 性别:男\n[BBOX-132] 年龄:64岁\n[BBOX-133] 卡号:4\n[BBOX-134] 患者\n[BBOX-135] 医疗证号:\n[BBOX-136] 处方号\n[BBOX-137] 地址:\n[BBOX-138] 身份证号:\n[BBOX-139] 诊断:支气管哮喘\n[BBOX-140] 西药处方\n[BBOX-141] 组号\n[BBOX-142] 项目名称\n[BBOX-143] 规格\n[BBOX-144] 总量\n[BBOX-145] 单价\n[BBOX-146] 金额\n[BBOX-147] R:\n[BBOX-148] 孟鲁司特钠片◆\n[BBOX-149] 10mg*30/瓶\n[BBOX-150] 30片\n[BBOX-151] 1.05\n[BBOX-152] 31.53\n[BBOX-153] Sig\n[BBOX-154] 10mg/次,口服,qn*30天\n[BBOX-155] 倍氯米松福莫特罗吸入气雾剂◆\n[BBOX-156] 6ug/揿*120揿\n[BBOX-157] 221.61\n[BBOX-158] 221.61\n[BBOX-159] Sig\n[BBOX-160] 2揿/次,吸入,bid*30天\n[BBOX-161] 医师\n[BBOX-162] 医生编号:1326\n[BBOX-163] 配剂人:\n[BBOX-164] 核对人:\n[BBOX-165] 合计:\n[BBOX-166] 收费员:\n[BBOX-167] 打印时间:2025-12-19\n[BBOX-168] 为了您的用药安全,药物处方当天有效 第 1 页共 1 页\n[BBOX-169] CS 扫描全能王\n[BBOX-170] 3亿人都在用的扫描App\n[BBOX-171] 门(急)诊处方\n[BBOX-172] 就诊时间:2025-08-18\n[BBOX-173] 就诊科室:内科门诊\n[BBOX-174] 主诊\n[BBOX-175] 姓名:\n[BBOX-176] 性别:男\n[BBOX-177] 年龄:64岁\n[BBOX-178] 卡号\n[BBOX-179] 患者类型:GCP支付\n[BBOX-180] 医疗证号:\n[BBOX-181] 处方\n[BBOX-182] 地址:\n[BBOX-183] 身份证号:\n[BBOX-184] 诊断:支气管哮喘\n[BBOX-185] 西药处方\n[BBOX-186] 组号\n[BBOX-187] 项目名称\n[BBOX-188] 规格\n[BBOX-189] 总量\n[BBOX-190] 单价\n[BBOX-191] 金额\n[BBOX-192] R:\n[BBOX-193] 孟鲁司特钠片◆\n[BBOX-194] 10mg*30/瓶\n[BBOX-195] 28片\n[BBOX-196] 1.05\n[BBOX-197] 29.43\n[BBOX-198] Sig\n[BBOX-199] 10mg/次,口服,qn*28天\n[BBOX-200] 倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿\n[BBOX-201] 221.61\n[BBOX-202] 221.61\n[BBOX-203] Sig\n[BBOX-204] 2揿/次,吸入,bid*30天\n[BBOX-205] 门(急)诊处方\n[BBOX-206] 就诊时间:2025-05-30\n[BBOX-207] 就诊科室:内科门诊\n[BBOX-208] 主\n[BBOX-209] 姓名\n[BBOX-210] 性别:男\n[BBOX-211] 年龄:64岁\n[BBOX-212] 卡\n[BBOX-213] 患者类型:GCP支付\n[BBOX-214] 医疗证号:\n[BBOX-215] 处\n[BBOX-216] 地址:\n[BBOX-217] 身份证号:\n[BBOX-218] 诊断:支气管哮喘\n[BBOX-219] 西药处方\n[BBOX-220] 组号\n[BBOX-221] 项目名称\n[BBOX-222] 规格\n[BBOX-223] 总量\n[BBOX-224] 单价\n[BBOX-225] 金额\n[BBOX-226] R:\n[BBOX-227] 孟鲁司特钠片◆\n[BBOX-228] 10mg*5/盒\n[BBOX-229] 90片\n[BBOX-230] 2.56\n[BBOX-231] 230.58\n[BBOX-232] Sig\n[BBOX-233] 10mg/次,口服,qn*90天\n[BBOX-234] 倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶\n[BBOX-235] 221.61\n[BBOX-236] 664.83\n[BBOX-237] Sig\n[BBOX-238] 2揿/次,吸入,bid*90天\n[BBOX-239] 门(急)诊处方\n[BBOX-240] 就诊时间:2025-03-05\n[BBOX-241] 就诊科室:内科门诊\n[BBOX-242] 主诊医\n[BBOX-243] 姓名\n[BBOX-244] 性别:男\n[BBOX-245] 年龄:64岁\n[BBOX-246] 卡号:\n[BBOX-247] 患者类型:GCP支付\n[BBOX-248] 医疗证号:\n[BBOX-249] 处方号:\n[BBOX-250] 地址:\n[BBOX-251] 身份证号:\n[BBOX-252] 诊断:支气管哮喘\n[BBOX-253] 西药处方\n[BBOX-254] 组号\n[BBOX-255] 项目名称\n[BBOX-256] 规格\n[BBOX-257] 总量\n[BBOX-258] 单价\n[BBOX-259] 金额\n[BBOX-260] R:\n[BBOX-261] 倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶\n[BBOX-262] 221.61 443.22\n[BBOX-263] Sig\n[BBOX-264] 2揿/次,吸入,bid*60天\n[BBOX-265] 孟鲁司特钠片\n[BBOX-266] 10mg*30/瓶\n[BBOX-267] 60片\n[BBOX-268] 1.05\n[BBOX-269] 63.06\n[BBOX-270] Sig\n[BBOX-271] 10mg/次,口服,qn*60天\n[BBOX-272] 门(急)诊处方\n[BBOX-273] 就诊时间:2025-03-05\n[BBOX-274] 就诊科室:内科门诊\n[BBOX-275] 主诊\n[BBOX-276] 姓名\n[BBOX-277] 性别:男\n[BBOX-278] 年龄:64岁\n[BBOX-279] 卡号\n[BBOX-280] 患者类型:GCP支付\n[BBOX-281] 医疗证号:\n[BBOX-282] 处方\n[BBOX-283] 地址:\n[BBOX-284] 身份证号:\n[BBOX-285] 诊断:支气管哮喘\n[BBOX-286] 西药处方\n[BBOX-287] 组号\n[BBOX-288] 项目名称\n[BBOX-289] 规格\n[BBOX-290] 总量\n[BBOX-291] 单价\n[BBOX-292] 金额\n[BBOX-293] R:\n[BBOX-294] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-295] 221.61 221.61\n[BBOX-296] Sig\n[BBOX-297] 2揿/次,吸入,bid*30天\n[BBOX-298] 孟鲁司特钠片\n[BBOX-299] 10mg*30/瓶\n[BBOX-300] 30片\n[BBOX-301] 1.05\n[BBOX-302] 31.53\n[BBOX-303] Sig\n[BBOX-304] 10mg/次,口服,qn*30天\n[BBOX-305] CS 扫描全能王\n[BBOX-306] 3亿人都在用的扫描App\n[BBOX-307] 门(急)诊处方\n[BBOX-308] 就诊时间:2025-02-08\n[BBOX-309] 就诊科室:内科门诊\n[BBOX-310] 主诊\n[BBOX-311] 姓名:\n[BBOX-312] 性别:男\n[BBOX-313] 年龄:64岁\n[BBOX-314] 卡号:\n[BBOX-315] 患者类型:001 支付\n[BBOX-316] 医疗证号:\n[BBOX-317] 处方\n[BBOX-318] 地址:\n[BBOX-319] 身份证号:\n[BBOX-320] 诊断:支气管哮喘\n[BBOX-321] 西药处方\n[BBOX-322] 组号\n[BBOX-323] 项目名称\n[BBOX-324] 规格\n[BBOX-325] 总量\n[BBOX-326] 单价\n[BBOX-327] 金额\n[BBOX-328] R:\n[BBOX-329] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶\n[BBOX-330] 221.61 221.61\n[BBOX-331] Sig\n[BBOX-332] 2揿/次,吸入,bid*30天\n[BBOX-333] 孟鲁司特钠片◆\n[BBOX-334] 10mg*30/瓶\n[BBOX-335] 30片\n[BBOX-336] 1.05\n[BBOX-337] 31.53\n[BBOX-338] Sig\n[BBOX-339] 10mg/次,口服,qn*30天\n[BBOX-340] CS 扫描全能王\n[BBOX-341] 3亿人都在用的扫描App\n[BBOX-342] 门(急)诊处方\n[BBOX-343] 就诊时间:2025-01-10\n[BBOX-344] 就诊科室:内科门诊\n[BBOX-345] 主诊\n[BBOX-346] 性别:男\n[BBOX-347] 年龄:64岁\n[BBOX-348] 卡号\n[BBOX-349] 患者类型:G\n[BBOX-350] 医疗证号:\n[BBOX-351] 处方\n[BBOX-352] 地址:\n[BBOX-353] 身份证号:\n[BBOX-354] 诊断:支气管哮喘\n[BBOX-355] 西药处方\n[BBOX-356] 组号\n[BBOX-357] 项目名称\n[BBOX-358] 规格\n[BBOX-359] 总量\n[BBOX-360] 单价\n[BBOX-361] 金额\n[BBOX-362] R:\n[BBOX-363] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-364] 221.61 221.61\n[BBOX-365] Sig\n[BBOX-366] 2揿/次,吸入,bid*30天\n[BBOX-367] 孟鲁司特钠片\n[BBOX-368] 10mg*30/瓶\n[BBOX-369] 30片\n[BBOX-370] 1.05\n[BBOX-371] 31.53\n[BBOX-372] Sig\n[BBOX-373] 10mg/次,口服,qn*30天\n[BBOX-374] 门(急)诊处方\n[BBOX-375] 就诊时间:2024-12-11\n[BBOX-376] 就诊科室:内科门诊\n[BBOX-377] 主诊\n[BBOX-378] 姓名:\n[BBOX-379] 性别:男\n[BBOX-380] 年龄:64岁\n[BBOX-381] 卡号\n[BBOX-382] 患者类型:GCP支付\n[BBOX-383] 医疗证号:\n[BBOX-384] 处方\n[BBOX-385] 地址:\n[BBOX-386] 身份证号:\n[BBOX-387] 诊断:支气管哮喘\n[BBOX-388] 西药处方\n[BBOX-389] 组号\n[BBOX-390] 项目名称\n[BBOX-391] 规格\n[BBOX-392] 总量\n[BBOX-393] 单价\n[BBOX-394] 金额\n[BBOX-395] R:\n[BBOX-396] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶\n[BBOX-397] 221.61 221.61\n[BBOX-398] Sig\n[BBOX-399] 2揿/次,吸入,bid*30天\n[BBOX-400] 孟鲁司特钠片◆\n[BBOX-401] 10mg*30/瓶\n[BBOX-402] 30片\n[BBOX-403] 1.05\n[BBOX-404] 31.53\n[BBOX-405] Sig\n[BBOX-406] 10mg/次,口服,qn*30天\n[BBOX-407] CS 扫描全能王\n[BBOX-408] 3亿人都在用的扫描App\n[BBOX-409] 门(急)诊处方\n[BBOX-410] 就诊时间:2024-11-18\n[BBOX-411] 就诊科室:内科门诊\n[BBOX-412] 主诊\n[BBOX-413] 姓名\n[BBOX-414] 性别:男\n[BBOX-415] 年龄:63岁\n[BBOX-416] 卡号:\n[BBOX-417] 患者类型:GLP支付\n[BBOX-418] 医疗证号:\n[BBOX-419] 处方\n[BBOX-420] 地址:\n[BBOX-421] 身份证号:\n[BBOX-422] 诊断:支气管哮喘,非危重\n[BBOX-423] 西药处方\n[BBOX-424] 组号\n[BBOX-425] 项目名称\n[BBOX-426] 规格\n[BBOX-427] 总量\n[BBOX-428] 单价\n[BBOX-429] 金额\n[BBOX-430] R:\n[BBOX-431] 倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n[BBOX-432] 221.61 221.61\n[BBOX-433] Sig\n[BBOX-434] 2揿/次,吸入,bid*30天\n[BBOX-435] 孟鲁司特钠片\n[BBOX-436] 10mg*30/瓶\n[BBOX-437] 30片\n[BBOX-438] 1.05\n[BBOX-439] 31.53\n[BBOX-440] Sig\n[BBOX-441] 10mg/次,口服,qn*30天\n[BBOX-442] CS 扫描全能王\n[BBOX-443] 3亿人都在用的扫描App\n[BBOX-444] \\begin{tabular}{ccccccl}\n[BBOX-445] \\hline\n[BBOX-446] 序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\\\\n[BBOX-447] \\hline\n[BBOX-448] 1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\\\\n[BBOX-449] 2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\\\\n[BBOX-450] 3 & 中性粒细胞百分数(NEUN) & 62.30 & & \\% & 40 -- 75 & \\\\\n[BBOX-451] 4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\\\\n[BBOX-452] 5 & 淋巴细胞百分数(LYN) & 28.60 & & \\% & 20 -- 50 & \\\\\n[BBOX-453] 6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\\\\n[BBOX-454] 7 & 单核细胞百分数(MON%) & 5.10 & & \\% & 3 -- 10 & \\\\\n[BBOX-455] 8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\\\\n[BBOX-456] 9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \\% & 0.4 -- 8 & \\\\\n[BBOX-457] 10 & 嗜碱性粒细胞总数(BASO) & 0.03 & & 10^9/L & 0 -- 0.06 & \\\\\n[BBOX-458] 11 & 嗜碱性粒细胞百分比(BASO%) & 0.30 & & \\% & 0 -- 1 & \\\\\n[BBOX-459] 12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\\\\n[BBOX-460] 13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\\\\n[BBOX-461] 14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \\% & 40 -- 50 & \\\\\n[BBOX-462] 15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\\\\n[BBOX-463] 16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\\\\n[BBOX-464] 17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\\\\n[BBOX-465] 18 & 红细胞分���宽度(RDW) & 12.40 & & \\% & 11.6 -- 14.8 & \\\\\n[BBOX-466] 19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\\\\n[BBOX-467] 20 & 血小板(PLT) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\\\\n[BBOX-468] 21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\\\\n[BBOX-469] 22 & 平均血小板比容(Pct) & 0.21 & & \\% & 0.10 -- 0.29 & \\\\\n[BBOX-470] 23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\\\\n[BBOX-471] 24 & 大血小板(P-LCR) & 30.90 & & \\% & & \\\\\n[BBOX-472] 25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\\\\n[BBOX-473] 26 & 网织红细胞百分数(RETR) & 1.64 & & \\% & & \\\\\n[BBOX-474] 27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\\downarrow$ & \\% & 89.9 -- 98.4 & \\\\\n[BBOX-475] 28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\\uparrow$ & \\% & 1.6 -- 9.5 & \\\\\n[BBOX-476] 29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\\uparrow$ & \\% & 0 -- 1.7 & \\\\\n[BBOX-477] 30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\\uparrow$ & \\% & 1.6 -- 10.5 & \\\\\n[BBOX-478] 31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\\\\n[BBOX-479] 32 & 有核红细胞百分比(NRBC%) & 0 & & \\% & & \\\\\n[BBOX-480] \\hline\n[BBOX-481] \\end{tabular}\n[BBOX-482] 处方笺\n[BBOX-483] 普通\n[BBOX-484] 诊疗\n[BBOX-485] 患者姓\n[BBOX-486] 男\n[BBOX-487] 年龄：65岁\n[BBOX-488] 费别：\n[BBOX-489] 科室：\n[BBOX-490] 2026-01-06 11:28:26\n[BBOX-491] 处方号\n[BBOX-492] 地址：\n[BBOX-493] 联系电\n[BBOX-494] 身份号\n[BBOX-495] 诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\n[BBOX-496] R\n[BBOX-497] P:\n[BBOX-498] 倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120\n[BBOX-499] 1瓶\n[BBOX-500] 剂量：每次2揿 （1/60 瓶）\n[BBOX-501] 用法：吸入用药\n[BBOX-502] bid 01-06\n[BBOX-503] 孟鲁司特钠片(省采)◆\n[BBOX-504] 10mg*5/盒\n[BBOX-505] 30片\n[BBOX-506] 剂量：每次10mg （1 片）\n[BBOX-507] 用法：口服\n[BBOX-508] qd 01-06\n[BBOX-509] 处方金额：298.47元\n[BBOX-510] 取药药房：门诊西药房（荔湾）\n[BBOX-511] 处方笺\n[BBOX-512] 普通\n[BBOX-513] 诊断\n[BBOX-514] 患者\n[BBOX-515] 年龄：65岁\n[BBOX-516] 费别\n[BBOX-517] 科室\n[BBOX-518] 6-01-06 11:31:02\n[BBOX-519] 处方\n[BBOX-520] 地址\n[BBOX-521] 联系\n[BBOX-522] 身份\n[BBOX-523] 诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎\n[BBOX-524] Rp:\n[BBOX-525] 左氧氟沙星片(省采)●⑥\n[BBOX-526] 0.5g*28片/盒\n[BBOX-527] 3片\n[BBOX-528] 剂量：每次0.5g\n[BBOX-529] (1 片)\n[BBOX-530] 用法：口服\n[BBOX-531] qd\n[BBOX-532] 01-06\n[BBOX-533] 醋酸泼尼松片●②⑥\n[BBOX-534] 5mg*100/瓶\n[BBOX-535] 6片\n[BBOX-536] 剂量：每次10mg\n[BBOX-537] (2 片)\n[BBOX-538] 用法：口服\n[BBOX-539] qm\n[BBOX-540] 01-06\n[BBOX-541] 盐酸氨溴索分散片(省采)●⑥\n[BBOX-542] 30mg*50/盒\n[BBOX-543] 15片\n[BBOX-544] 剂量：每次30mg\n[BBOX-545] (1 片)\n[BBOX-546] 用法：餐后口服\n[BBOX-547] tid\n[BBOX-548] 01-06\n[BBOX-549] 处方金额：3.47元\n[BBOX-550] 取药药房：门诊西药房（荔湾）\n[BBOX-551] 医师手签：\n[BBOX-552] 病历编号：\n[BBOX-553] 姓名：\n[BBOX-554] 性别：男\n[BBOX-555] 年龄：65岁\n[BBOX-556] 就诊科室：内科门诊（基础）\n[BBOX-557] 医生：\n[BBOX-558] 就诊时间：2026-02-04 11:23:30\n[BBOX-559] 主诉：支气管哮喘治疗后复诊\n[BBOX-560] 现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，\n[BBOX-561] 无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：\n[BBOX-562] 两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。\n[BBOX-563] 既往史：鼻炎病史，有糖尿病史\n[BBOX-564] 过敏史：未发现\n[BBOX-565] 个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。\n[BBOX-566] 体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。\n[BBOX-567] 专科情况：\n[BBOX-568] 辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：\n[BBOX-569] 5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：\n[BBOX-570] 0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化\n[BBOX-571] 氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发\n[BBOX-572] 试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常\n[BBOX-573] 治疗项目：\n[BBOX-574] 门诊诊断：\n[BBOX-575] 1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病\n[BBOX-576] 单病种：\n[BBOX-577] 发病时间：\n[BBOX-578] 处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。\n[BBOX-579] 倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天\n[BBOX-580] 孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天\n[BBOX-581] 备注：建议在停药附近社区医疗机构随访。"
  }
]
2026-08-10 11:06:54,472 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:54,507 INFO     29 [SmartSplitter] SmartSplitter done: 16 chunks from 16 LLM segments (all bbox_id). Types: {'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}
2026-08-10 11:06:54,525 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 11:06:54,526 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks": "16 items, types={'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}"}
2026-08-10 11:06:54,526 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 11:06:54,527 INFO     29 [ChunkRouter] Routed 16 chunks into 3 groups: {'chunks_Clinical': 4, 'chunks_Prescription': 11, 'chunks_LabExam': 1}
2026-08-10 11:06:54,539 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 11:06:54,539 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | ChunkRouter:Router | outputs={"html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks": "16 items, types={'OutpatientRecord': 4, 'PrescriptionRecord': 11, 'LabReport': 1}", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:06:54,540 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 11:06:54,546 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:06:54,547 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:06:54,547 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 11:06:54,547 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:06:54,725 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1653)
2026-08-10 11:06:54,726 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:54,726 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 444, \"bbox_end\": 481, \"encounter_dates\": [], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccl}\n\\hline\n序号 & 项目代码 & 结果 & 提示 & 单位 & 参考范围 & 试验方法 \\\\\n\\hline\n1 & 白细胞(WBC) & 9.17 & & 10^9/L & 3.5 -- 9.5 & \\\\\n2 & 中性粒细胞总数(NEU) & 5.71 & & 10^9/L & 1.8 -- 6.3 & \\\\\n3 & 中性粒细胞百分数(NEUN) & 62.30 & & \\% & 40 -- 75 & \\\\\n4 & 淋巴细胞总数(LY) & 2.62 & & 10^9/L & 1.1 -- 3.2 & \\\\\n5 & 淋巴细胞百分数(LYN) & 28.60 & & \\% & 20 -- 50 & \\\\\n6 & 单核细胞总数(MONO) & 0.47 & & 10^9/L & 0.1 -- 0.6 & \\\\\n7 & 单核细胞百分数(MON%) & 5.10 & & \\% & 3 -- 10 & \\\\\n8 & 嗜酸性粒细胞总数(EOS) & 0.34 & & 10^9/L & 0.02 -- 0.52 & \\\\\n9 & 嗜酸性粒细胞百分数(EOS%) & 3.70 & & \\% & 0.4 -- 8 & \\\\\n10 & 嗜碱性粒细胞总数(BASO) & 0.03 & & 10^9/L & 0 -- 0.06 & \\\\\n11 & 嗜碱性粒细胞百分比(BASO%) & 0.30 & & \\% & 0 -- 1 & \\\\\n12 & 红细胞(RBC) & 4.91 & 【广州】 & 10^12/L & 4.3 -- 5.8 & \\\\\n13 & 血红蛋白(HGB) & 158 & 【广州】 & g/L & 130 -- 175 & \\\\\n14 & 红细胞压积(HCT) & 47.10 & 【广州】 & \\% & 40 -- 50 & \\\\\n15 & 红细胞平均容积(MCV) & 96.90 & 【广州】 & fl & 82 -- 100 & \\\\\n16 & 红细胞平均血红蛋白(MCH) & 32.20 & 【广州】 & pg & 27 -- 34 & \\\\\n17 & 红细胞平均血红蛋白浓度(MCHC) & 335.00 & 【广州】 & g/L & 316 -- 354 & \\\\\n18 & 红细胞分布宽度(RDW) & 12.40 & & \\% & 11.6 -- 14.8 & \\\\\n19 & 红细胞分布宽度-SD(RDW-SD) & 44.10 & & fl & 37.1 -- 49.2 & \\\\\n20 & 血小板(PLT) & 197 & 【广州】 & 10^9/L & 125 -- 350 & \\\\\n21 & 平均血小板容积(MPV) & 10.70 & & fl & 6 -- 12 & \\\\\n22 & 平均血小板比容(Pct) & 0.21 & & \\% & 0.10 -- 0.29 & \\\\\n23 & 血小板分布宽度(PDW) & 13.00 & & 10(GSP) & 15.3 -- 20.5 & \\\\\n24 & 大血小板(P-LCR) & 30.90 & & \\% & & \\\\\n25 & 网织红细胞绝对值(RETR) & 90.5 & & 10^9/L & 46.4 -- 121.2 & \\\\\n26 & 网织红细胞百分数(RETR) & 1.64 & & \\% & & \\\\\n27 & 低荧光强度网织红细胞比率(LFF) & 83.8 & $\\downarrow$ & \\% & 89.9 -- 98.4 & \\\\\n28 & 中荧光强度网织红细胞比率(MFF) & 13.3 & $\\uparrow$ & \\% & 1.6 -- 9.5 & \\\\\n29 & 高荧光强度网织红细胞比率(HFF) & 2.9 & $\\uparrow$ & \\% & 0 -- 1.7 & \\\\\n30 & 未成熟网织红细胞比率(IRF) & 16.2 & $\\uparrow$ & \\% & 1.6 -- 10.5 & \\\\\n31 & 有核红细胞计数(NRBCW) & 0 & & 10^9/L & & \\\\\n32 & 有核红细胞百分比(NRBC%) & 0 & & \\% & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 11:06:58,992 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:06:58,992 INFO     29 [qwen-vl-text] LLM output (len=2868):
{
  "encounter_date": "2020-07-08",
  "dm_name": null,
  "dm_gender": "女",
  "dm_age": 36,
  "dm_ethnicity": "汉族",
  "dm_marital_status": "已婚",
  "dm_occupation": "护士",
  "dm_admission_time": "2020-07-08 08:36",
  "dm_record_time": "2020-07-08 08:36",
  "dm_history_provider": "本人",
  "cc_text": "停经39周，要求住院待产。",
  "cc_main_symptoms": [
    "停经"
  ],
  "cc_duration": "39周",
  "pi_text": "平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。",
  "pmh_disease_history": [
    "平素体健",
    "否认心脏病",
    "否认高血压",
    "否认糖尿病",
    "否认肾病",
    "否认肝炎",
    "否认结核"
  ],
  "pmh_allergy_history": [
    "无"
  ],
  "pmh_surgery_trauma_history": [
    "2016.08行剖宫产手术"
  ],
  "ph_smoking": "无",
  "ph_drinking": "无",
  "oh_menarche_age": 12,
  "oh_menopause_age": null,
  "oh_pregnancies": "G2P1",
  "fh_text": "父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。",
  "fh_hereditary_diseases": [],
  "vs_temperature_c": 36.5,
  "vs_pulse_bpm": 78,
  "vs_respiration_rpm": 18,
  "vs_systolic_bp_mmhg": 98,
  "vs_diastolic_bp_mmhg": 64,
  "pe_general_condition": "发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言语状态流利;检查时能合作等。",
  "pe_skin_mucosa": "色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创伤、溃疡、结节。",
  "pe_lymph_nodes": "全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。",
  "pe_lungs": "视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。触诊:语音震颤两侧相等,无摩擦感。叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm。听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、干啰音、湿啰音。",
  "pe_heart": "视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前区无异常搏动、局限性膨隆。触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、震颤、摩擦感。叩诊：左右心界线以每肋间距胸骨中线的cm数记载。听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分裂，P2<A2。",
  "pe_abdomen": "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆起，下腹可见一长约15cm横行手术疤痕。触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度鼓音，移动性浊音阴性。听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血管杂音。",
  "pe_extremities": "无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎缩;关节无红肿、畸形、运动障碍,双下肢水肿。",
  "pe_nervous_system": "膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。",
  "pe_specialist_exam": "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无宫缩,未见红,未破水,骨盆外测量及内诊:未做。",
  "pe_ecog_score": null,
  "pat_text": "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指数8.5cm),胎盘成熟度II°。",
  "pat_items": [
    "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指数8.5cm),胎盘成熟度II°"
  ],
  "preliminary_diagnoses": [
    {
      "name": "妊娠合并子宫瘢痕",
      "diagnosis_type": "西医",
      "is_primary": true
    },
    {
      "name": "孕2产1",
      "diagnosis_type": "西医",
      "is_primary": false
    },
    {
      "name": "宫内孕39周头位待产",
      "diagnosis_type": "西医",
      "is_primary": false
    }
  ],
  "department": "产科二区"
}
2026-08-10 11:06:58,992 INFO     29 [qwen-vl-text] Updated encounter_dates=[2020-07-08]
2026-08-10 11:06:58,994 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1324264, prompt_len=1697
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共49行）
["院", "入院记录", "姓名：", "科室：产科二区", "床号：", "科室：产科二区", "第(1)次入院记录", "过敏史：无", "姓名：", "性别：女", "年龄：36岁", "身份证号", "职业：", "婚姻：已婚", "民族：汉族", "出生地：", "现住址：", "入院日期：2020-07-08 08:36:09", "邮编", "病史采集时间：2020-07-08 08:36:09", "联系人：", "与病人关系：夫妻", "病史叙述者：本人", "联系人地址：同上地址", "电话.", "可靠程度：可靠", "主诉：停经39周，要求住院待产。", "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接", "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "婚育史：31岁结婚，爱人", "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "历），量中等，色暗红，偶有血块，无痛经。", "页", "书写者签名：", "总第 页"]

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
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord API raw response (len=3093):
[
	{"text": "院", "bbox": [587, 57, 619, 77]},
	{"text": "入院记录", "bbox": [445, 93, 580, 111]},
	{"text": "姓名：", "bbox": [139, 120, 216, 136]},
	{"text": "科室：产科二区", "bbox": [320, 120, 452, 136]},
	{"text": "床号：", "bbox": [519, 120, 562, 136]},
	{"text": "科室：产科二区", "bbox": [139, 144, 270, 159]},
	{"text": "第(1)次入院记录", "bbox": [389, 144, 529, 159]},
	{"text": "过敏史：无", "bbox": [597, 144, 693, 159]},
	{"text": "姓名：", "bbox": [139, 170, 184, 185]},
	{"text": "性别：女", "bbox": [315, 170, 391, 185]},
	{"text": "年龄：36岁", "bbox": [446, 170, 538, 185]},
	{"text": "身份证号", "bbox": [585, 170, 656, 185]},
	{"text": "职业：", "bbox": [139, 195, 184, 210]},
	{"text": "婚姻：已婚", "bbox": [315, 195, 410, 210]},
	{"text": "民族：汉族", "bbox": [446, 195, 540, 210]},
	{"text": "出生地：", "bbox": [585, 195, 647, 210]},
	{"text": "现住址：", "bbox": [139, 222, 231, 238]},
	{"text": "入院日期：2020-07-08 08:36:09", "bbox": [550, 222, 818, 238]},
	{"text": "邮编", "bbox": [139, 248, 177, 264]},
	{"text": "病史采集时间：2020-07-08 08:36:09", "bbox": [541, 248, 846, 264]},
	{"text": "联系人：", "bbox": [139, 274, 202, 290]},
	{"text": "与病人关系：夫妻", "bbox": [445, 274, 592, 290]},
	{"text": "病史叙述者：本人", "bbox": [667, 274, 814, 290]},
	{"text": "联系人地址：同上地址", "bbox": [139, 301, 328, 317]},
	{"text": "电话.", "bbox": [445, 301, 489, 317]},
	{"text": "可靠程度：可靠", "bbox": [667, 301, 797, 317]},
	{"text": "主诉：停经39周，要求住院待产。", "bbox": [168, 347, 440, 363]},
	{"text": "现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产", "bbox": [131, 372, 891, 388]},
	{"text": "期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合", "bbox": [131, 398, 891, 414]},
	{"text": "孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接", "bbox": [131, 424, 891, 440]},
	{"text": "触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA", "bbox": [131, 450, 891, 466]},
	{"text": "结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛", "bbox": [131, 476, 891, 492]},
	{"text": "查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰", "bbox": [131, 502, 891, 518]},
	{"text": "痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子", "bbox": [131, 528, 891, 544]},
	{"text": "宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。", "bbox": [131, 555, 770, 571]},
	{"text": "既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有", "bbox": [170, 581, 891, 597]},
	{"text": "“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血", "bbox": [139, 607, 882, 623]},
	{"text": "史，有献血史，否认食物及药物过敏史。预防接种随社会进行。", "bbox": [131, 634, 643, 650]},
	{"text": "个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住", "bbox": [172, 660, 893, 676]},
	{"text": "史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。", "bbox": [131, 687, 716, 703]},
	{"text": "婚育史：31岁结婚，爱人", "bbox": [169, 714, 378, 730]},
	{"text": "现年37岁，职员，工作于三门峡市党校，身体健康，无吸", "bbox": [431, 714, 893, 730]},
	{"text": "烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男", "bbox": [131, 740, 876, 756]},
	{"text": "婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。", "bbox": [131, 767, 624, 783]},
	{"text": "月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳", "bbox": [179, 793, 894, 809]},
	{"text": "历），量中等，色暗红，偶有血块，无痛经。", "bbox": [131, 820, 496, 836]},
	{"text": "页", "bbox": [491, 887, 538, 901]},
	{"text": "书写者签名：", "bbox": [613, 887, 700, 901]},
	{"text": "总第 页", "bbox": [833, 885, 897, 900]}
]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord API: raw_items=49, valid_items=49, elapsed=17.9s
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[587, 57, 619, 77]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[445, 93, 580, 111]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[139, 120, 216, 136]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[3]: text=科室：产科二区, bbox=[320, 120, 452, 136]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[4]: text=床号：, bbox=[519, 120, 562, 136]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[5]: text=科室：产科二区, bbox=[139, 144, 270, 159]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[6]: text=第(1)次入院记录, bbox=[389, 144, 529, 159]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[7]: text=过敏史：无, bbox=[597, 144, 693, 159]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[8]: text=姓名：, bbox=[139, 170, 184, 185]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[9]: text=性别：女, bbox=[315, 170, 391, 185]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[10]: text=年龄：36岁, bbox=[446, 170, 538, 185]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号, bbox=[585, 170, 656, 185]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[12]: text=职业：, bbox=[139, 195, 184, 210]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[13]: text=婚姻：已婚, bbox=[315, 195, 410, 210]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[14]: text=民族：汉族, bbox=[446, 195, 540, 210]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[15]: text=出生地：, bbox=[585, 195, 647, 210]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[16]: text=现住址：, bbox=[139, 222, 231, 238]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[17]: text=入院日期：2020-07-08 08:36:09, bbox=[550, 222, 818, 238]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[18]: text=邮编, bbox=[139, 248, 177, 264]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[19]: text=病史采集时间：2020-07-08 08:36:09, bbox=[541, 248, 846, 264]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[20]: text=联系人：, bbox=[139, 274, 202, 290]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[21]: text=与病人关系：夫妻, bbox=[445, 274, 592, 290]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[22]: text=病史叙述者：本人, bbox=[667, 274, 814, 290]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[23]: text=联系人地址：同上地址, bbox=[139, 301, 328, 317]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[24]: text=电话., bbox=[445, 301, 489, 317]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[25]: text=可靠程度：可靠, bbox=[667, 301, 797, 317]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[26]: text=主诉：停经39周，要求住院待产。, bbox=[168, 347, 440, 363]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[27]: text=现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产, bbox=[131, 372, 891, 388]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[28]: text=期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合, bbox=[131, 398, 891, 414]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[29]: text=孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接, bbox=[131, 424, 891, 440]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[30]: text=触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA, bbox=[131, 450, 891, 466]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[31]: text=结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛, bbox=[131, 476, 891, 492]
2026-08-10 11:07:16,941 INFO     29 [qwen-vl-text] coord item[32]: text=查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰, bbox=[131, 502, 891, 518]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[33]: text=痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子, bbox=[131, 528, 891, 544]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[34]: text=宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。, bbox=[131, 555, 770, 571]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[35]: text=既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有, bbox=[170, 581, 891, 597]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[36]: text=“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血, bbox=[139, 607, 882, 623]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[37]: text=史，有献血史，否认食物及药物过敏史。预防接种随社会进行。, bbox=[131, 634, 643, 650]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[38]: text=个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住, bbox=[172, 660, 893, 676]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[39]: text=史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。, bbox=[131, 687, 716, 703]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[40]: text=婚育史：31岁结婚，爱人, bbox=[169, 714, 378, 730]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[41]: text=现年37岁，职员，工作于三门峡市党校，身体健康，无吸, bbox=[431, 714, 893, 730]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[42]: text=烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男, bbox=[131, 740, 876, 756]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[43]: text=婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。, bbox=[131, 767, 624, 783]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[44]: text=月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳, bbox=[179, 793, 894, 809]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[45]: text=历），量中等，色暗红，偶有血块，无痛经。, bbox=[131, 820, 496, 836]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[46]: text=页, bbox=[491, 887, 538, 901]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[47]: text=书写者签名：, bbox=[613, 887, 700, 901]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] coord item[48]: text=总第 页, bbox=[833, 885, 897, 900]
2026-08-10 11:07:16,942 INFO     29 [qwen-vl-text] page=5 — 49/49 coords, api_time=17.9s
2026-08-10 11:07:16,944 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1249766, prompt_len=1544
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共40行）
["院", "入院记录", "姓名:", "科室:产科二区", "床号:", "生.", "家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。", "体格检查", "体温:36.5℃", "脉搏:78次/分", "呼吸:18次/分", "血压:98/64mmHg", "身高160cm", "体重:60Kg", "一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言", "语状态流利;检查时能合作等。", "皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "伤、溃疡、结节。", "淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。", "头部:", "头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。", "眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,", "间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。", "耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。", "鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异", "常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿", "大、分泌物;咽部无充血、分泌物。", "颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居", "中,甲状腺无肿大。", "胸部", "胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉", "曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。", "肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。", "触诊:语音震颤两侧相等,无摩擦感。", "叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,", "听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、", "第页", "书写者签名:", "总第页"]

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
2026-08-10 11:07:30,943 INFO     29 [qwen-vl-text] coord API raw response (len=2571):
[
	{"text": "院", "bbox": [577, 60, 624, 81]},
	{"text": "入院记录", "bbox": [442, 97, 584, 116]},
	{"text": "姓名:", "bbox": [125, 126, 170, 141]},
	{"text": "科室:产科二区", "bbox": [313, 126, 450, 141]},
	{"text": "床号:", "bbox": [519, 126, 564, 141]},
	{"text": "生.", "bbox": [698, 126, 762, 141]},
	{"text": "家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。", "bbox": [154, 149, 889, 165]},
	{"text": "体格检查", "bbox": [464, 180, 557, 197]},
	{"text": "体温:36.5℃", "bbox": [154, 212, 269, 227]},
	{"text": "脉搏:78次/分", "bbox": [309, 212, 435, 227]},
	{"text": "呼吸:18次/分", "bbox": [480, 212, 606, 227]},
	{"text": "血压:98/64mmHg", "bbox": [667, 212, 812, 228]},
	{"text": "身高160cm", "bbox": [154, 240, 251, 255]},
	{"text": "体重:60Kg", "bbox": [309, 240, 407, 257]},
	{"text": "一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言", "bbox": [154, 267, 909, 283]},
	{"text": "语状态流利;检查时能合作等。", "bbox": [114, 293, 376, 309]},
	{"text": "皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创", "bbox": [154, 321, 909, 337]},
	{"text": "伤、溃疡、结节。", "bbox": [114, 348, 259, 364]},
	{"text": "淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。", "bbox": [154, 375, 800, 391]},
	{"text": "头部:", "bbox": [154, 402, 198, 418]},
	{"text": "头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。", "bbox": [154, 429, 839, 445]},
	{"text": "眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,", "bbox": [154, 456, 897, 472]},
	{"text": "间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。", "bbox": [114, 483, 840, 499]},
	{"text": "耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。", "bbox": [154, 510, 713, 526]},
	{"text": "鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。", "bbox": [154, 536, 839, 552]},
	{"text": "口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异", "bbox": [154, 563, 909, 579]},
	{"text": "常:牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿", "bbox": [114, 590, 890, 606]},
	{"text": "大、分泌物;咽部无充血、分泌物。", "bbox": [114, 617, 416, 633]},
	{"text": "颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居", "bbox": [154, 644, 890, 660]},
	{"text": "中,甲状腺无肿大。", "bbox": [114, 671, 278, 687]},
	{"text": "胸部", "bbox": [154, 698, 193, 714]},
	{"text": "胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉", "bbox": [154, 725, 909, 741]},
	{"text": "曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。", "bbox": [114, 752, 588, 768]},
	{"text": "肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。", "bbox": [154, 779, 800, 795]},
	{"text": "触诊:语音震颤两侧相等,无摩擦感。", "bbox": [212, 806, 529, 822]},
	{"text": "叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,", "bbox": [212, 833, 772, 849]},
	{"text": "听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、", "bbox": [212, 859, 898, 875]},
	{"text": "第页", "bbox": [487, 906, 536, 920]},
	{"text": "书写者签名:", "bbox": [614, 906, 704, 920]},
	{"text": "总第页", "bbox": [844, 906, 911, 920]}
]
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord API: raw_items=40, valid_items=40, elapsed=14.0s
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[577, 60, 624, 81]
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[442, 97, 584, 116]
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord item[2]: text=姓名:, bbox=[125, 126, 170, 141]
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord item[3]: text=科室:产科二区, bbox=[313, 126, 450, 141]
2026-08-10 11:07:30,944 INFO     29 [qwen-vl-text] coord item[4]: text=床号:, bbox=[519, 126, 564, 141]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[5]: text=生., bbox=[698, 126, 762, 141]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[6]: text=家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。, bbox=[154, 149, 889, 165]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[7]: text=体格检查, bbox=[464, 180, 557, 197]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[8]: text=体温:36.5℃, bbox=[154, 212, 269, 227]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[9]: text=脉搏:78次/分, bbox=[309, 212, 435, 227]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[10]: text=呼吸:18次/分, bbox=[480, 212, 606, 227]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[11]: text=血压:98/64mmHg, bbox=[667, 212, 812, 228]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[12]: text=身高160cm, bbox=[154, 240, 251, 255]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[13]: text=体重:60Kg, bbox=[309, 240, 407, 257]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[14]: text=一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言, bbox=[154, 267, 909, 283]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[15]: text=语状态流利;检查时能合作等。, bbox=[114, 293, 376, 309]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[16]: text=皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创, bbox=[154, 321, 909, 337]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[17]: text=伤、溃疡、结节。, bbox=[114, 348, 259, 364]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[18]: text=淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。, bbox=[154, 375, 800, 391]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[19]: text=头部:, bbox=[154, 402, 198, 418]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[20]: text=头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。, bbox=[154, 429, 839, 445]
2026-08-10 11:07:30,945 INFO     29 [qwen-vl-text] coord item[21]: text=眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,, bbox=[154, 456, 897, 472]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[22]: text=间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。, bbox=[114, 483, 840, 499]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[23]: text=耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。, bbox=[154, 510, 713, 526]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[24]: text=鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。, bbox=[154, 536, 839, 552]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[25]: text=口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异, bbox=[154, 563, 909, 579]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[26]: text=常:牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿, bbox=[114, 590, 890, 606]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[27]: text=大、分泌物;咽部无充血、分泌物。, bbox=[114, 617, 416, 633]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[28]: text=颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居, bbox=[154, 644, 890, 660]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[29]: text=中,甲状腺无肿大。, bbox=[114, 671, 278, 687]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[30]: text=胸部, bbox=[154, 698, 193, 714]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[31]: text=胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉, bbox=[154, 725, 909, 741]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[32]: text=曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。, bbox=[114, 752, 588, 768]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[33]: text=肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。, bbox=[154, 779, 800, 795]
2026-08-10 11:07:30,946 INFO     29 [qwen-vl-text] coord item[34]: text=触诊:语音震颤两侧相等,无摩擦感。, bbox=[212, 806, 529, 822]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] coord item[35]: text=叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,, bbox=[212, 833, 772, 849]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] coord item[36]: text=听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、, bbox=[212, 859, 898, 875]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] coord item[37]: text=第页, bbox=[487, 906, 536, 920]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] coord item[38]: text=书写者签名:, bbox=[614, 906, 704, 920]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] coord item[39]: text=总第页, bbox=[844, 906, 911, 920]
2026-08-10 11:07:30,947 INFO     29 [qwen-vl-text] page=6 — 40/40 coords, api_time=14.0s
2026-08-10 11:07:30,951 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1167410, prompt_len=1429
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共44行）
["院", "入院记录", "姓名：", "科室：产科二区", "床号", "病号：", "干啰音、湿啰音。", "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "区无异常搏动、局限性膨隆。", "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "震颤、摩擦感。", "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "右cm", "肋间", "左cm", "2", "Ⅱ", "2.5", "2", "Ⅲ", "4", "3", "Ⅳ", "5.5", "V", "8", "左锁骨中线至前正中线的距离9cm。", "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "裂，P2<A2。", "血管：桡动脉搏动正常，血管壁硬度正常。", "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "腹部：", "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "起，下腹可见一长约15cm横行手术疤痕。", "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "鼓音，移动性浊音阴性。", "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "管杂音。", "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "肛、湿疣等。", "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎"]

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
2026-08-10 11:07:46,419 INFO     29 [qwen-vl-text] coord API raw response (len=2621):
[
	{"text": "院", "bbox": [579, 63, 625, 84]},
	{"text": "入院记录", "bbox": [442, 100, 586, 119]},
	{"text": "姓名：", "bbox": [115, 130, 164, 145]},
	{"text": "科室：产科二区", "bbox": [309, 130, 448, 145]},
	{"text": "床号", "bbox": [520, 130, 556, 145]},
	{"text": "病号：", "bbox": [718, 130, 765, 145]},
	{"text": "干啰音、湿啰音。", "bbox": [107, 154, 254, 170]},
	{"text": "心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前", "bbox": [148, 180, 915, 196]},
	{"text": "区无异常搏动、局限性膨隆。", "bbox": [107, 207, 353, 223]},
	{"text": "触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、", "bbox": [205, 237, 905, 253]},
	{"text": "震颤、摩擦感。", "bbox": [107, 264, 234, 280]},
	{"text": "叩诊：左右心界线以每肋间距胸骨中线的cm数记载。", "bbox": [205, 291, 648, 307]},
	{"text": "右cm", "bbox": [188, 317, 230, 331]},
	{"text": "肋间", "bbox": [418, 317, 459, 331]},
	{"text": "左cm", "bbox": [653, 317, 695, 331]},
	{"text": "2", "bbox": [202, 337, 214, 350]},
	{"text": "Ⅱ", "bbox": [431, 337, 447, 350]},
	{"text": "2.5", "bbox": [657, 337, 689, 350]},
	{"text": "2", "bbox": [202, 356, 214, 369]},
	{"text": "Ⅲ", "bbox": [428, 356, 451, 369]},
	{"text": "4", "bbox": [667, 356, 678, 369]},
	{"text": "3", "bbox": [202, 375, 214, 388]},
	{"text": "Ⅳ", "bbox": [430, 375, 451, 388]},
	{"text": "5.5", "bbox": [657, 375, 689, 388]},
	{"text": "V", "bbox": [431, 393, 447, 406]},
	{"text": "8", "bbox": [667, 393, 678, 406]},
	{"text": "左锁骨中线至前正中线的距离9cm。", "bbox": [156, 414, 451, 429]},
	{"text": "听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分", "bbox": [205, 443, 888, 459]},
	{"text": "裂，P2<A2。", "bbox": [107, 470, 204, 485]},
	{"text": "血管：桡动脉搏动正常，血管壁硬度正常。", "bbox": [147, 497, 509, 513]},
	{"text": "周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。", "bbox": [147, 525, 726, 541]},
	{"text": "腹部：", "bbox": [147, 552, 193, 568]},
	{"text": "视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆", "bbox": [147, 579, 897, 595]},
	{"text": "起，下腹可见一长约15cm横行手术疤痕。", "bbox": [107, 607, 451, 623]},
	{"text": "触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未", "bbox": [147, 634, 915, 650]},
	{"text": "触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。", "bbox": [107, 662, 865, 678]},
	{"text": "叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度", "bbox": [147, 689, 906, 705]},
	{"text": "鼓音，移动性浊音阴性。", "bbox": [107, 717, 312, 733]},
	{"text": "听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血", "bbox": [147, 744, 915, 760]},
	{"text": "管杂音。", "bbox": [107, 772, 174, 788]},
	{"text": "外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱", "bbox": [147, 799, 896, 815]},
	{"text": "肛、湿疣等。", "bbox": [107, 827, 214, 843]},
	{"text": "脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。", "bbox": [147, 854, 902, 870]},
	{"text": "四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎", "bbox": [147, 881, 902, 897]}
]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord API: raw_items=44, valid_items=44, elapsed=15.5s
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[579, 63, 625, 84]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[442, 100, 586, 119]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[115, 130, 164, 145]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[3]: text=科室：产科二区, bbox=[309, 130, 448, 145]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[4]: text=床号, bbox=[520, 130, 556, 145]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[5]: text=病号：, bbox=[718, 130, 765, 145]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[6]: text=干啰音、湿啰音。, bbox=[107, 154, 254, 170]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[7]: text=心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前, bbox=[148, 180, 915, 196]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[8]: text=区无异常搏动、局限性膨隆。, bbox=[107, 207, 353, 223]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[9]: text=触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、, bbox=[205, 237, 905, 253]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[10]: text=震颤、摩擦感。, bbox=[107, 264, 234, 280]
2026-08-10 11:07:46,420 INFO     29 [qwen-vl-text] coord item[11]: text=叩诊：左右心界线以每肋间距胸骨中线的cm数记载。, bbox=[205, 291, 648, 307]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[12]: text=右cm, bbox=[188, 317, 230, 331]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[13]: text=肋间, bbox=[418, 317, 459, 331]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[14]: text=左cm, bbox=[653, 317, 695, 331]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[15]: text=2, bbox=[202, 337, 214, 350]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[16]: text=Ⅱ, bbox=[431, 337, 447, 350]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[17]: text=2.5, bbox=[657, 337, 689, 350]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[18]: text=2, bbox=[202, 356, 214, 369]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[19]: text=Ⅲ, bbox=[428, 356, 451, 369]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[20]: text=4, bbox=[667, 356, 678, 369]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[21]: text=3, bbox=[202, 375, 214, 388]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[22]: text=Ⅳ, bbox=[430, 375, 451, 388]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[23]: text=5.5, bbox=[657, 375, 689, 388]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[24]: text=V, bbox=[431, 393, 447, 406]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[25]: text=8, bbox=[667, 393, 678, 406]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[26]: text=左锁骨中线至前正中线的距离9cm。, bbox=[156, 414, 451, 429]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[27]: text=听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分, bbox=[205, 443, 888, 459]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[28]: text=裂，P2<A2。, bbox=[107, 470, 204, 485]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[29]: text=血管：桡动脉搏动正常，血管壁硬度正常。, bbox=[147, 497, 509, 513]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[30]: text=周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。, bbox=[147, 525, 726, 541]
2026-08-10 11:07:46,421 INFO     29 [qwen-vl-text] coord item[31]: text=腹部：, bbox=[147, 552, 193, 568]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[32]: text=视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆, bbox=[147, 579, 897, 595]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[33]: text=起，下腹可见一长约15cm横行手术疤痕。, bbox=[107, 607, 451, 623]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[34]: text=触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未, bbox=[147, 634, 915, 650]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[35]: text=触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。, bbox=[107, 662, 865, 678]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[36]: text=叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度, bbox=[147, 689, 906, 705]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[37]: text=鼓音，移动性浊音阴性。, bbox=[107, 717, 312, 733]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[38]: text=听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血, bbox=[147, 744, 915, 760]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[39]: text=管杂音。, bbox=[107, 772, 174, 788]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[40]: text=外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱, bbox=[147, 799, 896, 815]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[41]: text=肛、湿疣等。, bbox=[107, 827, 214, 843]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[42]: text=脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。, bbox=[147, 854, 902, 870]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] coord item[43]: text=四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎, bbox=[147, 881, 902, 897]
2026-08-10 11:07:46,422 INFO     29 [qwen-vl-text] page=7 — 44/44 coords, api_time=15.5s
2026-08-10 11:07:46,424 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=596812, prompt_len=1012
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["院", "入院记录", "姓名.", "科室:产科二区", "床号", "住院号.", "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "专科情况", "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "辅助检查", "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "数8.5cm),胎盘成熟度II°.", "初步诊断:", "1.妊娠合并子宫瘢痕;", "3.孕2产,宫内孕39周头位待产。", "主治医师:", "孙小丹", "副主任医师:", "彭琼玉", "2020.07.08"]

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
2026-08-10 11:07:55,589 INFO     29 [qwen-vl-text] coord API raw response (len=1343):
[
	{"text": "院", "bbox": [569, 62, 629, 84]},
	{"text": "入院记录", "bbox": [440, 101, 588, 120]},
	{"text": "姓名.", "bbox": [111, 131, 158, 147]},
	{"text": "科室:产科二区", "bbox": [307, 131, 448, 147]},
	{"text": "床号", "bbox": [520, 131, 560, 147]},
	{"text": "住院号.", "bbox": [703, 131, 770, 147]},
	{"text": "缩;关节无红肿、畸形、运动障碍,双下肢水肿。", "bbox": [100, 155, 520, 172]},
	{"text": "神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、", "bbox": [141, 183, 912, 200]},
	{"text": "腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。", "bbox": [100, 210, 550, 227]},
	{"text": "专科情况", "bbox": [462, 245, 558, 263]},
	{"text": "宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无", "bbox": [158, 277, 925, 294]},
	{"text": "宫缩,未见红,未破水,骨盆外测量及内诊:未做。", "bbox": [102, 305, 550, 322]},
	{"text": "辅助检查", "bbox": [469, 334, 550, 350]},
	{"text": "B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指", "bbox": [141, 362, 925, 379]},
	{"text": "数8.5cm),胎盘成熟度II°.", "bbox": [102, 389, 352, 406]},
	{"text": "初步诊断:", "bbox": [407, 417, 496, 434]},
	{"text": "1.妊娠合并子宫瘢痕;", "bbox": [541, 445, 728, 462]},
	{"text": "3.孕2产,宫内孕39周头位待产。", "bbox": [541, 472, 845, 489]},
	{"text": "主治医师:", "bbox": [669, 526, 756, 542]},
	{"text": "孙小丹", "bbox": [776, 507, 860, 534]},
	{"text": "副主任医师:", "bbox": [649, 582, 756, 598]},
	{"text": "彭琼玉", "bbox": [772, 562, 864, 596]},
	{"text": "2020.07.08", "bbox": [702, 610, 804, 624]}
]
2026-08-10 11:07:55,589 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.2s
2026-08-10 11:07:55,589 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[569, 62, 629, 84]
2026-08-10 11:07:55,589 INFO     29 [qwen-vl-text] coord item[1]: text=入院记录, bbox=[440, 101, 588, 120]
2026-08-10 11:07:55,589 INFO     29 [qwen-vl-text] coord item[2]: text=姓名., bbox=[111, 131, 158, 147]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[3]: text=科室:产科二区, bbox=[307, 131, 448, 147]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[4]: text=床号, bbox=[520, 131, 560, 147]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[5]: text=住院号., bbox=[703, 131, 770, 147]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[6]: text=缩;关节无红肿、畸形、运动障碍,双下肢水肿。, bbox=[100, 155, 520, 172]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[7]: text=神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、, bbox=[141, 183, 912, 200]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[8]: text=腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。, bbox=[100, 210, 550, 227]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[9]: text=专科情况, bbox=[462, 245, 558, 263]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[10]: text=宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无, bbox=[158, 277, 925, 294]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[11]: text=宫缩,未见红,未破水,骨盆外测量及内诊:未做。, bbox=[102, 305, 550, 322]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[12]: text=辅助检查, bbox=[469, 334, 550, 350]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[13]: text=B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指, bbox=[141, 362, 925, 379]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[14]: text=数8.5cm),胎盘成熟度II°., bbox=[102, 389, 352, 406]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[15]: text=初步诊断:, bbox=[407, 417, 496, 434]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[16]: text=1.妊娠合并子宫瘢痕;, bbox=[541, 445, 728, 462]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[17]: text=3.孕2产,宫内孕39周头位待产。, bbox=[541, 472, 845, 489]
2026-08-10 11:07:55,590 INFO     29 [qwen-vl-text] coord item[18]: text=主治医师:, bbox=[669, 526, 756, 542]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] coord item[19]: text=孙小丹, bbox=[776, 507, 860, 534]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] coord item[20]: text=副主任医师:, bbox=[649, 582, 756, 598]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] coord item[21]: text=彭琼玉, bbox=[772, 562, 864, 596]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] coord item[22]: text=2020.07.08, bbox=[702, 610, 804, 624]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] page=8 — 23/23 coords, api_time=9.2s
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] new_positions (156):
[[5, 349.265, 368.305, 47.994, 64.834], [5, 264.775, 345.09999999999997, 78.306, 93.462], [5, 82.705, 128.51999999999998, 101.03999999999999, 114.512], [5, 190.39999999999998, 268.94, 101.03999999999999, 114.512], [5, 308.805, 334.39, 101.03999999999999, 114.512], [5, 82.705, 160.65, 121.24799999999999, 133.878], [5, 231.45499999999998, 314.755, 121.24799999999999, 133.878], [5, 355.215, 412.335, 121.24799999999999, 133.878], [5, 82.705, 109.47999999999999, 143.14, 155.76999999999998], [5, 187.42499999999998, 232.64499999999998, 143.14, 155.76999999999998], [5, 265.37, 320.11, 143.14, 155.76999999999998], [5, 348.075, 390.32, 143.14, 155.76999999999998], [5, 82.705, 109.47999999999999, 164.19, 176.82], [5, 187.42499999999998, 243.95, 164.19, 176.82], [5, 265.37, 321.3, 164.19, 176.82], [5, 348.075, 384.965, 164.19, 176.82], [5, 82.705, 137.445, 186.924, 200.396], [5, 327.25, 486.71, 186.924, 200.396], [5, 82.705, 105.315, 208.816, 222.28799999999998], [5, 321.895, 503.37, 208.816, 222.28799999999998], [5, 82.705, 120.19, 230.708, 244.17999999999998], [5, 264.775, 352.24, 230.708, 244.17999999999998], [5, 396.865, 484.33, 230.708, 244.17999999999998], [5, 82.705, 195.16, 253.44199999999998, 266.914], [5, 264.775, 290.955, 253.44199999999998, 266.914], [5, 396.865, 474.215, 253.44199999999998, 266.914], [5, 99.96, 261.8, 292.174, 305.646], [5, 77.945, 530.145, 313.224, 326.69599999999997], [5, 77.945, 530.145, 335.116, 348.58799999999997], [5, 77.945, 530.145, 357.008, 370.47999999999996], [5, 77.945, 530.145, 378.9, 392.372], [5, 77.945, 530.145, 400.792, 414.264], [5, 77.945, 530.145, 422.68399999999997, 436.156], [5, 77.945, 530.145, 444.57599999999996, 458.048], [5, 77.945, 458.15, 467.31, 480.782], [5, 101.14999999999999, 530.145, 489.202, 502.674], [5, 82.705, 524.79, 511.094, 524.566], [5, 77.945, 382.585, 533.828, 547.3], [5, 102.33999999999999, 531.3349999999999, 555.72, 569.192], [5, 77.945, 426.02, 578.454, 591.9259999999999], [5, 100.55499999999999, 224.91, 601.188, 614.66], [5, 256.445, 531.3349999999999, 601.188, 614.66], [5, 77.945, 521.22, 623.0799999999999, 636.552], [5, 77.945, 371.28, 645.814, 659.286], [5, 106.505, 531.93, 667.706, 681.178], [5, 77.945, 295.12, 690.4399999999999, 703.9119999999999], [5, 292.145, 320.11, 746.8539999999999, 758.6419999999999], [5, 364.73499999999996, 416.5, 746.8539999999999, 758.6419999999999], [5, 495.635, 533.715, 745.17, 757.8], [6, 343.315, 371.28, 50.519999999999996, 68.202], [6, 262.99, 347.47999999999996, 81.67399999999999, 97.672], [6, 74.375, 101.14999999999999, 106.092, 118.722], [6, 186.23499999999999, 267.75, 106.092, 118.722], [6, 308.805, 335.58, 106.092, 118.722], [6, 415.31, 453.39, 106.092, 118.722], [6, 91.63, 528.9549999999999, 125.458, 138.93], [6, 276.08, 331.41499999999996, 151.56, 165.874], [6, 91.63, 160.055, 178.504, 191.134], [6, 183.855, 258.825, 178.504, 191.134], [6, 285.59999999999997, 360.57, 178.504, 191.134], [6, 396.865, 483.14, 178.504, 191.976], [6, 91.63, 149.345, 202.07999999999998, 214.70999999999998], [6, 183.855, 242.165, 202.07999999999998, 216.394], [6, 91.63, 540.855, 224.814, 238.286], [6, 67.83, 223.72, 246.706, 260.178], [6, 91.63, 540.855, 270.282, 283.75399999999996], [6, 67.83, 154.105, 293.01599999999996, 306.488], [6, 91.63, 476.0, 315.75, 329.222], [6, 91.63, 117.80999999999999, 338.484, 351.95599999999996], [6, 91.63, 499.205, 361.21799999999996, 374.69], [6, 91.63, 533.715, 383.952, 397.424], [6, 67.83, 499.79999999999995, 406.686, 420.15799999999996], [6, 91.63, 424.23499999999996, 429.41999999999996, 442.892], [6, 91.63, 499.205, 451.312, 464.784], [6, 91.63, 540.855, 474.046, 487.518], [6, 67.83, 529.55, 496.78, 510.252], [6, 67.83, 247.51999999999998, 519.514, 532.986], [6, 91.63, 529.55, 542.2479999999999, 555.72], [6, 67.83, 165.41, 564.982, 578.454], [6, 91.63, 114.835, 587.716, 601.188], [6, 91.63, 540.855, 610.4499999999999, 623.922], [6, 67.83, 349.85999999999996, 633.184, 646.656], [6, 91.63, 476.0, 655.918, 669.39], [6, 126.14, 314.755, 678.6519999999999, 692.124], [6, 126.14, 459.34, 701.386, 714.858], [6, 126.14, 534.31, 723.278, 736.75], [6, 289.765, 318.91999999999996, 762.852, 774.64], [6, 365.33, 418.88, 762.852, 774.64], [6, 502.17999999999995, 542.045, 762.852, 774.64], [7, 344.505, 371.875, 53.046, 70.728], [7, 262.99, 348.66999999999996, 84.2, 100.198], [7, 68.425, 97.58, 109.46, 122.08999999999999], [7, 183.855, 266.56, 109.46, 122.08999999999999], [7, 309.4, 330.82, 109.46, 122.08999999999999], [7, 427.21, 455.17499999999995, 109.46, 122.08999999999999], [7, 63.665, 151.13, 129.668, 143.14], [7, 88.06, 544.425, 151.56, 165.03199999999998], [7, 63.665, 210.035, 174.29399999999998, 187.766], [7, 121.975, 538.475, 199.554, 213.02599999999998], [7, 63.665, 139.23, 222.28799999999998, 235.76], [7, 121.975, 385.56, 245.022, 258.49399999999997], [7, 111.86, 136.85, 266.914, 278.702], [7, 248.70999999999998, 273.10499999999996, 266.914, 278.702], [7, 388.53499999999997, 413.525, 266.914, 278.702], [7, 120.19, 127.33, 283.75399999999996, 294.7], [7, 256.445, 265.965, 283.75399999999996, 294.7], [7, 390.91499999999996, 409.955, 283.75399999999996, 294.7], [7, 120.19, 127.33, 299.752, 310.698], [7, 254.66, 268.34499999999997, 299.752, 310.698], [7, 396.865, 403.40999999999997, 299.752, 310.698], [7, 120.19, 127.33, 315.75, 326.69599999999997], [7, 255.85, 268.34499999999997, 315.75, 326.69599999999997], [7, 390.91499999999996, 409.955, 315.75, 326.69599999999997], [7, 256.445, 265.965, 330.906, 341.852], [7, 396.865, 403.40999999999997, 330.906, 341.852], [7, 92.82, 268.34499999999997, 348.58799999999997, 361.21799999999996], [7, 121.975, 528.36, 373.006, 386.478], [7, 63.665, 121.38, 395.74, 408.37], [7, 87.46499999999999, 302.85499999999996, 418.474, 431.94599999999997], [7, 87.46499999999999, 431.96999999999997, 442.05, 455.522], [7, 87.46499999999999, 114.835, 464.784, 478.256], [7, 87.46499999999999, 533.715, 487.518, 500.99], [7, 63.665, 268.34499999999997, 511.094, 524.566], [7, 87.46499999999999, 544.425, 533.828, 547.3], [7, 63.665, 514.675, 557.404, 570.876], [7, 87.46499999999999, 539.0699999999999, 580.138, 593.61], [7, 63.665, 185.64, 603.7139999999999, 617.1859999999999], [7, 87.46499999999999, 544.425, 626.448, 639.92], [7, 63.665, 103.53, 650.024, 663.496], [7, 87.46499999999999, 533.12, 672.7579999999999, 686.23], [7, 63.665, 127.33, 696.334, 709.8059999999999], [7, 87.46499999999999, 536.6899999999999, 719.068, 732.54], [7, 87.46499999999999, 536.6899999999999, 741.802, 755.274], [8, 338.555, 374.255, 52.204, 70.728], [8, 261.8, 349.85999999999996, 85.042, 101.03999999999999], [8, 66.045, 94.00999999999999, 110.30199999999999, 123.774], [8, 182.665, 266.56, 110.30199999999999, 123.774], [8, 309.4, 333.2, 110.30199999999999, 123.774], [8, 418.28499999999997, 458.15, 110.30199999999999, 123.774], [8, 59.5, 309.4, 130.51, 144.82399999999998], [8, 83.895, 542.64, 154.08599999999998, 168.4], [8, 59.5, 327.25, 176.82, 191.134], [8, 274.89, 332.01, 206.29, 221.446], [8, 94.00999999999999, 550.375, 233.23399999999998, 247.548], [8, 60.69, 327.25, 256.81, 271.12399999999997], [8, 279.055, 327.25, 281.228, 294.7], [8, 83.895, 550.375, 304.804, 319.118], [8, 60.69, 209.44, 327.538, 341.852], [8, 242.165, 295.12, 351.114, 365.428], [8, 321.895, 433.15999999999997, 374.69, 389.00399999999996], [8, 321.895, 502.775, 397.424, 411.738], [8, 398.055, 449.82, 442.892, 456.364], [8, 461.71999999999997, 511.7, 426.894, 449.628], [8, 386.155, 449.82, 490.044, 503.51599999999996], [8, 459.34, 514.0799999999999, 473.204, 501.832], [8, 417.69, 478.38, 513.62, 525.408]]
2026-08-10 11:07:55,591 INFO     29 [qwen-vl-text] ═══ DONE ═══ 156 positions, pages=4, time=80.7s
2026-08-10 11:07:55,606 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:07:55,606 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Extractor:Admission | outputs={"chunks": "1 items, types={'AdmissionRecord': 1}", "html": "", "json": "2326 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Progress": "7 items, types={'ProgressNote': 7}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "5 items, types={'PrescriptionRecord': 5}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Progress\": 7, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 5, \"chunks_LabExam\": 13}"}
2026-08-10 11:07:55,606 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:07:55,608 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:07:55.607+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:07:55,618 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:07:55,620 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:07:55,620 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:07:55,620 INFO     29 [qwen-vl-text] positions(70): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:07:55,620 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [70]
2026-08-10 11:07:55,828 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:07:55,829 INFO     29 [qwen-vl-text] LLM extraction start, text_len=768
2026-08-10 11:07:55,829 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:07:55,830 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 69, \"encounter_dates\": [\"2026-01-29\"], \"department\": \"普通儿科一区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "呼出气一氧化氮测定报告单\n病人信息：\n编号：482\n姓名：\n年龄：41岁9月27天\n性别：女\n科室：普通儿科一区\n出生日期：1984-04-02\n测定时间：2026/1/29 11:02:42\n测定信息：\n一小时内禁止饮食：■是\n一小时内禁止剧烈运动：■是\n三小时内禁止食用特殊食品*：■是\n一小时内禁止抽烟：■是\n三天内使用激素类药物：■是 □否\n三天内使用抗生素：□是 ■否\n症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n病史：□过敏史 □其它\n*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n测定项目：\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.1℃\n呼气压力：13.6cmH20\n呼气平均流速：48ml/s\n呼气NO浓度：\n32.7,31.0,32.0,31.8,32.1,31.7ppb\n呼气NO浓度均值:32ppb\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.3℃\n呼气压力：7.9cmH20\n呼气平均流速：207ml/s\n呼气NO浓度：\n11.7,11.9,11.3,11.6,11.6,11.6ppb\n呼气NO浓度均值:12ppb\n测定结果：\nFeNO50：32ppb\nFeNO200：12ppb\nCaNO：3.6ppb\n测定意义：\n测定浓度\n参考值\n炎症鉴别诊断\n>12岁\n≤12岁\nFeNO50\n<25ppb\n<20ppb*\n非嗜酸性气道炎症\n25-50ppb\n20-35ppb*\n混合型气道炎症\n≥50ppb\n≥35ppb*\n嗜酸性气道炎症\nFeNO200\n>10ppb\n>8ppb\n小气道炎症\nCaNO\n>5ppb\n>3ppb\n肺泡炎症\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)\n复查时间：\n操作员：赵彩红\n医生：马春英\n电\n告\n单\n更",
    "role": "user"
  }
]
2026-08-10 11:07:55,835 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:07:55,835 INFO     29 [qwen-vl-table] page=13 LLM output (len=5506):
{
  "report_date": null,
  "items": [
    {
      "name": "白细胞",
      "item_code": "WBC",
      "value": "9.17",
      "unit": "10^9/L",
      "reference_range": "3.5 -- 9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞总数",
      "item_code": "NEU",
      "value": "5.71",
      "unit": "10^9/L",
      "reference_range": "1.8 -- 6.3",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分数",
      "item_code": "NEUN",
      "value": "62.30",
      "unit": "%",
      "reference_range": "40 -- 75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞总数",
      "item_code": "LY",
      "value": "2.62",
      "unit": "10^9/L",
      "reference_range": "1.1 -- 3.2",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分数",
      "item_code": "LYN",
      "value": "28.60",
      "unit": "%",
      "reference_range": "20 -- 50",
      "abnormal": false
    },
    {
      "name": "单核细胞总数",
      "item_code": "MONO",
      "value": "0.47",
      "unit": "10^9/L",
      "reference_range": "0.1 -- 0.6",
      "abnormal": false
    },
    {
      "name": "单核细胞百分数",
      "item_code": "MON%",
      "value": "5.10",
      "unit": "%",
      "reference_range": "3 -- 10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞总数",
      "item_code": "EOS",
      "value": "0.34",
      "unit": "10^9/L",
      "reference_range": "0.02 -- 0.52",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分数",
      "item_code": "EOS%",
      "value": "3.70",
      "unit": "%",
      "reference_range": "0.4 -- 8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞总数",
      "item_code": "BASO",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0 -- 0.06",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分比",
      "item_code": "BASO%",
      "value": "0.30",
      "unit": "%",
      "reference_range": "0 -- 1",
      "abnormal": false
    },
    {
      "name": "红细胞",
      "item_code": "RBC",
      "value": "4.91",
      "unit": "10^12/L",
      "reference_range": "4.3 -- 5.8",
      "abnormal": false
    },
    {
      "name": "血红蛋白",
      "item_code": "HGB",
      "value": "158",
      "unit": "g/L",
      "reference_range": "130 -- 175",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "47.10",
      "unit": "%",
      "reference_range": "40 -- 50",
      "abnormal": false
    },
    {
      "name": "红细胞平均容积",
      "item_code": "MCV",
      "value": "96.90",
      "unit": "fl",
      "reference_range": "82 -- 100",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白",
      "item_code": "MCH",
      "value": "32.20",
      "unit": "pg",
      "reference_range": "27 -- 34",
      "abnormal": false
    },
    {
      "name": "红细胞平均血红蛋白浓度",
      "item_code": "MCHC",
      "value": "335.00",
      "unit": "g/L",
      "reference_range": "316 -- 354",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度",
      "item_code": "RDW",
      "value": "12.40",
      "unit": "%",
      "reference_range": "11.6 -- 14.8",
      "abnormal": false
    },
    {
      "name": "红细胞分布宽度-SD",
      "item_code": "RDW-SD",
      "value": "44.10",
      "unit": "fl",
      "reference_range": "37.1 -- 49.2",
      "abnormal": false
    },
    {
      "name": "血小板",
      "item_code": "PLT",
      "value": "197",
      "unit": "10^9/L",
      "reference_range": "125 -- 350",
      "abnormal": false
    },
    {
      "name": "平均血小板容积",
      "item_code": "MPV",
      "value": "10.70",
      "unit": "fl",
      "reference_range": "6 -- 12",
      "abnormal": false
    },
    {
      "name": "平均血小板比容",
      "item_code": "Pct",
      "value": "0.21",
      "unit": "%",
      "reference_range": "0.10 -- 0.29",
      "abnormal": false
    },
    {
      "name": "血小板分布宽度",
      "item_code": "PDW",
      "value": "13.00",
      "unit": "10(GSP)",
      "reference_range": "15.3 -- 20.5",
      "abnormal": true
    },
    {
      "name": "大血小板",
      "item_code": "P-LCR",
      "value": "30.90",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "网织红细胞绝对值",
      "item_code": "RETR",
      "value": "90.5",
      "unit": "10^9/L",
      "reference_range": "46.4 -- 121.2",
      "abnormal": false
    },
    {
      "name": "网织红细胞百分数",
      "item_code": "RETR",
      "value": "1.64",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "低荧光强度网织红细胞比率",
      "item_code": "LFF",
      "value": "83.8",
      "unit": "%",
      "reference_range": "89.9 -- 98.4",
      "abnormal": true
    },
    {
      "name": "中荧光强度网织红细胞比率",
      "item_code": "MFF",
      "value": "13.3",
      "unit": "%",
      "reference_range": "1.6 -- 9.5",
      "abnormal": true
    },
    {
      "name": "高荧光强度网织红细胞比率",
      "item_code": "HFF",
      "value": "2.9",
      "unit": "%",
      "reference_range": "0 -- 1.7",
      "abnormal": true
    },
    {
      "name": "未成熟网织红细胞比率",
      "item_code": "IRF",
      "value": "16.2",
      "unit": "%",
      "reference_range": "1.6 -- 10.5",
      "abnormal": true
    },
    {
      "name": "有核红细胞计数",
      "item_code": "NRBCW",
      "value": "0",
      "unit": "10^9/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "有核红细胞百分比",
      "item_code": "NRBC%",
      "value": "0",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 11:07:55,835 INFO     29 [qwen-vl-table] coord grouping: {13: 32}
2026-08-10 11:07:55,837 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1446940, prompt_len=777
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞、中性粒细胞总数、中性粒细胞百分数、淋巴细胞总数、淋巴细胞百分数、单核细胞总数、单核细胞百分数、嗜酸性粒细胞总数、嗜酸性粒细胞百分数、嗜碱性粒细胞总数、嗜碱性粒细胞百分比、红细胞、血红蛋白、红细胞压积、红细胞平均容积、红细胞平均血红蛋白、红细胞平均血红蛋白浓度、红细胞分布宽度、红细胞分布宽度-SD、血小板、平均血小板容积、平均血小板比容、血小板分布宽度、大血小板、网织红细胞绝对值、网织红细胞百分数、低荧光强度网织红细胞比率、中荧光强度网织红细胞比率、高荧光强度网织红细胞比率、未成熟网织红细胞比率、有核红细胞计数、有核红细胞百分比

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
2026-08-10 11:08:07,282 INFO     29 [qwen-vl-table] coord API raw response (len=1681):
[
	{"text": "白细胞", "bbox": [238, 147, 307, 164]},
	{"text": "中性粒细胞总数", "bbox": [238, 170, 356, 187]},
	{"text": "中性粒细胞百分数", "bbox": [238, 193, 375, 210]},
	{"text": "淋巴细胞总数", "bbox": [238, 217, 338, 234]},
	{"text": "淋巴细胞百分数", "bbox": [238, 240, 356, 257]},
	{"text": "单核细胞总数", "bbox": [238, 263, 350, 280]},
	{"text": "单核细胞百分数", "bbox": [238, 287, 368, 304]},
	{"text": "嗜酸性粒细胞总数", "bbox": [238, 310, 369, 327]},
	{"text": "嗜酸性粒细胞百分数", "bbox": [238, 334, 387, 351]},
	{"text": "嗜碱性粒细胞总数", "bbox": [238, 357, 375, 374]},
	{"text": "嗜碱性粒细胞百分比", "bbox": [238, 380, 393, 397]},
	{"text": "红细胞", "bbox": [238, 404, 306, 421]},
	{"text": "血红蛋白", "bbox": [238, 427, 317, 444]},
	{"text": "红细胞压积", "bbox": [238, 450, 331, 467]},
	{"text": "红细胞平均容积", "bbox": [238, 474, 355, 491]},
	{"text": "红细胞平均血红蛋白", "bbox": [238, 497, 380, 514]},
	{"text": "红细胞平均血红蛋白浓度", "bbox": [238, 520, 413, 537]},
	{"text": "红细胞分布宽度", "bbox": [238, 543, 355, 560]},
	{"text": "红细胞分布宽度-SD", "bbox": [238, 567, 393, 584]},
	{"text": "血小板", "bbox": [238, 590, 306, 607]},
	{"text": "平均血小板容积", "bbox": [238, 613, 355, 630]},
	{"text": "平均血小板比容", "bbox": [238, 637, 355, 654]},
	{"text": "血小板分布宽度", "bbox": [238, 660, 355, 677]},
	{"text": "大血小板", "bbox": [238, 683, 330, 700]},
	{"text": "网织红细胞绝对值", "bbox": [238, 706, 375, 723]},
	{"text": "网织红细胞百分数", "bbox": [238, 729, 375, 746]},
	{"text": "低荧光强度网织红细胞比率", "bbox": [238, 753, 420, 770]},
	{"text": "中荧光强度网织红细胞比率", "bbox": [238, 776, 420, 793]},
	{"text": "高荧光强度网织红细胞比率", "bbox": [238, 799, 420, 816]},
	{"text": "未成熟网织红细胞比率", "bbox": [238, 822, 393, 839]},
	{"text": "有核红细胞计数", "bbox": [238, 846, 368, 863]},
	{"text": "有核红细胞百分比", "bbox": [238, 869, 380, 886]}
]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord API: raw_items=32, valid_items=32, elapsed=11.4s
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞, bbox=[238, 147, 307, 164]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞总数, bbox=[238, 170, 356, 187]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[2]: text=中性粒细胞百分数, bbox=[238, 193, 375, 210]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[3]: text=淋巴细胞总数, bbox=[238, 217, 338, 234]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[4]: text=淋巴细胞百分数, bbox=[238, 240, 356, 257]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[5]: text=单核细胞总数, bbox=[238, 263, 350, 280]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[6]: text=单核细胞百分数, bbox=[238, 287, 368, 304]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[7]: text=嗜酸性粒细胞总数, bbox=[238, 310, 369, 327]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[8]: text=嗜酸性粒细胞百分数, bbox=[238, 334, 387, 351]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[9]: text=嗜碱性粒细胞总数, bbox=[238, 357, 375, 374]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞百分比, bbox=[238, 380, 393, 397]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞, bbox=[238, 404, 306, 421]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白, bbox=[238, 427, 317, 444]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[238, 450, 331, 467]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[14]: text=红细胞平均容积, bbox=[238, 474, 355, 491]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[15]: text=红细胞平均血红蛋白, bbox=[238, 497, 380, 514]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[16]: text=红细胞平均血红蛋白浓度, bbox=[238, 520, 413, 537]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞分布宽度, bbox=[238, 543, 355, 560]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[18]: text=红细胞分布宽度-SD, bbox=[238, 567, 393, 584]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[19]: text=血小板, bbox=[238, 590, 306, 607]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板容积, bbox=[238, 613, 355, 630]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[21]: text=平均血小板比容, bbox=[238, 637, 355, 654]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[22]: text=血小板分布宽度, bbox=[238, 660, 355, 677]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[23]: text=大血小板, bbox=[238, 683, 330, 700]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[24]: text=网织红细胞绝对值, bbox=[238, 706, 375, 723]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[25]: text=网织红细胞百分数, bbox=[238, 729, 375, 746]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[26]: text=低荧光强度网织红细胞比率, bbox=[238, 753, 420, 770]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[27]: text=中荧光强度网织红细胞比率, bbox=[238, 776, 420, 793]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[28]: text=高荧光强度网织红细胞比率, bbox=[238, 799, 420, 816]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[29]: text=未成熟网织红细胞比率, bbox=[238, 822, 393, 839]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[30]: text=有核红细胞计数, bbox=[238, 846, 368, 863]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] coord item[31]: text=有核红细胞百分比, bbox=[238, 869, 380, 886]
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] page=13 coord: matched 32/32, time=11.4s
2026-08-10 11:08:07,283 INFO     29 [qwen-vl-table] new_positions (32):
[[14, 200.396, 258.49399999999997, 87.46499999999999, 97.58], [14, 200.396, 299.752, 101.14999999999999, 111.265], [14, 200.396, 315.75, 114.835, 124.94999999999999], [14, 200.396, 284.596, 129.11499999999998, 139.23], [14, 200.396, 299.752, 142.79999999999998, 152.915], [14, 200.396, 294.7, 156.48499999999999, 166.6], [14, 200.396, 309.856, 170.765, 180.88], [14, 200.396, 310.698, 184.45, 194.565], [14, 200.396, 325.854, 198.73, 208.845], [14, 200.396, 315.75, 212.415, 222.53], [14, 200.396, 330.906, 226.1, 236.215], [14, 200.396, 257.652, 240.38, 250.49499999999998], [14, 200.396, 266.914, 254.065, 264.18], [14, 200.396, 278.702, 267.75, 277.865], [14, 200.396, 298.90999999999997, 282.03, 292.145], [14, 200.396, 319.96, 295.715, 305.83], [14, 200.396, 347.746, 309.4, 319.515], [14, 200.396, 298.90999999999997, 323.085, 333.2], [14, 200.396, 330.906, 337.365, 347.47999999999996], [14, 200.396, 257.652, 351.05, 361.16499999999996], [14, 200.396, 298.90999999999997, 364.73499999999996, 374.84999999999997], [14, 200.396, 298.90999999999997, 379.015, 389.13], [14, 200.396, 298.90999999999997, 392.7, 402.815], [14, 200.396, 277.86, 406.385, 416.5], [14, 200.396, 315.75, 420.07, 430.185], [14, 200.396, 315.75, 433.755, 443.87], [14, 200.396, 353.64, 448.03499999999997, 458.15], [14, 200.396, 353.64, 461.71999999999997, 471.835], [14, 200.396, 353.64, 475.405, 485.52], [14, 200.396, 330.906, 489.09, 499.205], [14, 200.396, 309.856, 503.37, 513.485], [14, 200.396, 319.96, 517.055, 527.17]]
2026-08-10 11:08:07,284 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=32, matched=32, pages=1, time=72.7s
2026-08-10 11:08:07,830 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 11:08:07,830 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:08:07,830 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 11:08:07,838 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:07,839 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:08:08,348 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:08,356 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 11:08:08,356 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:08:08,356 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 11:08:08,362 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:08:08,362 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:08:08,362 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:08:08,362 INFO     29 [qwen-vl-text] positions(33): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:08:08,362 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [33]
2026-08-10 11:08:08,723 INFO     29 [qwen-vl-text] page=0, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:08:08,724 INFO     29 [qwen-vl-text] LLM extraction start, text_len=272
2026-08-10 11:08:08,724 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:08,724 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 0, \"bbox_end\": 32, \"encounter_dates\": [\"2025-10-21\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡\n流水\n病历编号:\n姓\n别:男\n年\n龄:64岁\n就诊科室:内科门诊(荔湾)\n医\n诊时间:2025-10-21 16:24:23\n主\n诉:取药\n现病史:\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n支气管哮喘\n单病种:\n发病时间:\n处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。\n1孟鲁司特钠片(省采)◆\n1瓶10.0mg,口服,每晚1次\n30天\n2倍氯米松福莫特罗吸入气雾剂◆①\n1瓶2.0揿,吸入用药,一天2次\n30天\n备注:建议在住地附近社区医疗机构随诊。",
    "role": "user"
  }
]
2026-08-10 11:08:10,956 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:10,956 INFO     29 [qwen-vl-text] LLM output (len=503):
{
  "encounter_date": "2025-10-21",
  "chief_complaint": "取药",
  "present_illness": null,
  "past_history": null,
  "diagnosis": "支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "孟鲁司特钠片(省采)",
      "dosage": "10.0mg",
      "frequency": "每晚1次",
      "route": "口服",
      "quantity": "1瓶",
      "duration": "30天"
    },
    {
      "drug_name": "倍氯米松福莫特罗吸入气雾剂",
      "dosage": "2.0揿",
      "frequency": "一天2次",
      "route": "吸入用药",
      "quantity": "1瓶",
      "duration": "30天"
    }
  ]
}
2026-08-10 11:08:10,956 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-10-21]
2026-08-10 11:08:10,963 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3647382, prompt_len=984
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊病历信息", "就诊卡", "流水", "病历编号:", "姓", "别:男", "年", "龄:64岁", "就诊科室:内科门诊(荔湾)", "医", "诊时间:2025-10-21 16:24:23", "主", "诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "支气管哮喘", "单病种:", "发病时间:", "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:建议在住地附近社区医疗机构随诊。"]

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
2026-08-10 11:08:23,092 INFO     29 [qwen-vl-text] coord API raw response (len=2374):
[
	{"text": "门(急)诊病历信息", "bbox": [372, 130, 590, 150]},
	{"text": "就诊卡", "bbox": [196, 184, 246, 200], "label": "就诊卡"},
	{"text": "流水", "bbox": [196, 216, 246, 233], "label": "流水"},
	{"text": "病历编号:", "bbox": [568, 216, 645, 232], "label": "病历编号:"},
	{"text": "姓", "bbox": [196, 249, 214, 265], "label": "姓"},
	{"text": "别:男", "bbox": [489, 249, 529, 265], "label": "别:男"},
	{"text": "年", "bbox": [568, 250, 586, 265], "label": "年"},
	{"text": "龄:64岁", "bbox": [654, 250, 714, 265], "label": "龄:64岁"},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [196, 280, 404, 297], "label": "就诊科室:内科门诊(荔湾)"},
	{"text": "医", "bbox": [468, 280, 490, 297], "label": "医"},
	{"text": "诊时间:2025-10-21 16:24:23", "bbox": [578, 280, 816, 297], "label": "诊时间:2025-10-21 16:24:23"},
	{"text": "主", "bbox": [196, 312, 214, 328], "label": "主"},
	{"text": "诉:取药", "bbox": [288, 312, 362, 328], "label": "诉:取药"},
	{"text": "现病史:", "bbox": [196, 343, 299, 359], "label": "现病史:"},
	{"text": "既往史:", "bbox": [196, 373, 299, 389], "label": "既往史:"},
	{"text": "过敏史:", "bbox": [196, 403, 299, 419], "label": "过敏史:"},
	{"text": "个人史:", "bbox": [196, 433, 300, 449], "label": "个人史:"},
	{"text": "体格检查:", "bbox": [199, 463, 283, 478], "label": "体格检查:"},
	{"text": "专科情况:", "bbox": [200, 491, 283, 506], "label": "专科情况:"},
	{"text": "辅助检查:", "bbox": [200, 519, 283, 534], "label": "辅助检查:"},
	{"text": "治疗项目:", "bbox": [200, 547, 283, 562], "label": "治疗项目:"},
	{"text": "门诊诊断:", "bbox": [202, 575, 283, 590], "label": "门诊诊断:"},
	{"text": "支气管哮喘", "bbox": [312, 603, 394, 617], "label": "支气管哮喘"},
	{"text": "单病种:", "bbox": [202, 630, 300, 645], "label": "单病种:"},
	{"text": "发病时间:", "bbox": [202, 659, 283, 673], "label": "发病时间:"},
	{"text": "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。", "bbox": [291, 686, 735, 700], "label": "处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。"},
	{"text": "1孟鲁司特钠片(省采)◆", "bbox": [226, 713, 393, 727], "label": "1孟鲁司特钠片(省采)◆"},
	{"text": "1瓶10.0mg,口服,每晚1次", "bbox": [528, 713, 708, 727], "label": "1瓶10.0mg,口服,每晚1次"},
	{"text": "30天", "bbox": [738, 713, 770, 726], "label": "30天"},
	{"text": "2倍氯米松福莫特罗吸入气雾剂◆①", "bbox": [226, 739, 474, 753], "label": "2倍氯米松福莫特罗吸入气雾剂◆①"},
	{"text": "1瓶2.0揿,吸入用药,一天2次", "bbox": [527, 739, 730, 753], "label": "1瓶2.0揿,吸入用药,一天2次"},
	{"text": "30天", "bbox": [759, 740, 791, 752], "label": "30天"},
	{"text": "备注:建议在住地附近社区医疗机构随诊。", "bbox": [291, 766, 573, 780], "label": "备注:建议在住地附近社区医疗机构随诊。"}
]
2026-08-10 11:08:23,092 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=12.1s
2026-08-10 11:08:23,092 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[372, 130, 590, 150]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡, bbox=[196, 184, 246, 200]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[2]: text=流水, bbox=[196, 216, 246, 233]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[3]: text=病历编号:, bbox=[568, 216, 645, 232]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[4]: text=姓, bbox=[196, 249, 214, 265]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[5]: text=别:男, bbox=[489, 249, 529, 265]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[6]: text=年, bbox=[568, 250, 586, 265]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[7]: text=龄:64岁, bbox=[654, 250, 714, 265]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[8]: text=就诊科室:内科门诊(荔湾), bbox=[196, 280, 404, 297]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[9]: text=医, bbox=[468, 280, 490, 297]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[10]: text=诊时间:2025-10-21 16:24:23, bbox=[578, 280, 816, 297]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[11]: text=主, bbox=[196, 312, 214, 328]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[12]: text=诉:取药, bbox=[288, 312, 362, 328]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[13]: text=现病史:, bbox=[196, 343, 299, 359]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[14]: text=既往史:, bbox=[196, 373, 299, 389]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[15]: text=过敏史:, bbox=[196, 403, 299, 419]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[16]: text=个人史:, bbox=[196, 433, 300, 449]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[17]: text=体格检查:, bbox=[199, 463, 283, 478]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[18]: text=专科情况:, bbox=[200, 491, 283, 506]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[19]: text=辅助检查:, bbox=[200, 519, 283, 534]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[20]: text=治疗项目:, bbox=[200, 547, 283, 562]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[21]: text=门诊诊断:, bbox=[202, 575, 283, 590]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[22]: text=支气管哮喘, bbox=[312, 603, 394, 617]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[23]: text=单病种:, bbox=[202, 630, 300, 645]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[24]: text=发病时间:, bbox=[202, 659, 283, 673]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[25]: text=处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。, bbox=[291, 686, 735, 700]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[26]: text=1孟鲁司特钠片(省采)◆, bbox=[226, 713, 393, 727]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[27]: text=1瓶10.0mg,口服,每晚1次, bbox=[528, 713, 708, 727]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[28]: text=30天, bbox=[738, 713, 770, 726]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[29]: text=2倍氯米松福莫特罗吸入气雾剂◆①, bbox=[226, 739, 474, 753]
2026-08-10 11:08:23,093 INFO     29 [qwen-vl-text] coord item[30]: text=1瓶2.0揿,吸入用药,一天2次, bbox=[527, 739, 730, 753]
2026-08-10 11:08:23,094 INFO     29 [qwen-vl-text] coord item[31]: text=30天, bbox=[759, 740, 791, 752]
2026-08-10 11:08:23,094 INFO     29 [qwen-vl-text] coord item[32]: text=备注:建议在住地附近社区医疗机构随诊。, bbox=[291, 766, 573, 780]
2026-08-10 11:08:23,094 INFO     29 [qwen-vl-text] page=0 — 33/33 coords, api_time=12.1s
2026-08-10 11:08:23,095 INFO     29 [qwen-vl-text] new_positions (33):
[[0, 221.34, 351.05, 109.46, 126.3], [0, 116.61999999999999, 146.37, 154.928, 168.4], [0, 116.61999999999999, 146.37, 181.87199999999999, 196.186], [0, 337.96, 383.775, 181.87199999999999, 195.344], [0, 116.61999999999999, 127.33, 209.658, 223.13], [0, 290.955, 314.755, 209.658, 223.13], [0, 337.96, 348.66999999999996, 210.5, 223.13], [0, 389.13, 424.83, 210.5, 223.13], [0, 116.61999999999999, 240.38, 235.76, 250.07399999999998], [0, 278.46, 291.55, 235.76, 250.07399999999998], [0, 343.90999999999997, 485.52, 235.76, 250.07399999999998], [0, 116.61999999999999, 127.33, 262.704, 276.176], [0, 171.35999999999999, 215.39, 262.704, 276.176], [0, 116.61999999999999, 177.905, 288.806, 302.27799999999996], [0, 116.61999999999999, 177.905, 314.066, 327.538], [0, 116.61999999999999, 177.905, 339.32599999999996, 352.798], [0, 116.61999999999999, 178.5, 364.586, 378.058], [0, 118.405, 168.385, 389.846, 402.476], [0, 119.0, 168.385, 413.42199999999997, 426.05199999999996], [0, 119.0, 168.385, 436.998, 449.628], [0, 119.0, 168.385, 460.574, 473.204], [0, 120.19, 168.385, 484.15, 496.78], [0, 185.64, 234.42999999999998, 507.726, 519.514], [0, 120.19, 178.5, 530.46, 543.09], [0, 120.19, 168.385, 554.8779999999999, 566.6659999999999], [0, 173.14499999999998, 437.325, 577.612, 589.4], [0, 134.47, 233.83499999999998, 600.346, 612.134], [0, 314.15999999999997, 421.26, 600.346, 612.134], [0, 439.10999999999996, 458.15, 600.346, 611.292], [0, 134.47, 282.03, 622.2379999999999, 634.026], [0, 313.565, 434.34999999999997, 622.2379999999999, 634.026], [0, 451.60499999999996, 470.645, 623.0799999999999, 633.184], [0, 173.14499999999998, 340.935, 644.972, 656.76]]
2026-08-10 11:08:23,095 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=14.7s
2026-08-10 11:08:23,095 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:08:23,096 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:08:23,096 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:08:23,096 INFO     29 [qwen-vl-text] positions(29): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:08:23,096 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [29]
2026-08-10 11:08:23,393 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:08:23,395 INFO     29 [qwen-vl-text] LLM extraction start, text_len=226
2026-08-10 11:08:23,395 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:23,395 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 41, \"bbox_end\": 69, \"encounter_dates\": [\"2025-11-19\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡号:\n流水号:\n病历编号:\n性别:男\n年\n龄:65岁\n就诊科室:内科门诊(荔湾)\n医生:\n就诊时间:2025-11-19 11:33:52\n主诉:取药\n现病史:\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘\n处置:\n1孟鲁司特钠片(省采)◆\n1瓶10.0mg,口服,每晚1次\n30天\n2倍氯米松福莫特罗吸入气雾剂◆①\n1瓶2.0揿,吸入用药,一天2次\n30天\n备注:",
    "role": "user"
  }
]
2026-08-10 11:08:23,401 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:23,401 INFO     29 [qwen-vl-text] LLM output (len=1104):
{
  "exam_date": "2026-01-29",
  "report_date": "2026-01-29",
  "exam_name": "呼出气一氧化氮测定",
  "exam_category": "other",
  "body_part": "呼出气",
  "patient_name": null,
  "patient_gender": "女",
  "department": "普通儿科一区",
  "bed_number": null,
  "findings": "测定信息：\n一小时内禁止饮食：■是\n一小时内禁止剧烈运动：■是\n三小时内禁止食用特殊食品*：■是\n一小时内禁止抽烟：■是\n三天内使用激素类药物：■是 □否\n三天内使用抗生素：□是 ■否\n症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他\n病史：□过敏史 □其它\n*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。\n测定项目：\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.1℃\n呼气压力：13.6cmH20\n呼气平均流速：48ml/s\n呼气NO浓度：\n32.7,31.0,32.0,31.8,32.1,31.7ppb\n呼气NO浓度均值:32ppb\n呼气方式：■在线 □离线 □潮气\n呼气温度：20.3℃\n呼气压力：7.9cmH20\n呼气平均流速：207ml/s\n呼气NO浓度：\n11.7,11.9,11.3,11.6,11.6,11.6ppb\n呼气NO浓度均值:12ppb",
  "conclusion": "测定结果：\nFeNO50：32ppb\nFeNO200：12ppb\nCaNO：3.6ppb\n测定意义：\n| 测定浓度 | 参考值 >12岁 | 参考值 ≤12岁 | 炎症鉴别诊断 |\n| :--- | :--- | :--- | :--- |\n| FeNO50 | <25ppb | <20ppb* | 非嗜酸性气道炎症 |\n| FeNO50 | 25-50ppb | 20-35ppb* | 混合型气道炎症 |\n| FeNO50 | ≥50ppb | ≥35ppb* | 嗜酸性气道炎症 |\n| FeNO200 | >10ppb | >8ppb | 小气道炎症 |\n| CaNO | >5ppb | >3ppb | 肺泡炎症 |\n\n(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)",
  "physician": "马春英",
  "reviewer": null
}
2026-08-10 11:08:23,403 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1025288, prompt_len=1591
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共70行）
["呼出气一氧化氮测定报告单", "病人信息：", "编号：482", "姓名：", "年龄：41岁9月27天", "性别：女", "科室：普通儿科一区", "出生日期：1984-04-02", "测定时间：2026/1/29 11:02:42", "测定信息：", "一小时内禁止饮食：■是", "一小时内禁止剧烈运动：■是", "三小时内禁止食用特殊食品*：■是", "一小时内禁止抽烟：■是", "三天内使用激素类药物：■是 □否", "三天内使用抗生素：□是 ■否", "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "病史：□过敏史 □其它", "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "测定项目：", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.1℃", "呼气压力：13.6cmH20", "呼气平均流速：48ml/s", "呼气NO浓度：", "32.7,31.0,32.0,31.8,32.1,31.7ppb", "呼气NO浓度均值:32ppb", "呼气方式：■在线 □离线 □潮气", "呼气温度：20.3℃", "呼气压力：7.9cmH20", "呼气平均流速：207ml/s", "呼气NO浓度：", "11.7,11.9,11.3,11.6,11.6,11.6ppb", "呼气NO浓度均值:12ppb", "测定结果：", "FeNO50：32ppb", "FeNO200：12ppb", "CaNO：3.6ppb", "测定意义：", "测定浓度", "参考值", "炎症鉴别诊断", ">12岁", "≤12岁", "FeNO50", "<25ppb", "<20ppb*", "非嗜酸性气道炎症", "25-50ppb", "20-35ppb*", "混合型气道炎症", "≥50ppb", "≥35ppb*", "嗜酸性气道炎症", "FeNO200", ">10ppb", ">8ppb", "小气道炎症", "CaNO", ">5ppb", ">3ppb", "肺泡炎症", "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "复查时间：", "操作员：赵彩红", "医生：马春英", "电", "告", "单", "更"]

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
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord API raw response (len=3851):
[
	{"text": "呼出气一氧化氮测定报告单", "bbox": [377, 112, 652, 129]},
	{"text": "病人信息：", "bbox": [125, 140, 215, 154]},
	{"text": "编号：482", "bbox": [125, 156, 200, 169]},
	{"text": "姓名：", "bbox": [388, 157, 442, 170]},
	{"text": "年龄：41岁9月27天", "bbox": [647, 157, 790, 170]},
	{"text": "性别：女", "bbox": [125, 170, 191, 183]},
	{"text": "科室：普通儿科一区", "bbox": [388, 171, 536, 184]},
	{"text": "出生日期：1984-04-02", "bbox": [647, 171, 815, 184]},
	{"text": "测定时间：2026/1/29 11:02:42", "bbox": [125, 185, 360, 198]},
	{"text": "测定信息：", "bbox": [125, 200, 215, 214]},
	{"text": "一小时内禁止饮食：■是", "bbox": [125, 217, 458, 230]},
	{"text": "一小时内禁止剧烈运动：■是", "bbox": [517, 217, 867, 230]},
	{"text": "三小时内禁止食用特殊食品*：■是", "bbox": [125, 231, 458, 244]},
	{"text": "一小时内禁止抽烟：■是", "bbox": [517, 231, 867, 244]},
	{"text": "三天内使用激素类药物：■是 □否", "bbox": [125, 245, 458, 258]},
	{"text": "三天内使用抗生素：□是 ■否", "bbox": [517, 245, 867, 258]},
	{"text": "症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他", "bbox": [125, 259, 458, 272]},
	{"text": "病史：□过敏史 □其它", "bbox": [517, 259, 740, 272]},
	{"text": "*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。", "bbox": [125, 273, 638, 286]},
	{"text": "测定项目：", "bbox": [125, 288, 215, 302]},
	{"text": "呼气方式：■在线 □离线 □潮气", "bbox": [125, 305, 425, 318]},
	{"text": "呼气温度：20.1℃", "bbox": [125, 320, 257, 333]},
	{"text": "呼气压力：13.6cmH20", "bbox": [125, 335, 283, 348]},
	{"text": "呼气平均流速：48ml/s", "bbox": [125, 349, 291, 362]},
	{"text": "呼气NO浓度：", "bbox": [125, 363, 214, 376]},
	{"text": "32.7,31.0,32.0,31.8,32.1,31.7ppb", "bbox": [125, 377, 391, 390]},
	{"text": "呼气NO浓度均值:32ppb", "bbox": [125, 391, 296, 404]},
	{"text": "呼气方式：■在线 □离线 □潮气", "bbox": [517, 305, 816, 318]},
	{"text": "呼气温度：20.3℃", "bbox": [517, 320, 647, 333]},
	{"text": "呼气压力：7.9cmH20", "bbox": [517, 335, 665, 348]},
	{"text": "呼气平均流速：207ml/s", "bbox": [517, 349, 690, 362]},
	{"text": "呼气NO浓度：", "bbox": [517, 363, 606, 376]},
	{"text": "11.7,11.9,11.3,11.6,11.6,11.6ppb", "bbox": [517, 377, 782, 390]},
	{"text": "呼气NO浓度均值:12ppb", "bbox": [517, 391, 688, 404]},
	{"text": "测定结果：", "bbox": [125, 591, 215, 605]},
	{"text": "FeNO50：32ppb", "bbox": [267, 592, 394, 605]},
	{"text": "FeNO200：12ppb", "bbox": [475, 592, 607, 605]},
	{"text": "CaNO：3.6ppb", "bbox": [691, 592, 815, 605]},
	{"text": "测定意义：", "bbox": [125, 609, 215, 623]},
	{"text": "测定浓度", "bbox": [171, 627, 240, 640]},
	{"text": "参考值", "bbox": [377, 627, 427, 640]},
	{"text": "炎症鉴别诊断", "bbox": [658, 627, 760, 640]},
	{"text": ">12岁", "bbox": [314, 642, 360, 655]},
	{"text": "≤12岁", "bbox": [444, 642, 489, 655]},
	{"text": "FeNO50", "bbox": [180, 671, 229, 683]},
	{"text": "<25ppb", "bbox": [311, 657, 364, 669]},
	{"text": "<20ppb*", "bbox": [438, 657, 498, 669]},
	{"text": "非嗜酸性气道炎症", "bbox": [647, 657, 770, 669]},
	{"text": "25-50ppb", "bbox": [306, 671, 368, 683]},
	{"text": "20-35ppb*", "bbox": [433, 671, 502, 683]},
	{"text": "混合型气道炎症", "bbox": [655, 671, 762, 683]},
	{"text": "≥50ppb", "bbox": [310, 685, 365, 698]},
	{"text": "≥35ppb*", "bbox": [437, 685, 498, 698]},
	{"text": "嗜酸性气道炎症", "bbox": [655, 685, 762, 698]},
	{"text": "FeNO200", "bbox": [175, 700, 233, 712]},
	{"text": ">10ppb", "bbox": [311, 700, 365, 712]},
	{"text": ">8ppb", "bbox": [444, 700, 490, 712]},
	{"text": "小气道炎症", "bbox": [670, 700, 747, 712]},
	{"text": "CaNO", "bbox": [188, 714, 221, 726]},
	{"text": ">5ppb", "bbox": [314, 714, 360, 726]},
	{"text": ">3ppb", "bbox": [444, 714, 490, 726]},
	{"text": "肺泡炎症", "bbox": [678, 714, 740, 726]},
	{"text": "(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)", "bbox": [150, 727, 653, 739]},
	{"text": "复查时间：", "bbox": [129, 817, 209, 831]},
	{"text": "操作员：赵彩红", "bbox": [129, 840, 278, 854]},
	{"text": "医生：马春英", "bbox": [185, 862, 278, 876]},
	{"text": "电", "bbox": [488, 820, 505, 838]},
	{"text": "告", "bbox": [488, 854, 505, 877]},
	{"text": "单", "bbox": [488, 865, 505, 880]},
	{"text": "更", "bbox": [710, 826, 727, 840]}
]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord API: raw_items=70, valid_items=70, elapsed=21.0s
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[0]: text=呼出气一氧化氮测定报告单, bbox=[377, 112, 652, 129]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[1]: text=病人信息：, bbox=[125, 140, 215, 154]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[2]: text=编号：482, bbox=[125, 156, 200, 169]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[3]: text=姓名：, bbox=[388, 157, 442, 170]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：41岁9月27天, bbox=[647, 157, 790, 170]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[5]: text=性别：女, bbox=[125, 170, 191, 183]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[6]: text=科室：普通儿科一区, bbox=[388, 171, 536, 184]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[7]: text=出生日期：1984-04-02, bbox=[647, 171, 815, 184]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[8]: text=测定时间：2026/1/29 11:02:42, bbox=[125, 185, 360, 198]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[9]: text=测定信息：, bbox=[125, 200, 215, 214]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[10]: text=一小时内禁止饮食：■是, bbox=[125, 217, 458, 230]
2026-08-10 11:08:44,449 INFO     29 [qwen-vl-text] coord item[11]: text=一小时内禁止剧烈运动：■是, bbox=[517, 217, 867, 230]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[12]: text=三小时内禁止食用特殊食品*：■是, bbox=[125, 231, 458, 244]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[13]: text=一小时内禁止抽烟：■是, bbox=[517, 231, 867, 244]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[14]: text=三天内使用激素类药物：■是 □否, bbox=[125, 245, 458, 258]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[15]: text=三天内使用抗生素：□是 ■否, bbox=[517, 245, 867, 258]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[16]: text=症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他, bbox=[125, 259, 458, 272]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[17]: text=病史：□过敏史 □其它, bbox=[517, 259, 740, 272]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[18]: text=*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。, bbox=[125, 273, 638, 286]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[19]: text=测定项目：, bbox=[125, 288, 215, 302]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[20]: text=呼气方式：■在线 □离线 □潮气, bbox=[125, 305, 425, 318]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[21]: text=呼气温度：20.1℃, bbox=[125, 320, 257, 333]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[22]: text=呼气压力：13.6cmH20, bbox=[125, 335, 283, 348]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[23]: text=呼气平均流速：48ml/s, bbox=[125, 349, 291, 362]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[24]: text=呼气NO浓度：, bbox=[125, 363, 214, 376]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[25]: text=32.7,31.0,32.0,31.8,32.1,31.7ppb, bbox=[125, 377, 391, 390]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[26]: text=呼气NO浓度均值:32ppb, bbox=[125, 391, 296, 404]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[27]: text=呼气方式：■在线 □离线 □潮气, bbox=[517, 305, 816, 318]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[28]: text=呼气温度：20.3℃, bbox=[517, 320, 647, 333]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[29]: text=呼气压力：7.9cmH20, bbox=[517, 335, 665, 348]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[30]: text=呼气平均流速：207ml/s, bbox=[517, 349, 690, 362]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[31]: text=呼气NO浓度：, bbox=[517, 363, 606, 376]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[32]: text=11.7,11.9,11.3,11.6,11.6,11.6ppb, bbox=[517, 377, 782, 390]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[33]: text=呼气NO浓度均值:12ppb, bbox=[517, 391, 688, 404]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[34]: text=测定结果：, bbox=[125, 591, 215, 605]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[35]: text=FeNO50：32ppb, bbox=[267, 592, 394, 605]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[36]: text=FeNO200：12ppb, bbox=[475, 592, 607, 605]
2026-08-10 11:08:44,450 INFO     29 [qwen-vl-text] coord item[37]: text=CaNO：3.6ppb, bbox=[691, 592, 815, 605]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[38]: text=测定意义：, bbox=[125, 609, 215, 623]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[39]: text=测定浓度, bbox=[171, 627, 240, 640]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[40]: text=参考值, bbox=[377, 627, 427, 640]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[41]: text=炎症鉴别诊断, bbox=[658, 627, 760, 640]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[42]: text=>12岁, bbox=[314, 642, 360, 655]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[43]: text=≤12岁, bbox=[444, 642, 489, 655]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[44]: text=FeNO50, bbox=[180, 671, 229, 683]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[45]: text=<25ppb, bbox=[311, 657, 364, 669]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[46]: text=<20ppb*, bbox=[438, 657, 498, 669]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[47]: text=非嗜酸性气道炎症, bbox=[647, 657, 770, 669]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[48]: text=25-50ppb, bbox=[306, 671, 368, 683]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[49]: text=20-35ppb*, bbox=[433, 671, 502, 683]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[50]: text=混合型气道炎症, bbox=[655, 671, 762, 683]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[51]: text=≥50ppb, bbox=[310, 685, 365, 698]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[52]: text=≥35ppb*, bbox=[437, 685, 498, 698]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[53]: text=嗜酸性气道炎症, bbox=[655, 685, 762, 698]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[54]: text=FeNO200, bbox=[175, 700, 233, 712]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[55]: text=>10ppb, bbox=[311, 700, 365, 712]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[56]: text=>8ppb, bbox=[444, 700, 490, 712]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[57]: text=小气道炎症, bbox=[670, 700, 747, 712]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[58]: text=CaNO, bbox=[188, 714, 221, 726]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[59]: text=>5ppb, bbox=[314, 714, 360, 726]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[60]: text=>3ppb, bbox=[444, 714, 490, 726]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[61]: text=肺泡炎症, bbox=[678, 714, 740, 726]
2026-08-10 11:08:44,451 INFO     29 [qwen-vl-text] coord item[62]: text=(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb), bbox=[150, 727, 653, 739]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[63]: text=复查时间：, bbox=[129, 817, 209, 831]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[64]: text=操作员：赵彩红, bbox=[129, 840, 278, 854]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[65]: text=医生：马春英, bbox=[185, 862, 278, 876]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[66]: text=电, bbox=[488, 820, 505, 838]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[67]: text=告, bbox=[488, 854, 505, 877]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[68]: text=单, bbox=[488, 865, 505, 880]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] coord item[69]: text=更, bbox=[710, 826, 727, 840]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] page=0 — 70/70 coords, api_time=21.0s
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] new_positions (70):
[[0, 224.315, 387.94, 94.304, 108.618], [0, 74.375, 127.925, 117.88, 129.668], [0, 74.375, 119.0, 131.352, 142.298], [0, 230.85999999999999, 262.99, 132.194, 143.14], [0, 384.965, 470.04999999999995, 132.194, 143.14], [0, 74.375, 113.645, 143.14, 154.08599999999998], [0, 230.85999999999999, 318.91999999999996, 143.982, 154.928], [0, 384.965, 484.92499999999995, 143.982, 154.928], [0, 74.375, 214.2, 155.76999999999998, 166.716], [0, 74.375, 127.925, 168.4, 180.188], [0, 74.375, 272.51, 182.714, 193.66], [0, 307.615, 515.865, 182.714, 193.66], [0, 74.375, 272.51, 194.50199999999998, 205.44799999999998], [0, 307.615, 515.865, 194.50199999999998, 205.44799999999998], [0, 74.375, 272.51, 206.29, 217.236], [0, 307.615, 515.865, 206.29, 217.236], [0, 74.375, 272.51, 218.078, 229.024], [0, 307.615, 440.29999999999995, 218.078, 229.024], [0, 74.375, 379.60999999999996, 229.86599999999999, 240.81199999999998], [0, 74.375, 127.925, 242.49599999999998, 254.284], [0, 74.375, 252.875, 256.81, 267.756], [0, 74.375, 152.915, 269.44, 280.38599999999997], [0, 74.375, 168.385, 282.07, 293.01599999999996], [0, 74.375, 173.14499999999998, 293.858, 304.804], [0, 74.375, 127.33, 305.646, 316.592], [0, 74.375, 232.64499999999998, 317.43399999999997, 328.38], [0, 74.375, 176.12, 329.222, 340.168], [0, 307.615, 485.52, 256.81, 267.756], [0, 307.615, 384.965, 269.44, 280.38599999999997], [0, 307.615, 395.67499999999995, 282.07, 293.01599999999996], [0, 307.615, 410.54999999999995, 293.858, 304.804], [0, 307.615, 360.57, 305.646, 316.592], [0, 307.615, 465.28999999999996, 317.43399999999997, 328.38], [0, 307.615, 409.35999999999996, 329.222, 340.168], [0, 74.375, 127.925, 497.62199999999996, 509.40999999999997], [0, 158.86499999999998, 234.42999999999998, 498.464, 509.40999999999997], [0, 282.625, 361.16499999999996, 498.464, 509.40999999999997], [0, 411.145, 484.92499999999995, 498.464, 509.40999999999997], [0, 74.375, 127.925, 512.778, 524.566], [0, 101.74499999999999, 142.79999999999998, 527.934, 538.88], [0, 224.315, 254.065, 527.934, 538.88], [0, 391.51, 452.2, 527.934, 538.88], [0, 186.82999999999998, 214.2, 540.564, 551.51], [0, 264.18, 290.955, 540.564, 551.51], [0, 107.1, 136.255, 564.982, 575.086], [0, 185.045, 216.57999999999998, 553.194, 563.298], [0, 260.61, 296.31, 553.194, 563.298], [0, 384.965, 458.15, 553.194, 563.298], [0, 182.07, 218.95999999999998, 564.982, 575.086], [0, 257.635, 298.69, 564.982, 575.086], [0, 389.72499999999997, 453.39, 564.982, 575.086], [0, 184.45, 217.17499999999998, 576.77, 587.716], [0, 260.015, 296.31, 576.77, 587.716], [0, 389.72499999999997, 453.39, 576.77, 587.716], [0, 104.125, 138.635, 589.4, 599.504], [0, 185.045, 217.17499999999998, 589.4, 599.504], [0, 264.18, 291.55, 589.4, 599.504], [0, 398.65, 444.465, 589.4, 599.504], [0, 111.86, 131.495, 601.188, 611.292], [0, 186.82999999999998, 214.2, 601.188, 611.292], [0, 264.18, 291.55, 601.188, 611.292], [0, 403.40999999999997, 440.29999999999995, 601.188, 611.292], [0, 89.25, 388.53499999999997, 612.134, 622.2379999999999], [0, 76.755, 124.35499999999999, 687.914, 699.702], [0, 76.755, 165.41, 707.28, 719.068], [0, 110.07499999999999, 165.41, 725.804, 737.592], [0, 290.36, 300.47499999999997, 690.4399999999999, 705.596], [0, 290.36, 300.47499999999997, 719.068, 738.434], [0, 290.36, 300.47499999999997, 728.3299999999999, 740.9599999999999], [0, 422.45, 432.565, 695.492, 707.28]]
2026-08-10 11:08:44,452 INFO     29 [qwen-vl-text] ═══ DONE ═══ 70 positions, pages=1, time=48.8s
2026-08-10 11:08:44,452 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:08:44,460 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:08:44,460 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:08:44,460 INFO     29 [qwen-vl-text] positions(197): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:08:44,460 INFO     29 [qwen-vl-text] page grouping: [1], lines per page: [197]
2026-08-10 11:08:44,681 INFO     29 [qwen-vl-text] page=1, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:08:44,683 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1255
2026-08-10 11:08:44,683 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:44,683 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 70, \"bbox_end\": 266, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能检查报告单\n姓名：\n测试号：\n住院号：\n身高：\n160 cm\n年龄：\n41 岁\n体重：\n48 kg\n性别：\n女\n身份证号：\n科别：\n联系电话：\n预计值\nBst % (Bst/\nA1\nA2\nA3\nFVC\n[L]\n3.13\n3.15\n100.54\n3.15\n3.08\n3.07\nFEV 1\n[L]\n2.70\n1.99\n73.90\n1.99\n1.85\n1.96\nFEV6\n[L]\n3.13\n3.13\n3.05\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.31\n63.25\n60.02\n63.82\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.78\n63.25\n58.74\n62.12\nFIF 50\n[L/s]\n5.84\n5.77\n5.84\n5.48\nFEV3 % FVC\n[%]\n89.30\n89.30\n87.11\n88.97\nVC MAX\n[L]\n3.19\n3.15\n98.65\n2.99\nPEF\n[L/s]\n6.46\n6.33\n97.97\n6.33\n5.90\n5.95\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.03\n1.06\n0.89\n0.99\nMEF 25\n[L/s]\n1.77\n0.46\n26.28\n0.46\n0.38\n0.40\nMEF 50\n[L/s]\n4.06\n1.25\n30.90\n1.25\n1.13\n1.24\nMEF 75\n[L/s]\n5.73\n3.01\n52.56\n3.01\n2.22\n2.68\nV backextrapolation [B]\n0.06\n0.06\n0.05\n0.06\nV backextrapol. % FVC\n1.86\n1.86\n1.52\n1.82\nFET\n[s]\n8.73\n8.73\n5.99\n6.71\nFEF 200-1200\n[L/s]\n3.07\n3.07\n2.51\n2.98\nFVC IN\n[L]\n3.19\n2.99\n93.64\n2.26\n2.99\n2.94\nFIV1\n[L]\n2.96\n2.24\n2.96\n2.92\nFIV1 % FVC\n[%]\n99.14\n99.32\n99.14\n99.48\nFEF50 % FIF50\n[%]\n21.46\n21.72\n19.34\n22.60\nPIF\n[L/s]\n6.10\n5.87\n6.10\n5.50\nMVV\n[L/min]\n101.9\n91.45\n89.73\n91.45\nBF MVV\n[1/min]\n75.65\n75.65\n10\nFlow [L/s]\nF/V ex\nVol [L]\nVol%VCmax\nVol [L]\nTime [s]\nVol [L]\nTime [s]\n意见：\n1.轻度阻塞性通气功能障碍。\n检查质量：FVC：A级。 FEV1：A级。\n备注：受检者检查配合佳。结果仅供参考，请结合临床分析。\n2.最大自主分钟通气量（MVV）在正常范围。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n审核医生：孙帅森\n检测技师：韦龙华\n2026/1/15",
    "role": "user"
  }
]
2026-08-10 11:08:44,969 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:08:44.968+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:08:47,801 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:47,802 INFO     29 [qwen-vl-text] LLM output (len=505):
{
  "encounter_date": "2025-11-19",
  "chief_complaint": "取药",
  "present_illness": null,
  "past_history": null,
  "diagnosis": "1、支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "孟鲁司特钠片(省采)",
      "dosage": "10.0mg",
      "frequency": "每晚1次",
      "route": "口服",
      "duration": "30天",
      "quantity": "1瓶"
    },
    {
      "drug_name": "倍氯米松福莫特罗吸入气雾剂",
      "dosage": "2.0揿",
      "frequency": "一天2次",
      "route": "吸入用药",
      "duration": "30天",
      "quantity": "1瓶"
    }
  ]
}
2026-08-10 11:08:47,802 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-11-19]
2026-08-10 11:08:47,804 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1618598, prompt_len=926
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["门(急)诊病历信息", "就诊卡号:", "流水号:", "病历编号:", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "医生:", "就诊时间:2025-11-19 11:33:52", "主诉:取药", "现病史:", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "1孟鲁司特钠片(省采)◆", "1瓶10.0mg,口服,每晚1次", "30天", "2倍氯米松福莫特罗吸入气雾剂◆①", "1瓶2.0揿,吸入用药,一天2次", "30天", "备注:"]

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
2026-08-10 11:08:56,151 INFO     29 [qwen-vl-text] coord API raw response (len=1503):
[
	{"text": "门(急)诊病历信息", "bbox": [355, 22, 521, 50]},
	{"text": "就诊卡号:", "bbox": [219, 102, 275, 123]},
	{"text": "流水号:", "bbox": [219, 149, 262, 171]},
	{"text": "病历编号:", "bbox": [506, 150, 562, 171]},
	{"text": "性别:男", "bbox": [438, 199, 478, 220]},
	{"text": "年", "bbox": [505, 200, 520, 220]},
	{"text": "龄:65岁", "bbox": [569, 200, 616, 220]},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [219, 246, 382, 267]},
	{"text": "医生:", "bbox": [431, 246, 446, 267]},
	{"text": "就诊时间:2025-11-19 11:33:52", "bbox": [506, 247, 694, 267]},
	{"text": "主诉:取药", "bbox": [219, 293, 350, 314]},
	{"text": "现病史:", "bbox": [219, 339, 302, 360]},
	{"text": "既往史:", "bbox": [219, 384, 302, 405]},
	{"text": "过敏史:", "bbox": [219, 428, 302, 449]},
	{"text": "个人史:", "bbox": [219, 473, 302, 494]},
	{"text": "体格检查:", "bbox": [222, 518, 288, 538]},
	{"text": "专科情况:", "bbox": [223, 563, 288, 583]},
	{"text": "辅助检查:", "bbox": [223, 607, 288, 627]},
	{"text": "治疗项目:", "bbox": [223, 651, 288, 671]},
	{"text": "门诊诊断:", "bbox": [225, 693, 288, 712]},
	{"text": "1、支气管哮喘", "bbox": [294, 735, 378, 754]},
	{"text": "处置:", "bbox": [294, 777, 317, 796]},
	{"text": "1孟鲁司特钠片(省采)◆", "bbox": [243, 820, 375, 840]},
	{"text": "1瓶10.0mg,口服,每晚1次", "bbox": [480, 819, 621, 839]},
	{"text": "30天", "bbox": [644, 820, 670, 838]},
	{"text": "2倍氯米松福莫特罗吸入气雾剂◆①", "bbox": [243, 861, 437, 881]},
	{"text": "1瓶2.0揿,吸入用药,一天2次", "bbox": [480, 861, 638, 881]},
	{"text": "30天", "bbox": [661, 862, 687, 880]},
	{"text": "备注:", "bbox": [227, 902, 242, 919]}
]
2026-08-10 11:08:56,151 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.3s
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[355, 22, 521, 50]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号:, bbox=[219, 102, 275, 123]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[2]: text=流水号:, bbox=[219, 149, 262, 171]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[3]: text=病历编号:, bbox=[506, 150, 562, 171]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[438, 199, 478, 220]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[5]: text=年, bbox=[505, 200, 520, 220]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[6]: text=龄:65岁, bbox=[569, 200, 616, 220]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[7]: text=就诊科室:内科门诊(荔湾), bbox=[219, 246, 382, 267]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[8]: text=医生:, bbox=[431, 246, 446, 267]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2025-11-19 11:33:52, bbox=[506, 247, 694, 267]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[10]: text=主诉:取药, bbox=[219, 293, 350, 314]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[11]: text=现病史:, bbox=[219, 339, 302, 360]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[12]: text=既往史:, bbox=[219, 384, 302, 405]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[13]: text=过敏史:, bbox=[219, 428, 302, 449]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[14]: text=个人史:, bbox=[219, 473, 302, 494]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[15]: text=体格检查:, bbox=[222, 518, 288, 538]
2026-08-10 11:08:56,152 INFO     29 [qwen-vl-text] coord item[16]: text=专科情况:, bbox=[223, 563, 288, 583]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[17]: text=辅助检查:, bbox=[223, 607, 288, 627]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[18]: text=治疗项目:, bbox=[223, 651, 288, 671]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[19]: text=门诊诊断:, bbox=[225, 693, 288, 712]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[20]: text=1、支气管哮喘, bbox=[294, 735, 378, 754]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[21]: text=处置:, bbox=[294, 777, 317, 796]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[22]: text=1孟鲁司特钠片(省采)◆, bbox=[243, 820, 375, 840]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[23]: text=1瓶10.0mg,口服,每晚1次, bbox=[480, 819, 621, 839]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[24]: text=30天, bbox=[644, 820, 670, 838]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[25]: text=2倍氯米松福莫特罗吸入气雾剂◆①, bbox=[243, 861, 437, 881]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[26]: text=1瓶2.0揿,吸入用药,一天2次, bbox=[480, 861, 638, 881]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[27]: text=30天, bbox=[661, 862, 687, 880]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] coord item[28]: text=备注:, bbox=[227, 902, 242, 919]
2026-08-10 11:08:56,153 INFO     29 [qwen-vl-text] page=1 — 29/29 coords, api_time=8.3s
2026-08-10 11:08:56,154 INFO     29 [qwen-vl-text] new_positions (29):
[[1, 298.90999999999997, 438.68199999999996, 13.09, 29.75], [1, 184.398, 231.54999999999998, 60.69, 73.185], [1, 184.398, 220.60399999999998, 88.655, 101.74499999999999], [1, 426.05199999999996, 473.204, 89.25, 101.74499999999999], [1, 368.796, 402.476, 118.405, 130.9], [1, 425.21, 437.84, 119.0, 130.9], [1, 479.09799999999996, 518.672, 119.0, 130.9], [1, 184.398, 321.644, 146.37, 158.86499999999998], [1, 362.902, 375.532, 146.37, 158.86499999999998], [1, 426.05199999999996, 584.348, 146.965, 158.86499999999998], [1, 184.398, 294.7, 174.33499999999998, 186.82999999999998], [1, 184.398, 254.284, 201.70499999999998, 214.2], [1, 184.398, 254.284, 228.48, 240.975], [1, 184.398, 254.284, 254.66, 267.155], [1, 184.398, 254.284, 281.435, 293.93], [1, 186.924, 242.49599999999998, 308.21, 320.11], [1, 187.766, 242.49599999999998, 334.98499999999996, 346.885], [1, 187.766, 242.49599999999998, 361.16499999999996, 373.065], [1, 187.766, 242.49599999999998, 387.34499999999997, 399.245], [1, 189.45, 242.49599999999998, 412.335, 423.64], [1, 247.548, 318.276, 437.325, 448.63], [1, 247.548, 266.914, 462.315, 473.62], [1, 204.606, 315.75, 487.9, 499.79999999999995], [1, 404.15999999999997, 522.882, 487.30499999999995, 499.205], [1, 542.2479999999999, 564.14, 487.9, 498.60999999999996], [1, 204.606, 367.954, 512.295, 524.1949999999999], [1, 404.15999999999997, 537.196, 512.295, 524.1949999999999], [1, 556.562, 578.454, 512.89, 523.6], [1, 191.134, 203.76399999999998, 536.6899999999999, 546.805]]
2026-08-10 11:08:56,154 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=33.1s
2026-08-10 11:08:56,154 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:08:56,155 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:08:56,155 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:08:56,156 INFO     29 [qwen-vl-text] positions(56): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:08:56,156 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [22, 34]
2026-08-10 11:08:56,534 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:08:56,798 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:08:56,799 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1748
2026-08-10 11:08:56,800 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:56,800 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 70, \"bbox_end\": 125, \"encounter_dates\": [\"2025-12-12\"], \"department\": \"内科门诊(荔湾)\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "门(急)诊病历信息\n就诊卡号\n流水\n姓名\n性别:男\n年\n龄:65岁\n就诊科室:内科门诊(荔湾)\n病历编号:\n就诊时间:2025-12-12 09:26:46\n主诉:BAIYUN V8\n现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。\n完成下流操作:\n1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;\n2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。\n3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。\n4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。\n5、休息至少10分钟后,行12导联ECG检查。\n6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。\n7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。\nCS 扫描全能王\n3亿人都在用的扫描App\n门诊病历\n25/10/21 16时 门诊病历\n25/11/19 11时 门诊病历（GCP专用）\n25/12/12 09时 门诊病历（GCP专用）\n1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验\n药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。\n2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无\n关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。\n病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。\n3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试\n验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。\n跟踪合并用药\n1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏\n性鼻炎。\n2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。\n3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。\n补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸\n入 qd 治疗急性支气管炎。\n预约下次安全性电话随访时间。\n既往史:\n过敏史:\n个人史:\n体格检查:\n专科情况:\n辅助检查:\n治疗项目:\n门诊诊断:\n1、支气管哮喘\n处置:\n心电图(心电图室做)\n伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天\n孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天\n备注:\n医生:",
    "role": "user"
  }
]
2026-08-10 11:08:56,806 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:08:56,806 INFO     29 [qwen-vl-text] LLM output (len=1636):
{
  "exam_date": "2026-01-15",
  "report_date": "2026-01-15",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计值\nBst % (Bst/\nA1\nA2\nA3\nFVC\n[L]\n3.13\n3.15\n100.54\n3.15\n3.08\n3.07\nFEV 1\n[L]\n2.70\n1.99\n73.90\n1.99\n1.85\n1.96\nFEV6\n[L]\n3.13\n3.13\n3.05\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.31\n63.25\n60.02\n63.82\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.78\n63.25\n58.74\n62.12\nFIF 50\n[L/s]\n5.84\n5.77\n5.84\n5.48\nFEV3 % FVC\n[%]\n89.30\n89.30\n87.11\n88.97\nVC MAX\n[L]\n3.19\n3.15\n98.65\n2.99\nPEF\n[L/s]\n6.46\n6.33\n97.97\n6.33\n5.90\n5.95\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.03\n1.06\n0.89\n0.99\nMEF 25\n[L/s]\n1.77\n0.46\n26.28\n0.46\n0.38\n0.40\nMEF 50\n[L/s]\n4.06\n1.25\n30.90\n1.25\n1.13\n1.24\nMEF 75\n[L/s]\n5.73\n3.01\n52.56\n3.01\n2.22\n2.68\nV backextrapolation [B]\n0.06\n0.06\n0.05\n0.06\nV backextrapol. % FVC\n1.86\n1.86\n1.52\n1.82\nFET\n[s]\n8.73\n8.73\n5.99\n6.71\nFEF 200-1200\n[L/s]\n3.07\n3.07\n2.51\n2.98\nFVC IN\n[L]\n3.19\n2.99\n93.64\n2.26\n2.99\n2.94\nFIV1\n[L]\n2.96\n2.24\n2.96\n2.92\nFIV1 % FVC\n[%]\n99.14\n99.32\n99.14\n99.48\nFEF50 % FIF50\n[%]\n21.46\n21.72\n19.34\n22.60\nPIF\n[L/s]\n6.10\n5.87\n6.10\n5.50\nMVV\n[L/min]\n101.9\n91.45\n89.73\n91.45\nBF MVV\n[1/min]\n75.65\n75.65\n10\nFlow [L/s]\nF/V ex\nVol [L]\nVol%VCmax\nVol [L]\nTime [s]\nVol [L]\nTime [s]\n检查质量：FVC：A级。 FEV1：A级。\n备注：受检者检查配合佳。结果仅供参考，请结合临床分析。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。",
  "conclusion": "意见：\n1.轻度阻塞性通气功能障碍。\n2.最大自主分钟通气量（MVV）在正常范围。",
  "physician": "韦龙华",
  "reviewer": "孙帅森"
}
2026-08-10 11:08:56,808 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1156210, prompt_len=2460
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共197行）
["肺功能检查报告单", "姓名：", "测试号：", "住院号：", "身高：", "160 cm", "年龄：", "41 岁", "体重：", "48 kg", "性别：", "女", "身份证号：", "科别：", "联系电话：", "预计值", "Bst % (Bst/", "A1", "A2", "A3", "FVC", "[L]", "3.13", "3.15", "100.54", "3.15", "3.08", "3.07", "FEV 1", "[L]", "2.70", "1.99", "73.90", "1.99", "1.85", "1.96", "FEV6", "[L]", "3.13", "3.13", "3.05", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.31", "63.25", "60.02", "63.82", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.78", "63.25", "58.74", "62.12", "FIF 50", "[L/s]", "5.84", "5.77", "5.84", "5.48", "FEV3 % FVC", "[%]", "89.30", "89.30", "87.11", "88.97", "VC MAX", "[L]", "3.19", "3.15", "98.65", "2.99", "PEF", "[L/s]", "6.46", "6.33", "97.97", "6.33", "5.90", "5.95", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.03", "1.06", "0.89", "0.99", "MEF 25", "[L/s]", "1.77", "0.46", "26.28", "0.46", "0.38", "0.40", "MEF 50", "[L/s]", "4.06", "1.25", "30.90", "1.25", "1.13", "1.24", "MEF 75", "[L/s]", "5.73", "3.01", "52.56", "3.01", "2.22", "2.68", "V backextrapolation [B]", "0.06", "0.06", "0.05", "0.06", "V backextrapol. % FVC", "1.86", "1.86", "1.52", "1.82", "FET", "[s]", "8.73", "8.73", "5.99", "6.71", "FEF 200-1200", "[L/s]", "3.07", "3.07", "2.51", "2.98", "FVC IN", "[L]", "3.19", "2.99", "93.64", "2.26", "2.99", "2.94", "FIV1", "[L]", "2.96", "2.24", "2.96", "2.92", "FIV1 % FVC", "[%]", "99.14", "99.32", "99.14", "99.48", "FEF50 % FIF50", "[%]", "21.46", "21.72", "19.34", "22.60", "PIF", "[L/s]", "6.10", "5.87", "6.10", "5.50", "MVV", "[L/min]", "101.9", "91.45", "89.73", "91.45", "BF MVV", "[1/min]", "75.65", "75.65", "10", "Flow [L/s]", "F/V ex", "Vol [L]", "Vol%VCmax", "Vol [L]", "Time [s]", "Vol [L]", "Time [s]", "意见：", "1.轻度阻塞性通气功能障碍。", "检查质量：FVC：A级。 FEV1：A级。", "备注：受检者检查配合佳。结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）在正常范围。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "审核医生：孙帅森", "检测技师：韦龙华", "2026/1/15"]

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
2026-08-10 11:09:48,098 INFO     29 [qwen-vl-text] coord API raw response (len=9904):
[
	{"text": "肺功能检查报告单", "bbox": [417, 47, 607, 69]},
	{"text": "姓名：", "bbox": [184, 65, 230, 78]},
	{"text": "测试号：", "bbox": [184, 77, 245, 90]},
	{"text": "住院号：", "bbox": [513, 67, 574, 80]},
	{"text": "身高：", "bbox": [184, 90, 228, 102]},
	{"text": "160 cm", "bbox": [345, 93, 399, 104]},
	{"text": "年龄：", "bbox": [513, 79, 556, 92]},
	{"text": "41 岁", "bbox": [674, 80, 717, 92]},
	{"text": "体重：", "bbox": [184, 102, 228, 114]},
	{"text": "48 kg", "bbox": [345, 105, 390, 116]},
	{"text": "性别：", "bbox": [513, 91, 556, 104]},
	{"text": "女", "bbox": [674, 92, 691, 104]},
	{"text": "身份证号：", "bbox": [184, 114, 263, 126]},
	{"text": "科别：", "bbox": [513, 103, 556, 116]},
	{"text": "联系电话：", "bbox": [513, 115, 590, 127]},
	{"text": "预计值", "bbox": [312, 132, 359, 144]},
	{"text": "Bst % (Bst/", "bbox": [382, 133, 471, 144]},
	{"text": "A1", "bbox": [507, 133, 524, 143]},
	{"text": "A2", "bbox": [560, 133, 577, 143]},
	{"text": "A3", "bbox": [613, 133, 631, 143]},
	{"text": "FVC", "bbox": [107, 157, 136, 167]},
	{"text": "[L]", "bbox": [278, 157, 298, 168]},
	{"text": "3.13", "bbox": [321, 157, 356, 167]},
	{"text": "3.15", "bbox": [375, 157, 410, 167]},
	{"text": "100.54", "bbox": [419, 157, 471, 167]},
	{"text": "3.15", "bbox": [490, 157, 524, 167]},
	{"text": "3.08", "bbox": [542, 157, 577, 167]},
	{"text": "3.07", "bbox": [595, 157, 630, 167]},
	{"text": "FEV 1", "bbox": [107, 169, 152, 179]},
	{"text": "[L]", "bbox": [278, 169, 298, 180]},
	{"text": "2.70", "bbox": [321, 169, 356, 179]},
	{"text": "1.99", "bbox": [375, 169, 410, 179]},
	{"text": "73.90", "bbox": [427, 169, 471, 179]},
	{"text": "1.99", "bbox": [490, 169, 524, 179]},
	{"text": "1.85", "bbox": [542, 169, 577, 179]},
	{"text": "1.96", "bbox": [595, 169, 630, 179]},
	{"text": "FEV6", "bbox": [107, 181, 143, 191]},
	{"text": "[L]", "bbox": [278, 181, 298, 192]},
	{"text": "3.13", "bbox": [375, 181, 410, 191]},
	{"text": "3.13", "bbox": [490, 181, 524, 191]},
	{"text": "3.05", "bbox": [595, 181, 630, 191]},
	{"text": "FEV 1 % FVC", "bbox": [107, 193, 205, 203]},
	{"text": "[%]", "bbox": [278, 193, 298, 204]},
	{"text": "83.98", "bbox": [312, 193, 356, 203]},
	{"text": "63.25", "bbox": [367, 193, 410, 203]},
	{"text": "75.31", "bbox": [427, 193, 471, 203]},
	{"text": "63.25", "bbox": [480, 193, 524, 203]},
	{"text": "60.02", "bbox": [534, 193, 577, 203]},
	{"text": "63.82", "bbox": [587, 193, 630, 203]},
	{"text": "FEV 1 % VC MAX", "bbox": [107, 205, 232, 215]},
	{"text": "[%]", "bbox": [278, 205, 298, 216]},
	{"text": "81.31", "bbox": [312, 205, 356, 215]},
	{"text": "63.25", "bbox": [367, 205, 410, 215]},
	{"text": "77.78", "bbox": [427, 205, 471, 215]},
	{"text": "63.25", "bbox": [480, 205, 524, 215]},
	{"text": "58.74", "bbox": [534, 205, 577, 215]},
	{"text": "62.12", "bbox": [587, 205, 630, 215]},
	{"text": "FIF 50", "bbox": [107, 217, 160, 227]},
	{"text": "[L/s]", "bbox": [260, 217, 300, 228]},
	{"text": "5.84", "bbox": [375, 217, 410, 227]},
	{"text": "5.77", "bbox": [490, 217, 524, 227]},
	{"text": "5.84", "bbox": [542, 217, 577, 227]},
	{"text": "5.48", "bbox": [595, 217, 630, 227]},
	{"text": "FEV3 % FVC", "bbox": [107, 229, 195, 239]},
	{"text": "[%]", "bbox": [278, 229, 298, 240]},
	{"text": "89.30", "bbox": [367, 229, 410, 239]},
	{"text": "89.30", "bbox": [480, 229, 524, 239]},
	{"text": "87.11", "bbox": [534, 229, 577, 239]},
	{"text": "88.97", "bbox": [587, 229, 630, 239]},
	{"text": "VC MAX", "bbox": [107, 241, 160, 251]},
	{"text": "[L]", "bbox": [278, 241, 298, 252]},
	{"text": "3.19", "bbox": [321, 241, 356, 251]},
	{"text": "3.15", "bbox": [375, 241, 410, 251]},
	{"text": "98.65", "bbox": [427, 241, 471, 251]},
	{"text": "2.99", "bbox": [490, 241, 524, 251]},
	{"text": "PEF", "bbox": [107, 253, 134, 263]},
	{"text": "[L/s]", "bbox": [260, 253, 300, 264]},
	{"text": "6.46", "bbox": [321, 253, 356, 263]},
	{"text": "6.33", "bbox": [375, 253, 410, 263]},
	{"text": "97.97", "bbox": [427, 253, 471, 263]},
	{"text": "6.33", "bbox": [490, 253, 524, 263]},
	{"text": "5.90", "bbox": [542, 253, 577, 263]},
	{"text": "5.95", "bbox": [595, 253, 630, 263]},
	{"text": "MMEF 75/25", "bbox": [107, 265, 195, 275]},
	{"text": "[L/s]", "bbox": [260, 265, 300, 276]},
	{"text": "3.53", "bbox": [321, 265, 356, 275]},
	{"text": "1.06", "bbox": [375, 265, 410, 275]},
	{"text": "30.03", "bbox": [427, 265, 471, 275]},
	{"text": "1.06", "bbox": [490, 265, 524, 275]},
	{"text": "0.89", "bbox": [542, 265, 577, 275]},
	{"text": "0.99", "bbox": [595, 265, 630, 275]},
	{"text": "MEF 25", "bbox": [107, 277, 160, 287]},
	{"text": "[L/s]", "bbox": [260, 277, 300, 288]},
	{"text": "1.77", "bbox": [321, 277, 356, 287]},
	{"text": "0.46", "bbox": [375, 277, 410, 287]},
	{"text": "26.28", "bbox": [427, 277, 471, 287]},
	{"text": "0.46", "bbox": [490, 277, 524, 287]},
	{"text": "0.38", "bbox": [542, 277, 577, 287]},
	{"text": "0.40", "bbox": [595, 277, 630, 287]},
	{"text": "MEF 50", "bbox": [107, 289, 160, 299]},
	{"text": "[L/s]", "bbox": [260, 289, 300, 300]},
	{"text": "4.06", "bbox": [321, 289, 356, 299]},
	{"text": "1.25", "bbox": [375, 289, 410, 299]},
	{"text": "30.90", "bbox": [427, 289, 471, 299]},
	{"text": "1.25", "bbox": [490, 289, 524, 299]},
	{"text": "1.13", "bbox": [542, 289, 577, 299]},
	{"text": "1.24", "bbox": [595, 289, 630, 299]},
	{"text": "MEF 75", "bbox": [107, 301, 160, 311]},
	{"text": "[L/s]", "bbox": [260, 301, 300, 312]},
	{"text": "5.73", "bbox": [321, 301, 356, 311]},
	{"text": "3.01", "bbox": [375, 301, 410, 311]},
	{"text": "52.56", "bbox": [427, 301, 471, 311]},
	{"text": "3.01", "bbox": [490, 301, 524, 311]},
	{"text": "2.22", "bbox": [542, 301, 577, 311]},
	{"text": "2.68", "bbox": [595, 301, 630, 311]},
	{"text": "V backextrapolation [B]", "bbox": [107, 314, 303, 324]},
	{"text": "0.06", "bbox": [375, 314, 410, 324]},
	{"text": "0.06", "bbox": [490, 314, 524, 324]},
	{"text": "0.05", "bbox": [542, 314, 577, 324]},
	{"text": "0.06", "bbox": [595, 314, 630, 324]},
	{"text": "V backextrapol. % FVC", "bbox": [107, 326, 300, 336]},
	{"text": "1.86", "bbox": [375, 326, 410, 336]},
	{"text": "1.86", "bbox": [490, 326, 524, 336]},
	{"text": "1.52", "bbox": [542, 326, 577, 336]},
	{"text": "1.82", "bbox": [595, 326, 630, 336]},
	{"text": "FET", "bbox": [107, 338, 134, 349]},
	{"text": "[s]", "bbox": [278, 338, 298, 349]},
	{"text": "8.73", "bbox": [375, 338, 410, 349]},
	{"text": "8.73", "bbox": [490, 338, 524, 349]},
	{"text": "5.99", "bbox": [542, 338, 577, 349]},
	{"text": "6.71", "bbox": [595, 338, 630, 349]},
	{"text": "FEF 200-1200", "bbox": [107, 351, 212, 361]},
	{"text": "[L/s]", "bbox": [260, 351, 300, 362]},
	{"text": "3.07", "bbox": [375, 351, 410, 361]},
	{"text": "3.07", "bbox": [490, 351, 524, 361]},
	{"text": "2.51", "bbox": [542, 351, 577, 361]},
	{"text": "2.98", "bbox": [595, 351, 630, 361]},
	{"text": "FVC IN", "bbox": [107, 363, 160, 373]},
	{"text": "[L]", "bbox": [278, 363, 298, 374]},
	{"text": "3.19", "bbox": [321, 363, 356, 373]},
	{"text": "2.99", "bbox": [375, 363, 410, 373]},
	{"text": "93.64", "bbox": [427, 363, 471, 373]},
	{"text": "2.26", "bbox": [490, 363, 524, 373]},
	{"text": "2.99", "bbox": [542, 363, 577, 373]},
	{"text": "2.94", "bbox": [595, 363, 630, 373]},
	{"text": "FIV1", "bbox": [107, 375, 141, 385]},
	{"text": "[L]", "bbox": [278, 375, 298, 386]},
	{"text": "2.96", "bbox": [375, 375, 410, 385]},
	{"text": "2.24", "bbox": [490, 375, 524, 385]},
	{"text": "2.96", "bbox": [542, 375, 577, 385]},
	{"text": "2.92", "bbox": [595, 375, 630, 385]},
	{"text": "FIV1 % FVC", "bbox": [107, 387, 195, 397]},
	{"text": "[%]", "bbox": [278, 387, 298, 398]},
	{"text": "99.14", "bbox": [367, 387, 410, 397]},
	{"text": "99.32", "bbox": [480, 387, 524, 397]},
	{"text": "99.14", "bbox": [534, 387, 577, 397]},
	{"text": "99.48", "bbox": [587, 387, 630, 397]},
	{"text": "FEF50 % FIF50", "bbox": [107, 400, 221, 410]},
	{"text": "[%]", "bbox": [278, 400, 298, 411]},
	{"text": "21.46", "bbox": [367, 400, 410, 410]},
	{"text": "21.72", "bbox": [480, 400, 524, 410]},
	{"text": "19.34", "bbox": [534, 400, 577, 410]},
	{"text": "22.60", "bbox": [587, 400, 630, 410]},
	{"text": "PIF", "bbox": [107, 412, 134, 422]},
	{"text": "[L/s]", "bbox": [260, 412, 300, 423]},
	{"text": "6.10", "bbox": [375, 412, 410, 422]},
	{"text": "5.87", "bbox": [490, 412, 524, 422]},
	{"text": "6.10", "bbox": [542, 412, 577, 422]},
	{"text": "5.50", "bbox": [595, 412, 630, 422]},
	{"text": "MVV", "bbox": [107, 425, 134, 435]},
	{"text": "[L/min]", "bbox": [243, 425, 300, 436]},
	{"text": "101.9", "bbox": [312, 425, 356, 435]},
	{"text": "91.45", "bbox": [367, 425, 410, 435]},
	{"text": "89.73", "bbox": [427, 425, 471, 435]},
	{"text": "91.45", "bbox": [480, 425, 524, 435]},
	{"text": "BF MVV", "bbox": [107, 437, 160, 447]},
	{"text": "[1/min]", "bbox": [243, 437, 300, 448]},
	{"text": "75.65", "bbox": [367, 437, 410, 447]},
	{"text": "75.65", "bbox": [480, 437, 524, 447]},
	{"text": "10", "bbox": [240, 475, 252, 485]},
	{"text": "Flow [L/s]", "bbox": [258, 479, 307, 490]},
	{"text": "F/V ex", "bbox": [340, 480, 371, 490]},
	{"text": "Vol [L]", "bbox": [595, 482, 632, 493]},
	{"text": "Vol%VCmax", "bbox": [556, 515, 614, 525]},
	{"text": "Vol [L]", "bbox": [575, 607, 610, 618]},
	{"text": "Time [s]", "bbox": [708, 568, 747, 578]},
	{"text": "Vol [L]", "bbox": [556, 614, 573, 623]},
	{"text": "Time [s]", "bbox": [699, 702, 738, 712]},
	{"text": "意见：", "bbox": [98, 714, 157, 729]},
	{"text": "1.轻度阻塞性通气功能障碍。", "bbox": [93, 745, 315, 757]},
	{"text": "检查质量：FVC：A级。 FEV1：A级。", "bbox": [93, 757, 369, 769]},
	{"text": "备注：受检者检查配合佳。结果仅供参考，请结合临床分析。", "bbox": [93, 769, 563, 781]},
	{"text": "2.最大自主分钟通气量（MVV）在正常范围。", "bbox": [93, 781, 432, 793]},
	{"text": "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "bbox": [93, 793, 537, 805]},
	{"text": "审核医生：孙帅森", "bbox": [547, 813, 742, 829]},
	{"text": "检测技师：韦龙华", "bbox": [547, 832, 752, 853]},
	{"text": "2026/1/15", "bbox": [109, 889, 174, 898]}
]
2026-08-10 11:09:48,100 INFO     29 [qwen-vl-text] coord API: raw_items=197, valid_items=197, elapsed=51.3s
2026-08-10 11:09:48,100 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能检查报告单, bbox=[417, 47, 607, 69]
2026-08-10 11:09:48,100 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[184, 65, 230, 78]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[2]: text=测试号：, bbox=[184, 77, 245, 90]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[3]: text=住院号：, bbox=[513, 67, 574, 80]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[4]: text=身高：, bbox=[184, 90, 228, 102]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[5]: text=160 cm, bbox=[345, 93, 399, 104]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：, bbox=[513, 79, 556, 92]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[7]: text=41 岁, bbox=[674, 80, 717, 92]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[8]: text=体重：, bbox=[184, 102, 228, 114]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[9]: text=48 kg, bbox=[345, 105, 390, 116]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[10]: text=性别：, bbox=[513, 91, 556, 104]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[11]: text=女, bbox=[674, 92, 691, 104]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号：, bbox=[184, 114, 263, 126]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[13]: text=科别：, bbox=[513, 103, 556, 116]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[14]: text=联系电话：, bbox=[513, 115, 590, 127]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[15]: text=预计值, bbox=[312, 132, 359, 144]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[16]: text=Bst % (Bst/, bbox=[382, 133, 471, 144]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[17]: text=A1, bbox=[507, 133, 524, 143]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[18]: text=A2, bbox=[560, 133, 577, 143]
2026-08-10 11:09:48,101 INFO     29 [qwen-vl-text] coord item[19]: text=A3, bbox=[613, 133, 631, 143]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[20]: text=FVC, bbox=[107, 157, 136, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[21]: text=[L], bbox=[278, 157, 298, 168]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[22]: text=3.13, bbox=[321, 157, 356, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[23]: text=3.15, bbox=[375, 157, 410, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[24]: text=100.54, bbox=[419, 157, 471, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[25]: text=3.15, bbox=[490, 157, 524, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[26]: text=3.08, bbox=[542, 157, 577, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[27]: text=3.07, bbox=[595, 157, 630, 167]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[28]: text=FEV 1, bbox=[107, 169, 152, 179]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[29]: text=[L], bbox=[278, 169, 298, 180]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[30]: text=2.70, bbox=[321, 169, 356, 179]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[31]: text=1.99, bbox=[375, 169, 410, 179]
2026-08-10 11:09:48,102 INFO     29 [qwen-vl-text] coord item[32]: text=73.90, bbox=[427, 169, 471, 179]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[33]: text=1.99, bbox=[490, 169, 524, 179]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[34]: text=1.85, bbox=[542, 169, 577, 179]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[35]: text=1.96, bbox=[595, 169, 630, 179]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[36]: text=FEV6, bbox=[107, 181, 143, 191]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[37]: text=[L], bbox=[278, 181, 298, 192]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[38]: text=3.13, bbox=[375, 181, 410, 191]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[39]: text=3.13, bbox=[490, 181, 524, 191]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[40]: text=3.05, bbox=[595, 181, 630, 191]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[41]: text=FEV 1 % FVC, bbox=[107, 193, 205, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[42]: text=[%], bbox=[278, 193, 298, 204]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[43]: text=83.98, bbox=[312, 193, 356, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[44]: text=63.25, bbox=[367, 193, 410, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[45]: text=75.31, bbox=[427, 193, 471, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[46]: text=63.25, bbox=[480, 193, 524, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[47]: text=60.02, bbox=[534, 193, 577, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[48]: text=63.82, bbox=[587, 193, 630, 203]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[49]: text=FEV 1 % VC MAX, bbox=[107, 205, 232, 215]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[278, 205, 298, 216]
2026-08-10 11:09:48,103 INFO     29 [qwen-vl-text] coord item[51]: text=81.31, bbox=[312, 205, 356, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[52]: text=63.25, bbox=[367, 205, 410, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[53]: text=77.78, bbox=[427, 205, 471, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[54]: text=63.25, bbox=[480, 205, 524, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[55]: text=58.74, bbox=[534, 205, 577, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[56]: text=62.12, bbox=[587, 205, 630, 215]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[57]: text=FIF 50, bbox=[107, 217, 160, 227]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[58]: text=[L/s], bbox=[260, 217, 300, 228]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[59]: text=5.84, bbox=[375, 217, 410, 227]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[60]: text=5.77, bbox=[490, 217, 524, 227]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[61]: text=5.84, bbox=[542, 217, 577, 227]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[62]: text=5.48, bbox=[595, 217, 630, 227]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[63]: text=FEV3 % FVC, bbox=[107, 229, 195, 239]
2026-08-10 11:09:48,104 INFO     29 [qwen-vl-text] coord item[64]: text=[%], bbox=[278, 229, 298, 240]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[65]: text=89.30, bbox=[367, 229, 410, 239]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[66]: text=89.30, bbox=[480, 229, 524, 239]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[67]: text=87.11, bbox=[534, 229, 577, 239]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[68]: text=88.97, bbox=[587, 229, 630, 239]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[69]: text=VC MAX, bbox=[107, 241, 160, 251]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[70]: text=[L], bbox=[278, 241, 298, 252]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[71]: text=3.19, bbox=[321, 241, 356, 251]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[72]: text=3.15, bbox=[375, 241, 410, 251]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[73]: text=98.65, bbox=[427, 241, 471, 251]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[74]: text=2.99, bbox=[490, 241, 524, 251]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[75]: text=PEF, bbox=[107, 253, 134, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[76]: text=[L/s], bbox=[260, 253, 300, 264]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[77]: text=6.46, bbox=[321, 253, 356, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[78]: text=6.33, bbox=[375, 253, 410, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[79]: text=97.97, bbox=[427, 253, 471, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[80]: text=6.33, bbox=[490, 253, 524, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[81]: text=5.90, bbox=[542, 253, 577, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[82]: text=5.95, bbox=[595, 253, 630, 263]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[83]: text=MMEF 75/25, bbox=[107, 265, 195, 275]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[84]: text=[L/s], bbox=[260, 265, 300, 276]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[85]: text=3.53, bbox=[321, 265, 356, 275]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[86]: text=1.06, bbox=[375, 265, 410, 275]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[87]: text=30.03, bbox=[427, 265, 471, 275]
2026-08-10 11:09:48,105 INFO     29 [qwen-vl-text] coord item[88]: text=1.06, bbox=[490, 265, 524, 275]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[89]: text=0.89, bbox=[542, 265, 577, 275]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[90]: text=0.99, bbox=[595, 265, 630, 275]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[91]: text=MEF 25, bbox=[107, 277, 160, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[92]: text=[L/s], bbox=[260, 277, 300, 288]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[93]: text=1.77, bbox=[321, 277, 356, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[94]: text=0.46, bbox=[375, 277, 410, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[95]: text=26.28, bbox=[427, 277, 471, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[96]: text=0.46, bbox=[490, 277, 524, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[97]: text=0.38, bbox=[542, 277, 577, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[98]: text=0.40, bbox=[595, 277, 630, 287]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[99]: text=MEF 50, bbox=[107, 289, 160, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[100]: text=[L/s], bbox=[260, 289, 300, 300]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[101]: text=4.06, bbox=[321, 289, 356, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[102]: text=1.25, bbox=[375, 289, 410, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[103]: text=30.90, bbox=[427, 289, 471, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[104]: text=1.25, bbox=[490, 289, 524, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[105]: text=1.13, bbox=[542, 289, 577, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[106]: text=1.24, bbox=[595, 289, 630, 299]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[107]: text=MEF 75, bbox=[107, 301, 160, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[108]: text=[L/s], bbox=[260, 301, 300, 312]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[109]: text=5.73, bbox=[321, 301, 356, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[110]: text=3.01, bbox=[375, 301, 410, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[111]: text=52.56, bbox=[427, 301, 471, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[112]: text=3.01, bbox=[490, 301, 524, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[113]: text=2.22, bbox=[542, 301, 577, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[114]: text=2.68, bbox=[595, 301, 630, 311]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[115]: text=V backextrapolation [B], bbox=[107, 314, 303, 324]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[116]: text=0.06, bbox=[375, 314, 410, 324]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[117]: text=0.06, bbox=[490, 314, 524, 324]
2026-08-10 11:09:48,106 INFO     29 [qwen-vl-text] coord item[118]: text=0.05, bbox=[542, 314, 577, 324]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[119]: text=0.06, bbox=[595, 314, 630, 324]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[120]: text=V backextrapol. % FVC, bbox=[107, 326, 300, 336]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[121]: text=1.86, bbox=[375, 326, 410, 336]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[122]: text=1.86, bbox=[490, 326, 524, 336]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[123]: text=1.52, bbox=[542, 326, 577, 336]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[124]: text=1.82, bbox=[595, 326, 630, 336]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[125]: text=FET, bbox=[107, 338, 134, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[126]: text=[s], bbox=[278, 338, 298, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[127]: text=8.73, bbox=[375, 338, 410, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[128]: text=8.73, bbox=[490, 338, 524, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[129]: text=5.99, bbox=[542, 338, 577, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[130]: text=6.71, bbox=[595, 338, 630, 349]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[131]: text=FEF 200-1200, bbox=[107, 351, 212, 361]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[132]: text=[L/s], bbox=[260, 351, 300, 362]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[133]: text=3.07, bbox=[375, 351, 410, 361]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[134]: text=3.07, bbox=[490, 351, 524, 361]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[135]: text=2.51, bbox=[542, 351, 577, 361]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[136]: text=2.98, bbox=[595, 351, 630, 361]
2026-08-10 11:09:48,107 INFO     29 [qwen-vl-text] coord item[137]: text=FVC IN, bbox=[107, 363, 160, 373]
2026-08-10 11:09:48,108 INFO     29 [qwen-vl-text] coord item[138]: text=[L], bbox=[278, 363, 298, 374]
2026-08-10 11:09:48,108 INFO     29 [qwen-vl-text] coord item[139]: text=3.19, bbox=[321, 363, 356, 373]
2026-08-10 11:09:48,108 INFO     29 [qwen-vl-text] coord item[140]: text=2.99, bbox=[375, 363, 410, 373]
2026-08-10 11:09:48,108 INFO     29 [qwen-vl-text] coord item[141]: text=93.64, bbox=[427, 363, 471, 373]
2026-08-10 11:09:48,108 INFO     29 [qwen-vl-text] coord item[142]: text=2.26, bbox=[490, 363, 524, 373]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[143]: text=2.99, bbox=[542, 363, 577, 373]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[144]: text=2.94, bbox=[595, 363, 630, 373]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[145]: text=FIV1, bbox=[107, 375, 141, 385]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[146]: text=[L], bbox=[278, 375, 298, 386]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[147]: text=2.96, bbox=[375, 375, 410, 385]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[148]: text=2.24, bbox=[490, 375, 524, 385]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[149]: text=2.96, bbox=[542, 375, 577, 385]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[150]: text=2.92, bbox=[595, 375, 630, 385]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[151]: text=FIV1 % FVC, bbox=[107, 387, 195, 397]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[152]: text=[%], bbox=[278, 387, 298, 398]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[153]: text=99.14, bbox=[367, 387, 410, 397]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[154]: text=99.32, bbox=[480, 387, 524, 397]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[155]: text=99.14, bbox=[534, 387, 577, 397]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[156]: text=99.48, bbox=[587, 387, 630, 397]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[157]: text=FEF50 % FIF50, bbox=[107, 400, 221, 410]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[158]: text=[%], bbox=[278, 400, 298, 411]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[159]: text=21.46, bbox=[367, 400, 410, 410]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[160]: text=21.72, bbox=[480, 400, 524, 410]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[161]: text=19.34, bbox=[534, 400, 577, 410]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[162]: text=22.60, bbox=[587, 400, 630, 410]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[163]: text=PIF, bbox=[107, 412, 134, 422]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[164]: text=[L/s], bbox=[260, 412, 300, 423]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[165]: text=6.10, bbox=[375, 412, 410, 422]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[166]: text=5.87, bbox=[490, 412, 524, 422]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[167]: text=6.10, bbox=[542, 412, 577, 422]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[168]: text=5.50, bbox=[595, 412, 630, 422]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[169]: text=MVV, bbox=[107, 425, 134, 435]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[170]: text=[L/min], bbox=[243, 425, 300, 436]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[171]: text=101.9, bbox=[312, 425, 356, 435]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[172]: text=91.45, bbox=[367, 425, 410, 435]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[173]: text=89.73, bbox=[427, 425, 471, 435]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[174]: text=91.45, bbox=[480, 425, 524, 435]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[175]: text=BF MVV, bbox=[107, 437, 160, 447]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[176]: text=[1/min], bbox=[243, 437, 300, 448]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[177]: text=75.65, bbox=[367, 437, 410, 447]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[178]: text=75.65, bbox=[480, 437, 524, 447]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[179]: text=10, bbox=[240, 475, 252, 485]
2026-08-10 11:09:48,109 INFO     29 [qwen-vl-text] coord item[180]: text=Flow [L/s], bbox=[258, 479, 307, 490]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[181]: text=F/V ex, bbox=[340, 480, 371, 490]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[182]: text=Vol [L], bbox=[595, 482, 632, 493]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[183]: text=Vol%VCmax, bbox=[556, 515, 614, 525]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[184]: text=Vol [L], bbox=[575, 607, 610, 618]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[185]: text=Time [s], bbox=[708, 568, 747, 578]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[186]: text=Vol [L], bbox=[556, 614, 573, 623]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[187]: text=Time [s], bbox=[699, 702, 738, 712]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[188]: text=意见：, bbox=[98, 714, 157, 729]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[189]: text=1.轻度阻塞性通气功能障碍。, bbox=[93, 745, 315, 757]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[190]: text=检查质量：FVC：A级。 FEV1：A级。, bbox=[93, 757, 369, 769]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[191]: text=备注：受检者检查配合佳。结果仅供参考，请结合临床分析。, bbox=[93, 769, 563, 781]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[192]: text=2.最大自主分钟通气量（MVV）在正常范围。, bbox=[93, 781, 432, 793]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[193]: text=备注：患者MVV配合佳。结果仅供参考，请结合临床分析。, bbox=[93, 793, 537, 805]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[194]: text=审核医生：孙帅森, bbox=[547, 813, 742, 829]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[195]: text=检测技师：韦龙华, bbox=[547, 832, 752, 853]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] coord item[196]: text=2026/1/15, bbox=[109, 889, 174, 898]
2026-08-10 11:09:48,110 INFO     29 [qwen-vl-text] page=1 — 197/197 coords, api_time=51.3s
2026-08-10 11:09:48,111 INFO     29 [qwen-vl-text] new_positions (197):
[[1, 248.11499999999998, 361.16499999999996, 39.574, 58.098], [1, 109.47999999999999, 136.85, 54.73, 65.676], [1, 109.47999999999999, 145.775, 64.834, 75.78], [1, 305.235, 341.53, 56.414, 67.36], [1, 109.47999999999999, 135.66, 75.78, 85.884], [1, 205.27499999999998, 237.405, 78.306, 87.568], [1, 305.235, 330.82, 66.518, 77.464], [1, 401.03, 426.615, 67.36, 77.464], [1, 109.47999999999999, 135.66, 85.884, 95.988], [1, 205.27499999999998, 232.04999999999998, 88.41, 97.672], [1, 305.235, 330.82, 76.622, 87.568], [1, 401.03, 411.145, 77.464, 87.568], [1, 109.47999999999999, 156.48499999999999, 95.988, 106.092], [1, 305.235, 330.82, 86.726, 97.672], [1, 305.235, 351.05, 96.83, 106.934], [1, 185.64, 213.605, 111.14399999999999, 121.24799999999999], [1, 227.29, 280.245, 111.98599999999999, 121.24799999999999], [1, 301.66499999999996, 311.78, 111.98599999999999, 120.40599999999999], [1, 333.2, 343.315, 111.98599999999999, 120.40599999999999], [1, 364.73499999999996, 375.445, 111.98599999999999, 120.40599999999999], [1, 63.665, 80.92, 132.194, 140.614], [1, 165.41, 177.31, 132.194, 141.456], [1, 190.995, 211.82, 132.194, 140.614], [1, 223.125, 243.95, 132.194, 140.614], [1, 249.30499999999998, 280.245, 132.194, 140.614], [1, 291.55, 311.78, 132.194, 140.614], [1, 322.49, 343.315, 132.194, 140.614], [1, 354.025, 374.84999999999997, 132.194, 140.614], [1, 63.665, 90.44, 142.298, 150.718], [1, 165.41, 177.31, 142.298, 151.56], [1, 190.995, 211.82, 142.298, 150.718], [1, 223.125, 243.95, 142.298, 150.718], [1, 254.065, 280.245, 142.298, 150.718], [1, 291.55, 311.78, 142.298, 150.718], [1, 322.49, 343.315, 142.298, 150.718], [1, 354.025, 374.84999999999997, 142.298, 150.718], [1, 63.665, 85.085, 152.402, 160.822], [1, 165.41, 177.31, 152.402, 161.664], [1, 223.125, 243.95, 152.402, 160.822], [1, 291.55, 311.78, 152.402, 160.822], [1, 354.025, 374.84999999999997, 152.402, 160.822], [1, 63.665, 121.975, 162.506, 170.926], [1, 165.41, 177.31, 162.506, 171.768], [1, 185.64, 211.82, 162.506, 170.926], [1, 218.36499999999998, 243.95, 162.506, 170.926], [1, 254.065, 280.245, 162.506, 170.926], [1, 285.59999999999997, 311.78, 162.506, 170.926], [1, 317.72999999999996, 343.315, 162.506, 170.926], [1, 349.265, 374.84999999999997, 162.506, 170.926], [1, 63.665, 138.04, 172.60999999999999, 181.03], [1, 165.41, 177.31, 172.60999999999999, 181.87199999999999], [1, 185.64, 211.82, 172.60999999999999, 181.03], [1, 218.36499999999998, 243.95, 172.60999999999999, 181.03], [1, 254.065, 280.245, 172.60999999999999, 181.03], [1, 285.59999999999997, 311.78, 172.60999999999999, 181.03], [1, 317.72999999999996, 343.315, 172.60999999999999, 181.03], [1, 349.265, 374.84999999999997, 172.60999999999999, 181.03], [1, 63.665, 95.19999999999999, 182.714, 191.134], [1, 154.7, 178.5, 182.714, 191.976], [1, 223.125, 243.95, 182.714, 191.134], [1, 291.55, 311.78, 182.714, 191.134], [1, 322.49, 343.315, 182.714, 191.134], [1, 354.025, 374.84999999999997, 182.714, 191.134], [1, 63.665, 116.02499999999999, 192.81799999999998, 201.238], [1, 165.41, 177.31, 192.81799999999998, 202.07999999999998], [1, 218.36499999999998, 243.95, 192.81799999999998, 201.238], [1, 285.59999999999997, 311.78, 192.81799999999998, 201.238], [1, 317.72999999999996, 343.315, 192.81799999999998, 201.238], [1, 349.265, 374.84999999999997, 192.81799999999998, 201.238], [1, 63.665, 95.19999999999999, 202.922, 211.34199999999998], [1, 165.41, 177.31, 202.922, 212.184], [1, 190.995, 211.82, 202.922, 211.34199999999998], [1, 223.125, 243.95, 202.922, 211.34199999999998], [1, 254.065, 280.245, 202.922, 211.34199999999998], [1, 291.55, 311.78, 202.922, 211.34199999999998], [1, 63.665, 79.72999999999999, 213.02599999999998, 221.446], [1, 154.7, 178.5, 213.02599999999998, 222.28799999999998], [1, 190.995, 211.82, 213.02599999999998, 221.446], [1, 223.125, 243.95, 213.02599999999998, 221.446], [1, 254.065, 280.245, 213.02599999999998, 221.446], [1, 291.55, 311.78, 213.02599999999998, 221.446], [1, 322.49, 343.315, 213.02599999999998, 221.446], [1, 354.025, 374.84999999999997, 213.02599999999998, 221.446], [1, 63.665, 116.02499999999999, 223.13, 231.54999999999998], [1, 154.7, 178.5, 223.13, 232.392], [1, 190.995, 211.82, 223.13, 231.54999999999998], [1, 223.125, 243.95, 223.13, 231.54999999999998], [1, 254.065, 280.245, 223.13, 231.54999999999998], [1, 291.55, 311.78, 223.13, 231.54999999999998], [1, 322.49, 343.315, 223.13, 231.54999999999998], [1, 354.025, 374.84999999999997, 223.13, 231.54999999999998], [1, 63.665, 95.19999999999999, 233.23399999999998, 241.654], [1, 154.7, 178.5, 233.23399999999998, 242.49599999999998], [1, 190.995, 211.82, 233.23399999999998, 241.654], [1, 223.125, 243.95, 233.23399999999998, 241.654], [1, 254.065, 280.245, 233.23399999999998, 241.654], [1, 291.55, 311.78, 233.23399999999998, 241.654], [1, 322.49, 343.315, 233.23399999999998, 241.654], [1, 354.025, 374.84999999999997, 233.23399999999998, 241.654], [1, 63.665, 95.19999999999999, 243.338, 251.75799999999998], [1, 154.7, 178.5, 243.338, 252.6], [1, 190.995, 211.82, 243.338, 251.75799999999998], [1, 223.125, 243.95, 243.338, 251.75799999999998], [1, 254.065, 280.245, 243.338, 251.75799999999998], [1, 291.55, 311.78, 243.338, 251.75799999999998], [1, 322.49, 343.315, 243.338, 251.75799999999998], [1, 354.025, 374.84999999999997, 243.338, 251.75799999999998], [1, 63.665, 95.19999999999999, 253.44199999999998, 261.86199999999997], [1, 154.7, 178.5, 253.44199999999998, 262.704], [1, 190.995, 211.82, 253.44199999999998, 261.86199999999997], [1, 223.125, 243.95, 253.44199999999998, 261.86199999999997], [1, 254.065, 280.245, 253.44199999999998, 261.86199999999997], [1, 291.55, 311.78, 253.44199999999998, 261.86199999999997], [1, 322.49, 343.315, 253.44199999999998, 261.86199999999997], [1, 354.025, 374.84999999999997, 253.44199999999998, 261.86199999999997], [1, 63.665, 180.285, 264.388, 272.808], [1, 223.125, 243.95, 264.388, 272.808], [1, 291.55, 311.78, 264.388, 272.808], [1, 322.49, 343.315, 264.388, 272.808], [1, 354.025, 374.84999999999997, 264.388, 272.808], [1, 63.665, 178.5, 274.492, 282.912], [1, 223.125, 243.95, 274.492, 282.912], [1, 291.55, 311.78, 274.492, 282.912], [1, 322.49, 343.315, 274.492, 282.912], [1, 354.025, 374.84999999999997, 274.492, 282.912], [1, 63.665, 79.72999999999999, 284.596, 293.858], [1, 165.41, 177.31, 284.596, 293.858], [1, 223.125, 243.95, 284.596, 293.858], [1, 291.55, 311.78, 284.596, 293.858], [1, 322.49, 343.315, 284.596, 293.858], [1, 354.025, 374.84999999999997, 284.596, 293.858], [1, 63.665, 126.14, 295.542, 303.962], [1, 154.7, 178.5, 295.542, 304.804], [1, 223.125, 243.95, 295.542, 303.962], [1, 291.55, 311.78, 295.542, 303.962], [1, 322.49, 343.315, 295.542, 303.962], [1, 354.025, 374.84999999999997, 295.542, 303.962], [1, 63.665, 95.19999999999999, 305.646, 314.066], [1, 165.41, 177.31, 305.646, 314.908], [1, 190.995, 211.82, 305.646, 314.066], [1, 223.125, 243.95, 305.646, 314.066], [1, 254.065, 280.245, 305.646, 314.066], [1, 291.55, 311.78, 305.646, 314.066], [1, 322.49, 343.315, 305.646, 314.066], [1, 354.025, 374.84999999999997, 305.646, 314.066], [1, 63.665, 83.895, 315.75, 324.17], [1, 165.41, 177.31, 315.75, 325.012], [1, 223.125, 243.95, 315.75, 324.17], [1, 291.55, 311.78, 315.75, 324.17], [1, 322.49, 343.315, 315.75, 324.17], [1, 354.025, 374.84999999999997, 315.75, 324.17], [1, 63.665, 116.02499999999999, 325.854, 334.274], [1, 165.41, 177.31, 325.854, 335.116], [1, 218.36499999999998, 243.95, 325.854, 334.274], [1, 285.59999999999997, 311.78, 325.854, 334.274], [1, 317.72999999999996, 343.315, 325.854, 334.274], [1, 349.265, 374.84999999999997, 325.854, 334.274], [1, 63.665, 131.495, 336.8, 345.21999999999997], [1, 165.41, 177.31, 336.8, 346.062], [1, 218.36499999999998, 243.95, 336.8, 345.21999999999997], [1, 285.59999999999997, 311.78, 336.8, 345.21999999999997], [1, 317.72999999999996, 343.315, 336.8, 345.21999999999997], [1, 349.265, 374.84999999999997, 336.8, 345.21999999999997], [1, 63.665, 79.72999999999999, 346.904, 355.324], [1, 154.7, 178.5, 346.904, 356.166], [1, 223.125, 243.95, 346.904, 355.324], [1, 291.55, 311.78, 346.904, 355.324], [1, 322.49, 343.315, 346.904, 355.324], [1, 354.025, 374.84999999999997, 346.904, 355.324], [1, 63.665, 79.72999999999999, 357.84999999999997, 366.27], [1, 144.58499999999998, 178.5, 357.84999999999997, 367.11199999999997], [1, 185.64, 211.82, 357.84999999999997, 366.27], [1, 218.36499999999998, 243.95, 357.84999999999997, 366.27], [1, 254.065, 280.245, 357.84999999999997, 366.27], [1, 285.59999999999997, 311.78, 357.84999999999997, 366.27], [1, 63.665, 95.19999999999999, 367.954, 376.37399999999997], [1, 144.58499999999998, 178.5, 367.954, 377.216], [1, 218.36499999999998, 243.95, 367.954, 376.37399999999997], [1, 285.59999999999997, 311.78, 367.954, 376.37399999999997], [1, 142.79999999999998, 149.94, 399.95, 408.37], [1, 153.51, 182.665, 403.318, 412.58], [1, 202.29999999999998, 220.74499999999998, 404.15999999999997, 412.58], [1, 354.025, 376.03999999999996, 405.844, 415.106], [1, 330.82, 365.33, 433.63, 442.05], [1, 342.125, 362.95, 511.094, 520.356], [1, 421.26, 444.465, 478.256, 486.676], [1, 330.82, 340.935, 516.9879999999999, 524.566], [1, 415.905, 439.10999999999996, 591.084, 599.504], [1, 58.309999999999995, 93.41499999999999, 601.188, 613.818], [1, 55.335, 187.42499999999998, 627.29, 637.394], [1, 55.335, 219.55499999999998, 637.394, 647.4979999999999], [1, 55.335, 334.98499999999996, 647.4979999999999, 657.602], [1, 55.335, 257.03999999999996, 657.602, 667.706], [1, 55.335, 319.515, 667.706, 677.81], [1, 325.465, 441.48999999999995, 684.5459999999999, 698.018], [1, 325.465, 447.44, 700.544, 718.226], [1, 64.855, 103.53, 748.538, 756.116]]
2026-08-10 11:09:48,111 INFO     29 [qwen-vl-text] ═══ DONE ═══ 197 positions, pages=1, time=63.7s
2026-08-10 11:09:48,111 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:09:48,119 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:09:48,120 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:09:48,120 INFO     29 [qwen-vl-text] positions(126): [[2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:09:48,120 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [125, 1]
2026-08-10 11:09:48,288 INFO     29 [qwen-vl-text] page=2, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:09:48,502 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:09:48,504 INFO     29 [qwen-vl-text] LLM extraction start, text_len=803
2026-08-10 11:09:48,504 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:09:48,506 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 267, \"bbox_end\": 392, \"encounter_dates\": [\"2026-01-15\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能报告单\n姓名：\n性别：女\n出生日期：1984/11/02\n年龄：41岁\n住院号：\n测试号：\n身高：160 cm\n体重：48 kg\n身份证号：\n预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n26/1/15\n26/1/15\n测试时间\n9:51:00上午\n10:14:56上午\nFVC\n[L]\n3.13\n3.15\n100.5\n3.25\n103.9\n3.3\nFEV 1\n[L]\n2.70\n1.99\n73.9\n2.26\n83.8\n13.4\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.3\n69.40\n82.6\n9.7\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.8\n69.40\n85.4\n9.7\nPEF\n[L/s]\n6.46\n6.33\n98.0\n7.25\n112.2\n14.5\nMEF 75\n[L/s]\n5.73\n3.01\n52.6\n3.73\n65.1\n23.8\nMEF 50\n[L/s]\n4.06\n1.25\n30.9\n1.67\n41.2\n33.3\nMEF 25\n[L/s]\n1.77\n0.46\n26.3\n0.59\n33.6\n27.7\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.0\n1.46\n41.3\n37.6\nFET\n[s]\n8.73\n4.94\n-43.4\nV backextrapolation ex [L]\n0.06\n0.07\n20.1\nV backextrapol. % FVC [%]\n1.86\n2.17\n16.3\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V In\n医生意见：\n支气管舒张试验阳性。\n（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。\nFEV1较基线增加大于12 %，且绝对值增加大于200 ml。\n审核医生：孙帅森\n检测技师：朱龙华\n肺功能报告单",
    "role": "user"
  }
]
2026-08-10 11:09:48,809 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:09:48.807+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:09:55,921 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:09:55,921 INFO     29 [qwen-vl-text] LLM output (len=1115):
{
  "exam_date": "2026-01-15",
  "report_date": "2026-01-15",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n26/1/15\n26/1/15\n测试时间\n9:51:00上午\n10:14:56上午\nFVC\n[L]\n3.13\n3.15\n100.5\n3.25\n103.9\n3.3\nFEV 1\n[L]\n2.70\n1.99\n73.9\n2.26\n83.8\n13.4\nFEV 1 % FVC\n[%]\n83.98\n63.25\n75.3\n69.40\n82.6\n9.7\nFEV 1 % VC MAX\n[%]\n81.31\n63.25\n77.8\n69.40\n85.4\n9.7\nPEF\n[L/s]\n6.46\n6.33\n98.0\n7.25\n112.2\n14.5\nMEF 75\n[L/s]\n5.73\n3.01\n52.6\n3.73\n65.1\n23.8\nMEF 50\n[L/s]\n4.06\n1.25\n30.9\n1.67\n41.2\n33.3\nMEF 25\n[L/s]\n1.77\n0.46\n26.3\n0.59\n33.6\n27.7\nMMEF 75/25\n[L/s]\n3.53\n1.06\n30.0\n1.46\n41.3\n37.6\nFET\n[s]\n8.73\n4.94\n-43.4\nV backextrapolation ex [L]\n0.06\n0.07\n20.1\nV backextrapol. % FVC [%]\n1.86\n2.17\n16.3\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V In",
  "conclusion": "支气管舒张试验阳性。\n（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。\nFEV1较基线增加大于12 %，且绝对值增加大于200 ml。",
  "physician": "朱龙华",
  "reviewer": "孙帅森"
}
2026-08-10 11:09:55,923 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=738007, prompt_len=1785
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共125行）
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/11/02", "年龄：41岁", "住院号：", "测试号：", "身高：160 cm", "体重：48 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "26/1/15", "26/1/15", "测试时间", "9:51:00上午", "10:14:56上午", "FVC", "[L]", "3.13", "3.15", "100.5", "3.25", "103.9", "3.3", "FEV 1", "[L]", "2.70", "1.99", "73.9", "2.26", "83.8", "13.4", "FEV 1 % FVC", "[%]", "83.98", "63.25", "75.3", "69.40", "82.6", "9.7", "FEV 1 % VC MAX", "[%]", "81.31", "63.25", "77.8", "69.40", "85.4", "9.7", "PEF", "[L/s]", "6.46", "6.33", "98.0", "7.25", "112.2", "14.5", "MEF 75", "[L/s]", "5.73", "3.01", "52.6", "3.73", "65.1", "23.8", "MEF 50", "[L/s]", "4.06", "1.25", "30.9", "1.67", "41.2", "33.3", "MEF 25", "[L/s]", "1.77", "0.46", "26.3", "0.59", "33.6", "27.7", "MMEF 75/25", "[L/s]", "3.53", "1.06", "30.0", "1.46", "41.3", "37.6", "FET", "[s]", "8.73", "4.94", "-43.4", "V backextrapolation ex [L]", "0.06", "0.07", "20.1", "V backextrapol. % FVC [%]", "1.86", "2.17", "16.3", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "审核医生：孙帅森", "检测技师：朱龙华"]

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
2026-08-10 11:10:29,305 INFO     29 [qwen-vl-text] coord API raw response (len=6500):
[
	{"text": "肺功能报告单", "bbox": [410, 81, 555, 102]},
	{"text": "姓名：", "bbox": [91, 104, 140, 117]},
	{"text": "性别：", "bbox": [483, 102, 535, 117]},
	{"text": "女", "bbox": [677, 104, 697, 117]},
	{"text": "出生日期：", "bbox": [91, 117, 178, 130]},
	{"text": "1984/11/02", "bbox": [278, 117, 375, 127]},
	{"text": "年龄：", "bbox": [483, 117, 535, 130]},
	{"text": "41岁", "bbox": [677, 118, 727, 131]},
	{"text": "住院号：", "bbox": [91, 131, 158, 144]},
	{"text": "测试号：", "bbox": [483, 131, 555, 144]},
	{"text": "身高：", "bbox": [91, 145, 140, 158]},
	{"text": "160 cm", "bbox": [278, 147, 345, 158]},
	{"text": "体重：", "bbox": [483, 145, 535, 158]},
	{"text": "48 kg", "bbox": [677, 147, 728, 161]},
	{"text": "身份证号：", "bbox": [91, 159, 178, 172]},
	{"text": "预计", "bbox": [344, 179, 380, 193]},
	{"text": "实1 %(实1/预)", "bbox": [464, 179, 578, 194]},
	{"text": "实2 %(实2/预)", "bbox": [661, 180, 777, 195]},
	{"text": "变异率", "bbox": [807, 180, 860, 194]},
	{"text": "测试日期", "bbox": [97, 195, 169, 209]},
	{"text": "26/1/15", "bbox": [431, 196, 492, 209]},
	{"text": "26/1/15", "bbox": [628, 196, 690, 209]},
	{"text": "测试时间", "bbox": [97, 210, 169, 224]},
	{"text": "9:51:00上午", "bbox": [395, 211, 492, 225]},
	{"text": "10:14:56上午", "bbox": [587, 211, 690, 225]},
	{"text": "FVC", "bbox": [97, 244, 134, 257]},
	{"text": "[L]", "bbox": [297, 245, 320, 259]},
	{"text": "3.13", "bbox": [344, 245, 380, 258]},
	{"text": "3.15", "bbox": [455, 245, 492, 258]},
	{"text": "100.5", "bbox": [532, 245, 577, 258]},
	{"text": "3.25", "bbox": [654, 245, 690, 258]},
	{"text": "103.9", "bbox": [732, 245, 777, 258]},
	{"text": "3.3", "bbox": [837, 245, 862, 258]},
	{"text": "FEV 1", "bbox": [97, 260, 146, 273]},
	{"text": "[L]", "bbox": [297, 261, 320, 275]},
	{"text": "2.70", "bbox": [344, 261, 380, 274]},
	{"text": "1.99", "bbox": [455, 261, 492, 274]},
	{"text": "73.9", "bbox": [541, 261, 577, 274]},
	{"text": "2.26", "bbox": [654, 261, 690, 274]},
	{"text": "83.8", "bbox": [741, 261, 777, 274]},
	{"text": "13.4", "bbox": [829, 261, 862, 274]},
	{"text": "FEV 1 % FVC", "bbox": [97, 276, 208, 289]},
	{"text": "[%]", "bbox": [292, 277, 320, 290]},
	{"text": "83.98", "bbox": [334, 277, 380, 290]},
	{"text": "63.25", "bbox": [445, 277, 492, 290]},
	{"text": "75.3", "bbox": [541, 277, 577, 290]},
	{"text": "69.40", "bbox": [644, 277, 690, 290]},
	{"text": "82.6", "bbox": [741, 277, 777, 290]},
	{"text": "9.7", "bbox": [837, 277, 862, 290]},
	{"text": "FEV 1 % VC MAX", "bbox": [97, 291, 242, 304]},
	{"text": "[%]", "bbox": [292, 292, 320, 306]},
	{"text": "81.31", "bbox": [334, 292, 380, 305]},
	{"text": "63.25", "bbox": [445, 292, 492, 305]},
	{"text": "77.8", "bbox": [541, 292, 577, 305]},
	{"text": "69.40", "bbox": [644, 292, 690, 305]},
	{"text": "85.4", "bbox": [741, 292, 777, 305]},
	{"text": "9.7", "bbox": [837, 292, 862, 305]},
	{"text": "PEF", "bbox": [97, 307, 134, 320]},
	{"text": "[L/s]", "bbox": [282, 308, 320, 322]},
	{"text": "6.46", "bbox": [344, 308, 380, 321]},
	{"text": "6.33", "bbox": [455, 308, 492, 321]},
	{"text": "98.0", "bbox": [541, 308, 577, 321]},
	{"text": "7.25", "bbox": [654, 308, 690, 321]},
	{"text": "112.2", "bbox": [732, 308, 777, 321]},
	{"text": "14.5", "bbox": [829, 308, 862, 321]},
	{"text": "MEF 75", "bbox": [97, 323, 160, 336]},
	{"text": "[L/s]", "bbox": [282, 324, 320, 338]},
	{"text": "5.73", "bbox": [344, 324, 380, 337]},
	{"text": "3.01", "bbox": [455, 324, 492, 337]},
	{"text": "52.6", "bbox": [541, 324, 577, 337]},
	{"text": "3.73", "bbox": [654, 324, 690, 337]},
	{"text": "65.1", "bbox": [741, 324, 777, 337]},
	{"text": "23.8", "bbox": [829, 324, 862, 337]},
	{"text": "MEF 50", "bbox": [97, 339, 160, 352]},
	{"text": "[L/s]", "bbox": [282, 340, 320, 354]},
	{"text": "4.06", "bbox": [344, 340, 380, 353]},
	{"text": "1.25", "bbox": [455, 340, 492, 353]},
	{"text": "30.9", "bbox": [541, 340, 577, 353]},
	{"text": "1.67", "bbox": [654, 340, 690, 353]},
	{"text": "41.2", "bbox": [741, 340, 777, 353]},
	{"text": "33.3", "bbox": [829, 340, 862, 353]},
	{"text": "MEF 25", "bbox": [97, 355, 160, 368]},
	{"text": "[L/s]", "bbox": [282, 356, 320, 370]},
	{"text": "1.77", "bbox": [344, 356, 380, 369]},
	{"text": "0.46", "bbox": [455, 356, 492, 369]},
	{"text": "26.3", "bbox": [541, 356, 577, 369]},
	{"text": "0.59", "bbox": [654, 356, 690, 369]},
	{"text": "33.6", "bbox": [741, 356, 777, 369]},
	{"text": "27.7", "bbox": [829, 356, 862, 369]},
	{"text": "MMEF 75/25", "bbox": [97, 370, 200, 383]},
	{"text": "[L/s]", "bbox": [282, 371, 320, 385]},
	{"text": "3.53", "bbox": [344, 371, 380, 384]},
	{"text": "1.06", "bbox": [455, 371, 492, 384]},
	{"text": "30.0", "bbox": [541, 371, 577, 384]},
	{"text": "1.46", "bbox": [654, 371, 690, 384]},
	{"text": "41.3", "bbox": [741, 371, 777, 384]},
	{"text": "37.6", "bbox": [829, 371, 862, 384]},
	{"text": "FET", "bbox": [97, 386, 134, 399]},
	{"text": "[s]", "bbox": [297, 387, 320, 401]},
	{"text": "8.73", "bbox": [455, 387, 492, 400]},
	{"text": "4.94", "bbox": [654, 387, 690, 400]},
	{"text": "-43.4", "bbox": [821, 387, 862, 400]},
	{"text": "V backextrapolation ex [L]", "bbox": [97, 401, 320, 415]},
	{"text": "0.06", "bbox": [455, 402, 492, 415]},
	{"text": "0.07", "bbox": [654, 402, 690, 415]},
	{"text": "20.1", "bbox": [829, 402, 862, 415]},
	{"text": "V backextrapol. % FVC [%]", "bbox": [97, 417, 320, 431]},
	{"text": "1.86", "bbox": [455, 417, 492, 431]},
	{"text": "2.17", "bbox": [654, 417, 690, 431]},
	{"text": "16.3", "bbox": [829, 417, 862, 431]},
	{"text": "Flow [L/s]", "bbox": [150, 501, 200, 512]},
	{"text": "F/V ex", "bbox": [589, 502, 622, 511]},
	{"text": "10", "bbox": [134, 519, 148, 528]},
	{"text": "5", "bbox": [138, 545, 146, 554]},
	{"text": "0", "bbox": [138, 572, 146, 581]},
	{"text": "1", "bbox": [231, 582, 238, 590]},
	{"text": "2", "bbox": [316, 582, 324, 590]},
	{"text": "3", "bbox": [402, 582, 409, 590]},
	{"text": "4", "bbox": [487, 582, 495, 590]},
	{"text": "5", "bbox": [573, 582, 581, 590]},
	{"text": "6", "bbox": [661, 582, 669, 590]},
	{"text": "7", "bbox": [747, 582, 755, 590]},
	{"text": "10", "bbox": [134, 626, 148, 635]},
	{"text": "F/V In", "bbox": [593, 644, 622, 653]},
	{"text": "医生意见：", "bbox": [93, 664, 197, 681]},
	{"text": "支气管舒张试验阳性。", "bbox": [93, 684, 264, 697]},
	{"text": "（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。", "bbox": [93, 697, 526, 710]},
	{"text": "FEV1较基线增加大于12 %，且绝对值增加大于200 ml。", "bbox": [93, 709, 519, 722]},
	{"text": "审核医生：孙帅森", "bbox": [649, 791, 784, 806]},
	{"text": "检测技师：朱龙华", "bbox": [645, 812, 806, 838]}
]
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord API: raw_items=130, valid_items=130, elapsed=33.4s
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[410, 81, 555, 102]
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[91, 104, 140, 117]
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[483, 102, 535, 117]
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord item[3]: text=女, bbox=[677, 104, 697, 117]
2026-08-10 11:10:29,306 INFO     29 [qwen-vl-text] coord item[4]: text=出生日期：, bbox=[91, 117, 178, 130]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[5]: text=1984/11/02, bbox=[278, 117, 375, 127]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：, bbox=[483, 117, 535, 130]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[7]: text=41岁, bbox=[677, 118, 727, 131]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：, bbox=[91, 131, 158, 144]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[9]: text=测试号：, bbox=[483, 131, 555, 144]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[10]: text=身高：, bbox=[91, 145, 140, 158]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[11]: text=160 cm, bbox=[278, 147, 345, 158]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[12]: text=体重：, bbox=[483, 145, 535, 158]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[13]: text=48 kg, bbox=[677, 147, 728, 161]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[14]: text=身份证号：, bbox=[91, 159, 178, 172]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[15]: text=预计, bbox=[344, 179, 380, 193]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[16]: text=实1 %(实1/预), bbox=[464, 179, 578, 194]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[17]: text=实2 %(实2/预), bbox=[661, 180, 777, 195]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[18]: text=变异率, bbox=[807, 180, 860, 194]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[19]: text=测试日期, bbox=[97, 195, 169, 209]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[20]: text=26/1/15, bbox=[431, 196, 492, 209]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[21]: text=26/1/15, bbox=[628, 196, 690, 209]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[22]: text=测试时间, bbox=[97, 210, 169, 224]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[23]: text=9:51:00上午, bbox=[395, 211, 492, 225]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[24]: text=10:14:56上午, bbox=[587, 211, 690, 225]
2026-08-10 11:10:29,307 INFO     29 [qwen-vl-text] coord item[25]: text=FVC, bbox=[97, 244, 134, 257]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[26]: text=[L], bbox=[297, 245, 320, 259]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[27]: text=3.13, bbox=[344, 245, 380, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[28]: text=3.15, bbox=[455, 245, 492, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[29]: text=100.5, bbox=[532, 245, 577, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[30]: text=3.25, bbox=[654, 245, 690, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[31]: text=103.9, bbox=[732, 245, 777, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[32]: text=3.3, bbox=[837, 245, 862, 258]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[33]: text=FEV 1, bbox=[97, 260, 146, 273]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[34]: text=[L], bbox=[297, 261, 320, 275]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[35]: text=2.70, bbox=[344, 261, 380, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[36]: text=1.99, bbox=[455, 261, 492, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[37]: text=73.9, bbox=[541, 261, 577, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[38]: text=2.26, bbox=[654, 261, 690, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[39]: text=83.8, bbox=[741, 261, 777, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[40]: text=13.4, bbox=[829, 261, 862, 274]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[41]: text=FEV 1 % FVC, bbox=[97, 276, 208, 289]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[42]: text=[%], bbox=[292, 277, 320, 290]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[43]: text=83.98, bbox=[334, 277, 380, 290]
2026-08-10 11:10:29,308 INFO     29 [qwen-vl-text] coord item[44]: text=63.25, bbox=[445, 277, 492, 290]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[45]: text=75.3, bbox=[541, 277, 577, 290]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[46]: text=69.40, bbox=[644, 277, 690, 290]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[47]: text=82.6, bbox=[741, 277, 777, 290]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[48]: text=9.7, bbox=[837, 277, 862, 290]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[49]: text=FEV 1 % VC MAX, bbox=[97, 291, 242, 304]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[50]: text=[%], bbox=[292, 292, 320, 306]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[51]: text=81.31, bbox=[334, 292, 380, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[52]: text=63.25, bbox=[445, 292, 492, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[53]: text=77.8, bbox=[541, 292, 577, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[54]: text=69.40, bbox=[644, 292, 690, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[55]: text=85.4, bbox=[741, 292, 777, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[56]: text=9.7, bbox=[837, 292, 862, 305]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[57]: text=PEF, bbox=[97, 307, 134, 320]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[58]: text=[L/s], bbox=[282, 308, 320, 322]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[59]: text=6.46, bbox=[344, 308, 380, 321]
2026-08-10 11:10:29,309 INFO     29 [qwen-vl-text] coord item[60]: text=6.33, bbox=[455, 308, 492, 321]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[61]: text=98.0, bbox=[541, 308, 577, 321]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[62]: text=7.25, bbox=[654, 308, 690, 321]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[63]: text=112.2, bbox=[732, 308, 777, 321]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[64]: text=14.5, bbox=[829, 308, 862, 321]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[65]: text=MEF 75, bbox=[97, 323, 160, 336]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[66]: text=[L/s], bbox=[282, 324, 320, 338]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[67]: text=5.73, bbox=[344, 324, 380, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[68]: text=3.01, bbox=[455, 324, 492, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[69]: text=52.6, bbox=[541, 324, 577, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[70]: text=3.73, bbox=[654, 324, 690, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[71]: text=65.1, bbox=[741, 324, 777, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[72]: text=23.8, bbox=[829, 324, 862, 337]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[73]: text=MEF 50, bbox=[97, 339, 160, 352]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[74]: text=[L/s], bbox=[282, 340, 320, 354]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[75]: text=4.06, bbox=[344, 340, 380, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[76]: text=1.25, bbox=[455, 340, 492, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[77]: text=30.9, bbox=[541, 340, 577, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[78]: text=1.67, bbox=[654, 340, 690, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[79]: text=41.2, bbox=[741, 340, 777, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[80]: text=33.3, bbox=[829, 340, 862, 353]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[81]: text=MEF 25, bbox=[97, 355, 160, 368]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[82]: text=[L/s], bbox=[282, 356, 320, 370]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[83]: text=1.77, bbox=[344, 356, 380, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[84]: text=0.46, bbox=[455, 356, 492, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[85]: text=26.3, bbox=[541, 356, 577, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[86]: text=0.59, bbox=[654, 356, 690, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[87]: text=33.6, bbox=[741, 356, 777, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[88]: text=27.7, bbox=[829, 356, 862, 369]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[89]: text=MMEF 75/25, bbox=[97, 370, 200, 383]
2026-08-10 11:10:29,310 INFO     29 [qwen-vl-text] coord item[90]: text=[L/s], bbox=[282, 371, 320, 385]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[91]: text=3.53, bbox=[344, 371, 380, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[92]: text=1.06, bbox=[455, 371, 492, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[93]: text=30.0, bbox=[541, 371, 577, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[94]: text=1.46, bbox=[654, 371, 690, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[95]: text=41.3, bbox=[741, 371, 777, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[96]: text=37.6, bbox=[829, 371, 862, 384]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[97]: text=FET, bbox=[97, 386, 134, 399]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[98]: text=[s], bbox=[297, 387, 320, 401]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[99]: text=8.73, bbox=[455, 387, 492, 400]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[100]: text=4.94, bbox=[654, 387, 690, 400]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[101]: text=-43.4, bbox=[821, 387, 862, 400]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[102]: text=V backextrapolation ex [L], bbox=[97, 401, 320, 415]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[103]: text=0.06, bbox=[455, 402, 492, 415]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[104]: text=0.07, bbox=[654, 402, 690, 415]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[105]: text=20.1, bbox=[829, 402, 862, 415]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[106]: text=V backextrapol. % FVC [%], bbox=[97, 417, 320, 431]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[107]: text=1.86, bbox=[455, 417, 492, 431]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[108]: text=2.17, bbox=[654, 417, 690, 431]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[109]: text=16.3, bbox=[829, 417, 862, 431]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[110]: text=Flow [L/s], bbox=[150, 501, 200, 512]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[111]: text=F/V ex, bbox=[589, 502, 622, 511]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[112]: text=10, bbox=[134, 519, 148, 528]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[113]: text=5, bbox=[138, 545, 146, 554]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[114]: text=0, bbox=[138, 572, 146, 581]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[115]: text=1, bbox=[231, 582, 238, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[116]: text=2, bbox=[316, 582, 324, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[117]: text=3, bbox=[402, 582, 409, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[118]: text=4, bbox=[487, 582, 495, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[119]: text=5, bbox=[573, 582, 581, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[120]: text=6, bbox=[661, 582, 669, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[121]: text=7, bbox=[747, 582, 755, 590]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[122]: text=10, bbox=[134, 626, 148, 635]
2026-08-10 11:10:29,311 INFO     29 [qwen-vl-text] coord item[123]: text=F/V In, bbox=[593, 644, 622, 653]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[124]: text=医生意见：, bbox=[93, 664, 197, 681]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[125]: text=支气管舒张试验阳性。, bbox=[93, 684, 264, 697]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[126]: text=（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。, bbox=[93, 697, 526, 710]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[127]: text=FEV1较基线增加大于12 %，且绝对值增加大于200 ml。, bbox=[93, 709, 519, 722]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[128]: text=审核医生：孙帅森, bbox=[649, 791, 784, 806]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] coord item[129]: text=检测技师：朱龙华, bbox=[645, 812, 806, 838]
2026-08-10 11:10:29,312 INFO     29 [qwen-vl-text] page=2 — 125/125 coords, api_time=33.4s
2026-08-10 11:10:29,315 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1165294, prompt_len=621
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["肺功能报告单"]

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
2026-08-10 11:10:30,818 INFO     29 [qwen-vl-text] coord API raw response (len=63):
```json
[
	{"text": "肺功能报告单", "bbox": [407, 59, 549, 77]}
]
```
2026-08-10 11:10:30,818 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=1.5s
2026-08-10 11:10:30,818 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[407, 59, 549, 77]
2026-08-10 11:10:30,819 INFO     29 [qwen-vl-text] page=3 — 1/1 coords, api_time=1.5s
2026-08-10 11:10:30,819 INFO     29 [qwen-vl-text] new_positions (126):
[[2, 243.95, 330.22499999999997, 68.202, 85.884], [2, 54.144999999999996, 83.3, 87.568, 98.514], [2, 287.385, 318.325, 85.884, 98.514], [2, 402.815, 414.715, 87.568, 98.514], [2, 54.144999999999996, 105.91, 98.514, 109.46], [2, 165.41, 223.125, 98.514, 106.934], [2, 287.385, 318.325, 98.514, 109.46], [2, 402.815, 432.565, 99.356, 110.30199999999999], [2, 54.144999999999996, 94.00999999999999, 110.30199999999999, 121.24799999999999], [2, 287.385, 330.22499999999997, 110.30199999999999, 121.24799999999999], [2, 54.144999999999996, 83.3, 122.08999999999999, 133.036], [2, 165.41, 205.27499999999998, 123.774, 133.036], [2, 287.385, 318.325, 122.08999999999999, 133.036], [2, 402.815, 433.15999999999997, 123.774, 135.56199999999998], [2, 54.144999999999996, 105.91, 133.878, 144.82399999999998], [2, 204.67999999999998, 226.1, 150.718, 162.506], [2, 276.08, 343.90999999999997, 150.718, 163.34799999999998], [2, 393.29499999999996, 462.315, 151.56, 164.19], [2, 480.16499999999996, 511.7, 151.56, 163.34799999999998], [2, 57.714999999999996, 100.55499999999999, 164.19, 175.97799999999998], [2, 256.445, 292.74, 165.03199999999998, 175.97799999999998], [2, 373.65999999999997, 410.54999999999995, 165.03199999999998, 175.97799999999998], [2, 57.714999999999996, 100.55499999999999, 176.82, 188.608], [2, 235.02499999999998, 292.74, 177.662, 189.45], [2, 349.265, 410.54999999999995, 177.662, 189.45], [2, 57.714999999999996, 79.72999999999999, 205.44799999999998, 216.394], [2, 176.715, 190.39999999999998, 206.29, 218.078], [2, 204.67999999999998, 226.1, 206.29, 217.236], [2, 270.72499999999997, 292.74, 206.29, 217.236], [2, 316.53999999999996, 343.315, 206.29, 217.236], [2, 389.13, 410.54999999999995, 206.29, 217.236], [2, 435.53999999999996, 462.315, 206.29, 217.236], [2, 498.015, 512.89, 206.29, 217.236], [2, 57.714999999999996, 86.86999999999999, 218.92, 229.86599999999999], [2, 176.715, 190.39999999999998, 219.762, 231.54999999999998], [2, 204.67999999999998, 226.1, 219.762, 230.708], [2, 270.72499999999997, 292.74, 219.762, 230.708], [2, 321.895, 343.315, 219.762, 230.708], [2, 389.13, 410.54999999999995, 219.762, 230.708], [2, 440.895, 462.315, 219.762, 230.708], [2, 493.255, 512.89, 219.762, 230.708], [2, 57.714999999999996, 123.75999999999999, 232.392, 243.338], [2, 173.73999999999998, 190.39999999999998, 233.23399999999998, 244.17999999999998], [2, 198.73, 226.1, 233.23399999999998, 244.17999999999998], [2, 264.775, 292.74, 233.23399999999998, 244.17999999999998], [2, 321.895, 343.315, 233.23399999999998, 244.17999999999998], [2, 383.18, 410.54999999999995, 233.23399999999998, 244.17999999999998], [2, 440.895, 462.315, 233.23399999999998, 244.17999999999998], [2, 498.015, 512.89, 233.23399999999998, 244.17999999999998], [2, 57.714999999999996, 143.98999999999998, 245.022, 255.968], [2, 173.73999999999998, 190.39999999999998, 245.864, 257.652], [2, 198.73, 226.1, 245.864, 256.81], [2, 264.775, 292.74, 245.864, 256.81], [2, 321.895, 343.315, 245.864, 256.81], [2, 383.18, 410.54999999999995, 245.864, 256.81], [2, 440.895, 462.315, 245.864, 256.81], [2, 498.015, 512.89, 245.864, 256.81], [2, 57.714999999999996, 79.72999999999999, 258.49399999999997, 269.44], [2, 167.79, 190.39999999999998, 259.336, 271.12399999999997], [2, 204.67999999999998, 226.1, 259.336, 270.282], [2, 270.72499999999997, 292.74, 259.336, 270.282], [2, 321.895, 343.315, 259.336, 270.282], [2, 389.13, 410.54999999999995, 259.336, 270.282], [2, 435.53999999999996, 462.315, 259.336, 270.282], [2, 493.255, 512.89, 259.336, 270.282], [2, 57.714999999999996, 95.19999999999999, 271.966, 282.912], [2, 167.79, 190.39999999999998, 272.808, 284.596], [2, 204.67999999999998, 226.1, 272.808, 283.75399999999996], [2, 270.72499999999997, 292.74, 272.808, 283.75399999999996], [2, 321.895, 343.315, 272.808, 283.75399999999996], [2, 389.13, 410.54999999999995, 272.808, 283.75399999999996], [2, 440.895, 462.315, 272.808, 283.75399999999996], [2, 493.255, 512.89, 272.808, 283.75399999999996], [2, 57.714999999999996, 95.19999999999999, 285.438, 296.384], [2, 167.79, 190.39999999999998, 286.28, 298.068], [2, 204.67999999999998, 226.1, 286.28, 297.226], [2, 270.72499999999997, 292.74, 286.28, 297.226], [2, 321.895, 343.315, 286.28, 297.226], [2, 389.13, 410.54999999999995, 286.28, 297.226], [2, 440.895, 462.315, 286.28, 297.226], [2, 493.255, 512.89, 286.28, 297.226], [2, 57.714999999999996, 95.19999999999999, 298.90999999999997, 309.856], [2, 167.79, 190.39999999999998, 299.752, 311.53999999999996], [2, 204.67999999999998, 226.1, 299.752, 310.698], [2, 270.72499999999997, 292.74, 299.752, 310.698], [2, 321.895, 343.315, 299.752, 310.698], [2, 389.13, 410.54999999999995, 299.752, 310.698], [2, 440.895, 462.315, 299.752, 310.698], [2, 493.255, 512.89, 299.752, 310.698], [2, 57.714999999999996, 119.0, 311.53999999999996, 322.486], [2, 167.79, 190.39999999999998, 312.382, 324.17], [2, 204.67999999999998, 226.1, 312.382, 323.328], [2, 270.72499999999997, 292.74, 312.382, 323.328], [2, 321.895, 343.315, 312.382, 323.328], [2, 389.13, 410.54999999999995, 312.382, 323.328], [2, 440.895, 462.315, 312.382, 323.328], [2, 493.255, 512.89, 312.382, 323.328], [2, 57.714999999999996, 79.72999999999999, 325.012, 335.95799999999997], [2, 176.715, 190.39999999999998, 325.854, 337.642], [2, 270.72499999999997, 292.74, 325.854, 336.8], [2, 389.13, 410.54999999999995, 325.854, 336.8], [2, 488.495, 512.89, 325.854, 336.8], [2, 57.714999999999996, 190.39999999999998, 337.642, 349.43], [2, 270.72499999999997, 292.74, 338.484, 349.43], [2, 389.13, 410.54999999999995, 338.484, 349.43], [2, 493.255, 512.89, 338.484, 349.43], [2, 57.714999999999996, 190.39999999999998, 351.114, 362.902], [2, 270.72499999999997, 292.74, 351.114, 362.902], [2, 389.13, 410.54999999999995, 351.114, 362.902], [2, 493.255, 512.89, 351.114, 362.902], [2, 89.25, 119.0, 421.842, 431.104], [2, 350.455, 370.09, 422.68399999999997, 430.262], [2, 79.72999999999999, 88.06, 436.998, 444.57599999999996], [2, 82.11, 86.86999999999999, 458.89, 466.46799999999996], [2, 82.11, 86.86999999999999, 481.62399999999997, 489.202], [2, 137.445, 141.60999999999999, 490.044, 496.78], [2, 188.01999999999998, 192.78, 490.044, 496.78], [2, 239.19, 243.355, 490.044, 496.78], [2, 289.765, 294.525, 490.044, 496.78], [2, 340.935, 345.695, 490.044, 496.78], [2, 393.29499999999996, 398.055, 490.044, 496.78], [2, 444.465, 449.22499999999997, 490.044, 496.78], [2, 79.72999999999999, 88.06, 527.092, 534.67], [2, 352.835, 370.09, 542.2479999999999, 549.826], [2, 55.335, 117.21499999999999, 559.088, 573.4019999999999], [3, 242.165, 326.655, 49.678, 64.834]]
2026-08-10 11:10:30,820 INFO     29 [qwen-vl-text] ═══ DONE ═══ 126 positions, pages=2, time=42.7s
2026-08-10 11:10:30,820 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:10:30,830 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:10:30,830 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:10:30,830 INFO     29 [qwen-vl-text] positions(151): [[3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:10:30,831 INFO     29 [qwen-vl-text] page grouping: [3], lines per page: [151]
2026-08-10 11:10:31,045 INFO     29 [qwen-vl-text] page=3, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:10:31,047 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1052
2026-08-10 11:10:31,047 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:10:31,047 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 393, \"bbox_end\": 543, \"encounter_dates\": [\"2025-04-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "姓名：\n出生日期：1984/4/02\n门诊/住院/体检：\n身高：160 cm\n身份证号：\n性别：女\n年龄：41 岁\n测试号：\n体重：50 kg\n测试日期\n测试时间\n预计\n实测 % (实/预)\n25/4/11\n14:56:4\nVT\n[L]\n0.36\n0.41\n114.9\nBF\n[1/min]\n20.00\n20.79\n104.0\nMV\n[L/min]\n7.14\n8.54\n119.5\nERV\n[L]\n1.07\n1.07\n99.4\nVC MAX\n[L]\n3.19\n2.84\n88.9\nFVC\n[L]\n3.13\n2.84\n90.6\nFEV 1\n[L]\n2.70\n1.53\n56.9\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\nPEF\n[L/s]\n6.46\n4.56\n70.7\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\nFET\n[s]\n8.46\nV backextrapolation ex\n[L]\n0.03\nV backextrapol. % FVC\n[%]\n1.23\nMVV\n[L/min]\n101.93\n75.75\n74.3\nFEV 1*30\n[L/min]\n101.93\n46.03\n45.2\nRV-SB\n[L]\n1.55\n2.56\n164.9\nRV%TLC-SB\n[%]\n32.90\n47.52\n144.4\nTLC-SB\n[L]\n4.77\n5.39\n112.9\nFRC-SB\n[L]\n2.63\n3.31\n126.0\nFRC%TLC-SB\n[%]\n51.66\n61.42\n118.9\nDLCOc SB\n[mmol/min/kPa]\n8.34\n6.95\n83.4\nDLCO SB\n[mmol/min/kPa]\n8.34\n6.95\n83.4\n医生意见：\n1.中重度阻塞性通气功能障碍。\n检查质量：FVC：A级 。 FEV1：A级 。\n备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。\n2.最大自主分钟通气量（MVV）轻度下降。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n3.弥散功能在正常范围。4.残总比中度增高。\n审核医生：孙帅森\n检测技师：张青苹\n通气弥散B\n2025/4/11 15:18\n1/1",
    "role": "user"
  }
]
2026-08-10 11:10:31,050 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:10:31.049+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:10:31,054 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:10:31,054 INFO     29 [qwen-vl-text] LLM output (len=1404):
{
  "encounter_date": "2025-12-12",
  "chief_complaint": "BAIYUN V8",
  "present_illness": "自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。完成下流操作:1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。5、休息至少10分钟后,行12导联ECG检查。6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。",
  "past_history": null,
  "diagnosis": "1、支气管哮喘",
  "treatment_plan": [
    {
      "drug_name": "伯氟米松福莫特罗吸入气雾剂",
      "dosage": "2.0瓶",
      "frequency": "一天2次",
      "route": "吸入用药",
      "duration": "30天",
      "quantity": "1瓶"
    },
    {
      "drug_name": "孟鲁司特钠片(省采)",
      "dosage": "10.0mg",
      "frequency": "每日1次",
      "route": "口服",
      "duration": "30天",
      "quantity": "6盒"
    }
  ]
}
2026-08-10 11:10:31,054 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-12]
2026-08-10 11:10:31,061 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2948002, prompt_len=1699
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["门(急)诊病历信息", "就诊卡号", "流水", "姓名", "性别:男", "年", "龄:65岁", "就诊科室:内科门诊(荔湾)", "病历编号:", "就诊时间:2025-12-12 09:26:46", "主诉:BAIYUN V8", "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "完成下流操作:", "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "5、休息至少10分钟后,行12导联ECG检查。", "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "CS 扫描全能王", "3亿人都在用的扫描App"]

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
2026-08-10 11:10:44,041 INFO     29 [qwen-vl-text] coord API raw response (len=1989):
[
	{"text": "门(急)诊病历信息", "bbox": [309, 73, 532, 94]},
	{"text": "就诊卡号", "bbox": [130, 127, 198, 142]},
	{"text": "流水", "bbox": [131, 158, 184, 173]},
	{"text": "姓名", "bbox": [131, 190, 148, 205]},
	{"text": "性别:男", "bbox": [407, 189, 471, 204]},
	{"text": "年", "bbox": [510, 190, 529, 204]},
	{"text": "龄:65岁", "bbox": [597, 190, 657, 204]},
	{"text": "就诊科室:内科门诊(荔湾)", "bbox": [131, 221, 343, 237]},
	{"text": "病历编号:", "bbox": [510, 157, 587, 172]},
	{"text": "就诊时间:2025-12-12 09:26:46", "bbox": [515, 221, 761, 236]},
	{"text": "主诉:BAIYUN V8", "bbox": [130, 253, 352, 269]},
	{"text": "现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。", "bbox": [130, 283, 825, 340]},
	{"text": "完成下流操作:", "bbox": [130, 355, 245, 370]},
	{"text": "1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;", "bbox": [131, 385, 825, 421]},
	{"text": "2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。", "bbox": [131, 436, 823, 574]},
	{"text": "3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。", "bbox": [134, 588, 794, 645]},
	{"text": "4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。", "bbox": [135, 659, 514, 675]},
	{"text": "5、休息至少10分钟后,行12导联ECG检查。", "bbox": [135, 689, 457, 705]},
	{"text": "6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。", "bbox": [135, 720, 658, 736]},
	{"text": "7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。", "bbox": [135, 749, 809, 862]},
	{"text": "CS 扫描全能王", "bbox": [861, 958, 977, 974]},
	{"text": "3亿人都在用的扫描App", "bbox": [861, 977, 977, 987]}
]
2026-08-10 11:10:44,042 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=13.0s
2026-08-10 11:10:44,042 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊病历信息, bbox=[309, 73, 532, 94]
2026-08-10 11:10:44,042 INFO     29 [qwen-vl-text] coord item[1]: text=就诊卡号, bbox=[130, 127, 198, 142]
2026-08-10 11:10:44,042 INFO     29 [qwen-vl-text] coord item[2]: text=流水, bbox=[131, 158, 184, 173]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[3]: text=姓名, bbox=[131, 190, 148, 205]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[407, 189, 471, 204]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[5]: text=年, bbox=[510, 190, 529, 204]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[6]: text=龄:65岁, bbox=[597, 190, 657, 204]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[7]: text=就诊科室:内科门诊(荔湾), bbox=[131, 221, 343, 237]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[8]: text=病历编号:, bbox=[510, 157, 587, 172]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[9]: text=就诊时间:2025-12-12 09:26:46, bbox=[515, 221, 761, 236]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[10]: text=主诉:BAIYUN V8, bbox=[130, 253, 352, 269]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[11]: text=现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。, bbox=[130, 283, 825, 340]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[12]: text=完成下流操作:, bbox=[130, 355, 245, 370]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[13]: text=1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;, bbox=[131, 385, 825, 421]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[14]: text=2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。, bbox=[131, 436, 823, 574]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[15]: text=3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。, bbox=[134, 588, 794, 645]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[16]: text=4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。, bbox=[135, 659, 514, 675]
2026-08-10 11:10:44,043 INFO     29 [qwen-vl-text] coord item[17]: text=5、休息至少10分钟后,行12导联ECG检查。, bbox=[135, 689, 457, 705]
2026-08-10 11:10:44,044 INFO     29 [qwen-vl-text] coord item[18]: text=6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。, bbox=[135, 720, 658, 736]
2026-08-10 11:10:44,044 INFO     29 [qwen-vl-text] coord item[19]: text=7、回收试验药物BDA MDI&AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。, bbox=[135, 749, 809, 862]
2026-08-10 11:10:44,044 INFO     29 [qwen-vl-text] coord item[20]: text=CS 扫描全能王, bbox=[861, 958, 977, 974]
2026-08-10 11:10:44,044 INFO     29 [qwen-vl-text] coord item[21]: text=3亿人都在用的扫描App, bbox=[861, 977, 977, 987]
2026-08-10 11:10:44,045 INFO     29 [qwen-vl-text] page=2 — 22/22 coords, api_time=13.0s
2026-08-10 11:10:44,052 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2854201, prompt_len=1442
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门诊病历", "25/10/21 16时 门诊病历", "25/11/19 11时 门诊病历（GCP专用）", "25/12/12 09时 门诊病历（GCP专用）", "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试", "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "跟踪合并用药", "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏", "性鼻炎。", "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。", "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "入 qd 治疗急性支气管炎。", "预约下次安全性电话随访时间。", "既往史:", "过敏史:", "个人史:", "体格检查:", "专科情况:", "辅助检查:", "治疗项目:", "门诊诊断:", "1、支气管哮喘", "处置:", "心电图(心电图室做)", "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "备注:", "医生:"]

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
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord API raw response (len=2218):
[
	{"text": "门诊病历", "bbox": [15, 86, 60, 104]},
	{"text": "25/10/21 16时 门诊病历", "bbox": [15, 134, 123, 150]},
	{"text": "25/11/19 11时 门诊病历（GCP专用）", "bbox": [15, 182, 175, 198]},
	{"text": "25/12/12 09时 门诊病历（GCP专用）", "bbox": [15, 231, 177, 248]},
	{"text": "1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验", "bbox": [624, 82, 952, 97]},
	{"text": "药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。", "bbox": [624, 101, 848, 116]},
	{"text": "2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无", "bbox": [624, 130, 939, 145]},
	{"text": "关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。", "bbox": [624, 149, 948, 164]},
	{"text": "病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。", "bbox": [624, 169, 844, 184]},
	{"text": "3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试", "bbox": [624, 198, 948, 213]},
	{"text": "验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。", "bbox": [624, 217, 931, 232]},
	{"text": "跟踪合并用药", "bbox": [624, 247, 674, 261]},
	{"text": "1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏", "bbox": [624, 276, 951, 291]},
	{"text": "性鼻炎。", "bbox": [624, 296, 654, 310]},
	{"text": "2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。", "bbox": [624, 325, 891, 340]},
	{"text": "3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。", "bbox": [624, 355, 847, 370]},
	{"text": "补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸", "bbox": [624, 383, 923, 398]},
	{"text": "入 qd 治疗急性支气管炎。", "bbox": [624, 402, 727, 417]},
	{"text": "预约下次安全性电话随访时间。", "bbox": [624, 431, 735, 446]},
	{"text": "既往史:", "bbox": [624, 459, 673, 474]},
	{"text": "过敏史:", "bbox": [624, 488, 673, 503]},
	{"text": "个人史:", "bbox": [624, 517, 673, 532]},
	{"text": "体格检查:", "bbox": [624, 546, 664, 561]},
	{"text": "专科情况:", "bbox": [624, 575, 664, 590]},
	{"text": "辅助检查:", "bbox": [624, 604, 664, 619]},
	{"text": "治疗项目:", "bbox": [624, 633, 664, 648]},
	{"text": "门诊诊断:", "bbox": [624, 662, 664, 677]},
	{"text": "1、支气管哮喘", "bbox": [668, 692, 720, 707]},
	{"text": "处置:", "bbox": [624, 720, 682, 735]},
	{"text": "心电图(心电图室做)", "bbox": [643, 750, 719, 765]},
	{"text": "伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天", "bbox": [643, 779, 916, 794]},
	{"text": "孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天", "bbox": [643, 808, 927, 823]},
	{"text": "备注:", "bbox": [624, 837, 679, 852]},
	{"text": "医生:", "bbox": [653, 870, 674, 885]}
]
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=12.4s
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord item[0]: text=门诊病历, bbox=[15, 86, 60, 104]
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord item[1]: text=25/10/21 16时 门诊病历, bbox=[15, 134, 123, 150]
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord item[2]: text=25/11/19 11时 门诊病历（GCP专用）, bbox=[15, 182, 175, 198]
2026-08-10 11:10:56,478 INFO     29 [qwen-vl-text] coord item[3]: text=25/12/12 09时 门诊病历（GCP专用）, bbox=[15, 231, 177, 248]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[4]: text=1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验, bbox=[624, 82, 952, 97]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[5]: text=药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。, bbox=[624, 101, 848, 116]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[6]: text=2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无, bbox=[624, 130, 939, 145]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[7]: text=关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。, bbox=[624, 149, 948, 164]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[8]: text=病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。, bbox=[624, 169, 844, 184]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[9]: text=3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试, bbox=[624, 198, 948, 213]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[10]: text=验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。, bbox=[624, 217, 931, 232]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[11]: text=跟踪合并用药, bbox=[624, 247, 674, 261]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[12]: text=1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏, bbox=[624, 276, 951, 291]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[13]: text=性鼻炎。, bbox=[624, 296, 654, 310]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[14]: text=2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。, bbox=[624, 325, 891, 340]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[15]: text=3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。, bbox=[624, 355, 847, 370]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[16]: text=补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸, bbox=[624, 383, 923, 398]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[17]: text=入 qd 治疗急性支气管炎。, bbox=[624, 402, 727, 417]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[18]: text=预约下次安全性电话随访时间。, bbox=[624, 431, 735, 446]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[19]: text=既往史:, bbox=[624, 459, 673, 474]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[20]: text=过敏史:, bbox=[624, 488, 673, 503]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[21]: text=个人史:, bbox=[624, 517, 673, 532]
2026-08-10 11:10:56,479 INFO     29 [qwen-vl-text] coord item[22]: text=体格检查:, bbox=[624, 546, 664, 561]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[23]: text=专科情况:, bbox=[624, 575, 664, 590]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查:, bbox=[624, 604, 664, 619]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[25]: text=治疗项目:, bbox=[624, 633, 664, 648]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[26]: text=门诊诊断:, bbox=[624, 662, 664, 677]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[27]: text=1、支气管哮喘, bbox=[668, 692, 720, 707]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[28]: text=处置:, bbox=[624, 720, 682, 735]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[29]: text=心电图(心电图室做), bbox=[643, 750, 719, 765]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[30]: text=伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天, bbox=[643, 779, 916, 794]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[31]: text=孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天, bbox=[643, 808, 927, 823]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[32]: text=备注:, bbox=[624, 837, 679, 852]
2026-08-10 11:10:56,480 INFO     29 [qwen-vl-text] coord item[33]: text=医生:, bbox=[653, 870, 674, 885]
2026-08-10 11:10:56,481 INFO     29 [qwen-vl-text] page=3 — 34/34 coords, api_time=12.4s
2026-08-10 11:10:56,482 INFO     29 [qwen-vl-text] new_positions (56):
[[2, 183.855, 316.53999999999996, 61.466, 79.148], [2, 77.35, 117.80999999999999, 106.934, 119.564], [2, 77.945, 109.47999999999999, 133.036, 145.666], [2, 77.945, 88.06, 159.98, 172.60999999999999], [2, 242.165, 280.245, 159.138, 171.768], [2, 303.45, 314.755, 159.98, 171.768], [2, 355.215, 390.91499999999996, 159.98, 171.768], [2, 77.945, 204.08499999999998, 186.082, 199.554], [2, 303.45, 349.265, 132.194, 144.82399999999998], [2, 306.425, 452.79499999999996, 186.082, 198.712], [2, 77.35, 209.44, 213.02599999999998, 226.498], [2, 77.35, 490.875, 238.286, 286.28], [2, 77.35, 145.775, 298.90999999999997, 311.53999999999996], [2, 77.945, 490.875, 324.17, 354.48199999999997], [2, 77.945, 489.685, 367.11199999999997, 483.308], [2, 79.72999999999999, 472.43, 495.096, 543.09], [2, 80.325, 305.83, 554.8779999999999, 568.35], [2, 80.325, 271.91499999999996, 580.138, 593.61], [2, 80.325, 391.51, 606.24, 619.712], [2, 80.325, 481.35499999999996, 630.658, 725.804], [2, 512.295, 581.3149999999999, 806.636, 820.108], [2, 512.295, 581.3149999999999, 822.634, 831.054], [3, 12.629999999999999, 50.519999999999996, 51.169999999999995, 61.879999999999995], [3, 12.629999999999999, 103.566, 79.72999999999999, 89.25], [3, 12.629999999999999, 147.35, 108.28999999999999, 117.80999999999999], [3, 12.629999999999999, 149.034, 137.445, 147.56], [3, 525.408, 801.584, 48.79, 57.714999999999996], [3, 525.408, 714.016, 60.095, 69.02], [3, 525.408, 790.6379999999999, 77.35, 86.27499999999999], [3, 525.408, 798.216, 88.655, 97.58], [3, 525.408, 710.648, 100.55499999999999, 109.47999999999999], [3, 525.408, 798.216, 117.80999999999999, 126.735], [3, 525.408, 783.9019999999999, 129.11499999999998, 138.04], [3, 525.408, 567.5079999999999, 146.965, 155.295], [3, 525.408, 800.742, 164.22, 173.14499999999998], [3, 525.408, 550.668, 176.12, 184.45], [3, 525.408, 750.222, 193.375, 202.29999999999998], [3, 525.408, 713.174, 211.225, 220.14999999999998], [3, 525.408, 777.1659999999999, 227.885, 236.81], [3, 525.408, 612.134, 239.19, 248.11499999999998], [3, 525.408, 618.87, 256.445, 265.37], [3, 525.408, 566.6659999999999, 273.10499999999996, 282.03], [3, 525.408, 566.6659999999999, 290.36, 299.28499999999997], [3, 525.408, 566.6659999999999, 307.615, 316.53999999999996], [3, 525.408, 559.088, 324.87, 333.79499999999996], [3, 525.408, 559.088, 342.125, 351.05], [3, 525.408, 559.088, 359.38, 368.305], [3, 525.408, 559.088, 376.635, 385.56], [3, 525.408, 559.088, 393.89, 402.815], [3, 562.456, 606.24, 411.74, 420.66499999999996], [3, 525.408, 574.244, 428.4, 437.325], [3, 541.406, 605.398, 446.25, 455.17499999999995], [3, 541.406, 771.2719999999999, 463.505, 472.43], [3, 541.406, 780.534, 480.76, 489.685], [3, 525.408, 571.718, 498.015, 506.94], [3, 549.826, 567.5079999999999, 517.65, 526.5749999999999]]
2026-08-10 11:10:56,482 INFO     29 [qwen-vl-text] ═══ DONE ═══ 56 positions, pages=2, time=120.3s
2026-08-10 11:10:56,482 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:10:56,484 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:10:56,484 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 11:10:56,484 INFO     29 [qwen-vl-text] positions(30): [[16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0], [16, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:10:56,484 INFO     29 [qwen-vl-text] page grouping: [16], lines per page: [30]
2026-08-10 11:10:56,841 INFO     29 [qwen-vl-text] page=16, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:10:56,842 INFO     29 [qwen-vl-text] LLM extraction start, text_len=849
2026-08-10 11:10:56,842 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:10:56,842 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 552, \"bbox_end\": 581, \"encounter_dates\": [\"2026-02-04\"], \"department\": \"内科门诊（基础）\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "病历编号：\n姓名：\n性别：男\n年龄：65岁\n就诊科室：内科门诊（基础）\n医生：\n就诊时间：2026-02-04 11:23:30\n主诉：支气管哮喘治疗后复诊\n现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，\n无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：\n两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。\n既往史：鼻炎病史，有糖尿病史\n过敏史：未发现\n个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。\n体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。\n专科情况：\n辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：\n5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：\n0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化\n氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发\n试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常\n治疗项目：\n门诊诊断：\n1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病\n单病种：\n发病时间：\n处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。\n倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天\n孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天\n备注：建议在停药附近社区医疗机构随访。",
    "role": "user"
  }
]
2026-08-10 11:11:01,440 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:01,440 INFO     29 [qwen-vl-text] LLM output (len=728):
{
  "encounter_date": "2026-02-04",
  "chief_complaint": "支气管哮喘治疗后复诊",
  "present_illness": "2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。",
  "past_history": "鼻炎病史，有糖尿病史",
  "diagnosis": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病",
  "treatment_plan": [
    {
      "drug_name": "倍氯米松福莫特罗吸入气雾剂",
      "dosage": "2.0瓶",
      "frequency": "一天2次",
      "route": "吸入用药",
      "duration": "30天"
    },
    {
      "drug_name": "孟鲁司特钠片（省采）",
      "dosage": "10.0mg",
      "frequency": "每日1次",
      "route": "口服",
      "duration": "30天"
    }
  ]
}
2026-08-10 11:11:01,440 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-02-04]
2026-08-10 11:11:01,446 INFO     29 [qwen-vl-text] coord API call start, page=16, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3124705, prompt_len=1552
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["病历编号：", "姓名：", "性别：男", "年龄：65岁", "就诊科室：内科门诊（基础）", "医生：", "就诊时间：2026-02-04 11:23:30", "主诉：支气管哮喘治疗后复诊", "现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "既往史：鼻炎病史，有糖尿病史", "过敏史：未发现", "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "专科情况：", "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "治疗项目：", "门诊诊断：", "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "单病种：", "发病时间：", "处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "备注：建议在停药附近社区医疗机构随访。"]

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
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord API raw response (len=2164):
[
	{"text": "病历编号：", "bbox": [515, 50, 600, 66]},
	{"text": "姓名：", "bbox": [114, 84, 135, 99]},
	{"text": "性别：男", "bbox": [515, 84, 535, 99]},
	{"text": "年龄：65岁", "bbox": [607, 84, 678, 99]},
	{"text": "就诊科室：内科门诊（基础）", "bbox": [114, 117, 345, 133]},
	{"text": "医生：", "bbox": [408, 117, 442, 133]},
	{"text": "就诊时间：2026-02-04 11:23:30", "bbox": [515, 117, 808, 133]},
	{"text": "主诉：支气管哮喘治疗后复诊", "bbox": [114, 151, 450, 167]},
	{"text": "现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，", "bbox": [114, 185, 854, 219]},
	{"text": "无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：", "bbox": [114, 225, 868, 288]},
	{"text": "两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。", "bbox": [114, 293, 838, 331]},
	{"text": "既往史：鼻炎病史，有糖尿病史", "bbox": [114, 347, 428, 363]},
	{"text": "过敏史：未发现", "bbox": [114, 380, 297, 396]},
	{"text": "个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。", "bbox": [114, 410, 797, 427]},
	{"text": "体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。", "bbox": [114, 443, 851, 481]},
	{"text": "专科情况：", "bbox": [114, 497, 205, 512]},
	{"text": "辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：", "bbox": [114, 529, 748, 545]},
	{"text": "5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：", "bbox": [114, 551, 690, 567]},
	{"text": "0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化", "bbox": [114, 573, 725, 589]},
	{"text": "氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发", "bbox": [114, 594, 857, 610]},
	{"text": "试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常", "bbox": [114, 616, 686, 632]},
	{"text": "治疗项目：", "bbox": [114, 648, 203, 663]},
	{"text": "门诊诊断：", "bbox": [114, 680, 203, 696]},
	{"text": "1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病", "bbox": [140, 711, 625, 727]},
	{"text": "单病种：", "bbox": [114, 743, 221, 758]},
	{"text": "发病时间：", "bbox": [114, 773, 201, 789]},
	{"text": "处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。", "bbox": [114, 805, 720, 821]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天", "bbox": [158, 837, 778, 853]},
	{"text": "孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天", "bbox": [158, 867, 808, 883]},
	{"text": "备注：建议在停药附近社区医疗机构随访。", "bbox": [114, 897, 537, 912]}
]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=13.5s
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[0]: text=病历编号：, bbox=[515, 50, 600, 66]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[114, 84, 135, 99]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[515, 84, 535, 99]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：65岁, bbox=[607, 84, 678, 99]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[4]: text=就诊科室：内科门诊（基础）, bbox=[114, 117, 345, 133]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[5]: text=医生：, bbox=[408, 117, 442, 133]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[6]: text=就诊时间：2026-02-04 11:23:30, bbox=[515, 117, 808, 133]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[7]: text=主诉：支气管哮喘治疗后复诊, bbox=[114, 151, 450, 167]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[8]: text=现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，, bbox=[114, 185, 854, 219]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[9]: text=无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：, bbox=[114, 225, 868, 288]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[10]: text=两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。, bbox=[114, 293, 838, 331]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[11]: text=既往史：鼻炎病史，有糖尿病史, bbox=[114, 347, 428, 363]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[12]: text=过敏史：未发现, bbox=[114, 380, 297, 396]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[13]: text=个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。, bbox=[114, 410, 797, 427]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[14]: text=体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。, bbox=[114, 443, 851, 481]
2026-08-10 11:11:14,897 INFO     29 [qwen-vl-text] coord item[15]: text=专科情况：, bbox=[114, 497, 205, 512]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[16]: text=辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：, bbox=[114, 529, 748, 545]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[17]: text=5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：, bbox=[114, 551, 690, 567]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[18]: text=0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化, bbox=[114, 573, 725, 589]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[19]: text=氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发, bbox=[114, 594, 857, 610]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[20]: text=试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常, bbox=[114, 616, 686, 632]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[21]: text=治疗项目：, bbox=[114, 648, 203, 663]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[22]: text=门诊诊断：, bbox=[114, 680, 203, 696]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[23]: text=1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病, bbox=[140, 711, 625, 727]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[24]: text=单病种：, bbox=[114, 743, 221, 758]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[25]: text=发病时间：, bbox=[114, 773, 201, 789]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[26]: text=处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。, bbox=[114, 805, 720, 821]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[27]: text=倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天, bbox=[158, 837, 778, 853]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[28]: text=孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天, bbox=[158, 867, 808, 883]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] coord item[29]: text=备注：建议在停药附近社区医疗机构随访。, bbox=[114, 897, 537, 912]
2026-08-10 11:11:14,898 INFO     29 [qwen-vl-text] page=16 — 30/30 coords, api_time=13.5s
2026-08-10 11:11:14,899 INFO     29 [qwen-vl-text] new_positions (30):
[[16, 306.425, 357.0, 42.1, 55.571999999999996], [16, 67.83, 80.325, 70.728, 83.358], [16, 306.425, 318.325, 70.728, 83.358], [16, 361.16499999999996, 403.40999999999997, 70.728, 83.358], [16, 67.83, 205.27499999999998, 98.514, 111.98599999999999], [16, 242.76, 262.99, 98.514, 111.98599999999999], [16, 306.425, 480.76, 98.514, 111.98599999999999], [16, 67.83, 267.75, 127.142, 140.614], [16, 67.83, 508.13, 155.76999999999998, 184.398], [16, 67.83, 516.4599999999999, 189.45, 242.49599999999998], [16, 67.83, 498.60999999999996, 246.706, 278.702], [16, 67.83, 254.66, 292.174, 305.646], [16, 67.83, 176.715, 319.96, 333.432], [16, 67.83, 474.215, 345.21999999999997, 359.534], [16, 67.83, 506.34499999999997, 373.006, 405.002], [16, 67.83, 121.975, 418.474, 431.104], [16, 67.83, 445.06, 445.418, 458.89], [16, 67.83, 410.54999999999995, 463.942, 477.414], [16, 67.83, 431.375, 482.466, 495.938], [16, 67.83, 509.91499999999996, 500.14799999999997, 513.62], [16, 67.83, 408.16999999999996, 518.672, 532.144], [16, 67.83, 120.785, 545.616, 558.246], [16, 67.83, 120.785, 572.56, 586.0319999999999], [16, 83.3, 371.875, 598.662, 612.134], [16, 67.83, 131.495, 625.606, 638.236], [16, 67.83, 119.595, 650.866, 664.338], [16, 67.83, 428.4, 677.81, 691.2819999999999], [16, 94.00999999999999, 462.90999999999997, 704.754, 718.226], [16, 94.00999999999999, 480.76, 730.014, 743.486], [16, 67.83, 319.515, 755.274, 767.904]]
2026-08-10 11:11:14,899 INFO     29 [qwen-vl-text] ═══ DONE ═══ 30 positions, pages=1, time=18.4s
2026-08-10 11:11:14,908 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 11:11:14,908 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Clinical | outputs={"chunks": "4 items, types={'OutpatientRecord': 4}", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:11:14,908 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 11:11:14,910 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:11:14.909+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:11:14,917 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:14,917 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:11:14,920 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:14,920 INFO     29 [qwen-vl-text] LLM output (len=1663):
{
  "exam_date": "2025-04-11",
  "report_date": "2025-04-11",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "测试日期: 25/4/11\n测试时间: 14:56:4\n\n| 指标 | 单位 | 预计值 | 实测值 | 实测 % (实/预) |\n| :--- | :--- | :--- | :--- | :--- |\n| VT | [L] | 0.36 | 0.41 | 114.9 |\n| BF | [1/min] | 20.00 | 20.79 | 104.0 |\n| MV | [L/min] | 7.14 | 8.54 | 119.5 |\n| ERV | [L] | 1.07 | 1.07 | 99.4 |\n| VC MAX | [L] | 3.19 | 2.84 | 88.9 |\n| FVC | [L] | 3.13 | 2.84 | 90.6 |\n| FEV 1 | [L] | 2.70 | 1.53 | 56.9 |\n| FEV 1 % FVC | [%] | 83.98 | 54.07 | 64.4 |\n| FEV 1 % VC MAX | [%] | 81.31 | 54.07 | 66.5 |\n| PEF | [L/s] | 6.46 | 4.56 | 70.7 |\n| MEF 75 | [L/s] | 5.73 | 1.84 | 32.1 |\n| MEF 50 | [L/s] | 4.06 | 0.84 | 20.7 |\n| MEF 25 | [L/s] | 1.77 | 0.28 | 15.6 |\n| MMEF 75/25 | [L/s] | 3.53 | 0.65 | 18.3 |\n| FET | [s] | 8.46 | - | - |\n| V backextrapolation ex | [L] | 0.03 | - | - |\n| V backextrapol. % FVC | [%] | 1.23 | - | - |\n| MVV | [L/min] | 101.93 | 75.75 | 74.3 |\n| FEV 1*30 | [L/min] | 101.93 | 46.03 | 45.2 |\n| RV-SB | [L] | 1.55 | 2.56 | 164.9 |\n| RV%TLC-SB | [%] | 32.90 | 47.52 | 144.4 |\n| TLC-SB | [L] | 4.77 | 5.39 | 112.9 |\n| FRC-SB | [L] | 2.63 | 3.31 | 126.0 |\n| FRC%TLC-SB | [%] | 51.66 | 61.42 | 118.9 |\n| DLCOc SB | [mmol/min/kPa] | 8.34 | 6.95 | 83.4 |\n| DLCO SB | [mmol/min/kPa] | 8.34 | 6.95 | 83.4 |\n\n检查质量：FVC：A级 。 FEV1：A级 。\n备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。",
  "conclusion": "1.中重度阻塞性通气功能障碍。\n2.最大自主分钟通气量（MVV）轻度下降。\n备注：患者MVV配合佳。结果仅供参考，请结合临床分析。\n3.弥散功能在正常范围。\n4.残总比中度增高。",
  "physician": "张青苹",
  "reviewer": "孙帅森"
}
2026-08-10 11:11:14,921 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1165294, prompt_len=2119
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共151行）
["姓名：", "出生日期：1984/4/02", "门诊/住院/体检：", "身高：160 cm", "身份证号：", "性别：女", "年龄：41 岁", "测试号：", "体重：50 kg", "测试日期", "测试时间", "预计", "实测 % (实/预)", "25/4/11", "14:56:4", "VT", "[L]", "0.36", "0.41", "114.9", "BF", "[1/min]", "20.00", "20.79", "104.0", "MV", "[L/min]", "7.14", "8.54", "119.5", "ERV", "[L]", "1.07", "1.07", "99.4", "VC MAX", "[L]", "3.19", "2.84", "88.9", "FVC", "[L]", "3.13", "2.84", "90.6", "FEV 1", "[L]", "2.70", "1.53", "56.9", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "PEF", "[L/s]", "6.46", "4.56", "70.7", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "FET", "[s]", "8.46", "V backextrapolation ex", "[L]", "0.03", "V backextrapol. % FVC", "[%]", "1.23", "MVV", "[L/min]", "101.93", "75.75", "74.3", "FEV 1*30", "[L/min]", "101.93", "46.03", "45.2", "RV-SB", "[L]", "1.55", "2.56", "164.9", "RV%TLC-SB", "[%]", "32.90", "47.52", "144.4", "TLC-SB", "[L]", "4.77", "5.39", "112.9", "FRC-SB", "[L]", "2.63", "3.31", "126.0", "FRC%TLC-SB", "[%]", "51.66", "61.42", "118.9", "DLCOc SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "DLCO SB", "[mmol/min/kPa]", "8.34", "6.95", "83.4", "医生意见：", "1.中重度阻塞性通气功能障碍。", "检查质量：FVC：A级 。 FEV1：A级 。", "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "2.最大自主分钟通气量（MVV）轻度下降。", "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "3.弥散功能在正常范围。4.残总比中度增高。", "审核医生：孙帅森", "检测技师：张青苹", "通气弥散B", "2025/4/11 15:18", "1/1"]

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
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord API raw response (len=7674):
[
	{"text": "姓名：", "bbox": [83, 88, 136, 103]},
	{"text": "出生日期：1984/4/02", "bbox": [83, 103, 371, 118]},
	{"text": "门诊/住院/体检：", "bbox": [83, 118, 240, 132]},
	{"text": "身高：160 cm", "bbox": [83, 132, 341, 146]},
	{"text": "身份证号：", "bbox": [83, 146, 176, 159]},
	{"text": "性别：", "bbox": [477, 88, 527, 103]},
	{"text": "年龄：", "bbox": [477, 103, 527, 118]},
	{"text": "测试号：", "bbox": [477, 118, 548, 132]},
	{"text": "体重：", "bbox": [477, 132, 527, 146]},
	{"text": "测试日期", "bbox": [109, 189, 181, 203]},
	{"text": "测试时间", "bbox": [109, 203, 181, 218]},
	{"text": "预计", "bbox": [373, 173, 409, 188]},
	{"text": "实测 % (实/预)", "bbox": [445, 173, 553, 188]},
	{"text": "25/4/11", "bbox": [419, 190, 480, 203]},
	{"text": "14:56:4", "bbox": [419, 204, 480, 218]},
	{"text": "VT", "bbox": [109, 235, 128, 249]},
	{"text": "[L]", "bbox": [320, 235, 344, 249]},
	{"text": "0.36", "bbox": [373, 235, 410, 249]},
	{"text": "0.41", "bbox": [445, 235, 480, 249]},
	{"text": "114.9", "bbox": [510, 235, 553, 249]},
	{"text": "BF", "bbox": [109, 250, 128, 264]},
	{"text": "[1/min]", "bbox": [285, 250, 344, 264]},
	{"text": "20.00", "bbox": [364, 250, 410, 264]},
	{"text": "20.79", "bbox": [437, 250, 480, 264]},
	{"text": "104.0", "bbox": [510, 250, 553, 264]},
	{"text": "MV", "bbox": [109, 265, 128, 279]},
	{"text": "[L/min]", "bbox": [285, 265, 344, 279]},
	{"text": "7.14", "bbox": [373, 265, 410, 279]},
	{"text": "8.54", "bbox": [445, 265, 480, 279]},
	{"text": "119.5", "bbox": [510, 265, 553, 279]},
	{"text": "ERV", "bbox": [109, 280, 136, 294]},
	{"text": "[L]", "bbox": [320, 280, 344, 294]},
	{"text": "1.07", "bbox": [373, 280, 410, 294]},
	{"text": "1.07", "bbox": [445, 280, 480, 294]},
	{"text": "99.4", "bbox": [517, 280, 553, 294]},
	{"text": "VC MAX", "bbox": [109, 295, 164, 309]},
	{"text": "[L]", "bbox": [320, 295, 344, 309]},
	{"text": "3.19", "bbox": [373, 295, 410, 309]},
	{"text": "2.84", "bbox": [445, 295, 480, 309]},
	{"text": "88.9", "bbox": [517, 295, 553, 309]},
	{"text": "FVC", "bbox": [109, 326, 136, 340]},
	{"text": "[L]", "bbox": [320, 326, 344, 340]},
	{"text": "3.13", "bbox": [373, 326, 410, 340]},
	{"text": "2.84", "bbox": [445, 326, 480, 340]},
	{"text": "90.6", "bbox": [517, 326, 553, 340]},
	{"text": "FEV 1", "bbox": [109, 341, 153, 355]},
	{"text": "[L]", "bbox": [320, 341, 344, 355]},
	{"text": "2.70", "bbox": [373, 341, 410, 355]},
	{"text": "1.53", "bbox": [445, 341, 480, 355]},
	{"text": "56.9", "bbox": [517, 341, 553, 355]},
	{"text": "FEV 1 % FVC", "bbox": [109, 356, 210, 370]},
	{"text": "[%]", "bbox": [320, 356, 344, 370]},
	{"text": "83.98", "bbox": [364, 356, 410, 370]},
	{"text": "54.07", "bbox": [437, 356, 480, 370]},
	{"text": "64.4", "bbox": [517, 356, 553, 370]},
	{"text": "FEV 1 % VC MAX", "bbox": [109, 371, 237, 385]},
	{"text": "[%]", "bbox": [320, 371, 344, 385]},
	{"text": "81.31", "bbox": [364, 371, 410, 385]},
	{"text": "54.07", "bbox": [437, 371, 480, 385]},
	{"text": "66.5", "bbox": [517, 371, 553, 385]},
	{"text": "PEF", "bbox": [109, 386, 136, 400]},
	{"text": "[L/s]", "bbox": [302, 386, 344, 400]},
	{"text": "6.46", "bbox": [373, 386, 410, 400]},
	{"text": "4.56", "bbox": [437, 386, 480, 400]},
	{"text": "70.7", "bbox": [517, 386, 553, 400]},
	{"text": "MEF 75", "bbox": [109, 401, 164, 415]},
	{"text": "[L/s]", "bbox": [302, 401, 344, 415]},
	{"text": "5.73", "bbox": [373, 401, 410, 415]},
	{"text": "1.84", "bbox": [445, 401, 480, 415]},
	{"text": "32.1", "bbox": [517, 401, 553, 415]},
	{"text": "MEF 50", "bbox": [109, 416, 164, 430]},
	{"text": "[L/s]", "bbox": [302, 416, 344, 430]},
	{"text": "4.06", "bbox": [373, 416, 410, 430]},
	{"text": "0.84", "bbox": [445, 416, 480, 430]},
	{"text": "20.7", "bbox": [517, 416, 553, 430]},
	{"text": "MEF 25", "bbox": [109, 431, 164, 445]},
	{"text": "[L/s]", "bbox": [302, 431, 344, 445]},
	{"text": "1.77", "bbox": [373, 431, 410, 445]},
	{"text": "0.28", "bbox": [445, 431, 480, 445]},
	{"text": "15.6", "bbox": [517, 431, 553, 445]},
	{"text": "MMEF 75/25", "bbox": [109, 446, 200, 460]},
	{"text": "[L/s]", "bbox": [302, 446, 344, 460]},
	{"text": "3.53", "bbox": [373, 446, 410, 460]},
	{"text": "0.65", "bbox": [445, 446, 480, 460]},
	{"text": "18.3", "bbox": [517, 446, 553, 460]},
	{"text": "FET", "bbox": [109, 461, 136, 475]},
	{"text": "[s]", "bbox": [320, 461, 344, 475]},
	{"text": "8.46", "bbox": [445, 461, 480, 475]},
	{"text": "V backextrapolation ex", "bbox": [109, 476, 308, 490]},
	{"text": "[L]", "bbox": [320, 476, 344, 490]},
	{"text": "0.03", "bbox": [445, 476, 480, 490]},
	{"text": "V backextrapol. % FVC", "bbox": [109, 491, 300, 505]},
	{"text": "[%]", "bbox": [320, 491, 344, 505]},
	{"text": "1.23", "bbox": [445, 491, 480, 505]},
	{"text": "MVV", "bbox": [109, 522, 136, 536]},
	{"text": "[L/min]", "bbox": [285, 522, 344, 536]},
	{"text": "101.93", "bbox": [356, 522, 410, 536]},
	{"text": "75.75", "bbox": [437, 522, 480, 536]},
	{"text": "74.3", "bbox": [517, 522, 553, 536]},
	{"text": "FEV 1*30", "bbox": [109, 537, 181, 551]},
	{"text": "[L/min]", "bbox": [285, 537, 344, 551]},
	{"text": "101.93", "bbox": [356, 537, 410, 551]},
	{"text": "46.03", "bbox": [437, 537, 480, 551]},
	{"text": "45.2", "bbox": [517, 537, 553, 551]},
	{"text": "RV-SB", "bbox": [109, 568, 153, 582]},
	{"text": "[L]", "bbox": [320, 568, 344, 582]},
	{"text": "1.55", "bbox": [373, 568, 410, 582]},
	{"text": "2.56", "bbox": [445, 568, 480, 582]},
	{"text": "164.9", "bbox": [510, 568, 553, 582]},
	{"text": "RV%TLC-SB", "bbox": [109, 583, 190, 597]},
	{"text": "[%]", "bbox": [320, 583, 344, 597]},
	{"text": "32.90", "bbox": [364, 583, 410, 597]},
	{"text": "47.52", "bbox": [437, 583, 480, 597]},
	{"text": "144.4", "bbox": [510, 583, 553, 597]},
	{"text": "TLC-SB", "bbox": [109, 598, 162, 612]},
	{"text": "[L]", "bbox": [320, 598, 344, 612]},
	{"text": "4.77", "bbox": [373, 598, 410, 612]},
	{"text": "5.39", "bbox": [445, 598, 480, 612]},
	{"text": "112.9", "bbox": [510, 598, 553, 612]},
	{"text": "FRC-SB", "bbox": [109, 613, 162, 627]},
	{"text": "[L]", "bbox": [320, 613, 344, 627]},
	{"text": "2.63", "bbox": [373, 613, 410, 627]},
	{"text": "3.31", "bbox": [445, 613, 480, 627]},
	{"text": "126.0", "bbox": [510, 613, 553, 627]},
	{"text": "FRC%TLC-SB", "bbox": [109, 628, 198, 642]},
	{"text": "[%]", "bbox": [320, 628, 344, 642]},
	{"text": "51.66", "bbox": [364, 628, 410, 642]},
	{"text": "61.42", "bbox": [437, 628, 480, 642]},
	{"text": "118.9", "bbox": [510, 628, 553, 642]},
	{"text": "DLCOc SB", "bbox": [109, 643, 180, 657]},
	{"text": "[mmol/min/kPa]", "bbox": [218, 643, 344, 657]},
	{"text": "8.34", "bbox": [373, 643, 410, 657]},
	{"text": "6.95", "bbox": [445, 643, 480, 657]},
	{"text": "83.4", "bbox": [517, 643, 553, 657]},
	{"text": "DLCO SB", "bbox": [109, 658, 171, 672]},
	{"text": "[mmol/min/kPa]", "bbox": [218, 658, 344, 672]},
	{"text": "8.34", "bbox": [373, 658, 410, 672]},
	{"text": "6.95", "bbox": [445, 658, 480, 672]},
	{"text": "83.4", "bbox": [517, 658, 553, 672]},
	{"text": "医生意见：", "bbox": [87, 704, 190, 722]},
	{"text": "1.中重度阻塞性通气功能障碍。", "bbox": [87, 726, 328, 739]},
	{"text": "检查质量：FVC：A级 。 FEV1：A级 。", "bbox": [87, 739, 401, 752]},
	{"text": "备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。", "bbox": [87, 751, 594, 764]},
	{"text": "2.最大自主分钟通气量（MVV）轻度下降。", "bbox": [87, 763, 410, 776]},
	{"text": "备注：患者MVV配合佳。结果仅供参考，请结合临床分析。", "bbox": [87, 775, 532, 788]},
	{"text": "3.弥散功能在正常范围。4.残总比中度增高。", "bbox": [87, 787, 435, 800]},
	{"text": "审核医生：孙帅森", "bbox": [555, 840, 697, 856]},
	{"text": "检测技师：张青苹", "bbox": [552, 860, 703, 876]},
	{"text": "通气弥散B", "bbox": [72, 905, 123, 914]},
	{"text": "2025/4/11 15:18", "bbox": [451, 905, 529, 914]},
	{"text": "1/1", "bbox": [901, 905, 914, 914]}
]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord API: raw_items=151, valid_items=151, elapsed=37.6s
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[83, 88, 136, 103]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[1]: text=出生日期：1984/4/02, bbox=[83, 103, 371, 118]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[2]: text=门诊/住院/体检：, bbox=[83, 118, 240, 132]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[3]: text=身高：160 cm, bbox=[83, 132, 341, 146]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[4]: text=身份证号：, bbox=[83, 146, 176, 159]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[5]: text=性别：, bbox=[477, 88, 527, 103]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[6]: text=年龄：, bbox=[477, 103, 527, 118]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[7]: text=测试号：, bbox=[477, 118, 548, 132]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[8]: text=体重：, bbox=[477, 132, 527, 146]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[9]: text=测试日期, bbox=[109, 189, 181, 203]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[10]: text=测试时间, bbox=[109, 203, 181, 218]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[11]: text=预计, bbox=[373, 173, 409, 188]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[12]: text=实测 % (实/预), bbox=[445, 173, 553, 188]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[13]: text=25/4/11, bbox=[419, 190, 480, 203]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[14]: text=14:56:4, bbox=[419, 204, 480, 218]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[15]: text=VT, bbox=[109, 235, 128, 249]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[16]: text=[L], bbox=[320, 235, 344, 249]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[17]: text=0.36, bbox=[373, 235, 410, 249]
2026-08-10 11:11:52,498 INFO     29 [qwen-vl-text] coord item[18]: text=0.41, bbox=[445, 235, 480, 249]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[19]: text=114.9, bbox=[510, 235, 553, 249]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[20]: text=BF, bbox=[109, 250, 128, 264]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[21]: text=[1/min], bbox=[285, 250, 344, 264]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[22]: text=20.00, bbox=[364, 250, 410, 264]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[23]: text=20.79, bbox=[437, 250, 480, 264]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[24]: text=104.0, bbox=[510, 250, 553, 264]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[25]: text=MV, bbox=[109, 265, 128, 279]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[26]: text=[L/min], bbox=[285, 265, 344, 279]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[27]: text=7.14, bbox=[373, 265, 410, 279]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[28]: text=8.54, bbox=[445, 265, 480, 279]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[29]: text=119.5, bbox=[510, 265, 553, 279]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[30]: text=ERV, bbox=[109, 280, 136, 294]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[31]: text=[L], bbox=[320, 280, 344, 294]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[32]: text=1.07, bbox=[373, 280, 410, 294]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[33]: text=1.07, bbox=[445, 280, 480, 294]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[34]: text=99.4, bbox=[517, 280, 553, 294]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[35]: text=VC MAX, bbox=[109, 295, 164, 309]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[36]: text=[L], bbox=[320, 295, 344, 309]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[37]: text=3.19, bbox=[373, 295, 410, 309]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[38]: text=2.84, bbox=[445, 295, 480, 309]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[39]: text=88.9, bbox=[517, 295, 553, 309]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[40]: text=FVC, bbox=[109, 326, 136, 340]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[41]: text=[L], bbox=[320, 326, 344, 340]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[42]: text=3.13, bbox=[373, 326, 410, 340]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[43]: text=2.84, bbox=[445, 326, 480, 340]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[44]: text=90.6, bbox=[517, 326, 553, 340]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[45]: text=FEV 1, bbox=[109, 341, 153, 355]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[46]: text=[L], bbox=[320, 341, 344, 355]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[47]: text=2.70, bbox=[373, 341, 410, 355]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[48]: text=1.53, bbox=[445, 341, 480, 355]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[49]: text=56.9, bbox=[517, 341, 553, 355]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[50]: text=FEV 1 % FVC, bbox=[109, 356, 210, 370]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[51]: text=[%], bbox=[320, 356, 344, 370]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[52]: text=83.98, bbox=[364, 356, 410, 370]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[53]: text=54.07, bbox=[437, 356, 480, 370]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[54]: text=64.4, bbox=[517, 356, 553, 370]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[55]: text=FEV 1 % VC MAX, bbox=[109, 371, 237, 385]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[56]: text=[%], bbox=[320, 371, 344, 385]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[57]: text=81.31, bbox=[364, 371, 410, 385]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[58]: text=54.07, bbox=[437, 371, 480, 385]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[59]: text=66.5, bbox=[517, 371, 553, 385]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[60]: text=PEF, bbox=[109, 386, 136, 400]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[61]: text=[L/s], bbox=[302, 386, 344, 400]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[62]: text=6.46, bbox=[373, 386, 410, 400]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[63]: text=4.56, bbox=[437, 386, 480, 400]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[64]: text=70.7, bbox=[517, 386, 553, 400]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[65]: text=MEF 75, bbox=[109, 401, 164, 415]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[66]: text=[L/s], bbox=[302, 401, 344, 415]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[67]: text=5.73, bbox=[373, 401, 410, 415]
2026-08-10 11:11:52,499 INFO     29 [qwen-vl-text] coord item[68]: text=1.84, bbox=[445, 401, 480, 415]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[69]: text=32.1, bbox=[517, 401, 553, 415]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[70]: text=MEF 50, bbox=[109, 416, 164, 430]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[71]: text=[L/s], bbox=[302, 416, 344, 430]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[72]: text=4.06, bbox=[373, 416, 410, 430]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[73]: text=0.84, bbox=[445, 416, 480, 430]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[74]: text=20.7, bbox=[517, 416, 553, 430]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[75]: text=MEF 25, bbox=[109, 431, 164, 445]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[76]: text=[L/s], bbox=[302, 431, 344, 445]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[77]: text=1.77, bbox=[373, 431, 410, 445]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[78]: text=0.28, bbox=[445, 431, 480, 445]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[79]: text=15.6, bbox=[517, 431, 553, 445]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[80]: text=MMEF 75/25, bbox=[109, 446, 200, 460]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[81]: text=[L/s], bbox=[302, 446, 344, 460]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[82]: text=3.53, bbox=[373, 446, 410, 460]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[83]: text=0.65, bbox=[445, 446, 480, 460]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[84]: text=18.3, bbox=[517, 446, 553, 460]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[85]: text=FET, bbox=[109, 461, 136, 475]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[86]: text=[s], bbox=[320, 461, 344, 475]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[87]: text=8.46, bbox=[445, 461, 480, 475]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[88]: text=V backextrapolation ex, bbox=[109, 476, 308, 490]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[89]: text=[L], bbox=[320, 476, 344, 490]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[90]: text=0.03, bbox=[445, 476, 480, 490]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[91]: text=V backextrapol. % FVC, bbox=[109, 491, 300, 505]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[92]: text=[%], bbox=[320, 491, 344, 505]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[93]: text=1.23, bbox=[445, 491, 480, 505]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[94]: text=MVV, bbox=[109, 522, 136, 536]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[95]: text=[L/min], bbox=[285, 522, 344, 536]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[96]: text=101.93, bbox=[356, 522, 410, 536]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[97]: text=75.75, bbox=[437, 522, 480, 536]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[98]: text=74.3, bbox=[517, 522, 553, 536]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[99]: text=FEV 1*30, bbox=[109, 537, 181, 551]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[100]: text=[L/min], bbox=[285, 537, 344, 551]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[101]: text=101.93, bbox=[356, 537, 410, 551]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[102]: text=46.03, bbox=[437, 537, 480, 551]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[103]: text=45.2, bbox=[517, 537, 553, 551]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[104]: text=RV-SB, bbox=[109, 568, 153, 582]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[105]: text=[L], bbox=[320, 568, 344, 582]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[106]: text=1.55, bbox=[373, 568, 410, 582]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[107]: text=2.56, bbox=[445, 568, 480, 582]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[108]: text=164.9, bbox=[510, 568, 553, 582]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[109]: text=RV%TLC-SB, bbox=[109, 583, 190, 597]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[110]: text=[%], bbox=[320, 583, 344, 597]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[111]: text=32.90, bbox=[364, 583, 410, 597]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[112]: text=47.52, bbox=[437, 583, 480, 597]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[113]: text=144.4, bbox=[510, 583, 553, 597]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[114]: text=TLC-SB, bbox=[109, 598, 162, 612]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[115]: text=[L], bbox=[320, 598, 344, 612]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[116]: text=4.77, bbox=[373, 598, 410, 612]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[117]: text=5.39, bbox=[445, 598, 480, 612]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[118]: text=112.9, bbox=[510, 598, 553, 612]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[119]: text=FRC-SB, bbox=[109, 613, 162, 627]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[120]: text=[L], bbox=[320, 613, 344, 627]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[121]: text=2.63, bbox=[373, 613, 410, 627]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[122]: text=3.31, bbox=[445, 613, 480, 627]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[123]: text=126.0, bbox=[510, 613, 553, 627]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[124]: text=FRC%TLC-SB, bbox=[109, 628, 198, 642]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[125]: text=[%], bbox=[320, 628, 344, 642]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[126]: text=51.66, bbox=[364, 628, 410, 642]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[127]: text=61.42, bbox=[437, 628, 480, 642]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[128]: text=118.9, bbox=[510, 628, 553, 642]
2026-08-10 11:11:52,500 INFO     29 [qwen-vl-text] coord item[129]: text=DLCOc SB, bbox=[109, 643, 180, 657]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[130]: text=[mmol/min/kPa], bbox=[218, 643, 344, 657]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[131]: text=8.34, bbox=[373, 643, 410, 657]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[132]: text=6.95, bbox=[445, 643, 480, 657]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[133]: text=83.4, bbox=[517, 643, 553, 657]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[134]: text=DLCO SB, bbox=[109, 658, 171, 672]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[135]: text=[mmol/min/kPa], bbox=[218, 658, 344, 672]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[136]: text=8.34, bbox=[373, 658, 410, 672]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[137]: text=6.95, bbox=[445, 658, 480, 672]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[138]: text=83.4, bbox=[517, 658, 553, 672]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[139]: text=医生意见：, bbox=[87, 704, 190, 722]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[140]: text=1.中重度阻塞性通气功能障碍。, bbox=[87, 726, 328, 739]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[141]: text=检查质量：FVC：A级 。 FEV1：A级 。, bbox=[87, 739, 401, 752]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[142]: text=备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。, bbox=[87, 751, 594, 764]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[143]: text=2.最大自主分钟通气量（MVV）轻度下降。, bbox=[87, 763, 410, 776]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[144]: text=备注：患者MVV配合佳。结果仅供参考，请结合临床分析。, bbox=[87, 775, 532, 788]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[145]: text=3.弥散功能在正常范围。4.残总比中度增高。, bbox=[87, 787, 435, 800]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[146]: text=审核医生：孙帅森, bbox=[555, 840, 697, 856]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[147]: text=检测技师：张青苹, bbox=[552, 860, 703, 876]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[148]: text=通气弥散B, bbox=[72, 905, 123, 914]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[149]: text=2025/4/11 15:18, bbox=[451, 905, 529, 914]
2026-08-10 11:11:52,501 INFO     29 [qwen-vl-text] coord item[150]: text=1/1, bbox=[901, 905, 914, 914]
2026-08-10 11:11:52,502 INFO     29 [qwen-vl-text] page=3 — 151/151 coords, api_time=37.6s
2026-08-10 11:11:52,502 INFO     29 [qwen-vl-text] new_positions (151):
[[3, 49.385, 80.92, 74.096, 86.726], [3, 49.385, 220.74499999999998, 86.726, 99.356], [3, 49.385, 142.79999999999998, 99.356, 111.14399999999999], [3, 49.385, 202.89499999999998, 111.14399999999999, 122.932], [3, 49.385, 104.72, 122.932, 133.878], [3, 283.815, 313.565, 74.096, 86.726], [3, 283.815, 313.565, 86.726, 99.356], [3, 283.815, 326.06, 99.356, 111.14399999999999], [3, 283.815, 313.565, 111.14399999999999, 122.932], [3, 64.855, 107.695, 159.138, 170.926], [3, 64.855, 107.695, 170.926, 183.55599999999998], [3, 221.935, 243.355, 145.666, 158.296], [3, 264.775, 329.03499999999997, 145.666, 158.296], [3, 249.30499999999998, 285.59999999999997, 159.98, 170.926], [3, 249.30499999999998, 285.59999999999997, 171.768, 183.55599999999998], [3, 64.855, 76.16, 197.87, 209.658], [3, 190.39999999999998, 204.67999999999998, 197.87, 209.658], [3, 221.935, 243.95, 197.87, 209.658], [3, 264.775, 285.59999999999997, 197.87, 209.658], [3, 303.45, 329.03499999999997, 197.87, 209.658], [3, 64.855, 76.16, 210.5, 222.28799999999998], [3, 169.575, 204.67999999999998, 210.5, 222.28799999999998], [3, 216.57999999999998, 243.95, 210.5, 222.28799999999998], [3, 260.015, 285.59999999999997, 210.5, 222.28799999999998], [3, 303.45, 329.03499999999997, 210.5, 222.28799999999998], [3, 64.855, 76.16, 223.13, 234.91799999999998], [3, 169.575, 204.67999999999998, 223.13, 234.91799999999998], [3, 221.935, 243.95, 223.13, 234.91799999999998], [3, 264.775, 285.59999999999997, 223.13, 234.91799999999998], [3, 303.45, 329.03499999999997, 223.13, 234.91799999999998], [3, 64.855, 80.92, 235.76, 247.548], [3, 190.39999999999998, 204.67999999999998, 235.76, 247.548], [3, 221.935, 243.95, 235.76, 247.548], [3, 264.775, 285.59999999999997, 235.76, 247.548], [3, 307.615, 329.03499999999997, 235.76, 247.548], [3, 64.855, 97.58, 248.39, 260.178], [3, 190.39999999999998, 204.67999999999998, 248.39, 260.178], [3, 221.935, 243.95, 248.39, 260.178], [3, 264.775, 285.59999999999997, 248.39, 260.178], [3, 307.615, 329.03499999999997, 248.39, 260.178], [3, 64.855, 80.92, 274.492, 286.28], [3, 190.39999999999998, 204.67999999999998, 274.492, 286.28], [3, 221.935, 243.95, 274.492, 286.28], [3, 264.775, 285.59999999999997, 274.492, 286.28], [3, 307.615, 329.03499999999997, 274.492, 286.28], [3, 64.855, 91.035, 287.122, 298.90999999999997], [3, 190.39999999999998, 204.67999999999998, 287.122, 298.90999999999997], [3, 221.935, 243.95, 287.122, 298.90999999999997], [3, 264.775, 285.59999999999997, 287.122, 298.90999999999997], [3, 307.615, 329.03499999999997, 287.122, 298.90999999999997], [3, 64.855, 124.94999999999999, 299.752, 311.53999999999996], [3, 190.39999999999998, 204.67999999999998, 299.752, 311.53999999999996], [3, 216.57999999999998, 243.95, 299.752, 311.53999999999996], [3, 260.015, 285.59999999999997, 299.752, 311.53999999999996], [3, 307.615, 329.03499999999997, 299.752, 311.53999999999996], [3, 64.855, 141.015, 312.382, 324.17], [3, 190.39999999999998, 204.67999999999998, 312.382, 324.17], [3, 216.57999999999998, 243.95, 312.382, 324.17], [3, 260.015, 285.59999999999997, 312.382, 324.17], [3, 307.615, 329.03499999999997, 312.382, 324.17], [3, 64.855, 80.92, 325.012, 336.8], [3, 179.69, 204.67999999999998, 325.012, 336.8], [3, 221.935, 243.95, 325.012, 336.8], [3, 260.015, 285.59999999999997, 325.012, 336.8], [3, 307.615, 329.03499999999997, 325.012, 336.8], [3, 64.855, 97.58, 337.642, 349.43], [3, 179.69, 204.67999999999998, 337.642, 349.43], [3, 221.935, 243.95, 337.642, 349.43], [3, 264.775, 285.59999999999997, 337.642, 349.43], [3, 307.615, 329.03499999999997, 337.642, 349.43], [3, 64.855, 97.58, 350.272, 362.06], [3, 179.69, 204.67999999999998, 350.272, 362.06], [3, 221.935, 243.95, 350.272, 362.06], [3, 264.775, 285.59999999999997, 350.272, 362.06], [3, 307.615, 329.03499999999997, 350.272, 362.06], [3, 64.855, 97.58, 362.902, 374.69], [3, 179.69, 204.67999999999998, 362.902, 374.69], [3, 221.935, 243.95, 362.902, 374.69], [3, 264.775, 285.59999999999997, 362.902, 374.69], [3, 307.615, 329.03499999999997, 362.902, 374.69], [3, 64.855, 119.0, 375.532, 387.32], [3, 179.69, 204.67999999999998, 375.532, 387.32], [3, 221.935, 243.95, 375.532, 387.32], [3, 264.775, 285.59999999999997, 375.532, 387.32], [3, 307.615, 329.03499999999997, 375.532, 387.32], [3, 64.855, 80.92, 388.162, 399.95], [3, 190.39999999999998, 204.67999999999998, 388.162, 399.95], [3, 264.775, 285.59999999999997, 388.162, 399.95], [3, 64.855, 183.26, 400.792, 412.58], [3, 190.39999999999998, 204.67999999999998, 400.792, 412.58], [3, 264.775, 285.59999999999997, 400.792, 412.58], [3, 64.855, 178.5, 413.42199999999997, 425.21], [3, 190.39999999999998, 204.67999999999998, 413.42199999999997, 425.21], [3, 264.775, 285.59999999999997, 413.42199999999997, 425.21], [3, 64.855, 80.92, 439.524, 451.312], [3, 169.575, 204.67999999999998, 439.524, 451.312], [3, 211.82, 243.95, 439.524, 451.312], [3, 260.015, 285.59999999999997, 439.524, 451.312], [3, 307.615, 329.03499999999997, 439.524, 451.312], [3, 64.855, 107.695, 452.154, 463.942], [3, 169.575, 204.67999999999998, 452.154, 463.942], [3, 211.82, 243.95, 452.154, 463.942], [3, 260.015, 285.59999999999997, 452.154, 463.942], [3, 307.615, 329.03499999999997, 452.154, 463.942], [3, 64.855, 91.035, 478.256, 490.044], [3, 190.39999999999998, 204.67999999999998, 478.256, 490.044], [3, 221.935, 243.95, 478.256, 490.044], [3, 264.775, 285.59999999999997, 478.256, 490.044], [3, 303.45, 329.03499999999997, 478.256, 490.044], [3, 64.855, 113.05, 490.88599999999997, 502.674], [3, 190.39999999999998, 204.67999999999998, 490.88599999999997, 502.674], [3, 216.57999999999998, 243.95, 490.88599999999997, 502.674], [3, 260.015, 285.59999999999997, 490.88599999999997, 502.674], [3, 303.45, 329.03499999999997, 490.88599999999997, 502.674], [3, 64.855, 96.39, 503.51599999999996, 515.304], [3, 190.39999999999998, 204.67999999999998, 503.51599999999996, 515.304], [3, 221.935, 243.95, 503.51599999999996, 515.304], [3, 264.775, 285.59999999999997, 503.51599999999996, 515.304], [3, 303.45, 329.03499999999997, 503.51599999999996, 515.304], [3, 64.855, 96.39, 516.146, 527.934], [3, 190.39999999999998, 204.67999999999998, 516.146, 527.934], [3, 221.935, 243.95, 516.146, 527.934], [3, 264.775, 285.59999999999997, 516.146, 527.934], [3, 303.45, 329.03499999999997, 516.146, 527.934], [3, 64.855, 117.80999999999999, 528.776, 540.564], [3, 190.39999999999998, 204.67999999999998, 528.776, 540.564], [3, 216.57999999999998, 243.95, 528.776, 540.564], [3, 260.015, 285.59999999999997, 528.776, 540.564], [3, 303.45, 329.03499999999997, 528.776, 540.564], [3, 64.855, 107.1, 541.406, 553.194], [3, 129.71, 204.67999999999998, 541.406, 553.194], [3, 221.935, 243.95, 541.406, 553.194], [3, 264.775, 285.59999999999997, 541.406, 553.194], [3, 307.615, 329.03499999999997, 541.406, 553.194], [3, 64.855, 101.74499999999999, 554.036, 565.824], [3, 129.71, 204.67999999999998, 554.036, 565.824], [3, 221.935, 243.95, 554.036, 565.824], [3, 264.775, 285.59999999999997, 554.036, 565.824], [3, 307.615, 329.03499999999997, 554.036, 565.824], [3, 51.765, 113.05, 592.768, 607.924], [3, 51.765, 195.16, 611.292, 622.2379999999999], [3, 51.765, 238.595, 622.2379999999999, 633.184], [3, 51.765, 353.43, 632.342, 643.288], [3, 51.765, 243.95, 642.446, 653.3919999999999], [3, 51.765, 316.53999999999996, 652.55, 663.496], [3, 51.765, 258.825, 662.654, 673.6], [3, 330.22499999999997, 414.715, 707.28, 720.752], [3, 328.44, 418.28499999999997, 724.12, 737.592], [3, 42.839999999999996, 73.185, 762.01, 769.588], [3, 268.34499999999997, 314.755, 762.01, 769.588], [3, 536.095, 543.8299999999999, 762.01, 769.588]]
2026-08-10 11:11:52,502 INFO     29 [qwen-vl-text] ═══ DONE ═══ 151 positions, pages=1, time=81.7s
2026-08-10 11:11:52,502 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:11:52,510 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:11:52,510 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 11:11:52,510 INFO     29 [qwen-vl-text] positions(125): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:11:52,511 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [125]
2026-08-10 11:11:52,691 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:11:52,693 INFO     29 [qwen-vl-text] LLM extraction start, text_len=799
2026-08-10 11:11:52,693 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:52,693 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 584, \"bbox_end\": 708, \"encounter_dates\": [\"2025-04-11\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "肺功能报告单\n姓名：\n性别：女\n出生日期：1984/4/02\n年龄：41岁\n门诊/住院/体检：\n测试号：\n身高：160 cm\n体重：50 kg\n身份证号：\n预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n25/4/11\n25/4/11\n测试时间\n14:56:47下午\n15:14:32下午\nFVC\n[L]\n3.13\n2.84\n90.6\n3.05\n97.4\n7.5\nFEV 1\n[L]\n2.70\n1.53\n56.9\n1.91\n71.0\n24.7\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\n62.70\n74.7\n16.0\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\n62.70\n77.1\n16.0\nPEF\n[L/s]\n6.46\n4.56\n70.7\n5.64\n87.3\n23.6\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\n2.65\n46.3\n44.3\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\n1.23\n30.4\n47.0\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\n0.44\n25.0\n60.2\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\n1.02\n29.1\n58.8\nFET\n[s]\n8.46\n6.41\n-24.2\nV backextrapolation ex [L]\n0.03\n0.06\n71.7\nV backextrapol. % FVC [%]\n1.23\n1.96\n59.6\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V In\n医生意见：\n支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\nFEV1较基线增加大于12%，且绝对值增加大于200ml。）\n审核医生：孙帅森\n检测技师：张青苹",
    "role": "user"
  }
]
2026-08-10 11:11:52,954 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:11:52.953+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:11:53,753 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:53,767 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 11:11:53,768 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:11:53,768 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 11:11:53,782 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:11:53,784 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:11:53,784 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:11:53,784 INFO     29 [qwen-vl-text] positions(43): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:11:53,784 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [43]
2026-08-10 11:11:54,155 INFO     29 [qwen-vl-text] page=4, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:11:54,156 INFO     29 [qwen-vl-text] LLM extraction start, text_len=308
2026-08-10 11:11:54,156 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:54,156 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 126, \"bbox_end\": 168, \"encounter_dates\": [\"2025-09-15\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-09-15\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:64岁\n卡号:4\n患者\n医疗证号:\n处方号\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天\n倍氯米松福莫特罗吸入气雾剂◆\n6ug/揿*120揿\n221.61\n221.61\nSig\n2揿/次,吸入,bid*30天\n医师\n医生编号:1326\n配剂人:\n核对人:\n合计:\n收费员:\n打印时间:2025-12-19\n为了您的用药安全,药物处方当天有效 第 1 页共 1 页",
    "role": "user"
  }
]
2026-08-10 11:11:56,548 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:11:56,548 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "encounter_date": "2025-09-15",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": null
    }
  ]
}
2026-08-10 11:11:56,548 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-09-15]
2026-08-10 11:11:56,553 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2697300, prompt_len=1050
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["门(急)诊处方", "就诊时间:2025-09-15", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:4", "患者", "医疗证号:", "处方号", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天", "倍氯米松福莫特罗吸入气雾剂◆", "6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天", "医师", "医生编号:1326", "配剂人:", "核对人:", "合计:", "收费员:", "打印时间:2025-12-19", "为了您的用药安全,药物处方当天有效 第 1 页共 1 页"]

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
2026-08-10 11:12:09,355 INFO     29 [qwen-vl-text] coord API raw response (len=2179):
[
	{"text": "门(急)诊处方", "bbox": [383, 15, 617, 50]},
	{"text": "就诊时间:2025-09-15", "bbox": [48, 62, 287, 81]},
	{"text": "就诊科室:内科门诊", "bbox": [321, 62, 527, 82]},
	{"text": "主诊医", "bbox": [613, 64, 683, 84]},
	{"text": "姓名", "bbox": [48, 89, 94, 109]},
	{"text": "性别:男", "bbox": [321, 90, 407, 110]},
	{"text": "年龄:64岁", "bbox": [456, 91, 565, 110]},
	{"text": "卡号:4", "bbox": [613, 93, 683, 111]},
	{"text": "患者", "bbox": [48, 117, 94, 136]},
	{"text": "医疗证号:", "bbox": [321, 118, 427, 138]},
	{"text": "处方号", "bbox": [612, 121, 682, 140]},
	{"text": "地址:", "bbox": [48, 144, 101, 164]},
	{"text": "身份证号:", "bbox": [612, 148, 715, 168]},
	{"text": "诊断:支气管哮喘", "bbox": [48, 170, 226, 190]},
	{"text": "西药处方", "bbox": [435, 206, 566, 227]},
	{"text": "组号", "bbox": [112, 237, 160, 257]},
	{"text": "项目名称", "bbox": [218, 238, 316, 258]},
	{"text": "规格", "bbox": [509, 240, 553, 259]},
	{"text": "总量", "bbox": [713, 240, 760, 260]},
	{"text": "单价", "bbox": [818, 240, 864, 260]},
	{"text": "金额", "bbox": [900, 240, 946, 260]},
	{"text": "R:", "bbox": [67, 270, 112, 300]},
	{"text": "孟鲁司特钠片◆", "bbox": [199, 269, 365, 289]},
	{"text": "10mg*30/瓶", "bbox": [509, 271, 631, 291]},
	{"text": "30片", "bbox": [695, 272, 743, 291]},
	{"text": "1.05", "bbox": [800, 273, 850, 291]},
	{"text": "31.53", "bbox": [868, 273, 933, 291]},
	{"text": "Sig", "bbox": [426, 299, 466, 318]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [509, 300, 755, 320]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆", "bbox": [199, 325, 538, 345]},
	{"text": "6ug/揿*120揿", "bbox": [555, 326, 743, 346]},
	{"text": "221.61", "bbox": [770, 328, 850, 346]},
	{"text": "221.61", "bbox": [868, 328, 931, 346]},
	{"text": "Sig", "bbox": [426, 355, 466, 374]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [508, 355, 755, 374]},
	{"text": "医师", "bbox": [50, 607, 98, 627]},
	{"text": "医生编号:1326", "bbox": [353, 608, 514, 627]},
	{"text": "配剂人:", "bbox": [559, 608, 639, 627]},
	{"text": "核对人:", "bbox": [766, 608, 845, 627]},
	{"text": "合计:", "bbox": [57, 880, 112, 900]},
	{"text": "收费员:", "bbox": [269, 881, 350, 901]},
	{"text": "打印时间:2025-12-19", "bbox": [58, 905, 305, 924]},
	{"text": "为了您的用药安全,药物处方当天有效 第 1 页共 1 页", "bbox": [388, 904, 980, 924]}
]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=12.8s
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 15, 617, 50]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-09-15, bbox=[48, 62, 287, 81]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[321, 62, 527, 82]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[613, 64, 683, 84]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[48, 89, 94, 109]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[321, 90, 407, 110]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[456, 91, 565, 110]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:4, bbox=[613, 93, 683, 111]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[8]: text=患者, bbox=[48, 117, 94, 136]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[321, 118, 427, 138]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[10]: text=处方号, bbox=[612, 121, 682, 140]
2026-08-10 11:12:09,356 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[48, 144, 101, 164]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[612, 148, 715, 168]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[48, 170, 226, 190]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[435, 206, 566, 227]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[112, 237, 160, 257]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[218, 238, 316, 258]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[509, 240, 553, 259]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[713, 240, 760, 260]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[818, 240, 864, 260]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[900, 240, 946, 260]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[67, 270, 112, 300]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[199, 269, 365, 289]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*30/瓶, bbox=[509, 271, 631, 291]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[24]: text=30片, bbox=[695, 272, 743, 291]
2026-08-10 11:12:09,357 INFO     29 [qwen-vl-text] coord item[25]: text=1.05, bbox=[800, 273, 850, 291]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[26]: text=31.53, bbox=[868, 273, 933, 291]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[426, 299, 466, 318]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*30天, bbox=[509, 300, 755, 320]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂◆, bbox=[199, 325, 538, 345]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[30]: text=6ug/揿*120揿, bbox=[555, 326, 743, 346]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[31]: text=221.61, bbox=[770, 328, 850, 346]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[32]: text=221.61, bbox=[868, 328, 931, 346]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[33]: text=Sig, bbox=[426, 355, 466, 374]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[34]: text=2揿/次,吸入,bid*30天, bbox=[508, 355, 755, 374]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[35]: text=医师, bbox=[50, 607, 98, 627]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[36]: text=医生编号:1326, bbox=[353, 608, 514, 627]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[37]: text=配剂人:, bbox=[559, 608, 639, 627]
2026-08-10 11:12:09,358 INFO     29 [qwen-vl-text] coord item[38]: text=核对人:, bbox=[766, 608, 845, 627]
2026-08-10 11:12:09,359 INFO     29 [qwen-vl-text] coord item[39]: text=合计:, bbox=[57, 880, 112, 900]
2026-08-10 11:12:09,359 INFO     29 [qwen-vl-text] coord item[40]: text=收费员:, bbox=[269, 881, 350, 901]
2026-08-10 11:12:09,359 INFO     29 [qwen-vl-text] coord item[41]: text=打印时间:2025-12-19, bbox=[58, 905, 305, 924]
2026-08-10 11:12:09,359 INFO     29 [qwen-vl-text] coord item[42]: text=为了您的用药安全,药物处方当天有效 第 1 页共 1 页, bbox=[388, 904, 980, 924]
2026-08-10 11:12:09,361 INFO     29 [qwen-vl-text] page=4 — 43/43 coords, api_time=12.8s
2026-08-10 11:12:09,361 INFO     29 [qwen-vl-text] new_positions (43):
[[4, 227.885, 367.115, 12.629999999999999, 42.1], [4, 28.56, 170.765, 52.204, 68.202], [4, 190.995, 313.565, 52.204, 69.044], [4, 364.73499999999996, 406.385, 53.888, 70.728], [4, 28.56, 55.93, 74.938, 91.77799999999999], [4, 190.995, 242.165, 75.78, 92.61999999999999], [4, 271.32, 336.175, 76.622, 92.61999999999999], [4, 364.73499999999996, 406.385, 78.306, 93.462], [4, 28.56, 55.93, 98.514, 114.512], [4, 190.995, 254.065, 99.356, 116.196], [4, 364.14, 405.78999999999996, 101.88199999999999, 117.88], [4, 28.56, 60.095, 121.24799999999999, 138.088], [4, 364.14, 425.42499999999995, 124.616, 141.456], [4, 28.56, 134.47, 143.14, 159.98], [4, 258.825, 336.77, 173.452, 191.134], [4, 66.64, 95.19999999999999, 199.554, 216.394], [4, 129.71, 188.01999999999998, 200.396, 217.236], [4, 302.85499999999996, 329.03499999999997, 202.07999999999998, 218.078], [4, 424.23499999999996, 452.2, 202.07999999999998, 218.92], [4, 486.71, 514.0799999999999, 202.07999999999998, 218.92], [4, 535.5, 562.87, 202.07999999999998, 218.92], [4, 39.864999999999995, 66.64, 227.34, 252.6], [4, 118.405, 217.17499999999998, 226.498, 243.338], [4, 302.85499999999996, 375.445, 228.182, 245.022], [4, 413.525, 442.085, 229.024, 245.022], [4, 476.0, 505.75, 229.86599999999999, 245.022], [4, 516.4599999999999, 555.135, 229.86599999999999, 245.022], [4, 253.47, 277.27, 251.75799999999998, 267.756], [4, 302.85499999999996, 449.22499999999997, 252.6, 269.44], [4, 118.405, 320.11, 273.65, 290.49], [4, 330.22499999999997, 442.085, 274.492, 291.332], [4, 458.15, 505.75, 276.176, 291.332], [4, 516.4599999999999, 553.9449999999999, 276.176, 291.332], [4, 253.47, 277.27, 298.90999999999997, 314.908], [4, 302.26, 449.22499999999997, 298.90999999999997, 314.908], [4, 29.75, 58.309999999999995, 511.094, 527.934], [4, 210.035, 305.83, 511.936, 527.934], [4, 332.60499999999996, 380.205, 511.936, 527.934], [4, 455.77, 502.775, 511.936, 527.934], [4, 33.915, 66.64, 740.9599999999999, 757.8], [4, 160.055, 208.25, 741.802, 758.6419999999999], [4, 34.51, 181.475, 762.01, 778.0079999999999], [4, 230.85999999999999, 583.1, 761.168, 778.0079999999999]]
2026-08-10 11:12:09,361 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=15.6s
2026-08-10 11:12:09,361 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:12:09,364 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:12:09,364 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:12:09,364 INFO     29 [qwen-vl-text] positions(34): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:12:09,364 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [34]
2026-08-10 11:12:09,549 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:12:09,551 INFO     29 [qwen-vl-text] LLM extraction start, text_len=239
2026-08-10 11:12:09,551 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:09,552 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 171, \"bbox_end\": 204, \"encounter_dates\": [\"2025-08-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-08-18\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*30/瓶\n28片\n1.05\n29.43\nSig\n10mg/次,口服,qn*28天\n倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿\n221.61\n221.61\nSig\n2揿/次,吸入,bid*30天",
    "role": "user"
  }
]
2026-08-10 11:12:09,558 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:09,558 INFO     29 [qwen-vl-text] LLM output (len=1114):
{
  "exam_date": "2025-04-11",
  "report_date": "2025-04-11",
  "exam_name": "肺功能检查",
  "exam_category": "other",
  "body_part": "肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "预计\n实1 %(实1/预)\n实2 %(实2/预)\n变异率\n测试日期\n25/4/11\n25/4/11\n测试时间\n14:56:47下午\n15:14:32下午\nFVC\n[L]\n3.13\n2.84\n90.6\n3.05\n97.4\n7.5\nFEV 1\n[L]\n2.70\n1.53\n56.9\n1.91\n71.0\n24.7\nFEV 1 % FVC\n[%]\n83.98\n54.07\n64.4\n62.70\n74.7\n16.0\nFEV 1 % VC MAX\n[%]\n81.31\n54.07\n66.5\n62.70\n77.1\n16.0\nPEF\n[L/s]\n6.46\n4.56\n70.7\n5.64\n87.3\n23.6\nMEF 75\n[L/s]\n5.73\n1.84\n32.1\n2.65\n46.3\n44.3\nMEF 50\n[L/s]\n4.06\n0.84\n20.7\n1.23\n30.4\n47.0\nMEF 25\n[L/s]\n1.77\n0.28\n15.6\n0.44\n25.0\n60.2\nMMEF 75/25\n[L/s]\n3.53\n0.65\n18.3\n1.02\n29.1\n58.8\nFET\n[s]\n8.46\n6.41\n-24.2\nV backextrapolation ex [L]\n0.03\n0.06\n71.7\nV backextrapol. % FVC [%]\n1.23\n1.96\n59.6\nFlow [L/s]\nF/V ex\n10\n5\n0\n1\n2\n3\n4\n5\n6\n7\n10\nF/V In",
  "conclusion": "支气管舒张试验阳性。\n（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。\nFEV1较基线增加大于12%，且绝对值增加大于200ml。）",
  "physician": "张青苹",
  "reviewer": "孙帅森"
}
2026-08-10 11:12:09,559 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=737988, prompt_len=1788
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共125行）
["肺功能报告单", "姓名：", "性别：女", "出生日期：1984/4/02", "年龄：41岁", "门诊/住院/体检：", "测试号：", "身高：160 cm", "体重：50 kg", "身份证号：", "预计", "实1 %(实1/预)", "实2 %(实2/预)", "变异率", "测试日期", "25/4/11", "25/4/11", "测试时间", "14:56:47下午", "15:14:32下午", "FVC", "[L]", "3.13", "2.84", "90.6", "3.05", "97.4", "7.5", "FEV 1", "[L]", "2.70", "1.53", "56.9", "1.91", "71.0", "24.7", "FEV 1 % FVC", "[%]", "83.98", "54.07", "64.4", "62.70", "74.7", "16.0", "FEV 1 % VC MAX", "[%]", "81.31", "54.07", "66.5", "62.70", "77.1", "16.0", "PEF", "[L/s]", "6.46", "4.56", "70.7", "5.64", "87.3", "23.6", "MEF 75", "[L/s]", "5.73", "1.84", "32.1", "2.65", "46.3", "44.3", "MEF 50", "[L/s]", "4.06", "0.84", "20.7", "1.23", "30.4", "47.0", "MEF 25", "[L/s]", "1.77", "0.28", "15.6", "0.44", "25.0", "60.2", "MMEF 75/25", "[L/s]", "3.53", "0.65", "18.3", "1.02", "29.1", "58.8", "FET", "[s]", "8.46", "6.41", "-24.2", "V backextrapolation ex [L]", "0.03", "0.06", "71.7", "V backextrapol. % FVC [%]", "1.23", "1.96", "59.6", "Flow [L/s]", "F/V ex", "10", "5", "0", "1", "2", "3", "4", "5", "6", "7", "10", "F/V In", "医生意见：", "支气管舒张试验阳性。", "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "审核医生：孙帅森", "检测技师：张青苹"]

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
2026-08-10 11:12:41,650 INFO     29 [qwen-vl-text] coord API raw response (len=6457):
[
	{"text": "肺功能报告单", "bbox": [407, 83, 554, 102]},
	{"text": "姓名：", "bbox": [76, 104, 130, 117]},
	{"text": "性别：", "bbox": [481, 104, 535, 117]},
	{"text": "出生日期：", "bbox": [76, 117, 171, 131]},
	{"text": "1984/4/02", "bbox": [273, 119, 371, 131]},
	{"text": "年龄：", "bbox": [481, 117, 535, 131]},
	{"text": "41岁", "bbox": [680, 117, 733, 131]},
	{"text": "门诊/住院/体检：", "bbox": [76, 131, 237, 145]},
	{"text": "测试号：", "bbox": [481, 131, 555, 145]},
	{"text": "身高：", "bbox": [76, 145, 130, 158]},
	{"text": "160 cm", "bbox": [273, 147, 340, 159]},
	{"text": "体重：", "bbox": [481, 145, 535, 158]},
	{"text": "50 kg", "bbox": [680, 147, 734, 160]},
	{"text": "身份证号：", "bbox": [76, 158, 171, 172]},
	{"text": "预计", "bbox": [340, 179, 377, 193]},
	{"text": "实1 %(实1/预)", "bbox": [462, 179, 580, 193]},
	{"text": "实2 %(实2/预)", "bbox": [666, 179, 784, 193]},
	{"text": "变异率", "bbox": [814, 179, 870, 193]},
	{"text": "测试日期", "bbox": [87, 195, 161, 209]},
	{"text": "25/4/11", "bbox": [428, 196, 490, 209]},
	{"text": "25/4/11", "bbox": [632, 196, 694, 209]},
	{"text": "测试时间", "bbox": [87, 210, 161, 224]},
	{"text": "14:56:47下午", "bbox": [387, 210, 493, 224]},
	{"text": "15:14:32下午", "bbox": [589, 210, 696, 224]},
	{"text": "FVC", "bbox": [87, 243, 124, 256]},
	{"text": "[L]", "bbox": [292, 243, 315, 258]},
	{"text": "3.13", "bbox": [340, 243, 377, 256]},
	{"text": "2.84", "bbox": [454, 243, 491, 256]},
	{"text": "90.6", "bbox": [543, 243, 580, 256]},
	{"text": "3.05", "bbox": [658, 243, 695, 256]},
	{"text": "97.4", "bbox": [747, 243, 784, 256]},
	{"text": "7.5", "bbox": [845, 243, 871, 256]},
	{"text": "FEV 1", "bbox": [87, 258, 137, 272]},
	{"text": "[L]", "bbox": [292, 258, 315, 273]},
	{"text": "2.70", "bbox": [340, 258, 377, 272]},
	{"text": "1.53", "bbox": [454, 258, 491, 272]},
	{"text": "56.9", "bbox": [543, 258, 580, 272]},
	{"text": "1.91", "bbox": [658, 258, 695, 272]},
	{"text": "71.0", "bbox": [747, 258, 784, 272]},
	{"text": "24.7", "bbox": [835, 258, 871, 272]},
	{"text": "FEV 1 % FVC", "bbox": [87, 274, 200, 288]},
	{"text": "[%]", "bbox": [287, 274, 315, 289]},
	{"text": "83.98", "bbox": [330, 274, 377, 288]},
	{"text": "54.07", "bbox": [444, 274, 491, 288]},
	{"text": "64.4", "bbox": [543, 274, 580, 288]},
	{"text": "62.70", "bbox": [648, 274, 695, 288]},
	{"text": "74.7", "bbox": [747, 274, 784, 288]},
	{"text": "16.0", "bbox": [835, 274, 871, 288]},
	{"text": "FEV 1 % VC MAX", "bbox": [87, 290, 235, 304]},
	{"text": "[%]", "bbox": [287, 290, 315, 305]},
	{"text": "81.31", "bbox": [330, 290, 377, 304]},
	{"text": "54.07", "bbox": [444, 290, 491, 304]},
	{"text": "66.5", "bbox": [543, 290, 580, 304]},
	{"text": "62.70", "bbox": [648, 290, 695, 304]},
	{"text": "77.1", "bbox": [747, 290, 784, 304]},
	{"text": "16.0", "bbox": [835, 290, 871, 304]},
	{"text": "PEF", "bbox": [87, 306, 124, 320]},
	{"text": "[L/s]", "bbox": [276, 306, 315, 321]},
	{"text": "6.46", "bbox": [340, 306, 377, 320]},
	{"text": "4.56", "bbox": [454, 306, 491, 320]},
	{"text": "70.7", "bbox": [543, 306, 580, 320]},
	{"text": "5.64", "bbox": [658, 306, 695, 320]},
	{"text": "87.3", "bbox": [747, 306, 784, 320]},
	{"text": "23.6", "bbox": [835, 306, 871, 320]},
	{"text": "MEF 75", "bbox": [87, 322, 151, 336]},
	{"text": "[L/s]", "bbox": [276, 322, 315, 337]},
	{"text": "5.73", "bbox": [340, 322, 377, 336]},
	{"text": "1.84", "bbox": [454, 322, 491, 336]},
	{"text": "32.1", "bbox": [543, 322, 580, 336]},
	{"text": "2.65", "bbox": [658, 322, 695, 336]},
	{"text": "46.3", "bbox": [747, 322, 784, 336]},
	{"text": "44.3", "bbox": [835, 322, 871, 336]},
	{"text": "MEF 50", "bbox": [87, 338, 151, 352]},
	{"text": "[L/s]", "bbox": [276, 338, 315, 353]},
	{"text": "4.06", "bbox": [340, 338, 377, 352]},
	{"text": "0.84", "bbox": [454, 338, 491, 352]},
	{"text": "20.7", "bbox": [543, 338, 580, 352]},
	{"text": "1.23", "bbox": [658, 338, 695, 352]},
	{"text": "30.4", "bbox": [747, 338, 784, 352]},
	{"text": "47.0", "bbox": [835, 338, 871, 352]},
	{"text": "MEF 25", "bbox": [87, 354, 151, 368]},
	{"text": "[L/s]", "bbox": [276, 354, 315, 369]},
	{"text": "1.77", "bbox": [340, 354, 377, 368]},
	{"text": "0.28", "bbox": [454, 354, 491, 368]},
	{"text": "15.6", "bbox": [543, 354, 580, 368]},
	{"text": "0.44", "bbox": [658, 354, 695, 368]},
	{"text": "25.0", "bbox": [747, 354, 784, 368]},
	{"text": "60.2", "bbox": [835, 354, 871, 368]},
	{"text": "MMEF 75/25", "bbox": [87, 370, 192, 384]},
	{"text": "[L/s]", "bbox": [276, 370, 315, 385]},
	{"text": "3.53", "bbox": [340, 370, 377, 384]},
	{"text": "0.65", "bbox": [454, 370, 491, 384]},
	{"text": "18.3", "bbox": [543, 370, 580, 384]},
	{"text": "1.02", "bbox": [658, 370, 695, 384]},
	{"text": "29.1", "bbox": [747, 370, 784, 384]},
	{"text": "58.8", "bbox": [835, 370, 871, 384]},
	{"text": "FET", "bbox": [87, 386, 124, 400]},
	{"text": "[s]", "bbox": [292, 386, 315, 401]},
	{"text": "8.46", "bbox": [454, 386, 491, 400]},
	{"text": "6.41", "bbox": [658, 386, 695, 400]},
	{"text": "-24.2", "bbox": [829, 386, 871, 400]},
	{"text": "V backextrapolation ex [L]", "bbox": [87, 402, 315, 416]},
	{"text": "0.03", "bbox": [454, 402, 491, 416]},
	{"text": "0.06", "bbox": [658, 402, 695, 416]},
	{"text": "71.7", "bbox": [835, 402, 871, 416]},
	{"text": "V backextrapol. % FVC [%]", "bbox": [87, 417, 315, 432]},
	{"text": "1.23", "bbox": [454, 417, 491, 432]},
	{"text": "1.96", "bbox": [658, 417, 695, 432]},
	{"text": "59.6", "bbox": [835, 417, 871, 432]},
	{"text": "Flow [L/s]", "bbox": [142, 503, 193, 513]},
	{"text": "F/V ex", "bbox": [589, 504, 622, 513]},
	{"text": "10", "bbox": [124, 520, 139, 529]},
	{"text": "5", "bbox": [129, 548, 139, 557]},
	{"text": "0", "bbox": [129, 575, 137, 584]},
	{"text": "1", "bbox": [224, 584, 231, 592]},
	{"text": "2", "bbox": [310, 584, 318, 592]},
	{"text": "3", "bbox": [396, 584, 404, 592]},
	{"text": "4", "bbox": [483, 584, 491, 592]},
	{"text": "5", "bbox": [570, 584, 578, 592]},
	{"text": "6", "bbox": [658, 584, 667, 592]},
	{"text": "7", "bbox": [747, 584, 755, 592]},
	{"text": "10", "bbox": [124, 629, 139, 638]},
	{"text": "F/V In", "bbox": [589, 646, 619, 655]},
	{"text": "医生意见：", "bbox": [84, 666, 190, 684]},
	{"text": "支气管舒张试验阳性。", "bbox": [84, 686, 257, 699]},
	{"text": "（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。", "bbox": [92, 699, 493, 711]},
	{"text": "FEV1较基线增加大于12%，且绝对值增加大于200ml。）", "bbox": [84, 711, 513, 723]},
	{"text": "审核医生：孙帅森", "bbox": [645, 795, 783, 810]},
	{"text": "检测技师：张青苹", "bbox": [641, 818, 800, 840]}
]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord API: raw_items=129, valid_items=129, elapsed=32.1s
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[0]: text=肺功能报告单, bbox=[407, 83, 554, 102]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[76, 104, 130, 117]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[2]: text=性别：, bbox=[481, 104, 535, 117]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[3]: text=出生日期：, bbox=[76, 117, 171, 131]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[4]: text=1984/4/02, bbox=[273, 119, 371, 131]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：, bbox=[481, 117, 535, 131]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[6]: text=41岁, bbox=[680, 117, 733, 131]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[7]: text=门诊/住院/体检：, bbox=[76, 131, 237, 145]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[8]: text=测试号：, bbox=[481, 131, 555, 145]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[9]: text=身高：, bbox=[76, 145, 130, 158]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[10]: text=160 cm, bbox=[273, 147, 340, 159]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[11]: text=体重：, bbox=[481, 145, 535, 158]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[12]: text=50 kg, bbox=[680, 147, 734, 160]
2026-08-10 11:12:41,651 INFO     29 [qwen-vl-text] coord item[13]: text=身份证号：, bbox=[76, 158, 171, 172]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[14]: text=预计, bbox=[340, 179, 377, 193]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[15]: text=实1 %(实1/预), bbox=[462, 179, 580, 193]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[16]: text=实2 %(实2/预), bbox=[666, 179, 784, 193]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[17]: text=变异率, bbox=[814, 179, 870, 193]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[18]: text=测试日期, bbox=[87, 195, 161, 209]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[19]: text=25/4/11, bbox=[428, 196, 490, 209]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[20]: text=25/4/11, bbox=[632, 196, 694, 209]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[21]: text=测试时间, bbox=[87, 210, 161, 224]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[22]: text=14:56:47下午, bbox=[387, 210, 493, 224]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[23]: text=15:14:32下午, bbox=[589, 210, 696, 224]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[24]: text=FVC, bbox=[87, 243, 124, 256]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[25]: text=[L], bbox=[292, 243, 315, 258]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[26]: text=3.13, bbox=[340, 243, 377, 256]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[27]: text=2.84, bbox=[454, 243, 491, 256]
2026-08-10 11:12:41,652 INFO     29 [qwen-vl-text] coord item[28]: text=90.6, bbox=[543, 243, 580, 256]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[29]: text=3.05, bbox=[658, 243, 695, 256]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[30]: text=97.4, bbox=[747, 243, 784, 256]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[31]: text=7.5, bbox=[845, 243, 871, 256]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[32]: text=FEV 1, bbox=[87, 258, 137, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[33]: text=[L], bbox=[292, 258, 315, 273]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[34]: text=2.70, bbox=[340, 258, 377, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[35]: text=1.53, bbox=[454, 258, 491, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[36]: text=56.9, bbox=[543, 258, 580, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[37]: text=1.91, bbox=[658, 258, 695, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[38]: text=71.0, bbox=[747, 258, 784, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[39]: text=24.7, bbox=[835, 258, 871, 272]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[40]: text=FEV 1 % FVC, bbox=[87, 274, 200, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[41]: text=[%], bbox=[287, 274, 315, 289]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[42]: text=83.98, bbox=[330, 274, 377, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[43]: text=54.07, bbox=[444, 274, 491, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[44]: text=64.4, bbox=[543, 274, 580, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[45]: text=62.70, bbox=[648, 274, 695, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[46]: text=74.7, bbox=[747, 274, 784, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[47]: text=16.0, bbox=[835, 274, 871, 288]
2026-08-10 11:12:41,653 INFO     29 [qwen-vl-text] coord item[48]: text=FEV 1 % VC MAX, bbox=[87, 290, 235, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[49]: text=[%], bbox=[287, 290, 315, 305]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[50]: text=81.31, bbox=[330, 290, 377, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[51]: text=54.07, bbox=[444, 290, 491, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[52]: text=66.5, bbox=[543, 290, 580, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[53]: text=62.70, bbox=[648, 290, 695, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[54]: text=77.1, bbox=[747, 290, 784, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[55]: text=16.0, bbox=[835, 290, 871, 304]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[56]: text=PEF, bbox=[87, 306, 124, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[57]: text=[L/s], bbox=[276, 306, 315, 321]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[58]: text=6.46, bbox=[340, 306, 377, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[59]: text=4.56, bbox=[454, 306, 491, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[60]: text=70.7, bbox=[543, 306, 580, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[61]: text=5.64, bbox=[658, 306, 695, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[62]: text=87.3, bbox=[747, 306, 784, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[63]: text=23.6, bbox=[835, 306, 871, 320]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[64]: text=MEF 75, bbox=[87, 322, 151, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[65]: text=[L/s], bbox=[276, 322, 315, 337]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[66]: text=5.73, bbox=[340, 322, 377, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[67]: text=1.84, bbox=[454, 322, 491, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[68]: text=32.1, bbox=[543, 322, 580, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[69]: text=2.65, bbox=[658, 322, 695, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[70]: text=46.3, bbox=[747, 322, 784, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[71]: text=44.3, bbox=[835, 322, 871, 336]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[72]: text=MEF 50, bbox=[87, 338, 151, 352]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[73]: text=[L/s], bbox=[276, 338, 315, 353]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[74]: text=4.06, bbox=[340, 338, 377, 352]
2026-08-10 11:12:41,654 INFO     29 [qwen-vl-text] coord item[75]: text=0.84, bbox=[454, 338, 491, 352]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[76]: text=20.7, bbox=[543, 338, 580, 352]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[77]: text=1.23, bbox=[658, 338, 695, 352]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[78]: text=30.4, bbox=[747, 338, 784, 352]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[79]: text=47.0, bbox=[835, 338, 871, 352]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[80]: text=MEF 25, bbox=[87, 354, 151, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[81]: text=[L/s], bbox=[276, 354, 315, 369]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[82]: text=1.77, bbox=[340, 354, 377, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[83]: text=0.28, bbox=[454, 354, 491, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[84]: text=15.6, bbox=[543, 354, 580, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[85]: text=0.44, bbox=[658, 354, 695, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[86]: text=25.0, bbox=[747, 354, 784, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[87]: text=60.2, bbox=[835, 354, 871, 368]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[88]: text=MMEF 75/25, bbox=[87, 370, 192, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[89]: text=[L/s], bbox=[276, 370, 315, 385]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[90]: text=3.53, bbox=[340, 370, 377, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[91]: text=0.65, bbox=[454, 370, 491, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[92]: text=18.3, bbox=[543, 370, 580, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[93]: text=1.02, bbox=[658, 370, 695, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[94]: text=29.1, bbox=[747, 370, 784, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[95]: text=58.8, bbox=[835, 370, 871, 384]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[96]: text=FET, bbox=[87, 386, 124, 400]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[97]: text=[s], bbox=[292, 386, 315, 401]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[98]: text=8.46, bbox=[454, 386, 491, 400]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[99]: text=6.41, bbox=[658, 386, 695, 400]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[100]: text=-24.2, bbox=[829, 386, 871, 400]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[101]: text=V backextrapolation ex [L], bbox=[87, 402, 315, 416]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[102]: text=0.03, bbox=[454, 402, 491, 416]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[103]: text=0.06, bbox=[658, 402, 695, 416]
2026-08-10 11:12:41,655 INFO     29 [qwen-vl-text] coord item[104]: text=71.7, bbox=[835, 402, 871, 416]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[105]: text=V backextrapol. % FVC [%], bbox=[87, 417, 315, 432]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[106]: text=1.23, bbox=[454, 417, 491, 432]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[107]: text=1.96, bbox=[658, 417, 695, 432]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[108]: text=59.6, bbox=[835, 417, 871, 432]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[109]: text=Flow [L/s], bbox=[142, 503, 193, 513]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[110]: text=F/V ex, bbox=[589, 504, 622, 513]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[111]: text=10, bbox=[124, 520, 139, 529]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[112]: text=5, bbox=[129, 548, 139, 557]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[113]: text=0, bbox=[129, 575, 137, 584]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[114]: text=1, bbox=[224, 584, 231, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[115]: text=2, bbox=[310, 584, 318, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[116]: text=3, bbox=[396, 584, 404, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[117]: text=4, bbox=[483, 584, 491, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[118]: text=5, bbox=[570, 584, 578, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[119]: text=6, bbox=[658, 584, 667, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[120]: text=7, bbox=[747, 584, 755, 592]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[121]: text=10, bbox=[124, 629, 139, 638]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[122]: text=F/V In, bbox=[589, 646, 619, 655]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[123]: text=医生意见：, bbox=[84, 666, 190, 684]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[124]: text=支气管舒张试验阳性。, bbox=[84, 686, 257, 699]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[125]: text=（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。, bbox=[92, 699, 493, 711]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[126]: text=FEV1较基线增加大于12%，且绝对值增加大于200ml。）, bbox=[84, 711, 513, 723]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[127]: text=审核医生：孙帅森, bbox=[645, 795, 783, 810]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] coord item[128]: text=检测技师：张青苹, bbox=[641, 818, 800, 840]
2026-08-10 11:12:41,656 INFO     29 [qwen-vl-text] page=4 — 125/125 coords, api_time=32.1s
2026-08-10 11:12:41,657 INFO     29 [qwen-vl-text] new_positions (125):
[[4, 242.165, 329.63, 69.886, 85.884], [4, 45.22, 77.35, 87.568, 98.514], [4, 286.195, 318.325, 87.568, 98.514], [4, 45.22, 101.74499999999999, 98.514, 110.30199999999999], [4, 162.435, 220.74499999999998, 100.198, 110.30199999999999], [4, 286.195, 318.325, 98.514, 110.30199999999999], [4, 404.59999999999997, 436.135, 98.514, 110.30199999999999], [4, 45.22, 141.015, 110.30199999999999, 122.08999999999999], [4, 286.195, 330.22499999999997, 110.30199999999999, 122.08999999999999], [4, 45.22, 77.35, 122.08999999999999, 133.036], [4, 162.435, 202.29999999999998, 123.774, 133.878], [4, 286.195, 318.325, 122.08999999999999, 133.036], [4, 404.59999999999997, 436.72999999999996, 123.774, 134.72], [4, 45.22, 101.74499999999999, 133.036, 144.82399999999998], [4, 202.29999999999998, 224.315, 150.718, 162.506], [4, 274.89, 345.09999999999997, 150.718, 162.506], [4, 396.27, 466.47999999999996, 150.718, 162.506], [4, 484.33, 517.65, 150.718, 162.506], [4, 51.765, 95.795, 164.19, 175.97799999999998], [4, 254.66, 291.55, 165.03199999999998, 175.97799999999998], [4, 376.03999999999996, 412.93, 165.03199999999998, 175.97799999999998], [4, 51.765, 95.795, 176.82, 188.608], [4, 230.265, 293.335, 176.82, 188.608], [4, 350.455, 414.12, 176.82, 188.608], [4, 51.765, 73.78, 204.606, 215.552], [4, 173.73999999999998, 187.42499999999998, 204.606, 217.236], [4, 202.29999999999998, 224.315, 204.606, 215.552], [4, 270.13, 292.145, 204.606, 215.552], [4, 323.085, 345.09999999999997, 204.606, 215.552], [4, 391.51, 413.525, 204.606, 215.552], [4, 444.465, 466.47999999999996, 204.606, 215.552], [4, 502.775, 518.245, 204.606, 215.552], [4, 51.765, 81.515, 217.236, 229.024], [4, 173.73999999999998, 187.42499999999998, 217.236, 229.86599999999999], [4, 202.29999999999998, 224.315, 217.236, 229.024], [4, 270.13, 292.145, 217.236, 229.024], [4, 323.085, 345.09999999999997, 217.236, 229.024], [4, 391.51, 413.525, 217.236, 229.024], [4, 444.465, 466.47999999999996, 217.236, 229.024], [4, 496.825, 518.245, 217.236, 229.024], [4, 51.765, 119.0, 230.708, 242.49599999999998], [4, 170.765, 187.42499999999998, 230.708, 243.338], [4, 196.35, 224.315, 230.708, 242.49599999999998], [4, 264.18, 292.145, 230.708, 242.49599999999998], [4, 323.085, 345.09999999999997, 230.708, 242.49599999999998], [4, 385.56, 413.525, 230.708, 242.49599999999998], [4, 444.465, 466.47999999999996, 230.708, 242.49599999999998], [4, 496.825, 518.245, 230.708, 242.49599999999998], [4, 51.765, 139.825, 244.17999999999998, 255.968], [4, 170.765, 187.42499999999998, 244.17999999999998, 256.81], [4, 196.35, 224.315, 244.17999999999998, 255.968], [4, 264.18, 292.145, 244.17999999999998, 255.968], [4, 323.085, 345.09999999999997, 244.17999999999998, 255.968], [4, 385.56, 413.525, 244.17999999999998, 255.968], [4, 444.465, 466.47999999999996, 244.17999999999998, 255.968], [4, 496.825, 518.245, 244.17999999999998, 255.968], [4, 51.765, 73.78, 257.652, 269.44], [4, 164.22, 187.42499999999998, 257.652, 270.282], [4, 202.29999999999998, 224.315, 257.652, 269.44], [4, 270.13, 292.145, 257.652, 269.44], [4, 323.085, 345.09999999999997, 257.652, 269.44], [4, 391.51, 413.525, 257.652, 269.44], [4, 444.465, 466.47999999999996, 257.652, 269.44], [4, 496.825, 518.245, 257.652, 269.44], [4, 51.765, 89.845, 271.12399999999997, 282.912], [4, 164.22, 187.42499999999998, 271.12399999999997, 283.75399999999996], [4, 202.29999999999998, 224.315, 271.12399999999997, 282.912], [4, 270.13, 292.145, 271.12399999999997, 282.912], [4, 323.085, 345.09999999999997, 271.12399999999997, 282.912], [4, 391.51, 413.525, 271.12399999999997, 282.912], [4, 444.465, 466.47999999999996, 271.12399999999997, 282.912], [4, 496.825, 518.245, 271.12399999999997, 282.912], [4, 51.765, 89.845, 284.596, 296.384], [4, 164.22, 187.42499999999998, 284.596, 297.226], [4, 202.29999999999998, 224.315, 284.596, 296.384], [4, 270.13, 292.145, 284.596, 296.384], [4, 323.085, 345.09999999999997, 284.596, 296.384], [4, 391.51, 413.525, 284.596, 296.384], [4, 444.465, 466.47999999999996, 284.596, 296.384], [4, 496.825, 518.245, 284.596, 296.384], [4, 51.765, 89.845, 298.068, 309.856], [4, 164.22, 187.42499999999998, 298.068, 310.698], [4, 202.29999999999998, 224.315, 298.068, 309.856], [4, 270.13, 292.145, 298.068, 309.856], [4, 323.085, 345.09999999999997, 298.068, 309.856], [4, 391.51, 413.525, 298.068, 309.856], [4, 444.465, 466.47999999999996, 298.068, 309.856], [4, 496.825, 518.245, 298.068, 309.856], [4, 51.765, 114.24, 311.53999999999996, 323.328], [4, 164.22, 187.42499999999998, 311.53999999999996, 324.17], [4, 202.29999999999998, 224.315, 311.53999999999996, 323.328], [4, 270.13, 292.145, 311.53999999999996, 323.328], [4, 323.085, 345.09999999999997, 311.53999999999996, 323.328], [4, 391.51, 413.525, 311.53999999999996, 323.328], [4, 444.465, 466.47999999999996, 311.53999999999996, 323.328], [4, 496.825, 518.245, 311.53999999999996, 323.328], [4, 51.765, 73.78, 325.012, 336.8], [4, 173.73999999999998, 187.42499999999998, 325.012, 337.642], [4, 270.13, 292.145, 325.012, 336.8], [4, 391.51, 413.525, 325.012, 336.8], [4, 493.255, 518.245, 325.012, 336.8], [4, 51.765, 187.42499999999998, 338.484, 350.272], [4, 270.13, 292.145, 338.484, 350.272], [4, 391.51, 413.525, 338.484, 350.272], [4, 496.825, 518.245, 338.484, 350.272], [4, 51.765, 187.42499999999998, 351.114, 363.74399999999997], [4, 270.13, 292.145, 351.114, 363.74399999999997], [4, 391.51, 413.525, 351.114, 363.74399999999997], [4, 496.825, 518.245, 351.114, 363.74399999999997], [4, 84.49, 114.835, 423.526, 431.94599999999997], [4, 350.455, 370.09, 424.368, 431.94599999999997], [4, 73.78, 82.705, 437.84, 445.418], [4, 76.755, 82.705, 461.416, 468.99399999999997], [4, 76.755, 81.515, 484.15, 491.728], [4, 133.28, 137.445, 491.728, 498.464], [4, 184.45, 189.20999999999998, 491.728, 498.464], [4, 235.61999999999998, 240.38, 491.728, 498.464], [4, 287.385, 292.145, 491.728, 498.464], [4, 339.15, 343.90999999999997, 491.728, 498.464], [4, 391.51, 396.865, 491.728, 498.464], [4, 444.465, 449.22499999999997, 491.728, 498.464], [4, 73.78, 82.705, 529.6179999999999, 537.196], [4, 350.455, 368.305, 543.932, 551.51], [4, 49.98, 113.05, 560.7719999999999, 575.928], [4, 49.98, 152.915, 577.612, 588.558]]
2026-08-10 11:12:41,657 INFO     29 [qwen-vl-text] ═══ DONE ═══ 125 positions, pages=1, time=49.2s
2026-08-10 11:12:41,958 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:12:41,960 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "2326 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Progress": "7 items, types={'ProgressNote': 7}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "5 items, types={'PrescriptionRecord': 5}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Progress\": 7, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 5, \"chunks_LabExam\": 13}"}
2026-08-10 11:12:41,961 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:12:41,964 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:12:41.961+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:12:41,981 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:12:41,983 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:12:41,983 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:12:41,984 INFO     29 [qwen-vl-text] positions(32): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:12:41,984 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [32]
2026-08-10 11:12:42,245 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:12:42,248 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1107
2026-08-10 11:12:42,248 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:42,249 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 869, \"bbox_end\": 900, \"encounter_dates\": [\"2020-07-08\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "姓名：\n科室：产科二区\n床号\n住院号.\n2020年07月08日 09时22分\n首次病程记录\n患\n女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于\n2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥\n感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日\n(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单\n活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正\n常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正\n常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求\n住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，\n精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、\n专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律\n齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02\n本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度\nII°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位\n待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，\n末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎\n动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎\n位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、\n辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm\n羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊\n断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检\n查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相\n关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、\n患者要求明日剖宫产，纳入剖宫产临床路径。\n主治医师：孙州\n2020年07月08日 10时22分",
    "role": "user"
  }
]
2026-08-10 11:12:44,678 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:44,678 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "encounter_date": "2025-08-18",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 28,
      "quantity": "28片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": null
    }
  ]
}
2026-08-10 11:12:44,678 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-08-18]
2026-08-10 11:12:44,681 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1559196, prompt_len=954
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门(急)诊处方", "就诊时间:2025-08-18", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*30/瓶", "28片", "1.05", "29.43", "Sig", "10mg/次,口服,qn*28天", "倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿", "221.61", "221.61", "Sig", "2揿/次,吸入,bid*30天"]

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
2026-08-10 11:12:55,822 INFO     29 [qwen-vl-text] coord API raw response (len=1730):
[
	{"text": "门(急)诊处方", "bbox": [383, 18, 617, 84]},
	{"text": "就诊时间:2025-08-18", "bbox": [50, 110, 287, 146]},
	{"text": "就诊科室:内科门诊", "bbox": [323, 110, 529, 147]},
	{"text": "主诊", "bbox": [615, 116, 661, 150]},
	{"text": "姓名:", "bbox": [50, 167, 105, 201]},
	{"text": "性别:男", "bbox": [324, 167, 410, 202]},
	{"text": "年龄:64岁", "bbox": [458, 169, 567, 204]},
	{"text": "卡号", "bbox": [615, 172, 660, 205]},
	{"text": "患者类型:GCP支付", "bbox": [51, 224, 250, 258]},
	{"text": "医疗证号:", "bbox": [325, 224, 430, 259]},
	{"text": "处方", "bbox": [614, 230, 660, 263]},
	{"text": "地址:", "bbox": [51, 278, 105, 313]},
	{"text": "身份证号:", "bbox": [614, 283, 715, 317]},
	{"text": "诊断:支气管哮喘", "bbox": [51, 330, 232, 365]},
	{"text": "西药处方", "bbox": [440, 394, 570, 430]},
	{"text": "组号", "bbox": [119, 459, 167, 493]},
	{"text": "项目名称", "bbox": [225, 459, 322, 494]},
	{"text": "规格", "bbox": [514, 460, 557, 493]},
	{"text": "总量", "bbox": [716, 462, 761, 496]},
	{"text": "单价", "bbox": [819, 462, 864, 496]},
	{"text": "金额", "bbox": [900, 460, 946, 494]},
	{"text": "R:", "bbox": [74, 524, 119, 578]},
	{"text": "孟鲁司特钠片◆", "bbox": [205, 519, 371, 554]},
	{"text": "10mg*30/瓶", "bbox": [514, 521, 635, 556]},
	{"text": "28片", "bbox": [698, 522, 744, 555]},
	{"text": "1.05", "bbox": [802, 524, 851, 554]},
	{"text": "29.43", "bbox": [870, 524, 934, 554]},
	{"text": "Sig", "bbox": [433, 574, 471, 607]},
	{"text": "10mg/次,口服,qn*28天", "bbox": [514, 568, 757, 609]},
	{"text": "倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿", "bbox": [204, 625, 746, 661]},
	{"text": "221.61", "bbox": [774, 630, 852, 660]},
	{"text": "221.61", "bbox": [858, 630, 931, 660]},
	{"text": "Sig", "bbox": [433, 682, 471, 715]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [513, 680, 758, 715]}
]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=11.1s
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 18, 617, 84]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-08-18, bbox=[50, 110, 287, 146]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[323, 110, 529, 147]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[615, 116, 661, 150]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[50, 167, 105, 201]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[324, 167, 410, 202]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[458, 169, 567, 204]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[615, 172, 660, 205]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[51, 224, 250, 258]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[325, 224, 430, 259]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[614, 230, 660, 263]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[51, 278, 105, 313]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[614, 283, 715, 317]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[51, 330, 232, 365]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[440, 394, 570, 430]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[119, 459, 167, 493]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[225, 459, 322, 494]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[514, 460, 557, 493]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[716, 462, 761, 496]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[819, 462, 864, 496]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[900, 460, 946, 494]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[74, 524, 119, 578]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[205, 519, 371, 554]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*30/瓶, bbox=[514, 521, 635, 556]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[24]: text=28片, bbox=[698, 522, 744, 555]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[25]: text=1.05, bbox=[802, 524, 851, 554]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[26]: text=29.43, bbox=[870, 524, 934, 554]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[433, 574, 471, 607]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*28天, bbox=[514, 568, 757, 609]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿, bbox=[204, 625, 746, 661]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[30]: text=221.61, bbox=[774, 630, 852, 660]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[31]: text=221.61, bbox=[858, 630, 931, 660]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[32]: text=Sig, bbox=[433, 682, 471, 715]
2026-08-10 11:12:55,823 INFO     29 [qwen-vl-text] coord item[33]: text=2揿/次,吸入,bid*30天, bbox=[513, 680, 758, 715]
2026-08-10 11:12:55,824 INFO     29 [qwen-vl-text] page=5 — 34/34 coords, api_time=11.1s
2026-08-10 11:12:55,824 INFO     29 [qwen-vl-text] new_positions (34):
[[5, 322.486, 519.514, 10.709999999999999, 49.98], [5, 42.1, 241.654, 65.45, 86.86999999999999], [5, 271.966, 445.418, 65.45, 87.46499999999999], [5, 517.8299999999999, 556.562, 69.02, 89.25], [5, 42.1, 88.41, 99.365, 119.595], [5, 272.808, 345.21999999999997, 99.365, 120.19], [5, 385.63599999999997, 477.414, 100.55499999999999, 121.38], [5, 517.8299999999999, 555.72, 102.33999999999999, 121.975], [5, 42.942, 210.5, 133.28, 153.51], [5, 273.65, 362.06, 133.28, 154.105], [5, 516.9879999999999, 555.72, 136.85, 156.48499999999999], [5, 42.942, 88.41, 165.41, 186.23499999999999], [5, 516.9879999999999, 602.03, 168.385, 188.61499999999998], [5, 42.942, 195.344, 196.35, 217.17499999999998], [5, 370.47999999999996, 479.94, 234.42999999999998, 255.85], [5, 100.198, 140.614, 273.10499999999996, 293.335], [5, 189.45, 271.12399999999997, 273.10499999999996, 293.93], [5, 432.788, 468.99399999999997, 273.7, 293.335], [5, 602.872, 640.762, 274.89, 295.12], [5, 689.598, 727.4879999999999, 274.89, 295.12], [5, 757.8, 796.5319999999999, 273.7, 293.93], [5, 62.308, 100.198, 311.78, 343.90999999999997], [5, 172.60999999999999, 312.382, 308.805, 329.63], [5, 432.788, 534.67, 309.995, 330.82], [5, 587.716, 626.448, 310.59, 330.22499999999997], [5, 675.284, 716.542, 311.78, 329.63], [5, 732.54, 786.428, 311.78, 329.63], [5, 364.586, 396.582, 341.53, 361.16499999999996], [5, 432.788, 637.394, 337.96, 362.35499999999996], [5, 171.768, 628.132, 371.875, 393.29499999999996], [5, 651.708, 717.384, 374.84999999999997, 392.7], [5, 722.4359999999999, 783.9019999999999, 374.84999999999997, 392.7], [5, 364.586, 396.582, 405.78999999999996, 425.42499999999995], [5, 431.94599999999997, 638.236, 404.59999999999997, 425.42499999999995]]
2026-08-10 11:12:55,824 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=46.5s
2026-08-10 11:12:55,824 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:12:55,825 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:12:55,825 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:12:55,825 INFO     29 [qwen-vl-text] positions(34): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:12:55,825 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [34]
2026-08-10 11:12:56,005 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:12:56,006 INFO     29 [qwen-vl-text] LLM extraction start, text_len=233
2026-08-10 11:12:56,006 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:56,006 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 205, \"bbox_end\": 238, \"encounter_dates\": [\"2025-05-30\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-05-30\n就诊科室:内科门诊\n主\n姓名\n性别:男\n年龄:64岁\n卡\n患者类型:GCP支付\n医疗证号:\n处\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n孟鲁司特钠片◆\n10mg*5/盒\n90片\n2.56\n230.58\nSig\n10mg/次,口服,qn*90天\n倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶\n221.61\n664.83\nSig\n2揿/次,吸入,bid*90天",
    "role": "user"
  }
]
2026-08-10 11:12:56,011 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:12:56,012 INFO     29 [qwen-vl-text] LLM output (len=1617):
{
  "note_type": "首次病程记录",
  "record_time": "2020-07-08 10:22",
  "recorder": null,
  "reviewer": "孙州",
  "reviewer_title": "主治医师",
  "cf_summary": "已婚育龄妇女，孕₂产₁，否认产后出血及产褥感染史，否认不良孕产史；平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合孕周。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛查，未查B族链球菌。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产。",
  "cf_positive_findings": [
    "T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg",
    "神志清楚，精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆",
    "宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水",
    "B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°"
  ],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": "1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": "根据据病史、查体及辅助检查，目前诊断明确。",
  "tp_examinations": [
    "心电图",
    "彩超",
    "血常规",
    "血型",
    "凝血五项",
    "输血前检查",
    "尿常规",
    "肝功",
    "肾功",
    "血糖",
    "电解质"
  ],
  "tp_treatments": [
    "向患者及家属交代病情，围生期相关危险因素",
    "给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理",
    "患者要求明日剖宫产，纳入剖宫产临床路径"
  ],
  "tp_notes": null,
  "condition_changes": null,
  "test_results": null,
  "superior_opinion": null,
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:12:56,014 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1448182, prompt_len=1816
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["姓名：", "科室：产科二区", "床号", "住院号.", "2020年07月08日 09时22分", "首次病程记录", "患", "女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于", "2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥", "感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日", "(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单", "活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正", "常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正", "常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求", "住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，", "精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、", "专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律", "齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02", "本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度", "II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位", "待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，", "末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎", "动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎", "位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、", "辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm", "羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊", "断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检", "查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相", "关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、", "患者要求明日剖宫产，纳入剖宫产临床路径。", "主治医师：孙州", "2020年07月08日 10时22分"]

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
2026-08-10 11:13:10,840 INFO     29 [qwen-vl-text] coord API raw response (len=2577):
[
	{"text": "姓名：", "bbox": [141, 117, 187, 133]},
	{"text": "科室：产科二区", "bbox": [322, 117, 453, 133]},
	{"text": "床号", "bbox": [520, 117, 555, 133]},
	{"text": "住院号.", "bbox": [690, 117, 750, 133]},
	{"text": "2020年07月08日 09时22分", "bbox": [132, 141, 347, 156]},
	{"text": "首次病程记录", "bbox": [458, 141, 569, 156]},
	{"text": "患", "bbox": [188, 167, 206, 182]},
	{"text": "女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于", "bbox": [296, 167, 893, 182]},
	{"text": "2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥", "bbox": [132, 192, 893, 208]},
	{"text": "感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日", "bbox": [132, 218, 893, 234]},
	{"text": "(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单", "bbox": [132, 244, 893, 260]},
	{"text": "活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正", "bbox": [132, 270, 893, 286]},
	{"text": "常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正", "bbox": [132, 296, 893, 312]},
	{"text": "常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求", "bbox": [132, 322, 893, 338]},
	{"text": "住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，", "bbox": [132, 348, 881, 365]},
	{"text": "精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、", "bbox": [132, 375, 881, 391]},
	{"text": "专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律", "bbox": [132, 401, 893, 417]},
	{"text": "齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02", "bbox": [132, 427, 874, 443]},
	{"text": "本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度", "bbox": [132, 453, 893, 470]},
	{"text": "II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位", "bbox": [132, 479, 884, 496]},
	{"text": "待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，", "bbox": [132, 505, 881, 522]},
	{"text": "末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎", "bbox": [132, 531, 893, 548]},
	{"text": "动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎", "bbox": [132, 558, 893, 574]},
	{"text": "位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、", "bbox": [132, 584, 881, 600]},
	{"text": "辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm", "bbox": [132, 610, 884, 627]},
	{"text": "羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊", "bbox": [132, 636, 893, 653]},
	{"text": "断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检", "bbox": [132, 663, 893, 679]},
	{"text": "查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相", "bbox": [132, 689, 893, 705]},
	{"text": "关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、", "bbox": [132, 715, 881, 731]},
	{"text": "患者要求明日剖宫产，纳入剖宫产临床路径。", "bbox": [132, 741, 492, 758]},
	{"text": "主治医师：孙州", "bbox": [651, 777, 826, 810]},
	{"text": "2020年07月08日 10时22分", "bbox": [131, 823, 345, 839]},
	{"text": "科主任宋瑞香主治医师查房记录", "bbox": [427, 823, 688, 839]}
]
2026-08-10 11:13:10,841 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=14.8s
2026-08-10 11:13:10,841 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[141, 117, 187, 133]
2026-08-10 11:13:10,841 INFO     29 [qwen-vl-text] coord item[1]: text=科室：产科二区, bbox=[322, 117, 453, 133]
2026-08-10 11:13:10,841 INFO     29 [qwen-vl-text] coord item[2]: text=床号, bbox=[520, 117, 555, 133]
2026-08-10 11:13:10,841 INFO     29 [qwen-vl-text] coord item[3]: text=住院号., bbox=[690, 117, 750, 133]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[4]: text=2020年07月08日 09时22分, bbox=[132, 141, 347, 156]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[5]: text=首次病程记录, bbox=[458, 141, 569, 156]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[6]: text=患, bbox=[188, 167, 206, 182]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[7]: text=女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于, bbox=[296, 167, 893, 182]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[8]: text=2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥, bbox=[132, 192, 893, 208]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[9]: text=感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日, bbox=[132, 218, 893, 234]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[10]: text=(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单, bbox=[132, 244, 893, 260]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[11]: text=活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正, bbox=[132, 270, 893, 286]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[12]: text=常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正, bbox=[132, 296, 893, 312]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[13]: text=常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求, bbox=[132, 322, 893, 338]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[14]: text=住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，, bbox=[132, 348, 881, 365]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[15]: text=精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、, bbox=[132, 375, 881, 391]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[16]: text=专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律, bbox=[132, 401, 893, 417]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[17]: text=齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02, bbox=[132, 427, 874, 443]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[18]: text=本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度, bbox=[132, 453, 893, 470]
2026-08-10 11:13:10,842 INFO     29 [qwen-vl-text] coord item[19]: text=II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位, bbox=[132, 479, 884, 496]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[20]: text=待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，, bbox=[132, 505, 881, 522]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[21]: text=末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎, bbox=[132, 531, 893, 548]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[22]: text=动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎, bbox=[132, 558, 893, 574]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[23]: text=位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、, bbox=[132, 584, 881, 600]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[24]: text=辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm, bbox=[132, 610, 884, 627]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[25]: text=羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊, bbox=[132, 636, 893, 653]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[26]: text=断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检, bbox=[132, 663, 893, 679]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[27]: text=查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相, bbox=[132, 689, 893, 705]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[28]: text=关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、, bbox=[132, 715, 881, 731]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[29]: text=患者要求明日剖宫产，纳入剖宫产临床路径。, bbox=[132, 741, 492, 758]
2026-08-10 11:13:10,843 INFO     29 [qwen-vl-text] coord item[30]: text=主治医师：孙州, bbox=[651, 777, 826, 810]
2026-08-10 11:13:10,844 INFO     29 [qwen-vl-text] coord item[31]: text=2020年07月08日 10时22分, bbox=[131, 823, 345, 839]
2026-08-10 11:13:10,844 INFO     29 [qwen-vl-text] coord item[32]: text=科主任宋瑞香主治医师查房记录, bbox=[427, 823, 688, 839]
2026-08-10 11:13:10,844 INFO     29 [qwen-vl-text] page=9 — 32/32 coords, api_time=14.8s
2026-08-10 11:13:10,845 INFO     29 [qwen-vl-text] new_positions (32):
[[9, 83.895, 111.265, 98.514, 111.98599999999999], [9, 191.59, 269.53499999999997, 98.514, 111.98599999999999], [9, 309.4, 330.22499999999997, 98.514, 111.98599999999999], [9, 410.54999999999995, 446.25, 98.514, 111.98599999999999], [9, 78.53999999999999, 206.465, 118.722, 131.352], [9, 272.51, 338.555, 118.722, 131.352], [9, 111.86, 122.57, 140.614, 153.244], [9, 176.12, 531.3349999999999, 140.614, 153.244], [9, 78.53999999999999, 531.3349999999999, 161.664, 175.136], [9, 78.53999999999999, 531.3349999999999, 183.55599999999998, 197.028], [9, 78.53999999999999, 531.3349999999999, 205.44799999999998, 218.92], [9, 78.53999999999999, 531.3349999999999, 227.34, 240.81199999999998], [9, 78.53999999999999, 531.3349999999999, 249.232, 262.704], [9, 78.53999999999999, 531.3349999999999, 271.12399999999997, 284.596], [9, 78.53999999999999, 524.1949999999999, 293.01599999999996, 307.33], [9, 78.53999999999999, 524.1949999999999, 315.75, 329.222], [9, 78.53999999999999, 531.3349999999999, 337.642, 351.114], [9, 78.53999999999999, 520.03, 359.534, 373.006], [9, 78.53999999999999, 531.3349999999999, 381.426, 395.74], [9, 78.53999999999999, 525.98, 403.318, 417.632], [9, 78.53999999999999, 524.1949999999999, 425.21, 439.524], [9, 78.53999999999999, 531.3349999999999, 447.102, 461.416], [9, 78.53999999999999, 531.3349999999999, 469.83599999999996, 483.308], [9, 78.53999999999999, 524.1949999999999, 491.728, 505.2], [9, 78.53999999999999, 525.98, 513.62, 527.934], [9, 78.53999999999999, 531.3349999999999, 535.512, 549.826], [9, 78.53999999999999, 531.3349999999999, 558.246, 571.718], [9, 78.53999999999999, 531.3349999999999, 580.138, 593.61], [9, 78.53999999999999, 524.1949999999999, 602.03, 615.502], [9, 78.53999999999999, 292.74, 623.922, 638.236], [9, 387.34499999999997, 491.46999999999997, 654.2339999999999, 682.02], [9, 77.945, 205.27499999999998, 692.966, 706.438]]
2026-08-10 11:13:10,845 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=28.9s
2026-08-10 11:13:10,845 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:13:10,847 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:13:10,847 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:13:10,847 INFO     29 [qwen-vl-text] positions(20): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:13:10,847 INFO     29 [qwen-vl-text] page grouping: [9, 10], lines per page: [3, 17]
2026-08-10 11:13:11,097 INFO     29 [qwen-vl-text] page=9, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:13:11,366 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:13:11,368 INFO     29 [qwen-vl-text] LLM extraction start, text_len=480
2026-08-10 11:13:11,369 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:11,369 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 901, \"bbox_end\": 920, \"encounter_dates\": [\"2020-07-08\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "科主任宋瑞香主治医师查房记录\n第页\n总第页\n姓名：\n科室：产科二区\n床号：\n住院号\n今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破\n水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范\n围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依\n据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿\n体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及\n内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径\n9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：\n患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者\n及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心\n变化。以上医嘱已执行。\n主治医师：主治医师：\n孙丹\n2020年07月08日 10：20",
    "role": "user"
  }
]
2026-08-10 11:13:13,482 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:13:13.481+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:13:14,107 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:14,107 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "encounter_date": "2025-05-30",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 90,
      "quantity": "90片",
      "notes": null
    },
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 90,
      "quantity": "1瓶",
      "notes": null
    }
  ]
}
2026-08-10 11:13:14,107 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-05-30]
2026-08-10 11:13:14,112 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1527432, prompt_len=948
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共34行）
["门(急)诊处方", "就诊时间:2025-05-30", "就诊科室:内科门诊", "主", "姓名", "性别:男", "年龄:64岁", "卡", "患者类型:GCP支付", "医疗证号:", "处", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "孟鲁司特钠片◆", "10mg*5/盒", "90片", "2.56", "230.58", "Sig", "10mg/次,口服,qn*90天", "倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶", "221.61", "664.83", "Sig", "2揿/次,吸入,bid*90天"]

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
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord API raw response (len=1724):
[
	{"text": "门(急)诊处方", "bbox": [387, 38, 624, 104]},
	{"text": "就诊时间:2025-05-30", "bbox": [60, 135, 294, 169]},
	{"text": "就诊科室:内科门诊", "bbox": [328, 132, 535, 168]},
	{"text": "主", "bbox": [620, 135, 644, 170]},
	{"text": "姓名", "bbox": [60, 189, 87, 224]},
	{"text": "性别:男", "bbox": [329, 188, 415, 224]},
	{"text": "年龄:64岁", "bbox": [463, 188, 573, 224]},
	{"text": "卡", "bbox": [620, 189, 644, 224]},
	{"text": "患者类型:GCP支付", "bbox": [60, 245, 258, 280]},
	{"text": "医疗证号:", "bbox": [330, 245, 436, 280]},
	{"text": "处", "bbox": [620, 247, 644, 282]},
	{"text": "地址:", "bbox": [60, 300, 115, 336]},
	{"text": "身份证号:", "bbox": [621, 302, 725, 336]},
	{"text": "诊断:支气管哮喘", "bbox": [62, 351, 240, 386]},
	{"text": "西药处方", "bbox": [446, 414, 578, 450]},
	{"text": "组号", "bbox": [128, 477, 175, 512]},
	{"text": "项目名称", "bbox": [234, 477, 329, 512]},
	{"text": "规格", "bbox": [520, 477, 565, 512]},
	{"text": "总量", "bbox": [725, 477, 772, 512]},
	{"text": "单价", "bbox": [832, 477, 878, 512]},
	{"text": "金额", "bbox": [914, 477, 962, 512]},
	{"text": "R:", "bbox": [82, 543, 129, 596]},
	{"text": "孟鲁司特钠片◆", "bbox": [214, 538, 378, 573]},
	{"text": "10mg*5/盒", "bbox": [520, 540, 630, 575]},
	{"text": "90片", "bbox": [707, 540, 755, 573]},
	{"text": "2.56", "bbox": [810, 540, 868, 573]},
	{"text": "230.58", "bbox": [874, 540, 949, 573]},
	{"text": "Sig", "bbox": [439, 593, 478, 626]},
	{"text": "10mg/次,口服,qn*90天", "bbox": [520, 593, 768, 628]},
	{"text": "倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶", "bbox": [214, 643, 755, 678]},
	{"text": "221.61", "bbox": [784, 647, 864, 678]},
	{"text": "664.83", "bbox": [870, 647, 949, 678]},
	{"text": "Sig", "bbox": [440, 700, 479, 733]},
	{"text": "2揿/次,吸入,bid*90天", "bbox": [520, 698, 768, 733]}
]
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord API: raw_items=34, valid_items=34, elapsed=10.7s
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[387, 38, 624, 104]
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-05-30, bbox=[60, 135, 294, 169]
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[328, 132, 535, 168]
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord item[3]: text=主, bbox=[620, 135, 644, 170]
2026-08-10 11:13:24,839 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[60, 189, 87, 224]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[329, 188, 415, 224]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[463, 188, 573, 224]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[7]: text=卡, bbox=[620, 189, 644, 224]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[60, 245, 258, 280]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[330, 245, 436, 280]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[10]: text=处, bbox=[620, 247, 644, 282]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[60, 300, 115, 336]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[621, 302, 725, 336]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[62, 351, 240, 386]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[446, 414, 578, 450]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[128, 477, 175, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[234, 477, 329, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[520, 477, 565, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[725, 477, 772, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[832, 477, 878, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[914, 477, 962, 512]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[82, 543, 129, 596]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[22]: text=孟鲁司特钠片◆, bbox=[214, 538, 378, 573]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[23]: text=10mg*5/盒, bbox=[520, 540, 630, 575]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[24]: text=90片, bbox=[707, 540, 755, 573]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[25]: text=2.56, bbox=[810, 540, 868, 573]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[26]: text=230.58, bbox=[874, 540, 949, 573]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[27]: text=Sig, bbox=[439, 593, 478, 626]
2026-08-10 11:13:24,840 INFO     29 [qwen-vl-text] coord item[28]: text=10mg/次,口服,qn*90天, bbox=[520, 593, 768, 628]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] coord item[29]: text=倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶, bbox=[214, 643, 755, 678]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] coord item[30]: text=221.61, bbox=[784, 647, 864, 678]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] coord item[31]: text=664.83, bbox=[870, 647, 949, 678]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] coord item[32]: text=Sig, bbox=[440, 700, 479, 733]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] coord item[33]: text=2揿/次,吸入,bid*90天, bbox=[520, 698, 768, 733]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] page=6 — 34/34 coords, api_time=10.7s
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] new_positions (34):
[[6, 325.854, 525.408, 22.61, 61.879999999999995], [6, 50.519999999999996, 247.548, 80.325, 100.55499999999999], [6, 276.176, 450.46999999999997, 78.53999999999999, 99.96], [6, 522.04, 542.2479999999999, 80.325, 101.14999999999999], [6, 50.519999999999996, 73.25399999999999, 112.455, 133.28], [6, 277.018, 349.43, 111.86, 133.28], [6, 389.846, 482.466, 111.86, 133.28], [6, 522.04, 542.2479999999999, 112.455, 133.28], [6, 50.519999999999996, 217.236, 145.775, 166.6], [6, 277.86, 367.11199999999997, 145.775, 166.6], [6, 522.04, 542.2479999999999, 146.965, 167.79], [6, 50.519999999999996, 96.83, 178.5, 199.92], [6, 522.882, 610.4499999999999, 179.69, 199.92], [6, 52.204, 202.07999999999998, 208.845, 229.67], [6, 375.532, 486.676, 246.32999999999998, 267.75], [6, 107.776, 147.35, 283.815, 304.64], [6, 197.028, 277.018, 283.815, 304.64], [6, 437.84, 475.72999999999996, 283.815, 304.64], [6, 610.4499999999999, 650.024, 283.815, 304.64], [6, 700.544, 739.276, 283.815, 304.64], [6, 769.588, 810.004, 283.815, 304.64], [6, 69.044, 108.618, 323.085, 354.62], [6, 180.188, 318.276, 320.11, 340.935], [6, 437.84, 530.46, 321.3, 342.125], [6, 595.294, 635.7099999999999, 321.3, 340.935], [6, 682.02, 730.856, 321.3, 340.935], [6, 735.908, 799.058, 321.3, 340.935], [6, 369.638, 402.476, 352.835, 372.46999999999997], [6, 437.84, 646.656, 352.835, 373.65999999999997], [6, 180.188, 635.7099999999999, 382.585, 403.40999999999997], [6, 660.1279999999999, 727.4879999999999, 384.965, 403.40999999999997], [6, 732.54, 799.058, 384.965, 403.40999999999997], [6, 370.47999999999996, 403.318, 416.5, 436.135], [6, 437.84, 646.656, 415.31, 436.135]]
2026-08-10 11:13:24,841 INFO     29 [qwen-vl-text] ═══ DONE ═══ 34 positions, pages=1, time=29.0s
2026-08-10 11:13:24,842 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:13:24,843 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:13:24,843 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:13:24,843 INFO     29 [qwen-vl-text] positions(33): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:13:24,843 INFO     29 [qwen-vl-text] page grouping: [7], lines per page: [33]
2026-08-10 11:13:25,049 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:13:25,051 INFO     29 [qwen-vl-text] LLM extraction start, text_len=241
2026-08-10 11:13:25,051 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:25,051 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 239, \"bbox_end\": 271, \"encounter_dates\": [\"2025-03-05\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-03-05\n就诊科室:内科门诊\n主诊医\n姓名\n性别:男\n年龄:64岁\n卡号:\n患者类型:GCP支付\n医疗证号:\n处方号:\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶\n221.61 443.22\nSig\n2揿/次,吸入,bid*60天\n孟鲁司特钠片\n10mg*30/瓶\n60片\n1.05\n63.06\nSig\n10mg/次,口服,qn*60天",
    "role": "user"
  }
]
2026-08-10 11:13:25,057 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:25,057 INFO     29 [qwen-vl-text] LLM output (len=1140):
{
  "note_type": "科主任/副主任医师查房记录",
  "record_time": "2020-07-08 10:20",
  "recorder": "孙丹",
  "reviewer": "宋瑞香",
  "reviewer_title": "主治医师",
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": "1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [
    "明日剖宫产终止妊娠",
    "完善术前谈话",
    "积极术前准备",
    "严密监测胎心变化"
  ],
  "tp_notes": null,
  "condition_changes": "患者精神好，饮食及睡眠可，大小便正常，未破水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范围，无宫缩。",
  "test_results": "B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "superior_opinion": "患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心变化。以上医嘱已执行。",
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": "患者及其家属表示理解，要求明日剖宫产终止妊娠",
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:13:25,059 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1448182, prompt_len=642
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共3行）
["科主任宋瑞香主治医师查房记录", "第页", "总第页"]

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
2026-08-10 11:13:26,617 INFO     29 [qwen-vl-text] coord API raw response (len=228):
```json
[
	{"text": "科主任宋瑞香主治医师查房记录", "bbox": [427, 824, 689, 841]},
	{"text": "第页", "bbox": [512, 878, 559, 893], "bbox": [512, 878, 559, 893]},
	{"text": "总第页", "bbox": [829, 878, 893, 893], "bbox": [829, 878, 893, 893]}
]
```
2026-08-10 11:13:26,617 INFO     29 [qwen-vl-text] coord API: raw_items=3, valid_items=3, elapsed=1.6s
2026-08-10 11:13:26,617 INFO     29 [qwen-vl-text] coord item[0]: text=科主任宋瑞香主治医师查房记录, bbox=[427, 824, 689, 841]
2026-08-10 11:13:26,617 INFO     29 [qwen-vl-text] coord item[1]: text=第页, bbox=[512, 878, 559, 893]
2026-08-10 11:13:26,617 INFO     29 [qwen-vl-text] coord item[2]: text=总第页, bbox=[829, 878, 893, 893]
2026-08-10 11:13:26,618 INFO     29 [qwen-vl-text] page=9 — 3/3 coords, api_time=1.6s
2026-08-10 11:13:26,620 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540438, prompt_len=1122
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共17行）
["姓名：", "科室：产科二区", "床号：", "住院号", "今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破", "水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范", "围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依", "据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿", "体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及", "内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径", "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：", "患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者", "及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心", "变化。以上医嘱已执行。", "主治医师：主治医师：", "孙丹", "2020年07月08日 10：20"]

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
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord API raw response (len=1188):
[
	{"text": "姓名：", "bbox": [107, 30, 156, 48]},
	{"text": "科室：产科二区", "bbox": [305, 30, 450, 47]},
	{"text": "床号：", "bbox": [523, 30, 572, 47]},
	{"text": "住院号", "bbox": [709, 30, 768, 47]},
	{"text": "今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破", "bbox": [150, 55, 933, 73]},
	{"text": "水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范", "bbox": [97, 83, 933, 101]},
	{"text": "围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依", "bbox": [97, 110, 933, 128]},
	{"text": "据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿", "bbox": [97, 140, 933, 158]},
	{"text": "体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及", "bbox": [97, 168, 933, 186]},
	{"text": "内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径", "bbox": [97, 197, 933, 215]},
	{"text": "9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：", "bbox": [97, 227, 918, 245]},
	{"text": "患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者", "bbox": [97, 255, 933, 273]},
	{"text": "及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心", "bbox": [97, 284, 933, 302]},
	{"text": "变化。以上医嘱已执行。", "bbox": [97, 314, 310, 332]},
	{"text": "主治医师：主治医师：", "bbox": [504, 370, 696, 388]},
	{"text": "孙丹", "bbox": [715, 349, 801, 378]},
	{"text": "2020年07月08日 10：20", "bbox": [97, 402, 313, 419]}
]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord API: raw_items=17, valid_items=17, elapsed=7.2s
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[0]: text=姓名：, bbox=[107, 30, 156, 48]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[1]: text=科室：产科二区, bbox=[305, 30, 450, 47]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[2]: text=床号：, bbox=[523, 30, 572, 47]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[3]: text=住院号, bbox=[709, 30, 768, 47]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[4]: text=今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破, bbox=[150, 55, 933, 73]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[5]: text=水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范, bbox=[97, 83, 933, 101]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[6]: text=围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依, bbox=[97, 110, 933, 128]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[7]: text=据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿, bbox=[97, 140, 933, 158]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[8]: text=体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及, bbox=[97, 168, 933, 186]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[9]: text=内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径, bbox=[97, 197, 933, 215]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[10]: text=9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：, bbox=[97, 227, 918, 245]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[11]: text=患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者, bbox=[97, 255, 933, 273]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[12]: text=及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心, bbox=[97, 284, 933, 302]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[13]: text=变化。以上医嘱已执行。, bbox=[97, 314, 310, 332]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[14]: text=主治医师：主治医师：, bbox=[504, 370, 696, 388]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[15]: text=孙丹, bbox=[715, 349, 801, 378]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] coord item[16]: text=2020年07月08日 10：20, bbox=[97, 402, 313, 419]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] page=10 — 17/17 coords, api_time=7.2s
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] new_positions (20):
[[9, 254.065, 409.955, 693.808, 708.122], [9, 304.64, 332.60499999999996, 739.276, 751.906], [9, 493.255, 531.3349999999999, 739.276, 751.906], [10, 63.665, 92.82, 25.259999999999998, 40.416], [10, 181.475, 267.75, 25.259999999999998, 39.574], [10, 311.185, 340.34, 25.259999999999998, 39.574], [10, 421.85499999999996, 456.96, 25.259999999999998, 39.574], [10, 89.25, 555.135, 46.309999999999995, 61.466], [10, 57.714999999999996, 555.135, 69.886, 85.042], [10, 57.714999999999996, 555.135, 92.61999999999999, 107.776], [10, 57.714999999999996, 555.135, 117.88, 133.036], [10, 57.714999999999996, 555.135, 141.456, 156.612], [10, 57.714999999999996, 555.135, 165.874, 181.03], [10, 57.714999999999996, 546.2099999999999, 191.134, 206.29], [10, 57.714999999999996, 555.135, 214.70999999999998, 229.86599999999999], [10, 57.714999999999996, 555.135, 239.128, 254.284], [10, 57.714999999999996, 184.45, 264.388, 279.544], [10, 299.88, 414.12, 311.53999999999996, 326.69599999999997], [10, 425.42499999999995, 476.59499999999997, 293.858, 318.276], [10, 57.714999999999996, 186.23499999999999, 338.484, 352.798]]
2026-08-10 11:13:33,866 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=2, time=23.0s
2026-08-10 11:13:33,867 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:13:33,867 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:13:33,867 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:13:33,868 INFO     29 [qwen-vl-text] positions(28): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:13:33,868 INFO     29 [qwen-vl-text] page grouping: [10, 11], lines per page: [18, 10]
2026-08-10 11:13:34,135 INFO     29 [qwen-vl-text] page=10, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:13:34,266 INFO     29 [qwen-vl-text] page=11, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:13:34,268 INFO     29 [qwen-vl-text] LLM extraction start, text_len=587
2026-08-10 11:13:34,268 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:34,268 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 921, \"bbox_end\": 948, \"encounter_dates\": [\"2020-07-08\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "术前小结\n姓名：\n性别：女，年龄：36岁；\n病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感\n染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾\n肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，\n腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未\n破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎\n头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止\n妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同\n意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准\n备。\n术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。\n手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：\n拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；\n拟施麻醉：椎管内麻醉；\n第 页\n总第 页\n院\n姓名：\n科室：产科二区\n床号：\n注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好\n新生儿复苏工作。\n主治医师：\n孙丹丹\n第 页\n总第 页",
    "role": "user"
  }
]
2026-08-10 11:13:36,998 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:36,998 INFO     29 [qwen-vl-text] LLM output (len=665):
{
  "encounter_date": "2025-03-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 60,
      "quantity": "120瓶",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 60,
      "quantity": "60片",
      "notes": null
    }
  ]
}
2026-08-10 11:13:36,998 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-05]
2026-08-10 11:13:37,002 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1740969, prompt_len=953
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊医", "姓名", "性别:男", "年龄:64岁", "卡号:", "患者类型:GCP支付", "医疗证号:", "处方号:", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "221.61 443.22", "Sig", "2揿/次,吸入,bid*60天", "孟鲁司特钠片", "10mg*30/瓶", "60片", "1.05", "63.06", "Sig", "10mg/次,口服,qn*60天"]

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
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord API raw response (len=1687):
[
	{"text": "门(急)诊处方", "bbox": [382, 22, 608, 87]},
	{"text": "就诊时间:2025-03-05", "bbox": [55, 115, 288, 149]},
	{"text": "就诊科室:内科门诊", "bbox": [322, 112, 522, 147]},
	{"text": "主诊医", "bbox": [608, 115, 674, 147]},
	{"text": "姓名", "bbox": [55, 169, 98, 203]},
	{"text": "性别:男", "bbox": [322, 167, 406, 201]},
	{"text": "年龄:64岁", "bbox": [453, 167, 560, 201]},
	{"text": "卡号:", "bbox": [608, 169, 670, 201]},
	{"text": "患者类型:GCP支付", "bbox": [55, 225, 250, 258]},
	{"text": "医疗证号:", "bbox": [322, 223, 425, 257]},
	{"text": "处方号:", "bbox": [607, 223, 674, 257]},
	{"text": "地址:", "bbox": [55, 278, 109, 312]},
	{"text": "身份证号:", "bbox": [607, 276, 707, 310]},
	{"text": "诊断:支气管哮喘", "bbox": [55, 328, 232, 363]},
	{"text": "西药处方", "bbox": [435, 387, 563, 421]},
	{"text": "组号", "bbox": [121, 454, 169, 488]},
	{"text": "项目名称", "bbox": [225, 452, 320, 487]},
	{"text": "规格", "bbox": [508, 452, 551, 485]},
	{"text": "总量", "bbox": [708, 452, 753, 487]},
	{"text": "单价", "bbox": [808, 452, 854, 485]},
	{"text": "金额", "bbox": [889, 450, 934, 485]},
	{"text": "R:", "bbox": [77, 518, 123, 571]},
	{"text": "倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶", "bbox": [205, 510, 737, 546]},
	{"text": "221.61 443.22", "bbox": [764, 512, 921, 542]},
	{"text": "Sig", "bbox": [428, 565, 467, 597]},
	{"text": "2揿/次,吸入,bid*60天", "bbox": [507, 563, 748, 597]},
	{"text": "孟鲁司特钠片", "bbox": [206, 617, 350, 651]},
	{"text": "10mg*30/瓶", "bbox": [508, 615, 628, 650]},
	{"text": "60片", "bbox": [690, 615, 735, 648]},
	{"text": "1.05", "bbox": [790, 617, 839, 647]},
	{"text": "63.06", "bbox": [856, 617, 920, 647]},
	{"text": "Sig", "bbox": [428, 672, 467, 705]},
	{"text": "10mg/次,口服,qn*60天", "bbox": [508, 669, 748, 704]}
]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.3s
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[382, 22, 608, 87]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-03-05, bbox=[55, 115, 288, 149]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[322, 112, 522, 147]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[3]: text=主诊医, bbox=[608, 115, 674, 147]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[55, 169, 98, 203]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[322, 167, 406, 201]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[453, 167, 560, 201]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[608, 169, 670, 201]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[55, 225, 250, 258]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[322, 223, 425, 257]
2026-08-10 11:13:46,297 INFO     29 [qwen-vl-text] coord item[10]: text=处方号:, bbox=[607, 223, 674, 257]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[55, 278, 109, 312]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[607, 276, 707, 310]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[55, 328, 232, 363]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[435, 387, 563, 421]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[121, 454, 169, 488]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[225, 452, 320, 487]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[508, 452, 551, 485]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 452, 753, 487]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[808, 452, 854, 485]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[889, 450, 934, 485]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[77, 518, 123, 571]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶, bbox=[205, 510, 737, 546]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 443.22, bbox=[764, 512, 921, 542]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[428, 565, 467, 597]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*60天, bbox=[507, 563, 748, 597]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[206, 617, 350, 651]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[508, 615, 628, 650]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[28]: text=60片, bbox=[690, 615, 735, 648]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[790, 617, 839, 647]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[30]: text=63.06, bbox=[856, 617, 920, 647]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[428, 672, 467, 705]
2026-08-10 11:13:46,298 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*60天, bbox=[508, 669, 748, 704]
2026-08-10 11:13:46,299 INFO     29 [qwen-vl-text] page=7 — 33/33 coords, api_time=9.3s
2026-08-10 11:13:46,299 INFO     29 [qwen-vl-text] new_positions (33):
[[7, 321.644, 511.936, 13.09, 51.765], [7, 46.309999999999995, 242.49599999999998, 68.425, 88.655], [7, 271.12399999999997, 439.524, 66.64, 87.46499999999999], [7, 511.936, 567.5079999999999, 68.425, 87.46499999999999], [7, 46.309999999999995, 82.51599999999999, 100.55499999999999, 120.785], [7, 271.12399999999997, 341.852, 99.365, 119.595], [7, 381.426, 471.52, 99.365, 119.595], [7, 511.936, 564.14, 100.55499999999999, 119.595], [7, 46.309999999999995, 210.5, 133.875, 153.51], [7, 271.12399999999997, 357.84999999999997, 132.685, 152.915], [7, 511.094, 567.5079999999999, 132.685, 152.915], [7, 46.309999999999995, 91.77799999999999, 165.41, 185.64], [7, 511.094, 595.294, 164.22, 184.45], [7, 46.309999999999995, 195.344, 195.16, 215.98499999999999], [7, 366.27, 474.046, 230.265, 250.49499999999998], [7, 101.88199999999999, 142.298, 270.13, 290.36], [7, 189.45, 269.44, 268.94, 289.765], [7, 427.736, 463.942, 268.94, 288.575], [7, 596.136, 634.026, 268.94, 289.765], [7, 680.336, 719.068, 268.94, 288.575], [7, 748.538, 786.428, 267.75, 288.575], [7, 64.834, 103.566, 308.21, 339.745], [7, 172.60999999999999, 620.554, 303.45, 324.87], [7, 643.288, 775.482, 304.64, 322.49], [7, 360.376, 393.214, 336.175, 355.215], [7, 426.894, 629.816, 334.98499999999996, 355.215], [7, 173.452, 294.7, 367.115, 387.34499999999997], [7, 427.736, 528.776, 365.925, 386.75], [7, 580.98, 618.87, 365.925, 385.56], [7, 665.18, 706.438, 367.115, 384.965], [7, 720.752, 774.64, 367.115, 384.965], [7, 360.376, 393.214, 399.84, 419.47499999999997], [7, 427.736, 629.816, 398.055, 418.88]]
2026-08-10 11:13:46,299 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=21.5s
2026-08-10 11:13:46,299 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:13:46,305 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:13:46,305 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:13:46,305 INFO     29 [qwen-vl-text] positions(33): [[8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:13:46,305 INFO     29 [qwen-vl-text] page grouping: [8], lines per page: [33]
2026-08-10 11:13:46,476 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:13:46,477 INFO     29 [qwen-vl-text] LLM extraction start, text_len=238
2026-08-10 11:13:46,477 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:46,477 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 272, \"bbox_end\": 304, \"encounter_dates\": [\"2025-03-05\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-03-05\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
2026-08-10 11:13:46,480 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:13:46.479+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:13:46,485 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:46,485 INFO     29 [qwen-vl-text] LLM output (len=1224):
{
  "note_type": "术前小结",
  "record_time": null,
  "recorder": "孙丹丹",
  "reviewer": "宋瑞香",
  "reviewer_title": "副主任医师",
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [
    "拟定于明日07：30行二次子宫下段剖宫产术",
    "拟施麻醉：椎管内麻醉"
  ],
  "tp_notes": "规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好新生儿复苏工作。",
  "condition_changes": "以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准备。",
  "test_results": "B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。",
  "superior_opinion": "请示科主任宋瑞香副主任医师，同意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准备。",
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": "手术相关风险已向其讲明，并在手术同意书上签字。",
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:13:46,488 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1540438, prompt_len=1168
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共18行）
["术前小结", "姓名：", "性别：女，年龄：36岁；", "病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感", "染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾", "肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，", "腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未", "破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎", "头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止", "妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同", "意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准", "备。", "术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。", "手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：", "拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；", "拟施麻醉：椎管内麻醉；", "第 页", "总第 页"]

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
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord API raw response (len=1288):
[
	{"text": "术前小结", "bbox": [442, 402, 555, 420]},
	{"text": "姓名：", "bbox": [139, 432, 188, 449]},
	{"text": "性别：女，年龄：36岁；", "bbox": [263, 432, 471, 449]},
	{"text": "病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感", "bbox": [139, 459, 927, 477]},
	{"text": "染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾", "bbox": [99, 487, 934, 505]},
	{"text": "肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，", "bbox": [99, 516, 919, 534]},
	{"text": "腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未", "bbox": [99, 544, 934, 562]},
	{"text": "破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎", "bbox": [99, 573, 912, 591]},
	{"text": "头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止", "bbox": [99, 602, 934, 620]},
	{"text": "妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同", "bbox": [99, 630, 933, 648]},
	{"text": "意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准", "bbox": [99, 659, 912, 677]},
	{"text": "备。", "bbox": [99, 688, 128, 705]},
	{"text": "术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。", "bbox": [139, 716, 748, 734]},
	{"text": "手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：", "bbox": [139, 745, 735, 763]},
	{"text": "拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；", "bbox": [139, 773, 735, 791]},
	{"text": "拟施麻醉：椎管内麻醉；", "bbox": [139, 802, 350, 820]},
	{"text": "第 页", "bbox": [515, 864, 567, 879]},
	{"text": "总第 页", "bbox": [863, 864, 933, 879]}
]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord API: raw_items=18, valid_items=18, elapsed=8.2s
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[0]: text=术前小结, bbox=[442, 402, 555, 420]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[139, 432, 188, 449]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[2]: text=性别：女，年龄：36岁；, bbox=[263, 432, 471, 449]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[3]: text=病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感, bbox=[139, 459, 927, 477]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[4]: text=染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾, bbox=[99, 487, 934, 505]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[5]: text=肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，, bbox=[99, 516, 919, 534]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[6]: text=腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未, bbox=[99, 544, 934, 562]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[7]: text=破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎, bbox=[99, 573, 912, 591]
2026-08-10 11:13:54,700 INFO     29 [qwen-vl-text] coord item[8]: text=头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止, bbox=[99, 602, 934, 620]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[9]: text=妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同, bbox=[99, 630, 933, 648]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[10]: text=意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准, bbox=[99, 659, 912, 677]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[11]: text=备。, bbox=[99, 688, 128, 705]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[12]: text=术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。, bbox=[139, 716, 748, 734]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[13]: text=手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：, bbox=[139, 745, 735, 763]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[14]: text=拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；, bbox=[139, 773, 735, 791]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[15]: text=拟施麻醉：椎管内麻醉；, bbox=[139, 802, 350, 820]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[16]: text=第 页, bbox=[515, 864, 567, 879]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord item[17]: text=总第 页, bbox=[863, 864, 933, 879]
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] page=10 — 18/18 coords, api_time=8.2s
2026-08-10 11:13:54,701 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=213537, prompt_len=728
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["院", "姓名：", "科室：产科二区", "床号：", "注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好", "新生儿复苏工作。", "主治医师：", "孙丹丹", "第 页", "总第 页"]

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
2026-08-10 11:13:58,321 INFO     29 [qwen-vl-text] coord API raw response (len=526):
[
	{"text": "院", "bbox": [598, 67, 627, 83]},
	{"text": "姓名：", "bbox": [122, 129, 169, 144]},
	{"text": "科室：产科二区", "bbox": [313, 129, 451, 144]},
	{"text": "床号：", "bbox": [521, 132, 568, 144]},
	{"text": "注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好", "bbox": [151, 153, 917, 169]},
	{"text": "新生儿复苏工作。", "bbox": [113, 180, 258, 195]},
	{"text": "主治医师：", "bbox": [493, 234, 578, 249]},
	{"text": "孙丹丹", "bbox": [598, 213, 680, 241]},
	{"text": "第 页", "bbox": [517, 917, 567, 931]},
	{"text": "总第 页", "bbox": [852, 917, 917, 931]}
]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=3.6s
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[598, 67, 627, 83]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[122, 129, 169, 144]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[2]: text=科室：产科二区, bbox=[313, 129, 451, 144]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[3]: text=床号：, bbox=[521, 132, 568, 144]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[4]: text=注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好, bbox=[151, 153, 917, 169]
2026-08-10 11:13:58,322 INFO     29 [qwen-vl-text] coord item[5]: text=新生儿复苏工作。, bbox=[113, 180, 258, 195]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] coord item[6]: text=主治医师：, bbox=[493, 234, 578, 249]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] coord item[7]: text=孙丹丹, bbox=[598, 213, 680, 241]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] coord item[8]: text=第 页, bbox=[517, 917, 567, 931]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] coord item[9]: text=总第 页, bbox=[852, 917, 917, 931]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] page=11 — 10/10 coords, api_time=3.6s
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] new_positions (28):
[[10, 262.99, 330.22499999999997, 338.484, 353.64], [10, 82.705, 111.86, 363.74399999999997, 378.058], [10, 156.48499999999999, 280.245, 363.74399999999997, 378.058], [10, 82.705, 551.5649999999999, 386.478, 401.63399999999996], [10, 58.904999999999994, 555.73, 410.054, 425.21], [10, 58.904999999999994, 546.805, 434.472, 449.628], [10, 58.904999999999994, 555.73, 458.048, 473.204], [10, 58.904999999999994, 542.64, 482.466, 497.62199999999996], [10, 58.904999999999994, 555.73, 506.88399999999996, 522.04], [10, 58.904999999999994, 555.135, 530.46, 545.616], [10, 58.904999999999994, 542.64, 554.8779999999999, 570.034], [10, 58.904999999999994, 76.16, 579.2959999999999, 593.61], [10, 82.705, 445.06, 602.872, 618.028], [10, 82.705, 437.325, 627.29, 642.446], [10, 82.705, 437.325, 650.866, 666.0219999999999], [10, 82.705, 208.25, 675.284, 690.4399999999999], [10, 306.425, 337.365, 727.4879999999999, 740.1179999999999], [10, 513.485, 555.135, 727.4879999999999, 740.1179999999999], [11, 355.81, 373.065, 56.414, 69.886], [11, 72.59, 100.55499999999999, 108.618, 121.24799999999999], [11, 186.23499999999999, 268.34499999999997, 108.618, 121.24799999999999], [11, 309.995, 337.96, 111.14399999999999, 121.24799999999999], [11, 89.845, 545.615, 128.826, 142.298], [11, 67.235, 153.51, 151.56, 164.19], [11, 293.335, 343.90999999999997, 197.028, 209.658], [11, 355.81, 404.59999999999997, 179.346, 202.922], [11, 307.615, 337.365, 772.1139999999999, 783.9019999999999], [11, 506.94, 545.615, 772.1139999999999, 783.9019999999999]]
2026-08-10 11:13:58,323 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=2, time=24.5s
2026-08-10 11:13:58,324 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:13:58,326 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:13:58,326 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:13:58,326 INFO     29 [qwen-vl-text] positions(20): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:13:58,326 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [20]
2026-08-10 11:13:58,584 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:13:58,585 INFO     29 [qwen-vl-text] LLM extraction start, text_len=562
2026-08-10 11:13:58,586 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:13:58,586 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 949, \"bbox_end\": 968, \"encounter_dates\": [\"2020-07-09\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "院\n姓名：\n科室：产科二区\n床：\n住院号：\n2020年07月09日 09时47分\n术后首次病程记录\n患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫\n下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子\n宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸\n净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球\n擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝\n合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正\n常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不\n多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周\n头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头\n孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下\n肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。\n住院医师：冯雪云\n2020年07月10日 09时00分",
    "role": "user"
  }
]
2026-08-10 11:14:01,764 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:01,764 INFO     29 [qwen-vl-text] LLM output (len=662):
{
  "encounter_date": "2025-03-05",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:14:01,764 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-03-05]
2026-08-10 11:14:01,767 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1610510, prompt_len=950
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-03-05", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-10 11:14:11,023 INFO     29 [qwen-vl-text] coord API raw response (len=1684):
[
	{"text": "门(急)诊处方", "bbox": [382, 31, 617, 97]},
	{"text": "就诊时间:2025-03-05", "bbox": [45, 128, 285, 163]},
	{"text": "就诊科室:内科门诊", "bbox": [321, 123, 527, 158]},
	{"text": "主诊", "bbox": [614, 120, 662, 155]},
	{"text": "姓名", "bbox": [45, 183, 90, 218]},
	{"text": "性别:男", "bbox": [321, 177, 407, 212]},
	{"text": "年龄:64岁", "bbox": [455, 177, 565, 212]},
	{"text": "卡号", "bbox": [614, 175, 660, 209]},
	{"text": "患者类型:GCP支付", "bbox": [46, 236, 247, 270]},
	{"text": "医疗证号:", "bbox": [321, 234, 426, 268]},
	{"text": "处方", "bbox": [612, 231, 660, 265]},
	{"text": "地址:", "bbox": [46, 290, 102, 325]},
	{"text": "身份证号:", "bbox": [612, 283, 716, 317]},
	{"text": "诊断:支气管哮喘", "bbox": [47, 338, 226, 373]},
	{"text": "西药处方", "bbox": [435, 395, 567, 429]},
	{"text": "组号", "bbox": [112, 461, 160, 495]},
	{"text": "项目名称", "bbox": [219, 459, 317, 493]},
	{"text": "规格", "bbox": [509, 457, 554, 490]},
	{"text": "总量", "bbox": [715, 455, 762, 489]},
	{"text": "单价", "bbox": [821, 454, 868, 488]},
	{"text": "金额", "bbox": [904, 452, 951, 486]},
	{"text": "R:", "bbox": [67, 524, 114, 577]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [198, 515, 746, 550]},
	{"text": "221.61 221.61", "bbox": [775, 515, 936, 545]},
	{"text": "Sig", "bbox": [426, 569, 466, 602]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [508, 567, 758, 601]},
	{"text": "孟鲁司特钠片", "bbox": [200, 620, 347, 655]},
	{"text": "10mg*30/瓶", "bbox": [510, 617, 633, 652]},
	{"text": "30片", "bbox": [697, 616, 745, 649]},
	{"text": "1.05", "bbox": [802, 617, 854, 647]},
	{"text": "31.53", "bbox": [872, 617, 938, 647]},
	{"text": "Sig", "bbox": [427, 674, 467, 707]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [510, 670, 758, 705]}
]
2026-08-10 11:14:11,023 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.3s
2026-08-10 11:14:11,023 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[382, 31, 617, 97]
2026-08-10 11:14:11,023 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-03-05, bbox=[45, 128, 285, 163]
2026-08-10 11:14:11,023 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[321, 123, 527, 158]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[614, 120, 662, 155]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[45, 183, 90, 218]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[321, 177, 407, 212]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[455, 177, 565, 212]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[614, 175, 660, 209]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[46, 236, 247, 270]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[321, 234, 426, 268]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[612, 231, 660, 265]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[46, 290, 102, 325]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[612, 283, 716, 317]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[47, 338, 226, 373]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[435, 395, 567, 429]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[112, 461, 160, 495]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[219, 459, 317, 493]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[509, 457, 554, 490]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[715, 455, 762, 489]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[821, 454, 868, 488]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[904, 452, 951, 486]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[67, 524, 114, 577]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[198, 515, 746, 550]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[775, 515, 936, 545]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[426, 569, 466, 602]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[508, 567, 758, 601]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[200, 620, 347, 655]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[510, 617, 633, 652]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[697, 616, 745, 649]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[802, 617, 854, 647]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[872, 617, 938, 647]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[427, 674, 467, 707]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[510, 670, 758, 705]
2026-08-10 11:14:11,024 INFO     29 [qwen-vl-text] page=8 — 33/33 coords, api_time=9.3s
2026-08-10 11:14:11,025 INFO     29 [qwen-vl-text] new_positions (33):
[[8, 321.644, 519.514, 18.445, 57.714999999999996], [8, 37.89, 239.97, 76.16, 96.985], [8, 270.282, 443.734, 73.185, 94.00999999999999], [8, 516.9879999999999, 557.404, 71.39999999999999, 92.225], [8, 37.89, 75.78, 108.88499999999999, 129.71], [8, 270.282, 342.69399999999996, 105.315, 126.14], [8, 383.11, 475.72999999999996, 105.315, 126.14], [8, 516.9879999999999, 555.72, 104.125, 124.35499999999999], [8, 38.732, 207.974, 140.42, 160.65], [8, 270.282, 358.692, 139.23, 159.45999999999998], [8, 515.304, 555.72, 137.445, 157.67499999999998], [8, 38.732, 85.884, 172.54999999999998, 193.375], [8, 515.304, 602.872, 168.385, 188.61499999999998], [8, 39.574, 190.292, 201.10999999999999, 221.935], [8, 366.27, 477.414, 235.02499999999998, 255.255], [8, 94.304, 134.72, 274.295, 294.525], [8, 184.398, 266.914, 273.10499999999996, 293.335], [8, 428.578, 466.46799999999996, 271.91499999999996, 291.55], [8, 602.03, 641.6039999999999, 270.72499999999997, 290.955], [8, 691.2819999999999, 730.856, 270.13, 290.36], [8, 761.168, 800.742, 268.94, 289.16999999999996], [8, 56.414, 95.988, 311.78, 343.315], [8, 166.716, 628.132, 306.425, 327.25], [8, 652.55, 788.112, 306.425, 324.275], [8, 358.692, 392.372, 338.555, 358.19], [8, 427.736, 638.236, 337.365, 357.59499999999997], [8, 168.4, 292.174, 368.9, 389.72499999999997], [8, 429.41999999999996, 532.986, 367.115, 387.94], [8, 586.874, 627.29, 366.52, 386.155], [8, 675.284, 719.068, 367.115, 384.965], [8, 734.2239999999999, 789.7959999999999, 367.115, 384.965], [8, 359.534, 393.214, 401.03, 420.66499999999996], [8, 429.41999999999996, 638.236, 398.65, 419.47499999999997]]
2026-08-10 11:14:11,025 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=24.7s
2026-08-10 11:14:11,025 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:11,026 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:11,026 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:14:11,026 INFO     29 [qwen-vl-text] positions(33): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:11,026 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [33]
2026-08-10 11:14:11,254 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:14:11,255 INFO     29 [qwen-vl-text] LLM extraction start, text_len=242
2026-08-10 11:14:11,255 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:11,256 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 307, \"bbox_end\": 339, \"encounter_dates\": [\"2025-02-08\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-02-08\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号:\n患者类型:001 支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
2026-08-10 11:14:11,261 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:11,261 INFO     29 [qwen-vl-text] LLM output (len=1181):
{
  "note_type": "术后首次病程记录",
  "record_time": "2020-07-09 09:47",
  "recorder": "冯雪云",
  "reviewer": null,
  "reviewer_title": null,
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [
    "给予“头孢唑林钠针”预防感染",
    "加强宫缩",
    "会阴冲洗",
    "尿管护理",
    "支持对症等治疗",
    "嘱其按摩双下肢预防下肢静脉血栓形成",
    "注意观察生命体征、子宫收缩及阴道出血情况"
  ],
  "tp_notes": null,
  "condition_changes": "术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg",
  "test_results": null,
  "superior_opinion": null,
  "consultation_opinion": null,
  "measures_and_effects": "患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周头位剖宫产",
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:14:11,264 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1507263, prompt_len=1235
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["院", "姓名：", "科室：产科二区", "床：", "住院号：", "2020年07月09日 09时47分", "术后首次病程记录", "患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫", "下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子", "宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸", "净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球", "擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝", "合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正", "常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不", "多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周", "头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头", "孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下", "肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。", "住院医师：冯雪云", "2020年07月10日 09时00分"]

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
2026-08-10 11:14:20,896 INFO     29 [qwen-vl-text] coord API raw response (len=1432):
[
	{"text": "院", "bbox": [576, 2, 627, 24]},
	{"text": "姓名：", "bbox": [127, 69, 197, 87]},
	{"text": "科室：产科二区", "bbox": [316, 69, 453, 86]},
	{"text": "床：", "bbox": [523, 69, 552, 86]},
	{"text": "住院号：", "bbox": [700, 69, 765, 86]},
	{"text": "2020年07月09日 09时47分", "bbox": [117, 94, 341, 109]},
	{"text": "术后首次病程记录", "bbox": [427, 94, 583, 109]},
	{"text": "患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫", "bbox": [129, 119, 913, 136]},
	{"text": "下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子", "bbox": [117, 146, 913, 163]},
	{"text": "宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸", "bbox": [117, 173, 913, 190]},
	{"text": "净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球", "bbox": [117, 200, 913, 217]},
	{"text": "擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝", "bbox": [117, 227, 913, 244]},
	{"text": "合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正", "bbox": [117, 255, 913, 272]},
	{"text": "常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不", "bbox": [117, 282, 913, 300]},
	{"text": "多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周", "bbox": [117, 309, 913, 327]},
	{"text": "头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头", "bbox": [127, 338, 913, 356]},
	{"text": "孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下", "bbox": [117, 366, 913, 383]},
	{"text": "肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。", "bbox": [117, 393, 745, 410]},
	{"text": "住院医师：冯雪云", "bbox": [698, 428, 885, 464]},
	{"text": "2020年07月10日 09时00分", "bbox": [117, 477, 343, 493]}
]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=9.6s
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[0]: text=院, bbox=[576, 2, 627, 24]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[127, 69, 197, 87]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[2]: text=科室：产科二区, bbox=[316, 69, 453, 86]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[3]: text=床：, bbox=[523, 69, 552, 86]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[4]: text=住院号：, bbox=[700, 69, 765, 86]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[5]: text=2020年07月09日 09时47分, bbox=[117, 94, 341, 109]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[6]: text=术后首次病程记录, bbox=[427, 94, 583, 109]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[7]: text=患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫, bbox=[129, 119, 913, 136]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[8]: text=下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子, bbox=[117, 146, 913, 163]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[9]: text=宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸, bbox=[117, 173, 913, 190]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[10]: text=净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球, bbox=[117, 200, 913, 217]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[11]: text=擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝, bbox=[117, 227, 913, 244]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[12]: text=合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正, bbox=[117, 255, 913, 272]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[13]: text=常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不, bbox=[117, 282, 913, 300]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[14]: text=多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周, bbox=[117, 309, 913, 327]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[15]: text=头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头, bbox=[127, 338, 913, 356]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[16]: text=孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下, bbox=[117, 366, 913, 383]
2026-08-10 11:14:20,897 INFO     29 [qwen-vl-text] coord item[17]: text=肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。, bbox=[117, 393, 745, 410]
2026-08-10 11:14:20,898 INFO     29 [qwen-vl-text] coord item[18]: text=住院医师：冯雪云, bbox=[698, 428, 885, 464]
2026-08-10 11:14:20,898 INFO     29 [qwen-vl-text] coord item[19]: text=2020年07月10日 09时00分, bbox=[117, 477, 343, 493]
2026-08-10 11:14:20,898 INFO     29 [qwen-vl-text] page=12 — 20/20 coords, api_time=9.6s
2026-08-10 11:14:20,898 INFO     29 [qwen-vl-text] new_positions (20):
[[12, 342.71999999999997, 373.065, 1.684, 20.208], [12, 75.565, 117.21499999999999, 58.098, 73.25399999999999], [12, 188.01999999999998, 269.53499999999997, 58.098, 72.41199999999999], [12, 311.185, 328.44, 58.098, 72.41199999999999], [12, 416.5, 455.17499999999995, 58.098, 72.41199999999999], [12, 69.615, 202.89499999999998, 79.148, 91.77799999999999], [12, 254.065, 346.885, 79.148, 91.77799999999999], [12, 76.755, 543.235, 100.198, 114.512], [12, 69.615, 543.235, 122.932, 137.246], [12, 69.615, 543.235, 145.666, 159.98], [12, 69.615, 543.235, 168.4, 182.714], [12, 69.615, 543.235, 191.134, 205.44799999999998], [12, 69.615, 543.235, 214.70999999999998, 229.024], [12, 69.615, 543.235, 237.444, 252.6], [12, 69.615, 543.235, 260.178, 275.334], [12, 75.565, 543.235, 284.596, 299.752], [12, 69.615, 543.235, 308.17199999999997, 322.486], [12, 69.615, 443.275, 330.906, 345.21999999999997], [12, 415.31, 526.5749999999999, 360.376, 390.688], [12, 69.615, 204.08499999999998, 401.63399999999996, 415.106]]
2026-08-10 11:14:20,898 INFO     29 [qwen-vl-text] ═══ DONE ═══ 20 positions, pages=1, time=22.6s
2026-08-10 11:14:20,898 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:20,915 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:20,916 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:14:20,916 INFO     29 [qwen-vl-text] positions(12): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:20,916 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [12]
2026-08-10 11:14:21,181 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:14:21,183 INFO     29 [qwen-vl-text] LLM extraction start, text_len=360
2026-08-10 11:14:21,183 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:21,183 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 969, \"bbox_end\": 980, \"encounter_dates\": [\"2020-07-10\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "彭琼玉副主任医师查房记录\n今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师\n查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合\n好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量\n正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病\n情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连\n及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫\n恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活\n动，注意监测血糖情况，上述指示已执行。\n副主任医师：马\n住院医师：冯雪云\n2020年07月11日 08时06分",
    "role": "user"
  }
]
2026-08-10 11:14:21,441 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:14:21.439+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:14:24,282 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:24,282 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "encounter_date": "2025-02-08",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:14:24,283 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-02-08]
2026-08-10 11:14:24,290 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1920992, prompt_len=954
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2025-02-08", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号:", "患者类型:001 支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-10 11:14:33,538 INFO     29 [qwen-vl-text] coord API raw response (len=1688):
[
	{"text": "门(急)诊处方", "bbox": [374, 34, 609, 98]},
	{"text": "就诊时间:2025-02-08", "bbox": [40, 130, 278, 166]},
	{"text": "就诊科室:内科门诊", "bbox": [314, 127, 521, 163]},
	{"text": "主诊", "bbox": [606, 129, 662, 163]},
	{"text": "姓名:", "bbox": [40, 185, 100, 221]},
	{"text": "性别:男", "bbox": [314, 182, 400, 218]},
	{"text": "年龄:64岁", "bbox": [448, 182, 558, 218]},
	{"text": "卡号:", "bbox": [606, 182, 662, 218]},
	{"text": "患者类型:001 支付", "bbox": [40, 240, 238, 276]},
	{"text": "医疗证号:", "bbox": [314, 238, 420, 274]},
	{"text": "处方", "bbox": [605, 240, 654, 274]},
	{"text": "地址:", "bbox": [40, 295, 96, 331]},
	{"text": "身份证号:", "bbox": [605, 293, 709, 329]},
	{"text": "诊断:支气管哮喘", "bbox": [40, 347, 219, 383]},
	{"text": "西药处方", "bbox": [428, 407, 561, 443]},
	{"text": "组号", "bbox": [106, 474, 154, 509]},
	{"text": "项目名称", "bbox": [212, 473, 310, 509]},
	{"text": "规格", "bbox": [503, 471, 548, 505]},
	{"text": "总量", "bbox": [708, 471, 755, 505]},
	{"text": "单价", "bbox": [814, 471, 861, 505]},
	{"text": "金额", "bbox": [896, 470, 943, 505]},
	{"text": "R:", "bbox": [61, 539, 108, 593]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶", "bbox": [192, 531, 739, 569]},
	{"text": "221.61 221.61", "bbox": [767, 534, 927, 565]},
	{"text": "Sig", "bbox": [420, 587, 460, 620]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [502, 585, 750, 620]},
	{"text": "孟鲁司特钠片◆", "bbox": [194, 640, 360, 676]},
	{"text": "10mg*30/瓶", "bbox": [504, 637, 626, 673]},
	{"text": "30片", "bbox": [690, 638, 738, 673]},
	{"text": "1.05", "bbox": [795, 640, 846, 671]},
	{"text": "31.53", "bbox": [865, 640, 930, 671]},
	{"text": "Sig", "bbox": [420, 695, 460, 728]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [504, 692, 750, 728]}
]
2026-08-10 11:14:33,538 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.2s
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[374, 34, 609, 98]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-02-08, bbox=[40, 130, 278, 166]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[314, 127, 521, 163]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[606, 129, 662, 163]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[40, 185, 100, 221]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[314, 182, 400, 218]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[448, 182, 558, 218]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[606, 182, 662, 218]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:001 支付, bbox=[40, 240, 238, 276]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[314, 238, 420, 274]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[605, 240, 654, 274]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[40, 295, 96, 331]
2026-08-10 11:14:33,539 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[605, 293, 709, 329]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[40, 347, 219, 383]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[428, 407, 561, 443]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[106, 474, 154, 509]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[212, 473, 310, 509]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[503, 471, 548, 505]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 471, 755, 505]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[814, 471, 861, 505]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[896, 470, 943, 505]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[61, 539, 108, 593]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶, bbox=[192, 531, 739, 569]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[767, 534, 927, 565]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[420, 587, 460, 620]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[502, 585, 750, 620]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片◆, bbox=[194, 640, 360, 676]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[504, 637, 626, 673]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[690, 638, 738, 673]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[795, 640, 846, 671]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[865, 640, 930, 671]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[420, 695, 460, 728]
2026-08-10 11:14:33,540 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[504, 692, 750, 728]
2026-08-10 11:14:33,541 INFO     29 [qwen-vl-text] page=9 — 33/33 coords, api_time=9.2s
2026-08-10 11:14:33,541 INFO     29 [qwen-vl-text] new_positions (33):
[[9, 314.908, 512.778, 20.23, 58.309999999999995], [9, 33.68, 234.076, 77.35, 98.77], [9, 264.388, 438.68199999999996, 75.565, 96.985], [9, 510.252, 557.404, 76.755, 96.985], [9, 33.68, 84.2, 110.07499999999999, 131.495], [9, 264.388, 336.8, 108.28999999999999, 129.71], [9, 377.216, 469.83599999999996, 108.28999999999999, 129.71], [9, 510.252, 557.404, 108.28999999999999, 129.71], [9, 33.68, 200.396, 142.79999999999998, 164.22], [9, 264.388, 353.64, 141.60999999999999, 163.03], [9, 509.40999999999997, 550.668, 142.79999999999998, 163.03], [9, 33.68, 80.832, 175.525, 196.945], [9, 509.40999999999997, 596.978, 174.33499999999998, 195.755], [9, 33.68, 184.398, 206.465, 227.885], [9, 360.376, 472.36199999999997, 242.165, 263.585], [9, 89.252, 129.668, 282.03, 302.85499999999996], [9, 178.504, 261.02, 281.435, 302.85499999999996], [9, 423.526, 461.416, 280.245, 300.47499999999997], [9, 596.136, 635.7099999999999, 280.245, 300.47499999999997], [9, 685.3879999999999, 724.962, 280.245, 300.47499999999997], [9, 754.432, 794.006, 279.65, 300.47499999999997], [9, 51.361999999999995, 90.93599999999999, 320.705, 352.835], [9, 161.664, 622.2379999999999, 315.945, 338.555], [9, 645.814, 780.534, 317.72999999999996, 336.175], [9, 353.64, 387.32, 349.265, 368.9], [9, 422.68399999999997, 631.5, 348.075, 368.9], [9, 163.34799999999998, 303.12, 380.79999999999995, 402.21999999999997], [9, 424.368, 527.092, 379.015, 400.435], [9, 580.98, 621.396, 379.60999999999996, 400.435], [9, 669.39, 712.332, 380.79999999999995, 399.245], [9, 728.3299999999999, 783.06, 380.79999999999995, 399.245], [9, 353.64, 387.32, 413.525, 433.15999999999997], [9, 424.368, 631.5, 411.74, 433.15999999999997]]
2026-08-10 11:14:33,541 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=22.5s
2026-08-10 11:14:33,542 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:33,543 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:33,544 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:14:33,544 INFO     29 [qwen-vl-text] positions(32): [[10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:33,544 INFO     29 [qwen-vl-text] page grouping: [10], lines per page: [32]
2026-08-10 11:14:33,767 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:14:33,768 INFO     29 [qwen-vl-text] LLM extraction start, text_len=231
2026-08-10 11:14:33,768 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:33,768 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 342, \"bbox_end\": 373, \"encounter_dates\": [\"2025-01-10\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2025-01-10\n就诊科室:内科门诊\n主诊\n性别:男\n年龄:64岁\n卡号\n患者类型:G\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
2026-08-10 11:14:33,774 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:33,774 INFO     29 [qwen-vl-text] LLM output (len=957):
{
  "note_type": "科主任/副主任医师查房记录",
  "record_time": "2020-07-11 08:06",
  "recorder": "冯雪云",
  "reviewer": "彭琼玉",
  "reviewer_title": "副主任医师",
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [],
  "tp_notes": null,
  "condition_changes": "今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量正常，余查无特殊",
  "test_results": null,
  "superior_opinion": "现术后一天，未排气，流食，体温正常，切口无感染迹象，病情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活动，注意监测血糖情况，上述指示已执行。",
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:14:33,777 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1507263, prompt_len=1009
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共12行）
["彭琼玉副主任医师查房记录", "今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师", "查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合", "好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量", "正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病", "情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连", "及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫", "恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活", "动，注意监测血糖情况，上述指示已执行。", "副主任医师：马", "住院医师：冯雪云", "2020年07月11日 08时06分"]

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
2026-08-10 11:14:38,691 INFO     29 [qwen-vl-text] coord API raw response (len=903):
```json
[
	{"text": "彭琼玉副主任医师查房记录", "bbox": [410, 477, 640, 494]},
	{"text": "今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师", "bbox": [177, 504, 912, 521]},
	{"text": "查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合", "bbox": [118, 531, 912, 549]},
	{"text": "好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量", "bbox": [118, 558, 912, 576]},
	{"text": "正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病", "bbox": [118, 586, 912, 604]},
	{"text": "情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连", "bbox": [118, 613, 912, 631]},
	{"text": "及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫", "bbox": [118, 640, 912, 658]},
	{"text": "恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活", "bbox": [118, 668, 894, 686]},
	{"text": "动，注意监测血糖情况，上述指示已执行。", "bbox": [118, 695, 477, 713]},
	{"text": "副主任医师：马", "bbox": [496, 740, 600, 765]},
	{"text": "住院医师：冯雪云", "bbox": [703, 740, 788, 765]},
	{"text": "2020年07月11日 08时06分", "bbox": [118, 780, 342, 797]}
]
```
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord API: raw_items=12, valid_items=12, elapsed=4.9s
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[0]: text=彭琼玉副主任医师查房记录, bbox=[410, 477, 640, 494]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[1]: text=今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师, bbox=[177, 504, 912, 521]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[2]: text=查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合, bbox=[118, 531, 912, 549]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[3]: text=好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量, bbox=[118, 558, 912, 576]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[4]: text=正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病, bbox=[118, 586, 912, 604]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[5]: text=情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连, bbox=[118, 613, 912, 631]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[6]: text=及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫, bbox=[118, 640, 912, 658]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[7]: text=恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活, bbox=[118, 668, 894, 686]
2026-08-10 11:14:38,692 INFO     29 [qwen-vl-text] coord item[8]: text=动，注意监测血糖情况，上述指示已执行。, bbox=[118, 695, 477, 713]
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] coord item[9]: text=副主任医师：马, bbox=[496, 740, 600, 765]
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] coord item[10]: text=住院医师：冯雪云, bbox=[703, 740, 788, 765]
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] coord item[11]: text=2020年07月11日 08时06分, bbox=[118, 780, 342, 797]
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] page=12 — 12/12 coords, api_time=4.9s
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] new_positions (12):
[[12, 243.95, 380.79999999999995, 401.63399999999996, 415.948], [12, 105.315, 542.64, 424.368, 438.68199999999996], [12, 70.21, 542.64, 447.102, 462.258], [12, 70.21, 542.64, 469.83599999999996, 484.99199999999996], [12, 70.21, 542.64, 493.412, 508.568], [12, 70.21, 542.64, 516.146, 531.302], [12, 70.21, 542.64, 538.88, 554.036], [12, 70.21, 531.93, 562.456, 577.612], [12, 70.21, 283.815, 585.1899999999999, 600.346], [12, 295.12, 357.0, 623.0799999999999, 644.13], [12, 418.28499999999997, 468.85999999999996, 623.0799999999999, 644.13], [12, 70.21, 203.48999999999998, 656.76, 671.074]]
2026-08-10 11:14:38,693 INFO     29 [qwen-vl-text] ═══ DONE ═══ 12 positions, pages=1, time=17.8s
2026-08-10 11:14:38,694 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:38,695 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:38,696 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:14:38,696 INFO     29 [qwen-vl-text] positions(15): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:38,696 INFO     29 [qwen-vl-text] page grouping: [12, 13], lines per page: [3, 12]
2026-08-10 11:14:38,960 INFO     29 [qwen-vl-text] page=12, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:14:39,169 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:14:39,170 INFO     29 [qwen-vl-text] LLM extraction start, text_len=295
2026-08-10 11:14:39,170 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:39,171 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 981, \"bbox_end\": 995, \"encounter_dates\": [\"2020-07-11\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊\n第 页\n总第 页\n出院\n姓名：\n科室：产科二区\n床号\n住院\n未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血\n不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双\n下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切\n口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加\n益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。\n主治医师：孙丹丹\n2020年07月12日 10时00分",
    "role": "user"
  }
]
2026-08-10 11:14:42,304 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:42,304 INFO     29 [qwen-vl-text] LLM output (len=662):
{
  "encounter_date": "2025-01-10",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:14:42,304 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-01-10]
2026-08-10 11:14:42,310 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1610425, prompt_len=940
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["门(急)诊处方", "就诊时间:2025-01-10", "就诊科室:内科门诊", "主诊", "性别:男", "年龄:64岁", "卡号", "患者类型:G", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-10 11:14:52,474 INFO     29 [qwen-vl-text] coord API raw response (len=1635):
[
	{"text": "门(急)诊处方", "bbox": [378, 20, 595, 83]},
	{"text": "就诊时间:2025-01-10", "bbox": [67, 110, 289, 141]},
	{"text": "就诊科室:内科门诊", "bbox": [322, 108, 514, 141]},
	{"text": "主诊", "bbox": [593, 108, 628, 141]},
	{"text": "性别:男", "bbox": [322, 158, 402, 192]},
	{"text": "年龄:64岁", "bbox": [447, 158, 548, 192]},
	{"text": "卡号", "bbox": [593, 158, 628, 192]},
	{"text": "患者类型:G", "bbox": [70, 211, 187, 244]},
	{"text": "医疗证号:", "bbox": [322, 211, 420, 244]},
	{"text": "处方", "bbox": [592, 211, 628, 244]},
	{"text": "地址:", "bbox": [70, 262, 120, 295]},
	{"text": "身份证号:", "bbox": [593, 262, 689, 295]},
	{"text": "诊断:支气管哮喘", "bbox": [71, 309, 237, 344]},
	{"text": "西药处方", "bbox": [428, 368, 551, 401]},
	{"text": "组号", "bbox": [131, 427, 175, 460]},
	{"text": "项目名称", "bbox": [228, 427, 319, 460]},
	{"text": "规格", "bbox": [498, 427, 539, 460]},
	{"text": "总量", "bbox": [690, 427, 732, 460]},
	{"text": "单价", "bbox": [787, 427, 829, 460]},
	{"text": "金额", "bbox": [863, 427, 906, 460]},
	{"text": "R:", "bbox": [90, 488, 133, 538]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [210, 483, 716, 516]},
	{"text": "221.61 221.61", "bbox": [743, 488, 892, 516]},
	{"text": "Sig", "bbox": [422, 534, 458, 566]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [497, 534, 727, 566]},
	{"text": "孟鲁司特钠片", "bbox": [212, 582, 348, 615]},
	{"text": "10mg*30/瓶", "bbox": [498, 582, 611, 615]},
	{"text": "30片", "bbox": [671, 582, 715, 615]},
	{"text": "1.05", "bbox": [768, 587, 814, 613]},
	{"text": "31.53", "bbox": [833, 587, 892, 613]},
	{"text": "Sig", "bbox": [422, 634, 458, 666]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [498, 634, 727, 666]}
]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.2s
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[378, 20, 595, 83]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2025-01-10, bbox=[67, 110, 289, 141]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[322, 108, 514, 141]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[593, 108, 628, 141]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[4]: text=性别:男, bbox=[322, 158, 402, 192]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:64岁, bbox=[447, 158, 548, 192]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[6]: text=卡号, bbox=[593, 158, 628, 192]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型:G, bbox=[70, 211, 187, 244]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[8]: text=医疗证号:, bbox=[322, 211, 420, 244]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[9]: text=处方, bbox=[592, 211, 628, 244]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[10]: text=地址:, bbox=[70, 262, 120, 295]
2026-08-10 11:14:52,475 INFO     29 [qwen-vl-text] coord item[11]: text=身份证号:, bbox=[593, 262, 689, 295]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[12]: text=诊断:支气管哮喘, bbox=[71, 309, 237, 344]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[13]: text=西药处方, bbox=[428, 368, 551, 401]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[14]: text=组号, bbox=[131, 427, 175, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[15]: text=项目名称, bbox=[228, 427, 319, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[16]: text=规格, bbox=[498, 427, 539, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[17]: text=总量, bbox=[690, 427, 732, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[18]: text=单价, bbox=[787, 427, 829, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[19]: text=金额, bbox=[863, 427, 906, 460]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[20]: text=R:, bbox=[90, 488, 133, 538]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[21]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[210, 483, 716, 516]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[22]: text=221.61 221.61, bbox=[743, 488, 892, 516]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[23]: text=Sig, bbox=[422, 534, 458, 566]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[24]: text=2揿/次,吸入,bid*30天, bbox=[497, 534, 727, 566]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[25]: text=孟鲁司特钠片, bbox=[212, 582, 348, 615]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[26]: text=10mg*30/瓶, bbox=[498, 582, 611, 615]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[27]: text=30片, bbox=[671, 582, 715, 615]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[28]: text=1.05, bbox=[768, 587, 814, 613]
2026-08-10 11:14:52,476 INFO     29 [qwen-vl-text] coord item[29]: text=31.53, bbox=[833, 587, 892, 613]
2026-08-10 11:14:52,477 INFO     29 [qwen-vl-text] coord item[30]: text=Sig, bbox=[422, 634, 458, 666]
2026-08-10 11:14:52,477 INFO     29 [qwen-vl-text] coord item[31]: text=10mg/次,口服,qn*30天, bbox=[498, 634, 727, 666]
2026-08-10 11:14:52,478 INFO     29 [qwen-vl-text] page=10 — 32/32 coords, api_time=10.2s
2026-08-10 11:14:52,478 INFO     29 [qwen-vl-text] new_positions (32):
[[10, 318.276, 500.99, 11.899999999999999, 49.385], [10, 56.414, 243.338, 65.45, 83.895], [10, 271.12399999999997, 432.788, 64.25999999999999, 83.895], [10, 499.306, 528.776, 64.25999999999999, 83.895], [10, 271.12399999999997, 338.484, 94.00999999999999, 114.24], [10, 376.37399999999997, 461.416, 94.00999999999999, 114.24], [10, 499.306, 528.776, 94.00999999999999, 114.24], [10, 58.94, 157.454, 125.54499999999999, 145.18], [10, 271.12399999999997, 353.64, 125.54499999999999, 145.18], [10, 498.464, 528.776, 125.54499999999999, 145.18], [10, 58.94, 101.03999999999999, 155.89, 175.525], [10, 499.306, 580.138, 155.89, 175.525], [10, 59.782, 199.554, 183.855, 204.67999999999998], [10, 360.376, 463.942, 218.95999999999998, 238.595], [10, 110.30199999999999, 147.35, 254.065, 273.7], [10, 191.976, 268.598, 254.065, 273.7], [10, 419.316, 453.83799999999997, 254.065, 273.7], [10, 580.98, 616.3439999999999, 254.065, 273.7], [10, 662.654, 698.018, 254.065, 273.7], [10, 726.646, 762.852, 254.065, 273.7], [10, 75.78, 111.98599999999999, 290.36, 320.11], [10, 176.82, 602.872, 287.385, 307.02], [10, 625.606, 751.064, 290.36, 307.02], [10, 355.324, 385.63599999999997, 317.72999999999996, 336.77], [10, 418.474, 612.134, 317.72999999999996, 336.77], [10, 178.504, 293.01599999999996, 346.28999999999996, 365.925], [10, 419.316, 514.462, 346.28999999999996, 365.925], [10, 564.982, 602.03, 346.28999999999996, 365.925], [10, 646.656, 685.3879999999999, 349.265, 364.73499999999996], [10, 701.386, 751.064, 349.265, 364.73499999999996], [10, 355.324, 385.63599999999997, 377.22999999999996, 396.27], [10, 419.316, 612.134, 377.22999999999996, 396.27]]
2026-08-10 11:14:52,478 INFO     29 [qwen-vl-text] ═══ DONE ═══ 32 positions, pages=1, time=18.9s
2026-08-10 11:14:52,478 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:52,492 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:52,492 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:14:52,493 INFO     29 [qwen-vl-text] positions(33): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:52,493 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [33]
2026-08-10 11:14:52,683 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:14:52,684 INFO     29 [qwen-vl-text] LLM extraction start, text_len=240
2026-08-10 11:14:52,684 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:52,684 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 374, \"bbox_end\": 406, \"encounter_dates\": [\"2024-12-11\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-12-11\n就诊科室:内科门诊\n主诊\n姓名:\n性别:男\n年龄:64岁\n卡号\n患者类型:GCP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片◆\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
2026-08-10 11:14:52,688 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:14:52.688+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:14:52,693 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:52,693 INFO     29 [qwen-vl-text] LLM output (len=928):
{
  "note_type": "日常病程记录",
  "record_time": "2020-07-12 10:00",
  "recorder": null,
  "reviewer": "孙丹丹",
  "reviewer_title": "主治医师",
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [
    "改为II级护理",
    "已排气给予苔含",
    "继续予子宫复旧磁疗促进产后子宫恢复",
    "加用腹部切口红外线治疗促进伤口愈合",
    "加益宫颗粒(自各药物)促宫缩治疗"
  ],
  "tp_notes": "注意体温变化及切口情况；观察体温及阴道恶露情况",
  "condition_changes": "术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双下肢无水肿，现术后第二天，病情稳定",
  "test_results": null,
  "superior_opinion": null,
  "consultation_opinion": null,
  "measures_and_effects": null,
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:14:52,696 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1507263, prompt_len=669
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共3行）
["术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊", "第 页", "总第 页"]

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
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] coord API raw response (len=255):
```json
[
	{"text": "术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊", "bbox": [155, 806, 913, 825]},
	{"text": "第 页", "bbox": [515, 864, 565, 879], "bbox": [515, 864, 565, 879]},
	{"text": "总第 页", "bbox": [847, 864, 913, 879], "bbox": [847, 864, 913, 879]}
]
```
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] coord API: raw_items=3, valid_items=3, elapsed=1.7s
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] coord item[0]: text=术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊, bbox=[155, 806, 913, 825]
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] coord item[1]: text=第 页, bbox=[515, 864, 565, 879]
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] coord item[2]: text=总第 页, bbox=[847, 864, 913, 879]
2026-08-10 11:14:54,389 INFO     29 [qwen-vl-text] page=12 — 3/3 coords, api_time=1.7s
2026-08-10 11:14:54,391 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=934998, prompt_len=895
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共12行）
["出院", "姓名：", "科室：产科二区", "床号", "住院", "未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血", "不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双", "下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切", "口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加", "益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。", "主治医师：孙丹丹", "2020年07月12日 10时00分"]

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
2026-08-10 11:14:59,392 INFO     29 [qwen-vl-text] coord API raw response (len=775):
[
	{"text": "出院", "bbox": [570, 60, 630, 82]},
	{"text": "姓名：", "bbox": [115, 129, 163, 145]},
	{"text": "科室：产科二区", "bbox": [309, 129, 450, 145]},
	{"text": "床号", "bbox": [521, 129, 558, 145]},
	{"text": "住院", "bbox": [704, 129, 744, 145]},
	{"text": "未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血", "bbox": [107, 154, 923, 171]},
	{"text": "不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双", "bbox": [107, 181, 923, 199]},
	{"text": "下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切", "bbox": [107, 208, 923, 226]},
	{"text": "口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加", "bbox": [107, 237, 923, 255]},
	{"text": "益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。", "bbox": [107, 265, 630, 282]},
	{"text": "主治医师：孙丹丹", "bbox": [503, 300, 693, 337]},
	{"text": "2020年07月12日 10时00分", "bbox": [107, 352, 335, 368]}
]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord API: raw_items=12, valid_items=12, elapsed=5.0s
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[0]: text=出院, bbox=[570, 60, 630, 82]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[115, 129, 163, 145]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[2]: text=科室：产科二区, bbox=[309, 129, 450, 145]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[3]: text=床号, bbox=[521, 129, 558, 145]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[4]: text=住院, bbox=[704, 129, 744, 145]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[5]: text=未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血, bbox=[107, 154, 923, 171]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[6]: text=不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双, bbox=[107, 181, 923, 199]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[7]: text=下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切, bbox=[107, 208, 923, 226]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[8]: text=口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加, bbox=[107, 237, 923, 255]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[9]: text=益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。, bbox=[107, 265, 630, 282]
2026-08-10 11:14:59,393 INFO     29 [qwen-vl-text] coord item[10]: text=主治医师：孙丹丹, bbox=[503, 300, 693, 337]
2026-08-10 11:14:59,394 INFO     29 [qwen-vl-text] coord item[11]: text=2020年07月12日 10时00分, bbox=[107, 352, 335, 368]
2026-08-10 11:14:59,394 INFO     29 [qwen-vl-text] page=13 — 12/12 coords, api_time=5.0s
2026-08-10 11:14:59,394 INFO     29 [qwen-vl-text] new_positions (15):
[[12, 92.225, 543.235, 678.6519999999999, 694.65], [12, 306.425, 336.175, 727.4879999999999, 740.1179999999999], [12, 503.965, 543.235, 727.4879999999999, 740.1179999999999], [13, 339.15, 374.84999999999997, 50.519999999999996, 69.044], [13, 68.425, 96.985, 108.618, 122.08999999999999], [13, 183.855, 267.75, 108.618, 122.08999999999999], [13, 309.995, 332.01, 108.618, 122.08999999999999], [13, 418.88, 442.68, 108.618, 122.08999999999999], [13, 63.665, 549.185, 129.668, 143.982], [13, 63.665, 549.185, 152.402, 167.558], [13, 63.665, 549.185, 175.136, 190.292], [13, 63.665, 549.185, 199.554, 214.70999999999998], [13, 63.665, 374.84999999999997, 223.13, 237.444], [13, 299.28499999999997, 412.335, 252.6, 283.75399999999996], [13, 63.665, 199.325, 296.384, 309.856]]
2026-08-10 11:14:59,394 INFO     29 [qwen-vl-text] ═══ DONE ═══ 15 positions, pages=2, time=20.7s
2026-08-10 11:14:59,394 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:14:59,396 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:14:59,397 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 11:14:59,397 INFO     29 [qwen-vl-text] positions(10): [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:14:59,397 INFO     29 [qwen-vl-text] page grouping: [13], lines per page: [10]
2026-08-10 11:14:59,604 INFO     29 [qwen-vl-text] page=13, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:14:59,605 INFO     29 [qwen-vl-text] LLM extraction start, text_len=312
2026-08-10 11:14:59,605 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:14:59,606 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 996, \"bbox_end\": 1005, \"encounter_dates\": [\"2020-07-12\"], \"department\": \"产科二区\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "彭琼玉副主任医师查房记录\n今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生\n命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异\n常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性\n粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，\n切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任\n医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫\n产临床路径管理，今日办理出院。指示已执行。\n副主任医师：彭琼玉\n主治医师：孙丹丹",
    "role": "user"
  }
]
2026-08-10 11:15:02,453 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:02,453 INFO     29 [qwen-vl-text] LLM output (len=663):
{
  "encounter_date": "2024-12-11",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1瓶",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:15:02,453 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-12-11]
2026-08-10 11:15:02,456 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1414362, prompt_len=952
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2024-12-11", "就诊科室:内科门诊", "主诊", "姓名:", "性别:男", "年龄:64岁", "卡号", "患者类型:GCP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片◆", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord API raw response (len=1688):
[
	{"text": "门(急)诊处方", "bbox": [393, 33, 612, 92]},
	{"text": "就诊时间:2024-12-11", "bbox": [77, 117, 300, 150]},
	{"text": "就诊科室:内科门诊", "bbox": [336, 117, 530, 150]},
	{"text": "主诊", "bbox": [610, 120, 650, 152]},
	{"text": "姓名:", "bbox": [77, 168, 132, 201]},
	{"text": "性别:男", "bbox": [337, 168, 417, 201]},
	{"text": "年龄:64岁", "bbox": [463, 169, 565, 201]},
	{"text": "卡号", "bbox": [611, 170, 650, 201]},
	{"text": "患者类型:GCP支付", "bbox": [80, 219, 267, 252]},
	{"text": "医疗证号:", "bbox": [338, 220, 437, 253]},
	{"text": "处方", "bbox": [610, 223, 650, 255]},
	{"text": "地址:", "bbox": [81, 269, 133, 302]},
	{"text": "身份证号:", "bbox": [610, 271, 707, 304]},
	{"text": "诊断:支气管哮喘", "bbox": [84, 317, 251, 350]},
	{"text": "西药处方", "bbox": [447, 375, 569, 407]},
	{"text": "组号", "bbox": [146, 432, 190, 464]},
	{"text": "项目名称", "bbox": [245, 432, 337, 464]},
	{"text": "规格", "bbox": [516, 432, 558, 464]},
	{"text": "总量", "bbox": [708, 434, 751, 466]},
	{"text": "单价", "bbox": [804, 434, 847, 466]},
	{"text": "金额", "bbox": [880, 434, 922, 466]},
	{"text": "R:", "bbox": [104, 492, 147, 540]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶", "bbox": [226, 487, 735, 520]},
	{"text": "221.61 221.61", "bbox": [762, 490, 908, 517]},
	{"text": "Sig", "bbox": [440, 536, 475, 567]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [515, 536, 745, 567]},
	{"text": "孟鲁司特钠片◆", "bbox": [228, 584, 382, 616]},
	{"text": "10mg*30/瓶", "bbox": [517, 582, 629, 614]},
	{"text": "30片", "bbox": [688, 583, 732, 613]},
	{"text": "1.05", "bbox": [785, 585, 832, 612]},
	{"text": "31.53", "bbox": [851, 585, 909, 612]},
	{"text": "Sig", "bbox": [440, 633, 475, 664]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [516, 631, 744, 664]}
]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=9.4s
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[393, 33, 612, 92]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-12-11, bbox=[77, 117, 300, 150]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[336, 117, 530, 150]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[610, 120, 650, 152]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[77, 168, 132, 201]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[337, 168, 417, 201]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:64岁, bbox=[463, 169, 565, 201]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[7]: text=卡号, bbox=[611, 170, 650, 201]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GCP支付, bbox=[80, 219, 267, 252]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[338, 220, 437, 253]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[610, 223, 650, 255]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[81, 269, 133, 302]
2026-08-10 11:15:11,814 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[610, 271, 707, 304]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘, bbox=[84, 317, 251, 350]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[447, 375, 569, 407]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[146, 432, 190, 464]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[245, 432, 337, 464]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[516, 432, 558, 464]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[708, 434, 751, 466]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[804, 434, 847, 466]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[880, 434, 922, 466]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[104, 492, 147, 540]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶, bbox=[226, 487, 735, 520]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[762, 490, 908, 517]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[440, 536, 475, 567]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[515, 536, 745, 567]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片◆, bbox=[228, 584, 382, 616]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[517, 582, 629, 614]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[688, 583, 732, 613]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[785, 585, 832, 612]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[851, 585, 909, 612]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[440, 633, 475, 664]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[516, 631, 744, 664]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] page=11 — 33/33 coords, api_time=9.4s
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] new_positions (33):
[[11, 330.906, 515.304, 19.634999999999998, 54.739999999999995], [11, 64.834, 252.6, 69.615, 89.25], [11, 282.912, 446.26, 69.615, 89.25], [11, 513.62, 547.3, 71.39999999999999, 90.44], [11, 64.834, 111.14399999999999, 99.96, 119.595], [11, 283.75399999999996, 351.114, 99.96, 119.595], [11, 389.846, 475.72999999999996, 100.55499999999999, 119.595], [11, 514.462, 547.3, 101.14999999999999, 119.595], [11, 67.36, 224.814, 130.305, 149.94], [11, 284.596, 367.954, 130.9, 150.535], [11, 513.62, 547.3, 132.685, 151.725], [11, 68.202, 111.98599999999999, 160.055, 179.69], [11, 513.62, 595.294, 161.245, 180.88], [11, 70.728, 211.34199999999998, 188.61499999999998, 208.25], [11, 376.37399999999997, 479.09799999999996, 223.125, 242.165], [11, 122.932, 159.98, 257.03999999999996, 276.08], [11, 206.29, 283.75399999999996, 257.03999999999996, 276.08], [11, 434.472, 469.83599999999996, 257.03999999999996, 276.08], [11, 596.136, 632.342, 258.22999999999996, 277.27], [11, 676.968, 713.174, 258.22999999999996, 277.27], [11, 740.9599999999999, 776.324, 258.22999999999996, 277.27], [11, 87.568, 123.774, 292.74, 321.3], [11, 190.292, 618.87, 289.765, 309.4], [11, 641.6039999999999, 764.536, 291.55, 307.615], [11, 370.47999999999996, 399.95, 318.91999999999996, 337.365], [11, 433.63, 627.29, 318.91999999999996, 337.365], [11, 191.976, 321.644, 347.47999999999996, 366.52], [11, 435.31399999999996, 529.6179999999999, 346.28999999999996, 365.33], [11, 579.2959999999999, 616.3439999999999, 346.885, 364.73499999999996], [11, 660.97, 700.544, 348.075, 364.14], [11, 716.542, 765.3779999999999, 348.075, 364.14], [11, 370.47999999999996, 399.95, 376.635, 395.08], [11, 434.472, 626.448, 375.445, 395.08]]
2026-08-10 11:15:11,815 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=19.3s
2026-08-10 11:15:11,815 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:15:11,816 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:15:11,816 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:15:11,816 INFO     29 [qwen-vl-text] positions(33): [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:15:11,816 INFO     29 [qwen-vl-text] page grouping: [12], lines per page: [33]
2026-08-10 11:15:12,009 INFO     29 [qwen-vl-text] page=12, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:15:12,011 INFO     29 [qwen-vl-text] LLM extraction start, text_len=243
2026-08-10 11:15:12,011 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:12,011 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 409, \"bbox_end\": 441, \"encounter_dates\": [\"2024-11-18\"], \"department\": \"内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "门(急)诊处方\n就诊时间:2024-11-18\n就诊科室:内科门诊\n主诊\n姓名\n性别:男\n年龄:63岁\n卡号:\n患者类型:GLP支付\n医疗证号:\n处方\n地址:\n身份证号:\n诊断:支气管哮喘,非危重\n西药处方\n组号\n项目名称\n规格\n总量\n单价\n金额\nR:\n倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿\n221.61 221.61\nSig\n2揿/次,吸入,bid*30天\n孟鲁司特钠片\n10mg*30/瓶\n30片\n1.05\n31.53\nSig\n10mg/次,口服,qn*30天",
    "role": "user"
  }
]
2026-08-10 11:15:12,015 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:12,015 INFO     29 [qwen-vl-text] LLM output (len=905):
{
  "note_type": "科主任/副主任医师查房记录",
  "record_time": null,
  "recorder": "孙丹丹",
  "reviewer": "彭琼玉",
  "reviewer_title": "副主任医师",
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [],
  "tp_notes": null,
  "condition_changes": "患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异常，子宫收缩好，阴道出血不多，余查无特殊",
  "test_results": "再次复查血常规：白细胞10.59×10⁹/L,中性粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，切口无感染迹象，考虑术后炎性反应",
  "superior_opinion": "患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫产临床路径管理，今日办理出院。指示已执行。",
  "consultation_opinion": null,
  "measures_and_effects": "暂不特殊处理，嘱加强营养，加强运动",
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 11:15:12,017 INFO     29 [qwen-vl-text] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=934998, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共10行）
["彭琼玉副主任医师查房记录", "今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生", "命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异", "常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性", "粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，", "切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任", "医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫", "产临床路径管理，今日办理出院。指示已执行。", "副主任医师：彭琼玉", "主治医师：孙丹丹"]

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
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord API raw response (len=755):
[
	{"text": "彭琼玉副主任医师查房记录", "bbox": [394, 352, 633, 369]},
	{"text": "今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生", "bbox": [167, 378, 924, 397]},
	{"text": "命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异", "bbox": [108, 405, 924, 424]},
	{"text": "常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性", "bbox": [108, 433, 910, 452]},
	{"text": "粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，", "bbox": [108, 461, 900, 479]},
	{"text": "切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任", "bbox": [108, 488, 924, 507]},
	{"text": "医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫", "bbox": [108, 516, 923, 535]},
	{"text": "产临床路径管理，今日办理出院。指示已执行。", "bbox": [107, 543, 511, 561]},
	{"text": "副主任医师：彭琼玉", "bbox": [471, 578, 693, 614]},
	{"text": "主治医师：孙丹丹", "bbox": [695, 587, 887, 615]}
]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord API: raw_items=10, valid_items=10, elapsed=4.2s
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[0]: text=彭琼玉副主任医师查房记录, bbox=[394, 352, 633, 369]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[1]: text=今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生, bbox=[167, 378, 924, 397]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[2]: text=命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异, bbox=[108, 405, 924, 424]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[3]: text=常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性, bbox=[108, 433, 910, 452]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[4]: text=粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，, bbox=[108, 461, 900, 479]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[5]: text=切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任, bbox=[108, 488, 924, 507]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[6]: text=医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫, bbox=[108, 516, 923, 535]
2026-08-10 11:15:16,211 INFO     29 [qwen-vl-text] coord item[7]: text=产临床路径管理，今日办理出院。指示已执行。, bbox=[107, 543, 511, 561]
2026-08-10 11:15:16,212 INFO     29 [qwen-vl-text] coord item[8]: text=副主任医师：彭琼玉, bbox=[471, 578, 693, 614]
2026-08-10 11:15:16,212 INFO     29 [qwen-vl-text] coord item[9]: text=主治医师：孙丹丹, bbox=[695, 587, 887, 615]
2026-08-10 11:15:16,212 INFO     29 [qwen-vl-text] page=13 — 10/10 coords, api_time=4.2s
2026-08-10 11:15:16,212 INFO     29 [qwen-vl-text] new_positions (10):
[[13, 234.42999999999998, 376.635, 296.384, 310.698], [13, 99.365, 549.78, 318.276, 334.274], [13, 64.25999999999999, 549.78, 341.01, 357.008], [13, 64.25999999999999, 541.4499999999999, 364.586, 380.584], [13, 64.25999999999999, 535.5, 388.162, 403.318], [13, 64.25999999999999, 549.78, 410.89599999999996, 426.894], [13, 64.25999999999999, 549.185, 434.472, 450.46999999999997], [13, 63.665, 304.04499999999996, 457.20599999999996, 472.36199999999997], [13, 280.245, 412.335, 486.676, 516.9879999999999], [13, 413.525, 527.765, 494.25399999999996, 517.8299999999999]]
2026-08-10 11:15:16,212 INFO     29 [qwen-vl-text] ═══ DONE ═══ 10 positions, pages=1, time=16.8s
2026-08-10 11:15:16,487 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:15:16,489 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Extractor:Progress | outputs={"chunks": "7 items, types={'ProgressNote': 7}", "html": "", "json": "2326 items", "markdown": "", "text": "", "name": "DAXI-哮喘.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_Progress": "7 items, types={'ProgressNote': 7}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Clinical": "14 items, types={'OutpatientRecord': 14}", "chunks_Prescription": "5 items, types={'PrescriptionRecord': 5}", "chunks_LabExam": "13 items, types={'LabReport': 13}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Admission\": 1, \"chunks_Progress\": 7, \"chunks_Discharge\": 1, \"chunks_Clinical\": 14, \"chunks_Prescription\": 5, \"chunks_LabExam\": 13}"}
2026-08-10 11:15:16,490 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:15:16,498 INFO     29 [ChunkMerger] Merged 46 chunks from 9 sources: {'Extractor:LabExam': 13, 'Extractor:Imaging': 1, 'Extractor:Clinical': 14, 'Extractor:Medication': 1, 'Extractor:Prescription': 5, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5, 'Extractor:Progress': 7} (filtered 2 noise chunks)
2026-08-10 11:15:16,523 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:15:16,523 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "46 items, types={'LabReport': 13, 'OutpatientRecord': 14, 'PrescriptionRecord': 5, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 5, 'ProgressNote': 7}", "name": "DAXI-哮喘.pdf"}
2026-08-10 11:15:16,524 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:15:16,911 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786359894079, 'update_date': datetime.datetime(2026, 8, 10, 11, 4, 54), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 880976, 'status': '1'}
2026-08-10 11:15:17,136 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞数目  WBC  4.28  10^9/L  3.5~9.5  False    淋巴细胞百分比  Lym%  28.4  %  20~50  False    单核细胞百分比  Mon%  4.7  %  3~10  False    中性粒细胞百分比  Neu%  64.4  %  40~75  False    嗜酸性细胞百分比  Eos%  2.4  %  0.4~8  False    嗜碱性细胞百分比  Bas%  0.1  %  0.0~1.0  False    淋巴细胞数目  Lym#  1.22  10^9/L  1.1~3.2  False    单核细胞数目  Mon#  0.20  10^9/L  0.1~0.6  False    中性粒细胞数目  Neu#  2.76  10^9/L  1.8~6.3  False    嗜酸性细胞数目  Eos#  0.10  10^9/L  0.02~0.52  False    嗜碱性细胞数目  Bas#  0.00  10^9/L  0.00~0.06  False    红细胞数目  RBC  4.70  10^12/L  3.8~5.1  False    血红蛋白  HGB  122  g/L  115~150  False    红细胞压积  HCT  37.8  %  35~45  False    平均红细胞体积  MCV  80.4  fL  82~100  True    平均红细胞血红蛋白含量  MCH  26.0  pg  27~34  True    平均红细胞血红蛋白浓度  MCHC  323  g/L  316~354  False    红细胞分布宽度变异系数  RDW-CV  15.2  %  11~16  False    红细胞分布宽度标准差  RDW-SD  43.0  fL  35.0~56.0  False    血小板数目  PLT  224  10^9/L  125~350  False    平均血小板体积  MPV  8.0  fL  6.5~12  False    血小板分布宽度  PDW  16.0  fL  9~17  False    血小板压积  PCT  0.180  %  0.108~  False    大型血小板比率  P-LCR  15.8  %  11~45  False    未成熟粒细胞百分比  IG%  0.4  %  0.0~0.6  False    未成熟粒细胞计数  IG#  0.02  10^9/L  0.00~0.06  False   
---
   血沉  ESR  7  mm/h  0~20  False   
---
   总胆红素  TBIL  8.5  μmol/L  0.0~21.0  False    直接胆红素  DBIL  2.3  μmol/L  0.0~8.0  False    间接胆红素  IBIL  6.2  μmol/L  0.0~13.0  False    谷丙转氨酶  ALT  12.2  U/L  7~40  False    谷草转氨酶  AST  18  U/L  13~35  False    谷草/谷丙  AST/ALT  1.48  None  0.8~1.5  False    总蛋白  TP  73.6  g/L  65.0~85.0  False    白蛋白  ALB  46.0  g/L  40.0~55.0  False    球蛋白  GLB  27.6  g/L  20.0~40.0  False    白球比值  A/G  1.67  None  1.20~2.4  False    谷氨酰转肽酶  GGT  9.0  U/L  7~45  False    碱性磷酸酶  ALP  66  U/L  40~150  False    尿素  Urea  4.27  mmol/L  2.6~7.5  False    肌酐  CRE  49.9  μmol/L  41~73  False   
---
   清洁度  None  II  None  ~ ≤II  False    白细胞  None  5-15  /HP  ≤15/HP  False    红细胞  None  未检出  None  ~ 未检出  False    线索细胞  None  未检出  None  ~ 未检出  False    上皮细胞  None  10-15  None  ~ 满视野  False    滴虫  None  未检出  None  ~ 未检出  False    菌丝  None  未检出  None  ~ 未检出  False    孢子  None  未检出  None  ~ 未检出  False    芽生孢子  None  未检出  None  ~ 未检出  False    菌群密集度  None  ++  None  ~ ++  False    多样性  None  +  None  ~ ++  False    优势菌  None  G+杆菌  None  ~ G阳性杆菌  False    β-N-乙酰氨基葡萄糖苷酶(NAG)  NAG  -  None  ~ -  False    唾液酸苷酶  None  -  None  ~ -  False    白细胞酯酶  None  -  None  ~ -  False    胺试验  None  -  None  ~ -  False    脯氨酸氨基肽酶PIP  PIP  -  None  ~ -  False    过氧化氢(H2O2)  H2O2  +  None  ~ -  True    pH值  None  3.8  None  3.8 ~ 4.5  False   
---
   [β-HCG]人绒毛膜促性腺激素  β-HCG  0.40  mIU/ml  非孕期 0~2.9 0.2-1周 5~50 1-2周 50~500 2-3周 100~5000 3-4周 500~10000 4-5周 1000~50000 5-6周 10000~100000 6-8周 15000~200000  False   
---
   CA-125  CA-125  59.70  U/ml  0.00~35.00  True   
---
   颜色  颜色  黄色  None  清  False    尿酸结晶  尿酸结晶  0  个/ul  0~15  False    浊度  浊度  清亮  None  清  False    草酸钙结晶  草酸钙结晶  0  个/ul  0~30  False    葡萄糖  GLU  -  None  阴性  False    上皮细胞  上皮细胞  14  个/ul  0~20  False    潜血  BLD  -  None  阴性  False    粘液丝  粘液丝  5  个/ul  0~20  False    白细胞  LEU  2+  None  阴性  True    酵母菌  酵母菌  6  个/ul  0~0  True    蛋白质  PRO  -  None  阴性  False    透明管型  透明管型  0  个/ul  0~1  False    亚硝酸盐  NIT  +  None  阴性  True    颗粒管型  颗粒管型  0  个/ul  0~0  False    尿胆素原  URO  -  None  阴性  False    小圆上皮  小圆上皮  0  个/ul  0~3  False    胆红素  BIL  -  None  阴性  False    其他管型  其他管型  0  个/ul  0~0  False    酮体  KET  -  None  阴性  False    其他上皮  其他上皮  0  个/ul  0~10  False    维生素C  Vc  -  None  -  False    异常红细胞  异常红细胞  0  个/ul  0~5  False    酸碱性  pH  6.0  None  5.0~8.5  False    细菌  细菌  1072  个/ul  0~50  True    比重  SG  1.020  None  1.010~  False    尿沉渣镜检  尿沉渣镜检  :  None  None  False    红细胞  红细胞  0  个/ul  0~5  False    白细胞  白细胞  +++/HP  /HP  ≤5/HP  True    白细胞  白细胞  218  个/ul  0~7  True    红细胞  红细胞  未查见  /HP  ≤3/HP  False   
---
   凝血酶原时间  PT  11.0  s  9.4~12.5  False    国际标准化比例  INR  0.98  INR  0.8~1.2  False    凝血酶原活动度  HDD  103.00  %  70~130  False    部分凝血活酶时间(胶质硅)  APTT  33.7  s  25.1~36.5  False    纤维蛋白原  Fib  2.65  g/L  2.00~4.00  False    凝血酶时间  TT  15.1  s  10.3~16.6  False   
---
   白细胞数目  WBC  4.20  10^9/L  3.5~9.5  False    淋巴细胞百分比  Lym%  28.6  %  20~50  False    单核细胞百分比  Mon%  5.0  %  3~10  False    中性粒细胞百分比  Neu%  64.5  %  40~75  False    红细胞压积  HCT  38.3  None  None  False    平均红细胞体积  MCV  81.3  None  None  False    平均红细胞血红蛋白含量  MCH  25.6  None  None  False    平均红细胞血红蛋白浓度  MCHC  313  None  None  False    红细胞分布宽度变异系数  RDW-CV  14.9  None  None  False    红细胞分布宽度标准差  RDW-SD  43.2  None  None  False    血小板数目  PLT  288  None  None  False    平均血小板体积  MPV  9.0  None  None  False    血小板分布宽度  PDW  15.6  None  None  False    血小板压积  PCT  0.258  None  None  False    大型血小板比率  P-LCR  19.3  None  None  False    未成熟粒细胞百分比  IG%  0.1  None  None  False    未成熟粒细胞计数  IG#  0.00  None  None  False   
---
   总胆红素  TBIL  8.7  μmol/L  0.0~21.0  False    直接胆红素  DBIL  3.5  μmol/L  0.0~8.0  False    间接胆红素  IBIL  5.2  μmol/L  0.0~13.0  False    谷丙转氨酶  ALT  7.0  U/L  7~40  False    谷草转氨酶  AST  15  U/L  13~35  False    谷草/谷丙  AST/ALT  2.14  None  0.8~1.5  True    谷氨酰转肽酶  GGT  9.0  U/L  7~45  False    血糖(空腹)  GLU  4.85  mmol/L  3.9~6.10  False    尿素  Urea  4.89  mmol/L  2.6~7.5  False    肌酐  CRE  59.5  μmol/L  41~73  False    血尿酸  URIC  255.04  μmol/L  155~357  False    钾  K  4.10  mmol/L  3.5~5.3  False    钠  Na  139  mmol/L  137~147  False    氯  Cl  105  mmol/L  99~110  False    钙  Ca  2.38  mmol/L  2.11~2.52  False    二氧化碳结合力  CO2cp  27.6  mmol/L  21.0~31.0  False    谷草转氨酶线粒体同工酶  m-AST  2.0  U/L  0~18  False    肌酸激酶  CK  37  U/L  24~200  False    肌酸激酶同工酶  CK-MBm  13  U/L  0.00~24.0  False    乳酸脱氢酶  LDH  132  U/L  109~245  False    a羟基丁酸脱氢酶  HBDH  73  U/L  72~182  False    总胆固醇  CHO  3.80  mmol/L  2.80~5.18  False    甘油三酯  TG  0.71  mmol/L  0.56~1.70  False    高密度脂蛋白胆固醇  HDL-C  1.50  mmol/L  1.04~1.55  False    低密度脂蛋白胆固醇  LDL-C  1.87  mmol/L  0.00~3.37  False   
---
   颜色  颜色  黄色  None  黄、淡黄  False    浊度  浊度  清亮  None  清  False    葡萄糖  GLU  -  None  -  False    尿潜血  NQX  -  None  -  False    白细胞  LEU  -  None  -  False    尿蛋白  PRO  -  None  -  False    亚硝酸盐  NIT  +  None  -  True    尿胆原  URO  -  None  -  False    胆红素  BIL  -  None  -  False    尿酮体  KET  -  None  -  False    pH值  pH  6.0  None  4.5~8.0  False    尿比重  SG  1.020  None  1.003~  False    维生素C  VC  0.0  None  -  False    白细胞  WBC  28.00  mg/l  0~28  False    红细胞  RBC  6.00  mg/l  0~17  False    粘液丝  粘液丝  11  mg/l  0~28  False    结晶  结晶  0.0  mg/l  0~28  False    管型  管型  0  mg/l  0~2  False    上皮细胞  EC  39.00  mg/l  0~34  True    细菌  BACT  163.00  mg/l  0~7  True    真菌  BYST  0  mg/l  0~1  False   
---
   游离三碘甲状腺原氨酸  FT3  3.11  pg/mL  2.14~4.21  False    游离甲状腺素  FR T4  0.76  ng/dL  0.61~1.12  False    超敏促甲状腺素  fTSH3  1.350  uIU/ml  0.560~5.910  False   
---
   乙肝表面抗原(酶免法)  HBsAg  0.04  s/co  阴性  False    丙肝抗体(酶免法)  抗-HCV  0.15  s/co  阴性  False    人免疫缺陷病毒抗体(酶免法)  抗-HIV  0.06  s/co  阴性  False    梅毒螺旋体抗体(酶免法)  TP-Ab  0.07  s/co  阴性  False   
---
姓名：
性别：女
年龄：39岁
民族：汉族
身份证
现住址：
就诊类型：初诊
就诊科室：普通儿科三组（门）
就诊日期：2023-08-14 15:29
联系电话
主诉：咽峡炎购药
现病史：咽峡炎购药
既往史：平素体健，无肝炎、结核类传染病史
过敏史：无
体格检查：发育正常，营养良好，精神一般，口唇红润，双侧扁桃体无肿大，无充血、分泌物。咽腔黏膜无充
血、红肿、疱疹，双肺呼吸音清，听诊心律齐，无杂音，腹平软，无压痛、反跳痛
辅助检查：
初步印象：急性咽峡炎
处理意见：门诊
备注：
医师签名：谭真真
第1页
---
门诊病历
门诊号：
姓名
性别：女
年龄：39岁
民族：汉族
身份证号
现住址：
就诊类型：急诊
就诊科室：妇科一病区(门)
就诊日期：2024-01-05 10:32
联系电话
主诉：下腹痛2小时
现病史：患者月经第二天，无明显诱因出现下腹持续疼痛
既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史
婚育史：
月经史：患者平素月经规律，量中等，色正常，无痛经。
过敏史：无
专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小正常，宫体：正常大小，无压痛。附件：左侧附件区压痛明显。
辅助检查：
初步印象：女性盆腔炎性疾病
处理意见：门诊治疗
备注：
医师签名：汪会芳
第1页
---
姓名
性别:女
年龄:40岁
民族:汉族
2024-12-30 普通儿科三组 (...
身份证号
2024-07-05 普通儿科一组 (...
现住址:
就诊类型:初诊
2024-04-24 普通儿科一组 (...
就诊科室:妇科一病区(门)
就诊日期: 2024-04-08 09:44
联系电话
2024-04-19 普通儿科一组 (...
主诉:月经期下腹间断疼痛2个月
2024-04-08 妇科门诊
现病史:2024.1月经第3天左侧附件区疼痛,超声提示无异常,输消炎药后好转,2024.2无异常,2024.3月经
第3天下腹疼痛但是疼痛程度较前减轻,
2024-04-08 妇科一病区(门)
既往史:平素体健,无高血压、冠心病、糖尿病病史,无肝炎、结核等传染病史,无手术史
2024-01-05 妇科一病区(门)
婚育史:
月经史:患者平素月经规律,量中等,色正常,无痛经。
2023-08-14 普通儿科三组 (...
过敏史:无
2023-07-06 普通儿科三组 (...
专科检查:外阴:发育正常,阴毛呈女性分布;阴道:通畅,粘膜红润,未见异常分泌物;宫颈:光滑,大小
正常,宫体:正常大小,无压痛。附件:双侧附件区未触及明显异常。
辅助检查:
初步印象:女性盆腔炎性疾病
处理意见:门诊检查
备注:
医师签名:权丽丽
第1页
2026-08-10 11:15:17,710 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=门诊号
姓名
性别：女
年龄：40岁
民族：汉族
身份证号
现住址：
就诊类型：初诊
就诊科室：妇科门诊
就诊日期：2024-04-08 11:32
联系电话
主诉：月经期下腹间断疼痛2个月
现病史：2024.1月经第3天左侧附件区疼痛，超声提示无异常，输消炎药后好转，2024.2无异常，2024.3月经
第3天下腹疼痛但是疼痛程度较前减轻，
既往史：平素体健，无高血压、冠心病、糖尿病病史，无肝炎、结核等传染病史，无手术史
婚育史：
月经史：患者平素月经规律，量中等，色正常，无痛经。
过敏史：无
专科检查：外阴：发育正常，阴毛呈女性分布；阴道：通畅，粘膜红润，未见异常分泌物；宫颈：光滑，大小
正常，宫体：正常大小，无压痛。附件：双侧附件区未触及明显异常。
辅助检查：
初步印象：女性盆腔炎性疾病
处理意见：门诊检查
备注：
医师签名：
第1页
---
门诊号
姓
性别：女
年龄：40岁
民族：汉族
身份证号：
现住址：
就诊类型：急诊
就诊科室：普通儿科一组(门)
就诊日期：2024-04-19 08:07
联系电话
主诉：因呼吸道感染）不适要求开药
现病史：患者因（呼吸道感染）不适，要求开药（家属代开）。
既往史：既往体质一般
过敏史：无
体格检查：神志清晰，精神一般，自主体位，查体合作
辅助检查：
初步印象：1、急性上呼吸道感染.2、维生素A缺乏伴夜盲症
处理意见：开立药品
备注：
医师签名：李婉莹
第1页
---
（总）诊病历
门诊号：
姓
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证
职业：专业技术人员
现住址：
就诊类型：初诊
就诊科室：呼吸危重二病区(门)
就诊日期：2025-04-11
14:47
联系电话：
主诉：咳嗽憋气一周
现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊
既往史：平素体健，无高血压、冠心病、糖尿病病史
个人史：无吸烟史
过敏史：无
体格检查：呼吸平稳，口唇无紫绀，听诊：双肺呼吸音清，未闻及干、湿性啰音
辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。
初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]
处理意见：坚持门诊治疗，定期复查
备注：
医师签名：段竹云
第1页
---
门诊病历
门诊号
姓名
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 已婚
身份证号
职业: 职员
现住址:
就诊类型: 初诊
就诊科室:耳鼻咽喉头颈外科
就诊日期: 2025-04-11 15:43
联系电
主诉:鼻塞流涕,咳嗽憋气1周
现病史:1周前发现鼻塞流涕,患者无发热,感冒后咳嗽、憋气,间断治疗,时轻时重,今日来诊
既往史:平素体健,无高血压、冠心病、糖尿病病史
家族史:无家族遗传病史
过敏史:无
体格检查:鼻腔粘膜充血,水肿,水样分泌物附着
辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。
初步印象:1、支气管哮喘(急性发作期)2、过敏性鼻炎[变应性鼻炎]
处理意见:坚持门诊治疗,定期复查
备注:
医师签名:刘秀层
第1页
---
11(急)诊病历
2025-11-27 普通儿科二区(...
2025-11-24 普通儿科二区(...
2025-09-18 普通儿科二区(...
2025-07-11 普通儿科一组(...
2025-06-23 普通儿科三组(...
2025-05-09 呼吸危重二病区(门)
2025-04-11 耳鼻咽喉头颈外...
2025-04-11 呼吸危重二病区(门)
2025-01-06 普通儿科三组(...
2024-12-30 普通儿科三组(...
2024-07-05 普通儿科一组(...
姓名
性别:女
年龄:41岁
民族:汉族
婚姻状况:已婚
身份证
业:专业技术人员
现住址:
就诊类型:复诊
就诊科室:呼吸危重二病区(门)
就诊日期:2025-05-09
17:00
联系电话
主诉:咳嗽憋气一周
现病史:患者无发热,感冒后咳嗽、憋气一周,间断治疗,时轻时重,今日来诊
既往史:平素体健,无高血压、冠心病、糖尿病病史
个人史:无吸烟史
过敏史:无
体格检查:听诊:双肺呼吸音清,未闻及干、湿性啰音
辅助检查:肺功能检查提示中重度阻塞性肺通气功能障碍,支气管舒张试验阳性。
初步印象:1、支气管哮喘.2、过敏性鼻炎[变应性鼻炎]
处理意见:坚持门诊治疗,定期复查
备注:
医师签名:段竹云
第1页
---
门诊号:
姓名
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 小组
身份证号:
职业: 专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科三组(门)
就诊日期: 2025-06-23 10:49
联系电话
主诉: 呼吸道感染购药
现病史: 呼吸道感染购药
既往史: 平素体健, 无肝炎、结核类传染病史
过敏史: 无
体格检查: 发育正常, 营养良好, 精神一般, 口唇红润, 双侧扁桃体无肿大, 无充血、分泌物。咽腔黏膜有充
血, 无红肿、疱疹, 双肺呼吸音清, 听诊心律齐, 无杂音, 腹平软, 无压痛、反跳痛
辅助检查:
初步印象: 上呼吸道感染
处理意见: 门诊药物治疗
备注:
医师签名: 谭真真
第1页
---
门诊号
病历
姓名
性别:女
年龄:41岁
民族:汉族
婚姻状况:未婚
身份证
职业:专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科一组(门)
就诊日期:2025-07-1110:02
联系电话
主诉:呼吸道感染购药
现病史:呼吸道感染购药
既往史:平素体健,无肝炎、结核类传染病史
过敏史:无
体格检查:发育正常,营养良好,精神一般,口唇红润,双侧扁桃体无肿大,无充血、分泌物。咽腔黏膜无充
血、红肿、疱疹,双肺呼吸音清,听诊心律齐,无杂音,腹平软,无压痛、反跳痛
辅助检查:
初步印象:支气管炎
处理意见:门诊药物治疗
备注:
医师签名:赵艳
第1页
---
门诊病历
门诊
姓名:
性别：女
年龄:41岁
民族：汉族
婚姻状况：未婚
身份证
职业：职员
现住址：
就诊类型:初诊
就诊科室:普通儿科二区（门）
就诊日期：2025-09-18 15:22
联系电话
主诉：咽部疼痛伴眼部不适4天
现病史：4天前无明显诱因出现咽部疼痛，伴鼻塞，伴眼部不适，无发热、呕吐、腹泻、皮疹等不适。病后精神、食欲欠佳，大小便正常。
既往史：无特殊。
过敏史：无
体格检查：发育正常，营养良好，精神一般，呼吸平稳，双眼睑结膜充血，口唇红润，咽腔充血，无疱疹，双侧扁桃体I°，充血，无分泌物，双肺呼吸音清，未闻及干湿性啰音，听诊心律齐，无杂音，腹平软，无压痛、反跳痛，未触及包块，肠鸣音活跃，神经系统未见阳性体征。
辅助检查：无
初步印象：1.急性咽峡炎.2.急性变应性结膜炎
处理意见：门诊治疗，动态观察病情变化，不适及时随诊。
备注：
医师签名：赵艳
第1页
---
门诊
1. 门诊病历
2026-01-15 呼吸危重二病区(门)
2026-01-06 妇科一病区(门)
2025-12-09 普通儿科二区(...
2025-12-07 普通儿科二区(...
2025-12-01 普通儿科二区(...
2025-11-27 普通儿科二区(...
2025-11-24 普通儿科二区(...
2025-09-18 普通儿科二区(...
2025-07-11 普通儿科一组(...
2025-06-23 普通儿科三组(...
2025-05-09 呼吸危重二病区(门)
姓名:
性别: 女
年龄:41岁
民族: 汉族
婚姻状况: 未...
身份证:
职业: 专业技术人员
现住址:
就诊类型:初诊
就诊科室:普通儿科二区(门)
就诊日期: 2025-12-01 15:28
联系电
主诉: 发热半天。
现病史: 半天前出现发热, 最高体温38.0℃, 口服药物治疗1次, 无咳嗽, 无喘息, 无呼吸困难, 无咯血, 无腹泻、呕吐等。精神食欲一般, 大小便正常。
既往史: 无。
过敏史: 无
体格检查: 神志清, 精神一般, 呼吸浅快, 咽充血, 扁桃体二度大, 充血, 无疱疹, 无脓点, 双肺呼吸音清,
心音有力, 律齐, 腹软。
辅助检查:
初步印象: 急性上呼吸道感染
处理意见: 口服药物, 动态观察, 不适随诊。
备注:
医师签名: 赵海国
第1页
---
姓名：
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证号
职业：专业技术人员
现住址
就诊类型：初诊
就诊科室：妇科一病区(门)
就诊日期：2026-01-06 08:36
联系电话.
主诉：左下腹间断疼痛1年左右来诊
现病史：患者诉于2024年01月05日无明显诱因出现下腹持续疼痛行相关检查后诊断为盆腔炎性疾病后遗症，
慢性盆腔痛，药物治疗后好转，慢性盆腔痛病程12月，目前疾病状态持续，未治疗。
既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/
非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性
盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状
者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括
药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；
获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否
认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊
娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。
婚育史：已婚已育，孕2产2，有性生活史
手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术
月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-
28天，经期5天，经量较前不变
过敏史：无
生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：
98/76mmHg
体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究
疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。
专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件
区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。
辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清C -
125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。
初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便
黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎
性疾病后遗症，慢性盆腔痛
处理意见：根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患
绍“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临
床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出
门
既往史：2025年11月24日-2025年12月12日本院儿科门诊就诊代家属开药，否认3个月内其他病史及合并用药/非药物治疗，现患者无盆腔炎性疾病急性发作，否认既往有子宫肌瘤、子宫内膜异位症、子宫腺肌病、结核性盆腔炎、间质性膀胱炎、异常子宫出血、盆腔淤血综合征、子宫颈高级别上皮内病变等其他病症引起相关症状者；未放置宫内节育器；无子宫及双侧附件缺如；近2周内未使用过本方案规定研究期间禁止使用的治疗（包括药物和非药物治疗）；无控制不稳定的心血管、肝、肾和血液系统、糖尿病、甲状腺疾病等严重原发性疾病；获得知情同意书前5年内未患有恶性肿瘤；否认对试验用药品过敏，包括对本品成分或者药物辅料有过敏史；否认长期酗酒、药物滥用史；无智力障碍或精神障碍；近1个月内未参加过任何干预性临床试验；患者当前不在妊娠期、哺乳期，同意在试验期间及试验结束后3个月内采取有效避孕措施。
婚育史：已婚已育，孕2产2，有性生活史
手术史：2016年8月31日、2020年7月9日因生产行剖宫产手术
月经史：初潮12岁，既往月经周期规律，经量中，色红，无痛经，末次月经2025.12.29-2025.1.2，周期26-28天，经期5天，经量较前不变
过敏史：无
生命体征：2026.1.6测量身高：160.0cm 体重：51.0kg 体温：36.4℃ 脉搏：76次/分 呼吸：18次/分 血压：98/76mmHg
体格检查：淋巴结、头颈部、胸部、脊柱/四肢/关节、神经系统未见异常，腹部异常（左下腹压痛，CS，研究疾病相关），皮肤黏膜异常（腹部皮肤约5-6cm剖宫产手术瘢痕，NCS），其他未查。
专科检查：外阴已婚型，阴道畅，宫颈光滑，无摇举痛，有宫体压痛，无子宫活动受限或粘连固定，左侧附件区、右侧附件区压痛，无宫骶韧带增粗、变硬、触痛。
辅助检查：今日按方案要求开具血常规、尿沉渣（含尿常规）、肝功八项、肾功两项、血妊娠、血沉、血清CA-125、妇科微生态、十二导联心电图、妇科阴道彩色B超检查，结果详见检查单。
初步印象：盆腔痛中医辨证：主症：下腹胀痛，腰骶部胀痛、带下量多；次症：神疲乏力、口苦口腻、小便黄；舌象：舌质红、苔黄腻；脉象：脉弦滑；2026年01月06日由张丹丹医生辨证为湿热瘀阻症。 西医：盆腔炎性疾病后遗症，慢性盆腔痛
从细之间、根据目前临床表现及患者情况，权丽丽医生于2026年01月06日08时38分在9号楼4楼医患沟通室向患者“妇科千金片治疗盆腔炎性疾病后遗症（湿热瘀阻证）的随机、双盲、安慰剂平行对照、多中心临床试验”及知情同意书内容，已告知参加试验可能的风险与获益，患者已充分理解并同意参加该研究，未提出问题，患者本人于2026年01月06日08时58分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），权丽丽医生于2026年01月06日08时59分签署知情同意书（版本号：V1.0 三门峡市中心医院专用版，版本日期：2025年08月05日），知情同意书原件一份保存于受试者文件夹，一份交给患者本人，确定患者筛选号为04011，进入试验筛选，根据方案要求，收集受试者的试验相关资料，并于今日开始进行筛选期相关检查。
1.已完成体征McCormack量表评分，总分8分，回顾近1周非经期腹痛/腰骶疼痛NRS平均分为5分。
2.嘱受试者合理饮食，避免过度劳累；避免盆浴和坐浴，避免穿紧身衣物和化纤内裤；注意经期卫生。
3.今日结合受试者情况，2026年1月6日血清CA-125示：59.70（0.00-35.00）U/mL，符合排除标准第（8）条，筛选失败，告知受试者转为门诊常规诊疗。
备注：
医师签名：
---
门诊
姓名
性别：女
年龄：41岁
民族：汉族
婚姻状况：已婚
身份证号
职业：其他
现住址
就诊类型：复诊
就诊科室：呼吸危重三病区(门)
就诊日期：2026-01-15
10:56
联系电话
主诉：咳嗽憋气一周
现病史：患者无发热，感冒后咳嗽、憋气一周，间断治疗，时轻时重，今日来诊
既往史：平素体健，无高血压、冠心病、糖尿病病史
个人史：无吸烟史
过敏史：无
体格检查：听诊：双肺呼吸音清，未闻及干、湿性啰音
辅助检查：肺功能检查提示中重度阻塞性肺通气功能障碍，支气管舒张试验阳性。
初步印象：1、支气管哮喘(急性发作期).2、过敏性鼻炎[变应性鼻炎]
处理意见：坚持门诊治疗，定期复查
备注
医师签名：王辉
第1页
---
984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>
返回概览视图
门诊号：2
时间：2026-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容，按回车键检索
查询全部
类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师
药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-02-25 07:47:00 赵海国
药品 鼻渊通窍颗粒 口服 tid 1袋 3 2026-02-12 09:40:21 谭真真
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2026-02-12 09:40:21 谭真真
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2026-01-17 08:04:36 彭文娟
药品 (320ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 320ug 1 2026-01-17 08:04:36 彭文娟
药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-12-07 10:50:33 彭文娟
药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02:43 烟海丽
药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29:34 赵艳
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25:48 赵艳
药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25:48 赵艳
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07:36 赵艳
药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52:35 谭真真
药品 (倾尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04:48 段竹云
共10页 2026-02-12 1 2 3 4 > 前往 1 页
50/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>
时间：2026-02-12 11:40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森
返回概览视图
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容，按回车键检索
查询全部
类型 组 药品名称(规格) 用法 频率 实际用量 总量 开立时间 开立医师
药品 鼻渊通窍颗粒 口服 bid 1袋 2 2025-11-27 15:02.43 烟海丽
药品 盐酸氮卓斯丁滴眼液 滴眼 qid 0.01ml 1 2025-09-18 15:29.34 赵艳
药品 阿莫西林克拉维酸钾片(选) 口服(继续用药) tid 0.375g 24 2025-09-18 15:25.48 赵艳
药品 (成人)双黄连口服液(选) 口服 tid 20ml 2 2025-09-18 15:25.48 赵艳
药品 (160ug)布地奈德福莫特罗粉吸入剂(选) 吸入 bid 160ug 1 2025-07-11 10:07.36 赵艳
药品 (小儿)双黄连口服液(选) 口服 tid 20ml 2 2025-06-23 10:52.35 谭真真
药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 30 2025-05-09 17:04.48 段竹云
药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 2 2025-05-09 17:04.48 段竹云
药品 酮酸泼尼松片 口服 qm 30mg 36 2025-04-11 15:46.53 刘秀层
药品 鼻酸莫米松鼻喷雾剂(选) 喷鼻 bid 100ug 1 2025-04-11 15:31.05 段竹云
药品 (顺尔宁片)孟鲁司特钠片(选) 口服 qn 10mg 5 2025-04-11 15:31.05 段竹云
药品 (320ug)布地奈德福莫特罗粉吸入剂 吸入 bid 320ug 1 2025-04-11 15:31.05 段竹云
药品 磷酸奥司他韦胶囊(东阳光) 口服 bid 75mg 10 2025-01-06 17:15.28 谭真真
药品 氯雷他定颗粒 口服 qd 10mg 1 2024-12-30 10:40:10 谭真真
共70条 20条/页 < 1 2 3 4 > 前往 1
/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
84-04-02
最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>
返回概览视图
门诊时间: 2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容, 按回车键检索
查询全部
类型 组 药品名称[规格] 用法 频率 实际用量 总量 开立时间 开立医师
药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-07-05 09:30:58 李婉莹
药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-07-05 09:30:58 李婉莹
药品 小儿豉翘清热颗粒 口服 tid 6g 3 2024-04-24 11:59:55 赵艳
药品 (成人)双黄连口服液(基选) 口服 tid 20ml 3 2024-04-19 08:14:06 李婉莹
药品 (强力)阿莫西林克拉维酸钾干混悬剂(选) 口服(继续用药) bid 0.457g 2 2024-04-19 08:14:06 李婉莹
药品 (大伊可新)维生素AD滴剂 口服 qd 2000u 3 2024-04-19 08:14:06 李婉莹
药品 (普米克令舒)吸入用布地奈德混悬液 压缩雾化吸入 tid 2ml 20 2024-04-19 08:14:06 李婉莹
药品 替硝唑氯化钠注射液 静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳
药品 左氧氟沙星氯化钠注射液(选) 静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-08-14 15:30:23 谭真真
药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 12g 2 2023-07-06 20:00:14 谭真真
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2023-07-06 20:00:14 谭真真
共70条 20条/页 < 1 2 3 4 > 前往 2 页
---
50/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
984-04-02 首诊日期: 2020-07-08 最近诊疗日期: 2026-02-12 当前在院状态: 出院 过敏: 无 详情>>
返回概览视图
门诊
2026-02-12 11:40:02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称[规格]
药品 替硝唑氯化钠注射液
药品 左氧氟沙星氯化钠注射液(选)
药品 蒲地蓝消炎口服液
药品 (盖克)小儿氨酚黄那敏颗粒
药品 蒲地蓝消炎口服液
药品 (小儿)双黄连口服液(选)
药品 地塞米松磷酸钠注射液(选)
药品 5ml灭菌注射用水
药品 (扑尔敏针)马来酸氯苯那敏注射液
药品 消旋山莨菪碱注射液
药品 头孢克肟颗粒(选)
药品 (天晴速畅)吸入用布地奈德混悬液(选)
药品 (大伊可新)维生素AD滴剂
用法 频率 实际用量 总量 开立时间 开立医师
入
静滴 qd 200ml 6 2024-01-05 10:37:47 程会芳
静滴 qd 0.5g 3 2024-01-05 10:37:47 程会芳
口服 tid 10ml 2 2023-08-14 15:30:23 谭真真
口服 tid 12g 2 2023-07-06 20:00:14 谭真真
口服 tid 10ml 2 2023-07-06 20:00:14 谭真真
口服 tid 20ml 2 2023-07-06 20:00:14 谭真真
外用 bid 10mg 2 2023-06-26 15:19:59 谭真真
外用 bid 5ml 4 2023-06-26 15:19:59 谭真真
外用 bid 20mg 2 2023-06-26 15:19:59 谭真真
外用 bid 20mg 2 2023-06-26 15:19:59 谭真真
口服 bid 100mg 30 2023-05-08 19:56:47 陈音
压缩雾化吸入 bid 2ml 10 2023-05-08 19:52:42 段艳霞
口服 qd 2000u 2 2023-05-08 19:52:42 段艳霞
共70条 20条/页 < 1 2 3 4 > 前往: 2 页
返回概览视图
11.40.02 接诊科室: 呼吸危重三病区(门) 接诊医生: 孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称|规格 用法 频率 实际用量 总量 开立时间 开立医师
药品 *乙2)(大伊可新)维生素AD滴剂 口服 qd 2000u 2 2023-04-07 16:29.03 陈音
药品 乙1)头孢克肟颗粒(选) 口服 bid 100mg 30 2023-04-07 16:28.02 陈音
药品 乙0)阿奇霉素干混悬剂 口服 qd 0.25g 1 2023-04-07 16:27:17 陈音
药品 乙2)三拗片 口服 tid 2片 1 2023-04-07 16:27:17 陈音
药品 乙0)富马酸酮替芬片 口服 bid 1mg 6 2023-04-07 16:27:17 陈音
药品 蒲地蓝消炎口服液 口服 tid 10ml 2 2022-08-08 15:40.53 王晶
药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 5ml 1 2022-05-09 19:49:32 赵海国
药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 3 2022-05-09 19:49:32 赵海国
药品 乙0)5ml灭菌注射用水 外用 bid 20ml 4 2022-05-05 09:58:24 李凌蔚
药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚
药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 10mg 2 2022-05-05 09:58:24 李凌蔚
药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 20mg 2 2022-05-05 09:58:24 李凌蔚
药品 赖氨肌醇维B12口服溶液 口服 bid 10ml 1 2022-05-05 09:57:04 李凌蔚
药品 乙1)复合维生素B片 口服 tid 1片 100 2022-05-05 09:56:29 李凌蔚
药品 用维生素004/基 口服 4 100 2022-05-05 09:56:29 李凌蔚
共70条 20条/页 < 1 2 3 4 > 前往 3 页
---
50/patientsMainPage.html?parentPageJump=1 showTable=true#/patientView
984-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>
返回概览视图
门.
J26-02-12 11.40.02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容，按回车键检索
查询全部
类型 组 药品名称/规格 用法 频率 实际用量 总量 开立时间 开立医师
药品 口服 bid 5ml 1 2022-05-09 19.49.32 赵海国
药品 乙1)盐酸氨溴索口服溶液(基) 口服 bid 10ml 3 2022-05-09 19.49.32 赵海国
药品 赖氨肌醇维B12口服溶液 口服 bid 20ml 4 2022-05-05 09.58.24 李凌蔚
药品 乙0)5ml灭菌注射用水 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚
药品 乙1)(扑尔敏针)马来酸氯苯那敏注射液 外用 bid 10mg 2 2022-05-05 09.58.24 李凌蔚
药品 甲)地塞米松磷酸钠注射液(基) 外用 bid 20mg 2 2022-05-05 09.58.24 李凌蔚
药品 乙1)消旋山莨菪碱注射液(基) 外用 bid 10ml 1 2022-05-05 09.57.04 李凌蔚
药品 赖氨肌醇维B12口服溶液 口服 bid 1片 100 2022-05-05 09.56.29 李凌蔚
药品 乙1)复合维生素B片 口服 tid 5mg 100 2022-05-05 09.56.29 李凌蔚
药品 甲)维生素B2片(基) 口服 tid 50mg 2 2022-05-05 09.54.38 李凌蔚
药品 乙1)头孢克肟颗粒 口服 bid 10ml 1 2022-05-05 09.54.38 李凌蔚
药品 乙1)金振口服液(基) 口服 bid 3g 2 2022-04-19 16.05.18 陈媛
药品 (盖克)小儿氨酚黄那敏颗粒 口服 tid 4ml 1 2022-04-19 16.05.18 陈媛
药品 乙1)美敏伪麻口服溶液 口服 tid 5ml 1 2022-04-19 16.05.18 陈媛
药品 复方氨酚甲麻口服液 口服 qid 20条/页 < 1 2 3 4 > 前往 3 页
共70条
---
184-04-02 首诊日期：2020-07-08 最近诊疗日期：2026-02-12 当前在院状态：出院 过敏：无 详情>>
返回概览视图
2026-02-12 11:40:02 接诊科室：呼吸危重三病区(门) 接诊医生：孙帅森
集成视图 诊断 病历文书 处方 检验 检查 处置 肺功能检查 单机报告 透析治疗 费用 体检报告
请输入药品内容,按回车键检索
查询全部
类型 组 药品名称(规格)
药品 甲)(小儿)双黄连口服液(基)
药品 (盖克)小儿氨酚黄那敏颗粒
药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(基)
药品 蒲地蓝消炎口服液
药品 复方氨酚甲麻口服液
药品 (盖克)小儿氨酚黄那敏颗粒
药品 甲)(抗之膏)阿莫西林克拉维酸钾干混悬剂(国基)
药品 乙0)(普米克令舒)吸入用布地奈德混悬液(国基)
药品 右旋糖酐铁颗粒
药品 盐酸氨卓斯丁滴眼液
用法 频率 实际用量 总量 开立时间 开立医师
口服 tid 10ml 1 2022-03-26 19:51:46 谭真真
口服 tid 6g 2 2022-03-26 19:51:18 谭真真
口服(继续用药) bid 0.228g 2 2022-03-26 19:51:18 谭真真
口服 bid 10ml 1 2022-03-26 19:51:18 谭真真
口服 q6h 10ml 2 2021-11-04 17:18:07 宁秀琴
口服 tid 12g 2 2021-11-04 17:18:07 宁秀琴
口服(继续用药) q12h 0.45g 2 2021-11-04 17:18:07 宁秀琴
压缩雾化 bid 2ml 5 2021-10-11 10:07:54 张冬梅
口服 tid 1袋 80 2021-09-28 15:12:34 党建华
滴双眼 bid 0.1ml 1 2021-09-09 15:18:56 史艳艳
共70条 20条/页 < 1 2 3 4 > 前往 4 页
---
处方笺
4970401
姓名：
性别：□男 □女 年龄：60岁
科别： 费别： 电话/住址：
过敏史：无 开具日期：2021年2月16日
临床诊断：支气管哮喘
Rp
孟鲁司特钠片 10mg 2板
用法：二天一次 1片
审核： 调配： 医师：
核对： 发药： 金额：
2026-08-10 11:15:18,585 INFO     29 [EMBED-PIPELINE] batch[32:48] text_for_embed=出院记录
姓名
科室：产科二区
床号.
住院号.
2020年07月12日
出院记录
患者.
36岁
住院号：
入院日期：2020-07-08 08:36:09
出院日期：2020年07月12日
住院天数：4天
入院情况：以“停经39周，要求住院待产”为主诉入院。入院查体：生命体征平稳，心肺
听诊未闻及异常。腹隆，晚孕腹型，肝脾肋下未触及。专科检查：宫高34CM，腹围102CM，估
计胎儿体宣：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水，骨盆外
测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晚孕宫内单活胎头位(双顶径
9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。
入院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39周头位待产。
诊疗经过：患者入院后完善相关检查，要求剖宫产，于2020年07月09日 08：29-09：30在
腰硬联合麻醉+基础麻醉下行二次子宫下段剖宫产术+子宫修补术。取下腹原横切口，剔除原瘢
痕，逐层进腹，膀下指膀胱，暴露子宫下段，可见子宫下段肌层较薄，胎儿头发及胎脂漂浮，
切开子宫后见羊水清，约600ml，吸净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘
胎膜自娩完整，子宫收缩可，纱布球擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝
合子宫下段肌层，断裂的立皆给予缝合，以伦桥可吸收线分两层连续缝合子宫切口。探查子宫
切口无活动性出血，双侧附件外观正常，关腹，术程顺利，术中出血不多，术后予以降压、抗
感染、加强宫缩支持及对症治疗。
出院诊断：1.妊娠合并子宫瘢痕；2.孕产：宫内孕39+周头位剖宫产：
出院情况：患者精神、饮食好，无特殊不适。查体：生命体征平稳，心肺听诊未闻及明显
异常，双乳泌乳量可，双乳稍涨，腹部平软，切口无红肿、渗出、硬结等愈合良好，子宫收缩
好，宫底约脐耻之间，宫体无压痛，恶露呈淡红色，量少，无异味。现患者一般情况好，双乳
泌乳量多，子宫复旧好，腹部切口愈合良好，无需拆线，达临床治愈，于今日出院。完成计划
性剖宫产临床路径。
出院医嘱：1.注意休息，合理营养；
2.禁性生活、盆浴及重体力劳动2个月；
3.坚持纯母乳喂养大于4-6月；
第 页
总第 页
医院
出院记录
姓名：
科室：产科二区
床号：
住院号：2
4.产后42天门诊复查，如出院后出现任何异常情况请立即就诊，注意产妇心理
状态，必要时心理咨询门诊就诊；若阴道出血淋漓不尽持续1月或阴道出血量多于平素月经
量、腹痛、发热等，及时就诊：（每周二、周六门诊326彭琼玉副主任医师坐诊）
5.严格避孕，术后六个月可安环避孕，术后2年以上方可再次妊娠：
6.新生儿乙肝疫苗第一针，卡介苗已接种，新生儿生后10天补充维生素AD滴剂
1粒/次，一次/日（至2岁），出院后新生儿每日测胆红素值，黄疸加重或持续14天未消退，或
出院后有不适，可直接到1号楼9楼新生儿科探视大厅就诊（携带宝宝就诊卡）；
7.咨询电话产科：
，新生儿科：0398-3118382。母乳咨询电话：
0398-3118618.
主治医师：
孙州
---
院
入院记录
姓名：
科室：产科二区
床号：
科室：产科二区
第(1)次入院记录
过敏史：无
姓名：
性别：女
年龄：36岁
身份证号
职业：
婚姻：已婚
民族：汉族
出生地：
现住址：
入院日期：2020-07-08 08:36:09
邮编
病史采集时间：2020-07-08 08:36:09
联系人：
与病人关系：夫妻
病史叙述者：本人
联系人地址：同上地址
电话.
可靠程度：可靠
主诉：停经39周，要求住院待产。
现病史：平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日（阳历），预产
期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单活胎，发育符合
孕周。孕早期无早孕反应，孕早期无腹痛、出血，阴道流液，出血史，无放射线、有害物质接
触史。孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正常，孕中期行无创DNA
结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正常，未行糖耐量筛
查，未查B族链球菌。孕期经过顺利，孕晚期无头痛、头晕、眼花等症状，无皮肤黄染及痰
痒。现停经39周，无腹痛，未见红及破水，遂入院要求住院待产，门诊以“足月妊娠、瘢痕子
宫”收住院。自孕以来精神好，饮食、睡眠好，大小便正常，体重增加约10KG。
既往史：患者平素体健；否认有“心脏病、高血压、糖尿病、肾病”等慢性病史，否认有
“肝炎、结核”等传染性疾病。于2016.08行剖宫产手术，否认余手术及外伤史。否认有输血
史，有献血史，否认食物及药物过敏史。预防接种随社会进行。
个人史：出生于原籍，护士，本科文化，工作于三门峡市中心医院。否认长期外地居住
史，无疫区居住史，无烟酒等不良嗜好。生长环境一般，否认有冶游史。
婚育史：31岁结婚，爱人
现年37岁，职员，工作于三门峡市党校，身体健康，无吸
烟史，有饮酒史，否认“肝炎、结核”病史，夫妻感情好。孕;产;，2016年足月剖宫产1活男
婴，现体健，否认产后出血及产褥感染史，否认不良孕产史。
月经史：平素月经规律，12岁，5-7天/30-35天，末次月经为：2019年10月08日（阳
历），量中等，色暗红，偶有血块，无痛经。
页
书写者签名：
总第 页
院
入院记录
姓名:
科室:产科二区
床号:
生.
家族史:父母亲体健,1弟1妹均体健,1子体健,否认家族中有遗传性及传染性疾病史。
体格检查
体温:36.5℃
脉搏:78次/分
呼吸:18次/分
血压:98/64mmHg
身高160cm
体重:60Kg
一般状况:发育正常;营养中等;自动体位:面色红润;面容及表情自如;神志清晰;言
语状态流利;检查时能合作等。
皮肤:色泽正常,弹性正常,无水肿、出汗、紫癜、皮疹、色素沉着、蜘蛛痣、瘢痕、创
伤、溃疡、结节。
淋巴结:全身或局部表浅淋巴结未触及肿大;局部皮肤无红热、瘘管、瘢痕。
头部:
头颅:大小无异常、外形无异常;眉发分布正常;无疖、痈、外伤、瘢痕、肿块。
眼部:双眼裂正常,双眼睑无水肿,眼球运动正常。瞳孔:左3.0mm直接对光反应灵敏,
间接对光反应灵敏;右3.0mm直接对光反应灵敏,间接对光反应灵敏。视力粗测正常。
耳部:耳廓无畸形,外耳道无分泌物,乳突无压痛,听力粗测5米。
鼻部:无畸形、鼻翼扇动、阻塞、分泌物、鼻中隔异常、嗅觉障碍、鼻窦压痛等。
口腔:口唇红润,无畸形、疱疹、微血管搏动、口角皲裂;牙齿无缺损、龋病、镶补等异
常;牙龈无溢血、溢脓、萎缩、色素沉着;口腔粘膜无溃疡、假膜、色素沉着;扁桃体无肿
大、分泌物;咽部无充血、分泌物。
颈部:对称,无强直、压痛、运动受限、颈静脉怒张、颈动脉明显搏动、肿块,气管居
中,甲状腺无肿大。
胸部
胸廓:形状正常,对称,运动程度正常,肋间正常,胸壁无水肿、皮下气肿、肿块、静脉
曲张,肋骨及肋软骨无压痛、凹陷等异常。乳头,正常。
肺脏:视诊:腹式呼吸,呼吸节律正常,呼吸深度正常,两侧呼吸运动对称。
触诊:语音震颤两侧相等,无摩擦感。
叩诊:叩诊声响清音,肺下界肩胛线在第10肋间,呼吸移动度6cm,
听诊:呼吸音性质为肺泡呼吸音,强度正常,语音传导正常,无摩擦音、哮鸣音、
第页
书写者签名:
总第页
院
入院记录
姓名：
科室：产科二区
床号
病号：
干啰音、湿啰音。
心脏：视诊：心尖搏动的位置在左侧锁骨中线内第4肋间，范围为2.5cm，强度正常，心前
区无异常搏动、局限性膨隆。
触诊：心尖搏动最强部位在左侧锁骨中线第4肋间，范围为2.5cm，无抬举性搏动、
震颤、摩擦感。
叩诊：左右心界线以每肋间距胸骨中线的cm数记载。
右cm
肋间
左cm
2
Ⅱ
2.5
2
Ⅲ
4
3
Ⅳ
5.5
V
8
左锁骨中线至前正中线的距离9cm。
听诊：心率78次/分，心律整齐，无心脏杂音，无第三心音、第四心音、心音分
裂，P2<A2。
血管：桡动脉搏动正常，血管壁硬度正常。
周围血管征：无毛细血管搏动征、水冲脉、枪击音、动脉异常搏动。
腹部：
视诊：腹部膨隆，晓孕腹型，腹壁对称，无凹陷、膨隆、静脉曲张、蠕动波、局限性隆
起，下腹可见一长约15cm横行手术疤痕。
触诊：腹壁柔软，无压痛，无反跳痛；未触及肿块，无搏动、波动感等。肝脏：肋缘下未
触及，无压痛。胆囊：未触及，无压痛。脾脏：肋缘下未触及。肾：未触及，无压痛等。
叩诊：肝上界位于第5肋间，肝浊音界正常，肝区无叩击痛、脾区无叩击痛、腹部无过度
鼓音，移动性浊音阴性。
听诊：肠蠕动音正常，频率4次/分，胃区无振水声，肝区无摩擦音、脾区无摩擦音，无血
管杂音。
外阴及肛门：阴毛分布正常；外生殖器发育正常，肛门检查：无外痔、肛裂、肛瘘、脱
肛、湿疣等。
脊柱：脊柱无畸形、压痛、叩击痛；脊柱两侧肌肉无紧张、压痛；肋脊角无压痛、叩痛。
四肢：无畸形、杵状指（趾）、静脉曲张、外伤、骨折；肌肉张力正常与肌力5级，无萎
院
入院记录
姓名.
科室:产科二区
床号
住院号.
缩;关节无红肿、畸形、运动障碍,双下肢水肿。
神经反射:膝腱反射正常、跟腱反射正常、肱二头肌腱反射正常、肱三头肌腱反射正常、
腹壁反射正常、巴彬斯基征阴性、克尼格征阴性等。
专科情况
宫高34CM,腹围102CM,估计胎儿体重:3200g,胎位:头位,胎心152次/分,律齐,无
宫缩,未见红,未破水,骨盆外测量及内诊:未做。
辅助检查
B超(2020.07.02 本院):晓孕宫内单活胎头位(双顶径9.4cm,股骨长7.0cm羊水指
数8.5cm),胎盘成熟度II°.
初步诊断:
1.妊娠合并子宫瘢痕;
3.孕2产,宫内孕39周头位待产。
主治医师:
孙小丹
副主任医师:
彭琼玉
2020.07.08
---
呼出气一氧化氮测定报告单
病人信息：
编号：482
姓名：
年龄：41岁9月27天
性别：女
科室：普通儿科一区
出生日期：1984-04-02
测定时间：2026/1/29 11:02:42
测定信息：
一小时内禁止饮食：■是
一小时内禁止剧烈运动：■是
三小时内禁止食用特殊食品*：■是
一小时内禁止抽烟：■是
三天内使用激素类药物：■是 □否
三天内使用抗生素：□是 ■否
症状：□咳嗽 □喘息 □鼻塞 □喷嚏 ■其他
病史：□过敏史 □其它
*是指西兰花、芥蓝、生菜、莴苣、芹菜、水萝卜、熏制、腌制类食品。
测定项目：
呼气方式：■在线 □离线 □潮气
呼气温度：20.1℃
呼气压力：13.6cmH20
呼气平均流速：48ml/s
呼气NO浓度：
32.7,31.0,32.0,31.8,32.1,31.7ppb
呼气NO浓度均值:32ppb
呼气方式：■在线 □离线 □潮气
呼气温度：20.3℃
呼气压力：7.9cmH20
呼气平均流速：207ml/s
呼气NO浓度：
11.7,11.9,11.3,11.6,11.6,11.6ppb
呼气NO浓度均值:12ppb
测定结果：
FeNO50：32ppb
FeNO200：12ppb
CaNO：3.6ppb
测定意义：
测定浓度
参考值
炎症鉴别诊断
>12岁
≤12岁
FeNO50
<25ppb
<20ppb*
非嗜酸性气道炎症
25-50ppb
20-35ppb*
混合型气道炎症
≥50ppb
≥35ppb*
嗜酸性气道炎症
FeNO200
>10ppb
>8ppb
小气道炎症
CaNO
>5ppb
>3ppb
肺泡炎症
(*表示的切点值20与35ppb，对12岁以下儿童，年龄减少1岁，考虑降低1ppb)
复查时间：
操作员：赵彩红
医生：马春英
电
告
单
更
---
肺功能检查报告单
姓名：
测试号：
住院号：
身高：
160 cm
年龄：
41 岁
体重：
48 kg
性别：
女
身份证号：
科别：
联系电话：
预计值
Bst % (Bst/
A1
A2
A3
FVC
[L]
3.13
3.15
100.54
3.15
3.08
3.07
FEV 1
[L]
2.70
1.99
73.90
1.99
1.85
1.96
FEV6
[L]
3.13
3.13
3.05
FEV 1 % FVC
[%]
83.98
63.25
75.31
63.25
60.02
63.82
FEV 1 % VC MAX
[%]
81.31
63.25
77.78
63.25
58.74
62.12
FIF 50
[L/s]
5.84
5.77
5.84
5.48
FEV3 % FVC
[%]
89.30
89.30
87.11
88.97
VC MAX
[L]
3.19
3.15
98.65
2.99
PEF
[L/s]
6.46
6.33
97.97
6.33
5.90
5.95
MMEF 75/25
[L/s]
3.53
1.06
30.03
1.06
0.89
0.99
MEF 25
[L/s]
1.77
0.46
26.28
0.46
0.38
0.40
MEF 50
[L/s]
4.06
1.25
30.90
1.25
1.13
1.24
MEF 75
[L/s]
5.73
3.01
52.56
3.01
2.22
2.68
V backextrapolation [B]
0.06
0.06
0.05
0.06
V backextrapol. % FVC
1.86
1.86
1.52
1.82
FET
[s]
8.73
8.73
5.99
6.71
FEF 200-1200
[L/s]
3.07
3.07
2.51
2.98
FVC IN
[L]
3.19
2.99
93.64
2.26
2.99
2.94
FIV1
[L]
2.96
2.24
2.96
2.92
FIV1 % FVC
[%]
99.14
99.32
99.14
99.48
FEF50 % FIF50
[%]
21.46
21.72
19.34
22.60
PIF
[L/s]
6.10
5.87
6.10
5.50
MVV
[L/min]
101.9
91.45
89.73
91.45
BF MVV
[1/min]
75.65
75.65
10
Flow [L/s]
F/V ex
Vol [L]
Vol%VCmax
Vol [L]
Time [s]
Vol [L]
Time [s]
意见：
1.轻度阻塞性通气功能障碍。
检查质量：FVC：A级。 FEV1：A级。
备注：受检者检查配合佳。结果仅供参考，请结合临床分析。
2.最大自主分钟通气量（MVV）在正常范围。
备注：患者MVV配合佳。结果仅供参考，请结合临床分析。
审核医生：孙帅森
检测技师：韦龙华
2026/1/15
---
肺功能报告单
姓名：
性别：女
出生日期：1984/11/02
年龄：41岁
住院号：
测试号：
身高：160 cm
体重：48 kg
身份证号：
预计
实1 %(实1/预)
实2 %(实2/预)
变异率
测试日期
26/1/15
26/1/15
测试时间
9:51:00上午
10:14:56上午
FVC
[L]
3.13
3.15
100.5
3.25
103.9
3.3
FEV 1
[L]
2.70
1.99
73.9
2.26
83.8
13.4
FEV 1 % FVC
[%]
83.98
63.25
75.3
69.40
82.6
9.7
FEV 1 % VC MAX
[%]
81.31
63.25
77.8
69.40
85.4
9.7
PEF
[L/s]
6.46
6.33
98.0
7.25
112.2
14.5
MEF 75
[L/s]
5.73
3.01
52.6
3.73
65.1
23.8
MEF 50
[L/s]
4.06
1.25
30.9
1.67
41.2
33.3
MEF 25
[L/s]
1.77
0.46
26.3
0.59
33.6
27.7
MMEF 75/25
[L/s]
3.53
1.06
30.0
1.46
41.3
37.6
FET
[s]
8.73
4.94
-43.4
V backextrapolation ex [L]
0.06
0.07
20.1
V backextrapol. % FVC [%]
1.86
2.17
16.3
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
10
F/V In
医生意见：
支气管舒张试验阳性。
（通过储雾罐吸入硫酸沙丁胺醇气雾剂400ug20分钟后。
FEV1较基线增加大于12 %，且绝对值增加大于200 ml。
审核医生：孙帅森
检测技师：朱龙华
肺功能报告单
---
姓名：
出生日期：1984/4/02
门诊/住院/体检：
身高：160 cm
身份证号：
性别：女
年龄：41 岁
测试号：
体重：50 kg
测试日期
测试时间
预计
实测 % (实/预)
25/4/11
14:56:4
VT
[L]
0.36
0.41
114.9
BF
[1/min]
20.00
20.79
104.0
MV
[L/min]
7.14
8.54
119.5
ERV
[L]
1.07
1.07
99.4
VC MAX
[L]
3.19
2.84
88.9
FVC
[L]
3.13
2.84
90.6
FEV 1
[L]
2.70
1.53
56.9
FEV 1 % FVC
[%]
83.98
54.07
64.4
FEV 1 % VC MAX
[%]
81.31
54.07
66.5
PEF
[L/s]
6.46
4.56
70.7
MEF 75
[L/s]
5.73
1.84
32.1
MEF 50
[L/s]
4.06
0.84
20.7
MEF 25
[L/s]
1.77
0.28
15.6
MMEF 75/25
[L/s]
3.53
0.65
18.3
FET
[s]
8.46
V backextrapolation ex
[L]
0.03
V backextrapol. % FVC
[%]
1.23
MVV
[L/min]
101.93
75.75
74.3
FEV 1*30
[L/min]
101.93
46.03
45.2
RV-SB
[L]
1.55
2.56
164.9
RV%TLC-SB
[%]
32.90
47.52
144.4
TLC-SB
[L]
4.77
5.39
112.9
FRC-SB
[L]
2.63
3.31
126.0
FRC%TLC-SB
[%]
51.66
61.42
118.9
DLCOc SB
[mmol/min/kPa]
8.34
6.95
83.4
DLCO SB
[mmol/min/kPa]
8.34
6.95
83.4
医生意见：
1.中重度阻塞性通气功能障碍。
检查质量：FVC：A级 。 FEV1：A级 。
备注：受检者检查配合佳。 结果仅供参考，请结合临床分析。
2.最大自主分钟通气量（MVV）轻度下降。
备注：患者MVV配合佳。结果仅供参考，请结合临床分析。
3.弥散功能在正常范围。4.残总比中度增高。
审核医生：孙帅森
检测技师：张青苹
通气弥散B
2025/4/11 15:18
1/1
---
肺功能报告单
姓名：
性别：女
出生日期：1984/4/02
年龄：41岁
门诊/住院/体检：
测试号：
身高：160 cm
体重：50 kg
身份证号：
预计
实1 %(实1/预)
实2 %(实2/预)
变异率
测试日期
25/4/11
25/4/11
测试时间
14:56:47下午
15:14:32下午
FVC
[L]
3.13
2.84
90.6
3.05
97.4
7.5
FEV 1
[L]
2.70
1.53
56.9
1.91
71.0
24.7
FEV 1 % FVC
[%]
83.98
54.07
64.4
62.70
74.7
16.0
FEV 1 % VC MAX
[%]
81.31
54.07
66.5
62.70
77.1
16.0
PEF
[L/s]
6.46
4.56
70.7
5.64
87.3
23.6
MEF 75
[L/s]
5.73
1.84
32.1
2.65
46.3
44.3
MEF 50
[L/s]
4.06
0.84
20.7
1.23
30.4
47.0
MEF 25
[L/s]
1.77
0.28
15.6
0.44
25.0
60.2
MMEF 75/25
[L/s]
3.53
0.65
18.3
1.02
29.1
58.8
FET
[s]
8.46
6.41
-24.2
V backextrapolation ex [L]
0.03
0.06
71.7
V backextrapol. % FVC [%]
1.23
1.96
59.6
Flow [L/s]
F/V ex
10
5
0
1
2
3
4
5
6
7
10
F/V In
医生意见：
支气管舒张试验阳性。
（通过储雾罐吸入沙丁胺醇气雾剂400ug，20min后。
FEV1较基线增加大于12%，且绝对值增加大于200ml。）
审核医生：孙帅森
检测技师：张青苹
---
姓名：
科室：产科二区
床号
住院号.
2020年07月08日 09时22分
首次病程记录
患
女，36岁，汉族，-以“停经39周，要求住院待产”为主诉于
2020-07-08 08:36:09入院。一、病例特点：1、已婚育龄妇女，孕₂产₁，否认产后出血及产褥
感染史，否认不良孕产史；2、平素月经规律，5-7天/30-35天，末次月经为：2019年10月08日
(阳历)，预产期为2020年07月15日（阳历）。停经50天在我院行B超检查提示宫内早孕，单
活胎，发育符合孕周。3、孕4月余自觉胎动至今，孕期定期在我院行产检。孕早期查NT值正
常，孕中期行无创DNA结果正常，孕5月行四维超声检查未发现异常，行血压正常及空腹血糖正
常，未行糖耐量筛查，未查B族链球菌。4、现停经39周，无腹痛，未见红及破水，遂入院要求
住院待产。5.入院查体：T：36.5℃，P：78次/分，R：18次/分，BP：98/64mmHg。神志清楚，
精神好，全身皮肤黏膜无黄染，浅表淋巴结未触及，心肺听诊未闻及明显异常，腹膨隆。6、
专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律
齐，无宫缩，未见红，未破水，骨盆外测量及内诊：未做。7、辅助检查：B超（2020.07.02
本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度
II°。二、拟诊讨论：（一）初步诊断：1.妊娠合并子宫瘢痕；2.孕₂产；宫内孕39周头位
待产。（二）诊断依据：1、患者有停经史，平素月经规律，平素月经规律，5-7天/35-36天，
末次月经为：2019年10月08日（阳历），预产期为2020年07月15日（阳历），停经后有自觉胎
动，产前检查可同及胎心；2、专科检查：宫高34CM，腹围102CM，估计胎儿体重：3200g，胎
位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及内诊：未做。3、
辅助检查：B超（2020.07.02本院）：晚孕宫内单活胎头位(双顶径9.4cm，股骨长7.0cm
羊水指数8.5cm)，胎盘成熟度II°。（三）鉴别诊断：根据据病史、查体及辅助检查，目前诊
断明确。三、诊疗计划：完善各项检查：心电图、彩超、血常规、血型、凝血五项、输血前检
查、尿常规、心电图、肝功、肾功、血糖、电解质等；2、向患者及家属交代病情，围生期相
关危险因素；3，给予巡视病房、监测胎心、心理疏导，消除围产期恐惧心理等产前护理；4、
患者要求明日剖宫产，纳入剖宫产临床路径。
主治医师：孙州
2020年07月08日 10时22分
---
科主任宋瑞香主治医师查房记录
第页
总第页
姓名：
科室：产科二区
床号：
住院号
今日随科主任宋瑞香主治医师查房，患者精神好，饮食及睡眠可，大小便正常，未破
水，未见红，无腹痛。查体：生命体征平稳，心肺听诊未闻及明显异常，胎心波动于正常范
围，无宫缩。目前诊断：1.妊娠合并于宫瘢痕；2.孕2产；宫内孕39周头位待产。诊断依
据：1.停经后有自觉胎动，产前检查可闻及胎心。2、查体：宫高34CM，腹围102CM，估计胎儿
体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未破水。骨盆外测量及
内诊：未做。3、辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎头位(双顶径
9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。科主任宋瑞香主治医师查房指示：
患者孕足月、瘢痕子宫，若阴道分娩易出现先兆子宫破裂、子宫破裂、胎死宫内等情况，患者
及其家属表示理解，要求明日剖宫产终止妊娠，完善术前谈话，积极术前准备，严密监测胎心
变化。以上医嘱已执行。
主治医师：主治医师：
孙丹
2020年07月08日 10：20
---
术前小结
姓名：
性别：女，年龄：36岁；
病历摘要：以“伴经39周，要求住院待产”为主诉入院。孕2产，否认产后出血及产褥感
染史，否认不良孕产史。查体：生命体征平稳，心肺听诊未闻及异常。腹隆，晚孕腹型。肝脾
肋下未触及，下腹部可见一长约15cm的横行手术瘢痕。双下肢无水肿；专科检查：宫高34CM，
腹围102CM，估计胎儿体重：3200g，胎位：头位，胎心152次/分，律齐，无宫缩，未见红，未
破水。骨盆外测量及内诊：未做。辅助检查：B超（2020.07.02 本院）：晓孕宫内单活胎
头位(双顶径9.4cm，股骨长7.0cm羊水指数8.5cm)，胎盘成熟度II°。入院后要求剖宫产终止
妊娠，手术相关风险已向其讲明，并在手术同意书上签字。请示科主任宋瑞香副主任医师，同
意安排手术，手术医师宋瑞香主治医师查看病人，生命体征平稳，无手术禁忌，积极术前准
备。
术前诊断：1.妊娠合并子宫瘢痕；2.孕2产；宫内孕39周头位待产。
手术指证：足月妊娠，瘢痕子宫，患者及家属要求，无手术禁忌症：
拟施手术名称和方式：拟定于明日07：30行二次子宫下段剖宫产术；
拟施麻醉：椎管内麻醉；
第 页
总第 页
院
姓名：
科室：产科二区
床号：
注意事項：规范操作，彻底止血，待新生儿娩出后，给予“缩宫素针”促宫缩治疗，做好
新生儿复苏工作。
主治医师：
孙丹丹
第 页
总第 页
---
院
姓名：
科室：产科二区
床：
住院号：
2020年07月09日 09时47分
术后首次病程记录
患者术前测胎心150次/分，于今日08：29-09：30在腰硬联合麻醉+基础麻醉下行二次子宫
下段剖宫产术+子宫修补术，取下腹原横切口，剔除原瘢痕，逐层进腹，膀下指膀胱，暴露子
宫下段，可见于宫下段肌层较薄，胎儿头发及胎脂漂浮，切开子宫后见羊水清，约600ml，吸
净后以头位助娩一活男婴，出生1-10分钟均评10分，胎盘胎膜自娩完整，子宫收缩可，纱布球
擦拭子宫腔，可见子宫下段肌层断裂，用可吸收线间断缝合子宫下段肌层，断裂的血管给予缝
合，以恰桥可吸收线分两层连续缝合子宫切口。探查子宫切口无活动性出血，双侧附件外观正
常，关腹。术程顺利，术中麻醉好，呼吸血压平稳，输入晶体液800ml，胶体液0ml，出血不
多，约200ml，尿色清，量约100ml，术中诊断：1.妊娠合并子宫瘢痕；2.孕2产：宫内孕39*1周
头位剖宫产；术后安返病房，测P：64次/分，R：18次/分，Bp：84/54mmHg，术后给予“头
孢唑林钠针”预防感染、加强宫缩、会阴冲洗、尿管护理及支持对症等治疗，并嘱其按摩双下
肢预防下肢静脉血栓形成，注意观察生命体征、子宫收缩及阴道出血情况。
住院医师：冯雪云
2020年07月10日 09时00分
---
彭琼玉副主任医师查房记录
今日为剖宫产术后一天，患者精神、睡眠好，无特殊不适，未排气。彭琼玉副主任医师
查房：查体：生命体征平稳，双乳不胀，无泌乳，心肺未闻及异常，腹软，腹部切口皮肤对合
好，未见红肿、硬结等异常，宫底平脐，子宫收缩好，阴道出血不多，尿管畅，尿色清，尿量
正常，余查无特殊，查房意见：现术后一天，未排气，流食，体温正常，切口无感染迹象，病
情无特殊，继续抗炎补液加强宫缩等治疗；嘱患者床上多翻身并按摩双下肢，以防术后肠粘连
及栓塞性疾病发生，给予肌注缩宫素10uBID促进子宫收缩，给予子宫复旧磁疗促进产后子宫
恢复，嘱保持乳房畅通，并给予泌乳磁疗促进乳汁分泌，输完液体后拔除尿管，适当下床活
动，注意监测血糖情况，上述指示已执行。
副主任医师：马
住院医师：冯雪云
2020年07月11日 08时06分
---
术后第二天，患者无发热，已排气，尿管拔除后排尿畅。查体：生命体征平稳，心肺听诊
第 页
总第 页
出院
姓名：
科室：产科二区
床号
住院
未闻及异常，双乳泌乳量不多，腹软，子宫收缩好，宫底位于脐下两横指，无压痛，阴道出血
不多，暗红色，无异味，腹部切口换药见切口皮缘对合好，未见红肿、硬结及渗液等异常，双
下肢无水肿，现术后第二天，病情稳定，改为II级护理，已排气给予苔含，注意体温变化及切
口情况；继续予子宫复旧磁疗促进产后子宫恢复，加用腹部切口红外线治疗促进伤口愈合，加
益宫颗粒(自各药物)促宫缩治疗，观察体温及阴道恶露情况。
主治医师：孙丹丹
2020年07月12日 10时00分
---
彭琼玉副主任医师查房记录
今日查房，患者剖宫产术后三天，患者未诉不适，精神好，饮食、睡眠正常，查体：生
命体征平稳，心肺听诊未闻及异常，双乳泌乳量多，腹软，腹部切口无红肿、硬结、渗液等异
常，子宫收缩好，阴道出血不多，余查无特殊，再次复查血常规：白细胞10.59×10⁹/L,中性
粒细胞86.3%，偏高，血红蛋白100g/L，患者复查白细胞正常，中性粒细胞偏高，体温正常，
切口无感染迹象，考虑术后炎性反应，暂不特殊处理，嘱加强营养，加强运动。彭琼玉副主任
医师查房指示：患者现病情稳定，腹部伤口皮内结合，无需拆线，达临床治愈，顺利完成剖宫
产临床路径管理，今日办理出院。指示已执行。
副主任医师：彭琼玉
主治医师：孙丹丹
2026-08-10 11:15:19,536 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:15:19,537 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "46 items, types={'LabReport': 13, 'OutpatientRecord': 14, 'PrescriptionRecord': 5, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 5, 'ProgressNote': 7}", "name": "DAXI-哮喘.pdf", "embedding_token_consumption": 26927}
2026-08-10 11:15:19,537 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:15:19,543 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:19,543 INFO     29 [qwen-vl-text] LLM output (len=666):
{
  "encounter_date": "2024-11-18",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": "内科门诊",
  "diagnosis": "支气管哮喘,非危重",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入",
      "duration_days": 30,
      "quantity": "1",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qn",
      "route": "口服",
      "duration_days": 30,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:15:19,543 INFO     29 [qwen-vl-text] Updated encounter_dates=[2024-11-18]
2026-08-10 11:15:19,545 INFO     29 [qwen-vl-text] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1479468, prompt_len=955
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共33行）
["门(急)诊处方", "就诊时间:2024-11-18", "就诊科室:内科门诊", "主诊", "姓名", "性别:男", "年龄:63岁", "卡号:", "患者类型:GLP支付", "医疗证号:", "处方", "地址:", "身份证号:", "诊断:支气管哮喘,非危重", "西药处方", "组号", "项目名称", "规格", "总量", "单价", "金额", "R:", "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "221.61 221.61", "Sig", "2揿/次,吸入,bid*30天", "孟鲁司特钠片", "10mg*30/瓶", "30片", "1.05", "31.53", "Sig", "10mg/次,口服,qn*30天"]

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
2026-08-10 11:15:29,867 INFO     29 [qwen-vl-text] coord API raw response (len=1691):
[
	{"text": "门(急)诊处方", "bbox": [383, 26, 592, 85]},
	{"text": "就诊时间:2024-11-18", "bbox": [80, 112, 294, 144]},
	{"text": "就诊科室:内科门诊", "bbox": [325, 110, 513, 142]},
	{"text": "主诊", "bbox": [590, 110, 644, 142]},
	{"text": "姓名", "bbox": [80, 163, 118, 195]},
	{"text": "性别:男", "bbox": [325, 161, 403, 193]},
	{"text": "年龄:63岁", "bbox": [447, 160, 547, 192]},
	{"text": "卡号:", "bbox": [590, 160, 640, 192]},
	{"text": "患者类型:GLP支付", "bbox": [80, 214, 257, 245]},
	{"text": "医疗证号:", "bbox": [325, 212, 421, 244]},
	{"text": "处方", "bbox": [590, 210, 640, 242]},
	{"text": "地址:", "bbox": [80, 263, 130, 295]},
	{"text": "身份证号:", "bbox": [590, 260, 686, 292]},
	{"text": "诊断:支气管哮喘,非危重", "bbox": [81, 309, 331, 343]},
	{"text": "西药处方", "bbox": [430, 366, 551, 398]},
	{"text": "组号", "bbox": [140, 425, 184, 458]},
	{"text": "项目名称", "bbox": [235, 425, 323, 458]},
	{"text": "规格", "bbox": [498, 424, 539, 456]},
	{"text": "总量", "bbox": [687, 424, 728, 456]},
	{"text": "单价", "bbox": [781, 423, 822, 455]},
	{"text": "金额", "bbox": [855, 423, 898, 455]},
	{"text": "R:", "bbox": [100, 487, 142, 535]},
	{"text": "倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿", "bbox": [218, 480, 713, 513]},
	{"text": "221.61 221.61", "bbox": [738, 480, 884, 510]},
	{"text": "Sig", "bbox": [424, 531, 460, 563]},
	{"text": "2揿/次,吸入,bid*30天", "bbox": [498, 529, 723, 561]},
	{"text": "孟鲁司特钠片", "bbox": [220, 579, 351, 611]},
	{"text": "10mg*30/瓶", "bbox": [500, 578, 610, 610]},
	{"text": "30片", "bbox": [668, 577, 711, 609]},
	{"text": "1.05", "bbox": [763, 577, 808, 607]},
	{"text": "31.53", "bbox": [827, 577, 885, 607]},
	{"text": "Sig", "bbox": [424, 630, 460, 662]},
	{"text": "10mg/次,口服,qn*30天", "bbox": [500, 627, 723, 660]}
]
2026-08-10 11:15:29,867 INFO     29 [qwen-vl-text] coord API: raw_items=33, valid_items=33, elapsed=10.3s
2026-08-10 11:15:29,867 INFO     29 [qwen-vl-text] coord item[0]: text=门(急)诊处方, bbox=[383, 26, 592, 85]
2026-08-10 11:15:29,867 INFO     29 [qwen-vl-text] coord item[1]: text=就诊时间:2024-11-18, bbox=[80, 112, 294, 144]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[2]: text=就诊科室:内科门诊, bbox=[325, 110, 513, 142]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[3]: text=主诊, bbox=[590, 110, 644, 142]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[4]: text=姓名, bbox=[80, 163, 118, 195]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[5]: text=性别:男, bbox=[325, 161, 403, 193]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:63岁, bbox=[447, 160, 547, 192]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[7]: text=卡号:, bbox=[590, 160, 640, 192]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[8]: text=患者类型:GLP支付, bbox=[80, 214, 257, 245]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[9]: text=医疗证号:, bbox=[325, 212, 421, 244]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[10]: text=处方, bbox=[590, 210, 640, 242]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[11]: text=地址:, bbox=[80, 263, 130, 295]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[12]: text=身份证号:, bbox=[590, 260, 686, 292]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[13]: text=诊断:支气管哮喘,非危重, bbox=[81, 309, 331, 343]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[14]: text=西药处方, bbox=[430, 366, 551, 398]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[15]: text=组号, bbox=[140, 425, 184, 458]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[16]: text=项目名称, bbox=[235, 425, 323, 458]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[17]: text=规格, bbox=[498, 424, 539, 456]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[18]: text=总量, bbox=[687, 424, 728, 456]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[19]: text=单价, bbox=[781, 423, 822, 455]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[20]: text=金额, bbox=[855, 423, 898, 455]
2026-08-10 11:15:29,868 INFO     29 [qwen-vl-text] coord item[21]: text=R:, bbox=[100, 487, 142, 535]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[22]: text=倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿, bbox=[218, 480, 713, 513]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[23]: text=221.61 221.61, bbox=[738, 480, 884, 510]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[24]: text=Sig, bbox=[424, 531, 460, 563]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[25]: text=2揿/次,吸入,bid*30天, bbox=[498, 529, 723, 561]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[26]: text=孟鲁司特钠片, bbox=[220, 579, 351, 611]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[27]: text=10mg*30/瓶, bbox=[500, 578, 610, 610]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[28]: text=30片, bbox=[668, 577, 711, 609]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[29]: text=1.05, bbox=[763, 577, 808, 607]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[30]: text=31.53, bbox=[827, 577, 885, 607]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[31]: text=Sig, bbox=[424, 630, 460, 662]
2026-08-10 11:15:29,869 INFO     29 [qwen-vl-text] coord item[32]: text=10mg/次,口服,qn*30天, bbox=[500, 627, 723, 660]
2026-08-10 11:15:29,870 INFO     29 [qwen-vl-text] page=12 — 33/33 coords, api_time=10.3s
2026-08-10 11:15:29,870 INFO     29 [qwen-vl-text] new_positions (33):
[[12, 322.486, 498.464, 15.469999999999999, 50.574999999999996], [12, 67.36, 247.548, 66.64, 85.67999999999999], [12, 273.65, 431.94599999999997, 65.45, 84.49], [12, 496.78, 542.2479999999999, 65.45, 84.49], [12, 67.36, 99.356, 96.985, 116.02499999999999], [12, 273.65, 339.32599999999996, 95.795, 114.835], [12, 376.37399999999997, 460.574, 95.19999999999999, 114.24], [12, 496.78, 538.88, 95.19999999999999, 114.24], [12, 67.36, 216.394, 127.33, 145.775], [12, 273.65, 354.48199999999997, 126.14, 145.18], [12, 496.78, 538.88, 124.94999999999999, 143.98999999999998], [12, 67.36, 109.46, 156.48499999999999, 175.525], [12, 496.78, 577.612, 154.7, 173.73999999999998], [12, 68.202, 278.702, 183.855, 204.08499999999998], [12, 362.06, 463.942, 217.76999999999998, 236.81], [12, 117.88, 154.928, 252.875, 272.51], [12, 197.87, 271.966, 252.875, 272.51], [12, 419.316, 453.83799999999997, 252.28, 271.32], [12, 578.454, 612.976, 252.28, 271.32], [12, 657.602, 692.124, 251.685, 270.72499999999997], [12, 719.91, 756.116, 251.685, 270.72499999999997], [12, 84.2, 119.564, 289.765, 318.325], [12, 183.55599999999998, 600.346, 285.59999999999997, 305.235], [12, 621.396, 744.328, 285.59999999999997, 303.45], [12, 357.008, 387.32, 315.945, 334.98499999999996], [12, 419.316, 608.766, 314.755, 333.79499999999996], [12, 185.23999999999998, 295.542, 344.505, 363.54499999999996], [12, 421.0, 513.62, 343.90999999999997, 362.95], [12, 562.456, 598.662, 343.315, 362.35499999999996], [12, 642.446, 680.336, 343.315, 361.16499999999996], [12, 696.334, 745.17, 343.315, 361.16499999999996], [12, 357.008, 387.32, 374.84999999999997, 393.89], [12, 421.0, 608.766, 373.065, 392.7]]
2026-08-10 11:15:29,870 INFO     29 [qwen-vl-text] ═══ DONE ═══ 33 positions, pages=1, time=18.1s
2026-08-10 11:15:29,870 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:15:29,879 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:15:29,880 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:15:29,880 INFO     29 [qwen-vl-text] positions(29): [[14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0], [14, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:15:29,880 INFO     29 [qwen-vl-text] page grouping: [14], lines per page: [29]
2026-08-10 11:15:30,060 INFO     29 [qwen-vl-text] page=14, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 11:15:30,062 INFO     29 [qwen-vl-text] LLM extraction start, text_len=269
2026-08-10 11:15:30,062 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:30,063 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 482, \"bbox_end\": 510, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n普通\n诊疗\n患者姓\n男\n年龄：65岁\n费别：\n科室：\n2026-01-06 11:28:26\n处方号\n地址：\n联系电\n身份号\n诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎\nR\nP:\n倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120\n1瓶\n剂量：每次2揿 （1/60 瓶）\n用法：吸入用药\nbid 01-06\n孟鲁司特钠片(省采)◆\n10mg*5/盒\n30片\n剂量：每次10mg （1 片）\n用法：口服\nqd 01-06\n处方金额：298.47元\n取药药房：门诊西药房（荔湾）",
    "role": "user"
  }
]
2026-08-10 11:15:30,066 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:15:30.065+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 17, "failed": 0, "current": {"15a0534894a911f1bd9827cf206dfa2d": {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:15:30,067 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:15:30,067 INFO     29 [Trace] task=15a05348 | doc=DAXI-哮喘.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"partial\",\"synced_chunks\":45,\"skipped_hallucinated\":0,\"failed\":[{\"chunk_id\":\"3081663301b133b5\",\"error\":\"(sqlalchemy.dialects.postgresql.asyncpg.Error) <class 'asyncpg.exceptions.StringDataRi...(962 chars)"}
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=26 row[0]=(39, 131, 220, 166, 178) row[-1]=(39, 425, 541, 437, 449)
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(40, 158, 218, 124, 139) row[-1]=(40, 158, 218, 124, 139)
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=14 row[0]=(41, 91, 176, 183, 198) row[-1]=(41, 91, 149, 423, 438)
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=19 row[0]=(42, 59, 105, 186, 200) row[-1]=(42, 59, 88, 635, 648)
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(43, 67, 202, 254, 287) row[-1]=(43, 67, 202, 254, 287)
2026-08-10 11:15:30,088 INFO     29 [DIAG-EXECUTOR] row_position_int len=1 row[0]=(44, 158, 202, 125, 138) row[-1]=(44, 158, 202, 125, 138)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=30 row[0]=(45, 106, 162, 174, 187) row[-1]=(45, 423, 501, 421, 434)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=6 row[0]=(46, 78, 181, 187, 202) row[-1]=(46, 78, 168, 283, 298)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=17 row[0]=(47, 121, 212, 163, 175) row[-1]=(47, 425, 545, 437, 449)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=25 row[0]=(48, 106, 186, 189, 202) row[-1]=(48, 424, 550, 419, 433)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=21 row[0]=(49, 48, 115, 203, 218) row[-1]=(49, 426, 527, 403, 418)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=3 row[0]=(50, 67, 232, 197, 211) row[-1]=(50, 67, 205, 234, 248)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int len=4 row[0]=(51, 84, 224, 223, 239) row[-1]=(51, 84, 236, 290, 307)
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,089 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,090 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,092 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,092 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,093 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,093 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,093 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,093 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,094 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:15:30,100 INFO     29 set_progress(15a0534894a911f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:15:30 [DOC Engine]:
Start to index...
2026-08-10 11:15:30,139 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.033s]
2026-08-10 11:15:30,400 INFO     29 set_progress(15a0534894a911f1bd9827cf206dfa2d), progress: 0.8021739130434783, progress_msg: 
2026-08-10 11:15:30,437 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.015s]
2026-08-10 11:15:30,459 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 11:15:30,478 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 11:15:30,501 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 11:15:30,521 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 11:15:30,550 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.021s]
2026-08-10 11:15:30,567 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 11:15:30,593 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.018s]
2026-08-10 11:15:30,612 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 11:15:30,631 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.012s]
2026-08-10 11:15:30,647 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 11:15:30,656 INFO     29 set_progress(15a0534894a911f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:15:30 Indexing done (0.56s). Task done (1539.01s)
2026-08-10 11:15:30,662 INFO     29 [Done], chunks(46), token(26927), elapsed:1539.01
2026-08-10 11:15:31,344 INFO     29 handle_task done for task {"id": "15a0534894a911f1bd9827cf206dfa2d", "doc_id": "153d1f1c94a911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "DAXI-\u54ee\u5598.pdf", "type": "pdf", "location": "DAXI-\u54ee\u5598.pdf", "size": 25392062, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786358935844, "task_type": "dataflow", "root_trace_id": "8daf5e0f40214f739134726fc4b74f82", "root_traceparent": "00-8daf5e0f40214f739134726fc4b74f82-de4b1c88ad0d73e8-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 11:15:32,978 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:32,979 INFO     29 [qwen-vl-text] LLM output (len=702):
{
  "encounter_date": "2026-01-06",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": null,
  "diagnosis": "支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎",
  "items": [
    {
      "drug_generic_name": "倍氯米松福莫特罗吸入气雾剂",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "2揿",
      "frequency": "bid",
      "route": "吸入用药",
      "duration_days": null,
      "quantity": "1瓶",
      "notes": null
    },
    {
      "drug_generic_name": "孟鲁司特钠片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "30片",
      "notes": null
    }
  ]
}
2026-08-10 11:15:32,979 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-10 11:15:32,983 INFO     29 [qwen-vl-text] coord API call start, page=14, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=858191, prompt_len=969
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["处方笺", "普通", "诊疗", "患者姓", "男", "年龄：65岁", "费别：", "科室：", "2026-01-06 11:28:26", "处方号", "地址：", "联系电", "身份号", "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "R", "P:", "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "1瓶", "剂量：每次2揿 （1/60 瓶）", "用法：吸入用药", "bid 01-06", "孟鲁司特钠片(省采)◆", "10mg*5/盒", "30片", "剂量：每次10mg （1 片）", "用法：口服", "qd 01-06", "处方金额：298.47元", "取药药房：门诊西药房（荔湾）"]

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
2026-08-10 11:15:41,644 INFO     29 [qwen-vl-text] coord API raw response (len=1543):
[
	{"text": "处方笺", "bbox": [397, 8, 473, 41]},
	{"text": "普通", "bbox": [643, 54, 671, 74]},
	{"text": "诊疗", "bbox": [229, 115, 260, 135]},
	{"text": "患者姓", "bbox": [229, 149, 264, 167]},
	{"text": "男", "bbox": [411, 145, 424, 163]},
	{"text": "年龄：65岁", "bbox": [452, 143, 516, 161]},
	{"text": "费别：", "bbox": [564, 143, 595, 161]},
	{"text": "科室：", "bbox": [229, 181, 257, 199]},
	{"text": "2026-01-06 11:28:26", "bbox": [411, 177, 535, 194]},
	{"text": "处方号", "bbox": [564, 175, 600, 194]},
	{"text": "地址：", "bbox": [229, 210, 257, 229]},
	{"text": "联系电", "bbox": [563, 207, 600, 227]},
	{"text": "身份号", "bbox": [229, 241, 264, 260]},
	{"text": "诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎", "bbox": [230, 261, 720, 283]},
	{"text": "R", "bbox": [243, 315, 267, 354]},
	{"text": "P:", "bbox": [265, 331, 277, 349]},
	{"text": "倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120", "bbox": [246, 373, 564, 394]},
	{"text": "1瓶", "bbox": [602, 376, 620, 392]},
	{"text": "剂量：每次2揿 （1/60 瓶）", "bbox": [297, 405, 445, 431]},
	{"text": "用法：吸入用药", "bbox": [470, 409, 551, 426]},
	{"text": "bid 01-06", "bbox": [580, 411, 648, 428]},
	{"text": "孟鲁司特钠片(省采)◆", "bbox": [247, 472, 376, 490]},
	{"text": "10mg*5/盒", "bbox": [460, 473, 515, 490]},
	{"text": "30片", "bbox": [597, 474, 619, 489]},
	{"text": "剂量：每次10mg （1 片）", "bbox": [298, 503, 444, 520]},
	{"text": "用法：口服", "bbox": [468, 504, 523, 520]},
	{"text": "qd 01-06", "bbox": [575, 507, 640, 522]},
	{"text": "处方金额：298.47元", "bbox": [251, 878, 394, 900]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [492, 877, 679, 898]}
]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.7s
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[0]: text=处方笺, bbox=[397, 8, 473, 41]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[643, 54, 671, 74]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗, bbox=[229, 115, 260, 135]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[3]: text=患者姓, bbox=[229, 149, 264, 167]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[4]: text=男, bbox=[411, 145, 424, 163]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[5]: text=年龄：65岁, bbox=[452, 143, 516, 161]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[6]: text=费别：, bbox=[564, 143, 595, 161]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[7]: text=科室：, bbox=[229, 181, 257, 199]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[8]: text=2026-01-06 11:28:26, bbox=[411, 177, 535, 194]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[9]: text=处方号, bbox=[564, 175, 600, 194]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[10]: text=地址：, bbox=[229, 210, 257, 229]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[11]: text=联系电, bbox=[563, 207, 600, 227]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[12]: text=身份号, bbox=[229, 241, 264, 260]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[13]: text=诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎, bbox=[230, 261, 720, 283]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[14]: text=R, bbox=[243, 315, 267, 354]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[15]: text=P:, bbox=[265, 331, 277, 349]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[16]: text=倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120, bbox=[246, 373, 564, 394]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[17]: text=1瓶, bbox=[602, 376, 620, 392]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[18]: text=剂量：每次2揿 （1/60 瓶）, bbox=[297, 405, 445, 431]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[19]: text=用法：吸入用药, bbox=[470, 409, 551, 426]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[20]: text=bid 01-06, bbox=[580, 411, 648, 428]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[21]: text=孟鲁司特钠片(省采)◆, bbox=[247, 472, 376, 490]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[22]: text=10mg*5/盒, bbox=[460, 473, 515, 490]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[23]: text=30片, bbox=[597, 474, 619, 489]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[24]: text=剂量：每次10mg （1 片）, bbox=[298, 503, 444, 520]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[25]: text=用法：口服, bbox=[468, 504, 523, 520]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[26]: text=qd 01-06, bbox=[575, 507, 640, 522]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[27]: text=处方金额：298.47元, bbox=[251, 878, 394, 900]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] coord item[28]: text=取药药房：门诊西药房（荔湾）, bbox=[492, 877, 679, 898]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] page=14 — 29/29 coords, api_time=8.7s
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] new_positions (29):
[[14, 334.274, 398.26599999999996, 4.76, 24.395], [14, 541.406, 564.982, 32.129999999999995, 44.03], [14, 192.81799999999998, 218.92, 68.425, 80.325], [14, 192.81799999999998, 222.28799999999998, 88.655, 99.365], [14, 346.062, 357.008, 86.27499999999999, 96.985], [14, 380.584, 434.472, 85.085, 95.795], [14, 474.888, 500.99, 85.085, 95.795], [14, 192.81799999999998, 216.394, 107.695, 118.405], [14, 346.062, 450.46999999999997, 105.315, 115.42999999999999], [14, 474.888, 505.2, 104.125, 115.42999999999999], [14, 192.81799999999998, 216.394, 124.94999999999999, 136.255], [14, 474.046, 505.2, 123.16499999999999, 135.065], [14, 192.81799999999998, 222.28799999999998, 143.39499999999998, 154.7], [14, 193.66, 606.24, 155.295, 168.385], [14, 204.606, 224.814, 187.42499999999998, 210.63], [14, 223.13, 233.23399999999998, 196.945, 207.655], [14, 207.132, 474.888, 221.935, 234.42999999999998], [14, 506.88399999999996, 522.04, 223.72, 233.23999999999998], [14, 250.07399999999998, 374.69, 240.975, 256.445], [14, 395.74, 463.942, 243.355, 253.47], [14, 488.35999999999996, 545.616, 244.545, 254.66], [14, 207.974, 316.592, 280.84, 291.55], [14, 387.32, 433.63, 281.435, 291.55], [14, 502.674, 521.198, 282.03, 290.955], [14, 250.916, 373.848, 299.28499999999997, 309.4], [14, 394.056, 440.366, 299.88, 309.4], [14, 484.15, 538.88, 301.66499999999996, 310.59], [14, 211.34199999999998, 331.748, 522.41, 535.5], [14, 414.264, 571.718, 521.8149999999999, 534.31]]
2026-08-10 11:15:41,645 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=11.8s
2026-08-10 11:15:41,646 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 11:15:41,647 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 11:15:41,647 INFO     29 [qwen-vl-text] ═══ START ═══ type=PrescriptionRecord, doc_id=None
2026-08-10 11:15:41,647 INFO     29 [qwen-vl-text] positions(41): [[15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0], [15, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 11:15:41,647 INFO     29 [qwen-vl-text] page grouping: [15], lines per page: [41]
2026-08-10 11:15:41,867 INFO     29 [qwen-vl-text] page=15, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 11:15:41,868 INFO     29 [qwen-vl-text] LLM extraction start, text_len=309
2026-08-10 11:15:41,868 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:41,869 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{\"type\": \"PrescriptionRecord\", \"bbox_start\": 511, \"bbox_end\": 551, \"encounter_dates\": [\"2026-01-06\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "处方笺\n普通\n诊断\n患者\n年龄：65岁\n费别\n科室\n6-01-06 11:31:02\n处方\n地址\n联系\n身份\n诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎\nRp:\n左氧氟沙星片(省采)●⑥\n0.5g*28片/盒\n3片\n剂量：每次0.5g\n(1 片)\n用法：口服\nqd\n01-06\n醋酸泼尼松片●②⑥\n5mg*100/瓶\n6片\n剂量：每次10mg\n(2 片)\n用法：口服\nqm\n01-06\n盐酸氨溴索分散片(省采)●⑥\n30mg*50/盒\n15片\n剂量：每次30mg\n(1 片)\n用法：餐后口服\ntid\n01-06\n处方金额：3.47元\n取药药房：门诊西药房（荔湾）\n医师手签：",
    "role": "user"
  }
]
2026-08-10 11:15:45,465 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:45,466 INFO     29 [qwen-vl-text] LLM output (len=956):
{
  "encounter_date": "2026-01-06",
  "prescription_type": "门诊处方",
  "prescriber": null,
  "department": null,
  "diagnosis": "支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎",
  "items": [
    {
      "drug_generic_name": "左氧氟沙星片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "0.5g",
      "frequency": "qd",
      "route": "口服",
      "duration_days": null,
      "quantity": "3片",
      "notes": "省采"
    },
    {
      "drug_generic_name": "醋酸泼尼松片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "10mg",
      "frequency": "qm",
      "route": "口服",
      "duration_days": null,
      "quantity": "6片",
      "notes": null
    },
    {
      "drug_generic_name": "盐酸氨溴索分散片",
      "drug_trade_name": null,
      "drug_category": "西药",
      "dosage": "30mg",
      "frequency": "tid",
      "route": "口服",
      "duration_days": null,
      "quantity": "15片",
      "notes": "餐后口服, 省采"
    }
  ]
}
2026-08-10 11:15:45,466 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-06]
2026-08-10 11:15:45,468 INFO     29 [qwen-vl-text] coord API call start, page=15, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1247901, prompt_len=1045
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共41行）
["处方笺", "普通", "诊断", "患者", "年龄：65岁", "费别", "科室", "6-01-06 11:31:02", "处方", "地址", "联系", "身份", "诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎", "Rp:", "左氧氟沙星片(省采)●⑥", "0.5g*28片/盒", "3片", "剂量：每次0.5g", "(1 片)", "用法：口服", "qd", "01-06", "醋酸泼尼松片●②⑥", "5mg*100/瓶", "6片", "剂量：每次10mg", "(2 片)", "用法：口服", "qm", "01-06", "盐酸氨溴索分散片(省采)●⑥", "30mg*50/盒", "15片", "剂量：每次30mg", "(1 片)", "用法：餐后口服", "tid", "01-06", "处方金额：3.47元", "取药药房：门诊西药房（荔湾）", "医师手签："]

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
2026-08-10 11:15:57,964 INFO     29 [qwen-vl-text] coord API raw response (len=2116):
[
	{"text": "处方笺", "bbox": [378, 104, 494, 127]},
	{"text": "普通", "bbox": [744, 140, 784, 153]},
	{"text": "诊断", "bbox": [107, 170, 130, 186]},
	{"text": "患者", "bbox": [106, 194, 130, 208]},
	{"text": "年龄：65岁", "bbox": [464, 193, 560, 206]},
	{"text": "费别", "bbox": [635, 195, 672, 208]},
	{"text": "科室", "bbox": [104, 216, 130, 230]},
	{"text": "6-01-06 11:31:02", "bbox": [434, 215, 590, 228]},
	{"text": "处方", "bbox": [635, 216, 672, 230]},
	{"text": "地址", "bbox": [104, 237, 130, 251]},
	{"text": "联系", "bbox": [635, 238, 672, 251]},
	{"text": "身份", "bbox": [104, 259, 130, 273]},
	{"text": "诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎", "bbox": [104, 273, 876, 290]},
	{"text": "Rp:", "bbox": [125, 314, 180, 344]},
	{"text": "左氧氟沙星片(省采)●⑥", "bbox": [129, 358, 375, 375]},
	{"text": "0.5g*28片/盒", "bbox": [482, 358, 604, 373]},
	{"text": "3片", "bbox": [707, 356, 734, 369]},
	{"text": "剂量：每次0.5g", "bbox": [213, 387, 350, 401]},
	{"text": "(1 片)", "bbox": [380, 386, 455, 400]},
	{"text": "用法：口服", "bbox": [497, 386, 589, 400]},
	{"text": "qd", "bbox": [675, 386, 695, 399]},
	{"text": "01-06", "bbox": [723, 384, 782, 398]},
	{"text": "醋酸泼尼松片●②⑥", "bbox": [128, 440, 328, 457]},
	{"text": "5mg*100/瓶", "bbox": [479, 438, 583, 453]},
	{"text": "6片", "bbox": [706, 435, 734, 448]},
	{"text": "剂量：每次10mg", "bbox": [213, 467, 348, 481]},
	{"text": "(2 片)", "bbox": [380, 465, 454, 479]},
	{"text": "用法：口服", "bbox": [495, 465, 587, 479]},
	{"text": "qm", "bbox": [674, 466, 694, 478]},
	{"text": "01-06", "bbox": [722, 463, 781, 477]},
	{"text": "盐酸氨溴索分散片(省采)●⑥", "bbox": [133, 517, 418, 533]},
	{"text": "30mg*50/盒", "bbox": [479, 515, 581, 529]},
	{"text": "15片", "bbox": [705, 513, 740, 526]},
	{"text": "剂量：每次30mg", "bbox": [219, 543, 351, 557]},
	{"text": "(1 片)", "bbox": [380, 541, 453, 555]},
	{"text": "用法：餐后口服", "bbox": [494, 541, 622, 555]},
	{"text": "tid", "bbox": [671, 541, 699, 554]},
	{"text": "01-06", "bbox": [719, 540, 778, 554]},
	{"text": "处方金额：3.47元", "bbox": [126, 803, 339, 823]},
	{"text": "取药药房：门诊西药房（荔湾）", "bbox": [533, 803, 853, 821]},
	{"text": "医师手签：", "bbox": [644, 838, 742, 848]}
]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord API: raw_items=41, valid_items=41, elapsed=12.5s
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[0]: text=处方笺, bbox=[378, 104, 494, 127]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[1]: text=普通, bbox=[744, 140, 784, 153]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[2]: text=诊断, bbox=[107, 170, 130, 186]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[3]: text=患者, bbox=[106, 194, 130, 208]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：65岁, bbox=[464, 193, 560, 206]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[5]: text=费别, bbox=[635, 195, 672, 208]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[6]: text=科室, bbox=[104, 216, 130, 230]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[7]: text=6-01-06 11:31:02, bbox=[434, 215, 590, 228]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[8]: text=处方, bbox=[635, 216, 672, 230]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[9]: text=地址, bbox=[104, 237, 130, 251]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[10]: text=联系, bbox=[635, 238, 672, 251]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[11]: text=身份, bbox=[104, 259, 130, 273]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[12]: text=诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎, bbox=[104, 273, 876, 290]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[13]: text=Rp:, bbox=[125, 314, 180, 344]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[14]: text=左氧氟沙星片(省采)●⑥, bbox=[129, 358, 375, 375]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[15]: text=0.5g*28片/盒, bbox=[482, 358, 604, 373]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[16]: text=3片, bbox=[707, 356, 734, 369]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[17]: text=剂量：每次0.5g, bbox=[213, 387, 350, 401]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[18]: text=(1 片), bbox=[380, 386, 455, 400]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[19]: text=用法：口服, bbox=[497, 386, 589, 400]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[20]: text=qd, bbox=[675, 386, 695, 399]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[21]: text=01-06, bbox=[723, 384, 782, 398]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[22]: text=醋酸泼尼松片●②⑥, bbox=[128, 440, 328, 457]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[23]: text=5mg*100/瓶, bbox=[479, 438, 583, 453]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[24]: text=6片, bbox=[706, 435, 734, 448]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[25]: text=剂量：每次10mg, bbox=[213, 467, 348, 481]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[26]: text=(2 片), bbox=[380, 465, 454, 479]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[27]: text=用法：口服, bbox=[495, 465, 587, 479]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[28]: text=qm, bbox=[674, 466, 694, 478]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[29]: text=01-06, bbox=[722, 463, 781, 477]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[30]: text=盐酸氨溴索分散片(省采)●⑥, bbox=[133, 517, 418, 533]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[31]: text=30mg*50/盒, bbox=[479, 515, 581, 529]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[32]: text=15片, bbox=[705, 513, 740, 526]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[33]: text=剂量：每次30mg, bbox=[219, 543, 351, 557]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[34]: text=(1 片), bbox=[380, 541, 453, 555]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[35]: text=用法：餐后口服, bbox=[494, 541, 622, 555]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[36]: text=tid, bbox=[671, 541, 699, 554]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[37]: text=01-06, bbox=[719, 540, 778, 554]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[38]: text=处方金额：3.47元, bbox=[126, 803, 339, 823]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[39]: text=取药药房：门诊西药房（荔湾）, bbox=[533, 803, 853, 821]
2026-08-10 11:15:57,965 INFO     29 [qwen-vl-text] coord item[40]: text=医师手签：, bbox=[644, 838, 742, 848]
2026-08-10 11:15:57,966 INFO     29 [qwen-vl-text] page=15 — 41/41 coords, api_time=12.5s
2026-08-10 11:15:57,966 INFO     29 [qwen-vl-text] new_positions (41):
[[15, 224.91, 293.93, 87.568, 106.934], [15, 442.68, 466.47999999999996, 117.88, 128.826], [15, 63.665, 77.35, 143.14, 156.612], [15, 63.07, 77.35, 163.34799999999998, 175.136], [15, 276.08, 333.2, 162.506, 173.452], [15, 377.825, 399.84, 164.19, 175.136], [15, 61.879999999999995, 77.35, 181.87199999999999, 193.66], [15, 258.22999999999996, 351.05, 181.03, 191.976], [15, 377.825, 399.84, 181.87199999999999, 193.66], [15, 61.879999999999995, 77.35, 199.554, 211.34199999999998], [15, 377.825, 399.84, 200.396, 211.34199999999998], [15, 61.879999999999995, 77.35, 218.078, 229.86599999999999], [15, 61.879999999999995, 521.22, 229.86599999999999, 244.17999999999998], [15, 74.375, 107.1, 264.388, 289.64799999999997], [15, 76.755, 223.125, 301.436, 315.75], [15, 286.78999999999996, 359.38, 301.436, 314.066], [15, 420.66499999999996, 436.72999999999996, 299.752, 310.698], [15, 126.735, 208.25, 325.854, 337.642], [15, 226.1, 270.72499999999997, 325.012, 336.8], [15, 295.715, 350.455, 325.012, 336.8], [15, 401.625, 413.525, 325.012, 335.95799999999997], [15, 430.185, 465.28999999999996, 323.328, 335.116], [15, 76.16, 195.16, 370.47999999999996, 384.794], [15, 285.005, 346.885, 368.796, 381.426], [15, 420.07, 436.72999999999996, 366.27, 377.216], [15, 126.735, 207.06, 393.214, 405.002], [15, 226.1, 270.13, 391.53, 403.318], [15, 294.525, 349.265, 391.53, 403.318], [15, 401.03, 412.93, 392.372, 402.476], [15, 429.59, 464.695, 389.846, 401.63399999999996], [15, 79.13499999999999, 248.70999999999998, 435.31399999999996, 448.786], [15, 285.005, 345.695, 433.63, 445.418], [15, 419.47499999999997, 440.29999999999995, 431.94599999999997, 442.892], [15, 130.305, 208.845, 457.20599999999996, 468.99399999999997], [15, 226.1, 269.53499999999997, 455.522, 467.31], [15, 293.93, 370.09, 455.522, 467.31], [15, 399.245, 415.905, 455.522, 466.46799999999996], [15, 427.805, 462.90999999999997, 454.68, 466.46799999999996], [15, 74.97, 201.70499999999998, 676.126, 692.966], [15, 317.135, 507.53499999999997, 676.126, 691.2819999999999], [15, 383.18, 441.48999999999995, 705.596, 714.016]]
2026-08-10 11:15:57,966 INFO     29 [qwen-vl-text] ═══ DONE ═══ 41 positions, pages=1, time=16.3s
2026-08-10 11:15:57,973 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 11:15:57,974 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Prescription | outputs={"chunks": "11 items, types={'PrescriptionRecord': 11}", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:15:57,974 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 11:15:57,980 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:57,981 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:15:58,865 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:58,879 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 11:15:58,880 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Discharge | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:15:58,880 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 11:15:58,889 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:58,889 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:15:59,451 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:59,465 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 11:15:59,466 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:15:59,466 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 11:15:59,479 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:15:59,479 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:16:00,644 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:16:00,654 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 11:16:00,655 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:ExaminationReport | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:16:00,655 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 11:16:00,664 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:16:00,664 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 11:16:01,129 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T11:16:01.127+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 18, "failed": 0, "current": {"4e8b5bc494ab11f1bd9827cf206dfa2d": {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 11:16:01,148 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 11:16:01,161 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 11:16:01,162 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "582 items", "markdown": "", "text": "", "name": "HXJ 哮喘 广三.pdf", "output_format": "chunks", "chunks_Clinical": "4 items, types={'OutpatientRecord': 4}", "chunks_Prescription": "11 items, types={'PrescriptionRecord': 11}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Clinical\": 4, \"chunks_Prescription\": 11, \"chunks_LabExam\": 1}"}
2026-08-10 11:16:01,162 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 11:16:01,164 INFO     29 [ChunkMerger] Merged 16 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 4, 'Extractor:Medication': 1, 'Extractor:Prescription': 11, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 1, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 11:16:01,180 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 11:16:01,181 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 1, 'OutpatientRecord': 4, 'PrescriptionRecord': 11}", "name": "HXJ 哮喘 广三.pdf"}
2026-08-10 11:16:01,181 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 11:16:01,327 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786360519514, 'update_date': datetime.datetime(2026, 8, 10, 11, 15, 19), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 907903, 'status': '1'}
2026-08-10 11:16:01,540 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞  WBC  9.17  10^9/L  3.5 -- 9.5  False    中性粒细胞总数  NEU  5.71  10^9/L  1.8 -- 6.3  False    中性粒细胞百分数  NEUN  62.30  %  40 -- 75  False    淋巴细胞总数  LY  2.62  10^9/L  1.1 -- 3.2  False    淋巴细胞百分数  LYN  28.60  %  20 -- 50  False    单核细胞总数  MONO  0.47  10^9/L  0.1 -- 0.6  False    单核细胞百分数  MON%  5.10  %  3 -- 10  False    嗜酸性粒细胞总数  EOS  0.34  10^9/L  0.02 -- 0.52  False    嗜酸性粒细胞百分数  EOS%  3.70  %  0.4 -- 8  False    嗜碱性粒细胞总数  BASO  0.03  10^9/L  0 -- 0.06  False    嗜碱性粒细胞百分比  BASO%  0.30  %  0 -- 1  False    红细胞  RBC  4.91  10^12/L  4.3 -- 5.8  False    血红蛋白  HGB  158  g/L  130 -- 175  False    红细胞压积  HCT  47.10  %  40 -- 50  False    红细胞平均容积  MCV  96.90  fl  82 -- 100  False    红细胞平均血红蛋白  MCH  32.20  pg  27 -- 34  False    红细胞平均血红蛋白浓度  MCHC  335.00  g/L  316 -- 354  False    红细胞分布宽度  RDW  12.40  %  11.6 -- 14.8  False    红细胞分布宽度-SD  RDW-SD  44.10  fl  37.1 -- 49.2  False    血小板  PLT  197  10^9/L  125 -- 350  False    平均血小板容积  MPV  10.70  fl  6 -- 12  False    平均血小板比容  Pct  0.21  %  0.10 -- 0.29  False    血小板分布宽度  PDW  13.00  10(GSP)  15.3 -- 20.5  True    大血小板  P-LCR  30.90  %  None  False    网织红细胞绝对值  RETR  90.5  10^9/L  46.4 -- 121.2  False    网织红细胞百分数  RETR  1.64  %  None  False    低荧光强度网织红细胞比率  LFF  83.8  %  89.9 -- 98.4  True    中荧光强度网织红细胞比率  MFF  13.3  %  1.6 -- 9.5  True    高荧光强度网织红细胞比率  HFF  2.9  %  0 -- 1.7  True    未成熟网织红细胞比率  IRF  16.2  %  1.6 -- 10.5  True    有核红细胞计数  NRBCW  0  10^9/L  None  False    有核红细胞百分比  NRBC%  0  %  None  False   
---
门(急)诊病历信息
就诊卡
流水
病历编号:
姓
别:男
年
龄:64岁
就诊科室:内科门诊(荔湾)
医
诊时间:2025-10-21 16:24:23
主
诉:取药
现病史:
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
支气管哮喘
单病种:
发病时间:
处置:请仔细阅读药品说明书等文书资料,遵嘱诊疗,不适随诊。
1孟鲁司特钠片(省采)◆
1瓶10.0mg,口服,每晚1次
30天
2倍氯米松福莫特罗吸入气雾剂◆①
1瓶2.0揿,吸入用药,一天2次
30天
备注:建议在住地附近社区医疗机构随诊。
---
门(急)诊病历信息
就诊卡号:
流水号:
病历编号:
性别:男
年
龄:65岁
就诊科室:内科门诊(荔湾)
医生:
就诊时间:2025-11-19 11:33:52
主诉:取药
现病史:
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
1、支气管哮喘
处置:
1孟鲁司特钠片(省采)◆
1瓶10.0mg,口服,每晚1次
30天
2倍氯米松福莫特罗吸入气雾剂◆①
1瓶2.0揿,吸入用药,一天2次
30天
备注:
---
门(急)诊病历信息
就诊卡号
流水
姓名
性别:男
年
龄:65岁
就诊科室:内科门诊(荔湾)
病历编号:
就诊时间:2025-12-12 09:26:46
主诉:BAIYUN V8
现病史:自上次访视至今,询问及查询HIS系统受试者无新增AE、SAE、哮喘急性发作,有新增合并用药。发生过2次医疗相关事件,就诊于荔湾区逢源街道社区中心1次,就诊于专科门诊1次。期间未收到ePRO触发的哮喘警报邮件。
完成下流操作:
1、静坐10分钟后,测量坐位生命体征,血压:120/76mmHg,脉搏频率:59次/分(NCS),呼吸:20次/分,体温:36.5℃;
2、9:20体格检查:神志清,体置合作,自主体位,一般外表无异常,皮肤、粘膜无异常,唇甲无发绀,眼睛、耳、鼻、咽喉无异常,口咽部粘膜无异常,颈软,气管居中,甲状腺未及肿大,全身浅表淋巴结未及肿大,颈静脉无怒张,胸廓无畸形,双肺呼吸运动对称,双肺触觉语颤正常,双肺叩诊清音,双肺呼吸音清,未闻及啰音。心前区无隆起,心尖搏动无弥散,心界不大,心率:59次/分,律齐,各瓣膜听诊区未闻及病理性杂音。腹平软,全腹无压痛、反跳痛。肝、脾肋下未及,肝肾区无叩击痛,肠鸣音存,4次/分,脊柱、四肢无畸形,生理征存,未引出病理征,其他系统未见明显异常。
3、查看受试者电子日志,受试者漏填2025年10月26日(早间日志)、8月23日、9月10日、9月19日、9月24日、10月5日、10月25日、11月3日、12月2日(晚间日志)。
4、填写AQLQ+12和ACQ-5问卷,ACQ-5评分:1.0分。
5、休息至少10分钟后,行12导联ECG检查。
6、10:42采集中心实验室样本(血常规、血生化)并送往中心实验室。
7、回收试验药物BDA MDI AS MDI 3盒(137968-KF未开封、102035-IM未用74喷,实际已用:24喷,发药当天预喷4喷,2025.8.18-2025.9.10期间因超过7天未使用试验药物预喷1次共2喷,2025.9.10-11.19期间每七天清洗装置后预喷10次共20喷,总计预喷26喷;199863-TA未用106喷,实际已用:8喷,2025.11.20当天预喷4喷,2025.11.20-2025.12.12期间每七天清洗装置后预喷3次共6喷,总计预喷10喷)ePro记录使用总共32喷,与实际使用情况一致。
CS 扫描全能王
3亿人都在用的扫描App
门诊病历
25/10/21 16时 门诊病历
25/11/19 11时 门诊病历（GCP专用）
25/12/12 09时 门诊病历（GCP专用）
1、颈痛综合征:开始时间:2025年1月8日,持续中,中度,非SAE,与试验药物无关,对试验
药物采取措施:剂量无需改变,未因该AE退出研究,采取理疗。
2、功能性消化不良:开始时间:2025年5月20日,持续中,中度,非SAE,与试验药物无
关,对试验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:药物治疗。
病因:无诱因,症状:下腹痛,进食后明显,休息后可缓解。
3、慢性胃炎:开始时间:2025年3月4日,持续中,中度,非SAE,与试验药物无关,对试
验药物采取措施:剂量无需改变,未因该AE退出研究,对AE采取措施:暂无治疗措施。
跟踪合并用药
1、糠酸莫米松鼻喷雾剂 2024.7.19-2025.9.ub 每周每早一腔 喷鼻 必要时 治疗过敏
性鼻炎。
2、盐酸二甲双胍片 2024.10.10-2025.9.14 0.5 TID 治疗2型糖尿病。
3、达格列净片 2025.9.15至今 10mg qm 治疗2型糖尿病。
补充合并用药:1、硫酸特布他林雾化吸入用溶液 2025.6.17-2025.6.19 5mg 吸
入 qd 治疗急性支气管炎。
预约下次安全性电话随访时间。
既往史:
过敏史:
个人史:
体格检查:
专科情况:
辅助检查:
治疗项目:
门诊诊断:
1、支气管哮喘
处置:
心电图(心电图室做)
伯氟米松福莫特罗吸入气雾剂① 1瓶2.0瓶,吸入用药,一天2次 30天
孟鲁司特钠片(省采)① 6盒10.0mg,口服,每日1次(口服) 30天
备注:
医生:
---
病历编号：
姓名：
性别：男
年龄：65岁
就诊科室：内科门诊（基础）
医生：
就诊时间：2026-02-04 11:23:30
主诉：支气管哮喘治疗后复诊
现病史：2022年3月前开始出现咳嗽、咯痰，粘白，量少，能咯出，咳嗽呈阵发性，偶则激性，伴轻度咽痒，无气促，夜间有喘息、胸闷，伴鼻塞、流涕、喉咙，无咽痛，
无反酸、嗳气、腹胀，无上腹部隐痛不适感，无伴发热、畏寒，曾自服肺力咳症状未见缓解，现病情好转、稳定，本次门诊距上次门诊间隔时间7天；过去4周，症状控制情况：控制良好，吸入药物使用情况：遵医嘱使用；，吸入装置使用情况：有，正确；急性发作情况：
两次就诊期间急性发作：发作次数：0次，长期规律使用倍氯米松福莫特罗吸入气雾剂治疗。
既往史：鼻炎病史，有糖尿病史
过敏史：未发现
个人史：否认遗传病史，吸烟30年，6支/日，已戒烟8年，饮酒6年，1两/日。
体格检查：神志清，口腔无溃疡、粘膜白斑，肝在肋下，鼻塞，通气，气管居中，双肺呼吸音稍减弱，未闻及明显干湿性罗音。
专科情况：
辅助检查：血常规：Q-CRP：0.54mg/l 白细胞：5.5*109/L 中性粒细胞：
5.17*109/L 60.5% 淋巴细胞：2.23*109/L 26.2% 单个核细胞：
0.46*109/L 5.4% 嗜酸性粒细胞：0.6*109/L 7.1% 呼出气一氧化
氮：FeNO50：130ppb FnNO10：161ppb 肺功能：轻度阻塞性通气功能障碍，支气管激发
试验阳性（PD20=0.312mg AHI：轻度），胸片：心、肺、膈未见异常
治疗项目：
门诊诊断：
1、支气管哮喘，2、过敏性鼻炎[变应性鼻炎]，3、2型糖尿病
单病种：
发病时间：
处置：请仔细阅读药品说明书等文书资料，遵嘱治疗，不适随诊。
倍氯米松福莫特罗吸入气雾剂◆① 1瓶2.0瓶，吸入用药，一天2次 30天
孟鲁司特钠片（省采）◆ 6盒10.0mg，口服，每日1次（口服） 30天
备注：建议在停药附近社区医疗机构随访。
---
门(急)诊处方
就诊时间:2025-09-15
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:64岁
卡号:4
患者
医疗证号:
处方号
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
倍氯米松福莫特罗吸入气雾剂◆
6ug/揿*120揿
221.61
221.61
Sig
2揿/次,吸入,bid*30天
医师
医生编号:1326
配剂人:
核对人:
合计:
收费员:
打印时间:2025-12-19
为了您的用药安全,药物处方当天有效 第 1 页共 1 页
---
门(急)诊处方
就诊时间:2025-08-18
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
孟鲁司特钠片◆
10mg*30/瓶
28片
1.05
29.43
Sig
10mg/次,口服,qn*28天
倍氯米松福莫特罗吸入气雾剂0.05/6ug/揿*120揿
221.61
221.61
Sig
2揿/次,吸入,bid*30天
---
门(急)诊处方
就诊时间:2025-05-30
就诊科室:内科门诊
主
姓名
性别:男
年龄:64岁
卡
患者类型:GCP支付
医疗证号:
处
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
孟鲁司特钠片◆
10mg*5/盒
90片
2.56
230.58
Sig
10mg/次,口服,qn*90天
倍氯米松福莫特罗吸入气雾剂0006ug/揿*120瓶
221.61
664.83
Sig
2揿/次,吸入,bid*90天
---
门(急)诊处方
就诊时间:2025-03-05
就诊科室:内科门诊
主诊医
姓名
性别:男
年龄:64岁
卡号:
患者类型:GCP支付
医疗证号:
处方号:
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂*0ug/6ug/瓶*120瓶
221.61 443.22
Sig
2揿/次,吸入,bid*60天
孟鲁司特钠片
10mg*30/瓶
60片
1.05
63.06
Sig
10mg/次,口服,qn*60天
---
门(急)诊处方
就诊时间:2025-03-05
就诊科室:内科门诊
主诊
姓名
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2025-02-08
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号:
患者类型:001 支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120瓶
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2025-01-10
就诊科室:内科门诊
主诊
性别:男
年龄:64岁
卡号
患者类型:G
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2024-12-11
就诊科室:内科门诊
主诊
姓名:
性别:男
年龄:64岁
卡号
患者类型:GCP支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/瓶*120瓶
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片◆
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
门(急)诊处方
就诊时间:2024-11-18
就诊科室:内科门诊
主诊
姓名
性别:男
年龄:63岁
卡号:
患者类型:GLP支付
医疗证号:
处方
地址:
身份证号:
诊断:支气管哮喘,非危重
西药处方
组号
项目名称
规格
总量
单价
金额
R:
倍氯米松福莫特罗吸入气雾剂100ug/6ug/揿*120揿
221.61 221.61
Sig
2揿/次,吸入,bid*30天
孟鲁司特钠片
10mg*30/瓶
30片
1.05
31.53
Sig
10mg/次,口服,qn*30天
---
处方笺
普通
诊疗
患者姓
男
年龄：65岁
费别：
科室：
2026-01-06 11:28:26
处方号
地址：
联系电
身份号
诊断：支气管哮喘(急性发作期),过敏性鼻炎[变应性鼻炎],2型糖尿病,急性气管支气管炎
R
P:
倍氯米松福莫特罗吸入气雾剂◆① 100ug/6ug/揿*120
1瓶
剂量：每次2揿 （1/60 瓶）
用法：吸入用药
bid 01-06
孟鲁司特钠片(省采)◆
10mg*5/盒
30片
剂量：每次10mg （1 片）
用法：口服
qd 01-06
处方金额：298.47元
取药药房：门诊西药房（荔湾）
---
处方笺
普通
诊断
患者
年龄：65岁
费别
科室
6-01-06 11:31:02
处方
地址
联系
身份
诊断：支气管哮喘(急性发作期)，过敏性鼻炎[变应性鼻炎]，2型糖尿病，急性气管支气管炎
Rp:
左氧氟沙星片(省采)●⑥
0.5g*28片/盒
3片
剂量：每次0.5g
(1 片)
用法：口服
qd
01-06
醋酸泼尼松片●②⑥
5mg*100/瓶
6片
剂量：每次10mg
(2 片)
用法：口服
qm
01-06
盐酸氨溴索分散片(省采)●⑥
30mg*50/盒
15片
剂量：每次30mg
(1 片)
用法：餐后口服
tid
01-06
处方金额：3.47元
取药药房：门诊西药房（荔湾）
医师手签：
2026-08-10 11:16:02,339 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 11:16:02,339 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "16 items, types={'LabReport': 1, 'OutpatientRecord': 4, 'PrescriptionRecord': 11}", "name": "HXJ 哮喘 广三.pdf", "embedding_token_consumption": 5818}
2026-08-10 11:16:02,339 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 11:16:02,611 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 11:16:02,611 INFO     29 [Trace] task=4e8b5bc4 | doc=HXJ 哮喘 广三.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":16,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 11:16:02,618 INFO     29 [DIAG-EXECUTOR] row_position_int len=32 row[0]=(14, 200, 258, 87, 97) row[-1]=(14, 200, 319, 517, 527)
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,619 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,620 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,620 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,620 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 11:16:02,628 INFO     29 set_progress(4e8b5bc494ab11f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 11:16:02 [DOC Engine]:
Start to index...
2026-08-10 11:16:02,659 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.016s]
2026-08-10 11:16:02,662 INFO     29 set_progress(4e8b5bc494ab11f1bd9827cf206dfa2d), progress: 0.80625, progress_msg: 
2026-08-10 11:16:02,694 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.025s]
2026-08-10 11:16:02,711 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 11:16:02,728 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.009s]
2026-08-10 11:16:02,740 INFO     29 set_progress(4e8b5bc494ab11f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 11:16:02 Indexing done (0.11s). Task done (645.30s)
2026-08-10 11:16:02,744 INFO     29 [Done], chunks(16), token(5818), elapsed:645.30
2026-08-10 11:16:02,937 INFO     29 handle_task done for task {"id": "4e8b5bc494ab11f1bd9827cf206dfa2d", "doc_id": "4e37d76a94ab11f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "type": "pdf", "location": "HXJ \u54ee\u5598 \u5e7f\u4e09.pdf", "size": 8412394, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786359890330, "task_type": "dataflow", "root_trace_id": "088a6eece1684cffa8b7a32ff20ba1b7", "root_traceparent": "00-088a6eece1684cffa8b7a32ff20ba1b7-470d2fa575945e2c-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
