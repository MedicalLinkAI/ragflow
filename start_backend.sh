#!/bin/bash
# RAGflow 后端服务启动脚本（按环境配置隔离）
# 包含 API 服务 (ragflow_server.py) 和异步任务执行器 (task_executor.py)

set -euo pipefail

# Raise the descriptor ceiling for GraphRAG-style concurrent workloads on Linux hosts.
ulimit -n 1048575

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

TASK_EXECUTOR_COUNT=${WS:-1}

if [ -z "${RAGFLOW_ENV:-}" ] && [ -z "${RAGFLOW_CONF:-}" ]; then
    echo "❌ 必须显式指定 RAGFLOW_ENV 或 RAGFLOW_CONF，禁止使用默认配置启动"
    echo "示例: RAGFLOW_ENV=dev WS=1 bash start_backend.sh"
    exit 1
fi

mkdir -p logs run/pids

if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，请先运行 'uv sync --python 3.12'"
    exit 1
fi

# shellcheck disable=SC1091
source .venv/bin/activate

export PYTHONPATH="$SCRIPT_DIR"
export HF_ENDPOINT="${HF_ENDPOINT:-https://hf-mirror.com}"
export NLTK_DATA="${NLTK_DATA:-$SCRIPT_DIR/.venv/nltk_data}"
export DB_TYPE="${DB_TYPE:-postgres}"

if [ ! -d "$NLTK_DATA" ] && [ -d "$HOME/nltk_data" ]; then
    mkdir -p "$NLTK_DATA"
    cp -r "$HOME/nltk_data"/* "$NLTK_DATA"/ 2>/dev/null || true
fi

eval "$(python scripts/resolve_runtime_conf.py --format shell)"

ENV_SLUG="$(echo "${ACTIVE_ENV:-default}" | tr ' /:' '___')"
PID_DIR="run/pids/${ENV_SLUG}"
mkdir -p "$PID_DIR"

BACKEND_PID_FILE="$PID_DIR/backend.pid"
TASK_PID_GLOB="$PID_DIR/task_executor_*.pid"

BACKEND_LOG_FILE="logs/backend.${ENV_SLUG}.log"
TASK_LOG_PREFIX="logs/task_executor_${ENV_SLUG}"

echo "=========================================="
echo "RAGflow 后端服务启动脚本"
echo "=========================================="
echo "  - 环境: ${ACTIVE_ENV}"
echo "  - 配置文件: ${ACTIVE_CONF_PATH}"
echo "  - 叠加配置: ${APPLIED_CONF_PATHS}"
if [ -n "${LOCAL_CONF_PATHS}" ]; then
    echo "  - 本地覆盖: ${LOCAL_CONF_PATHS}"
fi
echo "  - API 服务: ragflow_server.py (${RAGFLOW_HOST}:${RAGFLOW_PORT})"
echo "  - 管理端口: ${ADMIN_HOST}:${ADMIN_PORT}"
echo "  - 任务执行器: task_executor.py x${TASK_EXECUTOR_COUNT}"
echo "=========================================="

kill_from_pid_file() {
    local pid_file="$1"
    local process_hint="$2"

    if [ ! -f "$pid_file" ]; then
        return 0
    fi

    local pid
    pid="$(cat "$pid_file" 2>/dev/null || true)"
    if [ -z "$pid" ]; then
        rm -f "$pid_file"
        return 0
    fi

    local cmd
    cmd="$(ps -p "$pid" -o command= 2>/dev/null || true)"
    if [ -z "$cmd" ]; then
        rm -f "$pid_file"
        return 0
    fi

    if [[ "$cmd" == *"$process_hint"* ]]; then
        kill -9 "$pid" 2>/dev/null || true
        echo "已停止历史进程 PID=$pid ($process_hint)"
    else
        echo "⚠️ 跳过 PID=$pid，命令不匹配预期: $cmd"
    fi

    rm -f "$pid_file"
}

get_listen_pid_by_port() {
    local port="$1"
    lsof -nP -tiTCP:"$port" -sTCP:LISTEN 2>/dev/null | head -n 1 || true
}

ensure_api_port_safe() {
    local port="$1"
    local listen_pid
    listen_pid="$(get_listen_pid_by_port "$port")"

    if [ -z "$listen_pid" ]; then
        return 0
    fi

    local cmd
    cmd="$(ps -p "$listen_pid" -o command= 2>/dev/null || true)"
    if [[ "$cmd" == *"ragflow_server.py"* ]]; then
        echo "❌ 端口 ${port} 上仍有 ragflow_server.py 进程（PID=${listen_pid}），请先用 stop 脚本清理"
        exit 1
    fi

    echo "❌ 端口 ${port} 已被非 ragflow_server.py 进程占用，拒绝启动避免误伤"
    echo "   PID=${listen_pid} CMD=${cmd}"
    exit 1
}

check_tcp() {
    local host="$1"
    local port="$2"
    local name="$3"

    if ! nc -z "$host" "$port" 2>/dev/null; then
        echo "❌ 依赖不可达: ${name} (${host}:${port})"
        return 1
    fi
    echo "✅ ${name} 可达 (${host}:${port})"
}

check_http_healthz() {
    local url="$1"
    local code
    local body

    if command -v curl >/dev/null 2>&1; then
        body="$(mktemp)"
        code="$(curl -sS -m 8 -o "$body" -w '%{http_code}' "$url" || true)"
        if [ "$code" != "200" ]; then
            echo "❌ 健康检查失败: ${url} (HTTP=${code:-000})"
            [ -s "$body" ] && head -c 300 "$body" && echo
            rm -f "$body"
            return 1
        fi
        echo "✅ 健康检查通过: ${url} (HTTP=${code})"
        head -c 300 "$body" && echo
        rm -f "$body"
        return 0
    fi

    python - "$url" <<'PY'
import json
import sys
import urllib.request

url = sys.argv[1]
try:
    with urllib.request.urlopen(url, timeout=8) as resp:
        body = resp.read(300).decode("utf-8", errors="replace")
        print(f"✅ 健康检查通过: {url} (HTTP={resp.status})")
        print(body)
        if resp.status != 200:
            raise SystemExit(1)
except Exception as ex:
    print(f"❌ 健康检查失败: {url} ({ex})")
    raise SystemExit(1)
PY
}

# 1. 清理当前环境历史 PID（不全局扫杀）
echo "[1/5] 检测并清理当前环境旧进程..."
kill_from_pid_file "$BACKEND_PID_FILE" "ragflow_server.py"
shopt -s nullglob
for f in $TASK_PID_GLOB; do
    kill_from_pid_file "$f" "task_executor.py"
done
shopt -u nullglob
ensure_api_port_safe "${RAGFLOW_PORT}"
sleep 1

# 2. 检查依赖环境（按配置文件读取）
echo "[2/5] 检查依赖环境..."
if [ "${DB_TYPE}" = "postgres" ]; then
    check_tcp "${POSTGRES_HOST}" "${POSTGRES_PORT}" "PostgreSQL"
else
    check_tcp "${MYSQL_HOST}" "${MYSQL_PORT}" "MySQL"
fi
check_tcp "${REDIS_HOST}" "${REDIS_PORT}" "Redis"
check_tcp "${MINIO_HOST}" "${MINIO_PORT}" "MinIO"

DOC_ENGINE_VAL="${DOC_ENGINE:-elasticsearch}"
echo "   - DOC_ENGINE=${DOC_ENGINE_VAL}"
if [ "${DOC_ENGINE_VAL}" = "elasticsearch" ]; then
    check_tcp "${ES_HOST}" "${ES_PORT}" "Elasticsearch"
fi

echo "✅ 依赖服务检查完成"

# 3. 环境信息展示
echo "[3/5] 当前环境配置..."
echo "   - RAGFLOW_ENV=${ACTIVE_ENV}"
echo "   - RAGFLOW_CONF=${ACTIVE_CONF_NAME}"
echo "   - APPLIED_CONF_PATHS=${APPLIED_CONF_PATHS}"
if [ -n "${LOCAL_CONF_PATHS}" ]; then
    echo "   - LOCAL_CONF_PATHS=${LOCAL_CONF_PATHS}"
fi

# 4. 启动 API 服务
echo "[4/5] 启动 API 服务 (ragflow_server.py)..."
nohup python api/ragflow_server.py > "$BACKEND_LOG_FILE" 2>&1 &
BACKEND_PID=$!
echo "$BACKEND_PID" > "$BACKEND_PID_FILE"

for _ in {1..30}; do
    LISTEN_PID="$(get_listen_pid_by_port "${RAGFLOW_PORT}")"
    if ps -p "$BACKEND_PID" >/dev/null 2>&1 && [ -n "$LISTEN_PID" ] && [ "$LISTEN_PID" = "$BACKEND_PID" ]; then
        echo "✅ API 服务启动成功！(PID: $BACKEND_PID)"
        break
    fi
    sleep 1
done

LISTEN_PID="$(get_listen_pid_by_port "${RAGFLOW_PORT}")"
if ! ps -p "$BACKEND_PID" >/dev/null 2>&1 || [ -z "$LISTEN_PID" ] || [ "$LISTEN_PID" != "$BACKEND_PID" ]; then
    echo "❌ API 服务启动失败，请检查日志: ${BACKEND_LOG_FILE}"
    echo "   当前端口监听 PID: ${LISTEN_PID:-none}，预期 PID: ${BACKEND_PID}"
    tail -50 "$BACKEND_LOG_FILE" || true
    exit 1
fi

# 5. 启动任务执行器
echo "[5/6] 启动任务执行器 (task_executor.py x${TASK_EXECUTOR_COUNT})..."

TASK_CUDA_VISIBLE_DEVICES_LIST="${TASK_CUDA_VISIBLE_DEVICES_LIST:-}"
TASK_CUDA_DEVICES=()
if [ -n "$TASK_CUDA_VISIBLE_DEVICES_LIST" ]; then
    IFS="," read -r -a TASK_CUDA_DEVICES <<< "$TASK_CUDA_VISIBLE_DEVICES_LIST"
fi

RUNNING_EXECUTORS=0
for ((i=0; i<TASK_EXECUTOR_COUNT; i++)); do
    EXECUTOR_LOG="${TASK_LOG_PREFIX}_${i}.log"
    EXECUTOR_PID_FILE="$PID_DIR/task_executor_${i}.pid"
    if [ ${#TASK_CUDA_DEVICES[@]} -gt 0 ] && [ -n "${TASK_CUDA_DEVICES[$i]:-}" ]; then
        CUDA_VISIBLE_DEVICES="${TASK_CUDA_DEVICES[$i]}" nohup python rag/svr/task_executor.py "$i" > "$EXECUTOR_LOG" 2>&1 &
    else
        nohup python rag/svr/task_executor.py "$i" > "$EXECUTOR_LOG" 2>&1 &
    fi
    EXECUTOR_PID=$!
    echo "$EXECUTOR_PID" > "$EXECUTOR_PID_FILE"
    echo "  启动任务执行器 $i (PID: $EXECUTOR_PID)"
done

sleep 2
for ((i=0; i<TASK_EXECUTOR_COUNT; i++)); do
    EXECUTOR_PID_FILE="$PID_DIR/task_executor_${i}.pid"
    if [ -f "$EXECUTOR_PID_FILE" ] && ps -p "$(cat "$EXECUTOR_PID_FILE")" >/dev/null 2>&1; then
        RUNNING_EXECUTORS=$((RUNNING_EXECUTORS + 1))
    fi
done

if [ "$RUNNING_EXECUTORS" -ge "$TASK_EXECUTOR_COUNT" ]; then
    echo "✅ 任务执行器启动成功！(${RUNNING_EXECUTORS} 个)"
else
    echo "⚠️  部分任务执行器可能未启动 (期望: $TASK_EXECUTOR_COUNT, 实际: $RUNNING_EXECUTORS)"
fi

# 6. 脚本内客观核验（同一链路内完成）
echo "[6/6] 启动后客观核验..."
echo "   - backend.pid=$(cat "$BACKEND_PID_FILE" 2>/dev/null || echo missing)"
if ! ps -p "$BACKEND_PID" >/dev/null 2>&1; then
    echo "❌ backend PID 不存在: $BACKEND_PID"
    exit 1
fi

LISTEN_PID="$(get_listen_pid_by_port "${RAGFLOW_PORT}")"
if [ -z "$LISTEN_PID" ] || [ "$LISTEN_PID" != "$BACKEND_PID" ]; then
    echo "❌ 端口监听校验失败: port=${RAGFLOW_PORT}, listen_pid=${LISTEN_PID:-none}, expected=${BACKEND_PID}"
    exit 1
fi

if [ "$RUNNING_EXECUTORS" -lt "$TASK_EXECUTOR_COUNT" ]; then
    echo "❌ 任务执行器数量不足，启动校验失败"
    exit 1
fi

check_http_healthz "http://127.0.0.1:${RAGFLOW_PORT}/v1/system/healthz"

echo
echo "=========================================="
echo "✅ RAGflow 后端服务启动完成！"
echo "=========================================="
echo "📊 服务状态:"
echo "   - 环境: ${ACTIVE_ENV}"
echo "   - 配置: ${ACTIVE_CONF_PATH}"
echo "   - API 地址: http://127.0.0.1:${RAGFLOW_PORT}"
echo "   - API PID 文件: ${BACKEND_PID_FILE}"
echo "📋 日志文件:"
echo "   - API 服务: tail -f ${BACKEND_LOG_FILE}"
echo "   - 任务执行器: tail -f ${TASK_LOG_PREFIX}_*.log"
echo "🔧 调整执行器数量: WS=4 RAGFLOW_ENV=${ACTIVE_ENV} bash start_backend.sh"
echo "=========================================="
