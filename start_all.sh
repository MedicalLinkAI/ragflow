#!/bin/bash
# RAGflow 一键启动脚本（前后端）

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

echo "=========================================="
echo "RAGflow 一键启动脚本"
echo "=========================================="
echo ""

# 创建日志目录
mkdir -p logs

# 1. 启动后端
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步骤 1/2: 启动后端服务"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
bash start_backend.sh
BACKEND_STATUS=$?

if [ $BACKEND_STATUS -ne 0 ]; then
    echo ""
    echo "❌ 后端启动失败，终止启动流程"
    exit 1
fi

echo ""
sleep 3

# 2. 启动前端
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "步骤 2/2: 启动前端服务"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
bash start_frontend.sh
FRONTEND_STATUS=$?

echo ""
echo "=========================================="
if [ $FRONTEND_STATUS -eq 0 ]; then
    echo "✅ RAGflow 启动完成！"
    echo "=========================================="
    echo ""
    echo "📝 访问信息:"
    echo "   访问地址: http://localhost (nginx 统一代理)"
    echo ""
    echo "📊 服务状态:"
    echo "   - PostgreSQL: localhost:5432 ✅"
    echo "   - Redis: localhost:6379 (db:2) ✅"
    echo "   - MinIO: localhost:9000 ✅"
    echo "   - Elasticsearch: localhost:1200 ✅"
    echo "   - Nginx 前端: localhost:80 ✅"
    echo "   - 后端 API: localhost:9380 ✅"
    echo ""
    echo "📋 日志文件:"
    echo "   - 后端: tail -f logs/backend.log"
    echo "   - 前端: tail -f logs/frontend.log"
    echo ""
    echo "🛑 停止服务:"
    echo "   bash stop_all.sh"
    echo ""
    echo "🌐 请在浏览器打开: http://localhost"
    echo "=========================================="
else
    echo "❌ 前端启动失败"
    echo "=========================================="
    exit 1
fi
