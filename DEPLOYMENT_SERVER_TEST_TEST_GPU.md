# RAGFlow 启动部署方案（172.16.1.116：test / test_gpu）

> **作者：** Architect（云峰）  
> **日期：** 2026-02-28（基于现有部署方案重构，增加方案 A 部署章节）  
> **状态：** Draft（待交叉 Review）

适用范围：只针对服务器 `172.16.1.116` 上的两套环境 `test`(CPU) 与 `test_gpu`(GPU) 的启动/停止/验收。

---

## 安全边界

- 不操作他人目录：例如 `/data/yugasun/ragflow`。
- 不操作他人容器：例如 `docker-ragflow-gpu-1`。
- 停启只允许按 **PID 文件** 精准停止当前环境的进程，不做全局 `pkill/grep` 扫杀。

## 目录与端口

| 环境 | 代码目录 | API 端口 | Web 端口 |
|:---|:---|:---|:---|
| CPU `test` | `/data/kca/ragflow` | 29380 | 29080 |
| GPU `test_gpu` | `/data/kca/ragflow_gpu` | 29480 | 29180 |

访问地址：
- CPU test：`http://172.16.1.116:29080/`（Web），`http://172.16.1.116:29380/v1/system/healthz`（API）
- GPU test_gpu：`http://172.16.1.116:29180/`（Web），`http://172.16.1.116:29480/v1/system/healthz`（API）

## 配置选择规则

启动/停止必须显式指定其一：
- `RAGFLOW_ENV=<env>`（推荐）
- 或 `RAGFLOW_CONF=<yaml>`（高级用法）

可选本地覆盖（一般放密码等敏感信息）：
- `conf/local.service_conf.<env>.yaml`

## 存储引擎复用

`test_gpu` 只隔离端口与算力，存储与 `test` 完全一致（**数据共享**，`test_gpu` 的操作会影响 `test` 的数据）。

| 组件 | 配置 |
|:---|:---|
| Postgres | 同库 `ragflow_test` |
| Redis | 同 `db=13` |
| MinIO | 同 `bucket=ragflow-test` + `prefix_path=test` |
| Elasticsearch | 同 `http://localhost:21200` |

## GPU 使用约束

- **GPU 4-7 已被 VLLM 进程占用（不要动）**
- `test_gpu` 使用 GPU 0-3
- 支持两种 task 分配模式：
  - **4-task 模式**（轻量）：`WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3` — 4 个 task 分别绑定 4 张卡
  - **32-task 模式**（生产）：`WS=32 TASK_CUDA_VISIBLE_DEVICES_LIST="0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3"` — 32 个 task 实例，每 4 个一轮绑定 GPU 0/1/2/3（即 Task 0→GPU0, Task 1→GPU1, ..., Task 4→GPU0, Task 5→GPU1, ...）

## 一键启动（推荐）

### 启动 CPU test

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow
RAGFLOW_ENV=test WS=2 START_FRONTEND=1 bash start_all.sh
```

### 启动 GPU test_gpu（4-task 轻量模式）

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow_gpu
RAGFLOW_ENV=test_gpu WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3 WEB_PORT=29180 START_FRONTEND=1 bash start_all.sh
```

### 启动 GPU test_gpu（32-task 生产模式）

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow_gpu
RAGFLOW_ENV=test_gpu \
WS=32 \
TASK_CUDA_VISIBLE_DEVICES_LIST="0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3" \
WEB_PORT=29180 \
START_FRONTEND=1 \
bash start_all.sh
```

**参数说明：**
- `WS=32`：启动 32 个 task executor 实例（编号 0-31）
- `TASK_CUDA_VISIBLE_DEVICES_LIST`：32 个元素，`"0,1,2,3"` 重复 8 遍，每个 task 绑定对应 GPU
- `WEB_PORT=29180`：前端 nginx 端口
- `START_FRONTEND=1`：同时启动前端服务

## 停止（按 PID 精准停止）

### 停止 CPU test

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow
STOP_FRONTEND=1 RAGFLOW_ENV=test bash stop_all.sh
```

### 停止 GPU test_gpu

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow_gpu
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh
```

## 分步启动（需要时）

只启动后端（API + task）：
```bash
RAGFLOW_ENV=test_gpu WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3 bash start_backend.sh
```

只启动前端（docker nginx，含 build）：
```bash
RAGFLOW_ENV=test_gpu WEB_PORT=29180 bash start_frontend.sh
```

## 客观验收（必须做）

### 1) 健康检查
```bash
curl -sS -i http://127.0.0.1:29480/v1/system/healthz | head
curl -sS -I http://127.0.0.1:29180/ | head
```

### 2) 进程与 PID 文件
```bash
ls -la /data/kca/ragflow_gpu/run/pids/test_gpu/
cat /data/kca/ragflow_gpu/run/pids/test_gpu/backend.pid
ls -1 /data/kca/ragflow_gpu/run/pids/test_gpu/task_executor_*.pid
```

### 3) 确认 task 绑定 GPU（32-task 模式）
```bash
cd /data/kca/ragflow_gpu
for f in run/pids/test_gpu/task_executor_*.pid; do
  pid=$(cat "$f")
  echo "$f pid=$pid"
  tr '\0' '\n' < /proc/$pid/environ | egrep '^CUDA_VISIBLE_DEVICES='
done
```

用 `nvidia-smi` 验证：
```bash
nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory --format=csv,noheader | head -n 30
```

## 更新代码（服务器侧）

```bash
cd /data/kca/ragflow_gpu
git pull
uv sync --python 3.12
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh
RAGFLOW_ENV=test_gpu \
WS=32 \
TASK_CUDA_VISIBLE_DEVICES_LIST="0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3" \
WEB_PORT=29180 \
START_FRONTEND=1 \
bash start_all.sh
```

## 方案 A（API 边界修复）部署流程

### 本次改动说明

| 项目 | 改动内容 | 影响 |
|:---|:---|:---|
| RAGFlow | `api/apps/sdk/dataset.py:knowledge_graph()` 扩展：新增 `doc_id` + `type=subgraph` 参数，返回文档级完整子图（不截断） | 原有行为不变（不传参数时走原逻辑） |
| NoeticAI | `GraphService._query_subgraph()` 重写：从 ES 直连改为调用 RAGFlow API；新增 config toggle `USE_RAGFLOW_GRAPH_API` | 默认走 API，可通过环境变量回退到 ES 直连 |

**部署目标：** 172 服务器 `test_gpu` 环境（API 端口 29480，Web 端口 29180）

---

### Phase 1：本地编译启动验证

**前提：** 本地已完成所有代码修改（RAGFlow + NoeticAI）

```bash
# 1.1 RAGFlow 本地启动
cd /Users/weixiaofeng/Desktop/zxwl/coding/ragflow
RAGFLOW_ENV=dev WS=1 START_FRONTEND=0 bash start_all.sh

# 1.2 验证 API 扩展（替换 {dataset_id}、{doc_id}、{api_key} 为实际值）
# 新功能验证：按文档查 subgraph
curl -s "http://localhost:9380/v1/datasets/{dataset_id}/knowledge_graph?doc_id={doc_id}&type=subgraph" \
  -H "Authorization: Bearer {api_key}" | jq '{
    node_count: (.data.graph.nodes | length),
    edge_count: (.data.graph.edges | length)
  }'

# 向后兼容验证：不传 doc_id，行为不变
curl -s "http://localhost:9380/v1/datasets/{dataset_id}/knowledge_graph" \
  -H "Authorization: Bearer {api_key}" | jq '.data.graph.nodes | length'
# 应返回 ≤ 256（原有截断逻辑）

# 空 doc_id 验证：不存在的文档返回空图
curl -s "http://localhost:9380/v1/datasets/{dataset_id}/knowledge_graph?doc_id=nonexistent&type=subgraph" \
  -H "Authorization: Bearer {api_key}" | jq '.data.graph'
# 应返回 {}

# 1.3 NoeticAI 本地启动
cd /Users/weixiaofeng/Desktop/zxwl/coding/NoeticAI
# 按现有方式启动，确认无编译错误
# 检查启动日志中有 use_ragflow_api=true

# 1.4 config toggle 验证
# 设置 USE_RAGFLOW_GRAPH_API=false 重启 NoeticAI
# 确认回退到 ES 直连路径（日志中出现 subgraph_es 相关内容）
# 恢复 USE_RAGFLOW_GRAPH_API=true
```

**通过标准：**
- [x] RAGFlow 编译启动零错误
- [x] NoeticAI 编译启动零错误
- [x] 新 API 返回完整子图（节点数不受 256 限制）
- [x] 不传 doc_id 时行为不变
- [x] config toggle 双路径均可工作

---

### Phase 2：远程服务器部署（172.16.1.116 test_gpu）

**前提：** Phase 1 通过，代码已 push 到远端仓库

```bash
# 2.1 SSH 登录
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116

# 2.2 更新代码
cd /data/kca/ragflow_gpu
git pull
uv sync --python 3.12

# 2.3 停止当前服务
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh

# 2.4 启动服务（32-task 生产模式）
RAGFLOW_ENV=test_gpu \
WS=32 \
TASK_CUDA_VISIBLE_DEVICES_LIST="0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3" \
WEB_PORT=29180 \
START_FRONTEND=1 \
bash start_all.sh

# 2.5 健康检查
curl -sS -i http://127.0.0.1:29480/v1/system/healthz | head
# 预期：HTTP/1.1 200 OK

curl -sS -I http://127.0.0.1:29180/ | head
# 预期：HTTP/1.1 200 OK

# 2.6 验证 32 个 task 进程
ls -1 /data/kca/ragflow_gpu/run/pids/test_gpu/task_executor_*.pid | wc -l
# 预期：32

# 2.7 验证 GPU 绑定
for f in run/pids/test_gpu/task_executor_{0..3}.pid; do
  pid=$(cat "$f")
  gpu=$(tr '\0' '\n' < /proc/$pid/environ | grep '^CUDA_VISIBLE_DEVICES=' | cut -d= -f2)
  echo "$(basename $f): GPU=$gpu"
done
# 预期：task_executor_0.pid: GPU=0, task_executor_1.pid: GPU=1, ...

# 2.8 新 API 验证
curl -s "http://127.0.0.1:29480/v1/datasets/{dataset_id}/knowledge_graph?doc_id={doc_id}&type=subgraph" \
  -H "Authorization: Bearer {api_key}" | jq '.data.graph.nodes | length'
# 预期：返回子图节点数
```

**通过标准：**
- [x] 健康检查 200 OK
- [x] 32 个 task executor 进程运行正常
- [x] GPU 0-3 绑定正确
- [x] 新 API 返回子图数据

---

### Phase 3：业务串联验证（本地 NoeticAI → 远程 172 RAGFlow）

**前提：** Phase 2 通过（172 RAGFlow 服务就绪），NoeticAI 代码已改

```bash
# 3.1 配置 NoeticAI 指向远程 RAGFlow
# 修改配置：ragflow_api_base = http://172.16.1.116:29480
# 确保 USE_RAGFLOW_GRAPH_API=true
# 重启 NoeticAI

# 3.2 端到端验证
# 1) 上传测试文档 → 等待图谱构建完成（写链路验证）
# 2) 查询该文档图谱 → 确认通过 API 获取子图（读链路验证）
# 3) 切换场景（股权结构 → 产业链 → 高管关联）→ 确认过滤正常
# 4) 打开前端 G6 图谱页面 → 确认渲染正常

# 3.3 数据一致性验证
# 同一文档，分别用 API 路径和 ES 路径（toggle 切换）查询
# 对比节点数、边数，差异应 < 5%（仅排序可能不同）

# 3.4 性能对比
# 同一文档查询 3 次，记录耗时
# API 路径 P50 耗时 < ES 路径 P50 的 150%
```

**通过标准：**
- [x] 写链路正常（文档上传 + 图谱构建）
- [x] 读链路正常（通过 API 获取子图）
- [x] 场景过滤正常（≥3 个场景）
- [x] 前端 G6 渲染正常
- [x] 双路径数据一致性 ≥ 95%

---

### Phase 4：回滚准备

**完整回滚方案见：** `/Users/weixiaofeng/.openclaw/workspace/design/kca-graph-refactor/scheme-a-rollback-design.md`

**快速回滚（热回滚 — 10 分钟内）：**
```bash
# 在 NoeticAI 部署环境设置：
export USE_RAGFLOW_GRAPH_API=false
# 重启 NoeticAI 服务
# 验证：日志中确认走 ES 直连路径
```

**冷回滚（代码回退）：**
```bash
# RAGFlow 侧
cd /data/kca/ragflow_gpu
git revert <scheme-a-commit>
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh
RAGFLOW_ENV=test_gpu \
WS=32 \
TASK_CUDA_VISIBLE_DEVICES_LIST="0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3,0,1,2,3" \
WEB_PORT=29180 \
START_FRONTEND=1 \
bash start_all.sh
```

---

### 客户端重启策略

| 组件 | 是否需要重启 | 说明 |
|:---|:---|:---|
| RAGFlow 后端 | ✅ 需要 | 代码有改动（API 扩展） |
| RAGFlow 前端 | ❌ 不需要 | 前端代码无改动（除非需要随后端一起重启） |
| NoeticAI 后端 | ✅ 需要 | 代码有改动（GraphService + Client） |
| NoeticAI 前端 | ❌ 不需要 | 前端代码零改动 |

**原则：** 改了哪里就重启哪里。本次改动不涉及前端代码，前端不需要单独重启。但如果 RAGFlow 使用 `START_FRONTEND=1` 启动脚本，前端会一起重启（无影响）。

## 常见问题

**前端端口不通：**
确认容器 `kca-ragflow-web-test_gpu` 存在且 `ss -ltnp | grep 29180` 有监听；必要时单独执行 `bash start_frontend.sh`。

**依赖不可达：**
`start_backend.sh` 会用 `nc` 检测依赖端口（PG/Redis/MinIO/ES），未通过会直接失败，按输出修复。

**Redis 连接告警：**
如果 `healthz` 中 `redis!=ok`，优先检查 `conf/local.service_conf.<env>.yaml` 是否补齐了 Redis 密码等参数。

**新 API 返回 "No authorization"：**
确认请求头携带了正确的 `Authorization: Bearer {api_key}`，且该 API key 有权访问目标 dataset。

**32-task 模式下部分 task 启动失败：**
检查 GPU 显存是否充足：`nvidia-smi` 查看 GPU 0-3 的显存占用。如果 VLLM 进程意外占用了 GPU 0-3，需先排查。
