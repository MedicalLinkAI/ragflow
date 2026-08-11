# 基准结果：徐州-LIYE-小肺-方穹推荐706-Ia期.pdf

## 基本信息

- 文件：`徐州-LIYE-小肺-方穹推荐706-Ia期.pdf`
- 大小：2804.8 KB
- PDF 总页数：14
- doc_id：`7f1b076e94d611f1bd9827cf206dfa2d`
- 上传方式：upload_file+upload
- 状态：run=DONE (code=DONE)  progress=1.0
- 开始时间：2026-08-11T00:13:58  完成时间：2026-08-11T00:20:14  耗时：375.7s
- progress_msg：`16:20:09 Indexing done (0.08s). Task done (347.00s)`
- **SyncChunks 同步失败：`None`**

## 1. Chunk 页数核对

| # | chunk_id(前8位) | 页数 | 页码范围 | 内容摘要 |
|---|----------------|------|----------|----------|
| 1 | 3f6a7f85 | 3 | 2-4 | 南京鼓楼医院 南京大学医学院附属鼓楼医院 出院记录 科别（江北）综合肿瘤中心 病 |
| 2 | ee8ad8df | 1 | 5-5 | 河北省人民医院 病理检查报告单 病理号 姓名: 性别:女 年龄:74岁 送检单位 |
| 3 | 04c044a2 | 2 | 5-6 | 住院病历 河北省人民医院 病理检查补充报告单 病理号: 姓名: 性别: 女 年龄 |
| 4 | 04da6806 | 1 | 7-7 | 南京鼓楼医院云胶片 南京鼓楼医院 南京大学医学院附属鼓楼医院 影像检查诊断报告  |
| 5 | 7197fdc9 | 4 | 8-11 | 南京鼓楼医院云胶片 女/75岁 设备类型 CT 患者类型 无 检查项目 [CT平 |
| 6 | a8488172 | 1 | 12-12 | 南京鼓楼医院 南京大学医学院附属鼓楼医院 互联网医院 门诊病历 姓名: 性别:女 |
| 7 | 70776ee0 | 1 | 14-14 | <table><tr><td>丙氨酸氨基转移酶</td><td>None</td |
| 8 | fab1ee3a | 1 | 14-14 | <table><tr><td>C反应蛋白</td><td>None</td><t |
| 9 | 0d0c8c44 | 1 | 13-13 | <table><tr><td>白细胞计数</td><td>WBC</td><td |

- chunks 总数：9
- 各 chunk 页数合计（含跨页重复）：15
- 页码并集：`[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- 覆盖页数：13 / 14；缺失页：`[1]`
- 超范围页（> PDF 总页数）：`[]`
- **结论：❌ 未完全覆盖：覆盖 13/14 页，缺失 [1]，超范围 []**

## 2. 六类文档过滤检查

| 类型 | 中文 | 识别 | 提取输出 | 落库 | 核心字段（缺失会被过滤） | 判定 |
|------|------|------|----------|------|--------------------------|------|
| OutpatientRecord | 门诊 | 1 | 0 | 1 | encounter_date, chief_complaint, diagnosis | **OK** |
| AdmissionRecord | 入院 | 0 | 1 | 0 | encounter_date, dm_admission_time, cc_text, department | **-** |
| DischargeRecord | 出院 | 1 | 1 | 1 | admission_date, discharge_date, department, outcome | **OK** |
| MedicationRecord | 购药 | 0 | 1 | 0 | encounter_date, pharmacy, payment_total | **-** |
| PrescriptionRecord | 处方 | 0 | 1 | 0 | encounter_date, prescriber, diagnosis | **-** |
| ExaminationReport | 检查报告 | 4 | 4 | 4 | exam_date, report_date, exam_name, body_part, department | **OK** |
| LabReport | 检验报告 | 3 | 0 | 3 | report_time, report_category, report_name | **OK** |

- SmartSplitter Types 统计：`{"DischargeRecord": 1, "ExaminationReport": 4, "OutpatientRecord": 1, "LabReport": 3}`
- ChunkMerger：`{"found": true, "merged": 9, "sources": 9, "stats": {"Extractor:LabExam": 3, "Extractor:Imaging": 1, "Extractor:Clinical": 1, "Extractor:Medication": 1, "Extractor:Prescription": 1, "Extractor:Discharge": 1, "Extractor:Admission": 1, "Extractor:ExaminationReport": 4, "Extractor:Progress": 1}, "filtered_noise": 5}`
- Extractor skip 证据：1 条
  - `[no_text_noise] 2026-08-10 16:20:07,690 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescr`
- worker 日志错误：0 条

## 3. 完整日志（该文档在 worker 容器中的全部日志行）

```text
2026-08-10 16:14:01,591 INFO     29 handle_task begin for task {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
2026-08-10 16:14:01,814 INFO     29 HEAD http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3 [status:200 duration:0.001s]
2026-08-10 16:14:01,937 INFO     29 [Pipeline] Executing component [1]: Parser:MedLink (type=Parser)
2026-08-10 16:14:01,950 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:14:01,950 INFO     29 🔧 OCR.__init__: ocr_version=default(v4), model_dir=/ragflow/rag/res/deepdoc
2026-08-10 16:14:01,950 INFO     29 load_model /ragflow/rag/res/deepdoc/det.onnx reuses cached model
2026-08-10 16:14:01,955 INFO     29 load_model /ragflow/rag/res/deepdoc/rec.onnx reuses cached model
2026-08-10 16:14:01,955 INFO     29 ============================================================
2026-08-10 16:14:01,956 INFO     29 ✅ [OCR VERSION] Using PP-OCRv4
2026-08-10 16:14:01,956 INFO     29    model_dir : /ragflow/rag/res/deepdoc
2026-08-10 16:14:01,956 INFO     29 ============================================================
2026-08-10 16:14:01,956 INFO     29 load_model /ragflow/rag/res/deepdoc/layout.onnx reuses cached model
2026-08-10 16:14:01,956 INFO     29 load_model /ragflow/rag/res/deepdoc/tsr.onnx reuses cached model
2026-08-10 16:14:01,957 INFO     29 No torch found.
2026-08-10 16:14:02,991 INFO     29 [qwen-vl-parser] parse_pdf start, total_pages=14
2026-08-10 16:14:03,050 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=145687, prompt_len=764
2026-08-10 16:14:04,265 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:14:04,266 INFO     29 [qwen-vl-parser] page=1 classify=text report_date=None
2026-08-10 16:14:04,279 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=145687, prompt_len=401
2026-08-10 16:14:05,088 INFO     29 [qwen-vl-parser] text API response (len=87):
["2025.5.21确诊小细胞肺癌", "2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利", "2025.8.13-2025.11.7 依托泊苷+斯鲁利"]
2026-08-10 16:14:05,089 INFO     29 [qwen-vl-parser] page=1 text: 3 lines (bbox 0-2)
2026-08-10 16:14:05,089 INFO     29 [qwen-vl-parser] page=1 text: 3 sections
2026-08-10 16:14:05,227 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1071362, prompt_len=764
2026-08-10 16:14:06,628 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:14:06,629 INFO     29 [qwen-vl-parser] page=2 classify=text report_date=None
2026-08-10 16:14:06,648 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1071362, prompt_len=401
2026-08-10 16:14:14,058 INFO     29 [qwen-vl-parser] text API response (len=1268):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "住院号", "姓名：", "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "8. 甲状腺功能减退症 9. 高血压2级（极高", "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "13. 心包积液（少量）14. 肾上腺结节（左侧）", "手术名称：", "手术日期：", "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "III级(NYHA分级) 10. 甲状腺功能减退症", "11. 高血压2级（极高危）12. 肺气肿(局", "限性) 13. 肺诊断性影像检查的异常所见(肺", "结节) 14. 二尖瓣反流(重度) 15. 心包积", "液(少量) 16. 肾上腺结节(左侧)", "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "第 1 页"]
2026-08-10 16:14:14,059 INFO     29 [qwen-vl-parser] page=2 text: 38 lines (bbox 3-40)
2026-08-10 16:14:14,059 INFO     29 [qwen-vl-parser] page=2 text: 38 sections
2026-08-10 16:14:14,185 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1111275, prompt_len=764
2026-08-10 16:14:15,478 INFO     29 [qwen-vl-parser] classify API response (len=55):
```json
{
  "type": "text",
  "report_date": null
}
```
2026-08-10 16:14:15,479 INFO     29 [qwen-vl-parser] page=3 classify=text report_date=None
2026-08-10 16:14:15,506 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1111275, prompt_len=401
2026-08-10 16:14:16,753 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:14:16.752+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:14:25,858 INFO     29 [qwen-vl-parser] text API response (len=1500):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "化。", "诊疗经过：", "患者入院完善相关检查：", "【检验】", "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "*游离甲状腺素 9.58 pmol/L↓。", "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "血小板计数 112 ×10^9/L↓。", "余未见明显异常。", "【检查】", "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "第 2 页"]
2026-08-10 16:14:25,859 INFO     29 [qwen-vl-parser] page=3 text: 36 lines (bbox 41-76)
2026-08-10 16:14:25,859 INFO     29 [qwen-vl-parser] page=3 text: 36 sections
2026-08-10 16:14:25,978 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885298, prompt_len=764
2026-08-10 16:14:27,253 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:14:27,254 INFO     29 [qwen-vl-parser] page=4 classify=text report_date=None
2026-08-10 16:14:27,269 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=885298, prompt_len=401
2026-08-10 16:14:32,424 INFO     29 [qwen-vl-parser] text API response (len=952):
["3/4", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "姓名 住院号", "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "诊。", "【诊疗经过】", "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "出院。", "出院情况： 好转", "伤口愈合：-", "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "痛。双下肢无明显水肿。", "出院医嘱：", "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "2、出院后继续用药", "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "素，内分泌科随诊调药）", "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "诊随诊。", "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "间治疗，请提前一周至杨阳主任医师门诊预约。", "5、不适门诊随诊。", "不存在尚未回归的病理检查结果。", "X光片号：-", "CT号： P049684", "MRI号：-", "病理号：-", "上级医师：", "医师：", "第 3 页"]
2026-08-10 16:14:32,425 INFO     29 [qwen-vl-parser] page=4 text: 38 lines (bbox 77-114)
2026-08-10 16:14:32,425 INFO     29 [qwen-vl-parser] page=4 text: 38 sections
2026-08-10 16:14:32,575 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051018, prompt_len=764
2026-08-10 16:14:33,889 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:14:33,890 INFO     29 [qwen-vl-parser] page=5 classify=text report_date=None
2026-08-10 16:14:33,908 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1051018, prompt_len=401
2026-08-10 16:14:36,215 INFO     29 [qwen-vl-parser] text API response (len=392):
["河北省人民医院", "病理检查报告单", "病理号", "姓名:", "性别:女", "年龄:74岁", "送检单位:本院", "科别:胸外二科病区", "住院号", "床号:", "送检日期:2025-05-23 16:44", "送检材料:左肺穿刺数条:", "临床诊断:左肺占位", "图像:", "大体检查:", "(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。", "病理诊断:", "(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。", "诊断医师:", "郑国卿王彤彤", "日期:2025-05-26 14:23", "注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183", "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。", "住院病历"]
2026-08-10 16:14:36,216 INFO     29 [qwen-vl-parser] page=5 text: 24 lines (bbox 115-138)
2026-08-10 16:14:36,216 INFO     29 [qwen-vl-parser] page=5 text: 24 sections
2026-08-10 16:14:36,446 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1166882, prompt_len=764
2026-08-10 16:14:37,804 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-05-27"}
```
2026-08-10 16:14:37,805 INFO     29 [qwen-vl-parser] page=6 classify=text report_date=2025-05-27
2026-08-10 16:14:37,814 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1166882, prompt_len=401
2026-08-10 16:14:40,211 INFO     29 [qwen-vl-parser] text API response (len=457):
["河北省人民医院", "病理检查补充报告单", "病理号:", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号:", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "补充病理诊断:", "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "诊断医师: 康林 郑国娜", "报告日期: 2025-05-27 16:", "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)", "河北省人民医院", "住院病历"]
2026-08-10 16:14:40,211 INFO     29 [qwen-vl-parser] page=6 text: 22 lines (bbox 139-160)
2026-08-10 16:14:40,211 INFO     29 [qwen-vl-parser] page=6 text: 22 sections
2026-08-10 16:14:40,319 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906121, prompt_len=764
2026-08-10 16:14:41,687 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2026-03-11"}
```
2026-08-10 16:14:41,687 INFO     29 [qwen-vl-parser] page=7 classify=text report_date=2026-03-11
2026-08-10 16:14:41,696 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=906121, prompt_len=401
2026-08-10 16:14:47,842 INFO     29 [qwen-vl-parser] text API response (len=1114):
["<", "南京鼓楼医院云胶片", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "影像检查诊断报告", "互联网医院", "电子影像", "检查号:", "患者类型: 住院", "患者编号:", "姓名:", "性别: 女", "年龄: 75岁", "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "病床:", "检查日期: 2026-03-11 13:39:06", "设备类型: CT", "技师: 王雨晓", "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "检查所见:", "颈部软组织CT平扫+增强:", "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "明显异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "未见明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强:", "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "肺上叶局部透亮区。", "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "上腹部、下腹部、盆腔CT平扫+增强:", "报告日期: 2026-03-11 15:35:37", "诊断医师: 申欣怡", " / 申欣怡", "审核日期: 2026-03-12 13:17:06", "审核医师: 王国", "（本报告仅供临床医生参考）", "南京市中山路321号"]
2026-08-10 16:14:47,842 INFO     29 [qwen-vl-parser] page=7 text: 50 lines (bbox 161-210)
2026-08-10 16:14:47,842 INFO     29 [qwen-vl-parser] page=7 text: 50 sections
2026-08-10 16:14:47,933 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=533615, prompt_len=764
2026-08-10 16:14:48,606 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:14:48.604+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:14:49,219 INFO     29 [qwen-vl-parser] classify API response (len=57):
```json
{"type": "text", "report_date": "2025-10-08"}
```
2026-08-10 16:14:49,219 INFO     29 [qwen-vl-parser] page=8 classify=text report_date=2025-10-08
2026-08-10 16:14:49,238 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=533615, prompt_len=401
2026-08-10 16:14:52,293 INFO     29 [qwen-vl-parser] text API response (len=542):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "报告 2025-10-08", "影像描述", "颈部软组织CT平扫+增强：", "【所见咽部】所见咽腔结构对称，未见明显异常", "密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称，会厌、声带、", "梨状窝形态及密度未见明显异常。增强后未见明显", "异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "异常。增强后未见明显异常强化。", "【气管及食管】气管居中，管腔通畅；食管颈段", "管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "影。增强后未见明显异常强化。", "【淋巴结】未见明显肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强：", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-10 16:14:52,293 INFO     29 [qwen-vl-parser] page=8 text: 29 lines (bbox 211-239)
2026-08-10 16:14:52,293 INFO     29 [qwen-vl-parser] page=8 text: 29 sections
2026-08-10 16:14:52,382 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=578473, prompt_len=764
2026-08-10 16:14:53,703 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:14:53,704 INFO     29 [qwen-vl-parser] page=9 classify=text report_date=None
2026-08-10 16:14:53,711 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=578473, prompt_len=401
2026-08-10 16:14:59,181 INFO     29 [qwen-vl-parser] text API response (len=618):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "密度影。两肺多发结节，较大者：右肺上叶（Img7", "9）见一实性结节影，大小约5mm×3mm。两肺索", "条及片絮影；右肺上叶局部透亮区。", "【肺门】双肺门多发小淋巴结，部分稍大。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "症，病灶周围结节影。", "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "稍大，较大者短径约10mm。", "【心脏及大血管】心影增大；主动脉及冠状动", "脉壁见致密影。", "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "积液：否。增强后未见明显异常强化。", "【膈肌】光整，未见明显异常抬高。增强后未见", "明显异常强化。", "【胸壁】胸廓对称，骨质未见明显异常。增强后", "未见明显异常强化。", "上腹部CT平扫+增强：", "【肝脏】各叶比例在正常范围内，外形轮廓规", "则，肝内小圆形无强化低密度影，较大者长径约6", "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "0）。", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-10 16:14:59,182 INFO     29 [qwen-vl-parser] page=9 text: 31 lines (bbox 240-270)
2026-08-10 16:14:59,183 INFO     29 [qwen-vl-parser] page=9 text: 31 sections
2026-08-10 16:14:59,281 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=580959, prompt_len=764
2026-08-10 16:15:00,541 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:15:00,542 INFO     29 [qwen-vl-parser] page=10 classify=text report_date=None
2026-08-10 16:15:00,560 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=580959, prompt_len=401
2026-08-10 16:15:04,063 INFO     29 [qwen-vl-parser] text API response (len=633):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "扩张。", "【胰腺】形态、大小正常，实质内未见明显异常", "密度影；胰管未见明显扩张。增强后未见明显异常", "强化。", "【脾脏】形态、大小正常，实质内未见明显异常", "密度影。增强后未见明显异常强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "下腹部CT平扫+增强：", "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "见明显异常强化。", "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "节，长径约12mm,可见强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "盆腔CT平扫+增强：", "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "明显异常密度影。增强后未见明显异常强化。", "【子宫及附件】子宫呈肌组织结构性空扫", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-10 16:15:04,063 INFO     29 [qwen-vl-parser] page=10 text: 32 lines (bbox 271-302)
2026-08-10 16:15:04,063 INFO     29 [qwen-vl-parser] page=10 text: 32 sections
2026-08-10 16:15:04,152 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555271, prompt_len=764
2026-08-10 16:15:05,487 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:15:05,488 INFO     29 [qwen-vl-parser] page=11 classify=text report_date=None
2026-08-10 16:15:05,504 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=555271, prompt_len=401
2026-08-10 16:15:09,073 INFO     29 [qwen-vl-parser] text API response (len=589):
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "诊断意见", "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "巴结，部分较前稍缩小。", "2.两肺多发结节，较前变化不大，密切随诊。", "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "解；右肺上叶局限性肺气肿。", "4.心影增大；主动脉及冠状动脉壁钙化。", "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "（薄层im290），较前相仿，随诊。", "6.肝内外胆管轻度扩张。", "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "查；右肾小结石。", "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "节。", "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "内容物多；十二指肠降部憩室；结合临床体征随", "诊。", "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "以上椎体I°滑脱。", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]
2026-08-10 16:15:09,074 INFO     29 [qwen-vl-parser] page=11 text: 30 lines (bbox 303-332)
2026-08-10 16:15:09,076 INFO     29 [qwen-vl-parser] page=11 text: 30 sections
2026-08-10 16:15:09,217 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=645107, prompt_len=764
2026-08-10 16:15:10,459 INFO     29 [qwen-vl-parser] classify API response (len=49):
```json
{"type": "text", "report_date": null}
```
2026-08-10 16:15:10,459 INFO     29 [qwen-vl-parser] page=12 classify=text report_date=None
2026-08-10 16:15:10,476 INFO     29 [qwen-vl-parser] text API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=645107, prompt_len=401
2026-08-10 16:15:12,259 INFO     29 [qwen-vl-parser] text API response (len=317):
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "互联网医院", "门诊病历", "姓名:", "性别:女", "年龄:75岁", "ID:", "预约挂号", "2026年03月16日15时20分 (江北)心血管内科门诊", "主诉:要求进行心功能分级", "病史:患者平时正常活动不受限。", "过敏史:无吸烟史", "药物过敏史。无流行病学史", "体查:", "级)", "诊断:", "1.心功能I级(NYHA分", "2.高脂血症", "处理:随诊", "1.非诺贝特胶囊(力平之)", "200mg/粒", "用法:1粒", "口服", "一次/日", "x3盒 28天", "医师:", "齐", "第1页"]
2026-08-10 16:15:12,260 INFO     29 [qwen-vl-parser] page=12 text: 29 lines (bbox 333-361)
2026-08-10 16:15:12,261 INFO     29 [qwen-vl-parser] page=12 text: 29 sections
2026-08-10 16:15:12,428 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1057984, prompt_len=764
2026-08-10 16:15:13,773 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-10 16:15:13,773 INFO     29 [qwen-vl-parser] page=13 classify=table report_date=2026-03-10
2026-08-10 16:15:13,787 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1057984, prompt_len=756
2026-08-10 16:15:17,859 INFO     29 [qwen-vl-parser] table API response (len=813):
\begin{tabular}{cccccc}
\hline
\multicolumn{2}{c}{\textbf{检验项目}} & \textbf{结果} & \textbf{参考区间-单位} & \multicolumn{2}{c}{\textbf{检验项目}} \\
\hline
*白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & 31.4 \\
中性粒细胞百分数 & & 74.5 & 40--75 \% & *平均红细胞血红蛋白浓度 & 332 \\
淋巴细胞百分数 & ↓ & 16.1 & 20--50 \% & 红细胞体积分布宽度 & 13.6 \\
单核细胞百分数 & & 6.9 & 3--10 \% & *血小板计数 & 179 \\
嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \% & & \\
嗜碱性粒细胞百分数 & & 0.8 & 0--1 \% & & \\
中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & \\
淋巴细胞绝对值 & ↓ & 0.7 & 1.1--3.2 10^9/L & & \\
单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & \\
嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & \\
嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & \\
*红细胞计数 & & 4.01 & 3.8--5.1 10^12/L & & \\
*血红蛋白量 & & 126 & 115--150 g/L & & \\
*红细胞压积 & & 38.0 & 35--45 \% & & \\
*平均红细胞体积 & & 94.7 & 82--100 fl & & \\
\hline
\end{tabular}
2026-08-10 16:15:17,863 INFO     29 [qwen-vl-parser] page=13 table: 22 LaTeX lines (bbox 362-383)
2026-08-10 16:15:17,863 INFO     29 [qwen-vl-parser] page=13 table: 22 sections
2026-08-10 16:15:17,975 INFO     29 [qwen-vl-parser] classify API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892009, prompt_len=764
2026-08-10 16:15:19,455 INFO     29 [qwen-vl-parser] classify API response (len=64):
```json
{
  "type": "table",
  "report_date": "2026-03-10"
}
```
2026-08-10 16:15:19,456 INFO     29 [qwen-vl-parser] page=14 classify=table report_date=2026-03-10
2026-08-10 16:15:19,482 INFO     29 [qwen-vl-parser] table API call start, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=892009, prompt_len=756
2026-08-10 16:15:20,462 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:15:20.461+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:15:38,036 INFO     29 [qwen-vl-parser] table API response (len=3994):
\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{南京鼓楼医院 检验科报告单}} \\
\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\
\multicolumn{8}{c}{苏HR} \\
\hline
\textbf{姓名:} & \textbf{名:} & \textbf{病历号:} & \multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \textbf{样本号::} & \multicolumn{2}{l}{} \\
\textbf{性别:} & \textbf{女:} & \textbf{科室:} & \multicolumn{2}{l}{(江北)综合肿瘤中} & \textbf{条码号::} & \multicolumn{2}{l}{} \\
\textbf{年龄:} & \textbf{75岁} & \textbf{床号:} & \multicolumn{2}{l}{标本种类: 血液} & \textbf{标本说明:} & \multicolumn{2}{l}{} \\
\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\
\hline
\multicolumn{2}{c}{\textbf{检验项目}} & \multicolumn{2}{c}{\textbf{结果}} & \multicolumn{2}{c}{\textbf{参考区间-单位}} & \multicolumn{2}{c}{\textbf{检验项目}} & \multicolumn{2}{c}{\textbf{结果}} & \multicolumn{2}{c}{\textbf{参考区间-单位}} \\
\hline
*丙氨酸氨基转移酶 & $\uparrow$ & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\
*天门冬氨酸氨基转移酶 & $\uparrow$ & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\
*碱性磷酸酶 & $\downarrow$ & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\
*γ-谷氨酰基转移酶 & $\uparrow$ & 130.5 & 7---45 U/L & *甘油三酯 & $\uparrow$ & 2.88 & $\leqslant$1.7 mmol/L \\
*乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & $\uparrow$ & 5.81 & 3---5.7 mmol/L \\
*总胆红素 & 10.2 & $\leqslant$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\
*直接胆红素 & 3.3 & $\leqslant$4 umol/L & *L-脂蛋白胆固醇 & $\uparrow$ & 3.66 & 健康人<3.4; 不同ASCVD危 \\
*胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\
*总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\
*白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\
*球蛋白 & 30.1 & 20---40 g/L & & & & \\
白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\
*总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & $\uparrow$ & 1.15 & 0.6---1.1 g/L \\
亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\
*腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\
*葡萄糖 & $\uparrow$ & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\
*尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\
& & & & *氯 & 101.7 & 99---110 mmol/L \\
\hline
\multicolumn{8}{l}{检验意见:} \\
\hline
\multicolumn{4}{l}{送检医生: 杨阳} & \multicolumn{2}{l}{检验者: 柏玉} & \multicolumn{2}{l}{审核者: 余安光} \\
\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\
\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\
\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\
\multicolumn{8}{l}{注: $\uparrow$-偏高, $\downarrow$-偏低, ★-危急值结果} \\
\hline
\end{tabular}

\begin{tabular}{llllllll}
\hline
\multicolumn{8}{c}{\textbf{南京鼓楼医院 检验科报告单}} \\
\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\
\multicolumn{8}{c}{苏HR} \\
\hline
\textbf{姓名:} & \textbf{名:} & \textbf{病历号:} & \multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \textbf{样本号} & \multicolumn{2}{l}{} \\
\textbf{性别:} & \textbf{女:} & \textbf{科室:} & \multicolumn{2}{l}{(江北)综合肿瘤中} & \textbf{条码号} & \multicolumn{2}{l}{} \\
\textbf{年龄:} & \textbf{75岁} & \textbf{床号:} & \multicolumn{2}{l}{标本种类: 血液} & \textbf{标本说明:} & \multicolumn{2}{l}{} \\
\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\
\hline
\multicolumn{2}{c}{\textbf{检验项目}} & \multicolumn{2}{c}{\textbf{结果}} & \multicolumn{2}{c}{\textbf{参考区间-单位}} & \multicolumn{2}{c}{\textbf{检验项目}} & \multicolumn{2}{c}{\textbf{结果}} & \multicolumn{2}{c}{\textbf{参考区间-单位}} \\
\hline
*C反应蛋白 & $\uparrow$ & 11.2 & 0---6 mg/L & & & & & & & & \\
*肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\
肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\
*a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\
eGFR (CKD-EPI) & $\downarrow$ & 69.6 & $>$90 ml/min/1.73m$^2$ & & & & & & & & \\
\hline
\multicolumn{8}{l}{检验意见:} \\
\hline
\multicolumn{4}{l}{送检医生: 杨阳} & \multicolumn{2}{l}{检验者: 柏玉} & \multicolumn{2}{l}{审核者: 余安光} \\
\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\
\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\
\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\
\multicolumn{8}{l}{注: $\uparrow$-偏高, $\downarrow$-偏低, ★-危急值结果} \\
\hline
\end{tabular}
2026-08-10 16:15:38,037 INFO     29 [qwen-vl-parser] page=14 table: 71 LaTeX lines (bbox 384-454)
2026-08-10 16:15:38,037 INFO     29 [qwen-vl-parser] page=14 table: 71 sections
2026-08-10 16:15:38,037 INFO     29 [qwen-vl-parser] parse_pdf done: 455 sections from 14 pages.
2026-08-10 16:15:38,045 INFO     29 Close text detector.
2026-08-10 16:15:38,458 INFO     29 Close text recognizer.
2026-08-10 16:15:38,886 INFO     29 Close recognizer.
2026-08-10 16:15:39,307 INFO     29 Close recognizer.
2026-08-10 16:15:40,099 INFO     29 [Pipeline] Component [1]: Parser:MedLink finished. error=None
2026-08-10 16:15:40,099 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Parser:MedLink | outputs={"html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "json"}
2026-08-10 16:15:40,099 INFO     29 [Pipeline] Executing component [2]: SmartSplitter:MedLink (type=SmartSplitter)
2026-08-10 16:15:40,134 INFO     29 [LLM] SmartSplitter call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:15:40,134 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档切分与分类专家。下面是一份完整的 OCR 扫描医疗文档，可能包含多种不同类型的文档内容混排在一起。\n\n重要：文档中每个文本块都有编号前缀 [BBOX-0], [BBOX-1], ... [BBOX-N]，这是文档的阅读顺序索引。\n\n请你：\n1. 按照医疗文档类型的语义边界进行切分——每个片段只包含一种文档类型\n2. 同时给每个切分片段分类并提取元数据\n3. 返回每个片段的 bbox 索引范围（bbox_start 和 bbox_end）\n4. 【强制要求】必须从[BBOX-0]逐个扫描到[BBOX-N]（文档末尾），不得遗漏任何符合条件的片段\n- 同一类型的文档可能出现多次，每个都必须识别并返回\n- 不要在处理完前几个segment后就停止扫描\n- 特别注意：每种类型文档可能有多份，必须全部识别\n\n## 文档类型定义\n\n### OutpatientRecord（门诊病历）\n完整的门诊就诊记录，核心特征：有就诊时间 + 主诉/现病史/诊断/处理意见等临床要素。\n- 通常以\"XX医院门诊病历\"或\"门诊复诊病历记录\"开头\n- 从\"就诊时间\"到\"医生签名\"或\"处理意见\"结束是一个完整记录\n- ⚠️ 门诊病历中提到的辅助检查结果（如\"ESR 50mm/h\"）是病历正文的一部分，不要把它切出来当作独立的 LabReport\n\n### PrescriptionRecord（处方用药/取药执行单）\n医院开具的处方或取药执行单。核心特征：有就诊科室 + 就诊医生 + 疾病诊断 + 药品用法用量。\n- 通常以\"XX医院 取药执行单\"开头\n- 包含：就诊科室、就诊医生、诊断、药品名称、剂量、频次、给药途径\n- 每张独立的取药执行单/处方是一个片段\n⚠️ HIS界面截图是医疗文档，不得跳过。含 药品明细 + 开立医师 + 科室 → PrescriptionRecord（即使无诊断、无标题）；仅药品清单 → MedicationRecord。\ntab/搜索框/分页等 UI 元素非内容，忽略即可。\n+ ⚠️ 命中以下表头即强制 PrescriptionRecord：文本含\"药品名称\"（或\"药品名称[规格]\"/\"(规格)\"）+ \"用法\" + \"频率\" + \"开立时间\" + \"开立医师\"列名，且表格行为药品记录。此类页面即使无诊断/无标题也必切。\n+ UI 噪音（忽略）：\"请输入药品内容,按回车键检索\"、\"查询全部\"、\"共70条 20条/页\"、\"前往 N 页\"、\"集成视图 诊断 病历文书 处方 检验...\"标签栏、\"CS 扫描全能王\"。\n⚠️ 区分要点：如果文档含有\"收款\"+\"操作员\"+\"凭条仅为…交款依据\"等交款凭条特征，\n但缺少\"疾病诊断\"且无\"取药执行单\"标题 → 应归为 MedicationRecord，不是 PrescriptionRecord。\n医院缴费/交款凭条虽然有科室和医生信息，但本质是购药付款凭证。\n\n### MedicationRecord（购药凭证）\n药店或医院购药的付款凭证。核心特征：有付款金额 + 药品清单，但无医生诊断和用法用量。\n- 药房/药店购药小票：含药单编号、收银员、品名、规格、零售价、数量、应收金额\n- 医院收费票据：含\"收费员\"\"收款\"字样\n- 医疗门诊收费票据\n- 电子发票：含\"大药房\"，\"药品名称\"，\"金额\" 等字段\n- 订单详情：含\"项目名称\"，\"规格型号\"，\"金额\" 等字段\n- **切分规则（强制）**：\n  - 按购药日期切分，每个不同日期的购药凭证必须是独立的 segment\n  - 关键识别特征：购药时间（YYYY-MM-DD HH:MM:SS）、药单编号、药店名称\n  - 即使两张购药凭证在物理页面上连续，只要购药时间不同，必须分为两个 segment\n  - 每个 segment 只包含一个购药时间点的记录\n\n### LabReport（检验报告）\n医院检验科出具的检验报告单。核心特征：有检验项目 + 检验结果 + 参考范围。\n- 通常以\"XX医院检验报告单\"或直接以检验项目表格开头\n- 包含多个检验指标和参考范围\n\n### DischargeRecord（出院记录/出院小结）\n住院出院记录或出院小结。核心特征：出院诊断 + 出院医嘱 + 住院经过。\n- 即使包含检验数据（如ESR、CRP等数值），只要有\"出院诊断\"和\"出院医嘱\"→ DischargeRecord\n\n### AdmissionRecord（入院记录）\n住院入院记录或住院病历。核心特征：入院时间 + 主诉 + 现病史 + 详细体格检查 + 初步诊断。\n- 通常以\"入院记录\"或\"住院病历\"标题开头\n- 包含完整体格检查（体温/脉搏/呼吸/血压 + 头颈心肺腹四肢神经系统逐一检查）和初步诊断\n- 区别于门诊病历：入院记录有完整的系统体格检查、个人史、婚育史、家族史，门诊病历通常没有\n- 区别于出院记录：入院记录有\"初步诊断\"（无\"出院诊断\"），有体格检查（无\"诊疗经过\"和\"出院医嘱\"）\n- 入院记录可能跨越多页，不要拆开（从入院信息到初步诊断是一个完整记录）\n\n### ProgressNote（病程记录）\n住院期间的连续性病程文书：首次病程记录、日常病程记录、查房记录（主治医师/主任医师/副主任医师）、术前小结、术后首次病程记录、VTE防治病程记录、会诊记录、转科记录、阶段小结、抢救记录等。核心特征：记录时间（YYYY-MM-DD HH:MM）+ 病情与诊疗叙述 + 医师签名。\n- 通常以\"病程记录\"页眉、\"首次病程记录\"、\"查房记录\"、\"术前小结\"等标题开头，或有\"YYYY-MM-DD HH:MM + 记录类型\"格式的行首时间戳\n- ⚠️病程记录是独立文书：即使紧跟在入院记录页之后，也**不得**并入 AdmissionRecord，**不得**归入 DischargeRecord，必须单独成段\n- **每条病程记录独立成一个 ProgressNote 片段**：以记录时间（YYYY-MM-DD HH:MM）或类型标题（首次病程记录/查房记录/术前小结等）为分界，遇到下一条记录的起始标记即切开\n- 单条记录跨页时合并为一个片段（不要拆开）；但**禁止把多条不同记录合并为一个片段**，record_count 恒为 1\n\n### ExaminationReport（检查报告）\n影像检查、心电图、超声、CT/MRI、病理检查等辅助检查报告。核心特征：有检查日期 + 检查所见/影像表现 + 检查结论/意见。\n- 通常以\"XX医院检查报告\"、\"影像报告\"、\"病理检查报告单\"、\"医学影像检查报告单\"、\"心电图报告\"开头\n- 包含检查所见（影像表现/大体检查/镜下所见）和检查结论（意见/诊断意见/病理诊断）\n- 同一份检查报告（含多页）不要拆开\n- ⚠️ 区分于 LabReport：LabReport 是检验报告，有检验项目+数值+参考范围的表格结构；ExaminationReport 是检查报告，以叙述性描述为主\n- ⚠️ 有主诉，病史但是没有出院时间，入院时间的，是OutpatientRecord（门诊病历），不是ExaminationReport（检查报告）\n\n## 忽略的内容（不切分、不输出）\n以下内容不属于临床医疗文档，直接跳过，不要为其生成切分片段：\n- 微信/支付宝支付凭证（OCR 文本包含\"支付成功\"+\"交易单号\"+\"财付通支付科技有限公司\"或\"支付宝\"等关键词，但不包含药品名称、规格、数量、单价）\n- 临床照片（患者手/足/关节等照片页，无文字内容或仅有少量 OCR 碎片）\n\n## 输出格式\n严格输出纯 JSON 数组，格式：[{...}, {...}, ...]，禁止 ```json 代码块。每个元素：\n{\n  \"type\": \"<文档类型>\",\n  \"bbox_start\": <起始 bbox 编号>,\n  \"bbox_end\": <结束 bbox 编号>,\n  \"row_start\": <表格内起始行号（可选）>,\n  \"row_end\": <表格内结束行号（可选）>,\n  \"encounter_dates\": [\"YYYY-MM-DD\"],\n  \"department\": \"<科室名称|null>\",\n  \"record_count\": 1\n}\n\n**bbox_start 和 bbox_end 是整数，表示该片段包含的 bbox 索引范围（inclusive）。**\n例如：`\"bbox_start\": 0, \"bbox_end\": 5` 表示该片段包含 [BBOX-0] 到 [BBOX-5] 的所有文本块。\n\n**row_start 和 row_end（可选）：** 当一个表格 bbox 内包含多个独立记录时使用。\n- 表格行有 [BBOX-N-R0], [BBOX-N-R1], ... 标记\n- row_start/row_end 指定该片段在表格内的行范围（inclusive）\n- 例如：一个表格 [BBOX-415] 包含两张购药小票，第一张是 R0-R24，第二张是 R25-R49\n  → 第一个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 0, \"row_end\": 24}\n  → 第二个片段：{\"bbox_start\": 415, \"bbox_end\": 415, \"row_start\": 25, \"row_end\": 49}\n- 如果表格只有一个记录（不需要拆分），不需要返回 row_start/row_end\n- 如果 bbox 不是表格（没有 R 标记），不需要返回 row_start/row_end\n\n## 切分规则\n1. 每次门诊就诊是一个独立片段。从\"就诊时间\"到\"处理意见/医生签名\"是一个完整记录——不要拆开，也不要把不同日期的多次就诊合并。\n2. 检验报告按\"检验日期 + 报告单\"切分——每份独立的检验报告单是一个片段（如：血常规报告单、肝功能报告单、血沉报告单各自独立）；同一份报告单含多页表格时不要拆开\n3. 购药凭证和取药执行单各自独立——每张票据/执行单是一个独立片段（不同日期或不同单号 = 不同片段），二者是不同的 type\n4. 出院记录不要拆开\n5. 病程记录（ProgressNote）独立成段——首次病程记录、查房记录、术前小结、术后首次病程记录、VTE防治病程记录等按连续区域切分，禁止并入入院记录或出院记录\n6. 如果文档末尾有几个字的残留碎片（<50字），合并到前一个片段\n7. 如果一个表格 bbox 内包含多个独立记录（如两张购药小票、两份检验报告），用 row_start/row_end 指定每个记录的行范围，而不是把整个表格作为一个片段。行号参考表格内的 [BBOX-N-Rn] 标记。\n8. 同一份检查报告（影像/病理/心电图）不要拆开\n\n## OCR 常见误识别纠正（切分和分类时参考）\nOCR 扫描可能导致药品名称识别错误，以下是本数据集常见的 OCR 错误，切分时请注意：\n- \"阿运木单抗\" → 应理解为\"阿达木单抗\"（adalimumab）\n- \"来氟未胺\" → 应理解为\"来氟米特\"（leflunomide）\n- \"甲氨喋呤\" → 应理解为\"甲氨蝶呤\"（methotrexate）\n- \"塞来昔布胺囊\" → 应理解为\"塞来昔布胶囊\"（celecoxib）\n- \"类风显性关节炎\" → 应理解为\"类风湿性关节炎\"（rheumatoid arthritis）\n- \"美洛昔庚\" → 应理解为\"美洛昔康\"（meloxicam）\n\n纠正原则：\n1. 仅纠正高置信度的标准医学术语\n2. 不确定的不要纠正\n3. 纠正后的文本应保持原文的语义和结构\n\n## 日期提取规则\n- 从文本中提取实际日期，格式 YYYY-MM-DD\n- 如果日期无法识别（OCR损坏），使用空数组 []\n- 不要猜测日期"
  },
  {
    "role": "user",
    "content": "[BBOX-0] 2025.5.21确诊小细胞肺癌\n[BBOX-1] 2025.5.28-2025.7.16 依托泊苷+卡铂+斯鲁利\n[BBOX-2] 2025.8.13-2025.11.7 依托泊苷+斯鲁利\n[BBOX-3] 南京鼓楼医院\n[BBOX-4] 南京大学医学院附属鼓楼医院\n[BBOX-5] 出院记录\n[BBOX-6] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名\n[BBOX-7] 住院号\n[BBOX-8] 姓名：\n[BBOX-9] 性别：女 年龄：75岁 婚姻：已婚 职业：农民\n[BBOX-10] 入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日\n[BBOX-11] 厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门\n[BBOX-12] 淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋\n[BBOX-13] 下淋巴结肿大（右）7. 心功能III级（NYHA分级）\n[BBOX-14] 8. 甲状腺功能减退症 9. 高血压2级（极高\n[BBOX-15] 危）10. 肺气肿（局限性）11. 肺诊断性影像检\n[BBOX-16] 查的异常所见（肺结节）12. 二尖瓣反流（重度）\n[BBOX-17] 13. 心包积液（少量）14. 肾上腺结节（左侧）\n[BBOX-18] 手术名称：\n[BBOX-19] 手术日期：\n[BBOX-20] 出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日\n[BBOX-21] 疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）\n[BBOX-22] 4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大\n[BBOX-23] 6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大\n[BBOX-24] (双侧) 8. 腋下淋巴结肿大(右) 9. 心功能\n[BBOX-25] III级(NYHA分级) 10. 甲状腺功能减退症\n[BBOX-26] 11. 高血压2级（极高危）12. 肺气肿(局\n[BBOX-27] 限性) 13. 肺诊断性影像检查的异常所见(肺\n[BBOX-28] 结节) 14. 二尖瓣反流(重度) 15. 心包积\n[BBOX-29] 液(少量) 16. 肾上腺结节(左侧)\n[BBOX-30] 入院时情况（主要症状、体征，有关实验室及器械检查结果）：\n[BBOX-31] 患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除\n[BBOX-32] 外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大\n[BBOX-33] 淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回\n[BBOX-34] 示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，\n[BBOX-35] CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情\n[BBOX-36] 于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于\n[BBOX-37] 2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复\n[BBOX-38] 查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07\n[BBOX-39] 行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟\n[BBOX-40] 第 1 页\n[BBOX-41] 南京鼓楼医院\n[BBOX-42] 南京大学医学院附属鼓楼医院\n[BBOX-43] 出院记录\n[BBOX-44] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号\n[BBOX-45] “肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变\n[BBOX-46] 化。\n[BBOX-47] 诊疗经过：\n[BBOX-48] 患者入院完善相关检查：\n[BBOX-49] 【检验】\n[BBOX-50] 2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，\n[BBOX-51] *游离甲状腺素 9.58 pmol/L↓。\n[BBOX-52] 2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶\n[BBOX-53] 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。\n[BBOX-54] 2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯\n[BBOX-55] 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51\n[BBOX-56] mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8\n[BBOX-57] mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。\n[BBOX-58] 2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数\n[BBOX-59] 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*\n[BBOX-60] 血小板计数 112 ×10^9/L↓。\n[BBOX-61] 余未见明显异常。\n[BBOX-62] 【检查】\n[BBOX-63] 2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支\n[BBOX-64] 阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长\n[BBOX-65] 2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺\n[BBOX-66] 门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软\n[BBOX-67] 组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上\n[BBOX-68] 考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建\n[BBOX-69] 议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左\n[BBOX-70] 肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺\n[BBOX-71] 瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度\n[BBOX-72] 欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉\n[BBOX-73] 及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可\n[BBOX-74] 能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔\n[BBOX-75] 内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑\n[BBOX-76] 第 2 页\n[BBOX-77] 3/4\n[BBOX-78] 南京鼓楼医院\n[BBOX-79] 南京大学医学院附属鼓楼医院\n[BBOX-80] 出院记录\n[BBOX-81] 科别（江北）综合肿瘤中心 病区（江北）B7病区床号\n[BBOX-82] 姓名 住院号\n[BBOX-83] 良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随\n[BBOX-84] 诊。\n[BBOX-85] 【诊疗经过】\n[BBOX-86] 患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05\n[BBOX-87] 行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理\n[BBOX-88] 出院。\n[BBOX-89] 出院情况： 好转\n[BBOX-90] 伤口愈合：-\n[BBOX-91] ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲\n[BBOX-92] 张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音\n[BBOX-93] 稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳\n[BBOX-94] 痛。双下肢无明显水肿。\n[BBOX-95] 出院医嘱：\n[BBOX-96] 1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。\n[BBOX-97] 2、出院后继续用药\n[BBOX-98] 左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激\n[BBOX-99] 素，内分泌科随诊调药）\n[BBOX-100] 3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化\n[BBOX-101] 全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门\n[BBOX-102] 诊随诊。\n[BBOX-103] 4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五\n[BBOX-104] 上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日\n[BBOX-105] 间治疗，请提前一周至杨阳主任医师门诊预约。\n[BBOX-106] 5、不适门诊随诊。\n[BBOX-107] 不存在尚未回归的病理检查结果。\n[BBOX-108] X光片号：-\n[BBOX-109] CT号： P049684\n[BBOX-110] MRI号：-\n[BBOX-111] 病理号：-\n[BBOX-112] 上级医师：\n[BBOX-113] 医师：\n[BBOX-114] 第 3 页\n[BBOX-115] 河北省人民医院\n[BBOX-116] 病理检查报告单\n[BBOX-117] 病理号\n[BBOX-118] 姓名:\n[BBOX-119] 性别:女\n[BBOX-120] 年龄:74岁\n[BBOX-121] 送检单位:本院\n[BBOX-122] 科别:胸外二科病区\n[BBOX-123] 住院号\n[BBOX-124] 床号:\n[BBOX-125] 送检日期:2025-05-23 16:44\n[BBOX-126] 送检材料:左肺穿刺数条:\n[BBOX-127] 临床诊断:左肺占位\n[BBOX-128] 图像:\n[BBOX-129] 大体检查:\n[BBOX-130] (左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。\n[BBOX-131] 病理诊断:\n[BBOX-132] (左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。\n[BBOX-133] 诊断医师:\n[BBOX-134] 郑国卿王彤彤\n[BBOX-135] 日期:2025-05-26 14:23\n[BBOX-136] 注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183\n[BBOX-137] 2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。\n[BBOX-138] 住院病历\n[BBOX-139] 河北省人民医院\n[BBOX-140] 病理检查补充报告单\n[BBOX-141] 病理号:\n[BBOX-142] 姓名:\n[BBOX-143] 性别: 女\n[BBOX-144] 年龄: 74岁\n[BBOX-145] 送检单位: 本院\n[BBOX-146] 科别: 胸外二科病区\n[BBOX-147] 住院号:\n[BBOX-148] 床号:\n[BBOX-149] 送检日期: 2025-05-23 16:44\n[BBOX-150] 送检材料: 左肺穿刺数条:\n[BBOX-151] 临床诊断: 左肺占位\n[BBOX-152] 补充病理诊断:\n[BBOX-153] (左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。\n[BBOX-154] 免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6\n[BBOX-155] (-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。\n[BBOX-156] 诊断医师: 康林 郑国娜\n[BBOX-157] 报告日期: 2025-05-27 16:\n[BBOX-158] 注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)\n[BBOX-159] 河北省人民医院\n[BBOX-160] 住院病历\n[BBOX-161] <\n[BBOX-162] 南京鼓楼医院云胶片\n[BBOX-163] 南京鼓楼医院\n[BBOX-164] 南京大学医学院附属鼓楼医院\n[BBOX-165] 影像检查诊断报告\n[BBOX-166] 互联网医院\n[BBOX-167] 电子影像\n[BBOX-168] 检查号:\n[BBOX-169] 患者类型: 住院\n[BBOX-170] 患者编号:\n[BBOX-171] 姓名:\n[BBOX-172] 性别: 女\n[BBOX-173] 年龄: 75岁\n[BBOX-174] 科别: (江北)综合肿瘤中心 病区: (江北)B7病区\n[BBOX-175] 病床:\n[BBOX-176] 检查日期: 2026-03-11 13:39:06\n[BBOX-177] 设备类型: CT\n[BBOX-178] 技师: 王雨晓\n[BBOX-179] 检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]\n[BBOX-180] 检查所见:\n[BBOX-181] 颈部软组织CT平扫+增强:\n[BBOX-182] 【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n[BBOX-183] 【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n[BBOX-184] 明显异常强化。\n[BBOX-185] 【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n[BBOX-186] 未见明显占位性病变。\n[BBOX-187] 【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n[BBOX-188] 【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n[BBOX-189] 【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n[BBOX-190] 【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n[BBOX-191] 【其他】副鼻窦内低密度影。\n[BBOX-192] 胸部CT平扫+增强:\n[BBOX-193] 【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n[BBOX-194] 多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n[BBOX-195] 肺上叶局部透亮区。\n[BBOX-196] 【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n[BBOX-197] 【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n[BBOX-198] 【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n[BBOX-199] 【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n[BBOX-200] 【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n[BBOX-201] 【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n[BBOX-202] 【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n[BBOX-203] 上腹部、下腹部、盆腔CT平扫+增强:\n[BBOX-204] 报告日期: 2026-03-11 15:35:37\n[BBOX-205] 诊断医师: 申欣怡\n[BBOX-206] / 申欣怡\n[BBOX-207] 审核日期: 2026-03-12 13:17:06\n[BBOX-208] 审核医师: 王国\n[BBOX-209] （本报告仅供临床医生参考）\n[BBOX-210] 南京市中山路321号\n[BBOX-211] 南京鼓楼医院云胶片\n[BBOX-212] 女/75岁\n[BBOX-213] 设备类型 CT 患者类型 无\n[BBOX-214] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-215] 腹部、盆腔）]\n[BBOX-216] PDF报告 图像 分享\n[BBOX-217] 报告 2025-10-08\n[BBOX-218] 影像描述\n[BBOX-219] 颈部软组织CT平扫+增强：\n[BBOX-220] 【所见咽部】所见咽腔结构对称，未见明显异常\n[BBOX-221] 密度影。增强后未见明显异常强化。\n[BBOX-222] 【喉部及下咽部】喉腔结构对称，会厌、声带、\n[BBOX-223] 梨状窝形态及密度未见明显异常。增强后未见明显\n[BBOX-224] 异常强化。\n[BBOX-225] 【甲状腺及甲状旁腺区】甲状腺左右叶大小、形\n[BBOX-226] 态正常，甲状腺双叶低密度结节；甲状旁腺区未见\n[BBOX-227] 明显占位性病变。\n[BBOX-228] 【唾液腺】双侧腮腺、颌下腺形态密度未见明显\n[BBOX-229] 异常。增强后未见明显异常强化。\n[BBOX-230] 【气管及食管】气管居中，管腔通畅；食管颈段\n[BBOX-231] 管壁未见明显增厚。\n[BBOX-232] 【颈部间隙】脂肪间隙清晰，未见明显异常密度\n[BBOX-233] 影。增强后未见明显异常强化。\n[BBOX-234] 【淋巴结】未见明显肿大淋巴结。\n[BBOX-235] 【其他】副鼻窦内低密度影。\n[BBOX-236] 胸部CT平扫+增强：\n[BBOX-237] 【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n[BBOX-238] 移动影像浏览\n[BBOX-239] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-240] 南京鼓楼医院云胶片\n[BBOX-241] 女/75岁\n[BBOX-242] 设备类型 CT 患者类型 无\n[BBOX-243] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-244] 腹部、盆腔）]\n[BBOX-245] PDF报告 图像 分享\n[BBOX-246] 【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n[BBOX-247] 密度影。两肺多发结节，较大者：右肺上叶（Img7\n[BBOX-248] 9）见���实性结节影，大小约5mm×3mm。两肺索\n[BBOX-249] 条及片絮影；右肺上叶局部透亮区。\n[BBOX-250] 【肺门】双肺门多发小淋巴结，部分稍大。\n[BBOX-251] 【气管及支气管】左下肺支气管闭塞伴阻塞性炎\n[BBOX-252] 症，病灶周围结节影。\n[BBOX-253] 【纵隔】纵隔居中，纵隔内多发小淋巴结，部分\n[BBOX-254] 稍大，较大者短径约10mm。\n[BBOX-255] 【心脏及大血管】心影增大；主动脉及冠状动\n[BBOX-256] 脉壁见致密影。\n[BBOX-257] 【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔\n[BBOX-258] 积液：否。增强后未见明显异常强化。\n[BBOX-259] 【膈肌】光整，未见明显异常抬高。增强后未见\n[BBOX-260] 明显异常强化。\n[BBOX-261] 【胸壁】胸廓对称，骨质未见明显异常。增强后\n[BBOX-262] 未见明显异常强化。\n[BBOX-263] 上腹部CT平扫+增强：\n[BBOX-264] 【肝脏】各叶比例在正常范围内，外形轮廓规\n[BBOX-265] 则，肝内小圆形无强化低密度影，较大者长径约6\n[BBOX-266] mm。静脉期肝左叶小片状稍低密度影（薄层im29\n[BBOX-267] 0）。\n[BBOX-268] 【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n[BBOX-269] 移动影像浏览\n[BBOX-270] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-271] 南京鼓楼医院云胶片\n[BBOX-272] 女/75岁\n[BBOX-273] 设备类型 CT 患者类型 无\n[BBOX-274] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-275] 腹部、盆腔）]\n[BBOX-276] PDF报告 图像 分享\n[BBOX-277] 【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n[BBOX-278] 增厚，囊内未见明显异常密度影；肝内外胆管轻度\n[BBOX-279] 扩张。\n[BBOX-280] 【胰腺】形态、大小正常，实质内未见明显异常\n[BBOX-281] 密度影；胰管未见明显扩张。增强后未见明显异常\n[BBOX-282] 强化。\n[BBOX-283] 【脾脏】形态、大小正常，实质内未见明显异常\n[BBOX-284] 密度影。增强后未见明显异常强化。\n[BBOX-285] 【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n[BBOX-286] 匀，未见明显肿大淋巴结，未见明显渗出及积液。\n[BBOX-287] 增强后未见明显异常强化。\n[BBOX-288] 下腹部CT平扫+增强：\n[BBOX-289] 【肾脏】两侧肾脏大小、形态、位置正常，右肾\n[BBOX-290] 窦点状致密影；肾盂肾盏未见明显扩张。增强后未\n[BBOX-291] 见明显异常强化。\n[BBOX-292] 【肾上腺】双肾上腺增粗，左肾上腺低密度结\n[BBOX-293] 节，长径约12mm,可见强化。\n[BBOX-294] 【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n[BBOX-295] 匀，未见明显肿大淋巴结，未见明显渗出及积液。\n[BBOX-296] 增强后未见明显异常强化。\n[BBOX-297] 盆腔CT平扫+增强：\n[BBOX-298] 【膀胱】充盈欠佳，壁未见明显增厚，其内未见\n[BBOX-299] 明显异常密度影。增强后未见明显异常强化。\n[BBOX-300] 【子宫及附件】子宫呈肌组织结构性空扫\n[BBOX-301] 移动影像浏览\n[BBOX-302] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-303] 南京鼓楼医院云胶片\n[BBOX-304] 女/75岁\n[BBOX-305] 设备类型 CT 患者类型 无\n[BBOX-306] 检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n[BBOX-307] 腹部、盆腔）]\n[BBOX-308] PDF报告 图像 分享\n[BBOX-309] 诊断意见\n[BBOX-310] 1.肺癌复查：左肺下叶斑片影较前（2025-07-15）\n[BBOX-311] 明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前\n[BBOX-312] 缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋\n[BBOX-313] 巴结，部分较前稍缩小。\n[BBOX-314] 2.两肺多发结节，较前变化不大，密切随诊。\n[BBOX-315] 3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓\n[BBOX-316] 解；右肺上叶局限性肺气肿。\n[BBOX-317] 4.心影增大；主动脉及冠状动脉壁钙化。\n[BBOX-318] 5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影\n[BBOX-319] （薄层im290），较前相仿，随诊。\n[BBOX-320] 6.肝内外胆管轻度扩张。\n[BBOX-321] 7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检\n[BBOX-322] 查；右肾小结石。\n[BBOX-323] 8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结\n[BBOX-324] 节。\n[BBOX-325] 9.下腹腔内肠系膜间隙多发稍大淋巴结。\n[BBOX-326] 10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠\n[BBOX-327] 内容物多；十二指肠降部憩室；结合临床体征随\n[BBOX-328] 诊。\n[BBOX-329] 11.右肩部皮下低密度结节，较前相仿，随诊；L4及\n[BBOX-330] 以上椎体I°滑脱。\n[BBOX-331] 移动影像浏览\n[BBOX-332] © 2022 南京鼓楼医院影像云平台 V1.0\n[BBOX-333] 南京鼓楼医院\n[BBOX-334] 南京大学医学院附属鼓楼医院\n[BBOX-335] 互联网医院\n[BBOX-336] 门诊病历\n[BBOX-337] 姓名:\n[BBOX-338] 性别:女\n[BBOX-339] 年龄:75岁\n[BBOX-340] ID:\n[BBOX-341] 预约挂号\n[BBOX-342] 2026年03月16日15时20分 (江北)心血管内科门诊\n[BBOX-343] 主诉:要求进行心功能分级\n[BBOX-344] 病史:患者平时正常活动不受限。\n[BBOX-345] 过敏史:无吸烟史\n[BBOX-346] 药物过敏史。无流行病学史\n[BBOX-347] 体查:\n[BBOX-348] 级)\n[BBOX-349] 诊断:\n[BBOX-350] 1.心功能I级(NYHA分\n[BBOX-351] 2.高脂血症\n[BBOX-352] 处理:随诊\n[BBOX-353] 1.非诺贝特胶囊(力平之)\n[BBOX-354] 200mg/粒\n[BBOX-355] 用法:1粒\n[BBOX-356] 口服\n[BBOX-357] 一次/日\n[BBOX-358] x3盒 28天\n[BBOX-359] 医师:\n[BBOX-360] 齐\n[BBOX-361] 第1页\n[BBOX-362] \\begin{tabular}{cccccc}\n[BBOX-363] 报告时间: 2026-03-10\n[BBOX-364] \\hline\n[BBOX-365] \\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} & \\multicolumn{2}{c}{\\textbf{检验项目}} \\\\\n[BBOX-366] \\hline\n[BBOX-367] *白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & 31.4 \\\\\n[BBOX-368] 中性粒细胞百分数 & & 74.5 & 40--75 \\% & *平均红细胞血红蛋白浓度 & 332 \\\\\n[BBOX-369] 淋巴细胞百分数 & ↓ & 16.1 & 20--50 \\% & 红细胞体积分布宽度 & 13.6 \\\\\n[BBOX-370] 单核细胞百分数 & & 6.9 & 3--10 \\% & *血小板计数 & 179 \\\\\n[BBOX-371] 嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \\% & & \\\\\n[BBOX-372] 嗜碱性粒细胞百分数 & & 0.8 & 0--1 \\% & & \\\\\n[BBOX-373] 中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & \\\\\n[BBOX-374] 淋巴细胞绝对值 & ↓ & 0.7 & 1.1--3.2 10^9/L & & \\\\\n[BBOX-375] 单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & \\\\\n[BBOX-376] 嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & \\\\\n[BBOX-377] 嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & \\\\\n[BBOX-378] *红细胞计数 & & 4.01 & 3.8--5.1 10^12/L & & \\\\\n[BBOX-379] *血红蛋白量 & & 126 & 115--150 g/L & & \\\\\n[BBOX-380] *红细胞压积 & & 38.0 & 35--45 \\% & & \\\\\n[BBOX-381] *平均红细胞体积 & & 94.7 & 82--100 fl & & \\\\\n[BBOX-382] \\hline\n[BBOX-383] \\end{tabular}\n[BBOX-384] \\begin{tabular}{llllllll}\n[BBOX-385] 报告时间: 2026-03-10\n[BBOX-386] \\hline\n[BBOX-387] \\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n[BBOX-388] \\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n[BBOX-389] \\multicolumn{8}{c}{苏HR} \\\\\n[BBOX-390] \\hline\n[BBOX-391] \\textbf{姓名:} & \\textbf{名:} & \\textbf{病历号:} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\textbf{样本号::} & \\multicolumn{2}{l}{} \\\\\n[BBOX-392] \\textbf{性别:} & \\textbf{女:} & \\textbf{科室:} & \\multicolumn{2}{l}{(江北)综合肿瘤中} & \\textbf{条码号::} & \\multicolumn{2}{l}{} \\\\\n[BBOX-393] \\textbf{年龄:} & \\textbf{75岁} & \\textbf{床号:} & \\multicolumn{2}{l}{标本种类: 血液} & \\textbf{标本说明:} & \\multicolumn{2}{l}{} \\\\\n[BBOX-394] \\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n[BBOX-395] \\hline\n[BBOX-396] \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} \\\\\n[BBOX-397] \\hline\n[BBOX-398] *丙氨酸氨基转移酶 & $\\uparrow$ & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\\\\n[BBOX-399] *天门冬氨酸氨基转移酶 & $\\uparrow$ & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\\\\n[BBOX-400] *碱性磷酸酶 & $\\downarrow$ & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\\\\n[BBOX-401] *γ-谷氨酰基转移酶 & $\\uparrow$ & 130.5 & 7---45 U/L & *甘油三酯 & $\\uparrow$ & 2.88 & $\\leqslant$1.7 mmol/L \\\\\n[BBOX-402] *乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & $\\uparrow$ & 5.81 & 3---5.7 mmol/L \\\\\n[BBOX-403] *总胆红素 & 10.2 & $\\leqslant$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\\\\n[BBOX-404] *直接胆红素 & 3.3 & $\\leqslant$4 umol/L & *L-脂蛋白胆固醇 & $\\uparrow$ & 3.66 & 健康人<3.4; 不同ASCVD危 \\\\\n[BBOX-405] *胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\\\\n[BBOX-406] *总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\\\\n[BBOX-407] *白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\\\\n[BBOX-408] *球蛋白 & 30.1 & 20---40 g/L & & & & \\\\\n[BBOX-409] 白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\\\\n[BBOX-410] *总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & $\\uparrow$ & 1.15 & 0.6---1.1 g/L \\\\\n[BBOX-411] 亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\\\\n[BBOX-412] *腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\\\\n[BBOX-413] *葡萄糖 & $\\uparrow$ & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\\\\n[BBOX-414] *尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\\\\n[BBOX-415] & & & & *氯 & 101.7 & 99---110 mmol/L \\\\\n[BBOX-416] \\hline\n[BBOX-417] \\multicolumn{8}{l}{检验意见:} \\\\\n[BBOX-418] \\hline\n[BBOX-419] \\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{2}{l}{检验者: 柏玉} & \\multicolumn{2}{l}{审核者: 余安光} \\\\\n[BBOX-420] \\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\\\\n[BBOX-421] \\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\\\\n[BBOX-422] \\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\\\\n[BBOX-423] \\multicolumn{8}{l}{注: $\\uparrow$-偏高, $\\downarrow$-偏低, ★-危急值结果} \\\\\n[BBOX-424] \\hline\n[BBOX-425] \\end{tabular}\n[BBOX-426] \\begin{tabular}{llllllll}\n[BBOX-427] 报告时间: 2026-03-10\n[BBOX-428] \\hline\n[BBOX-429] \\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n[BBOX-430] \\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n[BBOX-431] \\multicolumn{8}{c}{苏HR} \\\\\n[BBOX-432] \\hline\n[BBOX-433] \\textbf{姓名:} & \\textbf{名:} & \\textbf{病历号:} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\textbf{样本号} & \\multicolumn{2}{l}{} \\\\\n[BBOX-434] \\textbf{性别:} & \\textbf{女:} & \\textbf{科室:} & \\multicolumn{2}{l}{(江北)综合肿瘤中} & \\textbf{条码号} & \\multicolumn{2}{l}{} \\\\\n[BBOX-435] \\textbf{年龄:} & \\textbf{75岁} & \\textbf{床号:} & \\multicolumn{2}{l}{标本种类: 血液} & \\textbf{标本说明:} & \\multicolumn{2}{l}{} \\\\\n[BBOX-436] \\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n[BBOX-437] \\hline\n[BBOX-438] \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} \\\\\n[BBOX-439] \\hline\n[BBOX-440] *C反应蛋白 & $\\uparrow$ & 11.2 & 0---6 mg/L & & & & & & & & \\\\\n[BBOX-441] *肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\\\\n[BBOX-442] 肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\\\\n[BBOX-443] *a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\\\\n[BBOX-444] eGFR (CKD-EPI) & $\\downarrow$ & 69.6 & $>$90 ml/min/1.73m$^2$ & & & & & & & & \\\\\n[BBOX-445] \\hline\n[BBOX-446] \\multicolumn{8}{l}{检验意见:} \\\\\n[BBOX-447] \\hline\n[BBOX-448] \\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{2}{l}{检验者: 柏玉} & \\multicolumn{2}{l}{审核者: 余安光} \\\\\n[BBOX-449] \\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\\\\n[BBOX-450] \\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\\\\n[BBOX-451] \\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\\\\n[BBOX-452] \\multicolumn{8}{l}{注: $\\uparrow$-偏高, $\\downarrow$-偏低, ★-危急值结果} \\\\\n[BBOX-453] \\hline\n[BBOX-454] \\end{tabular}"
  }
]
2026-08-10 16:15:52,357 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:15:52.354+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:15:52,796 INFO     29 [LLM] SmartSplitter response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:15:52,817 INFO     29 [SmartSplitter] SmartSplitter done: 9 chunks from 9 LLM segments (all bbox_id). Types: {'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 3}
2026-08-10 16:15:52,827 INFO     29 [Pipeline] Component [2]: SmartSplitter:MedLink finished. error=None
2026-08-10 16:15:52,827 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | SmartSplitter:MedLink | outputs={"html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 3}"}
2026-08-10 16:15:52,827 INFO     29 [Pipeline] Executing component [3]: ChunkRouter:Router (type=ChunkRouter)
2026-08-10 16:15:52,828 INFO     29 [ChunkRouter] Routed 9 chunks into 4 groups: {'chunks_Discharge': 1, 'chunks_Examination': 4, 'chunks_Clinical': 1, 'chunks_LabExam': 3}
2026-08-10 16:15:52,841 INFO     29 [Pipeline] Component [3]: ChunkRouter:Router finished. error=None
2026-08-10 16:15:52,841 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | ChunkRouter:Router | outputs={"html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks": "9 items, types={'DischargeRecord': 1, 'ExaminationReport': 4, 'OutpatientRecord': 1, 'LabReport': 3}", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:15:52,841 INFO     29 [Pipeline] Executing component [4]: Extractor:LabExam (type=Extractor)
2026-08-10 16:15:52,846 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:15:52,847 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:15:52,847 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[12]
2026-08-10 16:15:52,847 INFO     29 [qwen-vl-table] positions ： [[12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0], [12, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:15:53,011 INFO     29 [qwen-vl-table] page=12, rect=842x595, img=(2339x1654)
2026-08-10 16:15:53,012 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:15:53,013 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 362, \"bbox_end\": 383, \"encounter_dates\": [\"2026-03-10\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{cccccc}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{2}{c}{\\textbf{检验项目}} & \\textbf{结果} & \\textbf{参考区间-单位} & \\multicolumn{2}{c}{\\textbf{检验项目}} \\\\\n\\hline\n*白细胞计数 & & 4.2 & 3.5--9.5 10^9/L & *平均红细胞血红蛋白含量 & 31.4 \\\\\n中性粒细胞百分数 & & 74.5 & 40--75 \\% & *平均红细胞血红蛋白浓度 & 332 \\\\\n淋巴细胞百分数 & ↓ & 16.1 & 20--50 \\% & 红细胞体积分布宽度 & 13.6 \\\\\n单核细胞百分数 & & 6.9 & 3--10 \\% & *血小板计数 & 179 \\\\\n嗜酸性粒细胞百分数 & & 1.7 & 0.4--8 \\% & & \\\\\n嗜碱性粒细胞百分数 & & 0.8 & 0--1 \\% & & \\\\\n中性粒细胞绝对值 & & 3.1 & 1.8--6.3 10^9/L & & \\\\\n淋巴细胞绝对值 & ↓ & 0.7 & 1.1--3.2 10^9/L & & \\\\\n单核细胞绝对值 & & 0.3 & 0.1--0.6 10^9/L & & \\\\\n嗜酸性粒细胞绝对值 & & 0.07 & 0.02--0.52 10^9/L & & \\\\\n嗜碱性粒细胞绝对值 & & 0.03 & 0--0.06 10^9/L & & \\\\\n*红细胞计数 & & 4.01 & 3.8--5.1 10^12/L & & \\\\\n*血红蛋白量 & & 126 & 115--150 g/L & & \\\\\n*红细胞压积 & & 38.0 & 35--45 \\% & & \\\\\n*平均红细胞体积 & & 94.7 & 82--100 fl & & \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:16:04,849 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:04,849 INFO     29 [qwen-vl-table] page=12 LLM output (len=3248):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "白细胞计数",
      "item_code": "WBC",
      "value": "4.2",
      "unit": "10^9/L",
      "reference_range": "3.5--9.5",
      "abnormal": false
    },
    {
      "name": "中性粒细胞百分数",
      "item_code": "NEUT%",
      "value": "74.5",
      "unit": "%",
      "reference_range": "40--75",
      "abnormal": false
    },
    {
      "name": "淋巴细胞百分数",
      "item_code": "LYMPH%",
      "value": "16.1",
      "unit": "%",
      "reference_range": "20--50",
      "abnormal": true
    },
    {
      "name": "单核细胞百分数",
      "item_code": "MONO%",
      "value": "6.9",
      "unit": "%",
      "reference_range": "3--10",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞百分数",
      "item_code": "EO%",
      "value": "1.7",
      "unit": "%",
      "reference_range": "0.4--8",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞百分数",
      "item_code": "BASO%",
      "value": "0.8",
      "unit": "%",
      "reference_range": "0--1",
      "abnormal": false
    },
    {
      "name": "中性粒细胞绝对值",
      "item_code": "NEUT#",
      "value": "3.1",
      "unit": "10^9/L",
      "reference_range": "1.8--6.3",
      "abnormal": false
    },
    {
      "name": "淋巴细胞绝对值",
      "item_code": "LYMPH#",
      "value": "0.7",
      "unit": "10^9/L",
      "reference_range": "1.1--3.2",
      "abnormal": true
    },
    {
      "name": "单核细胞绝对值",
      "item_code": "MONO#",
      "value": "0.3",
      "unit": "10^9/L",
      "reference_range": "0.1--0.6",
      "abnormal": false
    },
    {
      "name": "嗜酸性粒细胞绝对值",
      "item_code": "EO#",
      "value": "0.07",
      "unit": "10^9/L",
      "reference_range": "0.02--0.52",
      "abnormal": false
    },
    {
      "name": "嗜碱性粒细胞绝对值",
      "item_code": "BASO#",
      "value": "0.03",
      "unit": "10^9/L",
      "reference_range": "0--0.06",
      "abnormal": false
    },
    {
      "name": "红细胞计数",
      "item_code": "RBC",
      "value": "4.01",
      "unit": "10^12/L",
      "reference_range": "3.8--5.1",
      "abnormal": false
    },
    {
      "name": "血红蛋白量",
      "item_code": "HGB",
      "value": "126",
      "unit": "g/L",
      "reference_range": "115--150",
      "abnormal": false
    },
    {
      "name": "红细胞压积",
      "item_code": "HCT",
      "value": "38.0",
      "unit": "%",
      "reference_range": "35--45",
      "abnormal": false
    },
    {
      "name": "平均红细胞体积",
      "item_code": "MCV",
      "value": "94.7",
      "unit": "fl",
      "reference_range": "82--100",
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白含量",
      "item_code": "MCH",
      "value": "31.4",
      "unit": "pg",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "平均红细胞血红蛋白浓度",
      "item_code": "MCHC",
      "value": "332",
      "unit": "g/L",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "红细胞体积分布宽度",
      "item_code": "RDW",
      "value": "13.6",
      "unit": "%",
      "reference_range": null,
      "abnormal": false
    },
    {
      "name": "血小板计数",
      "item_code": "PLT",
      "value": "179",
      "unit": "10^9/L",
      "reference_range": null,
      "abnormal": false
    }
  ]
}
2026-08-10 16:16:04,850 INFO     29 [qwen-vl-table] coord grouping: {12: 19}
2026-08-10 16:16:04,852 INFO     29 [qwen-vl-table] coord API call start, page=12, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1145232, prompt_len=668
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
白细胞计数、中性粒细胞百分数、淋巴细胞百分数、单核细胞百分数、嗜酸性粒细胞百分数、嗜碱性粒细胞百分数、中性粒细胞绝对值、淋巴细胞绝对值、单核细胞绝对值、嗜酸性粒细胞绝对值、嗜碱性粒细胞绝对值、红细胞计数、血红蛋白量、红细胞压积、平均红细胞体积、平均红细胞血红蛋白含量、平均红细胞血红蛋白浓度、红细胞体积分布宽度、血小板计数

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
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord API raw response (len=1000):
[
	{"text": "白细胞计数", "bbox": [146, 331, 212, 348]},
	{"text": "中性粒细胞百分数", "bbox": [146, 354, 241, 371]},
	{"text": "淋巴细胞百分数", "bbox": [146, 377, 229, 394]},
	{"text": "单核细胞百分数", "bbox": [146, 400, 229, 417]},
	{"text": "嗜酸性粒细胞百分数", "bbox": [146, 423, 252, 440]},
	{"text": "嗜碱性粒细胞百分数", "bbox": [146, 446, 252, 463]},
	{"text": "中性粒细胞绝对值", "bbox": [146, 469, 241, 486]},
	{"text": "淋巴细胞绝对值", "bbox": [146, 492, 229, 509]},
	{"text": "单核细胞绝对值", "bbox": [146, 515, 229, 532]},
	{"text": "嗜酸性粒细胞绝对值", "bbox": [146, 538, 252, 555]},
	{"text": "嗜碱性粒细胞绝对值", "bbox": [146, 561, 252, 578]},
	{"text": "红细胞计数", "bbox": [146, 584, 212, 601]},
	{"text": "血红蛋白量", "bbox": [146, 607, 212, 624]},
	{"text": "红细胞压积", "bbox": [146, 630, 212, 647]},
	{"text": "平均红细胞体积", "bbox": [146, 653, 235, 670]},
	{"text": "平均红细胞血红蛋白含量", "bbox": [518, 331, 655, 348]},
	{"text": "平均红细胞血红蛋白浓度", "bbox": [518, 354, 655, 371]},
	{"text": "红细胞体积分布宽度", "bbox": [518, 377, 625, 394]},
	{"text": "血小板计数", "bbox": [518, 400, 585, 417]}
]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord API: raw_items=19, valid_items=19, elapsed=5.9s
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[0]: text=白细胞计数, bbox=[146, 331, 212, 348]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[1]: text=中性粒细胞百分数, bbox=[146, 354, 241, 371]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[2]: text=淋巴细胞百分数, bbox=[146, 377, 229, 394]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[3]: text=单核细胞百分数, bbox=[146, 400, 229, 417]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[4]: text=嗜酸性粒细胞百分数, bbox=[146, 423, 252, 440]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[5]: text=嗜碱性粒细胞百分数, bbox=[146, 446, 252, 463]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[6]: text=中性粒细胞绝对值, bbox=[146, 469, 241, 486]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[7]: text=淋巴细胞绝对值, bbox=[146, 492, 229, 509]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[8]: text=单核细胞绝对值, bbox=[146, 515, 229, 532]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[9]: text=嗜酸性粒细胞绝对值, bbox=[146, 538, 252, 555]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[10]: text=嗜碱性粒细胞绝对值, bbox=[146, 561, 252, 578]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[11]: text=红细胞计数, bbox=[146, 584, 212, 601]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[12]: text=血红蛋白量, bbox=[146, 607, 212, 624]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[13]: text=红细胞压积, bbox=[146, 630, 212, 647]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[14]: text=平均红细胞体积, bbox=[146, 653, 235, 670]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[15]: text=平均红细胞血红蛋白含量, bbox=[518, 331, 655, 348]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[16]: text=平均红细胞血红蛋白浓度, bbox=[518, 354, 655, 371]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[17]: text=红细胞体积分布宽度, bbox=[518, 377, 625, 394]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] coord item[18]: text=血小板计数, bbox=[518, 400, 585, 417]
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] page=12 coord: matched 19/19, time=5.9s
2026-08-10 16:16:10,756 INFO     29 [qwen-vl-table] new_positions (19):
[[13, 122.91594213867188, 178.48068310546876, 197.0363563232422, 207.15604833984375], [13, 122.91594213867188, 202.89549353027343, 210.72770434570313, 220.8473963623047], [13, 122.91594213867188, 192.79281335449218, 224.41905236816407, 234.53874438476564], [13, 122.91594213867188, 192.79281335449218, 238.11040039062502, 248.23009240722658], [13, 122.91594213867188, 212.15628369140626, 251.80174841308596, 261.9214404296875], [13, 122.91594213867188, 212.15628369140626, 265.4930964355469, 275.61278845214844], [13, 122.91594213867188, 202.89549353027343, 279.1844444580078, 289.3041364746094], [13, 122.91594213867188, 192.79281335449218, 292.87579248046876, 302.9954844970703], [13, 122.91594213867188, 192.79281335449218, 306.5671405029297, 316.68683251953127], [13, 122.91594213867188, 212.15628369140626, 320.25848852539065, 330.3781805419922], [13, 122.91594213867188, 212.15628369140626, 333.9498365478516, 344.06952856445315], [13, 122.91594213867188, 178.48068310546876, 347.64118457031253, 357.7608765869141], [13, 122.91594213867188, 178.48068310546876, 361.3325325927735, 371.45222460937504], [13, 122.91594213867188, 178.48068310546876, 375.0238806152344, 385.143572631836], [13, 122.91594213867188, 197.8441534423828, 388.7152286376953, 398.83492065429687], [13, 436.09902758789065, 551.4379595947265, 197.0363563232422, 207.15604833984375], [13, 436.09902758789065, 551.4379595947265, 210.72770434570313, 220.8473963623047], [13, 436.09902758789065, 526.1812591552734, 224.41905236816407, 234.53874438476564], [13, 436.09902758789065, 492.50565856933594, 238.11040039062502, 248.23009240722658]]
2026-08-10 16:16:10,757 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=19, matched=19, pages=1, time=17.9s
2026-08-10 16:16:10,757 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:16:10,758 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:16:10,758 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 16:16:10,758 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:16:10,886 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1654)
2026-08-10 16:16:10,887 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:10,887 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 384, \"bbox_end\": 425, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"(江北)综合肿瘤中\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n\\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n\\multicolumn{8}{c}{苏HR} \\\\\n\\hline\n\\textbf{姓名:} & \\textbf{名:} & \\textbf{病历号:} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\textbf{样本号::} & \\multicolumn{2}{l}{} \\\\\n\\textbf{性别:} & \\textbf{女:} & \\textbf{科室:} & \\multicolumn{2}{l}{(江北)综合肿瘤中} & \\textbf{条码号::} & \\multicolumn{2}{l}{} \\\\\n\\textbf{年龄:} & \\textbf{75岁} & \\textbf{床号:} & \\multicolumn{2}{l}{标本种类: 血液} & \\textbf{标本说明:} & \\multicolumn{2}{l}{} \\\\\n\\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n\\hline\n\\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} \\\\\n\\hline\n*丙氨酸氨基转移酶 & $\\uparrow$ & 50.3 & 7---40 U/L & *肌酐 & 73 & 41---81 umol/L \\\\\n*天门冬氨酸氨基转移酶 & $\\uparrow$ & 35.4 & 13---35 U/L & *尿酸 & 221 & 155---357 umol/L \\\\\n*碱性磷酸酶 & $\\downarrow$ & 43.2 & 50---135 U/L & 总二氧化碳 & 28.1 & 21---31 mmol/L \\\\\n*γ-谷氨酰基转移酶 & $\\uparrow$ & 130.5 & 7---45 U/L & *甘油三酯 & $\\uparrow$ & 2.88 & $\\leqslant$1.7 mmol/L \\\\\n*乳酸脱氢酶 & 193 & 120---250 U/L & *总胆固醇 & $\\uparrow$ & 5.81 & 3---5.7 mmol/L \\\\\n*总胆红素 & 10.2 & $\\leqslant$21 umol/L & *H-脂蛋白胆固醇 & 1.26 & 1.03---1.55 mmol/L \\\\\n*直接胆红素 & 3.3 & $\\leqslant$4 umol/L & *L-脂蛋白胆固醇 & $\\uparrow$ & 3.66 & 健康人<3.4; 不同ASCVD危 \\\\\n*胆碱酯酶 & 8.8 & 5.3---11.3 KU/L & & & & 险人群目标值: 低危<3.4 \\\\\n*总蛋白 & 78.9 & 65---85 g/L & & & & 中高危<2.6; 极高危<1.8 \\\\\n*白蛋白 & 48.8 & 40---55 g/L & & & & 超高危<1.4 mmol/L \\\\\n*球蛋白 & 30.1 & 20---40 g/L & & & & \\\\\n白/球比例 & 1.62 & 1.2---2.4 & *载脂蛋白A I & 1.30 & 1---1.6 g/L \\\\\n*总胆汁酸 & 4.0 & 0---13 umol/L & *载脂蛋白B & $\\uparrow$ & 1.15 & 0.6---1.1 g/L \\\\\n亮氨酸氨肽酶 & 35.3 & 12---37 U/L & *总钙 & 2.46 & 2.11---2.52 mmol/L \\\\\n*腺苷脱氨酶 & 21.3 & 0---25 U/L & *磷 & 1.37 & 0.85---1.51 mmol/L \\\\\n*葡萄糖 & $\\uparrow$ & 8.35 & 3.9---6.1 mmol/L & *钾 & 4.18 & 3.5---5.3 mmol/L \\\\\n*尿素 & 4.4 & 3.1---8.8 mmol/L & *钠 & 138.3 & 137---147 mmol/L \\\\\n& & & & *氯 & 101.7 & 99---110 mmol/L \\\\\n\\hline\n\\multicolumn{8}{l}{检验意见:} \\\\\n\\hline\n\\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{2}{l}{检验者: 柏玉} & \\multicolumn{2}{l}{审核者: 余安光} \\\\\n\\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\\\\n\\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\\\\n\\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\\\\n\\multicolumn{8}{l}{注: $\\uparrow$-偏高, $\\downarrow$-偏低, ★-危急值结果} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:16:24,235 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:16:24.234+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:16:28,145 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:28,145 INFO     29 [qwen-vl-table] page=13 LLM output (len=5248):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "丙氨酸氨基转移酶",
      "item_code": null,
      "value": "50.3",
      "unit": "U/L",
      "reference_range": "7---40",
      "abnormal": true
    },
    {
      "name": "天门冬氨酸氨基转移酶",
      "item_code": null,
      "value": "35.4",
      "unit": "U/L",
      "reference_range": "13---35",
      "abnormal": true
    },
    {
      "name": "碱性磷酸酶",
      "item_code": null,
      "value": "43.2",
      "unit": "U/L",
      "reference_range": "50---135",
      "abnormal": true
    },
    {
      "name": "γ-谷氨酰基转移酶",
      "item_code": null,
      "value": "130.5",
      "unit": "U/L",
      "reference_range": "7---45",
      "abnormal": true
    },
    {
      "name": "乳酸脱氢酶",
      "item_code": null,
      "value": "193",
      "unit": "U/L",
      "reference_range": "120---250",
      "abnormal": false
    },
    {
      "name": "总胆红素",
      "item_code": null,
      "value": "10.2",
      "unit": "umol/L",
      "reference_range": "≤21",
      "abnormal": false
    },
    {
      "name": "直接胆红素",
      "item_code": null,
      "value": "3.3",
      "unit": "umol/L",
      "reference_range": "≤4",
      "abnormal": false
    },
    {
      "name": "胆碱酯酶",
      "item_code": null,
      "value": "8.8",
      "unit": "KU/L",
      "reference_range": "5.3---11.3",
      "abnormal": false
    },
    {
      "name": "总蛋白",
      "item_code": null,
      "value": "78.9",
      "unit": "g/L",
      "reference_range": "65---85",
      "abnormal": false
    },
    {
      "name": "白蛋白",
      "item_code": null,
      "value": "48.8",
      "unit": "g/L",
      "reference_range": "40---55",
      "abnormal": false
    },
    {
      "name": "球蛋白",
      "item_code": null,
      "value": "30.1",
      "unit": "g/L",
      "reference_range": "20---40",
      "abnormal": false
    },
    {
      "name": "白/球比例",
      "item_code": null,
      "value": "1.62",
      "unit": null,
      "reference_range": "1.2---2.4",
      "abnormal": false
    },
    {
      "name": "总胆汁酸",
      "item_code": null,
      "value": "4.0",
      "unit": "umol/L",
      "reference_range": "0---13",
      "abnormal": false
    },
    {
      "name": "亮氨酸氨肽酶",
      "item_code": null,
      "value": "35.3",
      "unit": "U/L",
      "reference_range": "12---37",
      "abnormal": false
    },
    {
      "name": "腺苷脱氨酶",
      "item_code": null,
      "value": "21.3",
      "unit": "U/L",
      "reference_range": "0---25",
      "abnormal": false
    },
    {
      "name": "葡萄糖",
      "item_code": null,
      "value": "8.35",
      "unit": "mmol/L",
      "reference_range": "3.9---6.1",
      "abnormal": true
    },
    {
      "name": "尿素",
      "item_code": null,
      "value": "4.4",
      "unit": "mmol/L",
      "reference_range": "3.1---8.8",
      "abnormal": false
    },
    {
      "name": "肌酐",
      "item_code": null,
      "value": "73",
      "unit": "umol/L",
      "reference_range": "41---81",
      "abnormal": false
    },
    {
      "name": "尿酸",
      "item_code": null,
      "value": "221",
      "unit": "umol/L",
      "reference_range": "155---357",
      "abnormal": false
    },
    {
      "name": "总二氧化碳",
      "item_code": null,
      "value": "28.1",
      "unit": "mmol/L",
      "reference_range": "21---31",
      "abnormal": false
    },
    {
      "name": "甘油三酯",
      "item_code": null,
      "value": "2.88",
      "unit": "mmol/L",
      "reference_range": "≤1.7",
      "abnormal": true
    },
    {
      "name": "总胆固醇",
      "item_code": null,
      "value": "5.81",
      "unit": "mmol/L",
      "reference_range": "3---5.7",
      "abnormal": true
    },
    {
      "name": "H-脂蛋白胆固醇",
      "item_code": null,
      "value": "1.26",
      "unit": "mmol/L",
      "reference_range": "1.03---1.55",
      "abnormal": false
    },
    {
      "name": "L-脂蛋白胆固醇",
      "item_code": null,
      "value": "3.66",
      "unit": "mmol/L",
      "reference_range": "健康人<3.4; 不同ASCVD危险人群目标值: 低危<3.4 中高危<2.6; 极高危<1.8 超高危<1.4",
      "abnormal": true
    },
    {
      "name": "载脂蛋白A I",
      "item_code": null,
      "value": "1.30",
      "unit": "g/L",
      "reference_range": "1---1.6",
      "abnormal": false
    },
    {
      "name": "载脂蛋白B",
      "item_code": null,
      "value": "1.15",
      "unit": "g/L",
      "reference_range": "0.6---1.1",
      "abnormal": true
    },
    {
      "name": "总钙",
      "item_code": null,
      "value": "2.46",
      "unit": "mmol/L",
      "reference_range": "2.11---2.52",
      "abnormal": false
    },
    {
      "name": "磷",
      "item_code": null,
      "value": "1.37",
      "unit": "mmol/L",
      "reference_range": "0.85---1.51",
      "abnormal": false
    },
    {
      "name": "钾",
      "item_code": null,
      "value": "4.18",
      "unit": "mmol/L",
      "reference_range": "3.5---5.3",
      "abnormal": false
    },
    {
      "name": "钠",
      "item_code": null,
      "value": "138.3",
      "unit": "mmol/L",
      "reference_range": "137---147",
      "abnormal": false
    },
    {
      "name": "氯",
      "item_code": null,
      "value": "101.7",
      "unit": "mmol/L",
      "reference_range": "99---110",
      "abnormal": false
    }
  ]
}
2026-08-10 16:16:28,146 INFO     29 [qwen-vl-table] coord grouping: {13: 31}
2026-08-10 16:16:28,147 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822902, prompt_len=672
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
丙氨酸氨基转移酶、天门冬氨酸氨基转移酶、碱性磷酸酶、γ-谷氨酰基转移酶、乳酸脱氢酶、总胆红素、直接胆红素、胆碱酯酶、总蛋白、白蛋白、球蛋白、白/球比例、总胆汁酸、亮氨酸氨肽酶、腺苷脱氨酶、葡萄糖、尿素、肌酐、尿酸、总二氧化碳、甘油三酯、总胆固醇、H-脂蛋白胆固醇、L-脂蛋白胆固醇、载脂蛋白A I、载脂蛋白B、总钙、磷、钾、钠、氯

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
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord API raw response (len=1532):
[
	{"text": "丙氨酸氨基转移酶", "bbox": [305, 187, 360, 197]},
	{"text": "天门冬氨酸氨基转移酶", "bbox": [305, 199, 373, 209]},
	{"text": "碱性磷酸酶", "bbox": [305, 212, 342, 221]},
	{"text": "γ-谷氨酰基转移酶", "bbox": [305, 224, 364, 234]},
	{"text": "乳酸脱氢酶", "bbox": [305, 237, 342, 247]},
	{"text": "总胆红素", "bbox": [305, 249, 337, 259]},
	{"text": "直接胆红素", "bbox": [305, 262, 341, 272]},
	{"text": "胆碱酯酶", "bbox": [305, 275, 336, 285]},
	{"text": "总蛋白", "bbox": [305, 287, 330, 297]},
	{"text": "白蛋白", "bbox": [305, 300, 328, 310]},
	{"text": "球蛋白", "bbox": [305, 313, 327, 323]},
	{"text": "白/球比例", "bbox": [305, 326, 336, 336]},
	{"text": "总胆汁酸", "bbox": [305, 339, 336, 349]},
	{"text": "亮氨酸氨肽酶", "bbox": [305, 352, 344, 362]},
	{"text": "腺苷脱氨酶", "bbox": [305, 365, 342, 375]},
	{"text": "葡萄糖", "bbox": [305, 378, 328, 388]},
	{"text": "尿素", "bbox": [305, 390, 322, 400]},
	{"text": "肌酐", "bbox": [510, 187, 526, 197]},
	{"text": "尿酸", "bbox": [510, 200, 526, 209]},
	{"text": "总二氧化碳", "bbox": [510, 212, 542, 221]},
	{"text": "甘油三酯", "bbox": [510, 224, 538, 234]},
	{"text": "总胆固醇", "bbox": [510, 237, 538, 247]},
	{"text": "H-脂蛋白胆固醇", "bbox": [510, 249, 559, 259]},
	{"text": "L-脂蛋白胆固醇", "bbox": [510, 262, 558, 272]},
	{"text": "载脂蛋白A I", "bbox": [510, 317, 547, 327]},
	{"text": "载脂蛋白B", "bbox": [510, 330, 544, 340]},
	{"text": "总钙", "bbox": [510, 343, 526, 352]},
	{"text": "磷", "bbox": [510, 355, 520, 365]},
	{"text": "钾", "bbox": [510, 368, 520, 378]},
	{"text": "钠", "bbox": [510, 381, 520, 390]},
	{"text": "氯", "bbox": [510, 393, 520, 403]}
]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord API: raw_items=31, valid_items=31, elapsed=10.2s
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[0]: text=丙氨酸氨基转移酶, bbox=[305, 187, 360, 197]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[1]: text=天门冬氨酸氨基转移酶, bbox=[305, 199, 373, 209]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[2]: text=碱性磷酸酶, bbox=[305, 212, 342, 221]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[3]: text=γ-谷氨酰基转移酶, bbox=[305, 224, 364, 234]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[4]: text=乳酸脱氢酶, bbox=[305, 237, 342, 247]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[5]: text=总胆红素, bbox=[305, 249, 337, 259]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[6]: text=直接胆红素, bbox=[305, 262, 341, 272]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[7]: text=胆碱酯酶, bbox=[305, 275, 336, 285]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[8]: text=总蛋白, bbox=[305, 287, 330, 297]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[9]: text=白蛋白, bbox=[305, 300, 328, 310]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[10]: text=球蛋白, bbox=[305, 313, 327, 323]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[11]: text=白/球比例, bbox=[305, 326, 336, 336]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[12]: text=总胆汁酸, bbox=[305, 339, 336, 349]
2026-08-10 16:16:38,335 INFO     29 [qwen-vl-table] coord item[13]: text=亮氨酸氨肽酶, bbox=[305, 352, 344, 362]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[14]: text=腺苷脱氨酶, bbox=[305, 365, 342, 375]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[15]: text=葡萄糖, bbox=[305, 378, 328, 388]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[16]: text=尿素, bbox=[305, 390, 322, 400]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[17]: text=肌酐, bbox=[510, 187, 526, 197]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[18]: text=尿酸, bbox=[510, 200, 526, 209]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[19]: text=总二氧化碳, bbox=[510, 212, 542, 221]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[20]: text=甘油三酯, bbox=[510, 224, 538, 234]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[21]: text=总胆固醇, bbox=[510, 237, 538, 247]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[22]: text=H-脂蛋白胆固醇, bbox=[510, 249, 559, 259]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[23]: text=L-脂蛋白胆固醇, bbox=[510, 262, 558, 272]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[24]: text=载脂蛋白A I, bbox=[510, 317, 547, 327]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[25]: text=载脂蛋白B, bbox=[510, 330, 544, 340]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[26]: text=总钙, bbox=[510, 343, 526, 352]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[27]: text=磷, bbox=[510, 355, 520, 365]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[28]: text=钾, bbox=[510, 368, 520, 378]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[29]: text=钠, bbox=[510, 381, 520, 390]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] coord item[30]: text=氯, bbox=[510, 393, 520, 403]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] page=13 coord: matched 31/31, time=10.2s
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] new_positions (31):
[[14, 256.7764544677734, 303.0804052734375, 111.31661218261719, 117.26937219238282], [14, 256.7764544677734, 314.0249754638672, 118.45992419433594, 124.41268420410157], [14, 256.7764544677734, 287.9263850097656, 126.19851220703126, 131.55599621582033], [14, 256.7764544677734, 306.44796533203123, 133.34182421875, 139.29458422851562], [14, 256.7764544677734, 287.9263850097656, 141.0804122314453, 147.03317224121093], [14, 256.7764544677734, 283.71693493652344, 148.22372424316407, 154.1764842529297], [14, 256.7764544677734, 287.0844949951172, 155.9623122558594, 161.915072265625], [14, 256.7764544677734, 282.875044921875, 163.7009002685547, 169.65366027832033], [14, 256.7764544677734, 277.8237048339844, 170.84421228027344, 176.79697229003907], [14, 256.7764544677734, 276.1399248046875, 178.58280029296876, 184.53556030273438], [14, 256.7764544677734, 275.2980347900391, 186.32138830566407, 192.2741483154297], [14, 256.7764544677734, 282.875044921875, 194.0599763183594, 200.01273632812502], [14, 256.7764544677734, 282.875044921875, 201.7985643310547, 207.75132434082033], [14, 256.7764544677734, 289.6101650390625, 209.53715234375, 215.48991235351562], [14, 256.7764544677734, 287.9263850097656, 217.2757403564453, 223.22850036621094], [14, 256.7764544677734, 276.1399248046875, 225.01432836914063, 230.96708837890625], [14, 256.7764544677734, 271.08858471679684, 232.1576403808594, 238.11040039062502], [14, 429.3639074707031, 442.8341477050781, 111.31661218261719, 117.26937219238282], [14, 429.3639074707031, 442.8341477050781, 119.05520019531251, 124.41268420410157], [14, 429.3639074707031, 456.30438793945314, 126.19851220703126, 131.55599621582033], [14, 429.3639074707031, 452.93682788085937, 133.34182421875, 139.29458422851562], [14, 429.3639074707031, 452.93682788085937, 141.0804122314453, 147.03317224121093], [14, 429.3639074707031, 470.61651818847656, 148.22372424316407, 154.1764842529297], [14, 429.3639074707031, 469.7746281738281, 155.9623122558594, 161.915072265625], [14, 429.3639074707031, 460.5138380126953, 188.70249230957032, 194.65525231933594], [14, 429.3639074707031, 457.98816796875, 196.44108032226563, 202.39384033203126], [14, 429.3639074707031, 442.8341477050781, 204.17966833496095, 209.53715234375], [14, 429.3639074707031, 437.7828076171875, 211.32298034667969, 217.2757403564453], [14, 429.3639074707031, 437.7828076171875, 219.061568359375, 225.01432836914063], [14, 429.3639074707031, 437.7828076171875, 226.80015637207032, 232.1576403808594], [14, 429.3639074707031, 437.7828076171875, 233.94346838378908, 239.8962283935547]]
2026-08-10 16:16:38,336 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=31, matched=31, pages=1, time=27.6s
2026-08-10 16:16:38,337 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:16:38,338 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:16:38,338 INFO     29 [qwen-vl-table] ═══ START ═══ doc_id=None, pages=[13]
2026-08-10 16:16:38,338 INFO     29 [qwen-vl-table] positions ： [[13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0], [13, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:16:38,467 INFO     29 [qwen-vl-table] page=13, rect=842x595, img=(2339x1654)
2026-08-10 16:16:38,467 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:38,467 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检验检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"LabReport\", \"bbox_start\": 426, \"bbox_end\": 454, \"encounter_dates\": [\"2026-03-10\"], \"department\": \"(江北)综合肿瘤中\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（LabReport / ExamReport / ImagingReport 通用）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检验/检查项目名称>\",\n      \"item_code\": \"<string|null, 英文缩写/代码，如 WBC、RBC、HGB、PLT、ESR 等>\",\n      \"value\": \"<string, 结果数值，原样保留>\",\n      \"unit\": \"<string|null, 单位>\",\n      \"reference_range\": \"<string|null, 参考范围>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留（如\"44.00\"不要改为\"44\"）\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正\n5. 每个检验项目都必须逐条提取到 items 数组中，不得遗漏\n6. item_code 提取规则：\n   - 如果报告有中文名和英文缩写两列，name 填中文全名，item_code 填英文缩写\n   - 如果只有中文名，name 填中文名，item_code 填 null\n   - 如果只有英文缩写，name 填英文缩写，item_code 填 null（不要翻译）\n   - 如果原文中有英文缩写（如表格列\"英文名称\"或项目旁的括号注释），提取为 item_code；若原文无英文缩写则填 null\n   示例（双列报告）：\n   原文：| ALT | 丙氨酸氨基转移酶 | 16.9 | U/L | 7.0-40.0 |\n   输出：{\"name\": \"丙氨酸氨基转移酶\", \"item_code\": \"ALT\", \"value\": \"16.9\", \"unit\": \"U/L\", \"reference_range\": \"7.0-40.0\", \"abnormal\": false}\n\n## 边界场景：单位推断规则\n部分检验报告表格没有独立的\"单位\"列（例如血常规报告仅有\"项目名称|英文名称|结果|提示|参考范围\"五列）。\n此时按以下规则处理：\n- 如果参考范围中包含单位信息（如\"4.00-10.00×10^9/L\"），从参考范围中提取单位（此例为\"×10^9/L\"）\n- 如果参考范围无单位且原文无任何单位信息，填 null\n- 举例：\n  - 白细胞(WBC)，结果=6.70，参考范围=4.00-10.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞(RBC)，结果=4.58，参考范围=3.50-5.50×10^12/L → unit=\"×10^12/L\"\n  - 血红蛋白(HGB)，结果=114.00，参考范围=110.00-160.00g/L → unit=\"g/L\"\n  - 血小板(PLT)，结果=197.00，参考范围=100.00-300.00×10^9/L → unit=\"×10^9/L\"\n  - 红细胞沉降率(ESR)，结果=14，参考范围=0-20mm/h → unit=\"mm/h\""
  },
  {
    "content": "\\begin{tabular}{llllllll}\n报告时间: 2026-03-10\n\\hline\n\\multicolumn{8}{c}{\\textbf{南京鼓楼医院 检验科报告单}} \\\\\n\\multicolumn{8}{c}{南京大学医学院附属鼓楼医院} \\\\\n\\multicolumn{8}{c}{苏HR} \\\\\n\\hline\n\\textbf{姓名:} & \\textbf{名:} & \\textbf{病历号:} & \\multicolumn{2}{l}{临床诊断: 肺恶性肿瘤} & \\textbf{样本号} & \\multicolumn{2}{l}{} \\\\\n\\textbf{性别:} & \\textbf{女:} & \\textbf{科室:} & \\multicolumn{2}{l}{(江北)综合肿瘤中} & \\textbf{条码号} & \\multicolumn{2}{l}{} \\\\\n\\textbf{年龄:} & \\textbf{75岁} & \\textbf{床号:} & \\multicolumn{2}{l}{标本种类: 血液} & \\textbf{标本说明:} & \\multicolumn{2}{l}{} \\\\\n\\multicolumn{8}{l}{申请医嘱: 生化全套, 心肌酶测定} \\\\\n\\hline\n\\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} & \\multicolumn{2}{c}{\\textbf{检验项目}} & \\multicolumn{2}{c}{\\textbf{结果}} & \\multicolumn{2}{c}{\\textbf{参考区间-单位}} \\\\\n\\hline\n*C反应蛋白 & $\\uparrow$ & 11.2 & 0---6 mg/L & & & & & & & & \\\\\n*肌酸激酶 & 56 & 40---200 U/L & & & & & & & & & \\\\\n肌酸激酶MB同工酶 & 11 & 0---25 U/L & & & & & & & & & \\\\\n*a 羟丁酸脱氢酶 & 120 & 59---126.4 U/L & & & & & & & & & \\\\\neGFR (CKD-EPI) & $\\downarrow$ & 69.6 & $>$90 ml/min/1.73m$^2$ & & & & & & & & \\\\\n\\hline\n\\multicolumn{8}{l}{检验意见:} \\\\\n\\hline\n\\multicolumn{4}{l}{送检医生: 杨阳} & \\multicolumn{2}{l}{检验者: 柏玉} & \\multicolumn{2}{l}{审核者: 余安光} \\\\\n\\multicolumn{4}{l}{采集时间: 2026-03-10 09:20} & \\multicolumn{2}{l}{接收时间: 2026-03-10 09:38} & \\multicolumn{2}{l}{报告时间: 2026-03-10 12:08} \\\\\n\\multicolumn{8}{l}{本报告单结果仅对送检标本负责！如有疑问请于报告时间3日内与检验科210231联系！} \\\\\n\\multicolumn{8}{l}{项目名称前注“*”为省内互认项目} \\\\\n\\multicolumn{8}{l}{注: $\\uparrow$-偏高, $\\downarrow$-偏低, ★-危急值结果} \\\\\n\\hline\n\\end{tabular}",
    "role": "user"
  }
]
2026-08-10 16:16:42,581 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:42,581 INFO     29 [qwen-vl-table] page=13 LLM output (len=894):
{
  "report_date": "2026-03-10",
  "items": [
    {
      "name": "C反应蛋白",
      "item_code": null,
      "value": "11.2",
      "unit": "mg/L",
      "reference_range": "0---6",
      "abnormal": true
    },
    {
      "name": "肌酸激酶",
      "item_code": null,
      "value": "56",
      "unit": "U/L",
      "reference_range": "40---200",
      "abnormal": false
    },
    {
      "name": "肌酸激酶MB同工酶",
      "item_code": null,
      "value": "11",
      "unit": "U/L",
      "reference_range": "0---25",
      "abnormal": false
    },
    {
      "name": "a 羟丁酸脱氢酶",
      "item_code": null,
      "value": "120",
      "unit": "U/L",
      "reference_range": "59---126.4",
      "abnormal": false
    },
    {
      "name": "eGFR (CKD-EPI)",
      "item_code": "eGFR",
      "value": "69.6",
      "unit": "ml/min/1.73m^2",
      "reference_range": ">90",
      "abnormal": true
    }
  ]
}
2026-08-10 16:16:42,581 INFO     29 [qwen-vl-table] coord grouping: {13: 5}
2026-08-10 16:16:42,584 INFO     29 [qwen-vl-table] coord API call start, page=13, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=822902, prompt_len=551
[qwen-vl-table] coord prompt:
你是一个专业的医疗文档OCR识别引擎。
以下是一份检验报告中的已知检验项目名称列表，请在图片中找到每个名称的位置，返回其bbox坐标。

## 需要定位的检验项目名称
C反应蛋白、肌酸激酶、肌酸激酶MB同工酶、a 羟丁酸脱氢酶、eGFR (CKD-EPI)

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
2026-08-10 16:16:44,258 INFO     29 [qwen-vl-table] coord API raw response (len=279):
```json
[
	{"text": "C反应蛋白", "bbox": [305, 612, 337, 622]},
	{"text": "肌酸激酶", "bbox": [305, 627, 335, 637]},
	{"text": "肌酸激酶MB同工酶", "bbox": [305, 640, 357, 650]},
	{"text": "a 羟丁酸脱氢酶", "bbox": [305, 654, 354, 664]},
	{"text": "eGFR (CKD-EPI)", "bbox": [305, 667, 347, 677]}
]
```
2026-08-10 16:16:44,258 INFO     29 [qwen-vl-table] coord API: raw_items=5, valid_items=5, elapsed=1.7s
2026-08-10 16:16:44,258 INFO     29 [qwen-vl-table] coord item[0]: text=C反应蛋白, bbox=[305, 612, 337, 622]
2026-08-10 16:16:44,258 INFO     29 [qwen-vl-table] coord item[1]: text=肌酸激酶, bbox=[305, 627, 335, 637]
2026-08-10 16:16:44,259 INFO     29 [qwen-vl-table] coord item[2]: text=肌酸激酶MB同工酶, bbox=[305, 640, 357, 650]
2026-08-10 16:16:44,259 INFO     29 [qwen-vl-table] coord item[3]: text=a 羟丁酸脱氢酶, bbox=[305, 654, 354, 664]
2026-08-10 16:16:44,259 INFO     29 [qwen-vl-table] coord item[4]: text=eGFR (CKD-EPI), bbox=[305, 667, 347, 677]
2026-08-10 16:16:44,259 INFO     29 [qwen-vl-table] page=13 coord: matched 5/5, time=1.7s
2026-08-10 16:16:44,259 INFO     29 [qwen-vl-table] new_positions (5):
[[14, 256.7764544677734, 283.71693493652344, 364.3089125976563, 370.2616726074219], [14, 256.7764544677734, 282.03315490722656, 373.2380526123047, 379.1908126220703], [14, 256.7764544677734, 300.55473522949217, 380.976640625, 386.9294006347656], [14, 256.7764544677734, 298.02906518554687, 389.3105046386719, 395.26326464843754], [14, 256.7764544677734, 292.1358350830078, 397.04909265136723, 403.00185266113283]]
2026-08-10 16:16:44,260 INFO     29 [qwen-vl-table] ═══ DONE ═══ items=5, matched=5, pages=1, time=5.9s
2026-08-10 16:16:44,280 INFO     29 [Pipeline] Component [4]: Extractor:LabExam finished. error=None
2026-08-10 16:16:44,280 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:LabExam | outputs={"chunks": "3 items, types={'LabReport': 3}", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:16:44,280 INFO     29 [Pipeline] Executing component [5]: Extractor:Imaging (type=Extractor)
2026-08-10 16:16:44,288 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:44,288 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗影像报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ImagingReport）\n\n{\n  \"report_date\": \"<string|null, 报告日期 YYYY-MM-DD>\",\n  \"items\": [\n    {\n      \"name\": \"<string, 检查项目名称>\",\n      \"value\": \"<string, 检查所见/结果描述，原样保留>\",\n      \"unit\": \"<string|null, 单位，影像通常为null>\",\n      \"reference_range\": \"<string|null, 参考范围，影像通常为null>\",\n      \"abnormal\": \"<boolean, 是否异常>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 影像报告的 value 字段应保留完整的检查所见描述\n4. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:16:45,420 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:45,432 INFO     29 [Pipeline] Component [5]: Extractor:Imaging finished. error=None
2026-08-10 16:16:45,432 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Imaging | outputs={"chunks": "1 items", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:16:45,432 INFO     29 [Pipeline] Executing component [6]: Extractor:Clinical (type=Extractor)
2026-08-10 16:16:45,444 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:16:45,445 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:16:45,446 INFO     29 [qwen-vl-text] ═══ START ═══ type=OutpatientRecord, doc_id=None
2026-08-10 16:16:45,446 INFO     29 [qwen-vl-text] positions(29): [[11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0], [11, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:16:45,446 INFO     29 [qwen-vl-text] page grouping: [11], lines per page: [29]
2026-08-10 16:16:45,587 INFO     29 [qwen-vl-text] page=11, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:16:45,588 INFO     29 [qwen-vl-text] LLM extraction start, text_len=229
2026-08-10 16:16:45,588 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:45,588 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病历结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"OutpatientRecord\", \"bbox_start\": 333, \"bbox_end\": 361, \"encounter_dates\": [\"2026-03-16\"], \"department\": \"(江北)心血管内科门诊\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**多记录规则：**\n- 如果原文只包含 1 条记录：输出单个 JSON 对象\n- 如果原文包含多条独立记录（由不同的就诊时间标识）：输出 JSON 数组，每个元素为一条记录的完整提取结果\n\n## 提取 Schema（OutpatientRecord 门诊病历）\n\n{\n  \"encounter_date\": \"<string|null, 该条记录的就诊日期 YYYY-MM-DD, 多记录时必填>\",\n  \"chief_complaint\": \"<string|null, 主诉>\",\n  \"present_illness\": \"<string|null, 现病史，保留完整用药史、剂量、频次>\",\n  \"past_history\": \"<string|null, 既往史>\",\n  \"diagnosis\": \"<string|null, 诊断，保留中西医双诊断>\",\n  \"treatment_plan\": \"<string|object|array|null, 治疗方案，保留药品名+剂量+频次+给药途径>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 数值必须原样保留\n4. OCR 纠错规则（重要）：\n   - 医学术语中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"类风显性关节炎\" → ✓ \"类风湿性关节炎\"（\"湿\"=氵+显，OCR 常丢失三点水偏旁）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"（药名标准写法）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文（如票据编号、正文日期）推断正确日期。\n     若无法推断，保留原值并在该记录中添加 \"date_uncertain\": true\n     ✗ \"2023-10-00\" → 可能是 \"2023-10-02\"（OCR 将\"2\"误识别为\"0\"）\n     ✗ \"2023-00-15\" → 可能是 \"2023-09-13\"（OCR 将\"09\"误识别为\"00\"）\n   - 纠正原则：仅纠正高置信度的标准医学术语和明显无效格式，不得对非标准文本臆测\n5. 如果原文包含多次就诊记录，必须逐条提取每次就诊的完整信息，不得遗漏\n6. 诊断列表必须按原文顺序逐条完整提取，不得遗漏、不得合并\n\n## 示例：多次门诊记录\n\n上游分类：{\"type\": \"OutpatientRecord\", \"record_count\": 2, \"encounter_dates\": [\"2023-09-12\", \"2023-09-26\"], \"department\": \"内科门诊\"}\n\n输出：\n[\n  {\n    \"encounter_date\": \"2023-09-12\",\n    \"chief_complaint\": \"膝关节，腕关节疼痛2周余\",\n    \"present_illness\": \"患者自述3年前无明显诱因下出现多关节肿痛，于外院就诊后确诊为类风湿性关节炎\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  },\n  {\n    \"encounter_date\": \"2023-09-26\",\n    \"chief_complaint\": \"类风湿性关节炎复查\",\n    \"present_illness\": \"患者二周前于我院接受阿达木单抗注射液治疗，今来我院就诊复查\",\n    \"past_history\": \"无传染病，无药物过敏史\",\n    \"diagnosis\": \"西医：类风湿性关节炎 中医：痹症\",\n    \"treatment_plan\": \"阿达木单抗注射液（泰博维-40mg*0.8ml）0.8ml SC 每二周一次 1盒\"\n  }\n]"
  },
  {
    "content": "南京鼓楼医院\n南京大学医学院附属鼓楼医院\n互联网医院\n门诊病历\n姓名:\n性别:女\n年龄:75岁\nID:\n预约挂号\n2026年03月16日15时20分 (江北)心血管内科门诊\n主诉:要求进行心功能分级\n病史:患者平时正常活动不受限。\n过敏史:无吸烟史\n药物过敏史。无流行病学史\n体查:\n级)\n诊断:\n1.心功能I级(NYHA分\n2.高脂血症\n处理:随诊\n1.非诺贝特胶囊(力平之)\n200mg/粒\n用法:1粒\n口服\n一次/日\nx3盒 28天\n医师:\n齐\n第1页",
    "role": "user"
  }
]
2026-08-10 16:16:47,333 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:47,333 INFO     29 [qwen-vl-text] LLM output (len=262):
{
  "encounter_date": "2026-03-16",
  "chief_complaint": "要求进行心功能分级",
  "present_illness": "患者平时正常活动不受限。",
  "past_history": "无吸烟史。无药物过敏史。无流行病学史",
  "diagnosis": "1.心功能I级(NYHA分级)\n2.高脂血症",
  "treatment_plan": "1.非诺贝特胶囊(力平之) 200mg/粒 用法:1粒 口服 一次/日 x3盒 28天\n2.随诊"
}
2026-08-10 16:16:47,334 INFO     29 [qwen-vl-text] Updated encounter_dates=[2026-03-16]
2026-08-10 16:16:47,336 INFO     29 [qwen-vl-text] coord API call start, page=11, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=808447, prompt_len=929
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "互联网医院", "门诊病历", "姓名:", "性别:女", "年龄:75岁", "ID:", "预约挂号", "2026年03月16日15时20分 (江北)心血管内科门诊", "主诉:要求进行心功能分级", "病史:患者平时正常活动不受限。", "过敏史:无吸烟史", "药物过敏史。无流行病学史", "体查:", "级)", "诊断:", "1.心功能I级(NYHA分", "2.高脂血症", "处理:随诊", "1.非诺贝特胶囊(力平之)", "200mg/粒", "用法:1粒", "口服", "一次/日", "x3盒 28天", "医师:", "齐", "第1页"]

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
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord API raw response (len=1508):
[
	{"text": "南京鼓楼医院", "bbox": [444, 203, 579, 236]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [408, 227, 613, 266]},
	{"text": "互联网医院", "bbox": [336, 261, 388, 280]},
	{"text": "门诊病历", "bbox": [470, 261, 550, 293]},
	{"text": "姓名:", "bbox": [331, 287, 360, 305]},
	{"text": "性别:女", "bbox": [424, 294, 463, 312]},
	{"text": "年龄:75岁", "bbox": [509, 300, 553, 318]},
	{"text": "ID:", "bbox": [592, 308, 608, 323]},
	{"text": "预约挂号", "bbox": [638, 287, 676, 302]},
	{"text": "2026年03月16日15时20分 (江北)心血管内科门诊", "bbox": [328, 317, 556, 348]},
	{"text": "主诉:要求进行心功能分级", "bbox": [328, 349, 453, 370]},
	{"text": "病史:患者平时正常活动不受限。", "bbox": [327, 378, 478, 400]},
	{"text": "过敏史:无吸烟史", "bbox": [326, 408, 413, 426]},
	{"text": "药物过敏史。无流行病学史", "bbox": [367, 434, 497, 456]},
	{"text": "体查:", "bbox": [324, 463, 350, 478]},
	{"text": "级)", "bbox": [322, 514, 338, 529]},
	{"text": "诊断:", "bbox": [489, 500, 514, 514]},
	{"text": "1.心功能I级(NYHA分", "bbox": [568, 503, 666, 521]},
	{"text": "2.高脂血症", "bbox": [566, 553, 624, 569]},
	{"text": "处理:随诊", "bbox": [321, 569, 371, 584]},
	{"text": "1.非诺贝特胶囊(力平之)", "bbox": [340, 624, 468, 645]},
	{"text": "200mg/粒", "bbox": [484, 630, 528, 648]},
	{"text": "用法:1粒", "bbox": [371, 652, 416, 669]},
	{"text": "口服", "bbox": [442, 655, 464, 670]},
	{"text": "一次/日", "bbox": [489, 657, 527, 673]},
	{"text": "x3盒 28天", "bbox": [547, 660, 595, 675]},
	{"text": "医师:", "bbox": [512, 714, 537, 729]},
	{"text": "齐", "bbox": [580, 706, 620, 731]},
	{"text": "第1页", "bbox": [470, 909, 509, 926]}
]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=8.1s
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[444, 203, 579, 236]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[408, 227, 613, 266]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[2]: text=互联网医院, bbox=[336, 261, 388, 280]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[3]: text=门诊病历, bbox=[470, 261, 550, 293]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[4]: text=姓名:, bbox=[331, 287, 360, 305]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[5]: text=性别:女, bbox=[424, 294, 463, 312]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[6]: text=年龄:75岁, bbox=[509, 300, 553, 318]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[7]: text=ID:, bbox=[592, 308, 608, 323]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[8]: text=预约挂号, bbox=[638, 287, 676, 302]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[9]: text=2026年03月16日15时20分 (江北)心血管内科门诊, bbox=[328, 317, 556, 348]
2026-08-10 16:16:55,389 INFO     29 [qwen-vl-text] coord item[10]: text=主诉:要求进行心功能分级, bbox=[328, 349, 453, 370]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[11]: text=病史:患者平时正常活动不受限。, bbox=[327, 378, 478, 400]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[12]: text=过敏史:无吸烟史, bbox=[326, 408, 413, 426]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[13]: text=药物过敏史。无流行病学史, bbox=[367, 434, 497, 456]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[14]: text=体查:, bbox=[324, 463, 350, 478]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[15]: text=级), bbox=[322, 514, 338, 529]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[16]: text=诊断:, bbox=[489, 500, 514, 514]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[17]: text=1.心功能I级(NYHA分, bbox=[568, 503, 666, 521]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[18]: text=2.高脂血症, bbox=[566, 553, 624, 569]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[19]: text=处理:随诊, bbox=[321, 569, 371, 584]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[20]: text=1.非诺贝特胶囊(力平之), bbox=[340, 624, 468, 645]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[21]: text=200mg/粒, bbox=[484, 630, 528, 648]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[22]: text=用法:1粒, bbox=[371, 652, 416, 669]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[23]: text=口服, bbox=[442, 655, 464, 670]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[24]: text=一次/日, bbox=[489, 657, 527, 673]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[25]: text=x3盒 28天, bbox=[547, 660, 595, 675]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[26]: text=医师:, bbox=[512, 714, 537, 729]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[27]: text=齐, bbox=[580, 706, 620, 731]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] coord item[28]: text=第1页, bbox=[470, 909, 509, 926]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] page=11 — 29/29 coords, api_time=8.1s
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] new_positions (29):
[[11, 373.79916650390624, 487.4543184814453, 120.8410281982422, 140.48513623046875], [11, 343.4911259765625, 516.0785789794921, 135.12765222167968, 158.34341625976563], [11, 282.875044921875, 326.6533256835937, 155.3670362548828, 166.6772802734375], [11, 395.6883068847656, 463.0395080566406, 155.3670362548828, 174.41586828613282], [11, 278.6655948486328, 303.0804052734375, 170.84421228027344, 181.55918029785158], [11, 356.9613662109375, 389.79507678222654, 175.01114428710937, 185.72611230468752], [11, 428.5220174560547, 465.5651781005859, 178.58280029296876, 189.29776831054687], [11, 498.398888671875, 511.86912890625, 183.34500830078125, 192.2741483154297], [11, 537.1258293457031, 569.1176499023437, 170.84421228027344, 179.7733522949219], [11, 276.1399248046875, 468.09084814453126, 188.70249230957032, 207.15604833984375], [11, 276.1399248046875, 381.3761766357422, 207.75132434082033, 220.25212036132814], [11, 275.2980347900391, 402.42342700195314, 225.01432836914063, 238.11040039062502], [11, 274.4561447753906, 347.7005760498047, 242.8726083984375, 253.58757641601562], [11, 308.9736353759766, 418.41933728027345, 258.3497844238281, 271.44585644531253], [11, 272.77236474609373, 294.6615051269531, 275.61278845214844, 284.5419284667969], [11, 271.08858471679684, 284.55882495117186, 305.9718645019531, 314.9010045166016], [11, 411.6842171630859, 432.7314675292969, 297.63800048828125, 305.9718645019531], [11, 478.1935283203125, 560.6987497558594, 299.42382849121094, 310.1387965087891], [11, 476.5097482910156, 525.339369140625, 329.1876285400391, 338.7120445556641], [11, 270.24669470214843, 312.3411954345703, 338.7120445556641, 347.64118457031253], [11, 286.24260498046874, 394.0045268554687, 371.45222460937504, 383.9530206298828], [11, 407.47476708984374, 444.517927734375, 375.0238806152344, 385.7388486328125], [11, 312.3411954345703, 350.22624609375, 388.1199526367188, 398.23964465332034], [11, 372.11538647460935, 390.636966796875, 389.90578063964847, 398.83492065429687], [11, 411.6842171630859, 443.67603771972654, 391.0963326416016, 400.62074865722656], [11, 460.5138380126953, 500.9245587158203, 392.88216064453127, 401.8113006591797], [11, 431.0476875, 452.09493786621096, 425.02706469726564, 433.9562047119141], [11, 488.29620849609375, 521.9718090820312, 420.26485668945315, 435.1467567138672], [11, 395.6883068847656, 428.5220174560547, 541.1058848876953, 551.2255769042969]]
2026-08-10 16:16:55,390 INFO     29 [qwen-vl-text] ═══ DONE ═══ 29 positions, pages=1, time=9.9s
2026-08-10 16:16:55,399 INFO     29 [Pipeline] Component [6]: Extractor:Clinical finished. error=None
2026-08-10 16:16:55,399 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Clinical | outputs={"chunks": "1 items, types={'OutpatientRecord': 1}", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:16:55,399 INFO     29 [Pipeline] Executing component [7]: Extractor:Medication (type=Extractor)
2026-08-10 16:16:55,404 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:55,405 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条购药凭证/多少个收款日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多张购药凭证/多个收款日期的药品时，将所有药品行合并进同一个 JSON 对象的 medications 数组\n\n## MedicationRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 购药日期 YYYY-MM-DD, 多记录时必填>\",\n  \"pharmacy\": \"<string|null, 药房/药店名称>\",\n  \"medications\": [\n    {\n      \"name\": \"<string, 药品名称，含商品名>\",\n      \"specification\": \"<string|null, 药品规格，如 2.5mg*16粒*盒>\",\n      \"dosage\": \"<string|null, 单次剂量>\",\n      \"quantity\": \"<number|null, 购买数量（盒/支/瓶）>\",\n      \"unit_price\": \"<number|null, 单价（元）>\",\n      \"total_price\": \"<number|null, 金额小计（元）>\",\n      \"frequency\": \"<string|null, 给药频次>\",\n      \"route\": \"<string|null, 给药途径>\",\n      \"manufacturer\": \"<string|null, 生产厂商>\",\n      \"approval_number\": \"<string|null, 批准文号>\"\n    }\n  ],\n  \"payment_total\": \"<number|null, 支付总金额（元）>\",\n  \"payment_method\": \"<string|null, 支付方式>\"\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 如果原文包含多张购药凭证，必须全部逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 数量和金额必须从原文中精确提取，不要通过计算推导"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:16:56,147 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:16:56.145+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:16:56,839 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:56,847 INFO     29 [Pipeline] Component [7]: Extractor:Medication finished. error=None
2026-08-10 16:16:56,847 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Medication | outputs={"chunks": "1 items", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:16:56,847 INFO     29 [Pipeline] Executing component [8]: Extractor:Prescription (type=Extractor)
2026-08-10 16:16:56,855 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:56,856 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗文档结构化提取专家。根据文档分类结果和原文内容，提取处方/取药执行单的结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：无论原文包含多少条处方/多少个开立日期，始终只输出单个 JSON 对象（禁止输出 JSON 数组）。**\n- 原文包含多条处方或多个开立日期的药品行时，将它们全部合并进同一个 JSON 对象的 items 数组\n- encounter_date 取原文中出现的最新开立日期\n\n## PrescriptionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 处方/取药日期 YYYY-MM-DD>\",\n  \"prescription_type\": \"<string|null, 处方类型：门诊处方/住院处方/出院带药/取药执行单>\",\n  \"prescriber\": \"<string|null, 处方医师/开方医生姓名>\",\n  \"department\": \"<string|null, 开方科室>\",\n  \"diagnosis\": \"<string|null, 临床诊断（处方上的诊断信息）>\",\n  \"items\": [\n    {\n      \"drug_generic_name\": \"<string, 药品通用名>\",\n      \"drug_trade_name\": \"<string|null, 药品商品名>\",\n      \"drug_category\": \"<string|null, 药品分类：西药/中成药/中草药/生物制品>\",\n      \"dosage\": \"<string|null, 剂量（如 500mg、0.8ml）>\",\n      \"frequency\": \"<string|null, 频次（如 bid/tid/qd/每二周一次）>\",\n      \"route\": \"<string|null, 给药途径（口服/静脉/皮下注射/肌注等）>\",\n      \"duration_days\": \"<number|null, 用药天数>\",\n      \"quantity\": \"<string|null, 数量（如 1盒、2支）>\",\n      \"notes\": \"<string|null, 备注（如 饭后服用、需冷藏）>\"\n    }\n  ]\n}\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. 取药执行单中的每味药品必须逐条提取，不得遗漏\n4. OCR 纠错规则（重要）：\n   - 药品名称中的常见 OCR 错别字必须纠正为正确写法：\n     ✗ \"甲氨喋呤\" → ✓ \"甲氨蝶呤\"\n     ✗ \"塞来昔布胺囊\" → ✓ \"塞来昔布胶囊\"（OCR 常将\"胶\"误识别）\n     ✗ \"美洛昔庚\" → ✓ \"美洛昔康\"\n   - 日期中出现月份=00或日期=00为 OCR 数字错误，尝试从上下文推断正确日期。\n     若无法推断，保留原值并添加 \"date_uncertain\": true\n   - 纠正原则：仅纠正高置信度的标准药品名称和明显无效日期格式，不得臆测\n5. 如果原文包含多张处方，必须全部逐条提取，不得遗漏"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:16:57,311 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:57,320 INFO     29 [Pipeline] Component [8]: Extractor:Prescription finished. error=None
2026-08-10 16:16:57,320 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Prescription | outputs={"chunks": "1 items", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:16:57,320 INFO     29 [Pipeline] Executing component [9]: Extractor:Discharge (type=Extractor)
2026-08-10 16:16:57,328 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:16:57,329 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:16:57,329 INFO     29 [qwen-vl-text] ═══ START ═══ type=DischargeRecord, doc_id=None
2026-08-10 16:16:57,329 INFO     29 [qwen-vl-text] positions(112): [[1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [1, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [2, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0], [3, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:16:57,329 INFO     29 [qwen-vl-text] page grouping: [1, 2, 3], lines per page: [38, 36, 38]
2026-08-10 16:16:57,472 INFO     29 [qwen-vl-text] page=1, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:16:57,615 INFO     29 [qwen-vl-text] page=2, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:16:57,748 INFO     29 [qwen-vl-text] page=3, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:16:57,749 INFO     29 [qwen-vl-text] LLM extraction start, text_len=3383
2026-08-10 16:16:57,749 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:16:57,749 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗出院记录结构化提取专家。从出院记录/出院小结/出院病情证明书中提取结构化数据。\n\n## 上游分类结果\n{\"type\": \"DischargeRecord\", \"bbox_start\": 3, \"bbox_end\": 114, \"encounter_dates\": [\"2025-12-03\", \"2025-12-06\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## DischargeRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"admission_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"discharge_date\": \"<string|null, 出院日期 YYYY-MM-DD>\",\n  \"hospital_days\": \"<integer|null, 住院天数>\",\n  \"department\": \"<string|null, 科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"admission_condition\": \"<string|null, 入院情况/入院查体完整文本，包含体温脉搏血压等>\",\n  \"admission_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"treatment_summary\": \"<string|null, 诊疗经过完整文本，保留检查、手术、用药等全部细节>\",\n  \"auxiliary_exams\": \"<string|null, 入院后辅助检查结果摘要（含检验指标数值）>\",\n  \"imaging_findings\": \"<string|null, 影像检查结果摘要（CT/MRI/超声等）>\",\n  \"discharge_diagnoses\": [{\"name\": \"<诊断名称>\", \"diagnosis_type\": \"<中医/西医|null>\"}],\n  \"condition_at_discharge\": \"<string|null, 出院时情况>\",\n  \"outcome\": \"<string|null, 治愈/好转/未愈/死亡>\",\n  \"discharge_orders\": \"<string|null, 出院医嘱完整文本>\",\n  \"do_medications\": [\"<string, 出院带药：药名 剂量 频次 天数>\"],\n  \"do_follow_up\": \"<string|null, 随访建议>\",\n  \"do_precautions\": [\"<string, 注意事项>\"],\n  \"next_treatment_date\": \"<string|null, 下次化疗/复诊时间>\",\n  \"attending_physician\": \"<string|null, 主治医师/医疗组长>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG体能状态评分 0-4>\",\n  \"body_surface_area\": \"<number|null, 体表面积 m²>\",\n  \"vs_temperature_c\": \"<number|null, 入院体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 入院脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 入院呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 入院收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 入院舒张压 mmHg>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 诊断列表必须逐条完整提取，区分中医/西医\n4. 出院带药必须包含药名+剂量+频次+天数\n5. 诊疗经过要完整保留手术名称、化疗方案（药名+剂量）、靶向/免疫治疗药物等关键信息\n6. 如果文档含有ECOG评分或体表面积，必须提取\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名\n住院号\n姓名：\n性别：女 年龄：75岁 婚姻：已婚 职业：农民\n入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日\n厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门\n淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋\n下淋巴结肿大（右）7. 心功能III级（NYHA分级）\n8. 甲状腺功能减退症 9. 高血压2级（极高\n危）10. 肺气肿（局限性）11. 肺诊断性影像检\n查的异常所见（肺结节）12. 二尖瓣反流（重度）\n13. 心包积液（少量）14. 肾上腺结节（左侧）\n手术名称：\n手术日期：\n出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日\n疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）\n4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大\n6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大\n(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能\nIII级(NYHA分级) 10. 甲状腺功能减退症\n11. 高血压2级（极高危）12. 肺气肿(局\n限性) 13. 肺诊断性影像检查的异常所见(肺\n结节) 14. 二尖瓣反流(重度) 15. 心包积\n液(少量) 16. 肾上腺结节(左侧)\n入院时情况（主要症状、体征，有关实验室及器械检查结果）：\n患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除\n外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大\n淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回\n示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，\nCK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情\n于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于\n2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复\n查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07\n行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟\n第 1 页\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号\n“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变\n化。\n诊疗经过：\n患者入院完善相关检查：\n【检验】\n2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，\n*游离甲状腺素 9.58 pmol/L↓。\n2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶\n26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。\n2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯\n8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51\nmmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8\nmmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。\n2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数\n3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*\n血小板计数 112 ×10^9/L↓。\n余未见明显异常。\n【检查】\n2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支\n阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长\n2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺\n门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软\n组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上\n考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建\n议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左\n肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺\n瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度\n欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉\n及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可\n能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔\n内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑\n第 2 页\n3/4\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n出院记录\n科别（江北）综合肿瘤中心 病区（江北）B7病区床号\n姓名 住院号\n良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随\n诊。\n【诊疗经过】\n患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05\n行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理\n出院。\n出院情况： 好转\n伤口愈合：-\nECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲\n张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音\n稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳\n痛。双下肢无明显水肿。\n出院医嘱：\n1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。\n2、出院后继续用药\n左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激\n素，内分泌科随诊调药）\n3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化\n全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门\n诊随诊。\n4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五\n上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日\n间治疗，请提前一周至杨阳主任医师门诊预约。\n5、不适门诊随诊。\n不存在尚未回归的病理检查结果。\nX光片号：-\nCT号： P049684\nMRI号：-\n病理号：-\n上级医师：\n医师：\n第 3 页",
    "role": "user"
  }
]
2026-08-10 16:17:28,051 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:17:28.049+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:17:30,331 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:17:30,331 INFO     29 [qwen-vl-text] LLM output (len=6275):
{
  "encounter_date": "2025-12-06",
  "admission_date": "2025-12-03",
  "discharge_date": "2025-12-06",
  "hospital_days": 3,
  "department": "(江北)综合肿瘤中心",
  "bed_number": "07床",
  "admission_condition": "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变化。",
  "admission_diagnoses": [
    {"name": "肺恶性肿瘤（左肺，小细胞癌广泛期）", "diagnosis_type": "西医"},
    {"name": "肥厚型梗阻性心肌病", "diagnosis_type": "西医"},
    {"name": "纵隔淋巴结肿大", "diagnosis_type": "西医"},
    {"name": "肺门淋巴结肿大", "diagnosis_type": "西医"},
    {"name": "锁骨上淋巴结肿大（双侧）", "diagnosis_type": "西医"},
    {"name": "腋下淋巴结肿大（右）", "diagnosis_type": "西医"},
    {"name": "心功能III级（NYHA分级）", "diagnosis_type": "西医"},
    {"name": "甲状腺功能减退症", "diagnosis_type": "西医"},
    {"name": "高血压2级（极高危）", "diagnosis_type": "西医"},
    {"name": "肺气肿（局限性）", "diagnosis_type": "西医"},
    {"name": "肺诊断性影像检查的异常所见（肺结节）", "diagnosis_type": "西医"},
    {"name": "二尖瓣反流（重度）", "diagnosis_type": "西医"},
    {"name": "心包积液（少量）", "diagnosis_type": "西医"},
    {"name": "肾上腺结节（左侧）", "diagnosis_type": "西医"}
  ],
  "treatment_summary": "患者入院完善相关检查：【检验】2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，*游离甲状腺素 9.58 pmol/L↓。2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51 mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8 mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*血小板计数 112 ×10^9/L↓。余未见明显异常。【检查】2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长。2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随诊。【诊疗经过】患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理出院。",
  "auxiliary_exams": "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，*游离甲状腺素 9.58 pmol/L↓。2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶 26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯 8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51 mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8 mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数 3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*血小板计数 112 ×10^9/L↓。",
  "imaging_findings": "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长。2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随诊。",
  "discharge_diagnoses": [
    {"name": "恶性肿瘤支持治疗", "diagnosis_type": "西医"},
    {"name": "恶性肿瘤免疫治疗", "diagnosis_type": "西医"},
    {"name": "肺恶性肿瘤（左肺，小细胞癌广泛期）", "diagnosis_type": "西医"},
    {"name": "肥厚型梗阻性心肌病", "diagnosis_type": "西医"},
    {"name": "纵隔淋巴结肿大", "diagnosis_type": "西医"},
    {"name": "肺门淋巴结肿大", "diagnosis_type": "西医"},
    {"name": "锁骨上淋巴结肿大(双侧)", "diagnosis_type": "西医"},
    {"name": "腋下淋巴结肿大(右)", "diagnosis_type": "西医"},
    {"name": "心功能III级(NYHA分级)", "diagnosis_type": "西医"},
    {"name": "甲状腺功能减退症", "diagnosis_type": "西医"},
    {"name": "高血压2级（极高危）", "diagnosis_type": "西医"},
    {"name": "肺气肿(局限性)", "diagnosis_type": "西医"},
    {"name": "肺诊断性影像检查的异常所见(肺结节)", "diagnosis_type": "西医"},
    {"name": "二尖瓣反流(重度)", "diagnosis_type": "西医"},
    {"name": "心包积液(少量)", "diagnosis_type": "西医"},
    {"name": "肾上腺结节(左侧)", "diagnosis_type": "西医"}
  ],
  "condition_at_discharge": "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳痛。双下肢无明显水肿。",
  "outcome": "好转",
  "discharge_orders": "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。2、出院后继续用药 左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激素，内分泌科随诊调药）3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门诊随诊。4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日间治疗，请提前一周至杨阳主任医师门诊预约。5、不适门诊随诊。",
  "do_medications": [
    "左甲状腺素钠片（优甲乐） 50微克/片 1片 口服 QD"
  ],
  "do_follow_up": "定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门诊随诊。",
  "do_precautions": [
    "注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。"
  ],
  "next_treatment_date": "3-4周左右",
  "attending_physician": "杨阳",
  "pe_ecog_score": 1,
  "body_surface_area": null,
  "vs_temperature_c": null,
  "vs_pulse_bpm": null,
  "vs_respiration_rpm": null,
  "vs_systolic_bp_mmhg": null,
  "vs_diastolic_bp_mmhg": null
}
2026-08-10 16:17:30,331 INFO     29 [qwen-vl-text] Updated encounter_dates=[2025-12-06]
2026-08-10 16:17:30,334 INFO     29 [qwen-vl-text] coord API call start, page=1, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1026668, prompt_len=1880
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "住院号", "姓名：", "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "8. 甲状腺功能减退症 9. 高血压2级（极高", "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "13. 心包积液（少量）14. 肾上腺结节（左侧）", "手术名称：", "手术日期：", "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "III级(NYHA分级) 10. 甲状腺功能减退症", "11. 高血压2级（极高危）12. 肺气肿(局", "限性) 13. 肺诊断性影像检查的异常所见(肺", "结节) 14. 二尖瓣反流(重度) 15. 心包积", "液(少量) 16. 肾上腺结节(左侧)", "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "第 1 页"]

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
2026-08-10 16:17:46,667 INFO     29 [qwen-vl-text] coord API raw response (len=2827):
[
	{"text": "南京鼓楼医院", "bbox": [460, 94, 538, 111]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [415, 117, 584, 134]},
	{"text": "出院记录", "bbox": [436, 139, 562, 163]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名", "bbox": [295, 170, 561, 184]},
	{"text": "住院号", "bbox": [608, 170, 638, 184]},
	{"text": "姓名：", "bbox": [295, 197, 318, 211]},
	{"text": "性别：女 年龄：75岁 婚姻：已婚 职业：农民", "bbox": [364, 197, 602, 211]},
	{"text": "入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日", "bbox": [298, 227, 640, 241]},
	{"text": "厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门", "bbox": [343, 250, 527, 264]},
	{"text": "淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋", "bbox": [343, 273, 527, 287]},
	{"text": "下淋巴结肿大（右）7. 心功能III级（NYHA分级）", "bbox": [343, 296, 526, 310]},
	{"text": "8. 甲状腺功能减退症 9. 高血压2级（极高", "bbox": [343, 319, 527, 333]},
	{"text": "危）10. 肺气肿（局限性）11. 肺诊断性影像检", "bbox": [343, 342, 527, 356]},
	{"text": "查的异常所见（肺结节）12. 二尖瓣反流（重度）", "bbox": [343, 365, 527, 379]},
	{"text": "13. 心包积液（少量）14. 肾上腺结节（左侧）", "bbox": [343, 388, 511, 402]},
	{"text": "手术名称：", "bbox": [298, 415, 338, 428]},
	{"text": "手术日期：", "bbox": [531, 415, 567, 428]},
	{"text": "出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日", "bbox": [298, 441, 640, 455]},
	{"text": "疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）", "bbox": [343, 464, 520, 478]},
	{"text": "4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大", "bbox": [343, 487, 527, 501]},
	{"text": "6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大", "bbox": [343, 510, 517, 524]},
	{"text": "(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能", "bbox": [343, 533, 523, 547]},
	{"text": "III级(NYHA分级) 10. 甲状腺功能减退症", "bbox": [343, 556, 515, 570]},
	{"text": "11. 高血压2级（极高危）12. 肺气肿(局", "bbox": [343, 578, 527, 592]},
	{"text": "限性) 13. 肺诊断性影像检查的异常所见(肺", "bbox": [343, 601, 527, 615]},
	{"text": "结节) 14. 二尖瓣反流(重度) 15. 心包积", "bbox": [343, 624, 519, 638]},
	{"text": "液(少量) 16. 肾上腺结节(左侧)", "bbox": [343, 647, 480, 661]},
	{"text": "入院时情况（主要症状、体征，有关实验室及器械检查结果）：", "bbox": [298, 662, 523, 675]},
	{"text": "患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除", "bbox": [295, 678, 701, 692]},
	{"text": "外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大", "bbox": [295, 701, 701, 715]},
	{"text": "淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回", "bbox": [295, 724, 701, 738]},
	{"text": "示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，", "bbox": [295, 747, 701, 761]},
	{"text": "CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情", "bbox": [295, 770, 701, 784]},
	{"text": "于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于", "bbox": [295, 793, 701, 807]},
	{"text": "2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复", "bbox": [295, 816, 701, 830]},
	{"text": "查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07", "bbox": [295, 839, 701, 853]},
	{"text": "行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟", "bbox": [295, 862, 701, 876]},
	{"text": "第 1 页", "bbox": [471, 912, 515, 924]}
]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=16.3s
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[460, 94, 538, 111]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[415, 117, 584, 134]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[436, 139, 562, 163]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[3]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名, bbox=[295, 170, 561, 184]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[4]: text=住院号, bbox=[608, 170, 638, 184]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[5]: text=姓名：, bbox=[295, 197, 318, 211]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[6]: text=性别：女 年龄：75岁 婚姻：已婚 职业：农民, bbox=[364, 197, 602, 211]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[7]: text=入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日, bbox=[298, 227, 640, 241]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[8]: text=厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门, bbox=[343, 250, 527, 264]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[9]: text=淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋, bbox=[343, 273, 527, 287]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[10]: text=下淋巴结肿大（右）7. 心功能III级（NYHA分级）, bbox=[343, 296, 526, 310]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[11]: text=8. 甲状腺功能减退症 9. 高血压2级（极高, bbox=[343, 319, 527, 333]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[12]: text=危）10. 肺气肿（局限性）11. 肺诊断性影像检, bbox=[343, 342, 527, 356]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[13]: text=查的异常所见（肺结节）12. 二尖瓣反流（重度）, bbox=[343, 365, 527, 379]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[14]: text=13. 心包积液（少量）14. 肾上腺结节（左侧）, bbox=[343, 388, 511, 402]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[15]: text=手术名称：, bbox=[298, 415, 338, 428]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[16]: text=手术日期：, bbox=[531, 415, 567, 428]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[17]: text=出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日, bbox=[298, 441, 640, 455]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[18]: text=疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）, bbox=[343, 464, 520, 478]
2026-08-10 16:17:46,668 INFO     29 [qwen-vl-text] coord item[19]: text=4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大, bbox=[343, 487, 527, 501]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[20]: text=6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大, bbox=[343, 510, 517, 524]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[21]: text=(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能, bbox=[343, 533, 523, 547]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[22]: text=III级(NYHA分级) 10. 甲状腺功能减退症, bbox=[343, 556, 515, 570]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[23]: text=11. 高血压2级（极高危）12. 肺气肿(局, bbox=[343, 578, 527, 592]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[24]: text=限性) 13. 肺诊断性影像检查的异常所见(肺, bbox=[343, 601, 527, 615]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[25]: text=结节) 14. 二尖瓣反流(重度) 15. 心包积, bbox=[343, 624, 519, 638]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[26]: text=液(少量) 16. 肾上腺结节(左侧), bbox=[343, 647, 480, 661]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[27]: text=入院时情况（主要症状、体征，有关实验室及器械检查结果）：, bbox=[298, 662, 523, 675]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[28]: text=患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除, bbox=[295, 678, 701, 692]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[29]: text=外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大, bbox=[295, 701, 701, 715]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[30]: text=淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回, bbox=[295, 724, 701, 738]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[31]: text=示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，, bbox=[295, 747, 701, 761]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[32]: text=CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情, bbox=[295, 770, 701, 784]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[33]: text=于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于, bbox=[295, 793, 701, 807]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[34]: text=2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复, bbox=[295, 816, 701, 830]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[35]: text=查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07, bbox=[295, 839, 701, 853]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[36]: text=行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟, bbox=[295, 862, 701, 876]
2026-08-10 16:17:46,669 INFO     29 [qwen-vl-text] coord item[37]: text=第 1 页, bbox=[471, 912, 515, 924]
2026-08-10 16:17:46,670 INFO     29 [qwen-vl-text] page=1 — 38/38 coords, api_time=16.3s
2026-08-10 16:17:46,673 INFO     29 [qwen-vl-text] coord API call start, page=2, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1058415, prompt_len=2112
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共36行）
["南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "化。", "诊疗经过：", "患者入院完善相关检查：", "【检验】", "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "*游离甲状腺素 9.58 pmol/L↓。", "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "血小板计数 112 ×10^9/L↓。", "余未见明显异常。", "【检查】", "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "第 2 页"]

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
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord API raw response (len=2978):
[
	{"text": "南京鼓楼医院", "bbox": [462, 109, 536, 125]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [420, 132, 579, 148]},
	{"text": "出院记录", "bbox": [440, 152, 558, 174]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号", "bbox": [307, 180, 630, 195]},
	{"text": "“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变", "bbox": [307, 207, 690, 221]},
	{"text": "化。", "bbox": [307, 230, 320, 243]},
	{"text": "诊疗经过：", "bbox": [307, 245, 343, 258]},
	{"text": "患者入院完善相关检查：", "bbox": [307, 264, 392, 277]},
	{"text": "【检验】", "bbox": [307, 285, 337, 298]},
	{"text": "2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，", "bbox": [307, 306, 689, 320]},
	{"text": "*游离甲状腺素 9.58 pmol/L↓。", "bbox": [307, 328, 423, 342]},
	{"text": "2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶", "bbox": [307, 350, 690, 364]},
	{"text": "26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。", "bbox": [307, 372, 500, 385]},
	{"text": "2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯", "bbox": [307, 393, 690, 407]},
	{"text": "8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51", "bbox": [307, 415, 690, 428]},
	{"text": "mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8", "bbox": [307, 437, 690, 450]},
	{"text": "mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。", "bbox": [307, 458, 605, 471]},
	{"text": "2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数", "bbox": [307, 479, 690, 492]},
	{"text": "3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*", "bbox": [307, 500, 690, 514]},
	{"text": "血小板计数 112 ×10^9/L↓。", "bbox": [307, 522, 414, 535]},
	{"text": "余未见明显异常。", "bbox": [307, 542, 369, 555]},
	{"text": "【检查】", "bbox": [307, 563, 337, 576]},
	{"text": "2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支", "bbox": [307, 584, 690, 598]},
	{"text": "阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长", "bbox": [307, 606, 511, 619]},
	{"text": "2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺", "bbox": [307, 627, 690, 640]},
	{"text": "门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软", "bbox": [307, 648, 690, 662]},
	{"text": "组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上", "bbox": [307, 670, 690, 683]},
	{"text": "考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建", "bbox": [307, 691, 690, 705]},
	{"text": "议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左", "bbox": [307, 713, 690, 726]},
	{"text": "肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺", "bbox": [307, 734, 690, 748]},
	{"text": "瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度", "bbox": [307, 756, 690, 769]},
	{"text": "欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉", "bbox": [307, 777, 690, 790]},
	{"text": "及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可", "bbox": [307, 799, 690, 812]},
	{"text": "能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔", "bbox": [307, 820, 690, 834]},
	{"text": "内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑", "bbox": [307, 842, 690, 855]},
	{"text": "第 2 页", "bbox": [473, 880, 515, 891]}
]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord API: raw_items=36, valid_items=36, elapsed=18.3s
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院, bbox=[462, 109, 536, 125]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[1]: text=南京大学医学院附属鼓楼医院, bbox=[420, 132, 579, 148]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[2]: text=出院记录, bbox=[440, 152, 558, 174]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[3]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号, bbox=[307, 180, 630, 195]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[4]: text=“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变, bbox=[307, 207, 690, 221]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[5]: text=化。, bbox=[307, 230, 320, 243]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[6]: text=诊疗经过：, bbox=[307, 245, 343, 258]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[7]: text=患者入院完善相关检查：, bbox=[307, 264, 392, 277]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[8]: text=【检验】, bbox=[307, 285, 337, 298]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[9]: text=2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，, bbox=[307, 306, 689, 320]
2026-08-10 16:18:04,989 INFO     29 [qwen-vl-text] coord item[10]: text=*游离甲状腺素 9.58 pmol/L↓。, bbox=[307, 328, 423, 342]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[11]: text=2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶, bbox=[307, 350, 690, 364]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[12]: text=26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。, bbox=[307, 372, 500, 385]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[13]: text=2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯, bbox=[307, 393, 690, 407]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[14]: text=8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51, bbox=[307, 415, 690, 428]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[15]: text=mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8, bbox=[307, 437, 690, 450]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[16]: text=mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。, bbox=[307, 458, 605, 471]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[17]: text=2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数, bbox=[307, 479, 690, 492]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[18]: text=3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*, bbox=[307, 500, 690, 514]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[19]: text=血小板计数 112 ×10^9/L↓。, bbox=[307, 522, 414, 535]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[20]: text=余未见明显异常。, bbox=[307, 542, 369, 555]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[21]: text=【检查】, bbox=[307, 563, 337, 576]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[22]: text=2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支, bbox=[307, 584, 690, 598]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[23]: text=阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长, bbox=[307, 606, 511, 619]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[24]: text=2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺, bbox=[307, 627, 690, 640]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[25]: text=门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软, bbox=[307, 648, 690, 662]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[26]: text=组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上, bbox=[307, 670, 690, 683]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[27]: text=考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建, bbox=[307, 691, 690, 705]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[28]: text=议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左, bbox=[307, 713, 690, 726]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[29]: text=肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺, bbox=[307, 734, 690, 748]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[30]: text=瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度, bbox=[307, 756, 690, 769]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[31]: text=欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉, bbox=[307, 777, 690, 790]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[32]: text=及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可, bbox=[307, 799, 690, 812]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[33]: text=能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔, bbox=[307, 820, 690, 834]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[34]: text=内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑, bbox=[307, 842, 690, 855]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] coord item[35]: text=第 2 页, bbox=[473, 880, 515, 891]
2026-08-10 16:18:04,990 INFO     29 [qwen-vl-text] page=2 — 36/36 coords, api_time=18.3s
2026-08-10 16:18:04,991 INFO     29 [qwen-vl-text] coord API call start, page=3, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=854444, prompt_len=1564
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共38行）
["3/4", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "出院记录", "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "姓名 住院号", "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "诊。", "【诊疗经过】", "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "出院。", "出院情况： 好转", "伤口愈合：-", "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "痛。双下肢无明显水肿。", "出院医嘱：", "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "2、出院后继续用药", "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "素，内分泌科随诊调药）", "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "诊随诊。", "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "间治疗，请提前一周至杨阳主任医师门诊预约。", "5、不适门诊随诊。", "不存在尚未回归的病理检查结果。", "X光片号：-", "CT号： P049684", "MRI号：-", "病理号：-", "上级医师：", "医师：", "第 3 页"]

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
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord API raw response (len=2512):
[
	{"text": "3/4", "bbox": [315, 102, 340, 121]},
	{"text": "南京鼓楼医院", "bbox": [462, 103, 538, 118]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [418, 125, 582, 141]},
	{"text": "出院记录", "bbox": [439, 146, 561, 169]},
	{"text": "科别（江北）综合肿瘤中心 病区（江北）B7病区床号", "bbox": [303, 176, 510, 190]},
	{"text": "姓名 住院号", "bbox": [544, 176, 635, 190]},
	{"text": "良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随", "bbox": [303, 204, 696, 217]},
	{"text": "诊。", "bbox": [303, 226, 316, 239]},
	{"text": "【诊疗经过】", "bbox": [306, 248, 350, 261]},
	{"text": "患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05", "bbox": [303, 270, 696, 283]},
	{"text": "行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理", "bbox": [303, 293, 696, 306]},
	{"text": "出院。", "bbox": [303, 315, 324, 328]},
	{"text": "出院情况： 好转", "bbox": [303, 338, 365, 351]},
	{"text": "伤口愈合：-", "bbox": [515, 338, 562, 351]},
	{"text": "ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲", "bbox": [303, 360, 696, 373]},
	{"text": "张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音", "bbox": [303, 382, 696, 395]},
	{"text": "稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳", "bbox": [303, 405, 696, 418]},
	{"text": "痛。双下肢无明显水肿。", "bbox": [303, 427, 392, 440]},
	{"text": "出院医嘱：", "bbox": [304, 444, 340, 456]},
	{"text": "1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。", "bbox": [303, 478, 646, 491]},
	{"text": "2、出院后继续用药", "bbox": [303, 501, 374, 514]},
	{"text": "左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激", "bbox": [303, 523, 696, 536]},
	{"text": "素，内分泌科随诊调药）", "bbox": [303, 545, 391, 558]},
	{"text": "3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化", "bbox": [303, 567, 696, 580]},
	{"text": "全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门", "bbox": [303, 589, 696, 602]},
	{"text": "诊随诊。", "bbox": [303, 612, 332, 625]},
	{"text": "4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五", "bbox": [303, 634, 696, 647]},
	{"text": "上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日", "bbox": [303, 656, 696, 669]},
	{"text": "间治疗，请提前一周至杨阳主任医师门诊预约。", "bbox": [303, 678, 475, 691]},
	{"text": "5、不适门诊随诊。", "bbox": [303, 700, 378, 713]},
	{"text": "不存在尚未回归的病理检查结果。", "bbox": [303, 722, 424, 735]},
	{"text": "X光片号：-", "bbox": [519, 746, 563, 758]},
	{"text": "CT号： P049684", "bbox": [519, 770, 588, 782]},
	{"text": "MRI号：-", "bbox": [519, 792, 563, 805]},
	{"text": "病理号：-", "bbox": [519, 816, 563, 828]},
	{"text": "上级医师：", "bbox": [303, 860, 381, 875]},
	{"text": "医师：", "bbox": [497, 855, 558, 875]},
	{"text": "第 3 页", "bbox": [473, 895, 515, 907]}
]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord API: raw_items=38, valid_items=38, elapsed=13.0s
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[0]: text=3/4, bbox=[315, 102, 340, 121]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[1]: text=南京鼓楼医院, bbox=[462, 103, 538, 118]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[2]: text=南京大学医学院附属鼓楼医院, bbox=[418, 125, 582, 141]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[3]: text=出院记录, bbox=[439, 146, 561, 169]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[4]: text=科别（江北）综合肿瘤中心 病区（江北）B7病区床号, bbox=[303, 176, 510, 190]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[5]: text=姓名 住院号, bbox=[544, 176, 635, 190]
2026-08-10 16:18:18,035 INFO     29 [qwen-vl-text] coord item[6]: text=良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随, bbox=[303, 204, 696, 217]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[7]: text=诊。, bbox=[303, 226, 316, 239]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[8]: text=【诊疗经过】, bbox=[306, 248, 350, 261]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[9]: text=患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05, bbox=[303, 270, 696, 283]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[10]: text=行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理, bbox=[303, 293, 696, 306]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[11]: text=出院。, bbox=[303, 315, 324, 328]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[12]: text=出院情况： 好转, bbox=[303, 338, 365, 351]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[13]: text=伤口愈合：-, bbox=[515, 338, 562, 351]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[14]: text=ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲, bbox=[303, 360, 696, 373]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[15]: text=张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音, bbox=[303, 382, 696, 395]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[16]: text=稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳, bbox=[303, 405, 696, 418]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[17]: text=痛。双下肢无明显水肿。, bbox=[303, 427, 392, 440]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[18]: text=出院医嘱：, bbox=[304, 444, 340, 456]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[19]: text=1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。, bbox=[303, 478, 646, 491]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[20]: text=2、出院后继续用药, bbox=[303, 501, 374, 514]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[21]: text=左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激, bbox=[303, 523, 696, 536]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[22]: text=素，内分泌科随诊调药）, bbox=[303, 545, 391, 558]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[23]: text=3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化, bbox=[303, 567, 696, 580]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[24]: text=全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门, bbox=[303, 589, 696, 602]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[25]: text=诊随诊。, bbox=[303, 612, 332, 625]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[26]: text=4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五, bbox=[303, 634, 696, 647]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[27]: text=上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日, bbox=[303, 656, 696, 669]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[28]: text=间治疗，请提前一周至杨阳主任医师门诊预约。, bbox=[303, 678, 475, 691]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[29]: text=5、不适门诊随诊。, bbox=[303, 700, 378, 713]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[30]: text=不存在尚未回归的病理检查结果。, bbox=[303, 722, 424, 735]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[31]: text=X光片号：-, bbox=[519, 746, 563, 758]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[32]: text=CT号： P049684, bbox=[519, 770, 588, 782]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[33]: text=MRI号：-, bbox=[519, 792, 563, 805]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[34]: text=病理号：-, bbox=[519, 816, 563, 828]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[35]: text=上级医师：, bbox=[303, 860, 381, 875]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[36]: text=医师：, bbox=[497, 855, 558, 875]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] coord item[37]: text=第 3 页, bbox=[473, 895, 515, 907]
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] page=3 — 38/38 coords, api_time=13.0s
2026-08-10 16:18:18,036 INFO     29 [qwen-vl-text] new_positions (112):
[[1, 387.26940673828125, 452.93682788085937, 55.95594409179688, 66.07563610839844], [1, 349.38435607910156, 491.6637685546875, 69.64729211425781, 79.76698413085938], [1, 367.06404638671876, 473.14218823242186, 82.7433641357422, 97.0299881591797], [1, 248.35755432128906, 472.30029821777345, 101.19692016601563, 109.5307841796875], [1, 511.86912890625, 537.1258293457031, 101.19692016601563, 109.5307841796875], [1, 248.35755432128906, 267.72102465820313, 117.26937219238282, 125.60323620605469], [1, 306.44796533203123, 506.81778881835936, 117.26937219238282, 125.60323620605469], [1, 250.88322436523438, 538.809609375, 135.12765222167968, 143.46151623535158], [1, 288.76827502441404, 443.67603771972654, 148.81900024414062, 157.1528642578125], [1, 288.76827502441404, 443.67603771972654, 162.51034826660157, 170.84421228027344], [1, 288.76827502441404, 442.8341477050781, 176.2016962890625, 184.53556030273438], [1, 288.76827502441404, 443.67603771972654, 189.89304431152345, 198.22690832519532], [1, 288.76827502441404, 443.67603771972654, 203.5843923339844, 211.91825634765627], [1, 288.76827502441404, 443.67603771972654, 217.2757403564453, 225.6096043701172], [1, 288.76827502441404, 430.2057974853516, 230.96708837890625, 239.30095239257813], [1, 250.88322436523438, 284.55882495117186, 247.03954040527344, 254.77812841796876], [1, 447.0435977783203, 477.35163830566404, 247.03954040527344, 254.77812841796876], [1, 250.88322436523438, 538.809609375, 262.5167164306641, 270.85058044433595], [1, 288.76827502441404, 437.7828076171875, 276.208064453125, 284.5419284667969], [1, 288.76827502441404, 443.67603771972654, 289.89941247558596, 298.23327648925783], [1, 288.76827502441404, 435.2571375732422, 303.5907604980469, 311.9246245117188], [1, 288.76827502441404, 440.3084776611328, 317.28210852050785, 325.6159725341797], [1, 288.76827502441404, 433.5733575439453, 330.9734565429688, 339.30732055664066], [1, 288.76827502441404, 443.67603771972654, 344.06952856445315, 352.403392578125], [1, 288.76827502441404, 443.67603771972654, 357.7608765869141, 366.09474060058596], [1, 288.76827502441404, 436.94091760253906, 371.45222460937504, 379.7860886230469], [1, 288.76827502441404, 404.10720703124997, 385.143572631836, 393.47743664550785], [1, 250.88322436523438, 440.3084776611328, 394.0727126464844, 401.8113006591797], [1, 248.35755432128906, 590.1649002685547, 403.5971286621094, 411.9309926757813], [1, 248.35755432128906, 590.1649002685547, 417.28847668457036, 425.6223406982422], [1, 248.35755432128906, 590.1649002685547, 430.97982470703124, 439.31368872070317], [1, 248.35755432128906, 590.1649002685547, 444.6711727294922, 453.00503674316406], [1, 248.35755432128906, 590.1649002685547, 458.3625207519531, 466.696384765625], [1, 248.35755432128906, 590.1649002685547, 472.05386877441407, 480.38773278808594], [1, 248.35755432128906, 590.1649002685547, 485.745216796875, 494.0790808105469], [1, 248.35755432128906, 590.1649002685547, 499.43656481933596, 507.7704288330078], [1, 248.35755432128906, 590.1649002685547, 513.1279128417968, 521.4617768554688], [1, 396.5301968994141, 433.5733575439453, 542.8917128906251, 550.0350249023438], [2, 388.95318676757813, 451.2530478515625, 64.88508410644532, 74.40950012207031], [2, 353.59380615234375, 487.4543184814453, 78.57643212890625, 88.10084814453126], [2, 370.43160644531247, 469.7746281738281, 90.4819521484375, 103.57802416992187], [2, 258.4602344970703, 530.3907092285157, 107.14968017578126, 116.0788201904297], [2, 258.4602344970703, 580.9041101074218, 123.22213220214844, 131.55599621582033], [2, 258.4602344970703, 269.4048046875, 136.91348022460937, 144.6520682373047], [2, 258.4602344970703, 288.76827502441404, 145.84262023925783, 153.58120825195314], [2, 258.4602344970703, 330.0208857421875, 157.1528642578125, 164.8914522705078], [2, 258.4602344970703, 283.71693493652344, 169.65366027832033, 177.39224829101562], [2, 258.4602344970703, 580.0622200927735, 182.15445629882814, 190.4883203125], [2, 258.4602344970703, 356.11947619628904, 195.2505283203125, 203.5843923339844], [2, 258.4602344970703, 580.9041101074218, 208.3466003417969, 216.68046435546876], [2, 258.4602344970703, 420.94500732421875, 221.44267236328125, 229.18126037597656], [2, 258.4602344970703, 580.9041101074218, 233.94346838378908, 242.27733239746095], [2, 258.4602344970703, 580.9041101074218, 247.03954040527344, 254.77812841796876], [2, 258.4602344970703, 580.9041101074218, 260.1356124267578, 267.87420043945315], [2, 258.4602344970703, 509.34345886230466, 272.63640844726564, 280.3749964599609], [2, 258.4602344970703, 580.9041101074218, 285.1372044677735, 292.87579248046876], [2, 258.4602344970703, 580.9041101074218, 297.63800048828125, 305.9718645019531], [2, 258.4602344970703, 348.5424660644531, 310.7340725097656, 318.47266052246096], [2, 258.4602344970703, 310.6574154052734, 322.63959252929686, 330.3781805419922], [2, 258.4602344970703, 283.71693493652344, 335.1403885498047, 342.87897656250004], [2, 258.4602344970703, 580.9041101074218, 347.64118457031253, 355.9750485839844], [2, 258.4602344970703, 430.2057974853516, 360.7372565917969, 368.4758446044922], [2, 258.4602344970703, 580.9041101074218, 373.2380526123047, 380.976640625], [2, 258.4602344970703, 580.9041101074218, 385.7388486328125, 394.0727126464844], [2, 258.4602344970703, 580.9041101074218, 398.83492065429687, 406.5735086669922], [2, 258.4602344970703, 580.9041101074218, 411.3357166748047, 419.6695806884766], [2, 258.4602344970703, 580.9041101074218, 424.43178869628906, 432.1703767089844], [2, 258.4602344970703, 580.9041101074218, 436.9325847167969, 445.26644873046877], [2, 258.4602344970703, 580.9041101074218, 450.02865673828126, 457.7672447509766], [2, 258.4602344970703, 580.9041101074218, 462.5294527587891, 470.2680407714844], [2, 258.4602344970703, 580.9041101074218, 475.62552478027345, 483.3641127929688], [2, 258.4602344970703, 580.9041101074218, 488.1263208007813, 496.46018481445316], [2, 258.4602344970703, 580.9041101074218, 501.22239282226565, 508.96098083496094], [2, 398.2139769287109, 433.5733575439453, 523.842880859375, 530.3909168701172], [3, 265.19535461425784, 286.24260498046874, 60.71815209960938, 72.02839611816407], [3, 388.95318676757813, 452.93682788085937, 61.31342810058594, 70.24256811523438], [3, 351.91002612304686, 489.97998852539064, 74.40950012207031, 83.93391613769532], [3, 369.58971643066405, 472.30029821777345, 86.91029614257813, 100.60164416503906], [3, 255.09267443847656, 429.3639074707031, 104.768576171875, 113.10244018554688], [3, 457.98816796875, 534.6001593017578, 104.768576171875, 113.10244018554688], [3, 255.09267443847656, 585.9554501953124, 121.43630419921875, 129.17489221191406], [3, 255.09267443847656, 266.03724462890625, 134.53237622070313, 142.27096423339844], [3, 257.6183444824219, 294.6615051269531, 147.62844824218752, 155.3670362548828], [3, 255.09267443847656, 585.9554501953124, 160.72452026367188, 168.4631082763672], [3, 255.09267443847656, 585.9554501953124, 174.41586828613282, 182.15445629882814], [3, 255.09267443847656, 272.77236474609373, 187.5119403076172, 195.2505283203125], [3, 255.09267443847656, 307.2898553466797, 201.20328833007812, 208.94187634277344], [3, 433.5733575439453, 473.14218823242186, 201.20328833007812, 208.94187634277344], [3, 255.09267443847656, 585.9554501953124, 214.2993603515625, 222.03794836425783], [3, 255.09267443847656, 585.9554501953124, 227.39543237304687, 235.1340203857422], [3, 255.09267443847656, 585.9554501953124, 241.08678039550782, 248.82536840820313], [3, 255.09267443847656, 330.0208857421875, 254.1828524169922, 261.9214404296875], [3, 255.934564453125, 286.24260498046874, 264.30254443359377, 271.44585644531253], [3, 255.09267443847656, 543.8609494628906, 284.5419284667969, 292.2805164794922], [3, 255.09267443847656, 314.86686547851565, 298.23327648925783, 305.9718645019531], [3, 255.09267443847656, 585.9554501953124, 311.3293485107422, 319.06793652343754], [3, 255.09267443847656, 329.1789957275391, 324.42542053222655, 332.1640085449219], [3, 255.09267443847656, 585.9554501953124, 337.52149255371097, 345.26008056640626], [3, 255.09267443847656, 585.9554501953124, 350.61756457519533, 358.3561525878906], [3, 255.09267443847656, 279.50748486328126, 364.3089125976563, 372.04750061035156], [3, 255.09267443847656, 585.9554501953124, 377.40498461914063, 385.143572631836], [3, 255.09267443847656, 585.9554501953124, 390.501056640625, 398.23964465332034], [3, 255.09267443847656, 399.8977569580078, 403.5971286621094, 411.3357166748047], [3, 255.09267443847656, 318.23442553710936, 416.6932006835938, 424.43178869628906], [3, 255.09267443847656, 356.9613662109375, 429.78927270507813, 437.5278607177735], [3, 436.94091760253906, 473.98407824707033, 444.07589672851566, 451.2192087402344], [3, 436.94091760253906, 495.03132861328123, 458.3625207519531, 465.5058327636719], [3, 436.94091760253906, 473.98407824707033, 471.45859277343754, 479.19718078613283], [3, 436.94091760253906, 473.98407824707033, 485.745216796875, 492.8885288085938], [3, 255.09267443847656, 320.76009558105466, 511.9373608398438, 520.8665008544922], [3, 418.41933728027345, 469.7746281738281, 508.96098083496094, 520.8665008544922], [3, 398.2139769287109, 433.5733575439453, 532.7720208740235, 539.9153328857423]]
2026-08-10 16:18:18,037 INFO     29 [qwen-vl-text] ═══ DONE ═══ 112 positions, pages=3, time=80.7s
2026-08-10 16:18:18,053 INFO     29 [Pipeline] Component [9]: Extractor:Discharge finished. error=None
2026-08-10 16:18:18,054 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Discharge | outputs={"chunks": "1 items, types={'DischargeRecord': 1}", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:18:18,054 INFO     29 [Pipeline] Executing component [10]: Extractor:Admission (type=Extractor)
2026-08-10 16:18:18,054 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:18:18.054+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:18:18,061 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:18,061 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗入院记录结构化提取专家。从入院记录/住院病历中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## AdmissionRecord Schema\n\n{\n  \"encounter_date\": \"<string|null, 入院日期 YYYY-MM-DD>\",\n  \"dm_name\": \"<string|null, 患者姓名>\",\n  \"dm_gender\": \"<string|null, 性别>\",\n  \"dm_age\": \"<integer|null, 年龄>\",\n  \"dm_ethnicity\": \"<string|null, 民族>\",\n  \"dm_marital_status\": \"<string|null, 婚况>\",\n  \"dm_occupation\": \"<string|null, 职业>\",\n  \"dm_admission_time\": \"<string|null, 入院时间 YYYY-MM-DD HH:MM>\",\n  \"dm_record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"dm_history_provider\": \"<string|null, 病史陈述者>\",\n  \"cc_text\": \"<string|null, 主诉原文>\",\n  \"cc_main_symptoms\": [\"<string, 主要症状>\"],\n  \"cc_duration\": \"<string|null, 病程时长描述>\",\n  \"pi_text\": \"<string|null, 现病史完整文本，保留用药史、检查结果>\",\n  \"pmh_disease_history\": [\"<string, 既往疾病>\"],\n  \"pmh_allergy_history\": [\"<string, 过敏药物/食物>\"],\n  \"pmh_surgery_trauma_history\": [\"<string, 手术外伤史>\"],\n  \"ph_smoking\": \"<string|null, 吸烟情况>\",\n  \"ph_drinking\": \"<string|null, 饮酒情况>\",\n  \"oh_menarche_age\": \"<integer|null, 初潮年龄>\",\n  \"oh_menopause_age\": \"<integer|null, 闭经年龄>\",\n  \"oh_pregnancies\": \"<string|null, 孕产情况 如G2P1，育有1子>\",\n  \"fh_text\": \"<string|null, 家族史文本>\",\n  \"fh_hereditary_diseases\": [\"<string, 遗传倾向疾病>\"],\n  \"vs_temperature_c\": \"<number|null, 体温 ℃>\",\n  \"vs_pulse_bpm\": \"<integer|null, 脉搏 次/分>\",\n  \"vs_respiration_rpm\": \"<integer|null, 呼吸 次/分>\",\n  \"vs_systolic_bp_mmhg\": \"<integer|null, 收缩压 mmHg>\",\n  \"vs_diastolic_bp_mmhg\": \"<integer|null, 舒张压 mmHg>\",\n  \"pe_general_condition\": \"<string|null, 一般情况>\",\n  \"pe_skin_mucosa\": \"<string|null, 皮肤粘膜>\",\n  \"pe_lymph_nodes\": \"<string|null, 浅表淋巴结>\",\n  \"pe_lungs\": \"<string|null, 肺部检查>\",\n  \"pe_heart\": \"<string|null, 心脏检查>\",\n  \"pe_abdomen\": \"<string|null, 腹部检查>\",\n  \"pe_extremities\": \"<string|null, 四肢>\",\n  \"pe_nervous_system\": \"<string|null, 神经系统>\",\n  \"pe_specialist_exam\": \"<string|null, 专科检查>\",\n  \"pe_ecog_score\": \"<integer|null, ECOG评分 0-4>\",\n  \"pat_text\": \"<string|null, 辅助检查结果摘要>\",\n  \"pat_items\": [\"<string, 检查项目及结果>\"],\n  \"preliminary_diagnoses\": [{\"name\": \"<诊断名>\", \"diagnosis_type\": \"<中医/西医/初步|null>\", \"is_primary\": \"<boolean>\"}],\n  \"department\": \"<string|null, 科室>\"\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null\n3. 体格检查数值必须原样保留\n4. 诊断列表区分中医/西医，标注是否主诊断\n5. 现病史要完整保留，包括外院诊治经过\n6. 既往史、过敏史逐条提取，不要合并\n7. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:18:19,391 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:19,404 INFO     29 [Pipeline] Component [10]: Extractor:Admission finished. error=None
2026-08-10 16:18:19,404 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Admission | outputs={"chunks": "1 items", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:18:19,404 INFO     29 [Pipeline] Executing component [11]: Extractor:ExaminationReport (type=Extractor)
2026-08-10 16:18:19,413 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:18:19,414 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:18:19,414 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:18:19,414 INFO     29 [qwen-vl-text] positions(23): [[4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0], [4, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:18:19,414 INFO     29 [qwen-vl-text] page grouping: [4], lines per page: [23]
2026-08-10 16:18:19,580 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:18:19,581 INFO     29 [qwen-vl-text] LLM extraction start, text_len=314
2026-08-10 16:18:19,581 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:19,581 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 115, \"bbox_end\": 137, \"encounter_dates\": [\"2025-05-23\", \"2025-05-26\"], \"department\": \"胸外二科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "河北省人民医院\n病理检查报告单\n病理号\n姓名:\n性别:女\n年龄:74岁\n送检单位:本院\n科别:胸外二科病区\n住院号\n床号:\n送检日期:2025-05-23 16:44\n送检材料:左肺穿刺数条:\n临床诊断:左肺占位\n图像:\n大体检查:\n(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。\n病理诊断:\n(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。\n诊断医师:\n郑国卿王彤彤\n日期:2025-05-26 14:23\n注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183\n2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。",
    "role": "user"
  }
]
2026-08-10 16:18:21,438 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:21,439 INFO     29 [qwen-vl-text] LLM output (len=386):
{
  "exam_date": "2025-05-23",
  "report_date": "2025-05-26",
  "exam_name": "病理检查",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外二科病区",
  "bed_number": null,
  "findings": "大体检查:\n(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。",
  "conclusion": "病理诊断:\n(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。",
  "physician": "郑国卿王彤彤",
  "reviewer": null
}
2026-08-10 16:18:21,443 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1228635, prompt_len=996
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共23行）
["河北省人民医院", "病理检查报告单", "病理号", "姓名:", "性别:女", "年龄:74岁", "送检单位:本院", "科别:胸外二科病区", "住院号", "床号:", "送检日期:2025-05-23 16:44", "送检材料:左肺穿刺数条:", "临床诊断:左肺占位", "图像:", "大体检查:", "(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。", "病理诊断:", "(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。", "诊断医师:", "郑国卿王彤彤", "日期:2025-05-26 14:23", "注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183", "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。"]

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
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord API raw response (len=1329):
[
	{"text": "河北省人民医院", "bbox": [431, 113, 554, 131]},
	{"text": "病理检查报告单", "bbox": [435, 147, 548, 169]},
	{"text": "病理号", "bbox": [326, 189, 350, 201]},
	{"text": "姓名:", "bbox": [326, 211, 346, 223]},
	{"text": "性别:女", "bbox": [427, 211, 460, 223]},
	{"text": "年龄:74岁", "bbox": [505, 211, 545, 223]},
	{"text": "送检单位:本院", "bbox": [561, 211, 618, 223]},
	{"text": "科别:胸外二科病区", "bbox": [326, 233, 398, 245]},
	{"text": "住院号", "bbox": [427, 233, 451, 245]},
	{"text": "床号:", "bbox": [505, 233, 524, 245]},
	{"text": "送检日期:2025-05-23 16:44", "bbox": [561, 233, 668, 245]},
	{"text": "送检材料:左肺穿刺数条:", "bbox": [326, 254, 419, 267]},
	{"text": "临床诊断:左肺占位", "bbox": [505, 254, 578, 267]},
	{"text": "图像:", "bbox": [326, 280, 346, 292]},
	{"text": "大体检查:", "bbox": [326, 465, 361, 477]},
	{"text": "(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。", "bbox": [329, 485, 555, 499]},
	{"text": "病理诊断:", "bbox": [326, 528, 364, 541]},
	{"text": "(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。", "bbox": [329, 549, 545, 563]},
	{"text": "诊断医师:", "bbox": [323, 805, 359, 817]},
	{"text": "郑国卿王彤彤", "bbox": [371, 785, 459, 817]},
	{"text": "日期:2025-05-26 14:23", "bbox": [578, 805, 670, 819]},
	{"text": "注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183", "bbox": [322, 827, 592, 839]},
	{"text": "2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。", "bbox": [330, 838, 640, 850]}
]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord API: raw_items=23, valid_items=23, elapsed=9.5s
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[0]: text=河北省人民医院, bbox=[431, 113, 554, 131]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[1]: text=病理检查报告单, bbox=[435, 147, 548, 169]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[2]: text=病理号, bbox=[326, 189, 350, 201]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[326, 211, 346, 223]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[4]: text=性别:女, bbox=[427, 211, 460, 223]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[5]: text=年龄:74岁, bbox=[505, 211, 545, 223]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[6]: text=送检单位:本院, bbox=[561, 211, 618, 223]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[7]: text=科别:胸外二科病区, bbox=[326, 233, 398, 245]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[8]: text=住院号, bbox=[427, 233, 451, 245]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[9]: text=床号:, bbox=[505, 233, 524, 245]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[10]: text=送检日期:2025-05-23 16:44, bbox=[561, 233, 668, 245]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[11]: text=送检材料:左肺穿刺数条:, bbox=[326, 254, 419, 267]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[12]: text=临床诊断:左肺占位, bbox=[505, 254, 578, 267]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[13]: text=图像:, bbox=[326, 280, 346, 292]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[14]: text=大体检查:, bbox=[326, 465, 361, 477]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[15]: text=(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。, bbox=[329, 485, 555, 499]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[16]: text=病理诊断:, bbox=[326, 528, 364, 541]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[17]: text=(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。, bbox=[329, 549, 545, 563]
2026-08-10 16:18:30,945 INFO     29 [qwen-vl-text] coord item[18]: text=诊断医师:, bbox=[323, 805, 359, 817]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] coord item[19]: text=郑国卿王彤彤, bbox=[371, 785, 459, 817]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] coord item[20]: text=日期:2025-05-26 14:23, bbox=[578, 805, 670, 819]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] coord item[21]: text=注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183, bbox=[322, 827, 592, 839]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] coord item[22]: text=2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。, bbox=[330, 838, 640, 850]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] page=4 — 23/23 coords, api_time=9.5s
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] new_positions (23):
[[4, 362.8545963134766, 466.4070681152344, 67.26618811035156, 77.9811561279297], [4, 366.2221563720703, 461.35572802734373, 87.50557214355469, 100.60164416503906], [4, 274.4561447753906, 294.6615051269531, 112.50716418457031, 119.65047619628906], [4, 274.4561447753906, 291.2939450683594, 125.60323620605469, 132.74654821777344], [4, 359.4870362548828, 387.26940673828125, 125.60323620605469, 132.74654821777344], [4, 425.15445739746093, 458.83005798339843, 125.60323620605469, 132.74654821777344], [4, 472.30029821777345, 520.2880290527344, 125.60323620605469, 132.74654821777344], [4, 274.4561447753906, 335.07222583007814, 138.69930822753906, 145.84262023925783], [4, 359.4870362548828, 379.6923966064453, 138.69930822753906, 145.84262023925783], [4, 425.15445739746093, 441.15036767578124, 138.69930822753906, 145.84262023925783], [4, 472.30029821777345, 562.3825297851563, 138.69930822753906, 145.84262023925783], [4, 274.4561447753906, 352.75191613769533, 151.20010424804687, 158.9386922607422], [4, 425.15445739746093, 486.61242846679687, 151.20010424804687, 158.9386922607422], [4, 274.4561447753906, 291.2939450683594, 166.6772802734375, 173.82059228515627], [4, 274.4561447753906, 303.92229528808593, 276.8033404541016, 283.9466524658203], [4, 276.9818148193359, 467.2489581298828, 288.7088604736328, 297.0427244873047], [4, 274.4561447753906, 306.44796533203123, 314.305728515625, 322.04431652832034], [4, 276.9818148193359, 458.83005798339843, 326.8065245361328, 335.1403885498047], [4, 271.9304747314453, 302.23851525878905, 479.19718078613283, 486.3404927978516], [4, 312.3411954345703, 386.42751672363283, 467.2916607666016, 486.3404927978516], [4, 486.61242846679687, 564.0663098144531, 479.19718078613283, 487.5310447998047], [4, 271.08858471679684, 498.398888671875, 492.2932528076172, 499.43656481933596], [4, 277.8237048339844, 538.809609375, 498.8412888183594, 505.98460083007814]]
2026-08-10 16:18:30,946 INFO     29 [qwen-vl-text] ═══ DONE ═══ 23 positions, pages=1, time=11.5s
2026-08-10 16:18:30,946 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:18:30,947 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:18:30,947 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:18:30,947 INFO     29 [qwen-vl-text] positions(21): [[4, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0], [5, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:18:30,947 INFO     29 [qwen-vl-text] page grouping: [4, 5], lines per page: [1, 20]
2026-08-10 16:18:31,105 INFO     29 [qwen-vl-text] page=4, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:18:31,316 INFO     29 [qwen-vl-text] page=5, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:18:31,317 INFO     29 [qwen-vl-text] LLM extraction start, text_len=382
2026-08-10 16:18:31,317 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:31,317 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 138, \"bbox_end\": 158, \"encounter_dates\": [\"2025-05-23\", \"2025-05-27\"], \"department\": \"胸外二科病区\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "住院病历\n河北省人民医院\n病理检查补充报告单\n病理号:\n姓名:\n性别: 女\n年龄: 74岁\n送检单位: 本院\n科别: 胸外二科病区\n住院号:\n床号:\n送检日期: 2025-05-23 16:44\n送检材料: 左肺穿刺数条:\n临床诊断: 左肺占位\n补充病理诊断:\n(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。\n免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6\n(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。\n诊断医师: 康林 郑国娜\n报告日期: 2025-05-27 16:\n注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)",
    "role": "user"
  }
]
2026-08-10 16:18:34,044 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:34,044 INFO     29 [qwen-vl-text] LLM output (len=508):
{
  "exam_date": "2025-05-23",
  "report_date": "2025-05-27",
  "exam_name": "病理检查补充报告单",
  "exam_category": "pathology",
  "body_part": "左肺",
  "patient_name": null,
  "patient_gender": "女",
  "department": "胸外二科病区",
  "bed_number": null,
  "findings": "送检材料: 左肺穿刺数条:",
  "conclusion": "补充病理诊断:\n(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。\n免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6 (-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。",
  "physician": "康林 郑国娜",
  "reviewer": null
}
2026-08-10 16:18:34,046 INFO     29 [qwen-vl-text] coord API call start, page=4, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1228635, prompt_len=619
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共1行）
["住院病历"]

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
2026-08-10 16:18:34,775 INFO     29 [qwen-vl-text] coord API raw response (len=63):
```json
[
	{"text": "住院病历", "bbox": [547, 839, 584, 855]}
]
```
2026-08-10 16:18:34,775 INFO     29 [qwen-vl-text] coord API: raw_items=1, valid_items=1, elapsed=0.7s
2026-08-10 16:18:34,775 INFO     29 [qwen-vl-text] coord item[0]: text=住院病历, bbox=[547, 839, 584, 855]
2026-08-10 16:18:34,775 INFO     29 [qwen-vl-text] page=4 — 1/1 coords, api_time=0.7s
2026-08-10 16:18:34,777 INFO     29 [qwen-vl-text] coord API call start, page=5, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=1426754, prompt_len=1050
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共20行）
["河北省人民医院", "病理检查补充报告单", "病理号:", "姓名:", "性别: 女", "年龄: 74岁", "送检单位: 本院", "科别: 胸外二科病区", "住院号:", "床号:", "送检日期: 2025-05-23 16:44", "送检材料: 左肺穿刺数条:", "临床诊断: 左肺占位", "补充病理诊断:", "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "诊断医师: 康林 郑国娜", "报告日期: 2025-05-27 16:", "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)"]

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
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord API raw response (len=1260):
[
	{"text": "河北省人民医院", "bbox": [421, 152, 552, 171]},
	{"text": "病理检查补充报告单", "bbox": [410, 196, 564, 220]},
	{"text": "病理号:", "bbox": [311, 250, 341, 263]},
	{"text": "姓名:", "bbox": [311, 274, 333, 287]},
	{"text": "性别: 女", "bbox": [412, 273, 453, 287]},
	{"text": "年龄: 74岁", "bbox": [496, 273, 544, 287]},
	{"text": "送检单位: 本院", "bbox": [561, 273, 623, 287]},
	{"text": "科别: 胸外二科病区", "bbox": [311, 296, 393, 309]},
	{"text": "住院号:", "bbox": [412, 296, 443, 309]},
	{"text": "床号:", "bbox": [496, 296, 517, 309]},
	{"text": "送检日期: 2025-05-23 16:44", "bbox": [561, 296, 674, 309]},
	{"text": "送检材料: 左肺穿刺数条:", "bbox": [311, 319, 412, 332]},
	{"text": "临床诊断: 左肺占位", "bbox": [496, 319, 575, 332]},
	{"text": "补充病理诊断:", "bbox": [311, 353, 385, 369]},
	{"text": "(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。", "bbox": [315, 373, 513, 386]},
	{"text": "免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6", "bbox": [312, 387, 661, 400]},
	{"text": "(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。", "bbox": [315, 400, 618, 413]},
	{"text": "诊断医师: 康林 郑国娜", "bbox": [317, 790, 455, 818]},
	{"text": "报告日期: 2025-05-27 16:", "bbox": [545, 798, 663, 812]},
	{"text": "注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)", "bbox": [318, 828, 640, 840]}
]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord API: raw_items=20, valid_items=20, elapsed=7.9s
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[0]: text=河北省人民医院, bbox=[421, 152, 552, 171]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[1]: text=病理检查补充报告单, bbox=[410, 196, 564, 220]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[2]: text=病理号:, bbox=[311, 250, 341, 263]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[3]: text=姓名:, bbox=[311, 274, 333, 287]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[4]: text=性别: 女, bbox=[412, 273, 453, 287]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[5]: text=年龄: 74岁, bbox=[496, 273, 544, 287]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[6]: text=送检单位: 本院, bbox=[561, 273, 623, 287]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[7]: text=科别: 胸外二科病区, bbox=[311, 296, 393, 309]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[8]: text=住院号:, bbox=[412, 296, 443, 309]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[9]: text=床号:, bbox=[496, 296, 517, 309]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[10]: text=送检日期: 2025-05-23 16:44, bbox=[561, 296, 674, 309]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[11]: text=送检材料: 左肺穿刺数条:, bbox=[311, 319, 412, 332]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[12]: text=临床诊断: 左肺占位, bbox=[496, 319, 575, 332]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[13]: text=补充病理诊断:, bbox=[311, 353, 385, 369]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[14]: text=(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。, bbox=[315, 373, 513, 386]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[15]: text=免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6, bbox=[312, 387, 661, 400]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[16]: text=(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。, bbox=[315, 400, 618, 413]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[17]: text=诊断医师: 康林 郑国娜, bbox=[317, 790, 455, 818]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[18]: text=报告日期: 2025-05-27 16:, bbox=[545, 798, 663, 812]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] coord item[19]: text=注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409), bbox=[318, 828, 640, 840]
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] page=5 — 20/20 coords, api_time=7.9s
2026-08-10 16:18:42,692 INFO     29 [qwen-vl-text] new_positions (21):
[[4, 460.5138380126953, 491.6637685546875, 499.43656481933596, 508.96098083496094], [5, 354.43569616699216, 464.7232880859375, 90.4819521484375, 101.7921961669922], [5, 345.1749060058594, 474.82596826171874, 116.67409619140625, 130.96072021484375], [5, 261.82779455566407, 287.0844949951172, 148.81900024414062, 156.55758825683594], [5, 261.82779455566407, 280.3493748779297, 163.10562426757812, 170.84421228027344], [5, 346.85868603515627, 381.3761766357422, 162.51034826660157, 170.84421228027344], [5, 417.577447265625, 457.98816796875, 162.51034826660157, 170.84421228027344], [5, 472.30029821777345, 524.4974791259766, 162.51034826660157, 170.84421228027344], [5, 261.82779455566407, 330.86277575683596, 176.2016962890625, 183.94028430175783], [5, 346.85868603515627, 372.9572764892578, 176.2016962890625, 183.94028430175783], [5, 417.577447265625, 435.2571375732422, 176.2016962890625, 183.94028430175783], [5, 472.30029821777345, 567.4338698730469, 176.2016962890625, 183.94028430175783], [5, 261.82779455566407, 346.85868603515627, 189.89304431152345, 197.63163232421877], [5, 417.577447265625, 484.0867584228516, 189.89304431152345, 197.63163232421877], [5, 261.82779455566407, 324.1276556396484, 210.13242834472658, 219.65684436035158], [5, 265.19535461425784, 431.8895775146484, 222.03794836425783, 229.77653637695315], [5, 262.6696845703125, 556.4892996826172, 230.3718123779297, 238.11040039062502], [5, 265.19535461425784, 520.2880290527344, 238.11040039062502, 245.84898840332033], [5, 266.87913464355466, 383.05995666503907, 470.2680407714844, 486.9357687988281], [5, 458.83005798339843, 558.173079711914, 475.03024877929687, 483.3641127929688], [5, 267.72102465820313, 538.809609375, 492.8885288085938, 500.03184082031254]]
2026-08-10 16:18:42,693 INFO     29 [qwen-vl-text] ═══ DONE ═══ 21 positions, pages=2, time=11.7s
2026-08-10 16:18:42,693 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:18:42,693 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:18:42,693 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:18:42,694 INFO     29 [qwen-vl-text] positions(48): [[6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0], [6, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:18:42,694 INFO     29 [qwen-vl-text] page grouping: [6], lines per page: [48]
2026-08-10 16:18:42,817 INFO     29 [qwen-vl-text] page=6, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:18:42,818 INFO     29 [qwen-vl-text] LLM extraction start, text_len=949
2026-08-10 16:18:42,818 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:42,818 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 162, \"bbox_end\": 209, \"encounter_dates\": [\"2026-03-11\"], \"department\": \"(江北)综合肿瘤中心\", \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "南京鼓楼医院云胶片\n南京鼓楼医院\n南京大学医学院附属鼓楼医院\n影像检查诊断报告\n互联网医院\n电子影像\n检查号:\n患者类型: 住院\n患者编号:\n姓名:\n性别: 女\n年龄: 75岁\n科别: (江北)综合肿瘤中心 病区: (江北)B7病区\n病床:\n检查日期: 2026-03-11 13:39:06\n设备类型: CT\n技师: 王雨晓\n检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]\n检查所见:\n颈部软组织CT平扫+增强:\n【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强:\n【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n肺上叶局部透亮区。\n【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n上腹部、下腹部、盆腔CT平扫+增强:\n报告日期: 2026-03-11 15:35:37\n诊断医师: 申欣怡\n/ 申欣怡\n审核日期: 2026-03-12 13:17:06\n审核医师: 王国\n（本报告仅供临床医生参考）",
    "role": "user"
  }
]
2026-08-10 16:18:48,391 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:18:48,391 INFO     29 [qwen-vl-text] LLM output (len=1030):
{
  "exam_date": "2026-03-11",
  "report_date": "2026-03-11",
  "exam_name": "CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)",
  "exam_category": "imaging",
  "body_part": "颈部、胸部、上腹部、下腹部、盆腔",
  "patient_name": null,
  "patient_gender": "女",
  "department": "(江北)综合肿瘤中心",
  "bed_number": null,
  "findings": "颈部软组织CT平扫+增强:\n【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见\n明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区\n未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】两侧锁骨上窝多发肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强:\n【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺\n多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右\n肺上叶局部透亮区。\n【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。\n【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。\n【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。\n【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。\n上腹部、下腹部、盆腔CT平扫+增强:",
  "conclusion": null,
  "physician": "申欣怡",
  "reviewer": "王国"
}
2026-08-10 16:18:48,392 INFO     29 [qwen-vl-text] coord API call start, page=6, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=938136, prompt_len=1706
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共48行）
["南京鼓楼医院云胶片", "南京鼓楼医院", "南京大学医学院附属鼓楼医院", "影像检查诊断报告", "互联网医院", "电子影像", "检查号:", "患者类型: 住院", "患者编号:", "姓名:", "性别: 女", "年龄: 75岁", "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "病床:", "检查日期: 2026-03-11 13:39:06", "设备类型: CT", "技师: 王雨晓", "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "检查所见:", "颈部软组织CT平扫+增强:", "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "明显异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "未见明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强:", "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "肺上叶局部透亮区。", "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "上腹部、下腹部、盆腔CT平扫+增强:", "报告日期: 2026-03-11 15:35:37", "诊断医师: 申欣怡", "/ 申欣怡", "审核日期: 2026-03-12 13:17:06", "审核医师: 王国", "（本报告仅供临床医生参考）"]

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
2026-08-10 16:19:13,971 INFO     29 [qwen-vl-text] coord API raw response (len=4474):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [424, 134, 572, 158]},
	{"text": "南京鼓楼医院", "bbox": [460, 224, 551, 240], "bbox": [460, 224, 551, 240]},
	{"text": "南京大学医学院附属鼓楼医院", "bbox": [435, 240, 572, 255], "bbox": [435, 240, 572, 255]},
	{"text": "影像检查诊断报告", "bbox": [445, 255, 562, 275], "bbox": [445, 255, 562, 275]},
	{"text": "互联网医院", "bbox": [334, 300, 367, 309], "bbox": [334, 300, 367, 309]},
	{"text": "电子影像", "bbox": [623, 300, 650, 309], "bbox": [623, 300, 650, 309]},
	{"text": "检查号:", "bbox": [317, 327, 353, 340], "bbox": [317, 327, 353, 340]},
	{"text": "患者类型: 住院", "bbox": [445, 327, 505, 340], "bbox": [445, 327, 505, 340]},
	{"text": "患者编号:", "bbox": [549, 327, 584, 340], "bbox": [549, 327, 584, 340]},
	{"text": "姓名:", "bbox": [317, 349, 353, 362], "bbox": [317, 349, 353, 362]},
	{"text": "性别: 女", "bbox": [445, 349, 497, 362], "bbox": [445, 349, 497, 362]},
	{"text": "年龄: 75岁", "bbox": [549, 349, 610, 362], "bbox": [549, 349, 610, 362]},
	{"text": "科别: (江北)综合肿瘤中心 病区: (江北)B7病区", "bbox": [317, 368, 536, 381], "bbox": [317, 368, 536, 381]},
	{"text": "病床:", "bbox": [549, 368, 584, 381], "bbox": [549, 368, 584, 381]},
	{"text": "检查日期: 2026-03-11 13:39:06", "bbox": [317, 387, 438, 399], "bbox": [317, 387, 438, 399]},
	{"text": "设备类型: CT", "bbox": [317, 406, 370, 418], "bbox": [317, 406, 370, 418]},
	{"text": "技师: 王雨晓", "bbox": [549, 406, 614, 418], "bbox": [549, 406, 614, 418]},
	{"text": "检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]", "bbox": [317, 425, 555, 437], "bbox": [317, 425, 555, 437]},
	{"text": "检查所见:", "bbox": [317, 443, 353, 456], "bbox": [317, 443, 353, 456]},
	{"text": "颈部软组织CT平扫+增强:", "bbox": [317, 460, 405, 472], "bbox": [317, 460, 405, 472]},
	{"text": "【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。", "bbox": [337, 477, 624, 489], "bbox": [337, 477, 624, 489]},
	{"text": "【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见", "bbox": [337, 494, 661, 506], "bbox": [337, 494, 661, 506]},
	{"text": "明显异常强化。", "bbox": [317, 511, 370, 523], "bbox": [317, 511, 370, 523]},
	{"text": "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区", "bbox": [337, 528, 661, 540], "bbox": [337, 528, 661, 540]},
	{"text": "未见明显占位性病变。", "bbox": [317, 545, 394, 557], "bbox": [317, 545, 394, 557]},
	{"text": "【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。", "bbox": [337, 562, 616, 574], "bbox": [337, 562, 616, 574]},
	{"text": "【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。", "bbox": [337, 579, 568, 591], "bbox": [337, 579, 568, 591]},
	{"text": "【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。", "bbox": [337, 596, 608, 608], "bbox": [337, 596, 608, 608]},
	{"text": "【淋巴结】两侧锁骨上窝多发肿大淋巴结。", "bbox": [337, 613, 481, 625], "bbox": [337, 613, 481, 625]},
	{"text": "【其他】副鼻窦内低密度影。", "bbox": [337, 630, 433, 642], "bbox": [337, 630, 433, 642]},
	{"text": "胸部CT平扫+增强:", "bbox": [317, 647, 381, 659], "bbox": [317, 647, 381, 659]},
	{"text": "【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺", "bbox": [337, 664, 661, 676], "bbox": [337, 664, 661, 676]},
	{"text": "多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右", "bbox": [317, 681, 665, 693], "bbox": [317, 681, 665, 693]},
	{"text": "肺上叶局部透亮区。", "bbox": [317, 698, 387, 710], "bbox": [317, 698, 387, 710]},
	{"text": "【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。", "bbox": [337, 715, 616, 727], "bbox": [337, 715, 616, 727]},
	{"text": "【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。", "bbox": [337, 732, 576, 744], "bbox": [337, 732, 576, 744]},
	{"text": "【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。", "bbox": [337, 749, 560, 761], "bbox": [337, 749, 560, 761]},
	{"text": "【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。", "bbox": [337, 766, 550, 778], "bbox": [337, 766, 550, 778]},
	{"text": "【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。", "bbox": [337, 783, 632, 795], "bbox": [337, 783, 632, 795]},
	{"text": "【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。", "bbox": [337, 800, 554, 812], "bbox": [337, 800, 554, 812]},
	{"text": "【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。", "bbox": [337, 817, 568, 829], "bbox": [337, 817, 568, 829]},
	{"text": "上腹部、下腹部、盆腔CT平扫+增强:", "bbox": [317, 834, 445, 846], "bbox": [317, 834, 445, 846]},
	{"text": "报告日期: 2026-03-11 15:35:37", "bbox": [317, 858, 438, 870], "bbox": [317, 858, 438, 870]},
	{"text": "诊断医师: 申欣怡", "bbox": [465, 858, 534, 870], "bbox": [465, 858, 534, 870]},
	{"text": "/ 申欣怡", "bbox": [582, 858, 617, 870], "bbox": [582, 858, 617, 870]},
	{"text": "审核日期: 2026-03-12 13:17:06", "bbox": [317, 890, 438, 902], "bbox": [317, 890, 438, 902]},
	{"text": "审核医师: 王国", "bbox": [465, 889, 537, 905], "bbox": [465, 889, 537, 905]},
	{"text": "（本报告仅供临床医生参考）", "bbox": [377, 913, 450, 922], "bbox": [377, 913, 450, 922]}
]
2026-08-10 16:19:13,971 INFO     29 [qwen-vl-text] coord API: raw_items=48, valid_items=48, elapsed=25.6s
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[424, 134, 572, 158]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[1]: text=南京鼓楼医院, bbox=[460, 224, 551, 240]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[2]: text=南京大学医学院附属鼓楼医院, bbox=[435, 240, 572, 255]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[3]: text=影像检查诊断报告, bbox=[445, 255, 562, 275]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[4]: text=互联网医院, bbox=[334, 300, 367, 309]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[5]: text=电子影像, bbox=[623, 300, 650, 309]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[6]: text=检查号:, bbox=[317, 327, 353, 340]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[7]: text=患者类型: 住院, bbox=[445, 327, 505, 340]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[8]: text=患者编号:, bbox=[549, 327, 584, 340]
2026-08-10 16:19:13,972 INFO     29 [qwen-vl-text] coord item[9]: text=姓名:, bbox=[317, 349, 353, 362]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[10]: text=性别: 女, bbox=[445, 349, 497, 362]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[11]: text=年龄: 75岁, bbox=[549, 349, 610, 362]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[12]: text=科别: (江北)综合肿瘤中心 病区: (江北)B7病区, bbox=[317, 368, 536, 381]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[13]: text=病床:, bbox=[549, 368, 584, 381]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[14]: text=检查日期: 2026-03-11 13:39:06, bbox=[317, 387, 438, 399]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[15]: text=设备类型: CT, bbox=[317, 406, 370, 418]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[16]: text=技师: 王雨晓, bbox=[549, 406, 614, 418]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[17]: text=检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)], bbox=[317, 425, 555, 437]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[18]: text=检查所见:, bbox=[317, 443, 353, 456]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[19]: text=颈部软组织CT平扫+增强:, bbox=[317, 460, 405, 472]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[20]: text=【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。, bbox=[337, 477, 624, 489]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[21]: text=【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见, bbox=[337, 494, 661, 506]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[22]: text=明显异常强化。, bbox=[317, 511, 370, 523]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[23]: text=【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区, bbox=[337, 528, 661, 540]
2026-08-10 16:19:13,973 INFO     29 [qwen-vl-text] coord item[24]: text=未见明显占位性病变。, bbox=[317, 545, 394, 557]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[25]: text=【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。, bbox=[337, 562, 616, 574]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[26]: text=【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。, bbox=[337, 579, 568, 591]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[27]: text=【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。, bbox=[337, 596, 608, 608]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[28]: text=【淋巴结】两侧锁骨上窝多发肿大淋巴结。, bbox=[337, 613, 481, 625]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[29]: text=【其他】副鼻窦内低密度影。, bbox=[337, 630, 433, 642]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[30]: text=胸部CT平扫+增强:, bbox=[317, 647, 381, 659]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[31]: text=【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺, bbox=[337, 664, 661, 676]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[32]: text=多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右, bbox=[317, 681, 665, 693]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[33]: text=肺上叶局部透亮区。, bbox=[317, 698, 387, 710]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[34]: text=【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。, bbox=[337, 715, 616, 727]
2026-08-10 16:19:13,974 INFO     29 [qwen-vl-text] coord item[35]: text=【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。, bbox=[337, 732, 576, 744]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[36]: text=【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。, bbox=[337, 749, 560, 761]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[37]: text=【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。, bbox=[337, 766, 550, 778]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[38]: text=【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。, bbox=[337, 783, 632, 795]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[39]: text=【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。, bbox=[337, 800, 554, 812]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[40]: text=【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。, bbox=[337, 817, 568, 829]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[41]: text=上腹部、下腹部、盆腔CT平扫+增强:, bbox=[317, 834, 445, 846]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[42]: text=报告日期: 2026-03-11 15:35:37, bbox=[317, 858, 438, 870]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[43]: text=诊断医师: 申欣怡, bbox=[465, 858, 534, 870]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[44]: text=/ 申欣怡, bbox=[582, 858, 617, 870]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[45]: text=审核日期: 2026-03-12 13:17:06, bbox=[317, 890, 438, 902]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[46]: text=审核医师: 王国, bbox=[465, 889, 537, 905]
2026-08-10 16:19:13,975 INFO     29 [qwen-vl-text] coord item[47]: text=（本报告仅供临床医生参考）, bbox=[377, 913, 450, 922]
2026-08-10 16:19:13,976 INFO     29 [qwen-vl-text] page=6 — 48/48 coords, api_time=25.6s
2026-08-10 16:19:13,976 INFO     29 [qwen-vl-text] new_positions (48):
[[6, 356.9613662109375, 481.5610883789062, 79.76698413085938, 94.05360815429688], [6, 387.26940673828125, 463.8813980712891, 133.34182421875, 142.866240234375], [6, 366.2221563720703, 481.5610883789062, 142.866240234375, 151.79538024902345], [6, 374.6410565185547, 473.14218823242186, 151.79538024902345, 163.7009002685547], [6, 281.19126489257815, 308.9736353759766, 178.58280029296876, 183.94028430175783], [6, 524.4974791259766, 547.2285095214844, 178.58280029296876, 183.94028430175783], [6, 266.87913464355466, 297.18717517089846, 194.65525231933594, 202.39384033203126], [6, 374.6410565185547, 425.15445739746093, 194.65525231933594, 202.39384033203126], [6, 462.1976180419922, 491.6637685546875, 194.65525231933594, 202.39384033203126], [6, 266.87913464355466, 297.18717517089846, 207.75132434082033, 215.48991235351562], [6, 374.6410565185547, 418.41933728027345, 207.75132434082033, 215.48991235351562], [6, 462.1976180419922, 513.5529089355468, 207.75132434082033, 215.48991235351562], [6, 266.87913464355466, 451.2530478515625, 219.061568359375, 226.80015637207032], [6, 462.1976180419922, 491.6637685546875, 219.061568359375, 226.80015637207032], [6, 266.87913464355466, 368.74782641601564, 230.3718123779297, 237.51512438964843], [6, 266.87913464355466, 311.4993054199219, 241.6820563964844, 248.82536840820313], [6, 462.1976180419922, 516.9204689941406, 241.6820563964844, 248.82536840820313], [6, 266.87913464355466, 467.2489581298828, 252.99230041503907, 260.1356124267578], [6, 266.87913464355466, 297.18717517089846, 263.7072684326172, 271.44585644531253], [6, 266.87913464355466, 340.9654559326172, 273.82696044921875, 280.9702724609375], [6, 283.71693493652344, 525.339369140625, 283.9466524658203, 291.08996447753907], [6, 283.71693493652344, 556.4892996826172, 294.06634448242187, 301.20965649414063], [6, 266.87913464355466, 311.4993054199219, 304.18603649902343, 311.3293485107422], [6, 283.71693493652344, 556.4892996826172, 314.305728515625, 321.44904052734375], [6, 266.87913464355466, 331.7046657714844, 324.42542053222655, 331.5687325439453], [6, 283.71693493652344, 518.6042490234375, 334.5451125488281, 341.6884245605469], [6, 283.71693493652344, 478.1935283203125, 344.6648045654297, 351.80811657714844], [6, 283.71693493652344, 511.86912890625, 354.78449658203124, 361.92780859375], [6, 283.71693493652344, 404.94909704589844, 364.9041885986328, 372.04750061035156], [6, 283.71693493652344, 364.53837634277346, 375.0238806152344, 382.1671926269531], [6, 266.87913464355466, 320.76009558105466, 385.143572631836, 392.2868846435547], [6, 283.71693493652344, 556.4892996826172, 395.26326464843754, 402.40657666015625], [6, 266.87913464355466, 559.8568597412109, 405.3829566650391, 412.5262686767578], [6, 266.87913464355466, 325.8114356689453, 415.50264868164066, 422.64596069335937], [6, 283.71693493652344, 518.6042490234375, 425.6223406982422, 432.76565270996093], [6, 283.71693493652344, 484.9286484375, 435.7420327148438, 442.8853447265625], [6, 283.71693493652344, 471.458408203125, 445.86172473144535, 453.00503674316406], [6, 283.71693493652344, 463.0395080566406, 455.9814167480469, 463.1247287597656], [6, 283.71693493652344, 532.0744892578125, 466.1011087646485, 473.24442077636724], [6, 283.71693493652344, 466.4070681152344, 476.22080078125003, 483.3641127929688], [6, 283.71693493652344, 478.1935283203125, 486.3404927978516, 493.48380480957036], [6, 266.87913464355466, 374.6410565185547, 496.46018481445316, 503.6034968261719], [6, 266.87913464355466, 368.74782641601564, 510.7468088378906, 517.8901208496094], [6, 391.4788568115234, 449.5692678222656, 510.7468088378906, 517.8901208496094], [6, 489.97998852539064, 519.4461390380859, 510.7468088378906, 517.8901208496094], [6, 266.87913464355466, 368.74782641601564, 529.7956408691407, 536.9389528808593], [6, 391.4788568115234, 452.09493786621096, 529.2003648681641, 538.7247808837891], [6, 317.39253552246095, 378.8505065917969, 543.4869888916016, 548.8444729003907]]
2026-08-10 16:19:13,976 INFO     29 [qwen-vl-text] ═══ DONE ═══ 48 positions, pages=1, time=31.3s
2026-08-10 16:19:13,976 INFO     29 extractor ocr_parser=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, extractor_type=NONE, chunk_type=, chunk_id=
2026-08-10 16:19:13,978 INFO     29 [vl-ocr-endpoint] resolved from tenant_llm: tenant=d0a4dc3a1a2511f1aeb02a5fbb884ed3, llm_name=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8___OpenAI-API, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8
2026-08-10 16:19:13,979 INFO     29 [qwen-vl-text] ═══ START ═══ type=ExaminationReport, doc_id=None
2026-08-10 16:19:13,979 INFO     29 [qwen-vl-text] positions(122): [[7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [7, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [8, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [9, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0], [10, 0.0, 0.0, 0.0, 0.0]]
2026-08-10 16:19:13,979 INFO     29 [qwen-vl-text] page grouping: [7, 8, 9, 10], lines per page: [29, 31, 32, 30]
2026-08-10 16:19:14,092 INFO     29 [qwen-vl-text] page=7, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:19:14,209 INFO     29 [qwen-vl-text] page=8, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:19:14,322 INFO     29 [qwen-vl-text] page=9, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:19:14,436 INFO     29 [qwen-vl-text] page=10, rect=842x595, img=(2339x1654), dpi=200
2026-08-10 16:19:14,437 INFO     29 [qwen-vl-text] LLM extraction start, text_len=2015
2026-08-10 16:19:14,437 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:19:14,437 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗检查报告结构化提取专家。根据文档分类结果和原文内容，提取结构化临床数据。\n\n## 上游分类结果\n{\"type\": \"ExaminationReport\", \"bbox_start\": 211, \"bbox_end\": 332, \"encounter_dates\": [\"2025-10-08\"], \"department\": null, \"record_count\": 1}\n\n## 输出格式\n\n严格输出纯 JSON，禁止使用 json 代码块包裹，禁止输出任何非 JSON 文字。\n\n## 提取 Schema（ExaminationReport — 三段式结构）\n\n{\n  \"exam_date\": \"<string|null, 检查日期 YYYY-MM-DD，从报告日期/检查日期/送检日期提取>\",\n  \"report_date\": \"<string|null, 报告出具日期 YYYY-MM-DD>\",\n  \"exam_name\": \"<string|null, 检查名称，如：胸部CT平扫+增强、病理检查、心电图>\",\n  \"exam_category\": \"<string, imaging|pathology|other>\",\n  \"body_part\": \"<string|null, 检查部位或送检标本部位>\",\n  \"patient_name\": \"<string|null, 患者姓名>\",\n  \"patient_gender\": \"<string|null, 性别>\",\n  \"department\": \"<string|null, 科室/病区/申请科室/送检科室>\",\n  \"bed_number\": \"<string|null, 床号>\",\n  \"findings\": \"<string|null, 检查所见完整原文，保留段落标题>\",\n  \"conclusion\": \"<string|null, 检查结论完整原文>\",\n  \"physician\": \"<string|null, 报告医师/病理医师>\",\n  \"reviewer\": \"<string|null, 审核医师>\"\n}\n\n## exam_category 分类指南\n- imaging：CT/MRI/X光/超声/PET-CT/骨扫描/钼靶/DSA/影像检查\n- pathology：病理检查报告单/活检/手术病理/免疫组化/分子检测\n- other：心电图/动态监测/内镜/肺功能/其他辅助检查\n\n## 关键约束\n1. 所有提取字段的值必须来源于原文，禁止编造原文中不存在的信息\n2. 原文中不存在的字段填 null，不要猜测\n3. findings 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n4. conclusion 必须保留完整原文，不做摘要或缩写，并且将原文包含的html表格提取成markdown形式的内容\n5. 病理报告的\"大体检查\"属于findings，镜下所见不属于findings，保留段落标题\n6. 病理报告的免疫组化结果合并存入 conclusion 末尾\n7. 日期统一输出 YYYY-MM-DD 格式\n8. OCR 扫描件可能有识别错误，遇到明显 OCR 错字可纠正"
  },
  {
    "content": "南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n报告 2025-10-08\n影像描述\n颈部软组织CT平扫+增强：\n【所见咽部】所见咽腔结构对称，未见明显异常\n密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称，会厌、声带、\n梨状窝形态及密度未见明显异常。增强后未见明显\n异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形\n态正常，甲状腺双叶低密度结节；甲状旁腺区未见\n明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显\n异常。增强后未见明显异常强化。\n【气管及食管】气管居中，管腔通畅；食管颈段\n管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰，未见明显异常密度\n影。增强后未见明显异常强化。\n【淋巴结】未见明显肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强：\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高\n密度影。两肺多发结节，较大者：右肺上叶（Img7\n9）见一实性结节影，大小约5mm×3mm。两肺索\n条及片絮影；右肺上叶局部透亮区。\n【肺门】双肺门多发小淋巴结，部分稍大。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎\n症，病灶周围结节影。\n【纵隔】纵隔居中，纵隔内多发小淋巴结，部分\n稍大，较大者短径约10mm。\n【心脏及大血管】心影增大；主动脉及冠状动\n脉壁见致密影。\n【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔\n积液：否。增强后未见明显异常强化。\n【膈肌】光整，未见明显异常抬高。增强后未见\n明显异常强化。\n【胸壁】胸廓对称，骨质未见明显异常。增强后\n未见明显异常强化。\n上腹部CT平扫+增强：\n【肝脏】各叶比例在正常范围内，外形轮廓规\n则，肝内小圆形无强化低密度影，较大者长径约6\nmm。静脉期肝左叶小片状稍低密度影（薄层im29\n0）。\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见\n增厚，囊内未见明显异常密度影；肝内外胆管轻度\n扩张。\n【胰腺】形态、大小正常，实质内未见明显异常\n密度影；胰管未见明显扩张。增强后未见明显异常\n强化。\n【脾脏】形态、大小正常，实质内未见明显异常\n密度影。增强后未见明显异常强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n匀，未见明显肿大淋巴结，未见明显渗出及积液。\n增强后未见明显异常强化。\n下腹部CT平扫+增强：\n【肾脏】两侧肾脏大小、形态、位置正常，右肾\n窦点状致密影；肾盂肾盏未见明显扩张。增强后未\n见明显异常强化。\n【肾上腺】双肾上腺增粗，左肾上腺低密度结\n节，长径约12mm,可见强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均\n匀，未见明显肿大淋巴结，未见明显渗出及积液。\n增强后未见明显异常强化。\n盆腔CT平扫+增强：\n【膀胱】充盈欠佳，壁未见明显增厚，其内未见\n明显异常密度影。增强后未见明显异常强化。\n【子宫及附件】子宫呈肌组织结构性空扫\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0\n南京鼓楼医院云胶片\n女/75岁\n设备类型 CT 患者类型 无\n检查项目 [CT平扫+增强（颈部、胸部、上腹部、下\n腹部、盆腔）]\nPDF报告 图像 分享\n诊断意见\n1.肺癌复查：左肺下叶斑片影较前（2025-07-15）\n明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前\n缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋\n巴结，部分较前稍缩小。\n2.两肺多发结节，较前变化不大，密切随诊。\n3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓\n解；右肺上叶局限性肺气肿。\n4.心影增大；主动脉及冠状动脉壁钙化。\n5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影\n（薄层im290），较前相仿，随诊。\n6.肝内外胆管轻度扩张。\n7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检\n查；右肾小结石。\n8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结\n节。\n9.下腹腔内肠系膜间隙多发稍大淋巴结。\n10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠\n内容物多；十二指肠降部憩室；结合临床体征随\n诊。\n11.右肩部皮下低密度结节，较前相仿，随诊；L4及\n以上椎体I°滑脱。\n移动影像浏览\n© 2022 南京鼓楼医院影像云平台 V1.0",
    "role": "user"
  }
]
2026-08-10 16:19:14,439 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:19:14.439+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:19:24,719 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:19:24,719 INFO     29 [qwen-vl-text] LLM output (len=1854):
{
  "exam_date": "2025-10-08",
  "report_date": "2025-10-08",
  "exam_name": "CT平扫+增强（颈部、胸部、上腹部、下腹部、盆腔）",
  "exam_category": "imaging",
  "body_part": "颈部、胸部、上腹部、下腹部、盆腔",
  "patient_name": null,
  "patient_gender": "女",
  "department": null,
  "bed_number": null,
  "findings": "颈部软组织CT平扫+增强：\n【所见咽部】所见咽腔结构对称，未见明显异常密度影。增强后未见明显异常强化。\n【喉部及下咽部】喉腔结构对称，会厌、声带、梨状窝形态及密度未见明显异常。增强后未见明显异常强化。\n【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常，甲状腺双叶低密度结节；甲状旁腺区未见明显占位性病变。\n【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。\n【气管及食管】气管居中，管腔通畅；食管颈段管壁未见明显增厚。\n【颈部间隙】脂肪间隙清晰，未见明显异常密度影。增强后未见明显异常强化。\n【淋巴结】未见明显肿大淋巴结。\n【其他】副鼻窦内低密度影。\n胸部CT平扫+增强：\n【肺野】两肺野纹理清晰，左肺下叶见斑片状高密度影。两肺多发结节，较大者：右肺上叶（Img79）见一实性结节影，大小约5mm×3mm。两肺索条及片絮影；右肺上叶局部透亮区。\n【肺门】双肺门多发小淋巴结，部分稍大。\n【气管及支气管】左下肺支气管闭塞伴阻塞性炎症，病灶周围结节影。\n【纵隔】纵隔居中，纵隔内多发小淋巴结，部分稍大，较大者短径约10mm。\n【心脏及大血管】心影增大；主动脉及冠状动脉壁见致密影。\n【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔积液：否。增强后未见明显异常强化。\n【膈肌】光整，未见明显异常抬高。增强后未见明显异常强化。\n【胸壁】胸廓对称，骨质未见明显异常。增强后未见明显异常强化。\n上腹部CT平扫+增强：\n【肝脏】各叶比例在正常范围内，外形轮廓规则，肝内小圆形无强化低密度影，较大者长径约6mm。静脉期肝左叶小片状稍低密度影（薄层im290）。\n【胆囊及胆管】胆囊形态、大小正常，囊壁未见增厚，囊内未见明显异常密度影；肝内外胆管轻度扩张。\n【胰腺】形态、大小正常，实质内未见明显异常密度影；胰管未见明显扩张。增强后未见明显异常强化。\n【脾脏】形态、大小正常，实质内未见明显异常密度影。增强后未见明显异常强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均匀，未见明显肿大淋巴结，未见明显渗出及积液。增强后未见明显异常强化。\n下腹部CT平扫+增强：\n【肾脏】两侧肾脏大小、形态、位置正常，右肾窦点状致密影；肾盂肾盏未见明显扩张。增强后未见明显异常强化。\n【肾上腺】双肾上腺增粗，左肾上腺低密度结节，长径约12mm,可见强化。\n【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均匀，未见明显肿大淋巴结，未见明显渗出及积液。增强后未见明显异常强化。\n盆腔CT平扫+增强：\n【膀胱】充盈欠佳，壁未见明显增厚，其内未见明显异常密度影。增强后未见明显异常强化。\n【子宫及附件】子宫呈肌组织结构性空扫",
  "conclusion": "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋巴结，部分较前稍缩小。\n2.两肺多发结节，较前变化不大，密切随诊。\n3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓解；右肺上叶局限性肺气肿。\n4.心影增大；主动脉及冠状动脉壁钙化。\n5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影（薄层im290），较前相仿，随诊。\n6.肝内外胆管轻度扩张。\n7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检查；右肾小结石。\n8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结节。\n9.下腹腔内肠系膜间隙多发稍大淋巴结。\n10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠内容物多；十二指肠降部憩室；结合临床体征随诊。\n11.右肩部皮下低密度结节，较前相仿，随诊；L4及以上椎体I°滑脱。",
  "physician": null,
  "reviewer": null
}
2026-08-10 16:19:24,721 INFO     29 [qwen-vl-text] coord API call start, page=7, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=553741, prompt_len=1154
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共29行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "报告 2025-10-08", "影像描述", "颈部软组织CT平扫+增强：", "【所见咽部】所见咽腔结构对称，未见明显异常", "密度影。增强后未见明显异常强化。", "【喉部及下咽部】喉腔结构对称，会厌、声带、", "梨状窝形态及密度未见明显异常。增强后未见明显", "异常强化。", "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "明显占位性病变。", "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "异常。增强后未见明显异常强化。", "【气管及食管】气管居中，管腔通畅；食管颈段", "管壁未见明显增厚。", "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "影。增强后未见明显异常强化。", "【淋巴结】未见明显肿大淋巴结。", "【其他】副鼻窦内低密度影。", "胸部CT平扫+增强：", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord API raw response (len=1733):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 137]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 223]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [396, 315, 588, 337]},
	{"text": "报告 2025-10-08", "bbox": [387, 367, 609, 387]},
	{"text": "影像描述", "bbox": [387, 411, 431, 427]},
	{"text": "颈部软组织CT平扫+增强：", "bbox": [387, 451, 500, 467]},
	{"text": "【所见咽部】所见咽腔结构对称，未见明显异常", "bbox": [405, 472, 608, 488]},
	{"text": "密度影。增强后未见明显异常强化。", "bbox": [387, 493, 541, 508]},
	{"text": "【喉部及下咽部】喉腔结构对称，会厌、声带、", "bbox": [405, 513, 603, 529]},
	{"text": "梨状窝形态及密度未见明显异常。增强后未见明显", "bbox": [387, 534, 608, 550]},
	{"text": "异常强化。", "bbox": [387, 555, 436, 570]},
	{"text": "【甲状腺及甲状旁腺区】甲状腺左右叶大小、形", "bbox": [405, 576, 608, 591]},
	{"text": "态正常，甲状腺双叶低密度结节；甲状旁腺区未见", "bbox": [387, 596, 608, 612]},
	{"text": "明显占位性病变。", "bbox": [387, 617, 464, 633]},
	{"text": "【唾液腺】双侧腮腺、颌下腺形态密度未见明显", "bbox": [405, 638, 608, 654]},
	{"text": "异常。增强后未见明显异常强化。", "bbox": [387, 659, 531, 674]},
	{"text": "【气管及食管】气管居中，管腔通畅；食管颈段", "bbox": [405, 680, 608, 695]},
	{"text": "管壁未见明显增厚。", "bbox": [387, 701, 473, 717]},
	{"text": "【颈部间隙】脂肪间隙清晰，未见明显异常密度", "bbox": [405, 722, 608, 737]},
	{"text": "影。增强后未见明显异常强化。", "bbox": [387, 742, 521, 758]},
	{"text": "【淋巴结】未见明显肿大淋巴结。", "bbox": [405, 763, 544, 779]},
	{"text": "【其他】副鼻窦内低密度影。", "bbox": [405, 784, 524, 800]},
	{"text": "胸部CT平扫+增强：", "bbox": [387, 805, 471, 821]},
	{"text": "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "bbox": [405, 826, 608, 842]},
	{"text": "移动影像浏览", "bbox": [470, 859, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 576, 893]}
]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord API: raw_items=29, valid_items=29, elapsed=9.4s
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 137]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 223]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[396, 315, 588, 337]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[6]: text=报告 2025-10-08, bbox=[387, 367, 609, 387]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[7]: text=影像描述, bbox=[387, 411, 431, 427]
2026-08-10 16:19:34,074 INFO     29 [qwen-vl-text] coord item[8]: text=颈部软组织CT平扫+增强：, bbox=[387, 451, 500, 467]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[9]: text=【所见咽部】所见咽腔结构对称，未见明显异常, bbox=[405, 472, 608, 488]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[10]: text=密度影。增强后未见明显异常强化。, bbox=[387, 493, 541, 508]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[11]: text=【喉部及下咽部】喉腔结构对称，会厌、声带、, bbox=[405, 513, 603, 529]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[12]: text=梨状窝形态及密度未见明显异常。增强后未见明显, bbox=[387, 534, 608, 550]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[13]: text=异常强化。, bbox=[387, 555, 436, 570]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[14]: text=【甲状腺及甲状旁腺区】甲状腺左右叶大小、形, bbox=[405, 576, 608, 591]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[15]: text=态正常，甲状腺双叶低密度结节；甲状旁腺区未见, bbox=[387, 596, 608, 612]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[16]: text=明显占位性病变。, bbox=[387, 617, 464, 633]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[17]: text=【唾液腺】双侧腮腺、颌下腺形态密度未见明显, bbox=[405, 638, 608, 654]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[18]: text=异常。增强后未见明显异常强化。, bbox=[387, 659, 531, 674]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[19]: text=【气管及食管】气管居中，管腔通畅；食管颈段, bbox=[405, 680, 608, 695]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[20]: text=管壁未见明显增厚。, bbox=[387, 701, 473, 717]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[21]: text=【颈部间隙】脂肪间隙清晰，未见明显异常密度, bbox=[405, 722, 608, 737]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[22]: text=影。增强后未见明显异常强化。, bbox=[387, 742, 521, 758]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[23]: text=【淋巴结】未见明显肿大淋巴结。, bbox=[405, 763, 544, 779]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[24]: text=【其他】副鼻窦内低密度影。, bbox=[405, 784, 524, 800]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[25]: text=胸部CT平扫+增强：, bbox=[387, 805, 471, 821]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[26]: text=【肺野】两肺野纹理清晰，左肺下叶见斑片状高, bbox=[405, 826, 608, 842]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[27]: text=移动影像浏览, bbox=[470, 859, 525, 873]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] coord item[28]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 576, 893]
2026-08-10 16:19:34,075 INFO     29 [qwen-vl-text] page=7 — 29/29 coords, api_time=9.4s
2026-08-10 16:19:34,077 INFO     29 [qwen-vl-text] coord API call start, page=8, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=590262, prompt_len=1230
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共31行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "密度影。两肺多发结节，较大者：右肺上叶（Img7", "9）见一实性结节影，大小约5mm×3mm。两肺索", "条及片絮影；右肺上叶局部透亮区。", "【肺门】双肺门多发小淋巴结，部分稍大。", "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "症，病灶周围结节影。", "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "稍大，较大者短径约10mm。", "【心脏及大血管】心影增大；主动脉及冠状动", "脉壁见致密影。", "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "积液：否。增强后未见明显异常强化。", "【膈肌】光整，未见明显异常抬高。增强后未见", "明显异常强化。", "【胸壁】胸廓对称，骨质未见明显异常。增强后", "未见明显异常强化。", "上腹部CT平扫+增强：", "【肝脏】各叶比例在正常范围内，外形轮廓规", "则，肝内小圆形无强化低密度影，较大者长径约6", "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "0）。", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord API raw response (len=1891):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 137]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 222]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [398, 317, 587, 336]},
	{"text": "【肺野】两肺野纹理清晰，左肺下叶见斑片状高", "bbox": [405, 362, 608, 378]},
	{"text": "密度影。两肺多发结节，较大者：右肺上叶（Img7", "bbox": [387, 382, 608, 398]},
	{"text": "9）见一实性结节影，大小约5mm×3mm。两肺索", "bbox": [387, 402, 608, 418]},
	{"text": "条及片絮影；右肺上叶局部透亮区。", "bbox": [387, 422, 542, 438]},
	{"text": "【肺门】双肺门多发小淋巴结，部分稍大。", "bbox": [405, 444, 581, 460]},
	{"text": "【气管及支气管】左下肺支气管闭塞伴阻塞性炎", "bbox": [405, 464, 608, 480]},
	{"text": "症，病灶周围结节影。", "bbox": [387, 485, 484, 501]},
	{"text": "【纵隔】纵隔居中，纵隔内多发小淋巴结，部分", "bbox": [405, 506, 608, 522]},
	{"text": "稍大，较大者短径约10mm。", "bbox": [387, 527, 509, 543]},
	{"text": "【心脏及大血管】心影增大；主动脉及冠状动", "bbox": [405, 548, 608, 564]},
	{"text": "脉壁见致密影。", "bbox": [387, 569, 453, 585]},
	{"text": "【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔", "bbox": [405, 590, 608, 606]},
	{"text": "积液：否。增强后未见明显异常强化。", "bbox": [387, 611, 551, 627]},
	{"text": "【膈肌】光整，未见明显异常抬高。增强后未见", "bbox": [405, 632, 608, 648]},
	{"text": "明显异常强化。", "bbox": [387, 653, 453, 669]},
	{"text": "【胸壁】胸廓对称，骨质未见明显异常。增强后", "bbox": [405, 674, 608, 690]},
	{"text": "未见明显异常强化。", "bbox": [387, 694, 474, 710]},
	{"text": "上腹部CT平扫+增强：", "bbox": [387, 715, 481, 731]},
	{"text": "【肝脏】各叶比例在正常范围内，外形轮廓规", "bbox": [405, 736, 608, 752]},
	{"text": "则，肝内小圆形无强化低密度影，较大者长径约6", "bbox": [387, 757, 608, 773]},
	{"text": "mm。静脉期肝左叶小片状稍低密度影（薄层im29", "bbox": [387, 777, 608, 793]},
	{"text": "0）。", "bbox": [387, 798, 404, 814]},
	{"text": "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "bbox": [405, 819, 608, 835]},
	{"text": "移动影像浏览", "bbox": [470, 858, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 893]}
]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord API: raw_items=31, valid_items=31, elapsed=12.3s
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 137]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 222]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[398, 317, 587, 336]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[6]: text=【肺野】两肺野纹理清晰，左肺下叶见斑片状高, bbox=[405, 362, 608, 378]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[7]: text=密度影。两肺多发结节，较大者：右肺上叶（Img7, bbox=[387, 382, 608, 398]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[8]: text=9）见一实性结节影，大小约5mm×3mm。两肺索, bbox=[387, 402, 608, 418]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[9]: text=条及片絮影；右肺上叶局部透亮区。, bbox=[387, 422, 542, 438]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[10]: text=【肺门】双肺门多发小淋巴结，部分稍大。, bbox=[405, 444, 581, 460]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[11]: text=【气管及支气管】左下肺支气管闭塞伴阻塞性炎, bbox=[405, 464, 608, 480]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[12]: text=症，病灶周围结节影。, bbox=[387, 485, 484, 501]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[13]: text=【纵隔】纵隔居中，纵隔内多发小淋巴结，部分, bbox=[405, 506, 608, 522]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[14]: text=稍大，较大者短径约10mm。, bbox=[387, 527, 509, 543]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[15]: text=【心脏及大血管】心影增大；主动脉及冠状动, bbox=[405, 548, 608, 564]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[16]: text=脉壁见致密影。, bbox=[387, 569, 453, 585]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[17]: text=【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔, bbox=[405, 590, 608, 606]
2026-08-10 16:19:46,329 INFO     29 [qwen-vl-text] coord item[18]: text=积液：否。增强后未见明显异常强化。, bbox=[387, 611, 551, 627]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[19]: text=【膈肌】光整，未见明显异常抬高。增强后未见, bbox=[405, 632, 608, 648]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[20]: text=明显异常强化。, bbox=[387, 653, 453, 669]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[21]: text=【胸壁】胸廓对称，骨质未见明显异常。增强后, bbox=[405, 674, 608, 690]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[22]: text=未见明显异常强化。, bbox=[387, 694, 474, 710]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[23]: text=上腹部CT平扫+增强：, bbox=[387, 715, 481, 731]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[24]: text=【肝脏】各叶比例在正常范围内，外形轮廓规, bbox=[405, 736, 608, 752]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[25]: text=则，肝内小圆形无强化低密度影，较大者长径约6, bbox=[387, 757, 608, 773]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[26]: text=mm。静脉期肝左叶小片状稍低密度影（薄层im29, bbox=[387, 777, 608, 793]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[27]: text=0）。, bbox=[387, 798, 404, 814]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[28]: text=【胆囊及胆管】胆囊形态、大小正常，囊壁未见, bbox=[405, 819, 608, 835]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[29]: text=移动影像浏览, bbox=[470, 858, 525, 873]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] coord item[30]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 893]
2026-08-10 16:19:46,330 INFO     29 [qwen-vl-text] page=8 — 31/31 coords, api_time=12.3s
2026-08-10 16:19:46,331 INFO     29 [qwen-vl-text] coord API call start, page=9, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=594901, prompt_len=1245
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共32行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "扩张。", "【胰腺】形态、大小正常，实质内未见明显异常", "密度影；胰管未见明显扩张。增强后未见明显异常", "强化。", "【脾脏】形态、大小正常，实质内未见明显异常", "密度影。增强后未见明显异常强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "下腹部CT平扫+增强：", "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "见明显异常强化。", "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "节，长径约12mm,可见强化。", "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "增强后未见明显异常强化。", "盆腔CT平扫+增强：", "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "明显异常密度影。增强后未见明显异常强化。", "【子宫及附件】子宫呈肌组织结构性空扫", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-10 16:19:56,757 INFO     29 [qwen-vl-text] coord API raw response (len=1947):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 137]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 223]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 283]},
	{"text": "PDF报告 图像 分享", "bbox": [397, 317, 587, 336]},
	{"text": "【胆囊及胆管】胆囊形态、大小正常，囊壁未见", "bbox": [405, 358, 608, 374]},
	{"text": "增厚，囊内未见明显异常密度影；肝内外胆管轻度", "bbox": [387, 379, 608, 395]},
	{"text": "扩张。", "bbox": [387, 400, 414, 416]},
	{"text": "【胰腺】形态、大小正常，实质内未见明显异常", "bbox": [405, 420, 608, 437]},
	{"text": "密度影；胰管未见明显扩张。增强后未见明显异常", "bbox": [387, 441, 608, 458]},
	{"text": "强化。", "bbox": [387, 462, 414, 478]},
	{"text": "【脾脏】形态、大小正常，实质内未见明显异常", "bbox": [405, 483, 608, 499]},
	{"text": "密度影。增强后未见明显异常强化。", "bbox": [387, 504, 541, 520]},
	{"text": "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "bbox": [405, 524, 608, 541]},
	{"text": "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "bbox": [387, 545, 604, 561]},
	{"text": "增强后未见明显异常强化。", "bbox": [387, 566, 502, 582]},
	{"text": "下腹部CT平扫+增强：", "bbox": [387, 587, 481, 603]},
	{"text": "【肾脏】两侧肾脏大小、形态、位置正常，右肾", "bbox": [405, 608, 608, 624]},
	{"text": "窦点状致密影；肾盂肾盏未见明显扩张。增强后未", "bbox": [387, 629, 608, 645]},
	{"text": "见明显异常强化。", "bbox": [387, 650, 463, 666]},
	{"text": "【肾上腺】双肾上腺增粗，左肾上腺低密度结", "bbox": [405, 670, 608, 687]},
	{"text": "节，长径约12mm,可见强化。", "bbox": [387, 691, 512, 708]},
	{"text": "【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均", "bbox": [405, 712, 608, 728]},
	{"text": "匀，未见明显肿大淋巴结，未见明显渗出及积液。", "bbox": [387, 733, 604, 749]},
	{"text": "增强后未见明显异常强化。", "bbox": [387, 754, 502, 770]},
	{"text": "盆腔CT平扫+增强：", "bbox": [387, 774, 471, 790]},
	{"text": "【膀胱】充盈欠佳，壁未见明显增厚，其内未见", "bbox": [405, 795, 608, 811]},
	{"text": "明显异常密度影。增强后未见明显异常强化。", "bbox": [387, 816, 580, 832]},
	{"text": "【子宫及附件】子宫呈肌组织结构性空扫", "bbox": [405, 837, 598, 853]},
	{"text": "移动影像浏览", "bbox": [470, 859, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 878, 575, 893]}
]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord API: raw_items=32, valid_items=32, elapsed=10.4s
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 137]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 223]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 283]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[397, 317, 587, 336]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[6]: text=【胆囊及胆管】胆囊形态、大小正常，囊壁未见, bbox=[405, 358, 608, 374]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[7]: text=增厚，囊内未见明显异常密度影；肝内外胆管轻度, bbox=[387, 379, 608, 395]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[8]: text=扩张。, bbox=[387, 400, 414, 416]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[9]: text=【胰腺】形态、大小正常，实质内未见明显异常, bbox=[405, 420, 608, 437]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[10]: text=密度影；胰管未见明显扩张。增强后未见明显异常, bbox=[387, 441, 608, 458]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[11]: text=强化。, bbox=[387, 462, 414, 478]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[12]: text=【脾脏】形态、大小正常，实质内未见明显异常, bbox=[405, 483, 608, 499]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[13]: text=密度影。增强后未见明显异常强化。, bbox=[387, 504, 541, 520]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[14]: text=【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均, bbox=[405, 524, 608, 541]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[15]: text=匀，未见明显肿大淋巴结，未见明显渗出及积液。, bbox=[387, 545, 604, 561]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[16]: text=增强后未见明显异常强化。, bbox=[387, 566, 502, 582]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[17]: text=下腹部CT平扫+增强：, bbox=[387, 587, 481, 603]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[18]: text=【肾脏】两侧肾脏大小、形态、位置正常，右肾, bbox=[405, 608, 608, 624]
2026-08-10 16:19:56,758 INFO     29 [qwen-vl-text] coord item[19]: text=窦点状致密影；肾盂肾盏未见明显扩张。增强后未, bbox=[387, 629, 608, 645]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[20]: text=见明显异常强化。, bbox=[387, 650, 463, 666]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[21]: text=【肾上腺】双肾上腺增粗，左肾上腺低密度结, bbox=[405, 670, 608, 687]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[22]: text=节，长径约12mm,可见强化。, bbox=[387, 691, 512, 708]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[23]: text=【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均, bbox=[405, 712, 608, 728]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[24]: text=匀，未见明显肿大淋巴结，未见明显渗出及积液。, bbox=[387, 733, 604, 749]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[25]: text=增强后未见明显异常强化。, bbox=[387, 754, 502, 770]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[26]: text=盆腔CT平扫+增强：, bbox=[387, 774, 471, 790]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[27]: text=【膀胱】充盈欠佳，壁未见明显增厚，其内未见, bbox=[405, 795, 608, 811]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[28]: text=明显异常密度影。增强后未见明显异常强化。, bbox=[387, 816, 580, 832]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[29]: text=【子宫及附件】子宫呈肌组织结构性空扫, bbox=[405, 837, 598, 853]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[30]: text=移动影像浏览, bbox=[470, 859, 525, 873]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] coord item[31]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 878, 575, 893]
2026-08-10 16:19:56,759 INFO     29 [qwen-vl-text] page=9 — 32/32 coords, api_time=10.4s
2026-08-10 16:19:56,761 INFO     29 [qwen-vl-text] coord API call start, page=10, endpoint=http://10.16.3.16:8090/v1/chat/completions, model=Qwen/Qwen3-VL-30B-A3B-Instruct-FP8, img_bytes=566615, prompt_len=1201
[qwen-vl-text] coord prompt:
你是一个高精度的文档坐标定位引擎。请在图片中精确定位以下每行文本的位置。

## 需要定位的文本行（共30行）
["南京鼓楼医院云胶片", "女/75岁", "设备类型 CT 患者类型 无", "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "腹部、盆腔）]", "PDF报告 图像 分享", "诊断意见", "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "巴结，部分较前稍缩小。", "2.两肺多发结节，较前变化不大，密切随诊。", "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "解；右肺上叶局限性肺气肿。", "4.心影增大；主动脉及冠状动脉壁钙化。", "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "（薄层im290），较前相仿，随诊。", "6.肝内外胆管轻度扩张。", "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "查；右肾小结石。", "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "节。", "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "内容物多；十二指肠降部憩室；结合临床体征随", "诊。", "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "以上椎体I°滑脱。", "移动影像浏览", "© 2022 南京鼓楼医院影像云平台 V1.0"]

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
2026-08-10 16:20:06,745 INFO     29 [qwen-vl-text] coord API raw response (len=1821):
[
	{"text": "南京鼓楼医院云胶片", "bbox": [444, 118, 552, 136]},
	{"text": "女/75岁", "bbox": [588, 163, 629, 178]},
	{"text": "设备类型 CT 患者类型 无", "bbox": [387, 205, 594, 222]},
	{"text": "检查项目 [CT平扫+增强（颈部、胸部、上腹部、下", "bbox": [387, 250, 618, 267]},
	{"text": "腹部、盆腔）]", "bbox": [438, 267, 502, 282]},
	{"text": "PDF报告 图像 分享", "bbox": [397, 317, 587, 335]},
	{"text": "诊断意见", "bbox": [387, 368, 431, 384]},
	{"text": "1.肺癌复查：左肺下叶斑片影较前（2025-07-15）", "bbox": [387, 407, 603, 423]},
	{"text": "明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前", "bbox": [387, 428, 608, 444]},
	{"text": "缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋", "bbox": [387, 449, 608, 465]},
	{"text": "巴结，部分较前稍缩小。", "bbox": [387, 470, 494, 486]},
	{"text": "2.两肺多发结节，较前变化不大，密切随诊。", "bbox": [387, 491, 578, 507]},
	{"text": "3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓", "bbox": [387, 512, 608, 528]},
	{"text": "解；右肺上叶局限性肺气肿。", "bbox": [387, 532, 515, 548]},
	{"text": "4.心影增大；主动脉及冠状动脉壁钙化。", "bbox": [387, 553, 558, 569]},
	{"text": "5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影", "bbox": [387, 574, 608, 590]},
	{"text": "（薄层im290），较前相仿，随诊。", "bbox": [393, 595, 534, 611]},
	{"text": "6.肝内外胆管轻度扩张。", "bbox": [387, 616, 491, 632]},
	{"text": "7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检", "bbox": [387, 637, 608, 653]},
	{"text": "查；右肾小结石。", "bbox": [387, 658, 464, 674]},
	{"text": "8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结", "bbox": [387, 678, 608, 694]},
	{"text": "节。", "bbox": [387, 699, 405, 715]},
	{"text": "9.下腹腔内肠系膜间隙多发稍大淋巴结。", "bbox": [387, 720, 559, 736]},
	{"text": "10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠", "bbox": [387, 741, 608, 757]},
	{"text": "内容物多；十二指肠降部憩室；结合临床体征随", "bbox": [387, 762, 608, 778]},
	{"text": "诊。", "bbox": [387, 783, 405, 799]},
	{"text": "11.右肩部皮下低密度结节，较前相仿，随诊；L4及", "bbox": [387, 804, 608, 820]},
	{"text": "以上椎体I°滑脱。", "bbox": [387, 825, 460, 841]},
	{"text": "移动影像浏览", "bbox": [470, 860, 525, 873]},
	{"text": "© 2022 南京鼓楼医院影像云平台 V1.0", "bbox": [420, 879, 575, 893]}
]
2026-08-10 16:20:06,745 INFO     29 [qwen-vl-text] coord API: raw_items=30, valid_items=30, elapsed=10.0s
2026-08-10 16:20:06,745 INFO     29 [qwen-vl-text] coord item[0]: text=南京鼓楼医院云胶片, bbox=[444, 118, 552, 136]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[1]: text=女/75岁, bbox=[588, 163, 629, 178]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[2]: text=设备类型 CT 患者类型 无, bbox=[387, 205, 594, 222]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[3]: text=检查项目 [CT平扫+增强（颈部、胸部、上腹部、下, bbox=[387, 250, 618, 267]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[4]: text=腹部、盆腔）], bbox=[438, 267, 502, 282]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[5]: text=PDF报告 图像 分享, bbox=[397, 317, 587, 335]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[6]: text=诊断意见, bbox=[387, 368, 431, 384]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[7]: text=1.肺癌复查：左肺下叶斑片影较前（2025-07-15）, bbox=[387, 407, 603, 423]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[8]: text=明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前, bbox=[387, 428, 608, 444]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[9]: text=缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋, bbox=[387, 449, 608, 465]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[10]: text=巴结，部分较前稍缩小。, bbox=[387, 470, 494, 486]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[11]: text=2.两肺多发结节，较前变化不大，密切随诊。, bbox=[387, 491, 578, 507]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[12]: text=3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓, bbox=[387, 512, 608, 528]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[13]: text=解；右肺上叶局限性肺气肿。, bbox=[387, 532, 515, 548]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[14]: text=4.心影增大；主动脉及冠状动脉壁钙化。, bbox=[387, 553, 558, 569]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[15]: text=5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影, bbox=[387, 574, 608, 590]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[16]: text=（薄层im290），较前相仿，随诊。, bbox=[393, 595, 534, 611]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[17]: text=6.肝内外胆管轻度扩张。, bbox=[387, 616, 491, 632]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[18]: text=7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检, bbox=[387, 637, 608, 653]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[19]: text=查；右肾小结石。, bbox=[387, 658, 464, 674]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[20]: text=8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结, bbox=[387, 678, 608, 694]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[21]: text=节。, bbox=[387, 699, 405, 715]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[22]: text=9.下腹腔内肠系膜间隙多发稍大淋巴结。, bbox=[387, 720, 559, 736]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[23]: text=10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠, bbox=[387, 741, 608, 757]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[24]: text=内容物多；十二指肠降部憩室；结合临床体征随, bbox=[387, 762, 608, 778]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[25]: text=诊。, bbox=[387, 783, 405, 799]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[26]: text=11.右肩部皮下低密度结节，较前相仿，随诊；L4及, bbox=[387, 804, 608, 820]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[27]: text=以上椎体I°滑脱。, bbox=[387, 825, 460, 841]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[28]: text=移动影像浏览, bbox=[470, 860, 525, 873]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] coord item[29]: text=© 2022 南京鼓楼医院影像云平台 V1.0, bbox=[420, 879, 575, 893]
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] page=10 — 30/30 coords, api_time=10.0s
2026-08-10 16:20:06,746 INFO     29 [qwen-vl-text] new_positions (122):
[[7, 373.79916650390624, 464.7232880859375, 70.24256811523438, 81.55281213378906], [7, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [7, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.74654821777344], [7, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [7, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [7, 333.38844580078126, 495.03132861328123, 187.5119403076172, 200.60801232910157], [7, 325.8114356689453, 512.7110189208985, 218.46629235839845, 230.3718123779297], [7, 325.8114356689453, 362.8545963134766, 244.6584364013672, 254.1828524169922], [7, 325.8114356689453, 420.94500732421875, 268.4694764404297, 277.9938924560547], [7, 340.9654559326172, 511.86912890625, 280.9702724609375, 290.4946884765625], [7, 325.8114356689453, 455.46249792480467, 293.47106848144534, 302.40020849609374], [7, 340.9654559326172, 507.65967883300783, 305.3765885009766, 314.9010045166016], [7, 325.8114356689453, 511.86912890625, 317.8773845214844, 327.4018005371094], [7, 325.8114356689453, 367.06404638671876, 330.3781805419922, 339.30732055664066], [7, 340.9654559326172, 511.86912890625, 342.87897656250004, 351.80811657714844], [7, 325.8114356689453, 511.86912890625, 354.78449658203124, 364.3089125976563], [7, 325.8114356689453, 390.636966796875, 367.2852926025391, 376.80970861816405], [7, 340.9654559326172, 511.86912890625, 379.7860886230469, 389.3105046386719], [7, 325.8114356689453, 447.0435977783203, 392.2868846435547, 401.21602465820314], [7, 340.9654559326172, 511.86912890625, 404.7876806640625, 413.716820678711], [7, 325.8114356689453, 398.2139769287109, 417.28847668457036, 426.81289270019533], [7, 340.9654559326172, 511.86912890625, 429.78927270507813, 438.7184127197266], [7, 325.8114356689453, 438.62469763183594, 441.6947927246094, 451.2192087402344], [7, 340.9654559326172, 457.98816796875, 454.1955887451172, 463.7200047607422], [7, 340.9654559326172, 441.15036767578124, 466.696384765625, 476.22080078125003], [7, 325.8114356689453, 396.5301968994141, 479.19718078613283, 488.7215968017578], [7, 340.9654559326172, 511.86912890625, 491.69797680664067, 501.22239282226565], [7, 395.6883068847656, 441.9922576904297, 511.3420848388672, 519.6759488525391], [7, 353.59380615234375, 484.9286484375, 522.6523288574219, 531.5814688720703], [8, 373.79916650390624, 464.7232880859375, 70.24256811523438, 81.55281213378906], [8, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [8, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.15127221679688], [8, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [8, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [8, 335.07222583007814, 494.1894385986328, 188.70249230957032, 200.01273632812502], [8, 340.9654559326172, 511.86912890625, 215.48991235351562, 225.01432836914063], [8, 325.8114356689453, 511.86912890625, 227.39543237304687, 236.91984838867188], [8, 325.8114356689453, 511.86912890625, 239.30095239257813, 248.82536840820313], [8, 325.8114356689453, 456.30438793945314, 251.20647241210938, 260.7308884277344], [8, 340.9654559326172, 489.13809851074217, 264.30254443359377, 273.82696044921875], [8, 340.9654559326172, 511.86912890625, 276.208064453125, 285.73248046875], [8, 325.8114356689453, 407.47476708984374, 288.7088604736328, 298.23327648925783], [8, 340.9654559326172, 511.86912890625, 301.20965649414063, 310.7340725097656], [8, 325.8114356689453, 428.5220174560547, 313.71045251464847, 323.23486853027345], [8, 340.9654559326172, 511.86912890625, 326.21124853515624, 335.7356645507813], [8, 325.8114356689453, 381.3761766357422, 338.7120445556641, 348.23646057128906], [8, 340.9654559326172, 511.86912890625, 351.2128405761719, 360.7372565917969], [8, 325.8114356689453, 463.8813980712891, 363.7136365966797, 373.2380526123047], [8, 340.9654559326172, 511.86912890625, 376.2144326171875, 385.7388486328125], [8, 325.8114356689453, 381.3761766357422, 388.7152286376953, 398.23964465332034], [8, 340.9654559326172, 511.86912890625, 401.21602465820314, 410.7404406738281], [8, 325.8114356689453, 399.0558669433594, 413.1215446777344, 422.64596069335937], [8, 325.8114356689453, 404.94909704589844, 425.6223406982422, 435.1467567138672], [8, 340.9654559326172, 511.86912890625, 438.12313671875, 447.64755273437504], [8, 325.8114356689453, 511.86912890625, 450.62393273925784, 460.1483487548828], [8, 325.8114356689453, 511.86912890625, 462.5294527587891, 472.05386877441407], [8, 325.8114356689453, 340.12356591796873, 475.03024877929687, 484.5546647949219], [8, 340.9654559326172, 511.86912890625, 487.5310447998047, 497.0554608154297], [8, 395.6883068847656, 441.9922576904297, 510.7468088378906, 519.6759488525391], [8, 353.59380615234375, 484.0867584228516, 522.6523288574219, 531.5814688720703], [9, 373.79916650390624, 464.7232880859375, 70.24256811523438, 81.55281213378906], [9, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [9, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.74654821777344], [9, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [9, 368.74782641601564, 422.62878735351563, 158.9386922607422, 168.4631082763672], [9, 334.23033581542967, 494.1894385986328, 188.70249230957032, 200.01273632812502], [9, 340.9654559326172, 511.86912890625, 213.10880834960938, 222.63322436523438], [9, 325.8114356689453, 511.86912890625, 225.6096043701172, 235.1340203857422], [9, 325.8114356689453, 348.5424660644531, 238.11040039062502, 247.63481640625002], [9, 340.9654559326172, 511.86912890625, 250.01592041015627, 260.1356124267578], [9, 325.8114356689453, 511.86912890625, 262.5167164306641, 272.63640844726564], [9, 325.8114356689453, 348.5424660644531, 275.0175124511719, 284.5419284667969], [9, 340.9654559326172, 511.86912890625, 287.5183084716797, 297.0427244873047], [9, 325.8114356689453, 455.46249792480467, 300.0191044921875, 309.5435205078125], [9, 340.9654559326172, 511.86912890625, 311.9246245117188, 322.04431652832034], [9, 325.8114356689453, 508.50156884765624, 324.42542053222655, 333.9498365478516], [9, 325.8114356689453, 422.62878735351563, 336.9262165527344, 346.45063256835937], [9, 325.8114356689453, 404.94909704589844, 349.4270125732422, 358.9514285888672], [9, 340.9654559326172, 511.86912890625, 361.92780859375, 371.45222460937504], [9, 325.8114356689453, 511.86912890625, 374.42860461425784, 383.9530206298828], [9, 325.8114356689453, 389.79507678222654, 386.9294006347656, 396.45381665039065], [9, 340.9654559326172, 511.86912890625, 398.83492065429687, 408.9546126708984], [9, 325.8114356689453, 431.0476875, 411.3357166748047, 421.45540869140626], [9, 340.9654559326172, 511.86912890625, 423.83651269531254, 433.3609287109375], [9, 325.8114356689453, 508.50156884765624, 436.3373087158203, 445.86172473144535], [9, 325.8114356689453, 422.62878735351563, 448.83810473632815, 458.3625207519531], [9, 325.8114356689453, 396.5301968994141, 460.7436247558594, 470.2680407714844], [9, 340.9654559326172, 511.86912890625, 473.24442077636724, 482.7688367919922], [9, 325.8114356689453, 488.29620849609375, 485.745216796875, 495.26963281250005], [9, 340.9654559326172, 503.4502287597656, 498.24601281738285, 507.7704288330078], [9, 395.6883068847656, 441.9922576904297, 511.3420848388672, 519.6759488525391], [9, 353.59380615234375, 484.0867584228516, 522.6523288574219, 531.5814688720703], [10, 373.79916650390624, 464.7232880859375, 70.24256811523438, 80.9575361328125], [10, 495.03132861328123, 529.5488192138672, 97.0299881591797, 105.95912817382813], [10, 325.8114356689453, 500.0826687011719, 122.03158020019532, 132.15127221679688], [10, 325.8114356689453, 520.2880290527344, 148.81900024414062, 158.9386922607422], [10, 368.74782641601564, 422.62878735351563, 158.9386922607422, 167.86783227539064], [10, 334.23033581542967, 494.1894385986328, 188.70249230957032, 199.41746032714843], [10, 325.8114356689453, 362.8545963134766, 219.061568359375, 228.585984375], [10, 325.8114356689453, 507.65967883300783, 242.27733239746095, 251.80174841308596], [10, 325.8114356689453, 511.86912890625, 254.77812841796876, 264.30254443359377], [10, 325.8114356689453, 511.86912890625, 267.27892443847657, 276.8033404541016], [10, 325.8114356689453, 415.8936672363281, 279.7797204589844, 289.3041364746094], [10, 325.8114356689453, 486.61242846679687, 292.2805164794922, 301.8049324951172], [10, 325.8114356689453, 511.86912890625, 304.7813125, 314.305728515625], [10, 325.8114356689453, 433.5733575439453, 316.68683251953127, 326.21124853515624], [10, 325.8114356689453, 469.7746281738281, 329.1876285400391, 338.7120445556641], [10, 325.8114356689453, 511.86912890625, 341.6884245605469, 351.2128405761719], [10, 330.86277575683596, 449.5692678222656, 354.1892205810547, 363.7136365966797], [10, 325.8114356689453, 413.3679971923828, 366.6900166015625, 376.2144326171875], [10, 325.8114356689453, 511.86912890625, 379.1908126220703, 388.7152286376953], [10, 325.8114356689453, 390.636966796875, 391.69160864257816, 401.21602465820314], [10, 325.8114356689453, 511.86912890625, 403.5971286621094, 413.1215446777344], [10, 325.8114356689453, 340.9654559326172, 416.0979246826172, 425.6223406982422], [10, 325.8114356689453, 470.61651818847656, 428.598720703125, 438.12313671875], [10, 325.8114356689453, 511.86912890625, 441.0995167236328, 450.62393273925784], [10, 325.8114356689453, 511.86912890625, 453.60031274414064, 463.1247287597656], [10, 325.8114356689453, 340.9654559326172, 466.1011087646485, 475.62552478027345], [10, 325.8114356689453, 511.86912890625, 478.60190478515625, 488.1263208007813], [10, 325.8114356689453, 387.26940673828125, 491.1027008056641, 500.62711682128906], [10, 395.6883068847656, 441.9922576904297, 511.9373608398438, 519.6759488525391], [10, 353.59380615234375, 484.0867584228516, 523.2476048583984, 531.5814688720703]]
2026-08-10 16:20:06,747 INFO     29 [qwen-vl-text] ═══ DONE ═══ 122 positions, pages=4, time=52.8s
2026-08-10 16:20:06,762 INFO     29 [Pipeline] Component [11]: Extractor:ExaminationReport finished. error=None
2026-08-10 16:20:06,762 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:ExaminationReport | outputs={"chunks": "4 items, types={'ExaminationReport': 4}", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:20:06,762 INFO     29 [Pipeline] Executing component [12]: Extractor:Progress (type=Extractor)
2026-08-10 16:20:06,763 INFO     29 task_executor_f186a2ae4eff_0 reported heartbeat: {"ip_address": "172.18.0.8", "pid": 29, "name": "task_executor_f186a2ae4eff_0", "now": "2026-08-10T16:20:06.762+00:00", "boot_at": "2026-08-10T05:36:29.787+00:00", "pending": 7, "lag": 0, "done": 72, "failed": 0, "current": {"7f4c371294d611f1bd9827cf206dfa2d": {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "Baichuan-M3-Plus___OpenAI-API@OpenAI-API-Compatible", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}}}
2026-08-10 16:20:06,770 INFO     29 [LLM] Extractor call: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:20:06,770 INFO     29 [HISTORY][
  {
    "role": "system",
    "content": "你是一个医疗病程记录结构化提取专家。从病程记录/查房记录/术前小结/术后病程等住院连续性文书中提取结构化数据。\n\n## 上游分类结果\n{classify_result_tks}\n\n## 输出格式\n严格输出纯 JSON，禁止使用 ```json 代码块包裹，禁止输出任何非 JSON 文字。\n\n**输出规则：**\n- 每个片段只包含 1 条病程记录，**严格输出单个 JSON 对象，禁止输出 JSON 数组**\n- 若片段中意外出现多条记录，只提取第一条（以原文出现顺序为准），其余忽略\n\n## ProgressNote Schema\n\n{\n  \"note_type\": \"<string, 记录类型，必须是以下之一：首次病程记录/日常病程记录/主治医师查房记录/科主任/副主任医师查房记录/术前小结/术后首次病程记录/VTE防治病程记录/会诊记录/转科记录/阶段小结/抢救记录/有创诊疗操作记录/术前讨论记录/疑难病例讨论记录/死亡病例讨论记录/其他>\",\n  \"record_time\": \"<string|null, 记录时间 YYYY-MM-DD HH:MM>\",\n  \"recorder\": \"<string|null, 记录/书写医师姓名>\",\n  \"reviewer\": \"<string|null, 查房/审阅上级医师姓名>\",\n  \"reviewer_title\": \"<string|null, 上级医师职称，如主治医师/副主任医师/主任医师>\",\n  \"cf_summary\": \"<string|null, 病例特点归纳（首次病程记录）>\",\n  \"cf_positive_findings\": [\"<string, 阳性发现（首次病程记录）>\"],\n  \"cf_negative_findings\": [\"<string, 有鉴别意义的阴性发现（首次病程记录）>\"],\n  \"dd_diagnosis_basis\": \"<string|null, 诊断依据（首次病程记录）>\",\n  \"dd_differential_diagnoses\": [\"<string, 鉴别诊断病名（首次病程记录）>\"],\n  \"dd_differential_analysis\": \"<string|null, 鉴别诊断分析（首次病程记录）>\",\n  \"tp_examinations\": [\"<string, 拟行检查项目（首次病程记录/术前小结）>\"],\n  \"tp_treatments\": [\"<string, 治疗措施（首次病程记录/术前小结）>\"],\n  \"tp_notes\": \"<string|null, 诊疗计划备注/术前注意事项>\",\n  \"condition_changes\": \"<string|null, 病情变化情况>\",\n  \"test_results\": \"<string|null, 辅助检查结果及临床意义>\",\n  \"superior_opinion\": \"<string|null, 上级医师查房意见/指示>\",\n  \"consultation_opinion\": \"<string|null, 会诊意见>\",\n  \"measures_and_effects\": \"<string|null, 诊疗措施及效果>\",\n  \"order_changes\": \"<string|null, 医嘱更改及理由>\",\n  \"patient_notification\": \"<string|null, 告知患者/家属的重要事项>\",\n  \"rescue_time\": \"<string|null, 抢救时间（抢救记录）>\",\n  \"rescue_measures\": \"<string|null, 抢救措施（抢救记录）>\",\n  \"rescue_participants\": [\"<string, 参加抢救人员（抢救记录）>\"]\n}\n\n## 关键约束\n1. 所有字段值必须来源于原文，禁止编造\n2. 原文中不存在的字段填 null（数组字段填空数组 []）\n3. note_type 判定：标题或行首时间戳后跟类型名；\"主任医师查房记录\"/\"副主任医师查房记录\"归为\"科主任/副主任医师查房记录\"；无法明确归类的病程记录填\"其他\"\n4. 查体数据、检验数值、用药剂量必须原样保留，写入 condition_changes 或 test_results\n5. VTE防治病程记录：评估内容与防治措施写入 condition_changes\n6. 术前小结：拟行检查/手术准备写入 tp_examinations，注意事项写入 tp_notes\n7. 术后首次病程记录：手术经过写入 measures_and_effects，术后情况写入 condition_changes\n8. OCR 纠错规则：仅纠正高置信度的标准医学术语"
  },
  {
    "content": "",
    "role": "user"
  }
]
2026-08-10 16:20:07,682 INFO     29 [LLM] Extractor response: llm_id=qwen3.6-27b-fp8___OpenAI-API
2026-08-10 16:20:07,689 INFO     29 [Pipeline] Component [12]: Extractor:Progress finished. error=None
2026-08-10 16:20:07,689 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Extractor:Progress | outputs={"chunks": "1 items", "html": "", "json": "455 items", "markdown": "", "text": "", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "output_format": "chunks", "chunks_Discharge": "1 items, types={'DischargeRecord': 1}", "chunks_Examination": "4 items, types={'ExaminationReport': 4}", "chunks_Clinical": "1 items, types={'OutpatientRecord': 1}", "chunks_LabExam": "3 items, types={'LabReport': 3}", "route_summary": "{\"chunks_Discharge\": 1, \"chunks_Examination\": 4, \"chunks_Clinical\": 1, \"chunks_LabExam\": 3}"}
2026-08-10 16:20:07,689 INFO     29 [Pipeline] Executing component [13]: ChunkMerger:Merger (type=ChunkMerger)
2026-08-10 16:20:07,690 INFO     29 [ChunkMerger] Merged 9 chunks from 9 sources: {'Extractor:LabExam': 3, 'Extractor:Imaging': 1, 'Extractor:Clinical': 1, 'Extractor:Medication': 1, 'Extractor:Prescription': 1, 'Extractor:Discharge': 1, 'Extractor:Admission': 1, 'Extractor:ExaminationReport': 4, 'Extractor:Progress': 1} (filtered 5 noise chunks)
2026-08-10 16:20:07,704 INFO     29 [Pipeline] Component [13]: ChunkMerger:Merger finished. error=None
2026-08-10 16:20:07,704 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | ChunkMerger:Merger | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 4}", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf"}
2026-08-10 16:20:07,704 INFO     29 [Pipeline] Executing component [14]: Tokenizer:MedEmbed (type=Tokenizer)
2026-08-10 16:20:07,959 INFO     29 [Tokenizer] KB=fb850778372011f195bd2a5fbb884e34, embd_model_config type=dict, vars={'id': 426, 'create_time': 1783580086926, 'create_date': datetime.datetime(2026, 7, 9, 6, 54, 46), 'update_time': 1786378441810, 'update_date': datetime.datetime(2026, 8, 10, 16, 14, 1), 'tenant_id': 'd0a4dc3a1a2511f1aeb02a5fbb884ed3', 'llm_factory': 'OpenAI-API-Compatible', 'model_type': 'embedding', 'llm_name': 'qwen3-embedding___OpenAI-API', 'api_key': 'sk-0Hi3n4FmayMInQT-CcH92A', 'api_base': 'https://futurefab-mind-gw.dev.futurefab.cn', 'max_tokens': 8192, 'used_tokens': 1213553, 'status': '1'}
2026-08-10 16:20:08,187 INFO     29 [EMBED-PIPELINE] batch[0:16] text_for_embed=   白细胞计数  WBC  4.2  10^9/L  3.5--9.5  False    中性粒细胞百分数  NEUT%  74.5  %  40--75  False    淋巴细胞百分数  LYMPH%  16.1  %  20--50  True    单核细胞百分数  MONO%  6.9  %  3--10  False    嗜酸性粒细胞百分数  EO%  1.7  %  0.4--8  False    嗜碱性粒细胞百分数  BASO%  0.8  %  0--1  False    中性粒细胞绝对值  NEUT#  3.1  10^9/L  1.8--6.3  False    淋巴细胞绝对值  LYMPH#  0.7  10^9/L  1.1--3.2  True    单核细胞绝对值  MONO#  0.3  10^9/L  0.1--0.6  False    嗜酸性粒细胞绝对值  EO#  0.07  10^9/L  0.02--0.52  False    嗜碱性粒细胞绝对值  BASO#  0.03  10^9/L  0--0.06  False    红细胞计数  RBC  4.01  10^12/L  3.8--5.1  False    血红蛋白量  HGB  126  g/L  115--150  False    红细胞压积  HCT  38.0  %  35--45  False    平均红细胞体积  MCV  94.7  fl  82--100  False    平均红细胞血红蛋白含量  MCH  31.4  pg  None  False    平均红细胞血红蛋白浓度  MCHC  332  g/L  None  False    红细胞体积分布宽度  RDW  13.6  %  None  False    血小板计数  PLT  179  10^9/L  None  False   
---
   丙氨酸氨基转移酶  None  50.3  U/L  7---40  True    天门冬氨酸氨基转移酶  None  35.4  U/L  13---35  True    碱性磷酸酶  None  43.2  U/L  50---135  True    γ-谷氨酰基转移酶  None  130.5  U/L  7---45  True    乳酸脱氢酶  None  193  U/L  120---250  False    总胆红素  None  10.2  umol/L  ≤21  False    直接胆红素  None  3.3  umol/L  ≤4  False    胆碱酯酶  None  8.8  KU/L  5.3---11.3  False    总蛋白  None  78.9  g/L  65---85  False    白蛋白  None  48.8  g/L  40---55  False    球蛋白  None  30.1  g/L  20---40  False    白/球比例  None  1.62  None  1.2---2.4  False    总胆汁酸  None  4.0  umol/L  0---13  False    亮氨酸氨肽酶  None  35.3  U/L  12---37  False    腺苷脱氨酶  None  21.3  U/L  0---25  False    葡萄糖  None  8.35  mmol/L  3.9---6.1  True    尿素  None  4.4  mmol/L  3.1---8.8  False    肌酐  None  73  umol/L  41---81  False    尿酸  None  221  umol/L  155---357  False    总二氧化碳  None  28.1  mmol/L  21---31  False    甘油三酯  None  2.88  mmol/L  ≤1.7  True    总胆固醇  None  5.81  mmol/L  3---5.7  True    H-脂蛋白胆固醇  None  1.26  mmol/L  1.03---1.55  False    L-脂蛋白胆固醇  None  3.66  mmol/L  健康人<3.4; 不同ASCVD危险人群目标值: 低危<3.4 中高危<2.6; 极高危<1.8 超高危<1.4  True    载脂蛋白A I  None  1.30  g/L  1---1.6  False    载脂蛋白B  None  1.15  g/L  0.6---1.1  True    总钙  None  2.46  mmol/L  2.11---2.52  False    磷  None  1.37  mmol/L  0.85---1.51  False    钾  None  4.18  mmol/L  3.5---5.3  False    钠  None  138.3  mmol/L  137---147  False    氯  None  101.7  mmol/L  99---110  False   
---
   C反应蛋白  None  11.2  mg/L  0---6  True    肌酸激酶  None  56  U/L  40---200  False    肌酸激酶MB同工酶  None  11  U/L  0---25  False    a 羟丁酸脱氢酶  None  120  U/L  59---126.4  False    eGFR (CKD-EPI)  eGFR  69.6  ml/min/1.73m^2  >90  True   
---
南京鼓楼医院
南京大学医学院附属鼓楼医院
互联网医院
门诊病历
姓名:
性别:女
年龄:75岁
ID:
预约挂号
2026年03月16日15时20分 (江北)心血管内科门诊
主诉:要求进行心功能分级
病史:患者平时正常活动不受限。
过敏史:无吸烟史
药物过敏史。无流行病学史
体查:
级)
诊断:
1.心功能I级(NYHA分
2.高脂血症
处理:随诊
1.非诺贝特胶囊(力平之)
200mg/粒
用法:1粒
口服
一次/日
x3盒 28天
医师:
齐
第1页
---
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号07床 姓名
住院号
姓名：
性别：女 年龄：75岁 婚姻：已婚 职业：农民
入院诊断：1. 肺恶性肿瘤（左肺，小细胞癌广泛期）2. 肥 入院日期： 2025年12月03日
厚型梗阻性心肌病 3. 纵隔淋巴结肿大 4. 肺门
淋巴结肿大 5. 锁骨上淋巴结肿大（双侧）6. 腋
下淋巴结肿大（右）7. 心功能III级（NYHA分级）
8. 甲状腺功能减退症 9. 高血压2级（极高
危）10. 肺气肿（局限性）11. 肺诊断性影像检
查的异常所见（肺结节）12. 二尖瓣反流（重度）
13. 心包积液（少量）14. 肾上腺结节（左侧）
手术名称：
手术日期：
出院诊断：1. 恶性肿瘤支持治疗 2. 恶性肿瘤免疫治 出院日期： 2025年12月06日
疗 3. 肺恶性肿瘤（左肺，小细胞癌广泛期）
4. 肥厚型梗阻性心肌病 5. 纵隔淋巴结肿大
6. 肺门淋巴结肿大 7. 锁骨上淋巴结肿大
(双侧) 8. 腋下淋巴结肿大(右) 9. 心功能
III级(NYHA分级) 10. 甲状腺功能减退症
11. 高血压2级（极高危）12. 肺气肿(局
限性) 13. 肺诊断性影像检查的异常所见(肺
结节) 14. 二尖瓣反流(重度) 15. 心包积
液(少量) 16. 肾上腺结节(左侧)
入院时情况（主要症状、体征，有关实验室及器械检查结果）：
患者因“咳嗽1月余”于2025-05-21至河北省人民医院就诊，查胸部CT：左肺下叶占位性病变，恶性不除
外，远端阻塞性肺炎，建议完善实验室检查及增强CT。双侧锁骨窝、右侧腋下、纵隔内及双肺门多发肿大
淋巴结，转移不除外。左侧胸膜结节样增厚，转移不除外。后于2025-05-23行肺穿刺活检术，术后病理回
示：（左肺）穿刺组织：结合免疫组化染色支持小细胞癌。免疫组化染色： CKpan (+)，Vimentin (-)，
CK7 (+)，TTF -1(+)，NapsinA (-)，CK5/6(-)，P40(-)，P63(-)，CgA (+)，Syn (+)，CD56(+)。根据患者病情
于2025-05-28当地医院行依托泊苷+卡铂方案化疗+斯鲁利单抗免疫治疗1周期，过程顺利。于
2025-06-19、2025-07-16开始行依托泊苷+卡铂化疗+斯鲁利单抗免疫治疗2周期，过程顺利。2025-07-27复
查血常规示血小板38×10^9/L。予升血小板治疗后。2025-08-13、2025-09-06、2025-10-08、2025-11-07
行依托泊苷化疗+斯鲁利单抗免疫治疗4周期，期间疗效评价PR。患者为求进一步治疗就诊我科，门诊拟
第 1 页
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号 姓名 住院号
“肺恶性肿瘤”收住入院。病程中，患者神志清，精神可，食纳睡眠可，二便如常，近期体重未见明显变
化。
诊疗经过：
患者入院完善相关检查：
【检验】
2025.12.03 12:22 甲功三项：*促甲状腺激素 34.210 mIU/L↑，*游离三碘甲状腺原氨酸 2.60 pmol/L↓，
*游离甲状腺素 9.58 pmol/L↓。
2025.12.03 12:22 肺癌六项（江北）：*细胞角蛋白19片段 3.61 ng/mL↑，*神经元特异性烯醇化酶
26.80 ng/mL↑，胃泌素释放肽前体 243.00 pg/mL↑。
2025.12.03 13:33 生化全套，心肌酶：*碱性磷酸酶 46.8 U/L↓，*葡萄糖 6.66 mmol/L↑，*甘油三酯
8.26 mmol/L↑，*总胆固醇 7.14 mmol/L↑，*H-脂蛋白胆固醇 0.90 mmol/L↓，*L-脂蛋白胆固醇 3.51
mmol/L↑，*载脂蛋白AⅠ 0.79 g/L↓，*载脂蛋白B 1.87 g/L↑，*钠 136.1 mmol/L↓，*氯 97.8
mmol/L↓，*α羟丁酸脱氢酶 158 U/L↑，eGFR(CKD-EPI) 77.2 ml/min/1.73m^2↓。
2025.12.03 14:45 血常规：淋巴细胞百分数 19.7 %↓，淋巴细胞绝对值 0.8 ×10^9/L↓，*红细胞计数
3.30 ×10^12/L↓，*血红蛋白量 108 g/L↓，*红细胞压积 31.8 %↓，红细胞体积分布宽度 15.4 %↑，*
血小板计数 112 ×10^9/L↓。
余未见明显异常。
【检查】
2025.12.04 15:19 心电图检查（江北）（检查）常规心电图 检查结论 窦性心律一度房室传导阻滞左前分支
阻滞异常Q波(V1、V2)左心室高电压ST-T改变QTc间期延长
2025.12.04 16:29（江北）PET/CT（检查）PET/CT全身显像 检查结论 1.“左肺癌化疗后复查”；①左下肺
门稍大伴葡萄糖代谢增高灶，内部通行支气管狭窄，结合病史考虑符合小细胞癌表现；②左肺下叶两枚软
组织结节，葡萄糖代谢异常增高；双肺门、纵隔、右侧腋窝多发肿大淋巴结，葡萄糖代谢显著增高；以上
考虑同侧肺内转移、多发淋巴结转移；2.双肺多发小结节，部分为磨玻璃结节，葡萄糖代谢未见增高，建
议胸部CT随诊；双肺散在条索及渗出；左肺下叶节段性肺不张；右肺局限性肺气肿；双侧胸膜增厚；3.左
肾上腺稍低密度结节，葡萄糖代谢未见异常增高，左肾上腺稍增粗，葡萄糖代谢轻度增高，倾向增生伴腺
瘤形成，请比对老片、密切随诊观察；4.腔隙性脑梗死可能；脑萎缩；副鼻窦炎症；甲状腺左右两叶密度
欠均，葡萄糖代谢增高，考虑炎性摄取增高，必要时请结合甲功、颈部超声随诊；5.心影偏大，冠状动脉
及胸部大血管管壁钙化；6.食管中下段管壁似稍增厚，葡萄糖代谢轻度增高，考虑炎性或生理性摄取可
能，必要时内镜检查；十二指肠憩室可能；轻度脂肪肝；肝囊肿；胆囊饱满；7.慢性膀胱炎症可能；盆腔
内钙化结节；8.颈椎生理性曲度变直，脊柱退变；右股骨下段低密度伴内部钙化，葡萄糖代谢不高，考虑
第 2 页
3/4
南京鼓楼医院
南京大学医学院附属鼓楼医院
出院记录
科别（江北）综合肿瘤中心 病区（江北）B7病区床号
姓名 住院号
良性灶如内生软骨瘤可能，随诊；右肩背部皮下稍低密度结节，葡萄糖代谢未见增高，考虑良性灶，随
诊。
【诊疗经过】
患者入院后完善PET-CT复查，病情较前基本相仿，暂无根治性放疗指征。排除禁忌后，患者于2025-12-05
行斯鲁利单抗免疫维持治疗1周期。现本周期静脉治疗已结束，现整体病情稳定，一般情况尚可，准予办理
出院。
出院情况： 好转
伤口愈合：-
ECOG 1分，NRS 0分，神志清，精神可，无贫血貌，全身皮肤巩膜无黄染。胸廓外形正常，无胸壁静脉曲
张。双侧呼吸运动对称，肋间隙：正常，触觉语颤：对称，皮下捻发感：无，双肺叩诊清音，双肺呼吸音
稍粗，两肺未闻及明显干湿啰音。心律齐，心脏各瓣膜区未闻及杂音。腹部平坦，腹部无压痛，无反跳
痛。双下肢无明显水肿。
出院医嘱：
1、注意天气变化，注意休息、低脂饮食，避免受凉，避免手足接触冰冷物体，注意皮肤保暖。
2、出院后继续用药
左甲状腺素钠片（优甲乐）50微克/片 1片 口服 QD（7点）（每天早餐前半小时服用1片，补充甲状腺激
素，内分泌科随诊调药）
3、定期复查血常规（每周1-2次）及生化全套（每周1次），如WBC<3.0×10^9/L、PLT<60×10^9/L或生化
全套指标异常，请及时当地医院就诊（如有急症或危急值报告，请及时就近正规医院急诊就诊），我科门
诊随诊。
4、下次治疗时间：3-4周左右，具体等电话通知。杨阳主任医师专家门诊时间：门诊时间：每周二、周五
上午，（周二本部，周五江北），（江北肿瘤科医生办公室电话：025-83106666转220717）。如需肿瘤日
间治疗，请提前一周至杨阳主任医师门诊预约。
5、不适门诊随诊。
不存在尚未回归的病理检查结果。
X光片号：-
CT号： P049684
MRI号：-
病理号：-
上级医师：
医师：
第 3 页
---
河北省人民医院
病理检查报告单
病理号
姓名:
性别:女
年龄:74岁
送检单位:本院
科别:胸外二科病区
住院号
床号:
送检日期:2025-05-23 16:44
送检材料:左肺穿刺数条:
临床诊断:左肺占位
图像:
大体检查:
(左肺穿刺数条:)穿刺组织3条,长共3cm,直径0.1cm。
病理诊断:
(左肺)穿刺组织:浸润性癌,类型待免疫组化助诊。
诊断医师:
郑国卿王彤彤
日期:2025-05-26 14:23
注:1.此报告仅供临床医师参考,如有异议请在两日内与诊断医师联系。电话:0311)85988183
2.国家规定小标本(咬检及穿刺组织)3个工作日内出报告;其余标本5个工作日内出报告(特殊处理标本除外)。
---
住院病历
河北省人民医院
病理检查补充报告单
病理号:
姓名:
性别: 女
年龄: 74岁
送检单位: 本院
科别: 胸外二科病区
住院号:
床号:
送检日期: 2025-05-23 16:44
送检材料: 左肺穿刺数条:
临床诊断: 左肺占位
补充病理诊断:
(左肺)穿刺组织: 结合免疫组化染色支持小细胞癌。
免疫组化染色: CKpan (+), Vimentin (-), CK7 (+), TTF-1 (+), NapsinA (-), CK5/6
(-), P40 (-), P63 (-), CgA (+), Syn (+), CD56 (+), Ki-67 (90%+)。
诊断医师: 康林 郑国娜
报告日期: 2025-05-27 16:
注: 此报告仅供临床医师参考, 如有异议或病情有新变化务请及时与病理诊断医师联系(电话: 85988409)
---
南京鼓楼医院云胶片
南京鼓楼医院
南京大学医学院附属鼓楼医院
影像检查诊断报告
互联网医院
电子影像
检查号:
患者类型: 住院
患者编号:
姓名:
性别: 女
年龄: 75岁
科别: (江北)综合肿瘤中心 病区: (江北)B7病区
病床:
检查日期: 2026-03-11 13:39:06
设备类型: CT
技师: 王雨晓
检查项目: [CT平扫+增强(颈部、胸部、上腹部、下腹部、盆腔)]
检查所见:
颈部软组织CT平扫+增强:
【所见咽部】所见咽腔结构对称,未见明显异常密度影。增强后未见明显异常强化。
【喉部及下咽部】喉腔结构对称,会厌、声带、梨状窝形态及密度未见明显异常。增强后未见
明显异常强化。
【甲状腺及甲状旁腺区】甲状腺左右叶大小、形态正常,甲状腺双叶低密度结节;甲状旁腺区
未见明显占位性病变。
【唾液腺】双侧腮腺、颌下腺形态密度未见明显异常。增强后未见明显异常强化。
【气管及食管】气管居中,管腔通畅;食管颈段管壁未见明显增厚。
【颈部间隙】脂肪间隙清晰,未见明显异常密度影。增强后未见明显异常强化。
【淋巴结】两侧锁骨上窝多发肿大淋巴结。
【其他】副鼻窦内低密度影。
胸部CT平扫+增强:
【肺野】两肺野纹理清晰,左肺下叶见斑片状高密度影。右肺上叶舌段小片状高密度影。两肺
多发结节,较大者:右肺上叶(Img79)见一实性结节影,大小约5mm×3mm。两肺索条及片絮影;右
肺上叶局部透亮区。
【肺门】双肺门多发肿大淋巴结,大者位于左侧,短径约20mm,增强后强化不均。
【气管及支气管】左下肺支气管闭塞伴阻塞性炎症,病灶周围结节影。
【纵隔】纵隔居中,纵隔内多发肿大淋巴结,较大者短径约20mm。
【心脏及大血管】心影增大;主动脉及冠状动脉壁见致密影。
【胸膜及胸腔】胸膜:两侧胸膜可见增厚;胸腔积液:否。增强后未见明显异常强化。
【膈肌】光整,未见明显异常抬高。增强后未见明显异常强化。
【胸壁】胸廓对称,骨质未见明显异常。增强后未见明显异常强化。
上腹部、下腹部、盆腔CT平扫+增强:
报告日期: 2026-03-11 15:35:37
诊断医师: 申欣怡
/ 申欣怡
审核日期: 2026-03-12 13:17:06
审核医师: 王国
（本报告仅供临床医生参考）
---
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
报告 2025-10-08
影像描述
颈部软组织CT平扫+增强：
【所见咽部】所见咽腔结构对称，未见明显异常
密度影。增强后未见明显异常强化。
【喉部及下咽部】喉腔结构对称，会厌、声带、
梨状窝形态及密度未见明显异常。增强后未见明显
异常强化。
【甲状腺及甲状旁腺区】甲状腺左右叶大小、形
态正常，甲状腺双叶低密度结节；甲状旁腺区未见
明显占位性病变。
【唾液腺】双侧腮腺、颌下腺形态密度未见明显
异常。增强后未见明显异常强化。
【气管及食管】气管居中，管腔通畅；食管颈段
管壁未见明显增厚。
【颈部间隙】脂肪间隙清晰，未见明显异常密度
影。增强后未见明显异常强化。
【淋巴结】未见明显肿大淋巴结。
【其他】副鼻窦内低密度影。
胸部CT平扫+增强：
【肺野】两肺野纹理清晰，左肺下叶见斑片状高
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
【肺野】两肺野纹理清晰，左肺下叶见斑片状高
密度影。两肺多发结节，较大者：右肺上叶（Img7
9）见一实性结节影，大小约5mm×3mm。两肺索
条及片絮影；右肺上叶局部透亮区。
【肺门】双肺门多发小淋巴结，部分稍大。
【气管及支气管】左下肺支气管闭塞伴阻塞性炎
症，病灶周围结节影。
【纵隔】纵隔居中，纵隔内多发小淋巴结，部分
稍大，较大者短径约10mm。
【心脏及大血管】心影增大；主动脉及冠状动
脉壁见致密影。
【胸膜及胸腔】胸膜：两侧胸膜可见增厚；胸腔
积液：否。增强后未见明显异常强化。
【膈肌】光整，未见明显异常抬高。增强后未见
明显异常强化。
【胸壁】胸廓对称，骨质未见明显异常。增强后
未见明显异常强化。
上腹部CT平扫+增强：
【肝脏】各叶比例在正常范围内，外形轮廓规
则，肝内小圆形无强化低密度影，较大者长径约6
mm。静脉期肝左叶小片状稍低密度影（薄层im29
0）。
【胆囊及胆管】胆囊形态、大小正常，囊壁未见
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
【胆囊及胆管】胆囊形态、大小正常，囊壁未见
增厚，囊内未见明显异常密度影；肝内外胆管轻度
扩张。
【胰腺】形态、大小正常，实质内未见明显异常
密度影；胰管未见明显扩张。增强后未见明显异常
强化。
【脾脏】形态、大小正常，实质内未见明显异常
密度影。增强后未见明显异常强化。
【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均
匀，未见明显肿大淋巴结，未见明显渗出及积液。
增强后未见明显异常强化。
下腹部CT平扫+增强：
【肾脏】两侧肾脏大小、形态、位置正常，右肾
窦点状致密影；肾盂肾盏未见明显扩张。增强后未
见明显异常强化。
【肾上腺】双肾上腺增粗，左肾上腺低密度结
节，长径约12mm,可见强化。
【腹膜腔及腹膜后】结构清晰，脂肪间隙密度均
匀，未见明显肿大淋巴结，未见明显渗出及积液。
增强后未见明显异常强化。
盆腔CT平扫+增强：
【膀胱】充盈欠佳，壁未见明显增厚，其内未见
明显异常密度影。增强后未见明显异常强化。
【子宫及附件】子宫呈肌组织结构性空扫
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
南京鼓楼医院云胶片
女/75岁
设备类型 CT 患者类型 无
检查项目 [CT平扫+增强（颈部、胸部、上腹部、下
腹部、盆腔）]
PDF报告 图像 分享
诊断意见
1.肺癌复查：左肺下叶斑片影较前（2025-07-15）
明显缩小，左下肺支气管闭塞伴阻塞性炎症，较前
缓解，密切随诊；双侧纵隔内及双肺门多发稍大淋
巴结，部分较前稍缩小。
2.两肺多发结节，较前变化不大，密切随诊。
3.两侧胸膜增厚；两肺索条及炎性渗出，较前缓
解；右肺上叶局限性肺气肿。
4.心影增大；主动脉及冠状动脉壁钙化。
5.肝脏小囊肿；静脉期肝左叶小片状稍低密度影
（薄层im290），较前相仿，随诊。
6.肝内外胆管轻度扩张。
7.双肾上腺增粗，左肾上腺腺瘤可能，结合专科检
查；右肾小结石。
8.子宫肌瘤可能，结合妇科超声；盆腔内钙化结
节。
9.下腹腔内肠系膜间隙多发稍大淋巴结。
10.食管下段壁轻度增厚；乙状结肠迂曲冗长；结肠
内容物多；十二指肠降部憩室；结合临床体征随
诊。
11.右肩部皮下低密度结节，较前相仿，随诊；L4及
以上椎体I°滑脱。
移动影像浏览
© 2022 南京鼓楼医院影像云平台 V1.0
2026-08-10 16:20:08,996 INFO     29 [Pipeline] Component [14]: Tokenizer:MedEmbed finished. error=None
2026-08-10 16:20:08,996 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Tokenizer:MedEmbed | outputs={"output_format": "chunks", "chunks": "9 items, types={'LabReport': 3, 'OutpatientRecord': 1, 'DischargeRecord': 1, 'ExaminationReport': 4}", "name": "徐州-LIYE-小肺-方穹推荐706-Ia期.pdf", "embedding_token_consumption": 7346}
2026-08-10 16:20:08,996 INFO     29 [Pipeline] Executing component [15]: Invoke:SyncChunks (type=Invoke)
2026-08-10 16:20:09,206 INFO     29 [Pipeline] Component [15]: Invoke:SyncChunks finished. error=None
2026-08-10 16:20:09,206 INFO     29 [Trace] task=7f4c3712 | doc=徐州-LIYE-小肺-方穹推荐706-Ia期.pdf | Invoke:SyncChunks | outputs={"result": "{\"status\":\"ok\",\"synced_chunks\":9,\"skipped_hallucinated\":0,\"failed\":[]}"}
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int len=19 row[0]=(13, 122, 178, 197, 207) row[-1]=(13, 436, 492, 238, 248)
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int len=31 row[0]=(14, 256, 303, 111, 117) row[-1]=(14, 429, 437, 233, 239)
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int len=5 row[0]=(14, 256, 283, 364, 370) row[-1]=(14, 256, 292, 397, 403)
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,211 INFO     29 [DIAG-EXECUTOR] row_position_int is empty
2026-08-10 16:20:09,216 INFO     29 set_progress(7f4c371294d611f1bd9827cf206dfa2d), progress: 0.82, progress_msg: 16:20:09 [DOC Engine]:
Start to index...
2026-08-10 16:20:09,242 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.017s]
2026-08-10 16:20:09,246 INFO     29 set_progress(7f4c371294d611f1bd9827cf206dfa2d), progress: 0.8111111111111111, progress_msg: 
2026-08-10 16:20:09,269 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 16:20:09,284 INFO     29 PUT http://ragflow-dev-elasticsearch:9200/ragflow_d0a4dc3a1a2511f1aeb02a5fbb884ed3/_bulk?refresh=false&timeout=60s [status:200 duration:0.010s]
2026-08-10 16:20:09,291 INFO     29 set_progress(7f4c371294d611f1bd9827cf206dfa2d), progress: 1.0, progress_msg: 16:20:09 Indexing done (0.08s). Task done (347.00s)
2026-08-10 16:20:09,295 INFO     29 [Done], chunks(9), token(7346), elapsed:347.00
2026-08-10 16:20:09,480 INFO     29 handle_task done for task {"id": "7f4c371294d611f1bd9827cf206dfa2d", "doc_id": "7f1b076e94d611f1bd9827cf206dfa2d", "from_page": 0, "to_page": 100000000, "retry_count": 0, "kb_id": "fb850778372011f195bd2a5fbb884e34", "parser_id": "pipeline", "parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "name": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "type": "pdf", "location": "\u5f90\u5dde-LIYE-\u5c0f\u80ba-\u65b9\u7a79\u63a8\u8350706-Ia\u671f.pdf", "size": 2872089, "tenant_id": "d0a4dc3a1a2511f1aeb02a5fbb884ed3", "language": "English", "embd_id": "qwen3-embedding___OpenAI-API@OpenAI-API-Compatible", "pagerank": 0, "kb_parser_config": {"table_context_size": 0, "image_context_size": 0, "layout_recognize": "paddleocr-vl-1.5@PaddleOCR", "chunk_token_num": 512, "delimiter": "\n", "auto_keywords": 0, "auto_questions": 0, "html4excel": false, "topn_tags": 3, "raptor": {"use_raptor": true, "prompt": "Please summarize the following paragraphs. Be careful with the numbers, do not make things up. Paragraphs as following:\n      {cluster_content}\nThe above is the content you need to summarize.", "max_token": 256, "threshold": 0.1, "max_cluster": 64, "random_seed": 0}, "graphrag": {"use_graphrag": true, "entity_types": ["organization", "person", "geo", "event", "category"], "method": "light"}, "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "pipeline_id": "3e691ee797c2475da2ecc905e25de3fc"}, "img2txt_id": "qwen3-vl-plus@Tongyi-Qianwen", "asr_id": "qwen3-asr-flash-2025-09-08@Tongyi-Qianwen", "llm_id": "deepseek-v3.2@Tongyi-Qianwen", "update_time": 1786378440484, "task_type": "dataflow", "root_trace_id": "682440c36589451eae47176e464371f6", "root_traceparent": "00-682440c36589451eae47176e464371f6-fbeaf5b2187fd846-01", "trace_source": "traceparent", "dataflow_id": "3be6fcd058ce11f1ab13b5606b24de97"}
```
