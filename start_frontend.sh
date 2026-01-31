#!/bin/bash
# RAGflow 前端服务启动脚本

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR/web"

echo "=========================================="
echo "RAGflow 前端服务启动脚本"
echo "=========================================="

# 1. 检测并清理旧进程
echo "[1/5] 检测旧的前端进程..."
OLD_PIDS=$(lsof -ti:8888 2>/dev/null || true)
if [ -n "$OLD_PIDS" ]; then
    echo "发现旧进程在端口 8888: $OLD_PIDS"
    echo "$OLD_PIDS" | xargs kill -9 2>/dev/null || true
    sleep 2
    echo "✅ 旧进程已清理"
else
    echo "✅ 无旧进程"
fi

# 2. 检查 Node.js 环境
echo "[2/5] 检查 Node.js 环境..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js 未安装"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo "❌ npm 未安装"
    exit 1
fi

NODE_VERSION=$(node --version)
echo "✅ Node.js 版本: $NODE_VERSION"

# 3. 检查并安装依赖
echo "[3/5] 检查前端依赖..."
if [ ! -d "node_modules" ] || [ ! -d "node_modules/.bin" ]; then
    echo "⚠️  依赖缺失，正在安装..."
    rm -rf node_modules package-lock.json
    npm install --legacy-peer-deps
    echo "✅ 依赖安装完成"
else
    echo "✅ 依赖已存在"
fi

# 检查 monaco-editor
if [ ! -d "node_modules/monaco-editor" ]; then
    echo "⚠️  monaco-editor 缺失，正在安装..."
    npm install monaco-editor --legacy-peer-deps
fi

# 4. 重新构建前端
echo "[4/5] 构建前端..."
rm -rf dist
npm run build

if [ ! -d "dist" ] || [ ! -f "dist/index.html" ]; then
    echo "❌ 前端构建失败"
    exit 1
fi

echo "✅ 前端构建完成"

# 5. 启动 nginx
echo "[5/5] 启动 nginx..."

# 检查 nginx 配置
if ! nginx -t 2>/dev/null; then
    echo "❌ nginx 配置有误"
    exit 1
fi

# 停止旧的 nginx
brew services stop nginx 2>/dev/null || true
sleep 2

# 启动 nginx
brew services start nginx

# 等待启动
echo "等待 nginx 启动..."
for i in {1..15}; do
    if nc -z localhost 80 2>/dev/null; then
        echo "✅ 前端服务启动成功！"
        echo "   服务: nginx"
        echo "   访问地址: http://localhost"
        echo "   配置文件: /opt/homebrew/etc/nginx/servers/ragflow.conf"
        echo ""
        echo "🌐 请在浏览器打开: http://localhost"
        exit 0
    fi
    sleep 1
done

echo "❌ nginx 启动失败"
brew services list | grep nginx
nginx -t
exit 1
