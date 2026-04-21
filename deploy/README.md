# RAGflow 容器化部署指南

## 前置要求

| 依赖 | 最低版本 | 验证命令 |
|------|---------|---------|
| Docker | ≥ 24.0 | `docker --version` |
| Docker Compose | V2 (plugin) | `docker compose version` |
| Git | — | `git --version` |
| 磁盘空间 | ≥ 20 GB | `df -h` |

> ⚠️ RAGflow 主镜像约 5 GB，Elasticsearch 镜像约 1.5 GB，首次拉取耗时较长，请确保磁盘和网络充足。

---

## 快速开始（3 步走）

```bash
# 步骤 1：创建环境配置（从模板复制）
cp deploy/.env.example deploy/.env.dev

# 步骤 2：初始化基础设施（ES + PG + Redis + MinIO）
deploy/setup.sh --env dev

# 步骤 3：构建并部署应用
deploy/build.sh ragflow-web --env dev       # 构建 web 前端镜像
deploy/deploy.sh ragflow-all --env dev      # 部署全部应用
```

所有命令均从**仓库根目录**执行。

---

## apps.yml 应用清单

`deploy/apps.yml` 描述所有可部署单元的元数据，供部署脚本和 CI 消费。

### 9-field Schema

| 字段 | 类型 | 说明 |
|------|------|------|
| `app_id` | string | 应用唯一标识，作为脚本参数传入 |
| `compose_service` | string | 对应 `docker-compose.yml` 中的 service 名称 |
| `default_host_ports` | int[] | 默认宿主机端口列表 |
| `health_target` | string | 健康检查 URL |
| `depends_on_app_ids` | string[] | 依赖的其他 app_id |
| `exposure_class` | string | 暴露级别：`public` / `internal` / `none` |
| `required_env_groups` | string[] | 需要的环境变量分组 |
| `secret_inputs` | string[] | 敏感配置项列表 |
| `supported_actions` | string[] | 支持的操作：`build` / `deploy` / `logs` / `status` |

### 应用列表

| app_id | 说明 | Compose profile | 暴露级别 |
|--------|------|----------------|---------|
| `ragflow-api` | API 服务（nginx + ragflow_server） | api | internal |
| `ragflow-web` | Web 前端（轻量 nginx） | api | public |
| `ragflow-worker` | 任务执行器（task_executor） | worker | none |

---

## App ID 列表

脚本支持以下 app-id 参数：

| App ID | 说明 | 适用脚本 |
|--------|------|---------|
| `ragflow-api` | API 服务 | build.sh, deploy.sh |
| `ragflow-web` | Web 前端 | build.sh, deploy.sh |
| `ragflow-worker` | 任务执行器 | deploy.sh |
| `ragflow-all` | 全部应用（按依赖顺序） | deploy.sh |

> `ragflow-worker` 无需 build — 直接使用 `RAGFLOW_IMAGE` 主镜像。

---

## 端口表

开发环境使用 `1xxxx` 前缀端口，与裸金属部署隔离：

| 服务 | 容器端口 | 宿主机端口 (dev) | 环境变量 | 说明 |
|------|---------|----------------|---------|------|
| Elasticsearch | 9200 | 11200 | `ES_HOST_PORT` | 全文搜索引擎 |
| PostgreSQL | 5432 | 15455 | `POSTGRES_HOST_PORT` | 数据库（pgvector） |
| Redis (Valkey) | 6379 | 16379 | `REDIS_HOST_PORT` | 缓存与队列 |
| MinIO API | 9000 | 19000 | `MINIO_HOST_PORT` | 对象存储 API |
| MinIO Console | 9001 | 19001 | `MINIO_CONSOLE_HOST_PORT` | 对象存储管理界面 |
| ragflow-api | 9380 | 19380 | `RAGFLOW_API_HOST_PORT` | API 服务 |
| ragflow-web | 80 | 18080 | `RAGFLOW_WEB_HOST_PORT` | Web 前端 |

> 端口映射在 `.env.<env>` 中配置，不同环境可使用不同端口段。

---

## 环境配置说明

### 配置文件体系

```
deploy/
├── .env.example    # 模板文件（含完整注释，跟踪在 Git 中）
├── .env.dev        # 开发环境（跟踪在 Git 中）
├── .env.test       # 测试环境（按需创建）
├── .env.prod       # 生产环境（按需创建）
└── .env            # 本地覆盖（已 gitignore，不跟踪）
```

### 关键配置项

| 配置项 | 说明 | 示例值 |
|--------|------|--------|
| `RAGFLOW_IMAGE` | RAGflow 主镜像标签（源码构建，API 和 Worker 共享） | `ragflow:dev` |
| `DB_TYPE` | 数据库类型 | `postgres`（⚠️ **必须显式设置**，RAGflow 默认 MySQL） |
| `HF_ENDPOINT` | HuggingFace 镜像源（国内加速） | `https://hf-mirror.com` |
| `DATA_ROOT` | 基础设施数据 bind mount 根目录 | `./data` |
| `STACK_VERSION` | Elasticsearch 版本 | `8.11.3` |
| `GPU_ENABLED` | 是否启用 GPU（Worker） | `false` |

### ⚠️ 重要提醒

- **`DB_TYPE=postgres`** — RAGflow 上游默认使用 MySQL，我们显式切换为 PostgreSQL。此项务必保持为 `postgres`。
- **`service_conf.yaml.template`** — RAGflow 的 `entrypoint.sh` 会在启动时用环境变量渲染此模板。模板中的 postgres 段已激活、mysql 段已注释。
- **密码安全** — 生产环境必须替换所有默认密码（`infini_rag_flow`）。生成方式：`openssl rand -hex 32`

---

## RAGflow 架构说明

RAGflow 拆分为三个应用服务，分别独立部署：

```
┌───────────────────────────────────────────────────┐
│                   ragflow-api                      │
│  ┌──────────┐    ┌──────────────────────┐         │
│  │  nginx   │───►│  ragflow_server      │         │
│  │  :9380   │    │  --disable-taskexecutor        │
│  └──────────┘    └──────────────────────┘         │
│  使用 RAGFLOW_IMAGE，挂载 service_conf.yaml.template │
└───────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────┐
│                  ragflow-worker                    │
│  ┌──────────────────────────┐                     │
│  │   task_executor          │                     │
│  │   --disable-webserver    │                     │
│  └──────────────────────────┘                     │
│  使用 RAGFLOW_IMAGE，挂载 service_conf.yaml.template │
│  HF_ENDPOINT=https://hf-mirror.com               │
└───────────────────────────────────────────────────┘

┌───────────────────────────────────────────────────┐
│                   ragflow-web                      │
│  ┌──────────────────────────┐                     │
│  │  nginx (alpine)          │                     │
│  │  静态文件 + 反向代理      │                     │
│  │  :80 → ragflow-api:9380  │                     │
│  └──────────────────────────┘                     │
│  Dockerfile.web 从 RAGFLOW_IMAGE 提取前端产物       │
└───────────────────────────────────────────────────┘
```

### 组件详解

| 组件 | 镜像 | 启动命令 | 说明 |
|------|------|---------|------|
| **ragflow-api** | `RAGFLOW_IMAGE` | `entrypoint.sh --disable-taskexecutor` | 运行 ragflow_server + 内置 nginx，不启动 task_executor |
| **ragflow-worker** | `RAGFLOW_IMAGE` | `entrypoint.sh --disable-webserver` | 仅运行 task_executor，不启动 web 服务 |
| **ragflow-web** | `ragflow-web:latest`（自行构建） | `nginx -g 'daemon off;'` | 从 `RAGFLOW_IMAGE` 提取前端产物，轻量 nginx 提供静态文件并反向代理到 ragflow-api |

> **Worker 与 API 共享同一主镜像（`RAGFLOW_IMAGE`）**，通过启动参数区分角色。

---

## 脚本命令参考

### setup.sh — 基础设施初始化

初始化并启动全部基础设施组件（ES + PG + Redis + MinIO），脚本幂等可重复执行。

```bash
deploy/setup.sh --env dev
deploy/setup.sh --env prod
```

| 选项 | 说明 |
|------|------|
| `--env <name>` | 加载 `deploy/.env.<name>`（默认 `dev`） |
| `--help` | 显示帮助信息 |

**退出码：**

| 退出码 | 状态 | 说明 |
|--------|------|------|
| 0 | `initialized` | 首次初始化成功 |
| 0 | `skipped-existing` | 检测到已有数据卷，基础设施启动成功 |
| 1 | `failed` | 关键故障 |
| 2 | `repair-required` | 部分容器不健康 |

**基础设施组件：**

| 组件 | 镜像 | 健康检查 |
|------|------|---------|
| Elasticsearch | `elasticsearch:8.11.3` | `_cluster/health` API |
| PostgreSQL | `pgvector/pgvector:pg15` | `pg_isready` |
| Redis | `valkey/valkey:8` | `redis-cli ping` |
| MinIO | `minio/minio` | `/minio/health/live` |

### build.sh — 应用构建

构建 Docker 镜像并自动打上时间戳标签。

```bash
deploy/build.sh <app-id> [--env <name>] [--branch <name>]
```

| 选项 | 说明 |
|------|------|
| `<app-id>` | `ragflow-web`（当前仅 web 需要构建） |
| `--env <name>` | 加载 `deploy/.env.<name>`（默认 `dev`） |
| `--branch <name>` | 构建前切换并更新分支（要求工作区干净） |

> `ragflow-api` 和 `ragflow-worker` 直接使用 `RAGFLOW_IMAGE` 预构建镜像，无需 build。

### deploy.sh — 应用部署

部署应用容器并等待健康检查通过。

```bash
deploy/deploy.sh <app-id> [--env <name>] [--image <tag>]
```

| 选项 | 说明 |
|------|------|
| `<app-id>` | `ragflow-api` / `ragflow-web` / `ragflow-worker` / `ragflow-all` |
| `--env <name>` | 加载 `deploy/.env.<name>`（默认 `dev`） |
| `--image <tag>` | 指定镜像标签（默认 `latest`） |

**示例：**

```bash
deploy/deploy.sh ragflow-api --env dev       # 仅部署 API
deploy/deploy.sh ragflow-worker --env dev    # 仅部署 Worker
deploy/deploy.sh ragflow-all --env dev       # 部署全部
```

---

## 运维命令

### 查看容器状态

```bash
deploy/deploy.sh --status [--env <name>]
```

返回 JSON 格式的容器状态信息：

```json
{
  "containers": [
    {"name": "ragflow-dev-api", "service": "ragflow-api", "status": "running", "health": "healthy"},
    {"name": "ragflow-dev-web", "service": "ragflow-web", "status": "running", "health": "healthy"},
    {"name": "ragflow-dev-worker", "service": "ragflow-worker", "status": "running", "health": "N/A"}
  ]
}
```

### 查看服务日志

```bash
deploy/deploy.sh --logs ragflow-api [--env <name>]
deploy/deploy.sh --logs ragflow-worker [--env <name>]
```

实时流式输出日志，`Ctrl+C` 退出。

---

## CI/CD 集成指南

### 构建 + 部署流水线

```bash
# CI 构建阶段（仅 web 需要构建）
deploy/build.sh ragflow-web --env prod

# CD 部署阶段
deploy/deploy.sh ragflow-all --env prod
```

### JSON 输出格式

脚本最后一行为机器可读的 JSON，方便 CI 解析：

**build.sh 输出：**

```json
{"app_id": "ragflow-web", "image": "ragflow-web:20250720-160000", "status": "success"}
```

**deploy.sh 输出：**

```json
{"app_id": "ragflow-all", "status": "success", "containers": [...]}
```

### CI 脚本示例

```bash
#!/bin/bash
set -euo pipefail

# 构建 web 前端
deploy/build.sh ragflow-web --env prod

# 部署全部
deploy/deploy.sh ragflow-all --env prod

# 验证状态
deploy/deploy.sh --status --env prod
```

---

## 网络架构

```
┌──────────────────────────────────────────────────────────┐
│                medlinkai-shared (external)                │
│                                                          │
│  ┌────────────┐  ┌────────────┐  ┌────────────────┐     │
│  │ragflow-api │  │ragflow-web │  │ ragflow-worker │     │
│  │ :9380→19380│  │  :80→18080 │  │  (无端口暴露)   │     │
│  └─────┬──────┘  └────────────┘  └───────┬────────┘     │
│        │                                  │              │
│  ┌─────┴──────────────────────────────────┴────────┐     │
│  │  Elasticsearch  │ PostgreSQL │ Redis │  MinIO   │     │
│  │  :9200→11200    │ :5432→15455│:6379→ │:9000→    │     │
│  │                 │            │ 16379 │ 19000    │     │
│  └─────────────────────────────────────────────────┘     │
│                                                          │
│  ┌──────────────────┐  (MedLinkAI 同网络)                │
│  │medlinkai-server  │ ◄── 通过 RAGFLOW_API_URL 调用      │
│  │   :8000          │                                    │
│  └──────────────────┘                                    │
└──────────────────────────────────────────────────────────┘
```

- **`medlinkai-shared`** 是一个 Docker 外部网络（`external: true`），由 `setup.sh` 自动创建
- MedLinkAI 和 RAGflow 两套 Compose 项目通过此网络互通
- MedLinkAI Server 通过容器名 `ragflow-api` 访问 RAGflow API

---

## 常见问题

### Q: 首次构建镜像非常慢

RAGflow 从源码构建，首次构建需下载 `infiniflow/ragflow_deps:latest` 依赖镜像（ML 模型、工具包等），以及安装 Python 和 npm 依赖。建议：

1. 确保网络畅通（构建过程需从 Docker Hub、PyPI、npm registry 下载依赖）
2. 国内环境可设置 `NEED_MIRROR=1`（启用清华/阿里镜像源加速）：
   ```
   NEED_MIRROR=1
   ```
3. 后续增量构建会利用 Docker 层缓存，速度显著加快

### Q: Elasticsearch 启动失败 / 权限问题

在 **Linux** 环境下，ES 的 bind mount 目录需要正确的文件所有者：

```bash
# 创建数据目录并设置权限
mkdir -p deploy/data/esdata
chown -R 1000:1000 deploy/data/esdata

# 如果仍有问题，检查 vm.max_map_count
sudo sysctl -w vm.max_map_count=262144

# 持久化设置
echo "vm.max_map_count=262144" | sudo tee -a /etc/sysctl.conf
```

> macOS 上 Docker Desktop 自动处理文件权限，通常无需手动设置。

### Q: `DB_TYPE` 必须设为 `postgres` 吗？

是的。RAGflow 上游默认使用 MySQL，我们的部署方案显式切换为 PostgreSQL。关键配置点：

1. `.env` 中 `DB_TYPE=postgres`
2. `service_conf.yaml.template` 中 postgres 段已激活、mysql 段已注释

如果 `DB_TYPE` 缺失或设为 `mysql`，RAGflow 会尝试连接 MySQL 导致启动失败。

### Q: HuggingFace 模型下载失败

Worker 默认使用国内镜像源加速下载：

```
HF_ENDPOINT=https://hf-mirror.com
```

如在海外环境部署，可移除此配置或改为官方源：

```
HF_ENDPOINT=https://huggingface.co
```

### Q: 容器端口冲突

修改 `.env.dev` 中的端口变量后重新运行 `setup.sh` 和 `deploy.sh`：

```bash
# deploy/.env.dev
ES_HOST_PORT=21200
POSTGRES_HOST_PORT=25455
REDIS_HOST_PORT=26379
MINIO_HOST_PORT=29000
RAGFLOW_API_HOST_PORT=29380
RAGFLOW_WEB_HOST_PORT=28080
```

### Q: 如何单独重启 Worker？

```bash
deploy/deploy.sh ragflow-worker --env dev
```

Worker 无状态，可随时重启。

### Q: 如何查看 `service_conf.yaml` 渲染结果？

```bash
# 进入 ragflow-api 容器查看渲染后的配置
docker exec ragflow-dev-api cat /ragflow/conf/service_conf.yaml
```

### Q: MinIO Console 如何访问？

浏览器打开 `http://localhost:19001`，使用 `.env` 中配置的 `MINIO_USER` / `MINIO_PASSWORD` 登录。
