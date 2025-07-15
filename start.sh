#!/bin/bash

# Render启动脚本
echo "启动Gemini Balance应用..."

# 设置环境变量
export PYTHONPATH=/opt/render/project/src:$PYTHONPATH

# 启动应用
echo "使用端口: $PORT"
uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1
