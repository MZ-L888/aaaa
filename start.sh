#!/bin/bash

# Render启动脚本
echo "启动Gemini Balance应用..."

# 设置环境变量
export PYTHONPATH=/opt/render/project/src:$PYTHONPATH

# 验证关键环境变量
echo "验证环境变量..."
if [ -z "$API_KEYS" ]; then
    echo "警告: API_KEYS 环境变量未设置，使用默认值"
    export API_KEYS='["demo-key-please-replace"]'
fi

if [ -z "$ALLOWED_TOKENS" ]; then
    echo "警告: ALLOWED_TOKENS 环境变量未设置，使用默认值"
    export ALLOWED_TOKENS='["demo-token-please-replace"]'
fi

if [ -z "$AUTH_TOKEN" ]; then
    echo "警告: AUTH_TOKEN 环境变量未设置，使用默认值"
    export AUTH_TOKEN="demo-token-please-replace"
fi

# 显示配置信息
echo "数据库类型: ${DATABASE_TYPE:-sqlite}"
echo "使用端口: $PORT"
echo "API Keys 已配置: $(echo $API_KEYS | grep -o '\[.*\]' | wc -c) 字符"

# 启动应用
uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1
