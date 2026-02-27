# RAGFlow 启动部署方案（172.16.1.116：test / test_gpu）

适用范围：只针对服务器 `172.16.1.116` 上的两套环境 `test`(CPU) 与 `test_gpu`(GPU) 的启动/停止/验收。

## 安全边界

- 不操作他人目录：例如 `/data/yugasun/ragflow`。
- 不操作他人容器：例如 `docker-ragflow-gpu-1`。
- 停启只允许按 **PID 文件** 精准停止当前环境的进程，不做全局 `pkill/grep` 扫杀。

## 目录与端口

- CPU `test`：代码目录 `/data/kca/ragflow`，API `29380`，Web `29080`
- GPU `test_gpu`：代码目录 `/data/kca/ragflow_gpu`，API `29480`，Web `29180`

访问地址：
- CPU test：`http://172.16.1.116:29080/`（Web），`http://172.16.1.116:29380/v1/system/healthz`（API）
- GPU test_gpu：`http://172.16.1.116:29180/`（Web），`http://172.16.1.116:29480/v1/system/healthz`（API）

## 配置选择规则

启动/停止必须显式指定其一：
- `RAGFLOW_ENV=<env>`（推荐）
- 或 `RAGFLOW_CONF=<yaml>`（高级用法）

可选本地覆盖（一般放密码等敏感信息）：
- `conf/local.service_conf.<env>.yaml`

## 存储引擎复用（按你的要求：与 CPU test 完全共享）

`test_gpu` 只隔离端口与算力，存储与 `test` 完全一致（这意味着 **数据是共享的**，`test_gpu` 的操作会影响 `test` 的数据）。

当前对齐目标（test 与 test_gpu 一致）：
- Postgres：同库 `ragflow_test`
- Redis：同 `db=13`
- MinIO：同 `bucket=ragflow-test` + `prefix_path=test`
- Elasticsearch：同 `http://localhost:21200`

## GPU 使用约束

- GPU4-7 已被 VLLM 进程占用（不要动）。
- `test_gpu` 使用 GPU0-3。
- 4 个 task 分别绑定 4 张卡：用 `TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3`。

## 一键启动（推荐）

### 启动 CPU test

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow
RAGFLOW_ENV=test WS=2 START_FRONTEND=1 bash start_all.sh
```

### 启动 GPU test_gpu（4 个 task 绑定 GPU0-3）

```bash
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow_gpu
RAGFLOW_ENV=test_gpu WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3 WEB_PORT=29180 START_FRONTEND=1 bash start_all.sh
```

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

### 3) 确认 4 个 task 分别绑定 GPU0-3
```bash
cd /data/kca/ragflow_gpu
for f in run/pids/test_gpu/task_executor_*.pid; do
  pid=$(cat "$f")
  echo "$f pid=$pid"
  tr '\0' '\n' < /proc/$pid/environ | egrep '^CUDA_VISIBLE_DEVICES='
done
```

也可用 `nvidia-smi` 看 compute apps：
```bash
nvidia-smi --query-compute-apps=gpu_uuid,pid,process_name,used_memory --format=csv,noheader | head -n 30
```

## 更新代码（服务器侧）

```bash
cd /data/kca/ragflow_gpu
git pull
uv sync --python 3.12
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh
RAGFLOW_ENV=test_gpu WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3 WEB_PORT=29180 START_FRONTEND=1 bash start_all.sh
```

## 方案A（API边界修复）部署流程

### 本次改动点说明
- **RAGFlow 侧**：扩展 `knowledge_graph` API，支持 `doc_id` 和 `type=subgraph` 参数，返回文档级完整子图（不截断）
- **NoeticAI 侧**：`GraphService._query_subgraph()` 改为调用 RAGFlow API，移除 ES 直连代码
- **部署目标**：172 服务器 `test_gpu` 环境（API 端口 29480）

### 1. 本地编译启动验证流程
**前提**：本地已完成代码修改（RAGFlow + NoeticAI）

```bash
# 1.1 本地 RAGFlow 启动验证
cd /Users/weixiaofeng/Desktop/zxwl/coding/ragflow
RAGFLOW_ENV=dev WS=1 START_FRONTEND=0 bash start_all.sh

# 验证 API 扩展
curl -s "http://localhost:9380/datasets/{dataset_id}/knowledge_graph?doc_id={doc_id}&type=subgraph" | jq .

# 1.2 本地 NoeticAI 启动验证
cd /Users/weixiaofeng/Desktop/zxwl/coding/NoeticAI
# 启动 NoeticAI 服务（根据现有启动脚本）
# 验证服务健康，无编译错误

# 1.3 基础功能验证
# 使用测试脚本调用新 API，确认返回格式正确
# 验证场景过滤逻辑不受影响
```

### 2. 远程服务器部署验证流程
**前提**：本地验证通过，代码已 push 到远端仓库

```bash
# 2.1 更新 172 服务器代码
ssh -i ~/.ssh/id_ed25519_futurefab root@172.16.1.116
cd /data/kca/ragflow_gpu
git pull
uv sync --python 3.12

# 2.2 重启 RAGFlow 服务（test_gpu 环境）
STOP_FRONTEND=1 RAGFLOW_ENV=test_gpu bash stop_all.sh
RAGFLOW_ENV=test_gpu WS=4 TASK_CUDA_VISIBLE_DEVICES_LIST=0,1,2,3 WEB_PORT=29180 START_FRONTEND=1 bash start_all.sh

# 2.3 验证部署结果
# 健康检查
curl -sS -i http://127.0.0.1:29480/v1/system/healthz

# 新 API 验证（使用真实 dataset_id 和 doc_id）
curl -s "http://127.0.0.1:29480/datasets/{dataset_id}/knowledge_graph?doc_id={doc_id}&type=subgraph" | jq '.data.graph.nodes | length'
```

### 3. 业务串联验证流程
**前提**：172 服务器 RAGFlow 服务就绪，本地 NoeticAI 代码已修改

```bash
# 3.1 配置本地 NoeticAI 指向 172 RAGFlow
# 修改 NoeticAI 配置，将 RAGFlow 地址改为 172.16.1.116:29480
# 具体配置位置根据 NoeticAI 实际配置而定

# 3.2 重启本地 NoeticAI 服务
# 根据现有启动脚本重启 NoeticAI（前后端）

# 3.3 端到端验证
# 3.3.1 上传文档触发图谱构建
# 通过 NoeticAI 前端上传一个测试文档，等待解析完成

# 3.3.2 查询图谱验证
# 在前端查询该文档的图谱，确认展示正常（G6 渲染）
# 同时检查后端日志，确认走的是新 API 路径

# 3.3.3 场景过滤验证
# 切换不同场景（股权结构、产业链等），确认过滤逻辑正常
```

### 4. 回滚流程
**完整回滚方案见**：`/Users/weixiaofeng/.openclaw/workspace/design/kca-graph-refactor/scheme-a-rollback-design.md`

**热回滚（配置开关）**：
```bash
# 4.1 修改 NoeticAI 环境变量
# 在 NoeticAI 部署服务器上设置：
export USE_RAGFLOW_GRAPH_API=false

# 4.2 重启 NoeticAI 服务
# 根据实际部署方式重启（如 systemctl restart noeticai）

# 4.3 验证回滚
# 检查日志确认走 ES 直连路径
# 执行图谱查询确认功能正常
```

**冷回滚（代码回退）**：
- 如热回滚无效，需回退代码到方案A之前的版本
- 具体步骤见回滚方案文档 §4.2

### 5. 监控与告警
部署后需关注以下指标：
- RAGFlow API 可用性（健康检查成功率）
- 图谱查询延迟（P95 < 2 秒）
- 错误率（< 5%）
- 如指标异常，按回滚流程处理

## 常见问题

- 前端端口不通：确认容器 `kca-ragflow-web-test_gpu` 存在且 `ss -ltnp | grep 29180` 有监听；必要时单独执行 `bash start_frontend.sh`。
- 依赖不可达：`start_backend.sh` 会用 `nc` 检测依赖端口（PG/Redis/MinIO/ES），未通过会直接失败，按输出修复。
- Redis 连接告警：如果 `healthz` 中 `redis!=ok`，优先检查 `conf/local.service_conf.<env>.yaml` 是否补齐了 Redis 密码等参数。
