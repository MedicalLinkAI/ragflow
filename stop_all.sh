#!/bin/bash
# RAGflow 停止脚本（按环境 PID 隔离）

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

if [ -z "${RAGFLOW_ENV:-}" ] && [ -z "${RAGFLOW_CONF:-}" ]; then
    echo "❌ 停止时也必须显式指定 RAGFLOW_ENV 或 RAGFLOW_CONF，避免误停"
    echo "示例: RAGFLOW_ENV=dev bash stop_all.sh"
    exit 1
fi

if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，无法解析配置"
    exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate
export PYTHONPATH="$SCRIPT_DIR"

eval "$(python scripts/resolve_runtime_conf.py --format shell)"
ENV_SLUG="$(echo "${ACTIVE_ENV:-default}" | tr ' /:' '___')"
PID_DIR="run/pids/${ENV_SLUG}"

BACKEND_PID_FILE="$PID_DIR/backend.pid"
TASK_PID_GLOB="$PID_DIR/task_executor_*.pid"

echo "=========================================="
echo "停止 RAGflow 服务"
echo "=========================================="
echo "环境: ${ACTIVE_ENV}"
echo "配置: ${ACTIVE_CONF_PATH}"

did_stop=0

kill_from_pid_file() {
    local pid_file="$1"
    local process_hint="$2"

    if [ ! -f "$pid_file" ]; then
        return 0
    fi

    local pid
    pid="$(cat "$pid_file" 2>/dev/null || true)"
    rm -f "$pid_file"

    if [ -z "$pid" ]; then
        return 0
    fi

    local cmd
    cmd="$(ps -p "$pid" -o command= 2>/dev/null || true)"
    if [ -z "$cmd" ]; then
        return 0
    fi

    if [[ "$cmd" == *"$process_hint"* ]]; then
        kill -9 "$pid" 2>/dev/null || true
        echo "✅ 已停止 PID=$pid ($process_hint)"
        did_stop=1
    else
        echo "⚠️ 跳过 PID=$pid，命令不匹配预期: $cmd"
    fi
}

echo "[1/3] 停止 API 服务 (ragflow_server.py)..."
kill_from_pid_file "$BACKEND_PID_FILE" "ragflow_server.py"

echo "[2/3] 停止任务执行器 (task_executor.py)..."
shopt -s nullglob
for f in $TASK_PID_GLOB; do
    kill_from_pid_file "$f" "task_executor.py"
done
shopt -u nullglob

if [ "${STOP_NGINX:-0}" = "1" ]; then
    echo "[3/3] 停止前端服务 (nginx)..."
    if command -v brew >/dev/null 2>&1 && brew services list | grep nginx | grep started >/dev/null 2>&1; then
        brew services stop nginx
        echo "✅ nginx 已停止"
    else
        echo "✅ nginx 未运行或不由 brew 管理"
    fi
else
    echo "[3/3] 跳过前端停止（默认不动 nginx）。如需停止请加 STOP_NGINX=1"
fi

echo
echo "=========================================="
if [ "$did_stop" = "1" ]; then
    echo "✅ 当前环境服务已停止"
else
    echo "✅ 当前环境无可停止进程（或 PID 文件缺失）"
fi
echo "=========================================="
