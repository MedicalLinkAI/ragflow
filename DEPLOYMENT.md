# RAGflow 部署文档

## ✅ 部署完成

RAGflow v0.23.1 已成功部署，使用源码方式运行，集成 NoeticAI 现有服务。

## 🚀 快速启动

### 一键启动（推荐）
```bash
cd /Users/weixiaofeng/Desktop/zxwl/coding/ragflow
bash start_all.sh
```

### 分步启动
```bash
# 仅启动后端
bash start_backend.sh

# 仅启动前端
bash start_frontend.sh
```

### 停止服务
```bash
bash stop_all.sh
```

### 验证部署
```bash
bash test_access.sh
```

## 📍 访问地址

- **前端页面**: http://localhost
- **后端 API**: http://localhost:9380

## 🏗️ 架构说明

### 为什么使用 nginx？

**问题**: SPA 前端路由需要服务器支持 URL 重写
- 访问 `/login`, `/dataset` 等路径时，需要返回 `index.html`
- Python `http.server` 不支持路由重写，会返回 404

**解决方案**: 使用 nginx
- 统一入口: http://localhost (80 端口)
- 前端路由: 所有路径自动回退到 `index.html`
- API 代理: `/v1/*` 自动转发到后端 9380 端口
- 静态资源: 直接从 `web/dist/` 提供

### 服务架构

```
浏览器 (http://localhost)
    ↓
nginx (80 端口)
    ├── / → web/dist/index.html (前端)
    ├── /login → web/dist/index.html (SPA 路由)
    ├── /v1/* → localhost:9380 (API 代理)
    └── /static/* → web/dist/static/* (静态资源)
```

## 📦 服务依赖

| 服务 | 地址 | 说明 |
|------|------|------|
| PostgreSQL | localhost:5432 | 共用 NoeticAI，数据库: ragflow |
| Redis | localhost:6379 (db:2) | 共用 NoeticAI |
| MinIO | localhost:9000 | 共用 NoeticAI，bucket: ragflow |
| Elasticsearch | localhost:1200 | 独立容器 (ragflow-es01) |
| 后端 API | localhost:9380 | RAGflow Python 服务 |
| Nginx | localhost:80 | 前端 + API 代理 |

## 🔧 配置文件

### 主配置
- **后端配置**: `conf/service_conf.yaml`
- **Nginx 配置**: `/opt/homebrew/etc/nginx/servers/ragflow.conf`

### 日志文件
- **后端日志**: `logs/backend.log`
- **Nginx 日志**: `/opt/homebrew/var/log/nginx/`

## 🛠️ 启动脚本说明

### start_backend.sh
1. 检测并清理旧的后端进程
2. 检查依赖服务 (PostgreSQL, Redis, MinIO, ES)
3. 设置环境变量 (PYTHONPATH, NLTK_DATA, DB_TYPE=postgres)
4. 后台启动 Python 服务
5. 验证启动成功 (9380 端口)

### start_frontend.sh
1. 检测并清理旧的前端服务
2. 检查 Node.js 环境
3. 安装/检查前端依赖
4. 重新构建前端 (npm run build)
5. 启动 nginx
6. 验证启动成功 (80 端口)

### start_all.sh
按顺序执行:
1. 启动后端 (start_backend.sh)
2. 启动前端 (start_frontend.sh)
3. 显示服务状态和访问信息

### stop_all.sh
1. 停止后端进程
2. 停止 nginx

## 📝 使用说明

### 首次使用
1. 在浏览器打开 http://localhost
2. 点击"注册"创建新账号
3. 登录后创建知识库
4. 上传文档进行测试

### LLM 配置
已预配置通义千问:
- 厂商: Tongyi-Qianwen
- Chat 模型: qwen-plus
- Embedding 模型: text-embedding-v1
- API Key: sk-fad19b13dde544f6a5ca9e9725b133a3

## 🐛 故障排查

### 前端无法访问
```bash
# 检查 nginx 状态
brew services list | grep nginx

# 重启 nginx
brew services restart nginx

# 查看 nginx 日志
tail -f /opt/homebrew/var/log/nginx/error.log
```

### 后端无法访问
```bash
# 检查后端进程
ps aux | grep ragflow_server

# 查看后端日志
tail -f logs/backend.log

# 重启后端
bash start_backend.sh
```

### 依赖服务问题
```bash
# 检查 PostgreSQL
nc -z localhost 5432

# 检查 Redis
nc -z localhost 6379

# 检查 Elasticsearch
docker ps | grep ragflow-es01
curl http://localhost:1200
```

## 📚 相关文档

- RAGflow 官方文档: https://ragflow.io/docs
- 源码仓库: https://github.com/infiniflow/ragflow
- API 文档: http://localhost:9380/apidocs/ (启动后访问)

## 🔄 更新代码

```bash
cd /Users/weixiaofeng/Desktop/zxwl/coding/ragflow

# 停止服务
bash stop_all.sh

# 更新代码
git pull

# 更新 Python 依赖
source .venv/bin/activate
uv sync --python 3.12

# 重新启动（会自动重新构建前端）
bash start_all.sh
```

## ⚙️ 环境要求

- Python 3.12
- Node.js 22.20.0
- Docker (仅 Elasticsearch)
- Nginx 1.29.4
- PostgreSQL, Redis, MinIO (共用 NoeticAI)
