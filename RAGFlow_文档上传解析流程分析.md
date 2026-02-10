# RAGFlow 文档上传解析流程深度分析

## 执行摘要

**核心结论：RAGFlow 采用混合并行架构**

- ✅ **任务级并行**：多个文档可以并行处理（通过 Redis 队列 + 多个 worker）
- ✅ **页面级并行**：单个 PDF 文档的不同页面范围可以并行处理
- ✅ **图片处理并行**：文档内的多个图片使用 ThreadPoolExecutor 并行处理
- ✅ **Embedding 批量并行**：向量化使用批处理，但批次内是串行的
- ⚠️ **Chunk 构建串行**：单个任务的 chunk 构建过程是串行的（受 semaphore 限制）

---

## 1. 文档上传入口分析

### 1.1 上传 API 入口

**文件**：`api/apps/document_app.py`

```python
# 第 52-85 行
@manager.route("/upload", methods=["POST"])
@login_required
@validate_request("kb_id")
async def upload():
    # ... 省略验证代码 ...

    # 关键：使用 asyncio.to_thread 在线程池中执行上传
    err, files = await asyncio.to_thread(
        FileService.upload_document, kb, file_objs, current_user.id
    )

    return get_json_result(data=files)
```

**分析**：
- 上传接口本身是异步的（`async def`）
- 但实际上传逻辑在同步线程中执行（`asyncio.to_thread`）
- **多个文件的上传是串行处理的**（见下文）

### 1.2 文件上传实现

**文件**：`api/db/services/file_service.py` 第 431-488 行

```python
def upload_document(self, kb, file_objs, user_id, src="local", parent_path: str | None = None):
    # ... 初始化代码 ...

    err, files = [], []
    # 关键：使用 for 循环串行处理每个文件
    for file in file_objs:
        try:
            # 1. 检查文件健康度
            DocumentService.check_doc_health(kb.tenant_id, file.filename)

            # 2. 读取文件内容
            blob = file.read()

            # 3. 上传到 MinIO
            settings.STORAGE_IMPL.put(kb.id, location, blob)

            # 4. 创建文档记录
            DocumentService.insert(doc)

            files.append((doc, blob))
        except Exception as e:
            err.append(file.filename + ": " + str(e))

    return err, files
```

**结论**：
- ❌ **文件上传是串行的**：使用 `for` 循环逐个处理
- 上传 100 个文件需要等待每个文件依次完成
- 没有使用 `asyncio.gather()` 或并行机制

---

## 2. 文档解析任务队列

### 2.1 任务创建

**文件**：`api/db/services/document_service.py` 第 1047-1066 行

```python
@classmethod
def run(cls, tenant_id:str, doc:dict, kb_table_num_map:dict):
    from api.db.services.task_service import queue_dataflow, queue_tasks

    doc["tenant_id"] = tenant_id

    if doc.get("pipeline_id", ""):
        # 使用 Pipeline 处理
        queue_dataflow(tenant_id, flow_id=doc["pipeline_id"],
                      task_id=get_uuid(), doc_id=doc["id"])
    else:
        # 使用传统 Parser 处理
        bucket, name = File2DocumentService.get_storage_address(doc_id=doc["id"])
        queue_tasks(doc, bucket, name, 0)
```

### 2.2 任务分片策略

**文件**：`api/db/services/task_service.py` 第 333-437 行

```python
def queue_tasks(doc: dict, bucket: str, name: str, priority: int):
    parse_task_array = []

    # PDF 文档：按页面范围分片
    if doc["type"] == FileType.PDF.value:
        file_bin = settings.STORAGE_IMPL.get(bucket, name)
        pages = PdfParser.total_page_number(doc["name"], file_bin)
        page_size = doc["parser_config"].get("task_page_size") or 12

        # 关键：将 PDF 分成多个任务
        for s, e in page_ranges:
            for p in range(s, e, page_size):
                task = new_task()
                task["from_page"] = p
                task["to_page"] = min(p + page_size, e)
                parse_task_array.append(task)

    # Excel 文档：按行范围分片
    elif doc["parser_id"] == "table":
        rn = RAGFlowExcelParser.row_number(doc["name"], file_bin)
        for i in range(0, rn, 3000):
            task = new_task()
            task["from_page"] = i
            task["to_page"] = min(i + 3000, rn)
            parse_task_array.append(task)

    # 其他文档：单个任务
    else:
        parse_task_array.append(new_task())

    # 将任务插入数据库
    bulk_insert_into_db(Task, parse_task_array, True)

    # 将任务推送到 Redis 队列
    for unfinished_task in unfinished_task_array:
        REDIS_CONN.queue_product(
            settings.get_svr_queue_name(priority),
            message=unfinished_task
        )
```

**结论**：
- ✅ **支持任务级并行**：大文档被分成多个任务
- ✅ **任务通过 Redis 队列分发**：多个 worker 可以并行消费
- PDF 默认每 12 页一个任务（可配置）
- Excel 默认每 3000 行一个任务

---

## 3. 任务执行器（Task Executor）

### 3.1 并发控制

**文件**：`rag/svr/task_executor.py` 第 115-124 行

```python
# 并发控制参数（环境变量可配置）
MAX_CONCURRENT_TASKS = int(os.environ.get('MAX_CONCURRENT_TASKS', "5"))
MAX_CONCURRENT_CHUNK_BUILDERS = int(os.environ.get('MAX_CONCURRENT_CHUNK_BUILDERS', "1"))
MAX_CONCURRENT_MINIO = int(os.environ.get('MAX_CONCURRENT_MINIO', '10'))

# 使用 asyncio.Semaphore 控制并发
task_limiter = asyncio.Semaphore(MAX_CONCURRENT_TASKS)
chunk_limiter = asyncio.Semaphore(MAX_CONCURRENT_CHUNK_BUILDERS)
embed_limiter = asyncio.Semaphore(MAX_CONCURRENT_CHUNK_BUILDERS)
minio_limiter = asyncio.Semaphore(MAX_CONCURRENT_MINIO)
kg_limiter = asyncio.Semaphore(2)
```

**分析**：
- ✅ **任务级并发**：最多 5 个任务并行执行（默认）
- ⚠️ **Chunk 构建限制**：同时只能有 1 个任务在构建 chunks（默认）
- ✅ **MinIO 操作并发**：最多 10 个并发 MinIO 操作

### 3.2 主循环

**文件**：`rag/svr/task_executor.py` 第 1251-1303 行

```python
async def main():
    # ... 初始化代码 ...

    tasks = []
    try:
        while not stop_event.is_set():
            # 获取 semaphore 许可
            await task_limiter.acquire()

            # 创建异步任务
            t = asyncio.create_task(task_manager())
            tasks.append(t)
    finally:
        # 清理任务
        for t in tasks:
            t.cancel()
        await asyncio.gather(*tasks, return_exceptions=True)
```

**结论**：
- ✅ **使用 asyncio 并发模型**：多个任务可以并行执行
- ✅ **动态任务创建**：不断从 Redis 队列拉取新任务
- 受 `task_limiter` 限制，最多 5 个并发任务

---

## 4. Chunk 构建流程

### 4.1 Chunk 构建入口

**文件**：`rag/svr/task_executor.py` 第 235-280 行

```python
@timeout(60 * 80, 1)
async def build_chunks(task, progress_callback):
    # 1. 从 MinIO 获取文件
    bucket, name = File2DocumentService.get_storage_address(doc_id=task["doc_id"])
    binary = await get_storage_binary(bucket, name)

    # 2. 使用 chunk_limiter 限制并发
    async with chunk_limiter:
        # 在线程池中执行 chunk 操作（同步代码）
        cks = await asyncio.to_thread(
            chunker.chunk,
            task["name"],
            binary=binary,
            from_page=task["from_page"],
            to_page=task["to_page"],
            lang=task["language"],
            callback=progress_callback,
            kb_id=task["kb_id"],
            parser_config=task["parser_config"],
            tenant_id=task["tenant_id"],
        )

    # 3. 并行上传图片到 MinIO
    tasks = []
    for ck in cks:
        tasks.append(asyncio.create_task(upload_to_minio(doc, ck)))

    # 使用 asyncio.gather 并行执行
    await asyncio.gather(*tasks, return_exceptions=False)

    return cks
```

**分析**：
- ⚠️ **Chunk 构建串行**：`chunk_limiter` 默认为 1，同时只能有一个任务在构建 chunks
- ✅ **图片上传并行**：使用 `asyncio.gather()` 并行上传所有图片
- `chunker.chunk()` 本身是同步代码，在线程池中执行

### 4.2 Parser 实现

**文件**：`rag/app/naive.py` 第 730-900 行（简化）

```python
def chunk(filename, binary=None, from_page=0, to_page=100000,
          lang="Chinese", callback=None, **kwargs):
    # 1. 解析文档（PDF/DOCX/Excel 等）
    if re.search(r"\.pdf$", filename, re.IGNORECASE):
        sections, tables, pdf_parser = parse_pdf(...)
    elif re.search(r"\.docx$", filename, re.IGNORECASE):
        sections, tables = parse_docx(...)
    # ... 其他格式 ...

    # 2. 处理图片和表格（可能使用 Vision 模型）
    tables = vision_figure_parser_pdf_wrapper(
        tbls=tables,
        callback=callback,
        **kwargs
    )

    # 3. 合并文本和图片
    chunks = naive_merge_with_images(sections, tables, ...)

    # 4. Tokenize
    chunks = tokenize_chunks(chunks, ...)

    return chunks
```

**结论**：
- ❌ **单个任务的 chunk 构建是串行的**
- 但多个任务可以并行执行（受 `task_limiter` 限制）

---

## 5. 图片处理并行化

### 5.1 Vision Figure Parser

**文件**：`deepdoc/parser/figure_parser.py` 第 109-178 行

```python
# 共享线程池（10 个 worker）
shared_executor = ThreadPoolExecutor(max_workers=10)

class VisionFigureParser:
    def __call__(self, **kwargs):
        callback = kwargs.get("callback", lambda prog, msg: None)

        @timeout(30, 3)
        def process(figure_idx, figure_binary):
            # 使用 Vision 模型处理图片
            description_text = picture_vision_llm_chunk(
                binary=figure_binary,
                vision_model=self.vision_model,
                prompt=vision_llm_figure_describe_prompt(),
                callback=callback,
            )
            return figure_idx, description_text

        # 关键：使用 ThreadPoolExecutor 并行处理所有图片
        futures = []
        for idx, img_binary in enumerate(self.figures or []):
            futures.append(shared_executor.submit(process, idx, img_binary))

        # 等待所有图片处理完成
        for future in as_completed(futures):
            figure_num, txt = future.result()
            if txt:
                self.descriptions[figure_num] = txt + "\n".join(
                    self.descriptions[figure_num]
                )

        return self.assembled
```

**结论**：
- ✅ **图片处理完全并行**：使用 `ThreadPoolExecutor` 并行处理
- 最多 10 个图片同时处理
- 使用 `as_completed()` 等待所有任务完成

---

## 6. Embedding 向量化

### 6.1 Embedding 实现

**文件**：`rag/svr/task_executor.py` 第 546-597 行

```python
async def embedding(docs, mdl, parser_config=None, callback=None):
    # 1. 准备文本
    tts, cnts = [], []
    for d in docs:
        tts.append(d.get("docnm_kwd", "Title"))
        c = d["content_with_weight"]
        cnts.append(c)

    # 2. 编码标题（只编码一次，然后复制）
    vts, c = await asyncio.to_thread(mdl.encode, tts[0:1])
    tts = np.tile(vts[0], (len(cnts), 1))

    # 3. 批量编码内容
    @timeout(60)
    def batch_encode(txts):
        return mdl.encode([truncate(c, mdl.max_length - 10) for c in txts])

    cnts_ = np.array([])
    # 关键：按批次处理，但批次之间是串行的
    for i in range(0, len(cnts), settings.EMBEDDING_BATCH_SIZE):
        async with embed_limiter:
            vts, c = await asyncio.to_thread(
                batch_encode,
                cnts[i: i + settings.EMBEDDING_BATCH_SIZE]
            )
        if len(cnts_) == 0:
            cnts_ = vts
        else:
            cnts_ = np.concatenate((cnts_, vts), axis=0)
        tk_count += c
        callback(prog=0.7 + 0.2 * (i + 1) / len(cnts), msg="")

    # 4. 合并标题和内容向量
    filename_embd_weight = parser_config.get("filename_embd_weight", 0.1)
    title_w = float(filename_embd_weight)
    vects = title_w * tts + (1 - title_w) * cnts

    # 5. 将向量添加到文档
    for i, d in enumerate(docs):
        v = vects[i].tolist()
        d["q_%d_vec" % len(v)] = v

    return tk_count, vector_size
```

**分析**：
- ⚠️ **批次串行处理**：使用 `for` 循环逐批处理
- ✅ **批内并行**：`mdl.encode()` 内部可能使用 GPU 并行
- ✅ **使用 embed_limiter**：防止过多并发导致 OOM
- 批次大小由 `settings.EMBEDDING_BATCH_SIZE` 控制

---

## 7. 性能分析

### 7.1 处理 100 页 PDF 的时间估算

假设：
- 每页 OCR + 解析：2 秒
- 每页 Chunk 构建：0.5 秒
- 每个 Chunk Embedding：0.1 秒
- 平均每页 5 个 Chunks

#### 场景 1：完全串行（最坏情况）
```
总时间 = 100 页 × (2s OCR + 0.5s Chunk + 5 × 0.1s Embedding)
       = 100 × 3s
       = 300 秒 = 5 分钟
```

#### 场景 2：任务级并行（实际情况）
```
任务数 = 100 页 / 12 页/任务 = 9 个任务
并发数 = min(9, MAX_CONCURRENT_TASKS) = 5

每个任务时间 = 12 页 × 3s = 36 秒
总时间 = ceil(9 / 5) × 36s = 2 × 36s = 72 秒 ≈ 1.2 分钟
```

#### 场景 3：优化后（理论最优）
```
如果 chunk_limiter = 5（而不是 1）：
总时间 = ceil(9 / 5) × 36s / 5 = 15 秒
```

### 7.2 瓶颈分析

| 阶段 | 并行度 | 瓶颈 | 优化建议 |
|------|--------|------|----------|
| 文件上传 | ❌ 串行 | `for` 循环 | 使用 `asyncio.gather()` |
| 任务分发 | ✅ 并行 | Redis 队列 | 增加 worker 数量 |
| Chunk 构建 | ⚠️ 受限 | `chunk_limiter=1` | 增加到 3-5 |
| 图片处理 | ✅ 并行 | ThreadPoolExecutor | 已优化 |
| Embedding | ⚠️ 批次串行 | `for` 循环 | 使用 `asyncio.gather()` |
| MinIO 上传 | ✅ 并行 | `asyncio.gather()` | 已优化 |

---

## 8. 代码证据总结

### 8.1 串行证据

1. **文件上传串行**（`file_service.py:441`）：
```python
for file in file_objs:  # ❌ 串行
    blob = file.read()
    settings.STORAGE_IMPL.put(kb.id, location, blob)
```

2. **Chunk 构建受限**（`task_executor.py:261`）：
```python
async with chunk_limiter:  # ⚠️ 默认只允许 1 个并发
    cks = await asyncio.to_thread(chunker.chunk, ...)
```

3. **Embedding 批次串行**（`task_executor.py:572`）：
```python
for i in range(0, len(cnts), BATCH_SIZE):  # ⚠️ 批次串行
    async with embed_limiter:
        vts = await asyncio.to_thread(batch_encode, cnts[i:i+BATCH_SIZE])
```

### 8.2 并行证据

1. **任务级并行**（`task_executor.py:1293`）：
```python
while not stop_event.is_set():
    await task_limiter.acquire()  # ✅ 最多 5 个并发任务
    t = asyncio.create_task(task_manager())
```

2. **图片处理并行**（`figure_parser.py:168`）：
```python
futures = []
for idx, img_binary in enumerate(self.figures):
    futures.append(shared_executor.submit(process, idx, img_binary))  # ✅ 并行
```

3. **MinIO 上传并行**（`task_executor.py:314`）：
```python
tasks = []
for ck in cks:
    tasks.append(asyncio.create_task(upload_to_minio(doc, ck)))
await asyncio.gather(*tasks)  # ✅ 并行
```

---

## 9. 优化建议

### 9.1 短期优化（配置调整）

```bash
# 增加并发任务数
export MAX_CONCURRENT_TASKS=10

# 增加 Chunk 构建并发
export MAX_CONCURRENT_CHUNK_BUILDERS=3

# 增加 MinIO 并发
export MAX_CONCURRENT_MINIO=20
```

### 9.2 中期优化（代码改进）

1. **并行化文件上传**：
```python
# 修改 file_service.py:441
async def upload_document_parallel(self, kb, file_objs, user_id):
    tasks = []
    for file in file_objs:
        tasks.append(asyncio.create_task(self._upload_single_file(kb, file, user_id)))
    results = await asyncio.gather(*tasks, return_exceptions=True)
    return results
```

2. **并行化 Embedding 批次**：
```python
# 修改 task_executor.py:572
async def embedding_parallel(docs, mdl, parser_config=None):
    tasks = []
    for i in range(0, len(cnts), BATCH_SIZE):
        tasks.append(asyncio.create_task(
            asyncio.to_thread(batch_encode, cnts[i:i+BATCH_SIZE])
        ))
    results = await asyncio.gather(*tasks)
    return results
```

### 9.3 长期优化（架构改进）

1. **使用 Celery 或 Ray**：替代 Redis 队列，提供更强大的分布式任务调度
2. **GPU 批处理优化**：将多个文档的 Embedding 合并到一个 GPU 批次
3. **流式处理**：边解析边 Embedding，减少等待时间
4. **缓存机制**：缓存已处理的图片和 Embedding 结果

---

## 10. 总结

### 10.1 明确结论

**RAGFlow 原有能力：混合并行架构**

- ✅ **任务级并行**：多个文档/页面范围可以并行处理
- ✅ **图片处理并行**：使用 ThreadPoolExecutor
- ⚠️ **Chunk 构建受限**：默认只允许 1 个并发（可配置）
- ⚠️ **Embedding 批次串行**：批次之间是串行的
- ❌ **文件上传串行**：使用 `for` 循环

### 10.2 性能预估

| 场景 | 文档数 | 预估时间 | 瓶颈 |
|------|--------|----------|------|
| 单个 100 页 PDF | 1 | 1-2 分钟 | Chunk 构建 |
| 10 个 10 页 PDF | 10 | 2-3 分钟 | 任务并发数 |
| 100 个 1 页 PDF | 100 | 5-10 分钟 | 文件上传 + 任务调度 |

### 10.3 优化空间

- **立即可行**：调整环境变量（`MAX_CONCURRENT_TASKS`, `MAX_CONCURRENT_CHUNK_BUILDERS`）
- **短期改进**：并行化文件上传和 Embedding 批次
- **长期规划**：引入更强大的分布式任务调度框架

---

## 附录：关键配置参数

```python
# rag/svr/task_executor.py
MAX_CONCURRENT_TASKS = 5              # 最大并发任务数
MAX_CONCURRENT_CHUNK_BUILDERS = 1     # 最大并发 Chunk 构建数
MAX_CONCURRENT_MINIO = 10             # 最大并发 MinIO 操作数

# api/db/services/task_service.py
page_size = 12                        # PDF 每个任务的页数
excel_row_size = 3000                 # Excel 每个任务的行数

# deepdoc/parser/figure_parser.py
shared_executor = ThreadPoolExecutor(max_workers=10)  # 图片处理线程池

# settings
EMBEDDING_BATCH_SIZE = 32             # Embedding 批次大小
```

---

**文档版本**：v1.0
**生成时间**：2026-02-04
**分析基于**：RAGFlow 主分支代码
