# ==============================================================================
# RAGFlow 开发环境 Makefile
# ==============================================================================
# 用法示例:
#   make setup              # 初始化完整开发环境（Python + Node.js 依赖）
#   make base               # 启动依赖中间件（MySQL, Redis, MinIO, Elasticsearch...）
#   make backend            # 启动后端服务
#   make frontend           # 启动前端开发服务
#   make dev                # 一键启动：中间件 + 后端 + 前端
#   make stop               # 停止后端服务
# ==============================================================================

# ------------------------------------------------------------------------------
# 环境变量（可通过命令行覆盖，如: make backend ENV=prod WS=2）
# ------------------------------------------------------------------------------
ENV        ?= dev
WS         ?= 1
DOC_ENGINE ?= elasticsearch
DEVICE     ?= cpu
POSTGRES_HOST ?= localhost
POSTGRES_PORT ?= 5433

PYTHON     := uv run python
UV         := uv

.DEFAULT_GOAL := help

.PHONY: help setup setup-python setup-node \
        base backend frontend dev stop \
        pull pull-all \
        lint lint-python lint-frontend \
        test test-python test-frontend \
        clean clean-python clean-node clean-logs

# ==============================================================================
# 帮助
# ==============================================================================
help:
	@echo ""
	@echo "RAGFlow 开发环境 Makefile"
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  初始化"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make setup              初始化完整开发环境（Python + Node.js）"
	@echo "  make setup-python       仅初始化 Python 依赖（uv sync）"
	@echo "  make setup-node         仅初始化前端依赖（npm install）"
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  启动服务"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make base               启动中间件（Docker: MySQL/Redis/MinIO/ES...）"
	@echo "  make backend            启动后端服务（ENV=dev WS=1）"
	@echo "  make frontend           启动前端开发服务"
	@echo "  make dev                一键启动全部（中间件 + 后端 + 前端）"
	@echo "  make stop               停止后端服务（ENV=dev）"
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  Docker / 代理"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make pull               拉取中间件镜像（DOC_ENGINE=elasticsearch）"
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  代码质量"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make lint               运行全部 lint（Python + 前端）"
	@echo "  make lint-python        运行 ruff check + format"
	@echo "  make lint-frontend      运行前端 eslint"
	@echo "  make test               运行全部测试"
	@echo "  make test-python        运行后端测试（pytest）"
	@echo "  make test-frontend      运行前端测试（jest）"
	@echo ""
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  清理"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "  make clean              清理所有构建产物"
	@echo "  make clean-logs         清理日志文件"
	@echo ""
	@echo "  可覆盖的变量: ENV=$(ENV)  WS=$(WS)  DOC_ENGINE=$(DOC_ENGINE)  DEVICE=$(DEVICE)"
	@echo ""

# ==============================================================================
# 初始化
# ==============================================================================
setup: setup-python setup-node
	@echo ""
	@echo "✅ 开发环境初始化完成！"
	@echo "   下一步: make base 启动中间件，然后 make backend 启动后端"

setup-python:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "初始化 Python 环境"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	$(UV) sync --python 3.12 --all-extras
	@if [ -f "download_deps.py" ]; then $(UV) run python download_deps.py; fi
	@echo "✅ Python 依赖安装完成"

setup-node:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "初始化前端依赖"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	cd web && npm install --legacy-peer-deps
	@echo "✅ 前端依赖安装完成"

# ==============================================================================
# 服务启动 / 停止
# ==============================================================================
base:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "启动基础中间件"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	DOC_ENGINE=$(DOC_ENGINE) DEVICE=$(DEVICE) bash start_base.sh

backend:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "启动后端服务 (ENV=$(ENV), WS=$(WS))"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	RAGFLOW_ENV=$(ENV) WS=$(WS) bash start_backend.sh

frontend:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "启动前端开发服务"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	bash start_frontend.sh

dev: base backend frontend
	@echo ""
	@echo "✅ 全部服务已启动"

stop:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "停止后端服务 (ENV=$(ENV))"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	RAGFLOW_ENV=$(ENV) bash stop_all.sh

stop-base:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "停止中间件容器"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	cd docker && docker-compose -f docker-compose-base.yml down

# ==============================================================================
# 拉取 Docker 镜像
# ==============================================================================
pull:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "拉取中间件镜像 (DOC_ENGINE=$(DOC_ENGINE))"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	cd docker && \
		COMPOSE_PROFILES=$(DOC_ENGINE),$(DEVICE) \
		docker-compose -f docker-compose-base.yml pull

# ==============================================================================
# 代码质量
# ==============================================================================
lint: lint-python lint-frontend

lint-python:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "Python lint（ruff）"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	$(UV) run ruff check .
	$(UV) run ruff format --check .

lint-fix:
	$(UV) run ruff check --fix .
	$(UV) run ruff format .

lint-frontend:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "前端 lint（eslint）"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	cd web && npm run lint

# ==============================================================================
# 测试
# ==============================================================================
test: test-python test-frontend

test-python:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "运行后端测试（pytest）"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	$(UV) run pytest

test-frontend:
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	@echo "运行前端测试（jest）"
	@echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
	cd web && npm run test

# ==============================================================================
# 清理
# ==============================================================================
clean: clean-python clean-node clean-logs

clean-python:
	rm -rf .venv __pycache__ **/__pycache__ *.pyc **/*.pyc .ruff_cache

clean-node:
	rm -rf web/node_modules web/dist

clean-logs:
	rm -rf logs/*.log logs/**/*.log
