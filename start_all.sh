#!/bin/bash
# RAGflow 一键启动脚本（前后端）

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

mkdir -p logs

if [ -z "${RAGFLOW_ENV:-}" ] && [ -z "${RAGFLOW_CONF:-}" ]; then
    echo "❌ 必须显式指定 RAGFLOW_ENV 或 RAGFLOW_CONF，禁止默认启动"
    echo "示例: RAGFLOW_ENV=dev WS=1 START_FRONTEND=0 bash start_all.sh"
    exit 1
fi

echo "=========================================="
echo "RAGflow 一键启动脚本"
echo "=========================================="
echo "环境变量: RAGFLOW_ENV=${RAGFLOW_ENV:-default} RAGFLOW_CONF=${RAGFLOW_CONF:-<auto>}"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步骤 1/2: 启动后端服务"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
bash start_backend.sh

echo
sleep 2

if [ "${START_FRONTEND:-1}" = "1" ]; then
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "步骤 2/2: 启动前端服务"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    bash start_frontend.sh
else
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "步骤 2/2: 跳过前端启动 (START_FRONTEND=0)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
fi

echo
if [ -d ".venv" ]; then
    # shellcheck disable=SC1091
    source .venv/bin/activate
    export PYTHONPATH="$SCRIPT_DIR"
    eval "$(python scripts/resolve_runtime_conf.py --format shell)"
fi

echo "=========================================="
echo "✅ RAGflow 启动流程完成"
echo "=========================================="
echo "📊 环境信息:"
echo "   - 环境: ${ACTIVE_ENV:-default}"
echo "   - 配置: ${ACTIVE_CONF_PATH:-unknown}"
if [ -n "${RAGFLOW_PORT:-}" ]; then
    echo "   - API 地址: http://localhost:${RAGFLOW_PORT}"
fi
echo
echo "🛑 停止服务:"
echo "   RAGFLOW_ENV=${RAGFLOW_ENV:-default} bash stop_all.sh"
echo "=========================================="
