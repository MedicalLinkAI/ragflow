#!/bin/bash
# RAGflow 访问测试脚本

echo "=========================================="
echo "RAGflow 部署验证"
echo "=========================================="

echo ""
echo "1. 测试前端首页 (http://localhost/)..."
FRONTEND=$(curl -s http://localhost/ | grep -o '<title>RAGFlow</title>')
if [ "$FRONTEND" == "<title>RAGFlow</title>" ]; then
    echo "   ✅ 前端首页正常"
else
    echo "   ❌ 前端首页异常"
    exit 1
fi

echo ""
echo "2. 测试前端路由 (http://localhost/login)..."
LOGIN=$(curl -s http://localhost/login | grep -o '<title>RAGFlow</title>')
if [ "$LOGIN" == "<title>RAGFlow</title>" ]; then
    echo "   ✅ 前端 SPA 路由正常"
else
    echo "   ❌ 前端路由异常"
    exit 1
fi

echo ""
echo "3. 测试 API 代理 (http://localhost/v1/...)..."
API=$(curl -s http://localhost/v1/user/login -X POST -H "Content-Type: application/json" -d '{}' | python3 -c "import sys,json; print(json.load(sys.stdin)['code'])" 2>/dev/null)
if [ "$API" == "109" ]; then
    echo "   ✅ API 代理正常"
else
    echo "   ❌ API 代理异常"
    exit 1
fi

echo ""
echo "4. 测试后端直连 (http://localhost:9380)..."
BACKEND=$(curl -s http://localhost:9380/v1/user/login -X POST -H "Content-Type: application/json" -d '{}' | python3 -c "import sys,json; print(json.load(sys.stdin)['code'])" 2>/dev/null)
if [ "$BACKEND" == "109" ]; then
    echo "   ✅ 后端 API 正常"
else
    echo "   ❌ 后端 API 异常"
    exit 1
fi

echo ""
echo "=========================================="
echo "✅ 所有测试通过！"
echo "=========================================="
echo ""
echo "🌐 请在浏览器打开: http://localhost"
echo ""
echo "📋 说明:"
echo "   - 前端通过 nginx 提供 (80 端口)"
echo "   - API 请求自动代理到后端 (9380 端口)"
echo "   - 支持 SPA 前端路由 (/login, /dataset 等)"
echo ""
