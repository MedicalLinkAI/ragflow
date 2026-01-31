#!/bin/bash
# RAGflow 启动脚本

cd "$(dirname "$0")"

echo "正在启动 RAGflow..."

# 激活虚拟环境
source .venv/bin/activate

# 设置环境变量
export PYTHONPATH=$(pwd)
export HF_ENDPOINT=https://hf-mirror.com
export NLTK_DATA=$(pwd)/.venv/nltk_data
export DB_TYPE=postgres

# 启动后端服务
python api/ragflow_server.py

echo "RAGflow 已停止"
