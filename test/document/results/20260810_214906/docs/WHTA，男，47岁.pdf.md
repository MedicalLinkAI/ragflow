# 基准结果：WHTA，男，47岁.pdf

## 基本信息

- 文件：`WHTA，男，47岁.pdf`
- 大小：12795.0 KB
- PDF 总页数：10
- doc_id：`d952dce694c911f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-10T22:43:26  完成时间：2026-08-10T22:47:50  耗时：263.5s
- progress_msg：`14:47:45 Indexing done (0.07s). Task done (234.30s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 3a996436 | 1 | 1-1 | 华阴市人民医院 病理检查报告单 姓名： 性别：男 年龄：39 病理号：2018- |
| 2 | 961e4b5c | 2 | 2-3 | 24小时内入出院记录 姓名 性别：男 年龄：47岁 民族：汉族 出生日期：197 |
| 3 | 53f2f910 | 2 | 3-4 | 第 2 页 姓名 性别 男 年龄 47 岁 住院号 床号 231.2+13 送检 |
| 4 | 9d58a26b | 1 | 5-5 | CT诊断报告单 扫码查看影像报告 诊疗号 影像号 7159990 检查号 162 |
| 5 | 45c5f347 | 1 | 6-6 | 陕西省人民医院 MR诊断报告单 诊疗号 影像号 检查号 扫码查看影像报告 姓名  |
| 6 | 5a40e3a1 | 1 | 10-10 | 项目名称后标注“*”为必填项 诊断结论: 1. 窦性心律 2. 正常范围心电图  |
| 7 | a4ab0f22 | 4 | 0-9 | <table><tr><td>谷丙转氨酶</td><td>ALT</td><td |

- chunks 总数：7
- 各 chunk 页数合计（含跨页重复）：12
- 页码并集：`[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- 覆盖页数：11 / 10；缺失页：`[]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 11/10 页，缺失 []，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 0 | 0 | 0 | encounter_date, chief_complaint, diagnosis | **-** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 5 | 5 | 5 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 1 | 0 | 1 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"ExaminationReport": 5, "DischargeRecord": 1, "LabReport": 1}`
- ChunkMerger：`{"found": true, "merged": 7, "sources": 9, "stats": {"Extractor:LabExam": 1, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 5, "Extractor:Progress": 1}, "filtered_noise": 6}`
- Extractor skip 证据：2 条
  - `[no_text_noise] 2026-08-10 14:44:07,852 INFO     29 [ChunkMerger] Merged 18 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Presc`
  - `[no_text_noise] 2026-08-10 14:47:44,147 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 14:43:37,939 INFO     29 handle_task begin for task {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 14:43:38,165 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.002s]
2026-08-10 14:43:38,285 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 14:43:38,601 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:43:38,601 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 14:43:38,601 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 14:43:38,606 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 14:43:38,607 INFO     29 ============================================================
2026-08-10 14:43:38,607 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 14:43:38,607 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 14:43:38,607 INFO     29 ============================================================
2026-08-10 14:43:38,607 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 14:43:38,607 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 14:43:38,608 INFO     29 No torch found.
2026-08-10 14:43:39,836 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=10
2026-08-10 14:43:40,166 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1752688, prompt_len=764
2026-08-10 14:43:41,125 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:43:41,125 INFO     29 [qwen-vl-text] LLM output (len=568):
{
  "exam_date": null,
  "report_date": "2024-07-09",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "右中间新生物",
  "patient_name": null,
  "patient_gender": "男",
  "department": "特等四病区",
  "bed_number": "17",
  "findings": null,
  "conclusion": "(右中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化。\n免疫组化结果: Ki-67 (90%+), CD56 (-), TTF-1(SPT24) (个别+), CK (+), P40 (-), Syn (-), CgA (-), NapsinA (-), INSM1 (-), Pou2F3 (-), CK8/18 (+), EBER (-)。\nPD-L1(E1L3N, Leica BondMAX染色平台)肿瘤细胞数量:>100个;\n肿瘤细胞比例评分(TPS): <1%+\n阴阳性对照组织:染色正常",
  "physician": "谢晓枫",
  "reviewer": "武春燕"
}
2026-08-10 14:43:41,127 INFO     29 [qwen-vl-text] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=506368, prompt_len=1108
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共22行）
["病 理 诊 断 报 告 单", "病理号: Q2405649", "姓名", "性别: 男", "年龄: 69", "送检材料:", "住院号:", "门诊号: 9", "科别: 特等四病区", "病区: T4", "床号: 17", "(右中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化。", "免疫组化结果: Ki-67 (90%+), CD56 (-), TTF-1(SPT24) (个别+), CK (+), P40 (-), Syn", "(-), CgA (-), NapsinA (-), INSM1 (-), Pou2F3 (-), CK8/18 (+), EBER (-)。", "PD-L1(E1L3N, Leica BondMAX染色平台)肿瘤细胞数量:>100个;", "肿瘤细胞比例评分(TPS): <1%+", "阴阳性对照组织:染色正常", "备注:", "报告医生(签名)谢晓枫", "审核医生(签名)武春燕", "报告日期: 2024-07-09", "本报告仅供临床医生参考,经审核医生签名有效,如发现病理诊断与临床有意外不符,请即与我科联系。"]

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
2026-08-10 14:43:41,789 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2018-01-27"
}
```
2026-08-10 14:43:41,789 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=2018-01-27
2026-08-10 14:43:41,798 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1752688, prompt_len=401
2026-08-10 14:43:45,508 INFO     29 [qwen-vl-parser] text API response (len=516):
["华阴市人民医院", "病理检查报告单", "姓名：", "性别：男", "年龄：39", "病理号：2018-0079", "送检单位：本院", "科别：普外科", "住院号：1800732", "床号：25", "送检日期：2018-01-27", "送检医师：韩晔", "送检材料：食管", "临床诊断：", "肉眼所见：", "送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管", "端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c", "，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，", "V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，", "径0.8cm；另送第五组淋巴结，灰红色两块。", "光镜所见：", "病理诊断：", "食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润", "第五组淋巴结（1/1枚）可见癌转移", "食管周淋巴结（5枚）未见癌组织", "另送上下切缘未见癌组织", "上、下切缘未见癌组织", "纤维脂肪组织内未见癌组织"]
2026-08-10 14:43:45,509 INFO     29 [qwen-vl-parser] page=1 text: 28 lines (bbox 0-27)
2026-08-10 14:43:45,510 INFO     29 [qwen-vl-parser] page=1 text: 28 sections
2026-08-10 14:43:45,760 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1612703, prompt_len=764
2026-08-10 14:43:47,125 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 14:43:47,125 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 14:43:47,140 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1612703, prompt_len=401
2026-08-10 14:43:50,022 INFO     29 [qwen-vl-text] coord API raw response (len=1400):
[
	{"text": "病 理 诊 断 报 告 单", "bbox": [444, 139, 711, 159]},
	{"text": "病理号: Q2405649", "bbox": [722, 167, 850, 179]},
	{"text": "姓名", "bbox": [245, 199, 274, 209]},
	{"text": "性别: 男", "bbox": [383, 199, 445, 209]},
	{"text": "年龄: 69", "bbox": [531, 199, 589, 209]},
	{"text": "送检材料:", "bbox": [642, 199, 706, 209]},
	{"text": "住院号:", "bbox": [245, 223, 300, 233]},
	{"text": "门诊号: 9", "bbox": [383, 223, 457, 233]},
	{"text": "科别: 特等四病区", "bbox": [534, 223, 649, 233]},
	{"text": "病区: T4", "bbox": [693, 223, 749, 233]},
	{"text": "床号: 17", "bbox": [831, 221, 892, 232]},
	{"text": "(右中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化。", "bbox": [247, 246, 630, 257]},
	{"text": "免疫组化结果: Ki-67 (90%+), CD56 (-), TTF-1(SPT24) (个别+), CK (+), P40 (-), Syn", "bbox": [247, 269, 866, 280]},
	{"text": "(-), CgA (-), NapsinA (-), INSM1 (-), Pou2F3 (-), CK8/18 (+), EBER (-)。", "bbox": [252, 280, 821, 291]},
	{"text": "PD-L1(E1L3N, Leica BondMAX染色平台)肿瘤细胞数量:>100个;", "bbox": [247, 292, 658, 303]},
	{"text": "肿瘤细胞比例评分(TPS): <1%+", "bbox": [247, 304, 458, 315]},
	{"text": "阴阳性对照组织:染色正常", "bbox": [247, 316, 421, 327]},
	{"text": "备注:", "bbox": [248, 774, 284, 784]},
	{"text": "报告医生(签名)谢晓枫", "bbox": [247, 803, 438, 818]},
	{"text": "审核医生(签名)武春燕", "bbox": [493, 800, 689, 818]},
	{"text": "报告日期: 2024-07-09", "bbox": [749, 805, 893, 816]},
	{"text": "本报告仅供临床医生参考,经审核医生签名有效,如发现病理诊断与临床有意外不符,请即与我科联系。", "bbox": [247, 824, 850, 835]}
]
2026-08-10 14:43:50,022 INFO     29 [qwen-vl-text] coord API: raw_items=22, valid_items=22, elapsed=8.9s
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[0]: text=病 理 诊 断 报 告 单, bbox=[444, 139, 711, 159]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[1]: text=病理号: Q2405649, bbox=[722, 167, 850, 179]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[2]: text=姓名, bbox=[245, 199, 274, 209]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[3]: text=性别: 男, bbox=[383, 199, 445, 209]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[4]: text=年龄: 69, bbox=[531, 199, 589, 209]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[5]: text=送检材料:, bbox=[642, 199, 706, 209]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[6]: text=住院号:, bbox=[245, 223, 300, 233]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[7]: text=门诊号: 9, bbox=[383, 223, 457, 233]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[8]: text=科别: 特等四病区, bbox=[534, 223, 649, 233]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[9]: text=病区: T4, bbox=[693, 223, 749, 233]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[10]: text=床号: 17, bbox=[831, 221, 892, 232]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[11]: text=(右中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化。, bbox=[247, 246, 630, 257]
2026-08-10 14:43:50,023 INFO     29 [qwen-vl-text] coord item[12]: text=免疫组化结果: Ki-67 (90%+), CD56 (-), TTF-1(SPT24) (个别+), CK (+), P40 (-), Syn, bbox=[247, 269, 866, 280]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[13]: text=(-), CgA (-), NapsinA (-), INSM1 (-), Pou2F3 (-), CK8/18 (+), EBER (-)。, bbox=[252, 280, 821, 291]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[14]: text=PD-L1(E1L3N, Leica BondMAX染色平台)肿瘤细胞数量:>100个;, bbox=[247, 292, 658, 303]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[15]: text=肿瘤细胞比例评分(TPS): <1%+, bbox=[247, 304, 458, 315]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[16]: text=阴阳性对照组织:染色正常, bbox=[247, 316, 421, 327]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[17]: text=备注:, bbox=[248, 774, 284, 784]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[18]: text=报告医生(签名)谢晓枫, bbox=[247, 803, 438, 818]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[19]: text=审核医生(签名)武春燕, bbox=[493, 800, 689, 818]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[20]: text=报告日期: 2024-07-09, bbox=[749, 805, 893, 816]
2026-08-10 14:43:50,024 INFO     29 [qwen-vl-text] coord item[21]: text=本报告仅供临床医生参考,经审核医生签名有效,如发现病理诊断与临床有意外不符,请即与我科联系。, bbox=[247, 824, 850, 835]
2026-08-10 14:43:50,025 INFO     29 [qwen-vl-text] page=22 — 22/22 coords, api_time=8.9s
2026-08-10 14:43:50,025 INFO     29 [qwen-vl-text] new_positions (22):
[[22, 264.18, 423.04499999999996, 117.038, 133.878], [22, 429.59, 505.75, 140.614, 150.718], [22, 145.775, 163.03, 167.558, 175.97799999999998], [22, 227.885, 264.775, 167.558, 175.97799999999998], [22, 315.945, 350.455, 167.558, 175.97799999999998], [22, 381.99, 420.07, 167.558, 175.97799999999998], [22, 145.775, 178.5, 187.766, 196.186], [22, 227.885, 271.91499999999996, 187.766, 196.186], [22, 317.72999999999996, 386.155, 187.766, 196.186], [22, 412.335, 445.655, 187.766, 196.186], [22, 494.445, 530.74, 186.082, 195.344], [22, 146.965, 374.84999999999997, 207.132, 216.394], [22, 146.965, 515.27, 226.498, 235.76], [22, 149.94, 488.495, 235.76, 245.022], [22, 146.965, 391.51, 245.864, 255.126], [22, 146.965, 272.51, 255.968, 265.23], [22, 146.965, 250.49499999999998, 266.072, 275.334], [22, 147.56, 168.98, 651.708, 660.1279999999999], [22, 146.965, 260.61, 676.126, 688.756], [22, 293.335, 409.955, 673.6, 688.756], [22, 445.655, 531.3349999999999, 677.81, 687.072], [22, 146.965, 505.75, 693.808, 703.0699999999999]]
2026-08-10 14:43:50,025 INFO     29 [qwen-vl-text] ═══ DONE ═══ 22 positions, pages=1, time=12.4s
2026-08-10 14:43:50,036 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 14:43:50,037 INFO     29 [Trace] task=a1949cec | doc=SCBA--男71岁，大细胞神经内分泌癌.pdf | Extractor:ExaminationReport | outputs={"chunks": "12 items, types={'ExaminationReport': 12}", "html": "", "json": "3099 items", "markdown": "", "text": "", "name": "SCBA--男71岁，大细胞神经内分泌癌.pdf", "output_format": "chunks", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Progress": "1 items, types={'ProgressNote': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 12, \"chunks_Admission\": 1, \"chunks_LabExam\": 3, \"chunks_Progress\": 1, \"chunks_Discharge\": 1}"}
2026-08-10 14:43:50,037 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 14:43:50,045 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:43:50,046 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:43:50,046 INFO     29 [qwen-vl-text] ═══ START ═══ type=ProgressNote, doc_id=None
2026-08-10 14:43:50,046 INFO     29 [qwen-vl-text] positions(25): [[21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [21, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0], [22, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:43:50,046 INFO     29 [qwen-vl-text] page grouping: [21, 22], lines per page: [23, 2]
2026-08-10 14:43:50,267 INFO     29 [qwen-vl-text] page=21, rect=842x595, img=(2339x1653), dpi=200
2026-08-10 14:43:50,444 INFO     29 [qwen-vl-text] page=22, rect=595x842, img=(1653x2339), dpi=200
2026-08-10 14:43:50,446 INFO     29 [qwen-vl-text] LLM extraction start, text_len=575
2026-08-10 14:43:50,446 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:43:50,446 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"ProgressNote\", \"bbox_start\": 2995, \"bbox_end\": 3019, \"encounter_dates\": [\"2026-03-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "手术记录\n姓名：\n性别：男\n年龄：71岁科别：\n病案号：\n手术开始时间：{2026-03-03 16:00:00}\n手术结束时间：{2026-03-03 16:50:00}\n术前诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管\n继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后\n术中诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管\n继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后\n手术名称：肝动脉化疗栓塞术\n手术指导者：{无}\n手术者：\n助：{-}\n麻醉方法：{局部麻醉}\n手术经过、术中发现的情况及处理：患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞\n巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技\n术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝\n脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤\n供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油\n10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿\n刺部位压迫止血，加压包扎后返回病房休息。\n1/1\nT4",
    "role": "user"
  }
]
2026-08-10 14:43:56,053 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:43:56,053 INFO     29 [qwen-vl-text] LLM output (len=930):
{
  "note_type": "其他",
  "record_time": "2026-03-03 16:50",
  "recorder": null,
  "reviewer": null,
  "reviewer_title": null,
  "cf_summary": null,
  "cf_positive_findings": [],
  "cf_negative_findings": [],
  "dd_diagnosis_basis": null,
  "dd_differential_diagnoses": [],
  "dd_differential_analysis": null,
  "tp_examinations": [],
  "tp_treatments": [],
  "tp_notes": null,
  "condition_changes": null,
  "test_results": null,
  "superior_opinion": null,
  "consultation_opinion": null,
  "measures_and_effects": "患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿刺部位压迫止血，加压包扎后返回病房休息。",
  "order_changes": null,
  "patient_notification": null,
  "rescue_time": null,
  "rescue_measures": null,
  "rescue_participants": []
}
2026-08-10 14:43:56,055 INFO     29 [qwen-vl-text] coord API call start, page=21, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=916018, prompt_len=1250
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["手术记录", "姓名：", "性别：男", "年龄：71岁科别：", "病案号：", "手术开始时间：{2026-03-03 16:00:00}", "手术结束时间：{2026-03-03 16:50:00}", "术前诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管", "继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后", "术中诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管", "继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后", "手术名称：肝动脉化疗栓塞术", "手术指导者：{无}", "手术者：", "助：{-}", "麻醉方法：{局部麻醉}", "手术经过、术中发现的情况及处理：患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞", "巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技", "术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝", "脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤", "供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油", "10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿", "刺部位压迫止血，加压包扎后返回病房休息。"]

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
2026-08-10 14:43:56,426 INFO     29 [qwen-vl-parser] text API response (len=1264):
["24小时内入出院记录", "姓名", "性别：男", "年龄：47岁", "民族：汉族", "出生日期：1978-01-07", "婚姻状况：已婚", "籍贯：", "出生地：", "国籍：", "证件号码：", "工作单位：", "职业：", "详细地址：", "联系电话：", "联系人：", "关系：配偶", "入院日期：2026-01-16 10:19", "病历完成时间：2026-01-16 10:49", "病史陈述者：患者本人", "可靠性：可靠", "是否传染病：否", "既往是否健康：是", "主诉：食管鳞癌术后7年余，肝转移11月余。", "现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。", "入院情况：神志清，精神可，食纳夜休尚可。", "症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。", "症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。", "第1页"]
2026-08-10 14:43:56,426 INFO     29 [qwen-vl-parser] page=2 text: 29 lines (bbox 28-56)
2026-08-10 14:43:56,426 INFO     29 [qwen-vl-parser] page=2 text: 29 sections
2026-08-10 14:43:56,573 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=734924, prompt_len=764
2026-08-10 14:43:57,848 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 14:43:57,848 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 14:43:57,863 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=734924, prompt_len=401
2026-08-10 14:44:01,467 INFO     29 [qwen-vl-parser] text API response (len=554):
["入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐", "酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。", "出院情况：神志清，精神可，食纳夜休尚可。", "出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉", "奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我", "科随诊。", "接诊医师签名：", "住院医师签名：", "主治医师签名：", "主（副主）任医师签名：", "第 2 页"]
2026-08-10 14:44:01,468 INFO     29 [qwen-vl-parser] page=3 text: 17 lines (bbox 57-73)
2026-08-10 14:44:01,468 INFO     29 [qwen-vl-parser] page=3 text: 17 sections
2026-08-10 14:44:01,672 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1266251, prompt_len=764
2026-08-10 14:44:03,128 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-05"}
```
2026-08-10 14:44:03,128 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=2025-12-05
2026-08-10 14:44:03,143 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1266251, prompt_len=401
2026-08-10 14:44:06,939 INFO     29 [qwen-vl-text] coord API raw response (len=1583):
[
	{"text": "手术记录", "bbox": [434, 115, 551, 151]},
	{"text": "姓名：", "bbox": [164, 164, 200, 187]},
	{"text": "性别：男", "bbox": [285, 164, 342, 185]},
	{"text": "年龄：71岁科别：", "bbox": [357, 164, 450, 185]},
	{"text": "病案号：", "bbox": [713, 164, 760, 185]},
	{"text": "手术开始时间：{2026-03-03 16:00:00}", "bbox": [164, 197, 451, 220]},
	{"text": "手术结束时间：{2026-03-03 16:50:00}", "bbox": [164, 238, 458, 261]},
	{"text": "术前诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管", "bbox": [162, 277, 808, 301]},
	{"text": "继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后", "bbox": [279, 319, 638, 342]},
	{"text": "术中诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管", "bbox": [162, 359, 808, 383]},
	{"text": "继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后", "bbox": [279, 399, 638, 422]},
	{"text": "手术名称：肝动脉化疗栓塞术", "bbox": [161, 440, 411, 463]},
	{"text": "手术指导者：{无}", "bbox": [168, 480, 318, 504]},
	{"text": "手术者：", "bbox": [406, 480, 481, 504]},
	{"text": "助：{-}", "bbox": [563, 480, 768, 504]},
	{"text": "麻醉方法：{局部麻醉}", "bbox": [160, 521, 364, 545]},
	{"text": "手术经过、术中发现的情况及处理：患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞", "bbox": [158, 562, 808, 586]},
	{"text": "巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技", "bbox": [158, 603, 808, 627]},
	{"text": "术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝", "bbox": [157, 644, 800, 668]},
	{"text": "脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤", "bbox": [156, 685, 800, 709]},
	{"text": "供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油", "bbox": [156, 725, 785, 749]},
	{"text": "10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿", "bbox": [156, 766, 800, 790]},
	{"text": "刺部位压迫止血，加压包扎后返回病房休息。", "bbox": [154, 807, 472, 831]}
]
2026-08-10 14:44:06,939 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=10.9s
2026-08-10 14:44:06,939 INFO     29 [qwen-vl-text] coord item[0]: text=手术记录, bbox=[434, 115, 551, 151]
2026-08-10 14:44:06,939 INFO     29 [qwen-vl-text] coord item[1]: text=姓名：, bbox=[164, 164, 200, 187]
2026-08-10 14:44:06,939 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[285, 164, 342, 185]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：71岁科别：, bbox=[357, 164, 450, 185]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[4]: text=病案号：, bbox=[713, 164, 760, 185]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[5]: text=手术开始时间：{2026-03-03 16:00:00}, bbox=[164, 197, 451, 220]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[6]: text=手术结束时间：{2026-03-03 16:50:00}, bbox=[164, 238, 458, 261]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[7]: text=术前诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管, bbox=[162, 277, 808, 301]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[8]: text=继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后, bbox=[279, 319, 638, 342]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[9]: text=术中诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管, bbox=[162, 359, 808, 383]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[10]: text=继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后, bbox=[279, 399, 638, 422]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[11]: text=手术名称：肝动脉化疗栓塞术, bbox=[161, 440, 411, 463]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[12]: text=手术指导者：{无}, bbox=[168, 480, 318, 504]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[13]: text=手术者：, bbox=[406, 480, 481, 504]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[14]: text=助：{-}, bbox=[563, 480, 768, 504]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[15]: text=麻醉方法：{局部麻醉}, bbox=[160, 521, 364, 545]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[16]: text=手术经过、术中发现的情况及处理：患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞, bbox=[158, 562, 808, 586]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[17]: text=巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技, bbox=[158, 603, 808, 627]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[18]: text=术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝, bbox=[157, 644, 800, 668]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[19]: text=脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤, bbox=[156, 685, 800, 709]
2026-08-10 14:44:06,940 INFO     29 [qwen-vl-text] coord item[20]: text=供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油, bbox=[156, 725, 785, 749]
2026-08-10 14:44:06,941 INFO     29 [qwen-vl-text] coord item[21]: text=10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿, bbox=[156, 766, 800, 790]
2026-08-10 14:44:06,941 INFO     29 [qwen-vl-text] coord item[22]: text=刺部位压迫止血，加压包扎后返回病房休息。, bbox=[154, 807, 472, 831]
2026-08-10 14:44:06,942 INFO     29 [qwen-vl-text] page=21 — 23/23 coords, api_time=10.9s
2026-08-10 14:44:06,943 INFO     29 [qwen-vl-text] coord API call start, page=22, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=506368, prompt_len=624
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共2行）
["1/1", "T4"]

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
2026-08-10 14:44:07,819 INFO     29 [qwen-vl-text] coord API raw response (len=108):
```json
[
	{"text": "1/1", "bbox": [95, 107, 156, 135]},
	{"text": "T4", "bbox": [243, 120, 274, 138]}
]
```
2026-08-10 14:44:07,819 INFO     29 [qwen-vl-text] coord API: raw_items=2, valid_items=2, elapsed=0.9s
2026-08-10 14:44:07,819 INFO     29 [qwen-vl-text] coord item[0]: text=1/1, bbox=[95, 107, 156, 135]
2026-08-10 14:44:07,819 INFO     29 [qwen-vl-text] coord item[1]: text=T4, bbox=[243, 120, 274, 138]
2026-08-10 14:44:07,819 INFO     29 [qwen-vl-text] page=22 — 2/2 coords, api_time=0.9s
2026-08-10 14:44:07,820 INFO     29 [qwen-vl-text] new_positions (25):
[[21, 365.428, 463.942, 68.425, 89.845], [21, 138.088, 168.4, 97.58, 111.265], [21, 239.97, 287.964, 97.58, 110.07499999999999], [21, 300.594, 378.9, 97.58, 110.07499999999999], [21, 600.346, 639.92, 97.58, 110.07499999999999], [21, 138.088, 379.74199999999996, 117.21499999999999, 130.9], [21, 138.088, 385.63599999999997, 141.60999999999999, 155.295], [21, 136.404, 680.336, 164.815, 179.095], [21, 234.91799999999998, 537.196, 189.80499999999998, 203.48999999999998], [21, 136.404, 680.336, 213.605, 227.885], [21, 234.91799999999998, 537.196, 237.405, 251.08999999999997], [21, 135.56199999999998, 346.062, 261.8, 275.485], [21, 141.456, 267.756, 285.59999999999997, 299.88], [21, 341.852, 405.002, 285.59999999999997, 299.88], [21, 474.046, 646.656, 285.59999999999997, 299.88], [21, 134.72, 306.488, 309.995, 324.275], [21, 133.036, 680.336, 334.39, 348.66999999999996], [21, 133.036, 680.336, 358.78499999999997, 373.065], [21, 132.194, 673.6, 383.18, 397.46], [21, 131.352, 673.6, 407.575, 421.85499999999996], [21, 131.352, 660.97, 431.375, 445.655], [21, 131.352, 673.6, 455.77, 470.04999999999995], [21, 129.668, 397.424, 480.16499999999996, 494.445], [22, 56.525, 92.82, 90.094, 113.67], [22, 144.58499999999998, 163.03, 101.03999999999999, 116.196]]
2026-08-10 14:44:07,820 INFO     29 [qwen-vl-text] ═══ DONE ═══ 25 positions, pages=2, time=17.8s
2026-08-10 14:44:07,842 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 14:44:07,843 INFO     29 [Trace] task=a1949cec | doc=SCBA--男71岁，大细胞神经内分泌癌.pdf | Extractor:Progress | outputs={"chunks": "1 items, types={'ProgressNote': 1}", "html": "", "json": "3099 items", "markdown": "", "text": "", "name": "SCBA--男71岁，大细胞神经内分泌癌.pdf", "output_format": "chunks", "chunks_Examination": "12 items, types={'ExaminationReport': 12}", "chunks_Admission": "1 items, types={'AdmissionRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "chunks_Progress": "1 items, types={'ProgressNote': 1}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "route_summary": "{\"chunks_Examination\": 12, \"chunks_Admission\": 1, \"chunks_LabExam\": 3, \"chunks_Progress\": 1, \"chunks_Discharge\": 1}"}
2026-08-10 14:44:07,844 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 14:44:07,852 INFO     29 [ChunkMerger] Merged 18 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 12, 'Extractor:Progress': 1} (filtered 4 noise chunks)
2026-08-10 14:44:08,117 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 14:44:08,118 INFO     29 [Trace] task=a1949cec | doc=SCBA--男71岁，大细胞神经内分泌癌.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 3, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 12, 'ProgressNote': 1}", "name": "SCBA--男71岁，大细胞神经内分泌癌.pdf"}
2026-08-10 14:44:08,118 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 14:44:08,511 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786373018159, 'update_date': datetime.datetime(2026, 8, 10, 14, 43, 38), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1088085, 'status': '1'}
2026-08-10 14:44:08,751 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   凝血酶原时间  None  13.6  秒  11.0～14.5  False    PT活动度  None  92.0  %  70.0～130.0  False    国际标准化比值  None  1.050  None  0.800～1.200  False    活化部分凝血活酶时间  None  37.6  秒  28.0～43.5  False    血浆纤维蛋白原  None  4.340  g/L  2.000～4.000  True    凝血酶时间  None  16.8  秒  14.0～21.0  False    血浆D-二聚体  None  0.33  mg/L  ≤0.50  False    纤维蛋白原降解产物  None  2.88  μg/mL  ≤5.00  False   
---
   丙氨酸氨基转移酶  None  5  U/L  None  True    天门冬氨酸氨基转移  None  14  U/L  None  True    门丙比值  None  2.80  None  None  False    γ-谷氨酰基转移酶  None  14  U/L  None  False    总蛋白  None  63.5  g/L  None  True    白蛋白  None  36.9  g/L  None  True    球蛋白  None  26.6  g/L  None  False    白球比  None  1.4  None  None  False    总胆红素  None  13.90  μmol/L  None  False    直接胆红素  None  4.37  μmol/L  None  False    间接胆红素  None  9.53  μmol/L  None  False    碱性磷酸酶  None  60  U/L  None  False    尿素  None  5.94  mmol/L  None  False    肌酐  None  68.0  μmol/L  None  False    尿酸  None  242  μmol/L  None  False    β2-微球蛋白  None  1.98  mg/L  None  False    视黄醇结合蛋白  None  34.88  mg/L  None  False    肾小球滤过率  None  91.34  ml/min  None  False    葡萄糖  None  4.91  mmol/L  None  False    肌酸激酶  None  58  U/L  None  False    肌酸激酶-MB同工酶  None  16  U/L  None  False    乳酸脱氢酶  None  162  U/L  None  False    α-羟基丁酸脱氢酶  None  130  U/L  None  False   
---
   白细胞总数  None  4.91  10^9/L  3.50~9.50  False    红细胞计数  None  4.06  10^12/L  4.30~5.80  True    血红蛋白  None  124  g/L  130~175  True    血细胞比容  None  37.6  %  40.0~50.0  True    平均红细胞体积  None  92.4  fL  82.0~100.0  False    平均红细胞血红蛋白含量  None  30.6  pg  27.0~34.0  False    平均红细胞血红蛋白浓度  None  331  g/L  316~354  False    血小板总数  None  191  10^9/L  125~350  False    中性粒细胞%  None  72.1  %  50.0~70.0  True    淋巴细胞%  None  16.6  %  20.0~40.0  True    单核细胞%  None  7.4  %  3.0~10.0  False    嗜酸性粒细胞%  None  3.3  %  0.5~5.0  False    嗜碱性粒细胞%  None  0.6  %  0.0~1.0  False    中性粒细胞绝对数  None  3.53  10^9/L  2.00~7.00  False    淋巴细胞绝对数  None  0.82  10^9/L  0.80~4.00  False    单核细胞绝对数  None  0.37  10^9/L  0.12~1.00  False    嗜酸性粒细胞绝对数  None  0.16  10^9/L  0.02~0.50  False    嗜碱性粒细胞绝对数  None  0.03  10^9/L  0.00~1.00  False   
---
出院记录
姓名：
科室：
病案号
姓名：
入院日期：2026-02-24
性别：男
出院日期：2026-03-05
年龄：71岁
住院天数：9
入院情况：患者因“诊为右肺大细胞神经内分泌癌1年余，免疫治疗后3周余。”入院。体格
检查：全身皮肤黏膜无黄染，全身浅表淋巴结无肿大。胸廓无畸形，胸骨无叩痛。呼吸运动正
常，肋间隙正常，语颤无增强、减弱。双肺叩诊清音，呼吸规整。双肺呼吸音粗，可闻及痰鸣
音，无胸膜摩擦音。心律齐，各瓣膜听诊区未闻及杂音，无心包摩擦音。腹平坦，无压痛、反跳
痛，腹部无包块，无移动性浊音，肠鸣音正常。四肢活动自如，双下肢无水肿，四肢肌力、肌张
力未见异常。辅助检查：本院 2025-11-01胸部+上腹部CT增强：1.结合病史，符合右肺Ca并阻塞
性炎症治疗后所见；2.双肺索条影；3.双侧肾上腺增粗，建议随诊观察；4.肝右叶低密度灶，考
虑转移瘤，建议MR增强扫描；5.肝内小囊肿；6.T7椎体压缩性骨折并椎管狭窄。2025-11-01 磁共
振颅脑增强：1.脑白质高信号，FazekasⅠ级；考虑右侧脑室周围急性/亚急性脑死可能，请结合
临床；2.符合双侧脉络丛黄色肉芽肿MRI表现。
入院诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期
纵隔淋巴结继发恶性肿瘤
当前第：1/2页
243%
入院诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期
纵隔淋巴结继发恶性肿瘤
气管继发恶性肿瘤
肺不张
气管狭窄
脊柱骨水泥术后
诊疗经过：患者入院后完善相关辅助检查，2026-02-25 磁共振增强 颅脑：1、脑白质多发
异常高信号（Fazekas 1），符合脑小血管病MRI表现；2、鼻窦炎。2026-02-27 胸部+上腹部CT增
强：1.结合病史，符合右肺Ca并阻塞性炎症治疗后所见；2.支气管炎，肺气肿；双肺索条影；3.
双肺多发结节，考虑转移瘤可能性大；4.冠状动脉钙化；心包少量积液；5.双侧肾上腺增粗，建
议随诊观察；6.肝右叶多发低密度灶，考虑转移瘤，建议MR增强扫描；7.肝内小囊肿；8.T7椎体
压缩性骨折并椎管狭窄；左侧第2肋骨皮质略欠规整。评估患者病情，排除禁忌后于2026-02-28行
贝莫苏拜单抗1200mg免疫治疗1周期，2026-03-01起开始口服盐酸安罗替尼（一次8mg，一日1次）
抗血管生成治疗，2026-03-03行肝动脉化疗栓塞，过程顺利，患者未诉特殊不适。今日查房，患
者及家属要求出院口服安罗替尼，请示上级医师，交代相关注意事项后，今日予以办理出院。
出院诊断：恶性肿瘤介入治疗
恶性肿瘤免疫治疗
当前第：1/2页 243%
脊柱骨水泥术后
出院情况：患者无明显胸闷、憋喘，偶有咳嗽、咳痰，无胸痛，无发热，饮食睡眠尚可，大
小便无明显异常。
出院医嘱：1.注意休息，加强营养，避免受凉；
2.出院后遵医嘱用药
盐酸安罗替尼 一次8mg 一日1次（服药2周，停药1周）
利可君片 一次1片 一日3次
盐酸昂丹司琼片 一次2片 一日2次（连服5天）
3.出院后第3、7天复查血常规、肝功、电解质等相关辅助检查，如有异常，及时对症处理。
4.2026-03-23来院继续治疗，我科随诊。
医师签名：
当前第：2/2页
---
入院记录
病案号:
第6次入院记录
姓名:
出生:
性别: {男}
职业: {农民}
年龄: {71岁}
入院时间: {2026-02-24 15:19}
民族: {汉族}
记录时间: {2026-02-24 16:08}
婚姻: {已婚}
病史陈述者: {患者本人及家属}
主诉: 诊为右肺大细胞神经内分泌癌1年余,免疫治疗后[3]{周}余。
现病史: 患者2024-04因“痰中带血”就诊于威海市立医院,胸部CT示右肺占位。
2024-04-26行PET-CT示:右肺下叶结节,1.5cm,MT可能,余未见转移征象。后行电子支气
管镜检查,活检病理示:小细胞癌,未行特殊治疗,以对症治疗为主。后患者就诊于上海市
肺科医院,2024-06-11查胸部CT示:右肺病灶较前增大,2.9cm,伴肺不张,右侧少量胸腔
积液,纵隔淋巴结增大。于2024-06-25行气管镜下腔内治疗,同时送检病理,病理示:(右
中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化,免疫组化结果,Ki-67(90%+),
CD56(-),TTF-1(SPT24)(个别+),CK(+),P40(-),Syn(-),CgA(-),NapsinA(-),INSM1(-),
Pou2F3(-),CK8/18(+),EBER(-),TPS评分<1%。排除禁忌后于2024-07-12起行依托泊苷0.18g
d1-3+卡铂600mg d1静脉化疗3周期,后行胸部病灶放疗,共放疗30f,具体剂量不详。
2025-07-01行全麻气管镜下腔内治疗,镜下右肺下叶见新生物,完全堵塞管腔右下叶开口,
予以镜下切除新生物,管腔较前通畅,予以对症治疗后出院。2025-08-03患者第1次就诊于
我院,入院后完善相关辅助检查,2025-08-04胸部+上腹部增强CT:1.结合病史,符合右肺
Ca并右肺多发肺不张CT表现;2.双侧肾上腺结节灶,转移可疑,建议随诊观察;3.双肺炎性
索条灶;4.肝右前叶低密度灶,建议短期随诊观察,必要时MR检查;5.肝内低密度灶,考虑
Ca并右肺多发肺不张CT表现；2.双侧肾上腺结节灶，转移可疑，建议随诊观察；3.双肺炎性
索条灶；4.肝右前叶低密度灶，建议短期随诊观察，必要时MR检查；5.肝内低密度灶，考虑
囊肿；6.符合T7、L1椎体压缩骨折CT表现。排除禁忌后于2025-08-05行电子支气管镜检查，
镜下行气管肿物切除，术后患者胸闷、憋喘较前好转。2025-08-06行支气管动脉化疗栓塞，
灌注化疗药物为洛铂40mg，2025-08-07行贝莫苏拜单抗1200mg免疫治疗1周期，同日开始口
服盐酸安罗替尼（一次8mg，一日1次，服药2周，停药1周）抗血管生成治疗，后出院口服安
罗替尼。2025-08-25患者第2次入院，入院后完善相关辅助检查，评估患者病情，排除禁忌
后于2025-08-27行支气管动脉化疗栓塞，灌注化疗药物为洛铂50mg，2025-08-28行贝莫苏拜
第1页
入院记录
姓名：
科室：
病案号：
单抗1200mg免疫治疗1周期，2025-08-29开始口服盐酸安罗替尼（一次8mg，一日1次，服药2
周，停药1周）抗血管生成治疗，后出院口服安罗替尼靶向治疗。2025-09-15患者第3次入
院，入院后完善相关辅助检查，与既往检查结果对比，疗效评估PR，排除禁忌后于
2025-09-17行支气管动脉灌注化疗，灌注化疗药物为洛铂50mg，2025-09-18行贝莫苏拜单抗
1200mg免疫治疗1周期，2025-09-19开始口服盐酸安罗替尼（一次8mg，一日1次，服药2周，
停药1周）抗血管生成治疗，后出院口服安罗替尼。2025-09-22复查血常规示血小板总数
入院记录
姓名：
科：
病案号：
单抗1200mg免疫治疗1周期，2025-08-29开始口服盐酸安罗替尼（一次8mg，一日1次，服药2
周，停药1周）抗血管生成治疗，后出院口服安罗替尼靶向治疗。2025-09-15患者第3次入
院，入院后完善相关辅助检查，与既往检查结果对比，疗效评估PR，排除禁忌后于
2025-09-17行支气管动脉灌注化疗，灌注化疗药物为洛铂50mg，2025-09-18行贝莫苏拜单抗
1200mg免疫治疗1周期，2025-09-19开始口服盐酸安罗替尼（一次8mg，一日1次，服药2周，
停药1周）抗血管生成治疗，后出院口服安罗替尼。2025-09-22复查血常规示血小板总数
75×10^9/L，后予以升血小板药物应用，后复查血小板计数恢复正常。2025-10-09患者再次
入院，完善相关辅助检查，于2025-10-10行支气管动脉灌注化疗，灌注化疗药物为洛铂
50mg，2025-10-11行贝莫苏拜单抗1200mg免疫治疗1周期，2025-10-11开始口服盐酸安罗替
尼（一次8mg，一日1次，服药2周，停药1周）抗血管生成治疗，治疗结束后出院口服安罗替
尼。2025-10-30患者第5次入院，入院后完善相关辅助检查，排除禁忌后于2025-11-01行贝
莫苏拜单抗1200mg免疫治疗1周期，2025-11-01开始口服盐酸安罗替尼（一次8mg，一
日1次，服药2周，停药1周）抗血管生成治疗，后出院口服安罗替尼。后于当地医院行4周期
贝莫苏拜单抗联合安罗替尼抗肿瘤治疗，末次治疗时间为2026-02-02。现患者为求进一步诊
疗来院，门诊以“肺恶性肿瘤”收入院。自上次出院后，患者无明显咳嗽、咳痰、胸闷、胸
痛等不适，饮食睡眠尚可，大小便无明显异常，近期体重无明显变化。
既往史：否认高血压、糖尿病、冠心病病史，否认肝炎、结核、疟疾病史，2024年行
骨水泥手术，否认其他手术史，否认输血、使用血制品史，否认食物、药物过敏史，预防接
种史不详。
个人史：生于山东省威海市环翠区，否认疫区、疫情、疫水接触史，否认牧区、矿
山、高氟区、低碘区居住史，否认化学性物质、粉尘、放射性物质、有毒物质接触史，否认
75×10^9/L，后予以升血小板药物应用，后复查血小板计数恢复正常。2025-10-09患者再次
入院，完善相关辅助检查，于2025-10-10行支气管动脉灌注化疗，灌注化疗药物为洛铂
50mg，2025-10-11行贝莫苏拜单抗1200mg免疫治疗1周期，2025-10-11开始口服盐酸安罗替
尼（一次8mg，一日1次，服药2周，停药1周）抗血管生成治疗，治疗结束后出院口服安罗替
尼。2025-10-30患者第5次入院，入院后完善相关辅助检查，排除禁忌后于2025-11-01行贝
莫苏拜单抗1200mg免疫治疗1周期，2025-11-01开始口服盐酸安罗替尼（一次8mg，一
日1次，服药2周，停药1周）抗血管生成治疗，后出院口服安罗替尼。后于当地医院行4周期
贝莫苏拜单抗联合安罗替尼抗肿瘤治疗，末次治疗时间为2026-02-02。现患者为求进一步诊
疗来院，门诊以“肺恶性肿瘤”收入院。自上次出院后，患者无明显咳嗽、咳痰、胸闷、胸
痛等不适，饮食睡眠尚可，大小便无明显异常，近期体重无明显变化。
既往史：否认高血压、糖尿病、冠心病病史，否认肝炎、结核、疟疾病史，2024年行
骨水泥手术，否认其他手术史，否认输血、使用血制品史，否认食物、药物过敏史，预防接
种史不详。
个人史：生于山东省威海市环翠区，否认疫区、疫情、疫水接触史，否认牧区、矿
山、高氟区、低碘区居住史，否认化学性物质、粉尘、放射性物质、有毒物质接触史，否认
吸毒史，否认治游史；嗜烟：有，约50年，平均40支/日，已戒烟，约1年；嗜酒：经常，约
50年，平均5两/日，已戒酒，约1年。其他：无。
婚姻史：已婚，适龄结婚，配偶身体健康。育1子，家庭关系和睦。
家族史：否认家族性遗传病、精神病或类似的病史。
情况属实：
体格检查
第2页
入院记录
姓名：
科室：
病案号：
T{36.7}℃ P{78}次/分 R{18}次/分 Bp110/81[mmHg] 身高{162}CM 体重{68.5}KG VTE结果{
高危}。
一般情况：发育{正常}，营养{良好}，{正常面容}，表情{自如}，{自主体位}，神志
{清楚}，查体{合作}。皮肤黏膜：全身{皮肤黏膜无黄染}，{无皮疹、皮下出血、皮下结
节、瘢痕}，皮下{无水肿}，{无肝掌、蜘蛛痣}。浅表淋巴结：{全身浅表淋巴结无肿大}。
头颅五官：{无眼睑水肿}，结膜{无苍白}，{眼球无突出}，巩膜{无黄染}，瞳孔{等大等
圆}。对光反射{灵敏}，外耳道{无异常分泌物}，{乳突无压痛}，{无听力粗试障碍}。嗅觉{
正常}。口唇{无发绀}，口腔黏膜{正常}。舌苔{正常}，伸舌{无偏斜、震颤}，牙龈{无红
肿}，咽部黏膜{正常}，扁桃体{无肿大}。颈部：颈{软}{无抵抗}，颈动脉{搏动正常}，颈
静脉{未见充盈}，气管{正中}，肝颈静脉回流征{阴性}，甲状腺{未及肿大}，{无压痛、震
颤、血管杂音}。胸部：{胸廓无畸形}，{胸骨无叩痛}。呼吸运动{正常}，肋间隙{正常}，
语颤{无增强、减弱}。{双肺}叩诊{清音}，呼吸{规整}。肺部：双肺{呼吸音粗}，{可闻
及}痰鸣音，{无胸膜摩擦音}。心脏：心率{78}次/分，律{齐}，{各瓣膜听诊区未闻及杂
音}，{无心包摩擦音}。血管：桡动脉脉律规整。无毛细血管搏动征，无股动脉枪击音。腹
部：腹{平坦}，{无压痛、反跳痛}，腹部{无包块}。肝脏{未触及}，脾脏{未触及}，Murphy
氏征{阴性}，肾区{无叩击痛}，{无移动性浊音}。肠鸣音{正常}。肛门生殖器：肛门及外
生殖器{未查}。脊柱四肢：脊柱{正常生理弯曲}，四肢{活动自如}，{无畸形、下肢静脉曲
张、杵状指（趾）}，关节{无红肿}，{双}下肢{无水肿}。神经系统：四肢肌力、肌张力未
见异常，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，{双侧}Babinski征{阴
性}。
辅助检查
张、杵状指（趾）}，关节{无红肿}，{双}下肢{无水肿}。神经系统：四肢肌力、肌张力未
见异常，双侧肱二、三头肌腱反射正常，双侧膝、跟腱反射正常，{双侧}Babinski征{阴
性}。
辅助检查
本院 2025-11-01胸部+上腹部CT增强：1.结合病史，符合右肺Ca并阻塞性炎症治疗后
所见；2.双肺索条影；3.双侧肾上腺增粗，建议随诊观察；4.肝右叶低密度灶，考虑转移
瘤，建议MR增强扫描；5.肝内小囊肿；6.T7椎体压缩性骨折并椎管狭窄。2025-11-01 磁共
振颅脑增强：1.脑白质高信号，FazekasⅠ级；考虑右侧脑室周围急性/亚急性脑死可能，请
结合临床；2.符合双侧脉络丛黄色肉芽肿MRI表现。
刷新诊断
初步诊断：1.右肺下叶神经内分泌癌（cT4N2M
第3页
入院记录
姓名：孙初保
科室：肿瘤综合五科（介入微创）
病案号：698391
0）IIIB期
纵隔淋巴结继发恶性肿瘤
气管继发恶性肿瘤
2.肺不张
---
肺癌49基因+PDL1表达
· 患者信息
个人信息
姓名：
临床诊断： 右肺下叶大细胞神经内分泌癌
性别： 男
分型： 腺癌
年龄： 70
分期： 未知
身份证号：
样本信息
样本编号： -1
接收日期： 2025-08-12
样本类型： 组织
报告日期： 2025-08-21
病理编号：
· 检测项目简介
检测项目临床意义
检测项目
检测内容
检测意义
分子靶向治疗药物相关基因
包含EGFR、ALK、ROS1、RET、MET、NTRK、MMR等49个靶向免疫治疗相关基因，包括基因突变、缺失、扩增以及融合，涵盖目前已经获批的以及尚处于临床试验阶段的药物。
预测靶向药物有效性肿瘤分子分型临床预后判断
免疫治疗相关基因
微卫星不稳定性（限组织样本）、DNA错配修复通路(MMR)等免疫治疗相关基因及PD-L1表达检测（限组织样本）。
评估免疫治疗获益的可能性
检测方法
高通量测序（NGS）
本报告信息供临床医生参考，非临床诊断依据。癌症治疗方案需综合考虑其他临床信息，详情请遵循医嘱。
- 1 -
· 质控信息
样本主要质控
检测项目
质控指标
检测结果
质量标准
组织
血液
病理评估
恶性肿瘤细胞占比(%)
A
A-B-C
DNA总量(ng)
732
≥10
≥10
扫描全能王 创建
肿瘤个体化检测结果概览
检测项目
检测内容
检测结果
药物指导
靶向
靶向/耐药相关变异
APC,16外显子,p.L1087fs,突变丰
度:53.41%
敏感相关药物:
索凡替尼(A);依维莫司(A)
TP53,7外显子,p.H233fs,突变丰
度:13.68%
耐药相关药物:
无推荐
临床试验药物:
REC-4881;Atorvastatin;APG-115
+帕博利珠单抗;
免疫
肿瘤微卫星不稳定性
(MSI)
微卫星稳定型(MSS)
错配修复(MMR)基因
未见致病变异
免疫检查点抑制剂(PD1/PDL1等单抗)
(C)
免疫组化PD-L1表达
(IHC)
阳性(TPS:1%,CPS:5)
本报告信息供临床医生参考,非临床诊断依据。癌症治疗方案需综合考虑其他临床信息,详情请遵循医嘱。
-3-
扫描全能王 创建
---
常规病理诊断报告单
病理号
姓名:
性别:男
年龄:70岁
门诊号:
住院号
床号:1202D
送检医院:本院
送检日期:2025-08-05
送检医师:徐铠臻
送检科室
送检标本:右肺下叶TBB
临床诊断:1.右肺下叶大细胞神经内分泌癌纵隔淋巴结继发恶性肿瘤
肉眼所见:
(右肺下叶TBB):灰白组织一堆,体积2*1.5*.3cm,质软,取全。
镜下所见:
病理诊断:
(右肺下叶TBB)查见恶性肿瘤细胞,伴坏死,瘤细胞分化差,结合病史及免疫组
化,符合低分化癌伴神经内分泌分化,请结合临床。
免疫组化结果:
蜡块号:25-7788:CK(+),SSTR2(+),TTF-1(-),Syn(-),CgA(-),CD56(-
),INSM1(-),NapsinA(-),CK5/6(个别细胞+),P40(-),Brg-1(+，未缺
失),INI-1(+，未缺失),CK7(个别细胞+),CD117(-),NUT(-),Ki67(阳性
率约90%)。
初诊医师:杜中洪 复诊医师:
审核医师:
报告日期:2025-08-08
此报告,仅供临床参考!如有不符请及时与病理科联系
---
CT诊断报告单
影像号:PCT20260226119
姓名:..
性别:男
住院号:
申请科室:
检查类别:CT
年龄:71岁
病床号:1205D
检查项目:CT增强,CT增强
检查方法:CT增强上腹部,CT增强胸部
病区:
影像所见:
右肺中下叶、右肺中间段支气管管壁增厚,管腔变窄,增强扫描可见强化,较前2025-10-
31CT整体变化不大。右肺上叶前段、中下叶见多发条片、斑片、索条、结节样高密度影,密度不
均,下叶部分病变较密实,内见不规则支气管,增强扫描可见不均质强化,右肺中下叶部分病灶
范围较前略减小,余部分结节病灶新发,部分结节病灶吸收消失,较大结节病灶位于右肺上叶前
段(IM117),大小约6mm×5mm,可见胸膜凹陷征象;左肺另见多发结节影,较前变化不著。双肺
纹理增多、紊乱,肺野内见多发类圆形无肺纹理透光区。左肺见多发索条影。右侧胸膜增厚,胸
膜腔内见少量积液,较前范围略显减小。气管及支气管通畅。纵隔略右移,纵隔及右肺门见多发
小淋巴结显示,7区淋巴结可见斑点状钙化灶,增强扫描可见较均匀强化,较前略小。左右冠状动
脉见多发钙化灶,心包略厚。
肝脏边缘欠规整,肝实质密度不均匀,肝右叶下段胆囊旁见结节状稍低密度灶,边界欠清,
增强扫描轻度强化,较大截面约32mm×24mm,较前略增大;肝右叶近肝顶处,新发一低密度结节
影,直径为13mm,增强扫描呈环形强化。肝内另见多发结节样低密度灶,增强扫描未见明显强
化。肝内外胆管无明显扩张。胆囊不大,壁不厚,腔内未见明显异常密度影。脾脏、胰腺大小、
形态及密度未见明显异常。扫描野内,双侧肾上腺不均匀性增粗,左侧稍著,增强扫描强化不均
匀,较前变化不大。T7椎体明显变扁,骨质不连续,椎体后缘局部后突,相应节段椎管狭窄。左
侧第2肋骨皮质略欠规整。
影像诊断:
1.结合病史,符合右肺Ca并阻塞性炎症治疗后所见:
2.支气管炎,肺气肿;双肺索条影:
3.双肺多发结节,考虑转移瘤可能性大;
4.冠状动脉钙化;心包少量积液;
5.双侧肾上腺增粗,建议随诊观察;
6.肝右叶多发低密度灶,考虑转移瘤,建议MR增强扫描:
7.肝内小囊肿;
8.T7椎体压缩性骨折并椎管狭窄;左侧第2肋骨皮质略欠规整。
报告医师:李洪东
审核医师:
审核日期:2026-02-27
检查日期:2026-02-26
技术支持:青岛美迪康数字工程有限公司
---
影像号:PCT20251031075
姓名:
性别:男
住院号:
申请科室: 门
微创)
检查类别:CT
年龄:71岁
病床号:1205D
检查项目:CT增强,CT增强
岁
检查方法:CT增强 胸部,CT增强 上腹部
病区:
影像所见:
右肺中下叶、右肺中间段支气管管壁增厚,管腔变窄,增强扫描可见强化,较前2025-09-16
整体变化不大。右肺上叶前段、中下叶见多发条片、斑片、索条状高密度影,密度不均,下叶部
分病变较密实,内见不规则支气管,增强扫描可见不均质强化,右肺中下叶部分病灶范围较前略
减小。左肺见多发索条影。右侧胸膜增厚,胸膜腔内见少量积液,较前范围略显减小。气管及支
气管及支
气管通畅。纵隔略右移,纵隔及右肺门见多发小淋巴结显示,7区淋巴结可见斑点状钙化灶,增强
扫描可见较均匀强化。左右冠状动脉见多发钙化灶,心包略厚。
肝脏边缘欠规整,肝实质密度不均匀,肝右叶下段胆囊旁见结节状稍低密度灶,边界欠清,
增强扫描轻度强化,较大截面约25mm×24mm,较前略增大。肝内另见多发结节样低密度灶,增强
扫描未见明显强化。肝内外胆管无明显扩张。胆囊不大,壁不厚,腔内未见明显异常密度影。脾
脏、胰腺大小、形态及密度未见明显异常。扫描野内,双侧肾上腺不均匀性增粗,左侧稍著,增
强扫描强化不均匀,较前变化不大。T7椎体明显变扁,骨质不连续, 椎体后缘局部后突,相应节
段椎管狭窄。
影像诊断:
1.结合病史,符合右肺Ca并阻塞性炎症治疗后所见;
2.双肺索条影;
3.双侧肾上腺增粗,建议随诊观察;
4.肝右叶低密度灶,考虑转移瘤,建议MR增强扫描;
5.肝内小囊肿;
6.T7椎体压缩性骨折并椎管狭窄。
报告医师: 张金亮
审核医师: 俞春林
检查日期: 2025-11-01
2025-11-01
青岛美迪康数字工程有限公司
扫描全能王 创建
---
影像号:PCT20250916055
姓  名
性别:男
住院号.
请科
检查类别:CT
年龄:70岁
临床号
检查项目:CT增强,CT增强
检查方法:CT增强胸部,CT增强上腹部
病区:
影像所见:
右肺中下叶、右肺中间段支气管管壁增厚,管腔变窄,增强扫描可见强化,较前2025-08-04
管腔变窄范围减小。右肺上叶前段、中下叶见多发条片、斑片、索条状高密度影,密度不均,下
叶部分病变较密实,内见不规则支气管,增强扫描可见不均质强化。左肺见多发索条影。右侧胸
膜增厚,胸膜腔内见少量积液,较前范围减小。气管及支气管通畅。纵隔略右移,纵隔及右肺门
见多发小淋巴结显示,7区淋巴结可见斑点状钙化灶,增强扫描可见较均匀强化。左右冠状动脉见
多发钙化灶,心包略厚。
肝脏边缘欠规整,肝实质密度不均匀,肝右后叶下段胆囊旁见结节状稍低密度灶,边界欠清,
增强扫描轻度强化,强化程度较前片减轻,大小较前略缩小。肝内另见多发结节样低密度灶,增
强扫描未见明显强化。肝内外胆管无明显扩张。胆囊不大,壁略厚,腔内未见明显异常密度影。
脾脏、胰腺大小、形态及密度未见明显异常。双侧肾上腺不均匀性增粗,左侧为著,增强扫描强
化不均匀,较前变化不大。T7椎体明显变扁,骨质不连续,椎体后缘局部后突,相应节段椎管狭
窄。
影像诊断:
1.结合病史,符合右肺Ca并阻塞性炎症治疗后所见;
2.双肺索条影;
3.双侧肾上腺增粗,建议随诊观察;
4.肝右叶低密度灶,考虑转移瘤,建议MR增强扫描随诊;
5.肝内小囊肿;
6.T7椎体压缩性骨折并椎管狭窄。
报告医师:
李鹏
审核医师:
表小记
扫描全能王 创建
---
CT诊断报告单
影像号:PCT20250804014
姓名:
性别:男
住院号:
申请科室:
检查类别:CT
年龄:70岁
病床号:
检查项目:CT增强,CT增强
岁
检查方法:CT增强上腹部,CT增强胸部
病区:
影像所见:
右侧胸廓塌陷,纵隔右移。右肺中下叶、右肺中间段支气管管壁增厚,管腔变窄,增强扫描可见
轻度强化。右肺上叶前段、中下叶肺组织膨胀不全,呈实性改变,其内可见支气管气相,增强扫
描可见较高强化。双肺内另见多发索条状高密度灶。右侧胸膜腔见大量积液。气管及支气管通
畅。纵隔及右肺门见多发小淋巴结显示,7区淋巴结可见斑点状钙化灶,增强扫描可见较均匀强
化。心脏及大血管形态可。
肝脏边缘规整,肝实质密度不均匀,肝右前叶下段见类圆形稍低密度灶,边界清,增强扫描强化
不明显,截面约2.3cm×1.9cm。肝内另见多发结节样低密度灶,增强扫描未见明显强化。肝内外
胆管无明显扩张。胆囊不大,壁略厚,腔内未见明显异常密度影。脾不大,脾实质密度均匀。胰
腺大小、形态及密度未见明显异常。双侧肾上腺增粗,可见结节样改变,增强扫描似见环状强
化。T7、L1椎体变扁,T7为著。
影像诊断:
1.结合病史,符合右肺Ca并右肺多发肺不张CT表现;
2.双侧肾上腺结节灶,转移可疑,建议随诊观察;
3.双肺炎性索条灶;
4.肝右前叶低密度灶,建议短期随诊观察,必要时MR检查;
5.肝内低密度灶,考虑囊肿;
6.符合T7、L1椎体压缩骨折CT表现。
报告医师:
孙丽
审核医师:
鲁丽
检查日期: 2025-08-04
2025-08-04
---
超声诊断报告
住院号
诊疗号：L20260224030400025
姓名
性别：男
年龄：71岁
科室
检查项目：彩超（下肢静脉）
超声所见：
双侧股总静脉、股浅静脉、股深静脉、腘静脉、胫前静脉、胫
后静脉、腓静脉管壁光滑，管径正常，管腔内未探及异常回声，压
之完全变形，血流通畅，充盈良好，远段加压，近段血流加速。
双侧小腿肌间静脉丛内未探及异常扩张的静脉，压之完全变
形，腔内透声好，血流充盈良好。
右侧小腿段探及大隐静脉多条属支迂曲、扩张，小腿段最宽约
3.3mm，管腔内透声好；左侧小腿浅静脉未探及明显扩张，腔内未
探及明显异常。
瓦氏试验：右侧隐股静脉瓣探及反流信号，反流时间2秒。左
侧隐股静脉瓣未探及反流信号。
超声提示：
双侧下肢静脉未探及血栓征象
右侧大隐静脉曲张
右侧隐股静脉瓣膜功能不全
检查日期 2026-02-25 14:05:45
医师：
记录员：
本诊断报告供临床参考。报告仅此一份，请妥善保存，复诊时带来，
技术支持 青岛美迪康数字工程有限公司
卢佳佳
---
超声诊断报告
住院号
诊疗号：L20260224030400025
姓名
性别：男 年龄：71 岁科
检查项目：彩超（心脏）
AO 30mm (20-36mm)
LA 26mm (23-40mm)
LV 43mm (38-54mm)
IVS 10mm (6-11.7mm)
LVPW 10mm (6-11.7mm)
RV 20mm (14-31mm)
RA左右 33mm (26-45mm)
PA 21mm (15-28mm)
LVEF 56% (52-78%)
RA上下 41mm (34-55mm)
超声所见：
一、M型及二维超声表现
各房、室腔内径正常。房、室间隔连续性完整。室间隔及左室游离壁厚度正
常。心肌动度及收缩期增厚率正常，静息状态下未探及明显节段性室壁运动异常。
主动脉瓣膜增厚、回声增强，二尖瓣后叶瓣根部增厚、回声增强，余组瓣膜结构及
启闭活动正常。升主动脉及主肺动脉内径正常。心包腔内未探及明显液性暗区。
二、多普勒超声表现
主动脉瓣少量反流信号。二尖瓣少量反流信号。
三、心功能
LVEF：56%
二尖瓣前向血流频谱：E峰：45cm/s E/A<1
组织多普勒测：E/E'=7.2
超声提示：
主动脉瓣退行性变
二尖瓣退行性变变
检查日期：2026-02-25 14:05:41 医师： 间庆亮 记录员： 卢佳怡
本诊断报告供临床参考。报告仅此一份，请妥善保存，复诊时带来。
技术支持.青岛美迪康数字工程有限公司
---
姓名:
门诊号:
心律: 78 bpm
P-R间期: 181 ms
诊断结论: 1.窦性心律
年龄: 71岁
住院号: 698391
R/SV1: 1.3/0.59 mV
QRS时限: 91 ms
2.正常范围心电图
性别: 男性
科
89 mV
QT/QTc间期: 376 ms
P-QRS-T电轴: 60/67/43°
71
检查时间: 2026-02-26 09:06:46
I
V1
II
V2
III
V3
aVR
V4
aVL
V5
aVF
V6
II
105
125
155
185
215
245
275
305
335
365
395
425
455
485
515
545
575
605
635
665
695
725
755
785
815
845
875
905
935
965
995
1025
1055
1085
1115
1145
1175
1205
1235
1265
1295
1325
1355
1385
1415
1445
1475
1505
1535
1565
1595
1625
1655
1685
1715
1745
1775
1805
1835
1865
1895
1925
1955
1985
2015
2045
2075
2105
2135
2165
2195
2225
2255
2285
2315
2345
2375
2405
2435
2465
2495
2525
2555
2585
2615
2645
2675
2705
2735
2765
2795
2825
2855
2885
2915
2945
2975
3005
3035
3065
3095
3125
3155
3185
3215
3245
3275
3305
3335
3365
3395
3425
3455
3485
3515
3545
3575
3605
3635
3665
3695
3725
3755
3785
3815
3845
3875
3905
3935
3965
3995
4025
4055
4085
4115
4145
4175
4205
4235
4265
4295
4325
4355
4385
4415
4445
4475
4505
4535
4565
4595
4625
4655
4685
4715
4745
4775
4805
4835
4865
4895
4925
4955
4985
5015
5045
5075
5105
5135
5165
5195
5225
5255
5285
5315
5345
5375
5405
5435
5465
5495
5525
5555
5585
5615
5645
5675
5705
5735
5765
5795
5825
5855
5885
5915
5945
5975
6005
6035
6065
6095
6125
6155
6185
6215
6245
6275
6305
6335
6365
6395
6425
6455
6485
6515
6545
6575
6605
6635
6665
6695
6725
6755
6785
6815
6845
6875
6905
6935
6965
6995
7025
7055
7085
7115
7145
7175
7205
7235
7265
7295
7325
7355
7385
7415
7445
7475
7505
7535
7565
7595
7625
7655
7685
7715
7745
7775
7805
7835
7865
7895
7925
7955
7985
8015
8045
8075
8105
8135
8165
8195
8225
8255
8285
8315
8345
8375
8405
8435
8465
8495
8525
8555
8585
8615
8645
8675
8705
8735
8765
8795
8825
8855
8885
8915
8945
8975
9005
9035
9065
9095
9125
9155
9185
9215
9245
9275
9305
9335
9365
9395
9425
9455
9485
9515
9545
9575
9605
9635
9665
9695
9725
9755
9785
9815
9845
9875
9905
9935
9965
9995
10025
10055
10085
10115
10145
10175
10205
10235
10265
10295
10325
10355
10385
10415
10445
10475
10505
10535
10565
10595
10625
10655
10685
10715
10745
10775
10805
10835
10865
10895
10925
10955
10985
11015
11045
11075
11105
11135
11165
11195
11225
11255
11285
11315
11345
11375
11405
11435
11465
11495
11525
11555
11585
11615
11645
11675
11705
11735
11765
11795
11825
11855
11885
11915
11945
11975
12005
12035
12065
12095
12125
12155
12185
12215
12245
12275
12305
12335
12365
12395
12425
12455
12485
12515
12545
12575
12605
12635
12665
12695
12725
12755
12785
12815
12845
12875
12905
12935
12965
12995
13025
13055
13085
13115
13145
13175
13205
13235
13265
13295
13325
13355
13385
13415
13445
13475
13505
13535
13565
13595
13625
13655
13685
13715
13745
13775
13805
13835
13865
13895
13925
13955
13985
14015
14045
14075
14105
14135
14165
14195
14225
14255
14285
14315
14345
14375
14405
14435
14465
14495
14525
14555
14585
14615
14645
14675
14705
14735
14765
14795
14825
14855
14885
14915
14945
14975
15005
15035
15065
15095
15125
15155
15185
15215
15245
15275
15305
15335
15365
15395
15425
15455
15485
15515
15545
15575
15605
15635
15665
15695
15725
15755
15785
15815
15845
15875
15905
15935
15965
15995
16025
16055
16085
16115
16145
16175
16205
16235
16265
16295
16325
16355
16385
16415
16445
16475
16505
16535
16565
16595
16625
16655
16685
16715
16745
16775
16805
16835
16865
16895
16925
16955
16985
17015
17045
17075
17105
17135
17165
17195
17225
17255
17285
17315
17345
17375
17405
17435
17465
17495
17525
17555
17585
17615
17645
17675
17705
17735
17765
17795
17825
17855
17885
17915
17945
17975
18005
18035
18065
18095
18125
18155
18185
18215
18245
18275
18305
18335
18365
18395
18425
18455
18485
18515
18545
18575
18605
18635
18665
18695
18725
18755
18785
18815
18845
18875
18905
18935
18965
18995
19025
19055
19085
19115
19145
19175
19205
19235
19265
19295
19325
19355
19385
19415
19445
19475
19505
19535
19565
19595
19625
19655
19685
19715
19745
19775
19805
19835
19865
19895
19925
19955
19985
20015
20045
20075
20105
20135
20165
20195
20225
20255
20285
20315
20345
20375
20405
20435
20465
20495
20525
20555
20585
20615
20645
20675
20705
20735
20765
20795
20825
20855
20885
20915
20945
20975
21005
21035
21065
21095
21125
21155
21185
21215
21245
21275
21305
21335
21365
21395
21425
21455
21485
21515
21545
21575
21605
21635
21665
21695
21725
21755
21785
21815
21845
21875
21905
21935
21965
21995
22025
22055
22085
22115
22145
22175
22205
22235
22265
22295
22325
22355
22385
22415
22445
22475
22505
22535
22565
22595
22625
22655
22685
22715
22745
22775
22805
22835
22865
22895
22925
22955
22985
23015
23045
23075
23105
23135
23165
23195
23225
23255
23285
23315
23345
23375
23405
23435
23465
23495
23525
23555
23585
23615
23645
23675
23705
23735
23765
23795
23825
23855
23885
23915
23945
23975
24005
24035
24065
24095
24125
24155
24185
24215
24245
24275
24305
24335
24365
24395
24425
24455
24485
24515
24545
24575
24605
24635
24665
24695
24725
24755
24785
24815
24845
24875
24905
24935
24965
24995
25025
25055
25085
25115
25145
25175
25205
25235
25265
25295
25325
25355
25385
25415
25445
25475
25505
25535
25565
25595
25625
25655
25685
25715
25745
25775
25805
25835
25865
25895
25925
25955
25985
26015
26045
26075
26105
26135
26165
26195
26225
26255
26285
26315
26345
26375
26405
26435
26465
26495
26525
26555
26585
26615
26645
26675
26705
26735
26765
26795
26825
26855
26885
26915
26945
26975
27005
27035
27065
27095
27125
27155
27185
27215
27245
27275
27305
27335
27365
27395
27425
27455
27485
27515
27545
27575
27605
27635
27665
27695
27725
27755
27785
27815
27845
27875
27905
27935
27965
27995
28025
28055
28085
28115
28145
28175
28205
28235
28265
28295
28325
28355
28385
28415
28445
28475
28505
28535
28565
28595
28625
28655
28685
28715
28745
28775
28805
28835
28865
28895
28925
28955
28985
29015
29045
29075
29105
29135
29165
29195
29225
29255
29285
29315
29345
29375
29405
29435
29465
29495
29525
29555
29585
29615
29645
29675
29705
29735
29765
29795
29825
29855
29885
29915
29945
29975
30005
30035
30065
30095
30125
30155
30185
30215
30245
30275
30305
30335
30365
30395
30425
30455
30485
30515
30545
30575
30605
30635
30665
30695
30725
30755
30785
30815
30845
30875
30905
30935
30965
30995
31025
31055
31085
31115
31145
31175
31205
31235
31265
31295
31325
31355
31385
31415
31445
31475
31505
31535
31565
31595
31625
31655
31685
31715
31745
31775
31805
31835
31865
31895
31925
31955
31985
32015
32045
32075
32105
32135
32165
32195
32225
32255
32285
32315
32345
32375
32405
32435
32465
32495
32525
32555
32585
32615
32645
32675
32705
32735
32765
32795
32825
32855
32885
32915
32945
32975
33005
33035
33065
33095
33125
33155
33185
33215
33245
33275
33305
33335
33365
33395
33425
33455
33485
33515
33545
33575
33605
33635
33665
33695
33725
33755
33785
33815
33845
33875
33905
33935
33965
33995
34025
34055
34085
34115
34145
34175
34205
34235
34265
34295
34325
34355
34385
34415
34445
34475
34505
34535
34565
34595
34625
34655
34685
34715
34745
34775
34805
34835
34865
34895
34925
34955
34985
35015
35045
35075
35105
35135
35165
35195
35225
35255
35285
35315
35345
35375
35405
35435
35465
35495
35525
35555
35585
35615
35645
35675
35705
35735
35765
35795
35825
35855
35885
35915
35945
35975
36005
36035
36065
36095
36125
36155
36185
36215
36245
36275
36305
36335
36365
36395
36425
36455
36485
36515
36545
36575
36605
36635
36665
36695
36725
36755
36785
36815
36845
36875
36905
36935
36965
36995
37025
37055
37085
37115
37145
37175
37205
37235
37265
37295
37325
37355
37385
37415
37445
37475
37505
37535
37565
37595
37625
37655
37685
37715
37745
37775
37805
37835
37865
37895
37925
37955
37985
38015
38045
38075
38105
38135
38165
38195
38225
38255
38285
38315
38345
38375
38405
38435
38465
38495
38525
38555
38585
38615
38645
38675
38705
38735
38765
38795
38825
38855
38885
38915
38945
38975
39005
39035
39065
39095
39125
39155
39185
39215
39245
39275
39305
39335
39365
39395
39425
39455
39485
39515
39545
39575
39605
39635
39665
39695
39725
39755
39785
39815
39845
39875
39905
39935
39965
39995
40025
40055
40085
40115
40145
40175
40205
40235
40265
40295
40325
40355
40385
40415
40445
40475
40505
40535
40565
40595
40625
40655
40685
40715
40745
40775
40805
40835
40865
40895
40925
40955
40985
41015
41045
41075
41105
41135
41165
41195
41225
41255
41285
41315
41345
41375
41405
41435
41465
41495
41525
41555
41585
41615
41645
41675
41705
41735
41765
41795
41825
41855
41885
41915
41945
41975
42005
42035
42065
42095
42125
42155
42185
42215
42245
42275
42305
42335
42365
42395
42425
42455
42485
42515
42545
42575
42605
42635
42665
42695
42725
42755
42785
42815
42845
42875
42905
42935
42965
42995
43025
43055
43085
43115
43145
43175
43205
43235
43265
43295
43325
43355
43385
43415
43445
43475
43505
43535
43565
43595
43625
43655
43685
43715
43745
43775
43805
43835
43865
43895
43925
43955
43985
44015
44045
44075
44105
44135
44165
44195
44225
44255
44285
44315
44345
44375
44405
44435
44465
44495
44525
44555
44585
44615
44645
44675
44705
44735
44765
44795
44825
44855
44885
44915
44945
44975
45005
45035
45065
45095
45125
45155
45185
45215
45245
45275
45305
45335
45365
45395
45425
45455
45485
45515
45545
45575
45605
45635
45665
45695
45725
45755
45785
45815
45845
45875
45905
45935
45965
45995
46025
46055
46085
46115
46145
46175
46205
46235
46265
46295
46325
46355
46385
46415
46445
46475
46505
46535
46565
46595
46625
46655
46685
46715
46745
46775
46805
46835
46865
46895
46925
46955
46985
47015
47045
47075
47105
47135
47165
47195
47225
47255
47285
47315
47345
47375
47405
47435
47465
47495
47525
47555
47585
47615
47645
47675
47705
47735
47765
47795
47825
47855
47885
47915
47945
47975
48005
48035
48065
48095
48125
48155
48185
48215
48245
48275
48305
48335
48365
48395
48425
48455
48485
48515
48545
48575
48605
48635
48665
48695
48725
48755
48785
48815
48845
48875
48905
48935
48965
48995
49025
49055
49085
49115
49145
49175
49205
49235
49265
49295
49325
49355
49385
49415
49445
49475
49505
49535
49565
49595
49625
49655
49685
49715
49745
49775
49805
49835
49865
49895
49925
49955
49985
50015
50045
50075
50105
50135
50165
50195
50225
50255
50285
50315
50345
50375
50405
50435
50465
50495
50525
50555
50585
50615
50645
50675
50705
50735
50765
50795
50825
50855
50885
50915
50945
50975
51005
51035
51065
51095
51125
51155
51185
51215
51245
51275
51305
51335
51365
51395
51425
51455
51485
51515
51545
51575
51605
51635
51665
51695
51725
51755
51785
51815
51845
51875
51905
51935
51965
51995
52025
52055
52085
52115
52145
52175
52205
52235
52265
52295
52325
52355
52385
52415
52445
52475
52505
52535
52565
52595
52625
52655
52685
52715
52745
52775
52805
52835
52865
52895
52925
52955
52985
53015
53045
53075
53105
53135
53165
53195
53225
53255
53285
53315
53345
53375
53405
53435
53465
53495
53525
53555
53585
53615
53645
53675
53705
53735
53765
53795
53825
53855
53885
53915
53945
53975
54005
54035
54065
54095
54125
54155
54185
54215
54245
54275
54305
54335
54365
54395
54425
54455
54485
54515
54545
54575
54605
54635
54665
54695
54725
54755
54785
54815
54845
54875
54905
54935
54965
54995
55025
55055
55085
55115
55145
55175
55205
55235
55265
55295
55325
55355
55385
55415
55445
55475
55505
55535
55565
55595
55625
55655
55685
55715
55745
55775
55805
55835
55865
55895
55925
55955
55985
56015
56045
56075
56105
56135
56165
56195
56225
56255
56285
56315
56345
56375
56405
56435
56465
56495
56525
56555
56585
56615
56645
56675
56705
56735
56765
56795
56825
56855
56885
56915
56945
56975
57005
57035
57065
57095
57125
57155
57185
57215
57245
57275
57305
57335
57365
57395
57425
57455
57485
57515
57545
57575
57605
57635
57665
57695
57725
57755
57785
57815
57845
57875
57905
57935
57965
57995
58025
58055
58085
58115
58145
58175
58205
58235
58265
58295
58325
58355
58385
58415
58445
58475
58505
58535
58565
58595
58625
58655
58685
58715
58745
58775
58805
58835
58865
58895
58925
58955
58985
59015
59045
59075
59105
59135
59165
59195
59225
59255
59285
59315
59345
59375
59405
59435
59465
59495
59525
59555
59585
59615
59645
59675
59705
59735
59765
59795
59825
59855
59885
59915
59945
59975
60005
60035
60065
60095
60125
60155
60185
60215
60245
60275
60305
60335
60365
60395
60425
60455
60485
60515
60545
60575
60605
60635
60665
60695
60725
60755
60785
60815
60845
60875
60905
60935
60965
60995
61025
61055
61085
61115
61145
61175
61205
61235
61265
61295
61325
61355
61385
61415
61445
61475
61505
61535
61565
61595
61625
61655
61685
61715
61745
61775
61805
61835
61865
61895
61925
61955
61985
62015
62045
62075
62105
62135
62165
62195
62225
62255
62285
62315
62345
62375
62405
62435
62465
62495
62525
62555
62585
62615
62645
62675
62705
62735
62765
62795
62825
62855
62885
62915
62945
62975
63005
63035
63065
63095
63125
63155
63185
63215
63245
63275
63305
63335
63365
63395
63425
63455
63485
63515
63545
63575
63605
63635
63665
63695
63725
63755
63785
63815
63845
63875
63905
63935
63965
63995
64025
64055
64085
64115
64145
64175
64205
64235
64265
64295
64325
64355
64385
64415
64445
64475
64505
64535
64565
64595
64625
64655
64685
64715
64745
64775
64805
64835
64865
64895
64925
64955
64985
65015
65045
65075
65105
65135
65165
65195
65225
65255
65285
65315
65345
65375
65405
65435
65465
65495
65525
65555
65585
65615
65645
65675
65705
65735
65765
65795
65825
65855
65885
65915
65945
65975
66005
66035
66065
66095
66125
66155
66185
66215
66245
66275
66305
66335
66365
66395
66425
66455
66485
66515
66545
66575
66605
66635
66665
66695
66725
66755
66785
66815
66845
66875
66905
66935
66965
66995
67025
67055
67085
67115
67145
67175
67205
67235
67265
67295
67325
67355
67385
67415
67445
67475
67505
67535
67565
67595
67625
67655
67685
67715
67745
67775
67805
67835
67865
67895
67925
67955
67985
68015
68045
68075
68105
68135
68165
68195
68225
68255
68285
68315
68345
68375
68405
68435
68465
68495
68525
68555
68585
68615
68645
68675
68705
68735
68765
68795
68825
68855
68885
68915
68945
68975
69005
69035
69065
69095
69125
69155
69185
69215
69245
69275
69305
69335
69365
69395
69425
69455
69485
69515
69545
69575
69605
69635
69665
69695
69725
69755
69785
69815
69845
69875
69905
69935
69965
69995
70025
70055
70085
70115
70145
70175
70205
70235
70265
70295
70325
70355
70385
70415
70445
70475
70505
70535
70565
70595
70625
70655
70685
70715
70745
70775
70805
70835
70865
7089
告
---
MR诊断报告单
影像号:PMR20260225005
姓名:
性别:男
住院号:
申请科室:
检查类别:MR
年龄:71岁
临床号:
检查项目:磁共振增强,磁共振
岁
特殊成像
检查方法:磁共振增强颅脑,磁共振特殊成像弥散成像DWI
病
区:
影像所见:
双侧侧脑室周围、放射冠区、双侧额叶皮层下见多发斑点状等长T1长T2异常信号,边界尚清,T2-
Flair呈高信号,DWI未见明显高信号,ADC图未见明显低信号,增强扫描未见明显强化。脑室系统
未见明显扩张。脑沟、裂未见明显增宽、加深。中线结构未见移位。扫描野内双侧筛窦、上颌窦
粘膜稍增厚。
影像诊断:
1、脑白质多发异常高信号(Fazekas 1),符合脑小血管病MRI表现;
2、鼻窦炎。
报告医师:
韩培
审核医师:
表小记
检查日期:
2026-02-25
审核日期:
2026-02-25
扫描全能王 创建
---
超声诊断报告
住院号：698391
诊疗号：L20260224030400025
姓名：
性别：男 年龄：71 岁科室：
检查项目：彩超（心脏）
AO 30mm (20-36mm)
LA 26mm (23-40mm)
LV 43mm (38-54mm)
IVS 10mm (8-11.7mm)
LVPW 10mm (8-11.7mm)
RA 20mm (14-31mm)
RA左右 33mm (26-45mm)
PA 21mm (15-29mm)
LVEF 56% (52-78%)
RA上下 41mm (34-55mm)
超声所见：
一、M型及二维超声表现
各房、室腔内径正常。房、室间隔连续性完整。室间隔及左室游离壁厚度正常。心肌动度及收缩期增厚率正常，静息状态下未探及明显节段性室壁运动异常。
主动脉瓣膜增厚、凹声增强，二尖瓣后叶瓣根部增厚、凹声增强，余组瓣膜结构及
启闭活动正常：升主动脉及主肺动脉内径正常。心包腔内未探及明显液性暗区。
二、多普勒超声表现
主动脉瓣少量反流信号。二尖瓣少量反流信号。
三、心功能
LVEF：56%
二尖瓣前向血流频谱：E峰：45cm/s E/A<1
组织多普勒侧：E/E’=7.2
超声提示：
主动脉瓣退行性变
二尖瓣退行性变
检查日期：2026-02-25 14:05:41 医师：
记录员：
卢佳怡
本诊断报告供临床参考，报告仅此一份，请妥善保存，复诊时带来。
2026-08-10 14:44:09,124 INFO     29 [qwen-vl-parser] text API response (len=977):
["姓名", "性别 男", "年龄 47 岁 住院号", "床号 231.2+13", "送检科", "检查日期 2025-12-05 15:02:38", "检查项目", "胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成", "像,上腹部(肝胆胰脾)CT增强扫描", "影像学表现", "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "呈轻度不均匀强化。", "影像学意见", "胸部CT增强+薄层示:", "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃", "镜检查;", "2、双肺散在渗出及纤维灶,较前增多;", "3、原\"左肺上叶小结节影\"未见显示;", "4、双侧尖部胸膜局部增厚;", "5、左侧部分肋骨形态欠规则,必要时ECT检查。", "上下腹部CT增强示:", "1、肝内多发异常强化影,考虑肝转移;", "2、双肾多发囊肿;", "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;", "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;", "5、左肾周渗出性改变。", "本报告仅供临床参考,签字有效。", "报告医师 郭田田", "审核医师 寇明清", "标有(陕HR)的项目为互认项目", "寇明清"]
2026-08-10 14:44:09,124 INFO     29 [qwen-vl-parser] page=4 text: 39 lines (bbox 74-112)
2026-08-10 14:44:09,124 INFO     29 [qwen-vl-parser] page=4 text: 39 sections
2026-08-10 14:44:09,372 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1382610, prompt_len=764
2026-08-10 14:44:09,462 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:44:09.461+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 8, "lag": 0, "done": 62, "failed": 0, "current": {"a1949cec94c711f1bd9827cf206dfa2d": {"id": "a1949cec94c711f1bd9827cf206dfa2d", "doc_id": "a02dce5094c711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SCBA--\u753771\u5c81\uff0c\u5927\u7ec6\u80de\u795e\u7ecf\u5185\u5206\u6ccc\u764c.pdf", "type": "pdf", "location": "SCBA--\u753771\u5c81\uff0c\u5927\u7ec6\u80de\u795e\u7ecf\u5185\u5206\u6ccc\u764c.pdf", "size": 39815932, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786372055550, "task_type": "dataflow", "root_trace_id": "360d2405606643088eb7211aa2053763", "root_traceparent": "00-360d2405606643088eb7211aa2053763-a596baca0218486d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}, "d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:44:10,500 INFO     29 [EMBED-PIPELINE] batch[16:32] text_for_embed=病 理 诊 断 报 告 单
病理号: Q2405649
姓名
性别: 男
年龄: 69
送检材料:
住院号:
门诊号: 9
科别: 特等四病区
病区: T4
床号: 17
(右中间新生物)低分化癌,倾向大细胞癌伴神经内分泌分化。
免疫组化结果: Ki-67 (90%+), CD56 (-), TTF-1(SPT24) (个别+), CK (+), P40 (-), Syn
(-), CgA (-), NapsinA (-), INSM1 (-), Pou2F3 (-), CK8/18 (+), EBER (-)。
PD-L1(E1L3N, Leica BondMAX染色平台)肿瘤细胞数量:>100个;
肿瘤细胞比例评分(TPS): <1%+
阴阳性对照组织:染色正常
备注:
报告医生(签名)谢晓枫
审核医生(签名)武春燕
报告日期: 2024-07-09
本报告仅供临床医生参考,经审核医生签名有效,如发现病理诊断与临床有意外不符,请即与我科联系。
---
手术记录
姓名：
性别：男
年龄：71岁科别：
病案号：
手术开始时间：{2026-03-03 16:00:00}
手术结束时间：{2026-03-03 16:50:00}
术前诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管
继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后
术中诊断：右肺下叶神经内分泌癌（cT4N2M0）IIIB期 纵隔淋巴结继发恶性肿瘤 气管
继发恶性肿瘤 肺不张 气管狭窄 脊柱骨水泥术后
手术名称：肝动脉化疗栓塞术
手术指导者：{无}
手术者：
助：{-}
麻醉方法：{局部麻醉}
手术经过、术中发现的情况及处理：患者仰卧DSA手术床，常规消毒双侧腹股沟皮肤，铺无菌洞
巾。以2%利多卡因局麻右侧腹股沟手术区，取右侧股动脉为穿刺点，穿刺成功后，以Seldinger技
术置入5F导管鞘（泰尔茂），用5F肝管（益心达）联合亲水涂层导丝寻找腹腔干，造影后可见肝
脏转移瘤显影，应用2.2F微导管（埃普特）联合微导丝超选至肿瘤供血血管，再次造影明确肿瘤
供血动脉，予以洛铂30mg动脉灌注化疗，灌注过程顺利，灌注结束后予以用超液态罂粟乙碘油
10ml+伊立替康40mg混合悬液1ml栓塞肿瘤，过程顺利，患者未诉特殊不适，拔除导管及鞘组，穿
刺部位压迫止血，加压包扎后返回病房休息。
1/1
T4
2026-08-10 14:44:10,679 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 14:44:10,679 INFO     29 [Trace] task=a1949cec | doc=SCBA--男71岁，大细胞神经内分泌癌.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "18 items, types={'LabReport': 3, 'DischargeRecord': 1, 'AdmissionRecord': 1, 'ExaminationReport': 12, 'ProgressNote': 1}", "name": "SCBA--男71岁，大细胞神经内分泌癌.pdf", "embedding_token_consumption": 25893}
2026-08-10 14:44:10,679 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 14:44:10,853 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-02-03"
}
```
2026-08-10 14:44:10,854 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=2026-02-03
2026-08-10 14:44:10,862 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1382610, prompt_len=401
2026-08-10 14:44:11,232 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 14:44:11,232 INFO     29 [Trace] task=a1949cec | doc=SCBA--男71岁，大细胞神经内分泌癌.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":18,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 14:44:11,242 INFO     29 [DIAG-EXECUTOR] row_position_int len=8 row[0]=(19, 68, 175, 141, 155) row[-1]=(19, 68, 197, 264, 277)
2026-08-10 14:44:11,242 INFO     29 [DIAG-EXECUTOR] row_position_int len=23 row[0]=(20, 84, 206, 130, 142) row[-1]=(20, 84, 197, 443, 455)
2026-08-10 14:44:11,242 INFO     29 [DIAG-EXECUTOR] row_position_int len=18 row[0]=(21, 79, 164, 132, 144) row[-1]=(21, 79, 197, 384, 396)
2026-08-10 14:44:11,242 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,242 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,243 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,245 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,245 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,245 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,245 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,246 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:44:11,251 INFO     29 set_progress(a1949cec94c711f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 14:44:11 [DOC Engine]:
Start to index...
2026-08-10 14:44:11,271 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.013s]
2026-08-10 14:44:11,275 INFO     29 set_progress(a1949cec94c711f1bd9827cf206dfa2d), progress: 0.8055555555555556, progress_msg: 
2026-08-10 14:44:11,333 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.049s]
2026-08-10 14:44:11,370 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.024s]
2026-08-10 14:44:11,408 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.022s]
2026-08-10 14:44:11,427 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.014s]
2026-08-10 14:44:11,437 INFO     29 set_progress(a1949cec94c711f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 14:44:11 Indexing done (0.18s). Task done (915.99s)
2026-08-10 14:44:11,441 INFO     29 [Done], chunks(18), token(25893), elapsed:915.99
2026-08-10 14:44:11,948 INFO     29 handle_task done for task {"id": "a1949cec94c711f1bd9827cf206dfa2d", "doc_id": "a02dce5094c711f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "SCBA--\u753771\u5c81\uff0c\u5927\u7ec6\u80de\u795e\u7ecf\u5185\u5206\u6ccc\u764c.pdf", "type": "pdf", "location": "SCBA--\u753771\u5c81\uff0c\u5927\u7ec6\u80de\u795e\u7ecf\u5185\u5206\u6ccc\u764c.pdf", "size": 39815932, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786372055550, "task_type": "dataflow", "root_trace_id": "360d2405606643088eb7211aa2053763", "root_traceparent": "00-360d2405606643088eb7211aa2053763-a596baca0218486d-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 14:44:16,969 INFO     29 [qwen-vl-parser] text API response (len=1093):
["CT诊断报告单", "扫码查看影像报告", "诊疗号", "影像号 7159990", "检查号 16220702", "报告日期 2026-02-03 16:13:41", "性别 男", "年龄 48 岁", "住院号", "床号 231.2+7", "送检科别", "检查日期 2026-02-03 10:27:28", "检查项目", "胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像", "影像学表现", "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "呈轻度不均匀强化。左侧肾上腺区见软组织影。", "影像学意见", "胸部CT增强+薄层示:", "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检", "查:", "2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;", "3、双侧尖部胸膜局部增厚;", "4、左侧部分肋骨形态欠规则,必要时ECT检查。", "上下腹部CT增强示:", "1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;", "2、双肾多发囊肿;", "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;", "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;", "5、左肾周渗出性改变;", "6、扫及左侧肾上腺区软组织影,转移可能。", "本报告仅供临床参考,签字有效。", "报告医师 李政晓", "审核医师 马璐瑶", "标有(陕HR)的项目为互认项目"]
2026-08-10 14:44:16,969 INFO     29 [qwen-vl-parser] page=5 text: 43 lines (bbox 113-155)
2026-08-10 14:44:16,969 INFO     29 [qwen-vl-parser] page=5 text: 43 sections
2026-08-10 14:44:17,154 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1024905, prompt_len=764
2026-08-10 14:44:18,631 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-12-05"}
```
2026-08-10 14:44:18,632 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-12-05
2026-08-10 14:44:18,645 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1024905, prompt_len=401
2026-08-10 14:44:22,360 INFO     29 [qwen-vl-parser] text API response (len=653):
["陕西省人民医院", "MR诊断报告单", "诊疗号", "影像号", "检查号", "扫码查看影像报告", "姓名", "性别 男", "年龄 47岁 住院号", "告日期 2025-12-05 20:46:59", "送检", "床号 231.240", "检查日期 2025-12-05 19:14:50", "检查项目", "颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增", "强灌注成像(PWI)", "影像学表现", "双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显", "异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大", "小形态信号未见异常。", "膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×", "3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-", "3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。", "影像学意见", "颅脑MR平扫+DWI+增强未见明显异常。", "盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。", "本报告仅供临床参考,签字有效。", "报告医师 姚云翔", "审核医师 张东升", "标有(陕HR)的项目为互认项目", "张东升"]
2026-08-10 14:44:22,360 INFO     29 [qwen-vl-parser] page=6 text: 31 lines (bbox 156-186)
2026-08-10 14:44:22,361 INFO     29 [qwen-vl-parser] page=6 text: 31 sections
2026-08-10 14:44:22,541 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110320, prompt_len=764
2026-08-10 14:44:23,931 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-04"
}
```
2026-08-10 14:44:23,932 INFO     29 [qwen-vl-parser] page=7 classify=table report_date=2026-01-04
2026-08-10 14:44:23,951 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1110320, prompt_len=756
2026-08-10 14:44:28,957 INFO     29 [qwen-vl-parser] table API response (len=830):
\begin{tabular}{ccccccll}
\hline
1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\
\hline
谷丙转氨酶ALT(8-HR) & 谷草转氨酶AST(8-HR) & 碱性磷酸酶ALP(8-HR) & γ-谷氨酰基转移酶GGT(8-HR) & 胆碱脂酶CHE(陕HR) & 总胆汁酸TBA(陕HR) & 总胆红素TBIL(8-HR) & 直接胆红素DBIL(8-HR) \\
\hline
34 & 29 & 199H & 153H & 5394 & 2.16 & 7.49 & 1.59 \\
\hline
U/L & U/L & U/L & U/L & U/L & umol/L & umol/L & umol/L \\
\hline
9-50 & 15-40 & 45-125 & 10-60 & 5000-12000 & 0-10 & 0-23 & 0-6.84 \\
\hline
IFCC法 & IFCC法 & NPP底物AMP缓冲法 & GCANA底物法 & 底物法 & 酶循环法 & 钒酸盐氧化法 & 钒酸盐氧化法 \\
\hline
\end{tabular}

\begin{tabular}{ccccccll}
\hline
9 & 10 & 11 & 12 & & & & \\
\hline
总蛋白TP(8-HR) & 白蛋白ALB(8-HR) & 球蛋白GLOBU & 白球比A/G & & & & \\
\hline
62.9gL & 37.1L & 25.80 & 1.44 & & & & \\
\hline
g/L & g/L & g/L & & & & & \\
\hline
65-85 & 40-55 & 20-40 & 1.25-2.5 & & & & \\
\hline
双缩脲法 & 溴甲酚绿法 & & & & & & \\
\hline
\end{tabular}
2026-08-10 14:44:28,959 INFO     29 [qwen-vl-parser] page=7 table: 32 LaTeX lines (bbox 187-218)
2026-08-10 14:44:28,959 INFO     29 [qwen-vl-parser] page=7 table: 32 sections
2026-08-10 14:44:29,147 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1104761, prompt_len=764
2026-08-10 14:44:30,527 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-04"
}
```
2026-08-10 14:44:30,528 INFO     29 [qwen-vl-parser] page=8 classify=table report_date=2026-01-04
2026-08-10 14:44:30,547 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1104761, prompt_len=756
2026-08-10 14:44:33,510 INFO     29 [qwen-vl-parser] table API response (len=559):
\begin{tabular}{ccccccll}
\hline
1 & 二氧化碳结合力PCO2 & 27 & mmol/L & 22-29 & & & \\
2 & 尿素UREA (8-HR) & 5.24 & mmol/L & 2.86-8.2 & & & \\
3 & 肌酐CRE (8-HR) & 56.71 & umol/L & 53-123 & & & \\
4 & 钾K (8-HR) & 4.5 & mmol/L & 3.5-5.5 & & & \\
5 & 钠Na (8-HR) & 137 & mmol/L & 137-147 & & & \\
6 & 氯Cl (8-HR) & 102 & mmol/L & 96-108 & & & \\
7 & 尿酸UA (8-HR) & 210.46 & umol/L & 208-428 & & & \\
8 & 视黄醇结合蛋白RBP & 31.87 & mg/L & 25-70 & & & \\
9 & 胱抑素-CCys-C & 0.99 & mg/L & 0.59-1.03 & & & \\
10 & 中性粒细胞明胶酶相关脂质运载蛋白NGA 24.10 & & ng/ml & 0-180 & & & \\
\hline
\end{tabular}
2026-08-10 14:44:33,513 INFO     29 [qwen-vl-parser] page=8 table: 15 LaTeX lines (bbox 219-233)
2026-08-10 14:44:33,513 INFO     29 [qwen-vl-parser] page=8 table: 15 sections
2026-08-10 14:44:33,714 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1212619, prompt_len=764
2026-08-10 14:44:35,196 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-01-04"
}
```
2026-08-10 14:44:35,197 INFO     29 [qwen-vl-parser] page=9 classify=table report_date=2026-01-04
2026-08-10 14:44:35,204 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1212619, prompt_len=756
2026-08-10 14:44:41,882 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:44:41.880+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:44:42,384 INFO     29 [qwen-vl-parser] table API response (len=1085):
\begin{tabular}{cccccc}
\hline
姓名 & 太 & 病人ID: & & & \\
性 & & 床号: & & & \\
年 & & 科 & 室:肿瘤内科 & & \\
龄: & & & & & \\
\hline
白细胞计数WBC(8-HR) & 3.59 & $10^9$/L & 3.5-9.5 & & \\
中性粒细胞比率NEU & 64.70 & \% & 40-75 & & \\
淋巴细胞比率LYM & 22.00 & \% & 20-50 & & \\
单核细胞比率MONO & 11.40H & \% & 3-10 & & \\
嗜酸性粒细胞比率EOS & 1.90 & \% & 0.4-8 & & \\
嗜碱性粒细胞比率BASO & 0.00 & \% & 0-1 & & \\
中性粒细胞绝对值NEU\# & 2.32 & $10^9$/L & 1.8-6.3 & & \\
淋巴细胞绝对值LYM\# & 0.79L & $10^9$/L & 1.1-3.2 & & \\
单核细胞绝对值MONO\# & 0.41 & $10^9$/L & 0.1-0.6 & & \\
嗜酸性粒细胞绝对值EOS\# & 0.07 & $10^9$/L & 0.02-0.52 & & \\
嗜碱性粒细胞绝对值BASO\# & 0.00 & $10^9$/L & 0-0.06 & & \\
红细胞计数RBC(8-HR) & 3.28L & $10^{12}$/L & 4.3-5.8 & & \\
血红蛋白测定HB(8-HR) & 99L & g/L & 130-175 & & \\
红细胞比积测定HCT(8-HR) & 30.9L & \% & 40-50 & & \\
\hline
平均红细胞体积MCV(8-HR) & 94.20 & fL & & & \\
平均红细胞血红蛋白量MCH(8-HR) & 30.20 & pg & & & \\
平均红细胞血红蛋白浓度(8-HR) & 320.00 & g/L & & & \\
红细胞体积分布宽度RDW-CV & 15.10H & \% & & & \\
血小板计数PLT(8-HR) & 384H & $10^9$/L & & & \\
血小板比积PCT & 0.35 & \% & & & \\
平均血小板体积MPV & 9.00L & fL & & & \\
血小板体积分布宽度PDW & 8.50L & fL & & & \\
\hline
\end{tabular}
2026-08-10 14:44:42,385 INFO     29 [qwen-vl-parser] page=9 table: 33 LaTeX lines (bbox 234-266)
2026-08-10 14:44:42,385 INFO     29 [qwen-vl-parser] page=9 table: 33 sections
2026-08-10 14:44:42,726 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1955412, prompt_len=764
2026-08-10 14:44:44,331 INFO     29 [qwen-vl-parser] classify API response (len=63):
```json
{
  "type": "text",
  "report_date": "2026-01-04"
}
```
2026-08-10 14:44:44,331 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=2026-01-04
2026-08-10 14:44:44,354 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1955412, prompt_len=401
2026-08-10 14:44:47,665 INFO     29 [qwen-vl-parser] text API response (len=530):
["项目名称后标注“*”为必填项", "诊断结论:", "1. 窦性心律", "2. 正常范围心电图", "签名：", "姓名", "性别：男", "年龄：47岁", "住院号：0001145836 QRS（陕HR）：102↑ms(60-100)", "ID号：0020553584 P:116↑ms(0-110)", "二病区床号：231.2+7", "QT/QTc（陕HR）：328/397ms(320-440/0-440)", "QRS电轴：70°（-30-90)", "P-R（陕HR）：154ms(120-200)", "Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)", "纸速：25mm/s", "灵敏度：10mm/mV", "滤波：40", "检查日期：2026-01-04 13:", "临床诊断：食管恶性肿瘤", "心率（陕HR）：88(60-100)", "年龄不足1周岁的）", "年", "市）渭南市", "市华阴市", "农民", "婚姻", "2", "1.未婚 2.已婚 3.丧偶 4.离婚 9.其他", "邮编", "714200", "国", "中国", "2001145836", "民医院心电图报告单"]
2026-08-10 14:44:47,666 INFO     29 [qwen-vl-parser] page=10 text: 35 lines (bbox 267-301)
2026-08-10 14:44:47,667 INFO     29 [qwen-vl-parser] page=10 text: 35 sections
2026-08-10 14:44:47,667 INFO     29 [qwen-vl-parser] parse_pdf done: 302 sections from 10 pages.
2026-08-10 14:44:47,683 INFO     29 Close text detector.
2026-08-10 14:44:48,099 INFO     29 Close text recognizer.
2026-08-10 14:44:48,513 INFO     29 Close recognizer.
2026-08-10 14:44:48,928 INFO     29 Close recognizer.
2026-08-10 14:44:49,347 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 14:44:49,347 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Parser:MedLink | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "json"}
2026-08-10 14:44:49,347 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 14:44:49,375 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:44:49,375 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 华阴市人民医院\n[BBOX-1] 病理检查报告单\n[BBOX-2] 姓名：\n[BBOX-3] 性别：男\n[BBOX-4] 年龄：39\n[BBOX-5] 病理号：2018-0079\n[BBOX-6] 送检单位：本院\n[BBOX-7] 科别：普外科\n[BBOX-8] 住院号：1800732\n[BBOX-9] 床号：25\n[BBOX-10] 送检日期：2018-01-27\n[BBOX-11] 送检医师：韩晔\n[BBOX-12] 送检材料：食管\n[BBOX-13] 临床诊断：\n[BBOX-14] 肉眼所见：\n[BBOX-15] 送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管\n[BBOX-16] 端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c\n[BBOX-17] ，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，\n[BBOX-18] V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，\n[BBOX-19] 径0.8cm；另送第五组淋巴结，灰红色两块。\n[BBOX-20] 光镜所见：\n[BBOX-21] 病理诊断：\n[BBOX-22] 食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润\n[BBOX-23] 第五组淋巴结（1/1枚）可见癌转移\n[BBOX-24] 食管周淋巴结（5枚）未见癌组织\n[BBOX-25] 另送上下切缘未见癌组织\n[BBOX-26] 上、下切缘未见癌组织\n[BBOX-27] 纤维脂肪组织内未见癌组织\n[BBOX-28] 24小时内入出院记录\n[BBOX-29] 姓名\n[BBOX-30] 性别：男\n[BBOX-31] 年龄：47岁\n[BBOX-32] 民族：汉族\n[BBOX-33] 出生日期：1978-01-07\n[BBOX-34] 婚姻状况：已婚\n[BBOX-35] 籍贯：\n[BBOX-36] 出生地：\n[BBOX-37] 国籍：\n[BBOX-38] 证件号码：\n[BBOX-39] 工作单位：\n[BBOX-40] 职业：\n[BBOX-41] 详细地址：\n[BBOX-42] 联系电话：\n[BBOX-43] 联系人：\n[BBOX-44] 关系：配偶\n[BBOX-45] 入院日期：2026-01-16 10:19\n[BBOX-46] 病历完成时间：2026-01-16 10:49\n[BBOX-47] 病史陈述者：患者本人\n[BBOX-48] 可靠性：可靠\n[BBOX-49] 是否传染病：否\n[BBOX-50] 既往是否健康：是\n[BBOX-51] 主诉：食管鳞癌术后7年余，肝转移11月余。\n[BBOX-52] 现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。\n[BBOX-53] 入院情况：神志清，精神可，食纳夜休尚可。\n[BBOX-54] 症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。\n[BBOX-55] 症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。\n[BBOX-56] 第1页\n[BBOX-57] 入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后\n[BBOX-58] 4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后\n[BBOX-59] 7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架\n[BBOX-60] 诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐\n[BBOX-61] 酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。\n[BBOX-62] 出院情况：神志清，精神可，食纳夜休尚可。\n[BBOX-63] 出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后\n[BBOX-64] 4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后\n[BBOX-65] 7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架\n[BBOX-66] 出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉\n[BBOX-67] 奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我\n[BBOX-68] 科随诊。\n[BBOX-69] 接诊医师签名：\n[BBOX-70] 住院医师签名：\n[BBOX-71] 主治医师签名：\n[BBOX-72] 主（副主）任医师签名：\n[BBOX-73] 第 2 页\n[BBOX-74] 姓名\n[BBOX-75] 性别 男\n[BBOX-76] 年龄 47 岁 住院号\n[BBOX-77] 床号 231.2+13\n[BBOX-78] 送检科\n[BBOX-79] 检查日期 2025-12-05 15:02:38\n[BBOX-80] 检查项目\n[BBOX-81] 胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成\n[BBOX-82] 像,上腹部(肝胆胰脾)CT增强扫描\n[BBOX-83] 影像学表现\n[BBOX-84] 原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不\n[BBOX-85] 均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,\n[BBOX-86] 肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及\n[BBOX-87] 大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n[BBOX-88] 肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝\n[BBOX-89] 右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,\n[BBOX-90] 壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态\n[BBOX-91] 正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,\n[BBOX-92] 未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描\n[BBOX-93] 呈轻度不均匀强化。\n[BBOX-94] 影像学意见\n[BBOX-95] 胸部CT增强+薄层示:\n[BBOX-96] 1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃\n[BBOX-97] 镜检查;\n[BBOX-98] 2、双肺散在渗出及纤维灶,较前增多;\n[BBOX-99] 3、原\"左肺上叶小结节影\"未见显示;\n[BBOX-100] 4、双侧尖部胸膜局部增厚;\n[BBOX-101] 5、左侧部分肋骨形态欠规则,必要时ECT检查。\n[BBOX-102] 上下腹部CT增强示:\n[BBOX-103] 1、肝内多发异常强化影,考虑肝转移;\n[BBOX-104] 2、双肾多发囊肿;\n[BBOX-105] 3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;\n[BBOX-106] 4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;\n[BBOX-107] 5、左肾周渗出性改变。\n[BBOX-108] 本报告仅供临床参考,签字有效。\n[BBOX-109] 报告医师 郭田田\n[BBOX-110] 审核医师 寇明清\n[BBOX-111] 标有(陕HR)的项目为互认项目\n[BBOX-112] 寇明清\n[BBOX-113] CT诊断报告单\n[BBOX-114] 扫码查看影像报告\n[BBOX-115] 诊疗号\n[BBOX-116] 影像号 7159990\n[BBOX-117] 检查号 16220702\n[BBOX-118] 报告日期 2026-02-03 16:13:41\n[BBOX-119] 性别 男\n[BBOX-120] 年龄 48 岁\n[BBOX-121] 住院号\n[BBOX-122] 床号 231.2+7\n[BBOX-123] 送检科别\n[BBOX-124] 检查日期 2026-02-03 10:27:28\n[BBOX-125] 检查项目\n[BBOX-126] 胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像\n[BBOX-127] 影像学表现\n[BBOX-128] 原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不\n[BBOX-129] 均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,\n[BBOX-130] 肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及\n[BBOX-131] 大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n[BBOX-132] 肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝\n[BBOX-133] 右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,\n[BBOX-134] 壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态\n[BBOX-135] 正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,\n[BBOX-136] 未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描\n[BBOX-137] 呈轻度不均匀强化。左侧肾上腺区见软组织影。\n[BBOX-138] 影像学意见\n[BBOX-139] 胸部CT增强+薄层示:\n[BBOX-140] 1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检\n[BBOX-141] 查:\n[BBOX-142] 2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;\n[BBOX-143] 3、双侧尖部胸膜局部增厚;\n[BBOX-144] 4、左侧部分肋骨形态欠规则,必要时ECT检查。\n[BBOX-145] 上下腹部CT增强示:\n[BBOX-146] 1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;\n[BBOX-147] 2、双肾多发囊肿;\n[BBOX-148] 3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;\n[BBOX-149] 4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;\n[BBOX-150] 5、左肾周渗出性改变;\n[BBOX-151] 6、扫及左侧肾上腺区软组织影,转移可能。\n[BBOX-152] 本报告仅供临床参考,签字有效。\n[BBOX-153] 报告医师 李政晓\n[BBOX-154] 审核医师 马璐瑶\n[BBOX-155] 标有(陕HR)的项目为互认项目\n[BBOX-156] 陕西省人民医院\n[BBOX-157] MR诊断报告单\n[BBOX-158] 诊疗号\n[BBOX-159] 影像号\n[BBOX-160] 检查号\n[BBOX-161] 扫码查看影像报告\n[BBOX-162] 姓名\n[BBOX-163] 性别 男\n[BBOX-164] 年龄 47岁 住院号\n[BBOX-165] 告日期 2025-12-05 20:46:59\n[BBOX-166] 送检\n[BBOX-167] 床号 231.240\n[BBOX-168] 检查日期 2025-12-05 19:14:50\n[BBOX-169] 检查项目\n[BBOX-170] 颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增\n[BBOX-171] 强灌注成像(PWI)\n[BBOX-172] 影像学表现\n[BBOX-173] 双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显\n[BBOX-174] 异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大\n[BBOX-175] 小形态信号未见异常。\n[BBOX-176] 膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×\n[BBOX-177] 3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-\n[BBOX-178] 3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。\n[BBOX-179] 影像学意见\n[BBOX-180] 颅脑MR平扫+DWI+增强未见明显异常。\n[BBOX-181] 盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。\n[BBOX-182] 本报告仅供临床参考,签字有效。\n[BBOX-183] 报告医师 姚云翔\n[BBOX-184] 审核医师 张东升\n[BBOX-185] 标有(陕HR)的项目为互认项目\n[BBOX-186] 张东升\n[BBOX-187] \\begin{tabular}{ccccccll}\n[BBOX-188] 报告时间: 2026-01-04\n[BBOX-189] \\hline\n[BBOX-190] 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\\\\n[BBOX-191] \\hline\n[BBOX-192] 谷丙转氨酶ALT(8-HR) & 谷草转氨酶AST(8-HR) & 碱性磷酸酶ALP(8-HR) & γ-谷氨酰基转移酶GGT(8-HR) & 胆碱脂酶CHE(陕HR) & 总胆汁酸TBA(陕HR) & 总胆红素TBIL(8-HR) & 直接胆红素DBIL(8-HR) \\\\\n[BBOX-193] \\hline\n[BBOX-194] 34 & 29 & 199H & 153H & 5394 & 2.16 & 7.49 & 1.59 \\\\\n[BBOX-195] \\hline\n[BBOX-196] U/L & U/L & U/L & U/L & U/L & umol/L & umol/L & umol/L \\\\\n[BBOX-197] \\hline\n[BBOX-198] 9-50 & 15-40 & 45-125 & 10-60 & 5000-12000 & 0-10 & 0-23 & 0-6.84 \\\\\n[BBOX-199] \\hline\n[BBOX-200] IFCC法 & IFCC法 & NPP底物AMP缓冲法 & GCANA底物法 & 底物法 & 酶循环法 & 钒酸盐氧化法 & 钒酸盐氧化法 \\\\\n[BBOX-201] \\hline\n[BBOX-202] \\end{tabular}\n[BBOX-203] \\begin{tabular}{ccccccll}\n[BBOX-204] 报告时间: 2026-01-04\n[BBOX-205] \\hline\n[BBOX-206] 9 & 10 & 11 & 12 & & & & \\\\\n[BBOX-207] \\hline\n[BBOX-208] 总蛋白TP(8-HR) & 白蛋白ALB(8-HR) & 球蛋白GLOBU & 白球比A/G & & & & \\\\\n[BBOX-209] \\hline\n[BBOX-210] 62.9gL & 37.1L & 25.80 & 1.44 & & & & \\\\\n[BBOX-211] \\hline\n[BBOX-212] g/L & g/L & g/L & & & & & \\\\\n[BBOX-213] \\hline\n[BBOX-214] 65-85 & 40-55 & 20-40 & 1.25-2.5 & & & & \\\\\n[BBOX-215] \\hline\n[BBOX-216] 双缩脲法 & 溴甲酚绿法 & & & & & & \\\\\n[BBOX-217] \\hline\n[BBOX-218] \\end{tabular}\n[BBOX-219] \\begin{tabular}{ccccccll}\n[BBOX-220] 报告时间: 2026-01-04\n[BBOX-221] \\hline\n[BBOX-222] 1 & 二氧化碳结合力PCO2 & 27 & mmol/L & 22-29 & & & \\\\\n[BBOX-223] 2 & 尿素UREA (8-HR) & 5.24 & mmol/L & 2.86-8.2 & & & \\\\\n[BBOX-224] 3 & 肌酐CRE (8-HR) & 56.71 & umol/L & 53-123 & & & \\\\\n[BBOX-225] 4 & 钾K (8-HR) & 4.5 & mmol/L & 3.5-5.5 & & & \\\\\n[BBOX-226] 5 & 钠Na (8-HR) & 137 & mmol/L & 137-147 & & & \\\\\n[BBOX-227] 6 & 氯Cl (8-HR) & 102 & mmol/L & 96-108 & & & \\\\\n[BBOX-228] 7 & 尿酸UA (8-HR) & 210.46 & umol/L & 208-428 & & & \\\\\n[BBOX-229] 8 & 视黄醇结合蛋白RBP & 31.87 & mg/L & 25-70 & & & \\\\\n[BBOX-230] 9 & 胱抑素-CCys-C & 0.99 & mg/L & 0.59-1.03 & & & \\\\\n[BBOX-231] 10 & 中性粒细胞明胶酶相关脂质运载蛋白NGA 24.10 & & ng/ml & 0-180 & & & \\\\\n[BBOX-232] \\hline\n[BBOX-233] \\end{tabular}\n[BBOX-234] \\begin{tabular}{cccccc}\n[BBOX-235] 报告时间: 2026-01-04\n[BBOX-236] \\hline\n[BBOX-237] 姓名 & 太 & 病人ID: & & & \\\\\n[BBOX-238] 性 & & 床号: & & & \\\\\n[BBOX-239] 年 & & 科 & 室:肿瘤内科 & & \\\\\n[BBOX-240] 龄: & & & & & \\\\\n[BBOX-241] \\hline\n[BBOX-242] 白细胞计数WBC(8-HR) & 3.59 & $10^9$/L & 3.5-9.5 & & \\\\\n[BBOX-243] 中性粒细胞比率NEU & 64.70 & \\% & 40-75 & & \\\\\n[BBOX-244] 淋巴细胞比率LYM & 22.00 & \\% & 20-50 & & \\\\\n[BBOX-245] 单核细胞比率MONO & 11.40H & \\% & 3-10 & & \\\\\n[BBOX-246] 嗜酸性粒细胞比率EOS & 1.90 & \\% & 0.4-8 & & \\\\\n[BBOX-247] 嗜碱性粒细胞比率BASO & 0.00 & \\% & 0-1 & & \\\\\n[BBOX-248] 中性粒细胞绝对值NEU\\# & 2.32 & $10^9$/L & 1.8-6.3 & & \\\\\n[BBOX-249] 淋巴细胞绝对值LYM\\# & 0.79L & $10^9$/L & 1.1-3.2 & & \\\\\n[BBOX-250] 单核细胞绝对值MONO\\# & 0.41 & $10^9$/L & 0.1-0.6 & & \\\\\n[BBOX-251] 嗜酸性粒细胞绝对值EOS\\# & 0.07 & $10^9$/L & 0.02-0.52 & & \\\\\n[BBOX-252] 嗜碱性粒细胞绝对值BASO\\# & 0.00 & $10^9$/L & 0-0.06 & & \\\\\n[BBOX-253] 红细胞计数RBC(8-HR) & 3.28L & $10^{12}$/L & 4.3-5.8 & & \\\\\n[BBOX-254] 血红蛋白测定HB(8-HR) & 99L & g/L & 130-175 & & \\\\\n[BBOX-255] 红细胞比积测定HCT(8-HR) & 30.9L & \\% & 40-50 & & \\\\\n[BBOX-256] \\hline\n[BBOX-257] 平均红细胞体积MCV(8-HR) & 94.20 & fL & & & \\\\\n[BBOX-258] 平均红细胞血红蛋白量MCH(8-HR) & 30.20 & pg & & & \\\\\n[BBOX-259] 平均红细胞血红蛋白浓度(8-HR) & 320.00 & g/L & & & \\\\\n[BBOX-260] 红细胞体积分布宽度RDW-CV & 15.10H & \\% & & & \\\\\n[BBOX-261] 血小板计数PLT(8-HR) & 384H & $10^9$/L & & & \\\\\n[BBOX-262] 血小板比积PCT & 0.35 & \\% & & & \\\\\n[BBOX-263] 平均血小板体积MPV & 9.00L & fL & & & \\\\\n[BBOX-264] 血小板体积分布宽度PDW & 8.50L & fL & & & \\\\\n[BBOX-265] \\hline\n[BBOX-266] \\end{tabular}\n[BBOX-267] 项目名称后标注“*”为必填项\n[BBOX-268] 诊断结论:\n[BBOX-269] 1. 窦性心律\n[BBOX-270] 2. 正常范围心电图\n[BBOX-271] 签名：\n[BBOX-272] 姓名\n[BBOX-273] 性别：男\n[BBOX-274] 年龄：47岁\n[BBOX-275] 住院号：0001145836 QRS（陕HR）：102↑ms(60-100)\n[BBOX-276] ID号：0020553584 P:116↑ms(0-110)\n[BBOX-277] 二病区床号：231.2+7\n[BBOX-278] QT/QTc（陕HR）：328/397ms(320-440/0-440)\n[BBOX-279] QRS电轴：70°（-30-90)\n[BBOX-280] P-R（陕HR）：154ms(120-200)\n[BBOX-281] Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)\n[BBOX-282] 纸速：25mm/s\n[BBOX-283] 灵敏度：10mm/mV\n[BBOX-284] 滤波：40\n[BBOX-285] 检查日期：2026-01-04 13:\n[BBOX-286] 临床诊断：食管恶性肿瘤\n[BBOX-287] 心率（陕HR）：88(60-100)\n[BBOX-288] 年龄不足1周岁的）\n[BBOX-289] 年\n[BBOX-290] 市）渭南市\n[BBOX-291] 市华阴市\n[BBOX-292] 农民\n[BBOX-293] 婚姻\n[BBOX-294] 2\n[BBOX-295] 1.未婚 2.已婚 3.丧偶 4.离婚 9.其他\n[BBOX-296] 邮编\n[BBOX-297] 714200\n[BBOX-298] 国\n[BBOX-299] 中国\n[BBOX-300] 2001145836\n[BBOX-301] 民医院心电图报告单"
  }
]
2026-08-10 14:44:58,562 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:44:58,581 INFO     29 [SmartSplitter] SmartSplitter done: 7 chunks from 7 LLM segments (all bbox_id). Types: {'ExaminationReport': 5, 'DischargeRecord': 1, 'LabReport': 1}
2026-08-10 14:44:58,595 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 14:44:58,595 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks": "7 items, types={'ExaminationReport': 5, 'DischargeRecord': 1, 'LabReport': 1}"}
2026-08-10 14:44:58,595 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 14:44:58,595 INFO     29 [ChunkRouter] Routed 7 chunks into 3 groups: {'chunks_Examination': 5, 'chunks_Discharge': 1, 'chunks_LabExam': 1}
2026-08-10 14:44:58,606 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 14:44:58,607 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | ChunkRouter:Router | outputs={"html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks": "7 items, types={'ExaminationReport': 5, 'DischargeRecord': 1, 'LabReport': 1}", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:44:58,607 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 14:44:58,614 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:44:58,615 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:44:58,615 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[6, 7, 8]
2026-08-10 14:44:58,616 INFO     29 [qwen-vl-table] positions ： [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:44:58,823 INFO     29 [qwen-vl-table] page=6, rect=595x841, img=(1653x2337)
2026-08-10 14:44:59,038 INFO     29 [qwen-vl-table] page=7, rect=595x841, img=(1653x2337)
2026-08-10 14:44:59,246 INFO     29 [qwen-vl-table] page=8, rect=595x841, img=(1653x2337)
2026-08-10 14:44:59,247 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:44:59,247 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 187, \"bbox_end\": 266, \"encounter_dates\": [\"2026-01-04\"], \"department\": \"肿瘤内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{ccccccll}\n报告时间: 2026-01-04\n\\hline\n1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 \\\\\n\\hline\n谷丙转氨酶ALT(8-HR) & 谷草转氨酶AST(8-HR) & 碱性磷酸酶ALP(8-HR) & γ-谷氨酰基转移酶GGT(8-HR) & 胆碱脂酶CHE(陕HR) & 总胆汁酸TBA(陕HR) & 总胆红素TBIL(8-HR) & 直接胆红素DBIL(8-HR) \\\\\n\\hline\n34 & 29 & 199H & 153H & 5394 & 2.16 & 7.49 & 1.59 \\\\\n\\hline\nU/L & U/L & U/L & U/L & U/L & umol/L & umol/L & umol/L \\\\\n\\hline\n9-50 & 15-40 & 45-125 & 10-60 & 5000-12000 & 0-10 & 0-23 & 0-6.84 \\\\\n\\hline\nIFCC法 & IFCC法 & NPP底物AMP缓冲法 & GCANA底物法 & 底物法 & 酶循环法 & 钒酸盐氧化法 & 钒酸盐氧化法 \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccll}\n报告时间: 2026-01-04\n\\hline\n9 & 10 & 11 & 12 & & & & \\\\\n\\hline\n总蛋白TP(8-HR) & 白蛋白ALB(8-HR) & 球蛋白GLOBU & 白球比A/G & & & & \\\\\n\\hline\n62.9gL & 37.1L & 25.80 & 1.44 & & & & \\\\\n\\hline\ng/L & g/L & g/L & & & & & \\\\",
    "role": "user"
  }
]
2026-08-10 14:45:05,685 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:05,685 INFO     29 [qwen-vl-table] page=6 LLM output (len=2007):
{
  "report_date": "2026-01-04",
  "items": [
    {
      "name": "谷丙转氨酶",
      "item_code": "ALT",
      "value": "34",
      "unit": "U/L",
      "reference_range": "9-50",
      "abnormal": false
    },
    {
      "name": "谷草转氨酶",
      "item_code": "AST",
      "value": "29",
      "unit": "U/L",
      "reference_range": "15-40",
      "abnormal": false
    },
    {
      "name": "碱性磷酸酶",
      "item_code": "ALP",
      "value": "199",
      "unit": "U/L",
      "reference_range": "45-125",
      "abnormal": true
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": "GGT",
      "value": "153",
      "unit": "U/L",
      "reference_range": "10-60",
      "abnormal": true
    },
    {
      "name": "胆碱脂酶",
      "item_code": "CHE",
      "value": "5394",
      "unit": "U/L",
      "reference_range": "5000-12000",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": "TBA",
      "value": "2.16",
      "unit": "umol/L",
      "reference_range": "0-10",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": "TBIL",
      "value": "7.49",
      "unit": "umol/L",
      "reference_range": "0-23",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": "DBIL",
      "value": "1.59",
      "unit": "umol/L",
      "reference_range": "0-6.84",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": "TP",
      "value": "62.9",
      "unit": "g/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": "ALB",
      "value": "37.1",
      "unit": "g/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": "GLOBU",
      "value": "25.80",
      "unit": "g/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "白球比",
      "item_code": "A/G",
      "value": "1.44",
      "unit": null,
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 14:45:05,686 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:05,686 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 187, \"bbox_end\": 266, \"encounter_dates\": [\"2026-01-04\"], \"department\": \"肿瘤内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\hline\n65-85 & 40-55 & 20-40 & 1.25-2.5 & & & & \\\\\n\\hline\n双缩脲法 & 溴甲酚绿法 & & & & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{ccccccll}\n报告时间: 2026-01-04\n\\hline\n1 & 二氧化碳结合力PCO2 & 27 & mmol/L & 22-29 & & & \\\\\n2 & 尿素UREA (8-HR) & 5.24 & mmol/L & 2.86-8.2 & & & \\\\\n3 & 肌酐CRE (8-HR) & 56.71 & umol/L & 53-123 & & & \\\\\n4 & 钾K (8-HR) & 4.5 & mmol/L & 3.5-5.5 & & & \\\\\n5 & 钠Na (8-HR) & 137 & mmol/L & 137-147 & & & \\\\\n6 & 氯Cl (8-HR) & 102 & mmol/L & 96-108 & & & \\\\\n7 & 尿酸UA (8-HR) & 210.46 & umol/L & 208-428 & & & \\\\\n8 & 视黄醇结合蛋白RBP & 31.87 & mg/L & 25-70 & & & \\\\\n9 & 胱抑素-CCys-C & 0.99 & mg/L & 0.59-1.03 & & & \\\\\n10 & 中性粒细胞明胶酶相关脂质运载蛋白NGA 24.10 & & ng/ml & 0-180 & & & \\\\\n\\hline\n\\end{tabular}\n\\begin{tabular}{cccccc}\n报告时间: 2026-01-04\n\\hline\n姓名 & 太 & 病人ID: & & & \\\\\n性 & & 床号: & & & \\\\",
    "role": "user"
  }
]
2026-08-10 14:45:11,537 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:11,538 INFO     29 [qwen-vl-table] page=7 LLM output (len=1723):
{
  "report_date": "2026-01-04",
  "items": [
    {
      "name": "二氧化碳结合力",
      "item_code": "PCO2",
      "value": "27",
      "unit": "mmol/L",
      "reference_range": "22-29",
      "abnormal": false
    },
    {
      "name": "尿素",
      "item_code": "UREA",
      "value": "5.24",
      "unit": "mmol/L",
      "reference_range": "2.86-8.2",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": "CRE",
      "value": "56.71",
      "unit": "umol/L",
      "reference_range": "53-123",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": "K",
      "value": "4.5",
      "unit": "mmol/L",
      "reference_range": "3.5-5.5",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": "Na",
      "value": "137",
      "unit": "mmol/L",
      "reference_range": "137-147",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": "Cl",
      "value": "102",
      "unit": "mmol/L",
      "reference_range": "96-108",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": "UA",
      "value": "210.46",
      "unit": "umol/L",
      "reference_range": "208-428",
      "abnormal": false
    },
    {
      "name": "视黄醇结合蛋白",
      "item_code": "RBP",
      "value": "31.87",
      "unit": "mg/L",
      "reference_range": "25-70",
      "abnormal": false
    },
    {
      "name": "胱抑素-C",
      "item_code": "Cys-C",
      "value": "0.99",
      "unit": "mg/L",
      "reference_range": "0.59-1.03",
      "abnormal": false
    },
    {
      "name": "中性粒细胞明胶酶相关脂质运载蛋白",
      "item_code": "NGA",
      "value": "24.10",
      "unit": "ng/ml",
      "reference_range": "0-180",
      "abnormal": false
    }
  ]
}
2026-08-10 14:45:11,538 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:11,538 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 187, \"bbox_end\": 266, \"encounter_dates\": [\"2026-01-04\"], \"department\": \"肿瘤内科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "年 & & 科 & 室:肿瘤内科 & & \\\\\n龄: & & & & & \\\\\n\\hline\n白细胞计数WBC(8-HR) & 3.59 & $10^9$/L & 3.5-9.5 & & \\\\\n中性粒细胞比率NEU & 64.70 & \\% & 40-75 & & \\\\\n淋巴细胞比率LYM & 22.00 & \\% & 20-50 & & \\\\\n单核细胞比率MONO & 11.40H & \\% & 3-10 & & \\\\\n嗜酸性粒细胞比率EOS & 1.90 & \\% & 0.4-8 & & \\\\\n嗜碱性粒细胞比率BASO & 0.00 & \\% & 0-1 & & \\\\\n中性粒细胞绝对值NEU\\# & 2.32 & $10^9$/L & 1.8-6.3 & & \\\\\n淋巴细胞绝对值LYM\\# & 0.79L & $10^9$/L & 1.1-3.2 & & \\\\\n单核细胞绝对值MONO\\# & 0.41 & $10^9$/L & 0.1-0.6 & & \\\\\n嗜酸性粒细胞绝对值EOS\\# & 0.07 & $10^9$/L & 0.02-0.52 & & \\\\\n嗜碱性粒细胞绝对值BASO\\# & 0.00 & $10^9$/L & 0-0.06 & & \\\\\n红细胞计数RBC(8-HR) & 3.28L & $10^{12}$/L & 4.3-5.8 & & \\\\\n血红蛋白测定HB(8-HR) & 99L & g/L & 130-175 & & \\\\\n红细胞比积测定HCT(8-HR) & 30.9L & \\% & 40-50 & & \\\\\n\\hline\n平均红细胞体积MCV(8-HR) & 94.20 & fL & & & \\\\\n平均红细胞血红蛋白量MCH(8-HR) & 30.20 & pg & & & \\\\\n平均红细胞血红蛋白浓度(8-HR) & 320.00 & g/L & & & \\\\\n红细胞体积分布宽度RDW-CV & 15.10H & \\% & & & \\\\\n血小板计数PLT(8-HR) & 384H & $10^9$/L & & & \\\\\n血小板比积PCT & 0.35 & \\% & & & \\\\\n平均血小板体积MPV & 9.00L & fL & & & \\\\\n血小板体积分布宽度PDW & 8.50L & fL & & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 14:45:12,669 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:45:12.667+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:45:22,921 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:22,921 INFO     29 [qwen-vl-table] page=8 LLM output (len=3710):
{
  "report_date": "2026-01-04",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "3.59",
      "unit": "10^9/L",
      "reference_range": "3.5-9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞比率",
      "item_code": "NEU",
      "value": "64.70",
      "unit": "%",
      "reference_range": "40-75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞比率",
      "item_code": "LYM",
      "value": "22.00",
      "unit": "%",
      "reference_range": "20-50",
      "abnormal": false
    },
    {
      "name": "单核细胞比率",
      "item_code": "MONO",
      "value": "11.40",
      "unit": "%",
      "reference_range": "3-10",
      "abnormal": true
    },
    {
      "name": "嗜酸性粒细胞比率",
      "item_code": "EOS",
      "value": "1.90",
      "unit": "%",
      "reference_range": "0.4-8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞比率",
      "item_code": "BASO",
      "value": "0.00",
      "unit": "%",
      "reference_range": "0-1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEU#",
      "value": "2.32",
      "unit": "10^9/L",
      "reference_range": "1.8-6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYM#",
      "value": "0.79",
      "unit": "10^9/L",
      "reference_range": "1.1-3.2",
      "abnormal": true
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO#",
      "value": "0.41",
      "unit": "10^9/L",
      "reference_range": "0.1-0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EOS#",
      "value": "0.07",
      "unit": "10^9/L",
      "reference_range": "0.02-0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.00",
      "unit": "10^9/L",
      "reference_range": "0-0.06",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "3.28",
      "unit": "10^12/L",
      "reference_range": "4.3-5.8",
      "abnormal": true
    },
    {
      "name": "血红蛋白测定",
      "item_code": "HB",
      "value": "99",
      "unit": "g/L",
      "reference_range": "130-175",
      "abnormal": true
    },
    {
      "name": "红细胞比积测定",
      "item_code": "HCT",
      "value": "30.9",
      "unit": "%",
      "reference_range": "40-50",
      "abnormal": true
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "94.20",
      "unit": "fL",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白量",
      "item_code": "MCH",
      "value": "30.20",
      "unit": "pg",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": null,
      "value": "320.00",
      "unit": "g/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度",
      "item_code": "RDW-CV",
      "value": "15.10",
      "unit": "%",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "384",
      "unit": "10^9/L",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "血小板比积",
      "item_code": "PCT",
      "value": "0.35",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均血小板体积",
      "item_code": "MPV",
      "value": "9.00",
      "unit": "fL",
      "reference_range": null,
      "abnormal": true
    },
    {
      "name": "血小板体积分布宽度",
      "item_code": "PDW",
      "value": "8.50",
      "unit": "fL",
      "reference_range": null,
      "abnormal": true
    }
  ]
}
2026-08-10 14:45:22,921 INFO     29 [qwen-vl-table] coord grouping: {6: 12, 7: 10, 8: 22}
2026-08-10 14:45:22,924 INFO     29 [qwen-vl-table] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1631578, prompt_len=571
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
谷丙转氨酶、谷草转氨酶、碱性磷酸酶、γ-谷氨酰基转移酶、胆碱脂酶、总胆汁酸、总胆红素、直接胆红素、总蛋白、白蛋白、球蛋白、白球比

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
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord API raw response (len=607):
```json
[
	{"text": "谷丙转氨酶", "bbox": [668, 158, 690, 312]},
	{"text": "谷草转氨酶", "bbox": [639, 158, 661, 312]},
	{"text": "碱性磷酸酶", "bbox": [609, 158, 631, 312]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [578, 158, 600, 368]},
	{"text": "胆碱脂酶", "bbox": [549, 158, 571, 296]},
	{"text": "总胆汁酸", "bbox": [519, 158, 541, 296]},
	{"text": "总胆红素", "bbox": [489, 158, 511, 303]},
	{"text": "直接胆红素", "bbox": [459, 158, 481, 319]},
	{"text": "总蛋白", "bbox": [429, 158, 451, 269]},
	{"text": "白蛋白", "bbox": [400, 158, 422, 277]},
	{"text": "球蛋白", "bbox": [370, 155, 392, 247]},
	{"text": "白球比", "bbox": [340, 155, 362, 231]}
]
```
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord API: raw_items=12, valid_items=12, elapsed=4.2s
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[0]: text=谷丙转氨酶, bbox=[668, 158, 690, 312]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[1]: text=谷草转氨酶, bbox=[639, 158, 661, 312]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[2]: text=碱性磷酸酶, bbox=[609, 158, 631, 312]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[3]: text=γ-谷氨酰基转移酶, bbox=[578, 158, 600, 368]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[4]: text=胆碱脂酶, bbox=[549, 158, 571, 296]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[5]: text=总胆汁酸, bbox=[519, 158, 541, 296]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[6]: text=总胆红素, bbox=[489, 158, 511, 303]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[7]: text=直接胆红素, bbox=[459, 158, 481, 319]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[8]: text=总蛋白, bbox=[429, 158, 451, 269]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[9]: text=白蛋白, bbox=[400, 158, 422, 277]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[10]: text=球蛋白, bbox=[370, 155, 392, 247]
2026-08-10 14:45:27,130 INFO     29 [qwen-vl-table] coord item[11]: text=白球比, bbox=[340, 155, 362, 231]
2026-08-10 14:45:27,131 INFO     29 [qwen-vl-table] page=6 coord: matched 12/12, time=4.2s
2026-08-10 14:45:27,133 INFO     29 [qwen-vl-table] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1617757, prompt_len=560
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
二氧化碳结合力、尿素、肌酐、钾、钠、氯、尿酸、视黄醇结合蛋白、胱抑素-C、中性粒细胞明胶酶相关脂质运载蛋白

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
2026-08-10 14:45:32,228 INFO     29 [qwen-vl-table] coord API raw response (len=508):
```json
[
	{"text": "二氧化碳结合力", "bbox": [684, 155, 708, 300]},
	{"text": "尿素", "bbox": [660, 155, 680, 264]},
	{"text": "肌酐", "bbox": [631, 155, 651, 255]},
	{"text": "钾", "bbox": [604, 155, 623, 223]},
	{"text": "钠", "bbox": [575, 155, 594, 230]},
	{"text": "氯", "bbox": [546, 155, 565, 228]},
	{"text": "尿酸", "bbox": [517, 151, 537, 244]},
	{"text": "视黄醇结合蛋白", "bbox": [488, 148, 508, 286]},
	{"text": "胱抑素-C", "bbox": [459, 147, 479, 252]},
	{"text": "中性粒细胞明胶酶相关脂质运载蛋白", "bbox": [429, 145, 450, 473]}
]
```
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord API: raw_items=10, valid_items=10, elapsed=5.1s
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[0]: text=二氧化碳结合力, bbox=[684, 155, 708, 300]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[1]: text=尿素, bbox=[660, 155, 680, 264]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[2]: text=肌酐, bbox=[631, 155, 651, 255]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[3]: text=钾, bbox=[604, 155, 623, 223]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[4]: text=钠, bbox=[575, 155, 594, 230]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[5]: text=氯, bbox=[546, 155, 565, 228]
2026-08-10 14:45:32,229 INFO     29 [qwen-vl-table] coord item[6]: text=尿酸, bbox=[517, 151, 537, 244]
2026-08-10 14:45:32,230 INFO     29 [qwen-vl-table] coord item[7]: text=视黄醇结合蛋白, bbox=[488, 148, 508, 286]
2026-08-10 14:45:32,230 INFO     29 [qwen-vl-table] coord item[8]: text=胱抑素-C, bbox=[459, 147, 479, 252]
2026-08-10 14:45:32,230 INFO     29 [qwen-vl-table] coord item[9]: text=中性粒细胞明胶酶相关脂质运载蛋白, bbox=[429, 145, 450, 473]
2026-08-10 14:45:32,231 INFO     29 [qwen-vl-table] page=7 coord: matched 10/10, time=5.1s
2026-08-10 14:45:32,238 INFO     29 [qwen-vl-table] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1722451, prompt_len=689
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞比率、淋巴细胞比率、单核细胞比率、嗜酸性粒细胞比率、嗜碱性粒细胞比率、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、红细胞计数、血红蛋白测定、红细胞比积测定、平均红细胞体积、平均红细胞血红蛋白量、平均红细胞血红蛋白浓度、红细胞体积分布宽度、血小板计数、血小板比积、平均血小板体积、血小板体积分布宽度

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
2026-08-10 14:45:39,240 INFO     29 [qwen-vl-table] coord API raw response (len=1275):
[
	{"text": "白细胞计数WBC(8-HR)", "bbox": [734, 127, 757, 265]},
	{"text": "中性粒细胞比率NEU", "bbox": [705, 127, 727, 252]},
	{"text": "淋巴细胞比率LYM", "bbox": [674, 127, 696, 238]},
	{"text": "单核细胞比率MONO", "bbox": [643, 125, 665, 244]},
	{"text": "嗜酸性粒细胞比率EOS", "bbox": [611, 123, 633, 265]},
	{"text": "嗜碱性粒细胞比率BASO", "bbox": [579, 121, 601, 271]},
	{"text": "中性粒细胞绝对值NEU#", "bbox": [547, 120, 569, 271]},
	{"text": "淋巴细胞绝对值LYM#", "bbox": [515, 119, 537, 256]},
	{"text": "单核细胞绝对值MONO#", "bbox": [483, 118, 505, 262]},
	{"text": "嗜酸性粒细胞绝对值EOS#", "bbox": [451, 116, 473, 285]},
	{"text": "嗜碱性粒细胞绝对值BASO#", "bbox": [418, 115, 440, 290]},
	{"text": "红细胞计数RBC(8-HR)", "bbox": [386, 114, 408, 256]},
	{"text": "血红蛋白测定HB(8-HR)", "bbox": [354, 113, 376, 262]},
	{"text": "红细胞比积测定HCT(8-HR)", "bbox": [321, 112, 343, 285]},
	{"text": "平均红细胞体积MCV(8-HR)", "bbox": [734, 570, 756, 742]},
	{"text": "平均红细胞血红蛋白量MCH(8-HR)", "bbox": [702, 570, 724, 828]},
	{"text": "平均红细胞血红蛋白浓度(8-HR)", "bbox": [670, 570, 692, 782]},
	{"text": "红细胞体积分布宽度RDW-CV", "bbox": [638, 570, 660, 755]},
	{"text": "血小板计数PLT(8-HR)", "bbox": [605, 570, 627, 714]},
	{"text": "血小板比积PCT", "bbox": [573, 570, 595, 670]},
	{"text": "平均血小板体积MPV", "bbox": [541, 570, 563, 703]},
	{"text": "血小板体积分布宽度PDW", "bbox": [508, 570, 530, 735]}
]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord API: raw_items=22, valid_items=22, elapsed=7.0s
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数WBC(8-HR), bbox=[734, 127, 757, 265]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞比率NEU, bbox=[705, 127, 727, 252]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞比率LYM, bbox=[674, 127, 696, 238]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞比率MONO, bbox=[643, 125, 665, 244]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞比率EOS, bbox=[611, 123, 633, 265]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞比率BASO, bbox=[579, 121, 601, 271]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对值NEU#, bbox=[547, 120, 569, 271]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对值LYM#, bbox=[515, 119, 537, 256]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞绝对值MONO#, bbox=[483, 118, 505, 262]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对值EOS#, bbox=[451, 116, 473, 285]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对值BASO#, bbox=[418, 115, 440, 290]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数RBC(8-HR), bbox=[386, 114, 408, 256]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白测定HB(8-HR), bbox=[354, 113, 376, 262]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞比积测定HCT(8-HR), bbox=[321, 112, 343, 285]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积MCV(8-HR), bbox=[734, 570, 756, 742]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白量MCH(8-HR), bbox=[702, 570, 724, 828]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度(8-HR), bbox=[670, 570, 692, 782]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞体积分布宽度RDW-CV, bbox=[638, 570, 660, 755]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[18]: text=血小板计数PLT(8-HR), bbox=[605, 570, 627, 714]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[19]: text=血小板比积PCT, bbox=[573, 570, 595, 670]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[20]: text=平均血小板体积MPV, bbox=[541, 570, 563, 703]
2026-08-10 14:45:39,241 INFO     29 [qwen-vl-table] coord item[21]: text=血小板体积分布宽度PDW, bbox=[508, 570, 530, 735]
2026-08-10 14:45:39,247 INFO     29 [qwen-vl-table] page=8 coord: matched 16/22, time=7.0s
2026-08-10 14:45:39,247 INFO     29 [qwen-vl-table] new_positions (44):
[[7, 397.46, 410.54999999999995, 132.878, 262.392], [7, 380.205, 393.29499999999996, 132.878, 262.392], [7, 362.35499999999996, 375.445, 132.878, 262.392], [7, 343.90999999999997, 357.0, 132.878, 309.488], [7, 326.655, 339.745, 132.878, 248.93599999999998], [7, 308.805, 321.895, 132.878, 248.93599999999998], [7, 290.955, 304.04499999999996, 132.878, 254.82299999999998], [7, 273.10499999999996, 286.195, 132.878, 268.279], [7, 255.255, 268.34499999999997, 132.878, 226.22899999999998], [7, 238.0, 251.08999999999997, 132.878, 232.957], [7, 220.14999999999998, 233.23999999999998, 130.355, 207.727], [7, 202.29999999999998, 215.39, 130.355, 194.271], [8, 406.97999999999996, 421.26, 130.355, 252.29999999999998], [8, 392.7, 404.59999999999997, 130.355, 222.024], [8, 375.445, 387.34499999999997, 130.355, 214.45499999999998], [8, 359.38, 370.685, 130.355, 187.543], [8, 342.125, 353.43, 130.355, 193.43], [8, 324.87, 336.175, 130.355, 191.748], [8, 307.615, 319.515, 126.991, 205.20399999999998], [8, 290.36, 302.26, 124.46799999999999, 240.52599999999998], [8, 273.10499999999996, 285.005, 123.627, 211.932], [8, 255.255, 267.75, 121.945, 397.793], [0, 0, 0, 0, 0], [9, 419.47499999999997, 432.565, 106.807, 211.932], [9, 401.03, 414.12, 106.807, 200.158], [9, 382.585, 395.67499999999995, 105.125, 205.20399999999998], [9, 363.54499999999996, 376.635, 103.443, 222.86499999999998], [9, 344.505, 357.59499999999997, 101.761, 227.911], [9, 325.465, 338.555, 100.92, 227.911], [9, 306.425, 319.515, 100.079, 215.296], [9, 287.385, 300.47499999999997, 99.238, 220.34199999999998], [9, 268.34499999999997, 281.435, 97.556, 239.685], [9, 248.70999999999998, 261.8, 96.715, 243.89], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [9, 398.65, 411.74, 479.37, 657.6619999999999], [9, 398.65, 411.74, 479.37, 657.6619999999999], [9, 379.60999999999996, 392.7, 479.37, 634.9549999999999], [0, 0, 0, 0, 0], [9, 340.935, 354.025, 479.37, 563.47], [9, 321.895, 334.98499999999996, 479.37, 591.223], [9, 302.26, 315.34999999999997, 479.37, 618.135]]
2026-08-10 14:45:39,247 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=44, matched=38, pages=3, time=40.6s
2026-08-10 14:45:39,257 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 14:45:39,257 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:LabExam | outputs={"chunks": "1 items, types={'LabReport': 1}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:45:39,257 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 14:45:39,266 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:39,266 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:45:40,086 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:40,097 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 14:45:40,097 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:45:40,097 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 14:45:40,106 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:40,107 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:45:40,635 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:40,648 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 14:45:40,648 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Clinical | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:45:40,648 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 14:45:40,656 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:40,656 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:45:41,338 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:41,344 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 14:45:41,344 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:45:41,344 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 14:45:41,351 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:41,352 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:45:41,768 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:41,774 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 14:45:41,774 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:45:41,774 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 14:45:41,782 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:45:41,783 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:45:41,783 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 14:45:41,783 INFO     29 [qwen-vl-text] positions(45): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:45:41,783 INFO     29 [qwen-vl-text] page grouping: [1, 2], lines per page: [29, 16]
2026-08-10 14:45:42,038 INFO     29 [qwen-vl-text] page=1, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:45:42,218 INFO     29 [qwen-vl-text] page=2, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:45:42,221 INFO     29 [qwen-vl-text] LLM extraction start, text_len=1673
2026-08-10 14:45:42,221 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:42,222 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 28, \"bbox_end\": 72, \"encounter_dates\": [\"2026-01-16\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "24小时内入出院记录\n姓名\n性别：男\n年龄：47岁\n民族：汉族\n出生日期：1978-01-07\n婚姻状况：已婚\n籍贯：\n出生地：\n国籍：\n证件号码：\n工作单位：\n职业：\n详细地址：\n联系电话：\n联系人：\n关系：配偶\n入院日期：2026-01-16 10:19\n病历完成时间：2026-01-16 10:49\n病史陈述者：患者本人\n可靠性：可靠\n是否传染病：否\n既往是否健康：是\n主诉：食管鳞癌术后7年余，肝转移11月余。\n现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。\n入院情况：神志清，精神可，食纳夜休尚可。\n症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。\n症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。\n第1页\n入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后\n4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后\n7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架\n诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐\n酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。\n出院情况：神志清，精神可，食纳夜休尚可。\n出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后\n4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后\n7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架\n出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉\n奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我\n科随诊。\n接诊医师签名：\n住院医师签名：\n主治医师签名：\n主（副主）任医师签名：",
    "role": "user"
  }
]
2026-08-10 14:45:44,275 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:45:44.272+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:45:50,677 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:45:50,677 INFO     29 [qwen-vl-text] LLM output (len=2377):
{
  "encounter_date": "2026-01-16",
  "admission_date": "2026-01-16",
  "discharge_date": "2026-01-16",
  "hospital_days": 1,
  "department": null,
  "bed_number": null,
  "admission_condition": "神志清，精神可，食纳夜休尚可。症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。",
  "admission_diagnoses": [
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "食管恶性肿瘤(rTxNxM1 IV期)术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "多部位淋巴结继发恶性肿瘤(肝门区、腹膜后)",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤放射治疗后",
      "diagnosis_type": "西医"
    },
    {
      "name": "左侧肾积水伴输尿管狭窄",
      "diagnosis_type": "西医"
    },
    {
      "name": "左侧输尿管支架置入术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "更换输尿管支架",
      "diagnosis_type": "西医"
    }
  ],
  "treatment_summary": "预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。",
  "auxiliary_exams": "血常规：血红蛋白测定99g/L。",
  "imaging_findings": null,
  "discharge_diagnoses": [
    {
      "name": "姑息性化疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤免疫治疗",
      "diagnosis_type": "西医"
    },
    {
      "name": "食管恶性肿瘤(rTxNxM1 IV期)术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "肝继发恶性肿瘤",
      "diagnosis_type": "西医"
    },
    {
      "name": "多部位淋巴结继发恶性肿瘤(肝门区、腹膜后)",
      "diagnosis_type": "西医"
    },
    {
      "name": "恶性肿瘤放射治疗后",
      "diagnosis_type": "西医"
    },
    {
      "name": "左侧肾积水伴输尿管狭窄",
      "diagnosis_type": "西医"
    },
    {
      "name": "左侧输尿管支架置入术后",
      "diagnosis_type": "西医"
    },
    {
      "name": "更换输尿管支架",
      "diagnosis_type": "西医"
    }
  ],
  "condition_at_discharge": "神志清，精神可，食纳夜休尚可。",
  "outcome": null,
  "discharge_orders": "1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我科随诊。",
  "do_medications": [
    "替吉奥胶囊 60mg 口服 一日二次"
  ],
  "do_follow_up": "按时返院行下周期治疗，若有不适，我科随诊。",
  "do_precautions": [
    "注意休息，避免劳累和感染，注意有无腹泻",
    "每周监测血常规"
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
2026-08-10 14:45:50,677 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-01-16]
2026-08-10 14:45:50,681 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2171272, prompt_len=1876
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["24小时内入出院记录", "姓名", "性别：男", "年龄：47岁", "民族：汉族", "出生日期：1978-01-07", "婚姻状况：已婚", "籍贯：", "出生地：", "国籍：", "证件号码：", "工作单位：", "职业：", "详细地址：", "联系电话：", "联系人：", "关系：配偶", "入院日期：2026-01-16 10:19", "病历完成时间：2026-01-16 10:49", "病史陈述者：患者本人", "可靠性：可靠", "是否传染病：否", "既往是否健康：是", "主诉：食管鳞癌术后7年余，肝转移11月余。", "现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。", "入院情况：神志清，精神可，食纳夜休尚可。", "症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。", "症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。", "第1页"]

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
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord API raw response (len=2439):
[
	{"text": "24小时内入出院记录", "bbox": [407, 60, 650, 98]},
	{"text": "姓名", "bbox": [89, 80, 115, 98]},
	{"text": "性别：男", "bbox": [535, 107, 652, 131]},
	{"text": "年龄：47岁", "bbox": [89, 107, 254, 131]},
	{"text": "民族：汉族", "bbox": [535, 136, 670, 158]},
	{"text": "出生日期：1978-01-07", "bbox": [89, 135, 323, 159]},
	{"text": "婚姻状况：已婚", "bbox": [530, 159, 668, 183]},
	{"text": "籍贯：", "bbox": [89, 163, 193, 186]},
	{"text": "出生地：", "bbox": [528, 186, 614, 208]},
	{"text": "国籍：", "bbox": [89, 190, 190, 213]},
	{"text": "证件号码：", "bbox": [526, 212, 614, 233]},
	{"text": "工作单位：", "bbox": [89, 219, 193, 241]},
	{"text": "职业：", "bbox": [524, 238, 614, 259]},
	{"text": "详细地址：", "bbox": [89, 247, 193, 269]},
	{"text": "联系电话：", "bbox": [494, 262, 611, 283]},
	{"text": "联系人：", "bbox": [87, 297, 168, 318]},
	{"text": "关系：配偶", "bbox": [520, 308, 660, 328]},
	{"text": "入院日期：2026-01-16 10:19", "bbox": [87, 327, 378, 347]},
	{"text": "病历完成时间：2026-01-16 10:49", "bbox": [519, 334, 821, 354]},
	{"text": "病史陈述者：患者本人", "bbox": [85, 354, 312, 373]},
	{"text": "可靠性：可靠", "bbox": [518, 358, 660, 377]},
	{"text": "是否传染病：否", "bbox": [85, 380, 245, 399]},
	{"text": "既往是否健康：是", "bbox": [517, 382, 679, 402]},
	{"text": "主诉：食管鳞癌术后7年余，肝转移11月余。", "bbox": [125, 413, 569, 432]},
	{"text": "现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。", "bbox": [73, 434, 924, 821]},
	{"text": "入院情况：神志清，精神可，食纳夜休尚可。", "bbox": [118, 823, 528, 841]},
	{"text": "症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。", "bbox": [118, 842, 610, 860]},
	{"text": "症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。", "bbox": [118, 860, 610, 878]},
	{"text": "第1页", "bbox": [454, 880, 537, 898]}
]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=15.5s
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[0]: text=24小时内入出院记录, bbox=[407, 60, 650, 98]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[1]: text=姓名, bbox=[89, 80, 115, 98]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[2]: text=性别：男, bbox=[535, 107, 652, 131]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[3]: text=年龄：47岁, bbox=[89, 107, 254, 131]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[4]: text=民族：汉族, bbox=[535, 136, 670, 158]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[5]: text=出生日期：1978-01-07, bbox=[89, 135, 323, 159]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[6]: text=婚姻状况：已婚, bbox=[530, 159, 668, 183]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[7]: text=籍贯：, bbox=[89, 163, 193, 186]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[8]: text=出生地：, bbox=[528, 186, 614, 208]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[9]: text=国籍：, bbox=[89, 190, 190, 213]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[10]: text=证件号码：, bbox=[526, 212, 614, 233]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[11]: text=工作单位：, bbox=[89, 219, 193, 241]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[12]: text=职业：, bbox=[524, 238, 614, 259]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[13]: text=详细地址：, bbox=[89, 247, 193, 269]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[14]: text=联系电话：, bbox=[494, 262, 611, 283]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[15]: text=联系人：, bbox=[87, 297, 168, 318]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[16]: text=关系：配偶, bbox=[520, 308, 660, 328]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[17]: text=入院日期：2026-01-16 10:19, bbox=[87, 327, 378, 347]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[18]: text=病历完成时间：2026-01-16 10:49, bbox=[519, 334, 821, 354]
2026-08-10 14:46:06,133 INFO     29 [qwen-vl-text] coord item[19]: text=病史陈述者：患者本人, bbox=[85, 354, 312, 373]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[20]: text=可靠性：可靠, bbox=[518, 358, 660, 377]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[21]: text=是否传染病：否, bbox=[85, 380, 245, 399]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[22]: text=既往是否健康：是, bbox=[517, 382, 679, 402]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[23]: text=主诉：食管鳞癌术后7年余，肝转移11月余。, bbox=[125, 413, 569, 432]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[24]: text=现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。, bbox=[73, 434, 924, 821]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[25]: text=入院情况：神志清，精神可，食纳夜休尚可。, bbox=[118, 823, 528, 841]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[26]: text=症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。, bbox=[118, 842, 610, 860]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[27]: text=症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。, bbox=[118, 860, 610, 878]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] coord item[28]: text=第1页, bbox=[454, 880, 537, 898]
2026-08-10 14:46:06,134 INFO     29 [qwen-vl-text] page=1 — 29/29 coords, api_time=15.5s
2026-08-10 14:46:06,136 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1048035, prompt_len=1157
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共16行）
["入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐", "酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。", "出院情况：神志清，精神可，食纳夜休尚可。", "出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉", "奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我", "科随诊。", "接诊医师签名：", "住院医师签名：", "主治医师签名：", "主（副主）任医师签名："]

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
2026-08-10 14:46:13,135 INFO     29 [qwen-vl-text] coord API raw response (len=1190):
[
	{"text": "入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "bbox": [85, 65, 930, 115]},
	{"text": "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "bbox": [85, 87, 930, 135]},
	{"text": "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "bbox": [95, 105, 796, 151]},
	{"text": "诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐", "bbox": [85, 125, 930, 172]},
	{"text": "酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。", "bbox": [85, 145, 909, 191]},
	{"text": "出院情况：神志清，精神可，食纳夜休尚可。", "bbox": [134, 169, 552, 204]},
	{"text": "出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后", "bbox": [85, 189, 930, 234]},
	{"text": "4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后", "bbox": [85, 209, 930, 254]},
	{"text": "7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架", "bbox": [95, 230, 792, 270]},
	{"text": "出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉", "bbox": [85, 251, 930, 291]},
	{"text": "奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我", "bbox": [85, 271, 930, 311]},
	{"text": "科随诊。", "bbox": [85, 294, 168, 316]},
	{"text": "接诊医师签名：", "bbox": [489, 345, 619, 364]},
	{"text": "住院医师签名：", "bbox": [489, 370, 619, 389]},
	{"text": "主治医师签名：", "bbox": [489, 396, 619, 415]},
	{"text": "主（副主）任医师签名：", "bbox": [408, 420, 619, 439]}
]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord API: raw_items=16, valid_items=16, elapsed=7.0s
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[0]: text=入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后, bbox=[85, 65, 930, 115]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[1]: text=4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后, bbox=[85, 87, 930, 135]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[2]: text=7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架, bbox=[95, 105, 796, 151]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[3]: text=诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐, bbox=[85, 125, 930, 172]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[4]: text=酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。, bbox=[85, 145, 909, 191]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[5]: text=出院情况：神志清，精神可，食纳夜休尚可。, bbox=[134, 169, 552, 204]
2026-08-10 14:46:13,136 INFO     29 [qwen-vl-text] coord item[6]: text=出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后, bbox=[85, 189, 930, 234]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[7]: text=4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后, bbox=[85, 209, 930, 254]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[8]: text=7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架, bbox=[95, 230, 792, 270]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[9]: text=出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉, bbox=[85, 251, 930, 291]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[10]: text=奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我, bbox=[85, 271, 930, 311]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[11]: text=科随诊。, bbox=[85, 294, 168, 316]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[12]: text=接诊医师签名：, bbox=[489, 345, 619, 364]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[13]: text=住院医师签名：, bbox=[489, 370, 619, 389]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[14]: text=主治医师签名：, bbox=[489, 396, 619, 415]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] coord item[15]: text=主（副主）任医师签名：, bbox=[408, 420, 619, 439]
2026-08-10 14:46:13,137 INFO     29 [qwen-vl-text] page=2 — 16/16 coords, api_time=7.0s
2026-08-10 14:46:13,138 INFO     29 [qwen-vl-text] new_positions (45):
[[1, 242.165, 386.75, 50.46, 82.41799999999999], [1, 52.955, 68.425, 67.28, 82.41799999999999], [1, 318.325, 387.94, 89.987, 110.17099999999999], [1, 52.955, 151.13, 89.987, 110.17099999999999], [1, 318.325, 398.65, 114.37599999999999, 132.878], [1, 52.955, 192.185, 113.535, 133.719], [1, 315.34999999999997, 397.46, 133.719, 153.903], [1, 52.955, 114.835, 137.083, 156.426], [1, 314.15999999999997, 365.33, 156.426, 174.928], [1, 52.955, 113.05, 159.79, 179.13299999999998], [1, 312.96999999999997, 365.33, 178.292, 195.953], [1, 52.955, 114.835, 184.179, 202.68099999999998], [1, 311.78, 365.33, 200.158, 217.819], [1, 52.955, 114.835, 207.727, 226.22899999999998], [1, 293.93, 363.54499999999996, 220.34199999999998, 238.003], [1, 51.765, 99.96, 249.777, 267.438], [1, 309.4, 392.7, 259.02799999999996, 275.848], [1, 51.765, 224.91, 275.007, 291.827], [1, 308.805, 488.495, 280.894, 297.714], [1, 50.574999999999996, 185.64, 297.714, 313.693], [1, 308.21, 392.7, 301.078, 317.057], [1, 50.574999999999996, 145.775, 319.58, 335.55899999999997], [1, 307.615, 404.005, 321.262, 338.082], [1, 74.375, 338.555, 347.33299999999997, 363.312], [1, 43.434999999999995, 549.78, 364.99399999999997, 690.461], [1, 70.21, 314.15999999999997, 692.143, 707.281], [1, 70.21, 362.95, 708.122, 723.26], [1, 70.21, 362.95, 723.26, 738.398], [1, 270.13, 319.515, 740.0799999999999, 755.218], [2, 50.574999999999996, 553.35, 54.665, 96.715], [2, 50.574999999999996, 553.35, 73.167, 113.535], [2, 56.525, 473.62, 88.30499999999999, 126.991], [2, 50.574999999999996, 553.35, 105.125, 144.652], [2, 50.574999999999996, 540.855, 121.945, 160.631], [2, 79.72999999999999, 328.44, 142.129, 171.564], [2, 50.574999999999996, 553.35, 158.94899999999998, 196.79399999999998], [2, 50.574999999999996, 553.35, 175.769, 213.614], [2, 56.525, 471.23999999999995, 193.43, 227.07], [2, 50.574999999999996, 553.35, 211.09099999999998, 244.731], [2, 50.574999999999996, 553.35, 227.911, 261.551], [2, 50.574999999999996, 99.96, 247.254, 265.756], [2, 290.955, 368.305, 290.145, 306.12399999999997], [2, 290.955, 368.305, 311.17, 327.149], [2, 290.955, 368.305, 333.036, 349.015], [2, 242.76, 368.305, 353.21999999999997, 369.199]]
2026-08-10 14:46:13,138 INFO     29 [qwen-vl-text] ═══ DONE ═══ 45 positions, pages=2, time=31.4s
2026-08-10 14:46:13,159 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 14:46:13,160 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:46:13,160 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 14:46:13,168 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:13,168 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:46:14,130 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:14,143 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 14:46:14,143 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:46:14,143 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 14:46:14,152 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:46:14,152 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:46:14,152 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:46:14,153 INFO     29 [qwen-vl-text] positions(28): [[0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0], [0, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:46:14,153 INFO     29 [qwen-vl-text] page grouping: [0], lines per page: [28]
2026-08-10 14:46:14,428 INFO     29 [qwen-vl-text] page=0, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:46:14,430 INFO     29 [qwen-vl-text] LLM extraction start, text_len=431
2026-08-10 14:46:14,430 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:14,432 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 0, \"bbox_end\": 27, \"encounter_dates\": [\"2018-01-27\"], \"department\": \"普外科\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "华阴市人民医院\n病理检查报告单\n姓名：\n性别：男\n年龄：39\n病理号：2018-0079\n送检单位：本院\n科别：普外科\n住院号：1800732\n床号：25\n送检日期：2018-01-27\n送检医师：韩晔\n送检材料：食管\n临床诊断：\n肉眼所见：\n送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管\n端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c\n，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，\nV6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，\n径0.8cm；另送第五组淋巴结，灰红色两块。\n光镜所见：\n病理诊断：\n食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润\n第五组淋巴结（1/1枚）可见癌转移\n食管周淋巴结（5枚）未见癌组织\n另送上下切缘未见癌组织\n上、下切缘未见癌组织\n纤维脂肪组织内未见癌组织",
    "role": "user"
  }
]
2026-08-10 14:46:15,873 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:46:15.872+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:46:17,585 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:17,586 INFO     29 [qwen-vl-text] LLM output (len=622):
{
  "exam_date": "2018-01-27",
  "report_date": null,
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "食管",
  "patient_name": null,
  "patient_gender": "男",
  "department": "普外科",
  "bed_number": "25",
  "findings": "肉眼所见：\n送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管\n端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c\n，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，\nV6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，\n径0.8cm；另送第五组淋巴结，灰红色两块。",
  "conclusion": "病理诊断：\n食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润\n第五组淋巴结（1/1枚）可见癌转移\n食管周淋巴结（5枚）未见癌组织\n另送上下切缘未见癌组织\n上、下切缘未见癌组织\n纤维脂肪组织内未见癌组织",
  "physician": null,
  "reviewer": null
}
2026-08-10 14:46:17,594 INFO     29 [qwen-vl-text] coord API call start, page=0, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=2303418, prompt_len=1128
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共28行）
["华阴市人民医院", "病理检查报告单", "姓名：", "性别：男", "年龄：39", "病理号：2018-0079", "送检单位：本院", "科别：普外科", "住院号：1800732", "床号：25", "送检日期：2018-01-27", "送检医师：韩晔", "送检材料：食管", "临床诊断：", "肉眼所见：", "送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管", "端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c", "，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，", "V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，", "径0.8cm；另送第五组淋巴结，灰红色两块。", "光镜所见：", "病理诊断：", "食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润", "第五组淋巴结（1/1枚）可见癌转移", "食管周淋巴结（5枚）未见癌组织", "另送上下切缘未见癌组织", "上、下切缘未见癌组织", "纤维脂肪组织内未见癌组织"]

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
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord API raw response (len=1665):
[
	{"text": "华阴市人民医院", "bbox": [362, 97, 750, 141]},
	{"text": "病理检查报告单", "bbox": [430, 134, 696, 170]},
	{"text": "姓名：", "bbox": [140, 161, 195, 180]},
	{"text": "性别：男", "bbox": [360, 168, 454, 190]},
	{"text": "年龄：39", "bbox": [557, 181, 647, 200]},
	{"text": "病理号：2018-0079", "bbox": [771, 185, 971, 202]},
	{"text": "送检单位：本院", "bbox": [137, 190, 300, 212]},
	{"text": "科别：普外科", "bbox": [359, 195, 492, 220]},
	{"text": "住院号：1800732", "bbox": [555, 207, 714, 227]},
	{"text": "床号：25", "bbox": [771, 208, 890, 225]},
	{"text": "送检日期：2018-01-27", "bbox": [136, 216, 360, 240]},
	{"text": "送检医师：韩晔", "bbox": [771, 234, 932, 252]},
	{"text": "送检材料：食管", "bbox": [134, 247, 304, 269]},
	{"text": "临床诊断：", "bbox": [554, 263, 646, 281]},
	{"text": "肉眼所见：", "bbox": [126, 272, 227, 291]},
	{"text": "送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管", "bbox": [171, 302, 995, 338]},
	{"text": "端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c", "bbox": [171, 321, 995, 356]},
	{"text": "，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，", "bbox": [171, 339, 995, 373]},
	{"text": "V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，", "bbox": [170, 357, 995, 390]},
	{"text": "径0.8cm；另送第五组淋巴结，灰红色两块。", "bbox": [170, 375, 588, 400]},
	{"text": "光镜所见：", "bbox": [123, 398, 225, 416]},
	{"text": "病理诊断：", "bbox": [112, 791, 239, 816]},
	{"text": "食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润", "bbox": [164, 794, 720, 833]},
	{"text": "第五组淋巴结（1/1枚）可见癌转移", "bbox": [164, 820, 584, 855]},
	{"text": "食管周淋巴结（5枚）未见癌组织", "bbox": [164, 843, 558, 877]},
	{"text": "另送上下切缘未见癌组织", "bbox": [164, 868, 468, 900]},
	{"text": "上、下切缘未见癌组织", "bbox": [164, 891, 442, 921]},
	{"text": "纤维脂肪组织内未见癌组织", "bbox": [164, 911, 495, 944]}
]
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord API: raw_items=28, valid_items=28, elapsed=9.5s
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord item[0]: text=华阴市人民医院, bbox=[362, 97, 750, 141]
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord item[1]: text=病理检查报告单, bbox=[430, 134, 696, 170]
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord item[2]: text=姓名：, bbox=[140, 161, 195, 180]
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord item[3]: text=性别：男, bbox=[360, 168, 454, 190]
2026-08-10 14:46:27,052 INFO     29 [qwen-vl-text] coord item[4]: text=年龄：39, bbox=[557, 181, 647, 200]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[5]: text=病理号：2018-0079, bbox=[771, 185, 971, 202]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[6]: text=送检单位：本院, bbox=[137, 190, 300, 212]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[7]: text=科别：普外科, bbox=[359, 195, 492, 220]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：1800732, bbox=[555, 207, 714, 227]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[9]: text=床号：25, bbox=[771, 208, 890, 225]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[10]: text=送检日期：2018-01-27, bbox=[136, 216, 360, 240]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[11]: text=送检医师：韩晔, bbox=[771, 234, 932, 252]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[12]: text=送检材料：食管, bbox=[134, 247, 304, 269]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[13]: text=临床诊断：, bbox=[554, 263, 646, 281]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[14]: text=肉眼所见：, bbox=[126, 272, 227, 291]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[15]: text=送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管, bbox=[171, 302, 995, 338]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[16]: text=端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c, bbox=[171, 321, 995, 356]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[17]: text=，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，, bbox=[171, 339, 995, 373]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[18]: text=V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，, bbox=[170, 357, 995, 390]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[19]: text=径0.8cm；另送第五组淋巴结，灰红色两块。, bbox=[170, 375, 588, 400]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[20]: text=光镜所见：, bbox=[123, 398, 225, 416]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[21]: text=病理诊断：, bbox=[112, 791, 239, 816]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[22]: text=食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润, bbox=[164, 794, 720, 833]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[23]: text=第五组淋巴结（1/1枚）可见癌转移, bbox=[164, 820, 584, 855]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[24]: text=食管周淋巴结（5枚）未见癌组织, bbox=[164, 843, 558, 877]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[25]: text=另送上下切缘未见癌组织, bbox=[164, 868, 468, 900]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[26]: text=上、下切缘未见癌组织, bbox=[164, 891, 442, 921]
2026-08-10 14:46:27,053 INFO     29 [qwen-vl-text] coord item[27]: text=纤维脂肪组织内未见癌组织, bbox=[164, 911, 495, 944]
2026-08-10 14:46:27,054 INFO     29 [qwen-vl-text] page=0 — 28/28 coords, api_time=9.5s
2026-08-10 14:46:27,054 INFO     29 [qwen-vl-text] new_positions (28):
[[0, 215.39, 446.25, 81.577, 118.58099999999999], [0, 255.85, 414.12, 112.694, 142.97], [0, 83.3, 116.02499999999999, 135.40099999999998, 151.38], [0, 214.2, 270.13, 141.28799999999998, 159.79], [0, 331.41499999999996, 384.965, 152.221, 168.2], [0, 458.745, 577.745, 155.585, 169.882], [0, 81.515, 178.5, 159.79, 178.292], [0, 213.605, 292.74, 163.995, 185.01999999999998], [0, 330.22499999999997, 424.83, 174.087, 190.90699999999998], [0, 458.745, 529.55, 174.928, 189.225], [0, 80.92, 214.2, 181.656, 201.84], [0, 458.745, 554.54, 196.79399999999998, 211.932], [0, 79.72999999999999, 180.88, 207.727, 226.22899999999998], [0, 329.63, 384.37, 221.183, 236.321], [0, 74.97, 135.065, 228.75199999999998, 244.731], [0, 101.74499999999999, 592.025, 253.982, 284.258], [0, 101.74499999999999, 592.025, 269.961, 299.396], [0, 101.74499999999999, 592.025, 285.099, 313.693], [0, 101.14999999999999, 592.025, 300.23699999999997, 327.99], [0, 101.14999999999999, 349.85999999999996, 315.375, 336.4], [0, 73.185, 133.875, 334.71799999999996, 349.856], [0, 66.64, 142.20499999999998, 665.231, 686.256], [0, 97.58, 428.4, 667.754, 700.553], [0, 97.58, 347.47999999999996, 689.62, 719.055], [0, 97.58, 332.01, 708.963, 737.557], [0, 97.58, 278.46, 729.9879999999999, 756.9], [0, 97.58, 262.99, 749.331, 774.5609999999999], [0, 97.58, 294.525, 766.151, 793.904]]
2026-08-10 14:46:27,054 INFO     29 [qwen-vl-text] ═══ DONE ═══ 28 positions, pages=1, time=12.9s
2026-08-10 14:46:27,054 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:46:27,055 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:46:27,055 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:46:27,055 INFO     29 [qwen-vl-text] positions(40): [[2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:46:27,055 INFO     29 [qwen-vl-text] page grouping: [2, 3], lines per page: [1, 39]
2026-08-10 14:46:27,230 INFO     29 [qwen-vl-text] page=2, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:46:27,454 INFO     29 [qwen-vl-text] page=3, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:46:27,455 INFO     29 [qwen-vl-text] LLM extraction start, text_len=859
2026-08-10 14:46:27,455 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:27,455 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 73, \"bbox_end\": 112, \"encounter_dates\": [\"2025-12-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "第 2 页\n姓名\n性别 男\n年龄 47 岁 住院号\n床号 231.2+13\n送检科\n检查日期 2025-12-05 15:02:38\n检查项目\n胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成\n像,上腹部(肝胆胰脾)CT增强扫描\n影像学表现\n原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不\n均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,\n肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及\n大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝\n右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,\n壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态\n正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,\n未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描\n呈轻度不均匀强化。\n影像学意见\n胸部CT增强+薄层示:\n1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃\n镜检查;\n2、双肺散在渗出及纤维灶,较前增多;\n3、原\"左肺上叶小结节影\"未见显示;\n4、双侧尖部胸膜局部增厚;\n5、左侧部分肋骨形态欠规则,必要时ECT检查。\n上下腹部CT增强示:\n1、肝内多发异常强化影,考虑肝转移;\n2、双肾多发囊肿;\n3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;\n4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;\n5、左肾周渗出性改变。\n本报告仅供临床参考,签字有效。\n报告医师 郭田田\n审核医师 寇明清\n标有(陕HR)的项目为互认项目\n寇明清",
    "role": "user"
  }
]
2026-08-10 14:46:34,680 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:34,680 INFO     29 [qwen-vl-text] LLM output (len=1045):
{
  "exam_date": "2025-12-05",
  "report_date": null,
  "exam_name": "胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成像,上腹部(肝胆胰脾)CT增强扫描",
  "exam_category": "imaging",
  "body_part": "胸部,下腹部,上腹部(肝胆胰脾)",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "231.2+13",
  "findings": "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描呈轻度不均匀强化。",
  "conclusion": "胸部CT增强+薄层示:\n1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃镜检查;\n2、双肺散在渗出及纤维灶,较前增多;\n3、原\"左肺上叶小结节影\"未见显示;\n4、双侧尖部胸膜局部增厚;\n5、左侧部分肋骨形态欠规则,必要时ECT检查。\n上下腹部CT增强示:\n1、肝内多发异常强化影,考虑肝转移;\n2、双肾多发囊肿;\n3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;\n4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;\n5、左肾周渗出性改变。",
  "physician": "郭田田",
  "reviewer": "寇明清"
}
2026-08-10 14:46:34,685 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1048035, prompt_len=620
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["第 2 页"]

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
2026-08-10 14:46:35,368 INFO     29 [qwen-vl-text] coord API raw response (len=64):
```json
[
	{"text": "第 2 页", "bbox": [470, 872, 550, 888]}
]
```
2026-08-10 14:46:35,368 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 14:46:35,368 INFO     29 [qwen-vl-text] coord item[0]: text=第 2 页, bbox=[470, 872, 550, 888]
2026-08-10 14:46:35,368 INFO     29 [qwen-vl-text] page=2 — 1/1 coords, api_time=0.7s
2026-08-10 14:46:35,371 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1697957, prompt_len=1589
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共39行）
["姓名", "性别 男", "年龄 47 岁 住院号", "床号 231.2+13", "送检科", "检查日期 2025-12-05 15:02:38", "检查项目", "胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成", "像,上腹部(肝胆胰脾)CT增强扫描", "影像学表现", "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "呈轻度不均匀强化。", "影像学意见", "胸部CT增强+薄层示:", "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃", "镜检查;", "2、双肺散在渗出及纤维灶,较前增多;", "3、原\"左肺上叶小结节影\"未见显示;", "4、双侧尖部胸膜局部增厚;", "5、左侧部分肋骨形态欠规则,必要时ECT检查。", "上下腹部CT增强示:", "1、肝内多发异常强化影,考虑肝转移;", "2、双肾多发囊肿;", "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;", "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;", "5、左肾周渗出性改变。", "本报告仅供临床参考,签字有效。", "报告医师 郭田田", "审核医师 寇明清", "标有(陕HR)的项目为互认项目", "寇明清"]

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
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord API raw response (len=2548):
[
	{"text": "姓名", "bbox": [90, 123, 137, 140]},
	{"text": "性别 男", "bbox": [273, 127, 351, 145]},
	{"text": "年龄 47 岁 住院号", "bbox": [409, 131, 605, 150]},
	{"text": "床号 231.2+13", "bbox": [772, 136, 910, 153]},
	{"text": "送检科", "bbox": [90, 149, 187, 167]},
	{"text": "检查日期 2025-12-05 15:02:38", "bbox": [377, 156, 690, 176]},
	{"text": "检查项目", "bbox": [84, 183, 162, 198]},
	{"text": "胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成", "bbox": [84, 201, 905, 225]},
	{"text": "像,上腹部(肝胆胰脾)CT增强扫描", "bbox": [84, 219, 368, 237]},
	{"text": "影像学表现", "bbox": [84, 255, 201, 272]},
	{"text": "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "bbox": [124, 276, 909, 294]},
	{"text": "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "bbox": [84, 293, 898, 312]},
	{"text": "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "bbox": [84, 310, 907, 329]},
	{"text": "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "bbox": [84, 328, 715, 345]},
	{"text": "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "bbox": [124, 346, 907, 364]},
	{"text": "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "bbox": [84, 363, 895, 381]},
	{"text": "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "bbox": [84, 380, 905, 398]},
	{"text": "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "bbox": [84, 397, 903, 415]},
	{"text": "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "bbox": [84, 414, 903, 432]},
	{"text": "呈轻度不均匀强化。", "bbox": [84, 431, 250, 448]},
	{"text": "影像学意见", "bbox": [84, 498, 199, 515]},
	{"text": "胸部CT增强+薄层示:", "bbox": [84, 516, 256, 533]},
	{"text": "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前（2021-06-23）壁厚程度略加重,建议胃", "bbox": [84, 532, 908, 550]},
	{"text": "镜检查;", "bbox": [84, 550, 151, 567]},
	{"text": "2、双肺散在渗出及纤维灶,较前增多;", "bbox": [84, 566, 406, 584]},
	{"text": "3、原\"左肺上叶小结节影\"未见显示;", "bbox": [84, 583, 387, 600]},
	{"text": "4、双侧尖部胸膜局部增厚;", "bbox": [84, 600, 312, 617]},
	{"text": "5、左侧部分肋骨形态欠规则,必要时ECT检查。", "bbox": [84, 615, 470, 633]},
	{"text": "上下腹部CT增强示:", "bbox": [88, 634, 246, 650]},
	{"text": "1、肝内多发异常强化影,考虑肝转移;", "bbox": [88, 649, 404, 667]},
	{"text": "2、双肾多发囊肿;", "bbox": [88, 666, 237, 683]},
	{"text": "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;", "bbox": [88, 680, 521, 698]},
	{"text": "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;", "bbox": [88, 696, 512, 714]},
	{"text": "5、左肾周渗出性改变。", "bbox": [88, 713, 276, 730]},
	{"text": "本报告仅供临床参考,签字有效。", "bbox": [95, 807, 340, 827]},
	{"text": "报告医师 郭田田", "bbox": [417, 802, 576, 818]},
	{"text": "审核医师 寇明清", "bbox": [608, 803, 769, 819]},
	{"text": "标有(陕HR)的项目为互认项目", "bbox": [95, 824, 315, 843]},
	{"text": "寇明清", "bbox": [769, 807, 893, 850]}
]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord API: raw_items=39, valid_items=39, elapsed=13.5s
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[0]: text=姓名, bbox=[90, 123, 137, 140]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[1]: text=性别 男, bbox=[273, 127, 351, 145]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[2]: text=年龄 47 岁 住院号, bbox=[409, 131, 605, 150]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[3]: text=床号 231.2+13, bbox=[772, 136, 910, 153]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[4]: text=送检科, bbox=[90, 149, 187, 167]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[5]: text=检查日期 2025-12-05 15:02:38, bbox=[377, 156, 690, 176]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[6]: text=检查项目, bbox=[84, 183, 162, 198]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[7]: text=胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成, bbox=[84, 201, 905, 225]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[8]: text=像,上腹部(肝胆胰脾)CT增强扫描, bbox=[84, 219, 368, 237]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[9]: text=影像学表现, bbox=[84, 255, 201, 272]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[10]: text=原系"食管CA术后"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不, bbox=[124, 276, 909, 294]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[11]: text=均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,, bbox=[84, 293, 898, 312]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[12]: text=肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及, bbox=[84, 310, 907, 329]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[13]: text=大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。, bbox=[84, 328, 715, 345]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[14]: text=肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝, bbox=[124, 346, 907, 364]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[15]: text=右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,, bbox=[84, 363, 895, 381]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[16]: text=壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态, bbox=[84, 380, 905, 398]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[17]: text=正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,, bbox=[84, 397, 903, 415]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[18]: text=未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描, bbox=[84, 414, 903, 432]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[19]: text=呈轻度不均匀强化。, bbox=[84, 431, 250, 448]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[20]: text=影像学意见, bbox=[84, 498, 199, 515]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[21]: text=胸部CT增强+薄层示:, bbox=[84, 516, 256, 533]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[22]: text=1、原系"食管CA术后"改变,吻合口壁增厚并异常强化,较前（2021-06-23）壁厚程度略加重,建议胃, bbox=[84, 532, 908, 550]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[23]: text=镜检查;, bbox=[84, 550, 151, 567]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[24]: text=2、双肺散在渗出及纤维灶,较前增多;, bbox=[84, 566, 406, 584]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[25]: text=3、原"左肺上叶小结节影"未见显示;, bbox=[84, 583, 387, 600]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[26]: text=4、双侧尖部胸膜局部增厚;, bbox=[84, 600, 312, 617]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[27]: text=5、左侧部分肋骨形态欠规则,必要时ECT检查。, bbox=[84, 615, 470, 633]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[28]: text=上下腹部CT增强示:, bbox=[88, 634, 246, 650]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[29]: text=1、肝内多发异常强化影,考虑肝转移;, bbox=[88, 649, 404, 667]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[30]: text=2、双肾多发囊肿;, bbox=[88, 666, 237, 683]
2026-08-10 14:46:48,870 INFO     29 [qwen-vl-text] coord item[31]: text=3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;, bbox=[88, 680, 521, 698]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[32]: text=4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;, bbox=[88, 696, 512, 714]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[33]: text=5、左肾周渗出性改变。, bbox=[88, 713, 276, 730]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[34]: text=本报告仅供临床参考,签字有效。, bbox=[95, 807, 340, 827]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[35]: text=报告医师 郭田田, bbox=[417, 802, 576, 818]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[36]: text=审核医师 寇明清, bbox=[608, 803, 769, 819]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[37]: text=标有(陕HR)的项目为互认项目, bbox=[95, 824, 315, 843]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] coord item[38]: text=寇明清, bbox=[769, 807, 893, 850]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] page=3 — 39/39 coords, api_time=13.5s
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] new_positions (40):
[[2, 279.65, 327.25, 733.352, 746.808], [3, 53.55, 81.515, 103.443, 117.74], [3, 162.435, 208.845, 106.807, 121.945], [3, 243.355, 359.97499999999997, 110.17099999999999, 126.14999999999999], [3, 459.34, 541.4499999999999, 114.37599999999999, 128.673], [3, 53.55, 111.265, 125.309, 140.447], [3, 224.315, 410.54999999999995, 131.196, 148.016], [3, 49.98, 96.39, 153.903, 166.518], [3, 49.98, 538.475, 169.041, 189.225], [3, 49.98, 218.95999999999998, 184.179, 199.31699999999998], [3, 49.98, 119.595, 214.45499999999998, 228.75199999999998], [3, 73.78, 540.855, 232.11599999999999, 247.254], [3, 49.98, 534.31, 246.41299999999998, 262.392], [3, 49.98, 539.665, 260.71, 276.68899999999996], [3, 49.98, 425.42499999999995, 275.848, 290.145], [3, 73.78, 539.665, 290.986, 306.12399999999997], [3, 49.98, 532.525, 305.283, 320.421], [3, 49.98, 538.475, 319.58, 334.71799999999996], [3, 49.98, 537.285, 333.877, 349.015], [3, 49.98, 537.285, 348.174, 363.312], [3, 49.98, 148.75, 362.471, 376.768], [3, 49.98, 118.405, 418.818, 433.115], [3, 49.98, 152.32, 433.95599999999996, 448.253], [3, 49.98, 540.26, 447.412, 462.55], [3, 49.98, 89.845, 462.55, 476.847], [3, 49.98, 241.57, 476.006, 491.144], [3, 49.98, 230.265, 490.303, 504.59999999999997], [3, 49.98, 185.64, 504.59999999999997, 518.8969999999999], [3, 49.98, 279.65, 517.215, 532.353], [3, 52.36, 146.37, 533.194, 546.65], [3, 52.36, 240.38, 545.809, 560.947], [3, 52.36, 141.015, 560.106, 574.403], [3, 52.36, 309.995, 571.88, 587.018], [3, 52.36, 304.64, 585.336, 600.4739999999999], [3, 52.36, 164.22, 599.6329999999999, 613.93], [3, 56.525, 202.29999999999998, 678.687, 695.507], [3, 248.11499999999998, 342.71999999999997, 674.482, 687.938], [3, 361.76, 457.555, 675.323, 688.779], [3, 56.525, 187.42499999999998, 692.9839999999999, 708.963], [3, 457.555, 531.3349999999999, 678.687, 714.85]]
2026-08-10 14:46:48,871 INFO     29 [qwen-vl-text] ═══ DONE ═══ 40 positions, pages=2, time=21.8s
2026-08-10 14:46:48,871 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:46:48,880 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:46:48,880 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:46:48,880 INFO     29 [qwen-vl-text] positions(43): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:46:48,881 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [43]
2026-08-10 14:46:49,144 INFO     29 [qwen-vl-text] page=4, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:46:49,146 INFO     29 [qwen-vl-text] LLM extraction start, text_len=959
2026-08-10 14:46:49,147 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:49,147 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 113, \"bbox_end\": 155, \"encounter_dates\": [\"2026-02-03\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "CT诊断报告单\n扫码查看影像报告\n诊疗号\n影像号 7159990\n检查号 16220702\n报告日期 2026-02-03 16:13:41\n性别 男\n年龄 48 岁\n住院号\n床号 231.2+7\n送检科别\n检查日期 2026-02-03 10:27:28\n检查项目\n胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像\n影像学表现\n原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不\n均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,\n肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及\n大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝\n右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,\n壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态\n正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,\n未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描\n呈轻度不均匀强化。左侧肾上腺区见软组织影。\n影像学意见\n胸部CT增强+薄层示:\n1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检\n查:\n2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;\n3、双侧尖部胸膜局部增厚;\n4、左侧部分肋骨形态欠规则,必要时ECT检查。\n上下腹部CT增强示:\n1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;\n2、双肾多发囊肿;\n3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;\n4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;\n5、左肾周渗出性改变;\n6、扫及左侧肾上腺区软组织影,转移可能。\n本报告仅供临床参考,签字有效。\n报告医师 李政晓\n审核医师 马璐瑶\n标有(陕HR)的项目为互认项目",
    "role": "user"
  }
]
2026-08-10 14:46:49,150 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:46:49.149+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:46:55,085 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:46:55,085 INFO     29 [qwen-vl-text] LLM output (len=1093):
{
  "exam_date": "2026-02-03",
  "report_date": "2026-02-03",
  "exam_name": "胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像",
  "exam_category": "imaging",
  "body_part": "胸部,下腹部,上腹部(肝胆胰脾)",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "231.2+7",
  "findings": "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。\n肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描呈轻度不均匀强化。左侧肾上腺区见软组织影。",
  "conclusion": "胸部CT增强+薄层示:\n1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检查:\n2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;\n3、双侧尖部胸膜局部增厚;\n4、左侧部分肋骨形态欠规则,必要时ECT检查。\n上下腹部CT增强示:\n1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;\n2、双肾多发囊肿;\n3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;\n4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;\n5、左肾周渗出性改变;\n6、扫及左侧肾上腺区软组织影,转移可能。",
  "physician": "李政晓",
  "reviewer": "马璐瑶"
}
2026-08-10 14:46:55,090 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1958418, prompt_len=1705
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共43行）
["CT诊断报告单", "扫码查看影像报告", "诊疗号", "影像号 7159990", "检查号 16220702", "报告日期 2026-02-03 16:13:41", "性别 男", "年龄 48 岁", "住院号", "床号 231.2+7", "送检科别", "检查日期 2026-02-03 10:27:28", "检查项目", "胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像", "影像学表现", "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "呈轻度不均匀强化。左侧肾上腺区见软组织影。", "影像学意见", "胸部CT增强+薄层示:", "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检", "查:", "2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;", "3、双侧尖部胸膜局部增厚;", "4、左侧部分肋骨形态欠规则,必要时ECT检查。", "上下腹部CT增强示:", "1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;", "2、双肾多发囊肿;", "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;", "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;", "5、左肾周渗出性改变;", "6、扫及左侧肾上腺区软组织影,转移可能。", "本报告仅供临床参考,签字有效。", "报告医师 李政晓", "审核医师 马璐瑶", "标有(陕HR)的项目为互认项目"]

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
2026-08-10 14:47:12,147 INFO     29 [qwen-vl-text] coord API raw response (len=2830):
[
	{"text": "CT诊断报告单", "bbox": [390, 149, 588, 176]},
	{"text": "扫码查看影像报告", "bbox": [797, 167, 938, 185]},
	{"text": "诊疗号", "bbox": [77, 181, 134, 196]},
	{"text": "影像号 7159990", "bbox": [291, 182, 435, 200]},
	{"text": "检查号 16220702", "bbox": [483, 184, 630, 200]},
	{"text": "报告日期 2026-02-03 16:13:41", "bbox": [664, 185, 943, 204]},
	{"text": "性别 男", "bbox": [257, 213, 338, 232]},
	{"text": "年龄 48 岁", "bbox": [398, 217, 510, 237]},
	{"text": "住院号", "bbox": [533, 217, 602, 237]},
	{"text": "床号 231.2+7", "bbox": [778, 219, 913, 238]},
	{"text": "送检科别", "bbox": [74, 238, 166, 256]},
	{"text": "检查日期 2026-02-03 10:27:28", "bbox": [365, 244, 689, 264]},
	{"text": "检查项目", "bbox": [65, 270, 142, 287]},
	{"text": "胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像", "bbox": [66, 290, 849, 313]},
	{"text": "影像学表现", "bbox": [71, 326, 188, 345]},
	{"text": "原系\"食管CA术后\"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不", "bbox": [114, 347, 911, 370]},
	{"text": "均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,", "bbox": [77, 364, 900, 387]},
	{"text": "肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及", "bbox": [78, 381, 908, 404]},
	{"text": "大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。", "bbox": [80, 398, 715, 421]},
	{"text": "肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝", "bbox": [81, 415, 907, 439]},
	{"text": "右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,", "bbox": [81, 432, 894, 455]},
	{"text": "壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态", "bbox": [83, 450, 904, 473]},
	{"text": "正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,", "bbox": [84, 467, 901, 490]},
	{"text": "未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描", "bbox": [84, 484, 902, 507]},
	{"text": "呈轻度不均匀强化。左侧肾上腺区见软组织影。", "bbox": [86, 500, 468, 517]},
	{"text": "影像学意见", "bbox": [85, 616, 194, 634]},
	{"text": "胸部CT增强+薄层示:", "bbox": [85, 635, 250, 652]},
	{"text": "1、原系\"食管CA术后\"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检", "bbox": [86, 652, 907, 676]},
	{"text": "查:", "bbox": [87, 670, 112, 684]},
	{"text": "2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;", "bbox": [87, 685, 653, 707]},
	{"text": "3、双侧尖部胸膜局部增厚;", "bbox": [87, 702, 306, 720]},
	{"text": "4、左侧部分肋骨形态欠规则,必要时ECT检查。", "bbox": [88, 718, 464, 737]},
	{"text": "上下腹部CT增强示:", "bbox": [90, 734, 240, 752]},
	{"text": "1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;", "bbox": [90, 750, 751, 776]},
	{"text": "2、双肾多发囊肿;", "bbox": [90, 767, 232, 785]},
	{"text": "3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;", "bbox": [90, 782, 603, 805]},
	{"text": "4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;", "bbox": [91, 797, 647, 820]},
	{"text": "5、左肾周渗出性改变;", "bbox": [92, 814, 269, 833]},
	{"text": "6、扫及左侧肾上腺区软组织影,转移可能。", "bbox": [93, 830, 437, 849]},
	{"text": "本报告仅供临床参考,签字有效。", "bbox": [102, 888, 336, 910]},
	{"text": "报告医师 李政晓", "bbox": [413, 887, 569, 910]},
	{"text": "审核医师 马璐瑶", "bbox": [600, 887, 759, 905]},
	{"text": "标有(陕HR)的项目为互认项目", "bbox": [103, 905, 310, 926]}
]
2026-08-10 14:47:12,149 INFO     29 [qwen-vl-text] coord API: raw_items=43, valid_items=43, elapsed=17.1s
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[0]: text=CT诊断报告单, bbox=[390, 149, 588, 176]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[1]: text=扫码查看影像报告, bbox=[797, 167, 938, 185]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗号, bbox=[77, 181, 134, 196]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[3]: text=影像号 7159990, bbox=[291, 182, 435, 200]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[4]: text=检查号 16220702, bbox=[483, 184, 630, 200]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[5]: text=报告日期 2026-02-03 16:13:41, bbox=[664, 185, 943, 204]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[6]: text=性别 男, bbox=[257, 213, 338, 232]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[7]: text=年龄 48 岁, bbox=[398, 217, 510, 237]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[8]: text=住院号, bbox=[533, 217, 602, 237]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[9]: text=床号 231.2+7, bbox=[778, 219, 913, 238]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[10]: text=送检科别, bbox=[74, 238, 166, 256]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[11]: text=检查日期 2026-02-03 10:27:28, bbox=[365, 244, 689, 264]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[12]: text=检查项目, bbox=[65, 270, 142, 287]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[13]: text=胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像, bbox=[66, 290, 849, 313]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[14]: text=影像学表现, bbox=[71, 326, 188, 345]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[15]: text=原系"食管CA术后"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不, bbox=[114, 347, 911, 370]
2026-08-10 14:47:12,150 INFO     29 [qwen-vl-text] coord item[16]: text=均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,, bbox=[77, 364, 900, 387]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[17]: text=肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及, bbox=[78, 381, 908, 404]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[18]: text=大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。, bbox=[80, 398, 715, 421]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[19]: text=肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝, bbox=[81, 415, 907, 439]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[20]: text=右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,, bbox=[81, 432, 894, 455]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[21]: text=壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态, bbox=[83, 450, 904, 473]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[22]: text=正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,, bbox=[84, 467, 901, 490]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[23]: text=未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描, bbox=[84, 484, 902, 507]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[24]: text=呈轻度不均匀强化。左侧肾上腺区见软组织影。, bbox=[86, 500, 468, 517]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[25]: text=影像学意见, bbox=[85, 616, 194, 634]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[26]: text=胸部CT增强+薄层示:, bbox=[85, 635, 250, 652]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[27]: text=1、原系"食管CA术后"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检, bbox=[86, 652, 907, 676]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[28]: text=查:, bbox=[87, 670, 112, 684]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[29]: text=2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;, bbox=[87, 685, 653, 707]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[30]: text=3、双侧尖部胸膜局部增厚;, bbox=[87, 702, 306, 720]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[31]: text=4、左侧部分肋骨形态欠规则,必要时ECT检查。, bbox=[88, 718, 464, 737]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[32]: text=上下腹部CT增强示:, bbox=[90, 734, 240, 752]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[33]: text=1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;, bbox=[90, 750, 751, 776]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[34]: text=2、双肾多发囊肿;, bbox=[90, 767, 232, 785]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[35]: text=3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;, bbox=[90, 782, 603, 805]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[36]: text=4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;, bbox=[91, 797, 647, 820]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[37]: text=5、左肾周渗出性改变;, bbox=[92, 814, 269, 833]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[38]: text=6、扫及左侧肾上腺区软组织影,转移可能。, bbox=[93, 830, 437, 849]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[39]: text=本报告仅供临床参考,签字有效。, bbox=[102, 888, 336, 910]
2026-08-10 14:47:12,151 INFO     29 [qwen-vl-text] coord item[40]: text=报告医师 李政晓, bbox=[413, 887, 569, 910]
2026-08-10 14:47:12,152 INFO     29 [qwen-vl-text] coord item[41]: text=审核医师 马璐瑶, bbox=[600, 887, 759, 905]
2026-08-10 14:47:12,152 INFO     29 [qwen-vl-text] coord item[42]: text=标有(陕HR)的项目为互认项目, bbox=[103, 905, 310, 926]
2026-08-10 14:47:12,153 INFO     29 [qwen-vl-text] page=4 — 43/43 coords, api_time=17.1s
2026-08-10 14:47:12,153 INFO     29 [qwen-vl-text] new_positions (43):
[[4, 232.04999999999998, 349.85999999999996, 125.309, 148.016], [4, 474.215, 558.11, 140.447, 155.585], [4, 45.815, 79.72999999999999, 152.221, 164.83599999999998], [4, 173.14499999999998, 258.825, 153.06199999999998, 168.2], [4, 287.385, 374.84999999999997, 154.744, 168.2], [4, 395.08, 561.0849999999999, 155.585, 171.564], [4, 152.915, 201.10999999999999, 179.13299999999998, 195.112], [4, 236.81, 303.45, 182.49699999999999, 199.31699999999998], [4, 317.135, 358.19, 182.49699999999999, 199.31699999999998], [4, 462.90999999999997, 543.235, 184.179, 200.158], [4, 44.03, 98.77, 200.158, 215.296], [4, 217.17499999999998, 409.955, 205.20399999999998, 222.024], [4, 38.675, 84.49, 227.07, 241.367], [4, 39.269999999999996, 505.155, 243.89, 263.233], [4, 42.245, 111.86, 274.166, 290.145], [4, 67.83, 542.045, 291.827, 311.17], [4, 45.815, 535.5, 306.12399999999997, 325.467], [4, 46.41, 540.26, 320.421, 339.764], [4, 47.599999999999994, 425.42499999999995, 334.71799999999996, 354.061], [4, 48.195, 539.665, 349.015, 369.199], [4, 48.195, 531.93, 363.312, 382.655], [4, 49.385, 537.88, 378.45, 397.793], [4, 49.98, 536.095, 392.747, 412.09], [4, 49.98, 536.6899999999999, 407.044, 426.387], [4, 51.169999999999995, 278.46, 420.5, 434.79699999999997], [4, 50.574999999999996, 115.42999999999999, 518.0559999999999, 533.194], [4, 50.574999999999996, 148.75, 534.035, 548.332], [4, 51.169999999999995, 539.665, 548.332, 568.516], [4, 51.765, 66.64, 563.47, 575.244], [4, 51.765, 388.53499999999997, 576.0849999999999, 594.587], [4, 51.765, 182.07, 590.382, 605.52], [4, 52.36, 276.08, 603.838, 619.817], [4, 53.55, 142.79999999999998, 617.294, 632.432], [4, 53.55, 446.84499999999997, 630.75, 652.616], [4, 53.55, 138.04, 645.047, 660.185], [4, 53.55, 358.78499999999997, 657.6619999999999, 677.005], [4, 54.144999999999996, 384.965, 670.2769999999999, 689.62], [4, 54.739999999999995, 160.055, 684.574, 700.553], [4, 55.335, 260.015, 698.03, 714.009], [4, 60.69, 199.92, 746.808, 765.31], [4, 245.73499999999999, 338.555, 745.967, 765.31], [4, 357.0, 451.60499999999996, 745.967, 761.105], [4, 61.285, 184.45, 761.105, 778.766]]
2026-08-10 14:47:12,153 INFO     29 [qwen-vl-text] ═══ DONE ═══ 43 positions, pages=1, time=23.3s
2026-08-10 14:47:12,153 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:47:12,155 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:47:12,155 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:47:12,155 INFO     29 [qwen-vl-text] positions(31): [[5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:47:12,155 INFO     29 [qwen-vl-text] page grouping: [5], lines per page: [31]
2026-08-10 14:47:12,356 INFO     29 [qwen-vl-text] page=5, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:47:12,358 INFO     29 [qwen-vl-text] LLM extraction start, text_len=559
2026-08-10 14:47:12,358 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:12,359 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 156, \"bbox_end\": 186, \"encounter_dates\": [\"2025-12-05\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "陕西省人民医院\nMR诊断报告单\n诊疗号\n影像号\n检查号\n扫码查看影像报告\n姓名\n性别 男\n年龄 47岁 住院号\n告日期 2025-12-05 20:46:59\n送检\n床号 231.240\n检查日期 2025-12-05 19:14:50\n检查项目\n颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增\n强灌注成像(PWI)\n影像学表现\n双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显\n异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大\n小形态信号未见异常。\n膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×\n3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-\n3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。\n影像学意见\n颅脑MR平扫+DWI+增强未见明显异常。\n盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。\n本报告仅供临床参考,签字有效。\n报告医师 姚云翔\n审核医师 张东升\n标有(陕HR)的项目为互认项目\n张东升",
    "role": "user"
  }
]
2026-08-10 14:47:16,252 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:16,252 INFO     29 [qwen-vl-text] LLM output (len=709):
{
  "exam_date": "2025-12-05",
  "report_date": "2025-12-05",
  "exam_name": "颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增强灌注成像(PWI)",
  "exam_category": "imaging",
  "body_part": "颅脑,盆腔",
  "patient_name": null,
  "patient_gender": "男",
  "department": null,
  "bed_number": "231.240",
  "findings": "影像学表现\n双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大小形态信号未见异常。\n膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。",
  "conclusion": "影像学意见\n颅脑MR平扫+DWI+增强未见明显异常。\n盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。\n本报告仅供临床参考,签字有效。",
  "physician": "姚云翔",
  "reviewer": "张东升"
}
2026-08-10 14:47:16,259 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1395770, prompt_len=1265
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["陕西省人民医院", "MR诊断报告单", "诊疗号", "影像号", "检查号", "扫码查看影像报告", "姓名", "性别 男", "年龄 47岁 住院号", "告日期 2025-12-05 20:46:59", "送检", "床号 231.240", "检查日期 2025-12-05 19:14:50", "检查项目", "颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增", "强灌注成像(PWI)", "影像学表现", "双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显", "异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大", "小形态信号未见异常。", "膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×", "3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-", "3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。", "影像学意见", "颅脑MR平扫+DWI+增强未见明显异常。", "盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。", "本报告仅供临床参考,签字有效。", "报告医师 姚云翔", "审核医师 张东升", "标有(陕HR)的项目为互认项目", "张东升"]

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
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord API raw response (len=1906):
[
	{"text": "陕西省人民医院", "bbox": [351, 58, 685, 96]},
	{"text": "MR诊断报告单", "bbox": [398, 98, 595, 122]},
	{"text": "诊疗号", "bbox": [78, 117, 140, 133]},
	{"text": "影像号", "bbox": [300, 124, 360, 140]},
	{"text": "检查号", "bbox": [490, 130, 549, 145]},
	{"text": "扫码查看影像报告", "bbox": [790, 123, 925, 140]},
	{"text": "姓名", "bbox": [78, 149, 126, 167]},
	{"text": "性别 男", "bbox": [266, 154, 347, 173]},
	{"text": "年龄 47岁 住院号", "bbox": [407, 159, 610, 181]},
	{"text": "告日期 2025-12-05 20:46:59", "bbox": [681, 138, 936, 158]},
	{"text": "送检", "bbox": [77, 174, 130, 193]},
	{"text": "床号 231.240", "bbox": [782, 169, 913, 187]},
	{"text": "检查日期 2025-12-05 19:14:50", "bbox": [375, 185, 698, 208]},
	{"text": "检查项目", "bbox": [69, 209, 150, 226]},
	{"text": "颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增", "bbox": [69, 228, 929, 261]},
	{"text": "强灌注成像(PWI)", "bbox": [69, 247, 229, 265]},
	{"text": "影像学表现", "bbox": [68, 284, 189, 303]},
	{"text": "双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显", "bbox": [68, 306, 936, 335]},
	{"text": "异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大", "bbox": [68, 324, 927, 353]},
	{"text": "小形态信号未见异常。", "bbox": [68, 343, 260, 360]},
	{"text": "膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×", "bbox": [118, 362, 913, 387]},
	{"text": "3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-", "bbox": [66, 380, 923, 405]},
	{"text": "3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。", "bbox": [66, 398, 799, 420]},
	{"text": "影像学意见", "bbox": [66, 431, 187, 450]},
	{"text": "颅脑MR平扫+DWI+增强未见明显异常。", "bbox": [65, 452, 387, 469]},
	{"text": "盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。", "bbox": [65, 470, 634, 488]},
	{"text": "本报告仅供临床参考,签字有效。", "bbox": [65, 874, 327, 896]},
	{"text": "报告医师 姚云翔", "bbox": [409, 870, 578, 887]},
	{"text": "审核医师 张东升", "bbox": [612, 871, 782, 889]},
	{"text": "标有(陕HR)的项目为互认项目", "bbox": [65, 893, 300, 914]},
	{"text": "张东升", "bbox": [773, 875, 927, 924]}
]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=10.3s
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[0]: text=陕西省人民医院, bbox=[351, 58, 685, 96]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[1]: text=MR诊断报告单, bbox=[398, 98, 595, 122]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[2]: text=诊疗号, bbox=[78, 117, 140, 133]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[3]: text=影像号, bbox=[300, 124, 360, 140]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[4]: text=检查号, bbox=[490, 130, 549, 145]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[5]: text=扫码查看影像报告, bbox=[790, 123, 925, 140]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[6]: text=姓名, bbox=[78, 149, 126, 167]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[7]: text=性别 男, bbox=[266, 154, 347, 173]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[8]: text=年龄 47岁 住院号, bbox=[407, 159, 610, 181]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[9]: text=告日期 2025-12-05 20:46:59, bbox=[681, 138, 936, 158]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[10]: text=送检, bbox=[77, 174, 130, 193]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[11]: text=床号 231.240, bbox=[782, 169, 913, 187]
2026-08-10 14:47:26,599 INFO     29 [qwen-vl-text] coord item[12]: text=检查日期 2025-12-05 19:14:50, bbox=[375, 185, 698, 208]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[13]: text=检查项目, bbox=[69, 209, 150, 226]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[14]: text=颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增, bbox=[69, 228, 929, 261]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[15]: text=强灌注成像(PWI), bbox=[69, 247, 229, 265]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[16]: text=影像学表现, bbox=[68, 284, 189, 303]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[17]: text=双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显, bbox=[68, 306, 936, 335]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[18]: text=异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大, bbox=[68, 324, 927, 353]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[19]: text=小形态信号未见异常。, bbox=[68, 343, 260, 360]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[20]: text=膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×, bbox=[118, 362, 913, 387]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[21]: text=3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-, bbox=[66, 380, 923, 405]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[22]: text=3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。, bbox=[66, 398, 799, 420]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[23]: text=影像学意见, bbox=[66, 431, 187, 450]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[24]: text=颅脑MR平扫+DWI+增强未见明显异常。, bbox=[65, 452, 387, 469]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[25]: text=盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。, bbox=[65, 470, 634, 488]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[26]: text=本报告仅供临床参考,签字有效。, bbox=[65, 874, 327, 896]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[27]: text=报告医师 姚云翔, bbox=[409, 870, 578, 887]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[28]: text=审核医师 张东升, bbox=[612, 871, 782, 889]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[29]: text=标有(陕HR)的项目为互认项目, bbox=[65, 893, 300, 914]
2026-08-10 14:47:26,600 INFO     29 [qwen-vl-text] coord item[30]: text=张东升, bbox=[773, 875, 927, 924]
2026-08-10 14:47:26,601 INFO     29 [qwen-vl-text] page=5 — 31/31 coords, api_time=10.3s
2026-08-10 14:47:26,601 INFO     29 [qwen-vl-text] new_positions (31):
[[5, 208.845, 407.575, 48.778, 80.73599999999999], [5, 236.81, 354.025, 82.41799999999999, 102.60199999999999], [5, 46.41, 83.3, 98.39699999999999, 111.853], [5, 178.5, 214.2, 104.28399999999999, 117.74], [5, 291.55, 326.655, 109.33, 121.945], [5, 470.04999999999995, 550.375, 103.443, 117.74], [5, 46.41, 74.97, 125.309, 140.447], [5, 158.26999999999998, 206.465, 129.51399999999998, 145.493], [5, 242.165, 362.95, 133.719, 152.221], [5, 405.195, 556.92, 116.05799999999999, 132.878], [5, 45.815, 77.35, 146.334, 162.313], [5, 465.28999999999996, 543.235, 142.129, 157.267], [5, 223.125, 415.31, 155.585, 174.928], [5, 41.055, 89.25, 175.769, 190.066], [5, 41.055, 552.755, 191.748, 219.501], [5, 41.055, 136.255, 207.727, 222.86499999999998], [5, 40.46, 112.455, 238.844, 254.82299999999998], [5, 40.46, 556.92, 257.346, 281.735], [5, 40.46, 551.5649999999999, 272.484, 296.873], [5, 40.46, 154.7, 288.46299999999997, 302.76], [5, 70.21, 543.235, 304.442, 325.467], [5, 39.269999999999996, 549.185, 319.58, 340.60499999999996], [5, 39.269999999999996, 475.405, 334.71799999999996, 353.21999999999997], [5, 39.269999999999996, 111.265, 362.471, 378.45], [5, 38.675, 230.265, 380.132, 394.429], [5, 38.675, 377.22999999999996, 395.27, 410.40799999999996], [5, 38.675, 194.565, 735.034, 753.536], [5, 243.355, 343.90999999999997, 731.67, 745.967], [5, 364.14, 465.28999999999996, 732.511, 747.649], [5, 38.675, 178.5, 751.0129999999999, 768.674], [5, 459.935, 551.5649999999999, 735.875, 777.084]]
2026-08-10 14:47:26,601 INFO     29 [qwen-vl-text] ═══ DONE ═══ 31 positions, pages=1, time=14.4s
2026-08-10 14:47:26,601 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 14:47:26,607 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 14:47:26,607 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 14:47:26,607 INFO     29 [qwen-vl-text] positions(35): [[9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 14:47:26,607 INFO     29 [qwen-vl-text] page grouping: [9], lines per page: [35]
2026-08-10 14:47:26,919 INFO     29 [qwen-vl-text] page=9, rect=595x841, img=(1653x2337), dpi=200
2026-08-10 14:47:26,920 INFO     29 [qwen-vl-text] LLM extraction start, text_len=424
2026-08-10 14:47:26,920 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:26,920 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 267, \"bbox_end\": 301, \"encounter_dates\": [\"2026-01-04\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "项目名称后标注“*”为必填项\n诊断结论:\n1. 窦性心律\n2. 正常范围心电图\n签名：\n姓名\n性别：男\n年龄：47岁\n住院号：0001145836 QRS（陕HR）：102↑ms(60-100)\nID号：0020553584 P:116↑ms(0-110)\n二病区床号：231.2+7\nQT/QTc（陕HR）：328/397ms(320-440/0-440)\nQRS电轴：70°（-30-90)\nP-R（陕HR）：154ms(120-200)\nRv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)\n纸速：25mm/s\n灵敏度：10mm/mV\n滤波：40\n检查日期：2026-01-04 13:\n临床诊断：食管恶性肿瘤\n心率（陕HR）：88(60-100)\n年龄不足1周岁的）\n年\n市）渭南市\n市华阴市\n农民\n婚姻\n2\n1.未婚 2.已婚 3.丧偶 4.离婚 9.其他\n邮编\n714200\n国\n中国\n2001145836\n民医院心电图报告单",
    "role": "user"
  }
]
2026-08-10 14:47:26,922 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T14:47:26.921+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 63, "failed": 0, "current": {"d9b80e2c94c911f1bd9827cf206dfa2d": {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 14:47:30,388 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:30,389 INFO     29 [qwen-vl-text] LLM output (len=528):
{
  "exam_date": "2026-01-04",
  "report_date": null,
  "exam_name": "心电图",
  "exam_category": "other",
  "body_part": null,
  "patient_name": null,
  "patient_gender": "男",
  "department": "二病区",
  "bed_number": "231.2+7",
  "findings": "QRS（陕HR）：102↑ms(60-100)\nP:116↑ms(0-110)\nQT/QTc（陕HR）：328/397ms(320-440/0-440)\nQRS电轴：70°（-30-90)\nP-R（陕HR）：154ms(120-200)\nRv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)\n纸速：25mm/s\n灵敏度：10mm/mV\n滤波：40\n心率（陕HR）：88(60-100)",
  "conclusion": "1. 窦性心律\n2. 正常范围心电图",
  "physician": null,
  "reviewer": null
}
2026-08-10 14:47:30,396 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=3021945, prompt_len=1142
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共35行）
["项目名称后标注“*”为必填项", "诊断结论:", "1. 窦性心律", "2. 正常范围心电图", "签名：", "姓名", "性别：男", "年龄：47岁", "住院号：0001145836 QRS（陕HR）：102↑ms(60-100)", "ID号：0020553584 P:116↑ms(0-110)", "二病区床号：231.2+7", "QT/QTc（陕HR）：328/397ms(320-440/0-440)", "QRS电轴：70°（-30-90)", "P-R（陕HR）：154ms(120-200)", "Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)", "纸速：25mm/s", "灵敏度：10mm/mV", "滤波：40", "检查日期：2026-01-04 13:", "临床诊断：食管恶性肿瘤", "心率（陕HR）：88(60-100)", "年龄不足1周岁的）", "年", "市）渭南市", "市华阴市", "农民", "婚姻", "2", "1.未婚 2.已婚 3.丧偶 4.离婚 9.其他", "邮编", "714200", "国", "中国", "2001145836", "民医院心电图报告单"]

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
2026-08-10 14:47:42,867 INFO     29 [qwen-vl-text] coord API raw response (len=1960):
[
	{"text": "项目名称后标注“*”为必填项", "bbox": [10, 153, 28, 323]},
	{"text": "诊断结论:", "bbox": [113, 157, 129, 208]},
	{"text": "1. 窦性心律", "bbox": [90, 157, 107, 220]},
	{"text": "2. 正常范围心电图", "bbox": [71, 157, 88, 255]},
	{"text": "签名：", "bbox": [14, 738, 35, 775]},
	{"text": "姓名", "bbox": [780, 172, 795, 185]},
	{"text": "性别：男", "bbox": [762, 172, 777, 210]},
	{"text": "年龄：47岁", "bbox": [740, 172, 756, 220]},
	{"text": "住院号：0001145836 QRS（陕HR）：102↑ms(60-100)", "bbox": [765, 280, 780, 544]},
	{"text": "ID号：0020553584 P:116↑ms(0-110)", "bbox": [785, 280, 800, 477]},
	{"text": "二病区床号：231.2+7", "bbox": [813, 242, 830, 355]},
	{"text": "QT/QTc（陕HR）：328/397ms(320-440/0-440)", "bbox": [773, 563, 790, 788]},
	{"text": "QRS电轴：70°（-30-90)", "bbox": [760, 563, 775, 680]},
	{"text": "P-R（陕HR）：154ms(120-200)", "bbox": [743, 386, 758, 536]},
	{"text": "Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)", "bbox": [737, 563, 752, 742]},
	{"text": "纸速：25mm/s", "bbox": [687, 711, 700, 782]},
	{"text": "灵敏度：10mm/mV", "bbox": [679, 796, 694, 878]},
	{"text": "滤波：40", "bbox": [664, 911, 680, 948]},
	{"text": "检查日期：2026-01-04 13:", "bbox": [785, 807, 814, 931]},
	{"text": "临床诊断：食管恶性肿瘤", "bbox": [736, 807, 765, 925]},
	{"text": "心率（陕HR）：88(60-100)", "bbox": [758, 807, 777, 925]},
	{"text": "年龄不足1周岁的）", "bbox": [943, 213, 983, 313]},
	{"text": "年", "bbox": [975, 318, 988, 343]},
	{"text": "市）渭南市", "bbox": [945, 348, 977, 417]},
	{"text": "市华阴市", "bbox": [967, 428, 990, 490]},
	{"text": "农民", "bbox": [940, 487, 957, 514]},
	{"text": "婚姻", "bbox": [943, 529, 962, 555]},
	{"text": "2", "bbox": [945, 555, 962, 575]},
	{"text": "1.未婚 2.已婚 3.丧偶 4.离婚 9.其他", "bbox": [945, 575, 973, 750]},
	{"text": "邮编", "bbox": [918, 680, 932, 705]},
	{"text": "714200", "bbox": [920, 718, 935, 750]},
	{"text": "国", "bbox": [937, 796, 952, 817]},
	{"text": "中国", "bbox": [930, 835, 945, 855]},
	{"text": "2001145836", "bbox": [973, 796, 988, 841]},
	{"text": "民医院心电图报告单", "bbox": [847, 514, 883, 717]}
]
2026-08-10 14:47:42,867 INFO     29 [qwen-vl-text] coord API: raw_items=35, valid_items=35, elapsed=12.5s
2026-08-10 14:47:42,867 INFO     29 [qwen-vl-text] coord item[0]: text=项目名称后标注“*”为必填项, bbox=[10, 153, 28, 323]
2026-08-10 14:47:42,867 INFO     29 [qwen-vl-text] coord item[1]: text=诊断结论:, bbox=[113, 157, 129, 208]
2026-08-10 14:47:42,867 INFO     29 [qwen-vl-text] coord item[2]: text=1. 窦性心律, bbox=[90, 157, 107, 220]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[3]: text=2. 正常范围心电图, bbox=[71, 157, 88, 255]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[4]: text=签名：, bbox=[14, 738, 35, 775]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[5]: text=姓名, bbox=[780, 172, 795, 185]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[6]: text=性别：男, bbox=[762, 172, 777, 210]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[7]: text=年龄：47岁, bbox=[740, 172, 756, 220]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[8]: text=住院号：0001145836 QRS（陕HR）：102↑ms(60-100), bbox=[765, 280, 780, 544]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[9]: text=ID号：0020553584 P:116↑ms(0-110), bbox=[785, 280, 800, 477]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[10]: text=二病区床号：231.2+7, bbox=[813, 242, 830, 355]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[11]: text=QT/QTc（陕HR）：328/397ms(320-440/0-440), bbox=[773, 563, 790, 788]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[12]: text=QRS电轴：70°（-30-90), bbox=[760, 563, 775, 680]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[13]: text=P-R（陕HR）：154ms(120-200), bbox=[743, 386, 758, 536]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[14]: text=Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5), bbox=[737, 563, 752, 742]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[15]: text=纸速：25mm/s, bbox=[687, 711, 700, 782]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[16]: text=灵敏度：10mm/mV, bbox=[679, 796, 694, 878]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[17]: text=滤波：40, bbox=[664, 911, 680, 948]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[18]: text=检查日期：2026-01-04 13:, bbox=[785, 807, 814, 931]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[19]: text=临床诊断：食管恶性肿瘤, bbox=[736, 807, 765, 925]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[20]: text=心率（陕HR）：88(60-100), bbox=[758, 807, 777, 925]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[21]: text=年龄不足1周岁的）, bbox=[943, 213, 983, 313]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[22]: text=年, bbox=[975, 318, 988, 343]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[23]: text=市）渭南市, bbox=[945, 348, 977, 417]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[24]: text=市华阴市, bbox=[967, 428, 990, 490]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[25]: text=农民, bbox=[940, 487, 957, 514]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[26]: text=婚姻, bbox=[943, 529, 962, 555]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[27]: text=2, bbox=[945, 555, 962, 575]
2026-08-10 14:47:42,868 INFO     29 [qwen-vl-text] coord item[28]: text=1.未婚 2.已婚 3.丧偶 4.离婚 9.其他, bbox=[945, 575, 973, 750]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[29]: text=邮编, bbox=[918, 680, 932, 705]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[30]: text=714200, bbox=[920, 718, 935, 750]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[31]: text=国, bbox=[937, 796, 952, 817]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[32]: text=中国, bbox=[930, 835, 945, 855]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[33]: text=2001145836, bbox=[973, 796, 988, 841]
2026-08-10 14:47:42,869 INFO     29 [qwen-vl-text] coord item[34]: text=民医院心电图报告单, bbox=[847, 514, 883, 717]
2026-08-10 14:47:42,870 INFO     29 [qwen-vl-text] page=9 — 35/35 coords, api_time=12.5s
2026-08-10 14:47:42,870 INFO     29 [qwen-vl-text] new_positions (35):
[[9, 5.949999999999999, 16.66, 128.673, 271.643], [9, 67.235, 76.755, 132.037, 174.928], [9, 53.55, 63.665, 132.037, 185.01999999999998], [9, 42.245, 52.36, 132.037, 214.45499999999998], [9, 8.33, 20.825, 620.658, 651.775], [9, 464.09999999999997, 473.025, 144.652, 155.585], [9, 453.39, 462.315, 144.652, 176.60999999999999], [9, 440.29999999999995, 449.82, 144.652, 185.01999999999998], [9, 455.17499999999995, 464.09999999999997, 235.48, 457.50399999999996], [9, 467.075, 476.0, 235.48, 401.157], [9, 483.73499999999996, 493.84999999999997, 203.522, 298.555], [9, 459.935, 470.04999999999995, 473.483, 662.708], [9, 452.2, 461.125, 473.483, 571.88], [9, 442.085, 451.01, 324.626, 450.776], [9, 438.515, 447.44, 473.483, 624.0219999999999], [9, 408.765, 416.5, 597.951, 657.6619999999999], [9, 404.005, 412.93, 669.4359999999999, 738.398], [9, 395.08, 404.59999999999997, 766.151, 797.2679999999999], [9, 467.075, 484.33, 678.687, 782.971], [9, 437.91999999999996, 455.17499999999995, 678.687, 777.925], [9, 451.01, 462.315, 678.687, 777.925], [9, 561.0849999999999, 584.885, 179.13299999999998, 263.233], [9, 580.125, 587.86, 267.438, 288.46299999999997], [9, 562.275, 581.3149999999999, 292.668, 350.697], [9, 575.365, 589.05, 359.948, 412.09], [9, 559.3, 569.415, 409.567, 432.274], [9, 561.0849999999999, 572.39, 444.889, 466.755], [9, 562.275, 572.39, 466.755, 483.575], [9, 562.275, 578.935, 483.575, 630.75], [9, 546.2099999999999, 554.54, 571.88, 592.905], [9, 547.4, 556.3249999999999, 603.838, 630.75], [9, 557.515, 566.4399999999999, 669.4359999999999, 687.097], [9, 553.35, 562.275, 702.235, 719.055], [9, 578.935, 587.86, 669.4359999999999, 707.281], [9, 503.965, 525.385, 432.274, 602.997]]
2026-08-10 14:47:42,870 INFO     29 [qwen-vl-text] ═══ DONE ═══ 35 positions, pages=1, time=16.3s
2026-08-10 14:47:42,887 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 14:47:42,887 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:ExaminationReport | outputs={"chunks": "5 items, types={'ExaminationReport': 5}", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:47:42,887 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 14:47:42,895 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:42,895 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 14:47:44,139 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 14:47:44,147 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 14:47:44,147 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "302 items", "markdown": "", "text": "", "name": "WHTA，男，47岁.pdf", "output_format": "chunks", "chunks_Examination": "5 items, types={'ExaminationReport': 5}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_LabExam": "1 items, types={'LabReport': 1}", "route_summary": "{\"chunks_Examination\": 5, \"chunks_Discharge\": 1, \"chunks_LabExam\": 1}"}
2026-08-10 14:47:44,147 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 14:47:44,147 INFO     29 [ChunkMerger] Merged 7 chunks from 9 sources: {'Extractor:LabExam': 1, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 5, 'Extractor:Progress': 1} (filtered 6 noise chunks)
2026-08-10 14:47:44,163 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 14:47:44,163 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'DischargeRecord': 1, 'ExaminationReport': 5}", "name": "WHTA，男，47岁.pdf"}
2026-08-10 14:47:44,163 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 14:47:44,299 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786373050663, 'update_date': datetime.datetime(2026, 8, 10, 14, 44, 10), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1113978, 'status': '1'}
2026-08-10 14:47:44,500 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   谷丙转氨酶  ALT  34  U/L  9-50  False    谷草转氨酶  AST  29  U/L  15-40  False    碱性磷酸酶  ALP  199  U/L  45-125  True    γ-谷氨酰基转移酶  GGT  153  U/L  10-60  True    胆碱脂酶  CHE  5394  U/L  5000-12000  False    总胆汁酸  TBA  2.16  umol/L  0-10  False    总胆红素  TBIL  7.49  umol/L  0-23  False    直接胆红素  DBIL  1.59  umol/L  0-6.84  False    总蛋白  TP  62.9  g/L  None  False    白蛋白  ALB  37.1  g/L  None  False    球蛋白  GLOBU  25.80  g/L  None  False    白球比  A/G  1.44  None  None  False    二氧化碳结合力  PCO2  27  mmol/L  22-29  False    尿素  UREA  5.24  mmol/L  2.86-8.2  False    肌酐  CRE  56.71  umol/L  53-123  False    钾  K  4.5  mmol/L  3.5-5.5  False    钠  Na  137  mmol/L  137-147  False    氯  Cl  102  mmol/L  96-108  False    尿酸  UA  210.46  umol/L  208-428  False    视黄醇结合蛋白  RBP  31.87  mg/L  25-70  False    胱抑素-C  Cys-C  0.99  mg/L  0.59-1.03  False    中性粒细胞明胶酶相关脂质运载蛋白  NGA  24.10  ng/ml  0-180  False    白细胞计数  WBC  3.59  10^9/L  3.5-9.5  False    中性粒细胞比率  NEU  64.70  %  40-75  False    淋巴细胞比率  LYM  22.00  %  20-50  False    单核细胞比率  MONO  11.40  %  3-10  True    嗜酸性粒细胞比率  EOS  1.90  %  0.4-8  False    嗜碱性粒细胞比率  BASO  0.00  %  0-1  False    中性粒细胞绝对值  NEU#  2.32  10^9/L  1.8-6.3  False    淋巴细胞绝对值  LYM#  0.79  10^9/L  1.1-3.2  True    单核细胞绝对值  MONO#  0.41  10^9/L  0.1-0.6  False    嗜酸性粒细胞绝对值  EOS#  0.07  10^9/L  0.02-0.52  False    嗜碱性粒细胞绝对值  BASO#  0.00  10^9/L  0-0.06  False    红细胞计数  RBC  3.28  10^12/L  4.3-5.8  True    血红蛋白测定  HB  99  g/L  130-175  True    红细胞比积测定  HCT  30.9  %  40-50  True    平均红细胞体积  MCV  94.20  fL  None  False    平均红细胞血红蛋白量  MCH  30.20  pg  None  False    平均红细胞血红蛋白浓度  None  320.00  g/L  None  False    红细胞体积分布宽度  RDW-CV  15.10  %  None  True    血小板计数  PLT  384  10^9/L  None  True    血小板比积  PCT  0.35  %  None  False    平均血小板体积  MPV  9.00  fL  None  True    血小板体积分布宽度  PDW  8.50  fL  None  True   
---
24小时内入出院记录
姓名
性别：男
年龄：47岁
民族：汉族
出生日期：1978-01-07
婚姻状况：已婚
籍贯：
出生地：
国籍：
证件号码：
工作单位：
职业：
详细地址：
联系电话：
联系人：
关系：配偶
入院日期：2026-01-16 10:19
病历完成时间：2026-01-16 10:49
病史陈述者：患者本人
可靠性：可靠
是否传染病：否
既往是否健康：是
主诉：食管鳞癌术后7年余，肝转移11月余。
现病史：7年余前（2018-01）因吞咽困难就诊华阴市人民医院，确诊食管鳞癌，行食管癌根治术，术后病理及分期不详，术后行5周期全身化疗，具体方案及剂量不详。术后定期复查。2020-09就诊本院，复查CT提示吻合口增厚（未见报告），行胃镜取活检，病理为：（吻合口下缘）中分化鳞状细胞癌，考虑食管癌复发，予以放疗27次及化疗6次（顺铂60mg/W+卡培他滨d1-5/W），随后予以信迪利单抗200mg免疫维持2年，期间未定期复查。2025-01因上腹胀痛、左侧腰部隐痛，就诊华阴市人民医院，查胃镜提示：残胃炎伴胆汁反流；腹部CT提示食管下段占位术后改变，术区斑点状高密度缝合线影，吻合口处壁稍增厚；肝脏多发类圆形低密度影，转移瘤不除外。双肾密度减低，左肾体积增大，左肾积水，左侧输尿管J管置入术后，腹主动脉旁多发肿大淋巴结，部分融合，转移瘤不除外。2025-01-07就诊渭南市中心医院，行CT提示胸中部食管术后，其吻合器下缘壁稍显增厚。肝脏多发占位性病变，考虑转移瘤；腹膜后多发增大淋巴结。于2025-01-10、2025-02-06行2周期免疫+化疗，具体为：替雷利珠单抗200mg静滴d0，白蛋白结合型紫杉醇200mgd1、8，奈达铂40mgd1-3。复查CT（2025.03.03）提示肝脏多发转移瘤较前减小；腹膜后多发稍增大淋巴结，较前减少。评估病情缓解。于2025-03-04至2025-05-17继续予以原方案型免疫联合化疗4周期。于2025-07-03至2025-09-29行免疫维持治疗5周期，具体为：替雷利珠单抗200mg静滴d1。2025-10-27和2025-12-03复查CT提示病情进展。2025-12-08就诊本院予以伊立替康+S-1化疗，期间出现消化道反应。2026.01.08使用盐酸伊立替康脂质体（43mgd1,8）+S-1（60mg口服bid d1-14）化疗联合卡度尼利（250mg）免疫治疗。现为求进一步诊治，就诊本科，门诊以“食管恶性肿瘤”收住。近1月，神志清，精神可，食纳夜休尚可，大小便未见明显异常，诉左腰部隐痛不适，体重未见明显变化。
入院情况：神志清，精神可，食纳夜休尚可。
症状名称：无发热，无腹痛腹胀，无恶心呕吐等不适。
症状描述：无发热，无腹痛腹胀，无恶心呕吐等不适。
第1页
入院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后
4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后
7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架
诊疗过程：预住院完善检查，血常规：血红蛋白测定99g/L。无排除治疗禁忌，予以盐
酸伊立替康脂质体43mg d8行抗肿瘤治疗，辅以止吐、抗过敏、抑酸护胃等对症支持治疗。
出院情况：神志清，精神可，食纳夜休尚可。
出院诊断：1.姑息性化疗 2.恶性肿瘤免疫治疗 3.食管恶性肿瘤(rTxNxM1 IV期)术后
4.肝继发恶性肿瘤 5.多部位淋巴结继发恶性肿瘤(肝门区、腹膜后) 6.恶性肿瘤放射治疗后
7.左侧肾积水伴输尿管狭窄 8.左侧输尿管支架置入术后 9.更换输尿管支架
出院医嘱：1.注意休息，避免劳累和感染，注意有无腹泻；2.院外继续使用药物：替吉
奥胶囊 60mg 口服 一日二次，每周监测血常规；3.按时返院行下周期治疗，若有不适，我
科随诊。
接诊医师签名：
住院医师签名：
主治医师签名：
主（副主）任医师签名：
---
华阴市人民医院
病理检查报告单
姓名：
性别：男
年龄：39
病理号：2018-0079
送检单位：本院
科别：普外科
住院号：1800732
床号：25
送检日期：2018-01-27
送检医师：韩晔
送检材料：食管
临床诊断：
肉眼所见：
送检食管组织，长11cm，直径1.5cm，浆膜面灰红色光滑，切开粘膜灰红色光滑，距食管
端3cm，下端7cm处有一突出，长6cm，直径3cm，突出顶端有一灰白色隆起肿块，V4x2x2c
，切开切面灰白色质硬，肿块周检见淋巴结5枚，直径0.3cm；另见灰黄色脂肪组织一堆，
V6x6x4cm，其内未见明显肿大淋巴结；另见灰红色切缘一块，直径1cm；另见钢钉切缘，
径0.8cm；另送第五组淋巴结，灰红色两块。
光镜所见：
病理诊断：
食管隆起型鳞状细胞癌III级侵及外膜伴神经浸润
第五组淋巴结（1/1枚）可见癌转移
食管周淋巴结（5枚）未见癌组织
另送上下切缘未见癌组织
上、下切缘未见癌组织
纤维脂肪组织内未见癌组织
---
第 2 页
姓名
性别 男
年龄 47 岁 住院号
床号 231.2+13
送检科
检查日期 2025-12-05 15:02:38
检查项目
胸部CT增强扫描,胸部CT增强薄层扫描成像,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强薄层扫描成
像,上腹部(肝胆胰脾)CT增强扫描
影像学表现
原系"食管CA术后"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不
均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,
肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及
大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。
肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝
右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,
壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态
正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,
未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描
呈轻度不均匀强化。
影像学意见
胸部CT增强+薄层示:
1、原系"食管CA术后"改变,吻合口壁增厚并异常强化,较前(2021-06-23)壁厚程度略加重,建议胃
镜检查;
2、双肺散在渗出及纤维灶,较前增多;
3、原"左肺上叶小结节影"未见显示;
4、双侧尖部胸膜局部增厚;
5、左侧部分肋骨形态欠规则,必要时ECT检查。
上下腹部CT增强示:
1、肝内多发异常强化影,考虑肝转移;
2、双肾多发囊肿;
3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水;
4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移;
5、左肾周渗出性改变。
本报告仅供临床参考,签字有效。
报告医师 郭田田
审核医师 寇明清
标有(陕HR)的项目为互认项目
寇明清
---
CT诊断报告单
扫码查看影像报告
诊疗号
影像号 7159990
检查号 16220702
报告日期 2026-02-03 16:13:41
性别 男
年龄 48 岁
住院号
床号 231.2+7
送检科别
检查日期 2026-02-03 10:27:28
检查项目
胸部CT增强扫描,下腹部CT增强扫描,上腹部(肝胆胰脾)CT增强扫描,胸部CT增强薄层扫描成像
影像学表现
原系"食管CA术后"改变,现片示:食管局部见线状高密度影,吻合口壁增厚,增强扫描呈轻度不
均匀强化。胸廓对称,左侧部分肋骨形态欠规则,胸壁软组织未见明显异常;双侧肺野透光度正常,
肺纹理走行自然,双肺见散在索条及絮状密度增高影;双侧肺门不大;纵隔窗示纵隔无偏移,心影及
大血管未见明显异常,纵隔内未见明显肿大淋巴结。双侧尖部胸膜局部增厚。
肝脏边缘光滑,各叶大小比例正常,肝内见多个类圆形低密度轻度不均匀强化影,边界欠清;肝
右叶边缘见结节样高密度影;肝内外胆管未见扩张,肝门部结构清晰,未见占位性病变。胆囊不大,
壁厚薄均匀,未见阳性结石影。胰腺大小、形态及密度正常。脾不大,实质密度均匀。双肾大小形态
正常,双肾见小类圆形低密度无强化影,左侧肾盂输尿管内见双J管影,左侧肾盂肾盏轻度扩张积液,
未见阳性结石影;左肾周见片絮影及条索影。腹腔内及腹膜后见多个淋巴结影,部分肿大,增强扫描
呈轻度不均匀强化。左侧肾上腺区见软组织影。
影像学意见
胸部CT增强+薄层示:
1、原系"食管CA术后"改变,吻合口壁增厚并异常强化,较前(2025-12-05)变化不明显,建议内镜检
查:
2、双肺散在渗出及纤维灶,较前右肺下叶索条显示清晰,余变化不著;
3、双侧尖部胸膜局部增厚;
4、左侧部分肋骨形态欠规则,必要时ECT检查。
上下腹部CT增强示:
1、肝内多发异常强化影,考虑肝转移,较前(2025-12-5)部分稍增大,部分新现;
2、双肾多发囊肿;
3、左侧肾盂输尿管J管置入术后改变,左肾轻度积水较前稍减轻;
4、腹腔内腹膜后多个肿大淋巴结,考虑淋巴结转移,较前部分稍增大;
5、左肾周渗出性改变;
6、扫及左侧肾上腺区软组织影,转移可能。
本报告仅供临床参考,签字有效。
报告医师 李政晓
审核医师 马璐瑶
标有(陕HR)的项目为互认项目
---
陕西省人民医院
MR诊断报告单
诊疗号
影像号
检查号
扫码查看影像报告
姓名
性别 男
年龄 47岁 住院号
告日期 2025-12-05 20:46:59
送检
床号 231.240
检查日期 2025-12-05 19:14:50
检查项目
颅脑磁共振平扫(陕HR),脑弥散成像(DWI)(陕HR),盆腔功能成像(DWI),盆腔磁共振平扫,颅脑磁共振增
强灌注成像(PWI)
影像学表现
双侧大脑半球、小脑半球及脑干对称,灰白质对比自然,脑实质内未见明显异常信号影,DWI未见明显
异常高信号,增强扫描未见异常强化。脑室系统对称。中线结构居中。脑沟、脑池正常。所见垂体大
小形态信号未见异常。
膀胱充盈欠佳,膀胱壁局部略增厚毛糙。前列腺体积略增大,形态欠规整,大小约5.0×3.0×
3.0cm,左侧外周带内见斑片状等T1稍短T2信号影,边界欠清,DWI呈高信号,ADC值约1.1-1.33×10-
3mm2/s。直肠管壁光整,其内未见明显异常信号影。盆壁结构正常,未见肿大淋巴结。
影像学意见
颅脑MR平扫+DWI+增强未见明显异常。
盆腔MRI平扫+DWI示:前列腺左侧外周带异常所见,考虑炎性病变。
本报告仅供临床参考,签字有效。
报告医师 姚云翔
审核医师 张东升
标有(陕HR)的项目为互认项目
张东升
---
项目名称后标注“*”为必填项
诊断结论:
1. 窦性心律
2. 正常范围心电图
签名：
姓名
性别：男
年龄：47岁
住院号：0001145836 QRS（陕HR）：102↑ms(60-100)
ID号：0020553584 P:116↑ms(0-110)
二病区床号：231.2+7
QT/QTc（陕HR）：328/397ms(320-440/0-440)
QRS电轴：70°（-30-90)
P-R（陕HR）：154ms(120-200)
Rv5/Sv1:1.6/0.63mV(0-2.5/0-1.5)
纸速：25mm/s
灵敏度：10mm/mV
滤波：40
检查日期：2026-01-04 13:
临床诊断：食管恶性肿瘤
心率（陕HR）：88(60-100)
年龄不足1周岁的）
年
市）渭南市
市华阴市
农民
婚姻
2
1.未婚 2.已婚 3.丧偶 4.离婚 9.其他
邮编
714200
国
中国
2001145836
民医院心电图报告单
2026-08-10 14:47:45,010 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 14:47:45,010 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "7 items, types={'LabReport': 1, 'DischargeRecord': 1, 'ExaminationReport': 5}", "name": "WHTA，男，47岁.pdf", "embedding_token_consumption": 5146}
2026-08-10 14:47:45,011 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 14:47:45,205 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 14:47:45,205 INFO     29 [Trace] task=d9b80e2c | doc=WHTA，男，47岁.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":7,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int len=44 row[0]=(7, 397, 410, 132, 262) row[-1]=(9, 302, 315, 479, 618)
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,209 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 14:47:45,215 INFO     29 set_progress(d9b80e2c94c911f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 14:47:45 [DOC Engine]:
Start to index...
2026-08-10 14:47:45,256 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.033s]
2026-08-10 14:47:45,260 INFO     29 set_progress(d9b80e2c94c911f1bd9827cf206dfa2d), progress: 0.8142857142857143, progress_msg: 
2026-08-10 14:47:45,279 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.011s]
2026-08-10 14:47:45,294 INFO     29 set_progress(d9b80e2c94c911f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 14:47:45 Indexing done (0.07s). Task done (234.30s)
2026-08-10 14:47:45,299 INFO     29 [Done], chunks(7), token(5146), elapsed:234.30
2026-08-10 14:47:45,435 INFO     29 handle_task done for task {"id": "d9b80e2c94c911f1bd9827cf206dfa2d", "doc_id": "d952dce694c911f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "type": "pdf", "location": "WHTA\uff0c\u7537\uff0c47\u5c81.pdf", "size": 13102054, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786373008728, "task_type": "dataflow", "root_trace_id": "89033196689c4d5397c2736f5a635371", "root_traceparent": "00-89033196689c4d5397c2736f5a635371-40a65f839b7d9353-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
