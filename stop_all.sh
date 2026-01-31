#!/bin/bash
# RAGflow 停止脚本

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "停止 RAGflow 服务"
echo "=========================================="

# 停止 API 服务
echo "[1/3] 停止 API 服务 (ragflow_server.py)..."
BACKEND_PIDS=$(ps aux | grep "python.*ragflow_server.py" | grep -v grep | awk '{print $2}')
if [ -n "$BACKEND_PIDS" ]; then
    echo "发现 API 服务进程: $BACKEND_PIDS"
    echo "$BACKEND_PIDS" | xargs kill -9 2>/dev/null || true
    echo "✅ API 服务已停止"
else
    echo "✅ API 服务未运行"
fi

# 停止任务执行器
echo "[2/3] 停止任务执行器 (task_executor.py)..."
EXECUTOR_PIDS=$(ps aux | grep "python.*task_executor.py" | grep -v grep | awk '{print $2}')
if [ -n "$EXECUTOR_PIDS" ]; then
    echo "发现任务执行器进程: $EXECUTOR_PIDS"
    echo "$EXECUTOR_PIDS" | xargs kill -9 2>/dev/null || true
    echo "✅ 任务执行器已停止"
else
    echo "✅ 任务执行器未运行"
fi

# 停止前端 (nginx)
echo "[3/3] 停止前端服务 (nginx)..."
if brew services list | grep nginx | grep started >/dev/null 2>&1; then
    brew services stop nginx
    echo "✅ nginx 已停止"
else
    echo "✅ nginx 未运行"
fi

echo ""
echo "✅ 所有服务已停止"
echo "=========================================="
