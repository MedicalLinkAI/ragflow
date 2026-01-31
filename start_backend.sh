#!/bin/bash
# RAGflow 后端服务启动脚本
# 包含 API 服务 (ragflow_server.py) 和异步任务执行器 (task_executor.py)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

# Task Executor 数量 (可通过环境变量 WS 设置)
TASK_EXECUTOR_COUNT=${WS:-1}

echo "=========================================="
echo "RAGflow 后端服务启动脚本"
echo "=========================================="
echo "  - API 服务: ragflow_server.py"
echo "  - 任务执行器: task_executor.py x${TASK_EXECUTOR_COUNT}"
echo "=========================================="

# 1. 检测并清理旧进程
echo "[1/5] 检测旧的后端进程..."

# 清理 ragflow_server.py
OLD_SERVER_PIDS=$(ps aux | grep "python.*ragflow_server.py" | grep -v grep | awk '{print $2}')
if [ -n "$OLD_SERVER_PIDS" ]; then
    echo "发现旧 API 服务进程: $OLD_SERVER_PIDS"
    echo "$OLD_SERVER_PIDS" | xargs kill -9 2>/dev/null || true
    echo "✅ API 服务进程已清理"
else
    echo "✅ 无旧 API 服务进程"
fi

# 清理 task_executor.py
OLD_EXECUTOR_PIDS=$(ps aux | grep "python.*task_executor.py" | grep -v grep | awk '{print $2}')
if [ -n "$OLD_EXECUTOR_PIDS" ]; then
    echo "发现旧任务执行器进程: $OLD_EXECUTOR_PIDS"
    echo "$OLD_EXECUTOR_PIDS" | xargs kill -9 2>/dev/null || true
    echo "✅ 任务执行器进程已清理"
else
    echo "✅ 无旧任务执行器进程"
fi

sleep 2

# 2. 检查依赖环境
echo "[2/5] 检查依赖环境..."
if [ ! -d ".venv" ]; then
    echo "❌ 虚拟环境不存在，请先运行 'uv sync --python 3.12'"
    exit 1
fi

if [ ! -d ".venv/nltk_data" ]; then
    echo "⚠️  NLTK 数据缺失，正在复制..."
    mkdir -p .venv/nltk_data
    cp -r ~/nltk_data/* .venv/nltk_data/ 2>/dev/null || true
fi

# 检查 PostgreSQL
if ! nc -z localhost 5432 2>/dev/null; then
    echo "❌ PostgreSQL 未运行 (端口 5432)"
    exit 1
fi

# 检查 Redis
if ! nc -z localhost 6379 2>/dev/null; then
    echo "❌ Redis 未运行 (端口 6379)"
    exit 1
fi

# 检查 MinIO
if ! nc -z localhost 9000 2>/dev/null; then
    echo "❌ MinIO 未运行 (端口 9000)"
    exit 1
fi

# 检查 Elasticsearch
if ! nc -z localhost 1200 2>/dev/null; then
    echo "⚠️  Elasticsearch 未运行 (端口 1200)，正在启动..."
    docker-compose -f docker-compose-es.yml up -d
    sleep 10
fi

echo "✅ 依赖服务检查完成"

# 3. 设置环境变量
echo "[3/5] 设置环境变量..."
export PYTHONPATH="$SCRIPT_DIR"
export HF_ENDPOINT=https://hf-mirror.com
export NLTK_DATA="$SCRIPT_DIR/.venv/nltk_data"
export DB_TYPE=postgres

# 4. 启动后端服务
echo "[4/5] 启动 API 服务 (ragflow_server.py)..."
source .venv/bin/activate

# 后台启动 API 服务
nohup python api/ragflow_server.py > logs/backend.log 2>&1 &
BACKEND_PID=$!

# 等待 API 服务启动
echo "等待 API 服务启动..."
for i in {1..30}; do
    if nc -z localhost 9380 2>/dev/null; then
        echo "✅ API 服务启动成功！(PID: $BACKEND_PID)"
        break
    fi
    sleep 1
done

if ! nc -z localhost 9380 2>/dev/null; then
    echo "❌ API 服务启动失败，请检查日志:"
    tail -50 logs/backend.log
    exit 1
fi

# 5. 启动任务执行器
echo "[5/5] 启动任务执行器 (task_executor.py x${TASK_EXECUTOR_COUNT})..."

EXECUTOR_PIDS=""
for ((i=0; i<TASK_EXECUTOR_COUNT; i++)); do
    nohup python rag/svr/task_executor.py "$i" > "logs/task_executor_${i}.log" 2>&1 &
    EXECUTOR_PID=$!
    EXECUTOR_PIDS="$EXECUTOR_PIDS $EXECUTOR_PID"
    echo "  启动任务执行器 $i (PID: $EXECUTOR_PID)"
done

# 等待任务执行器启动
sleep 3

# 检查任务执行器是否运行
RUNNING_EXECUTORS=$(ps aux | grep "python.*task_executor.py" | grep -v grep | wc -l | tr -d ' ')
if [ "$RUNNING_EXECUTORS" -ge "$TASK_EXECUTOR_COUNT" ]; then
    echo "✅ 任务执行器启动成功！(${RUNNING_EXECUTORS} 个)"
else
    echo "⚠️  部分任务执行器可能未启动 (期望: $TASK_EXECUTOR_COUNT, 实际: $RUNNING_EXECUTORS)"
fi

echo ""
echo "=========================================="
echo "✅ RAGflow 后端服务启动完成！"
echo "=========================================="
echo ""
echo "📊 服务状态:"
echo "   - API 服务 PID: $BACKEND_PID"
echo "   - 任务执行器 PIDs:$EXECUTOR_PIDS"
echo "   - API 地址: http://localhost:9380"
echo ""
echo "📋 日志文件:"
echo "   - API 服务: tail -f logs/backend.log"
echo "   - 任务执行器: tail -f logs/task_executor_*.log"
echo ""
echo "🔧 调整执行器数量: WS=4 bash start_backend.sh"
echo "=========================================="
exit 0
