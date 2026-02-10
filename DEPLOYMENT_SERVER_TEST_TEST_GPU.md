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

## 常见问题

- 前端端口不通：确认容器 `kca-ragflow-web-test_gpu` 存在且 `ss -ltnp | grep 29180` 有监听；必要时单独执行 `bash start_frontend.sh`。
- 依赖不可达：`start_backend.sh` 会用 `nc` 检测依赖端口（PG/Redis/MinIO/ES），未通过会直接失败，按输出修复。
- Redis 连接告警：如果 `healthz` 中 `redis!=ok`，优先检查 `conf/local.service_conf.<env>.yaml` 是否补齐了 Redis 密码等参数。
