#!/bin/bash

# Render启动脚本
echo "启动Gemini Balance应用..."

# 设置环境变量
export PYTHONPATH=/opt/render/project/src:$PYTHONPATH

# 设置默认环境变量（如果未设置）
export DATABASE_TYPE=${DATABASE_TYPE:-sqlite}
export SQLITE_DATABASE=${SQLITE_DATABASE:-gemini_balance.db}
export API_KEYS=${API_KEYS:-'["AIzaSyDEMO_KEY_REPLACE_WITH_YOUR_ACTUAL_KEY"]'}
export ALLOWED_TOKENS=${ALLOWED_TOKENS:-'["sk-demo-token-replace-with-your-token"]'}
export AUTH_TOKEN=${AUTH_TOKEN:-sk-demo-token-replace-with-your-token}
export BASE_URL=${BASE_URL:-https://generativelanguage.googleapis.com/v1beta}
export TEST_MODEL=${TEST_MODEL:-gemini-1.5-flash}
export TOOLS_CODE_EXECUTION_ENABLED=${TOOLS_CODE_EXECUTION_ENABLED:-false}
export IMAGE_MODELS=${IMAGE_MODELS:-'["gemini-2.0-flash-exp"]'}
export SEARCH_MODELS=${SEARCH_MODELS:-'["gemini-2.0-flash-exp","gemini-2.0-pro-exp"]'}
export FILTERED_MODELS=${FILTERED_MODELS:-'["gemini-1.0-pro-vision-latest","gemini-pro-vision"]'}
export URL_NORMALIZATION_ENABLED=${URL_NORMALIZATION_ENABLED:-false}
export SHOW_SEARCH_LINK=${SHOW_SEARCH_LINK:-true}
export SHOW_THINKING_PROCESS=${SHOW_THINKING_PROCESS:-true}
export MAX_FAILURES=${MAX_FAILURES:-10}
export MAX_RETRIES=${MAX_RETRIES:-3}
export TIME_OUT=${TIME_OUT:-300}
export TIMEZONE=${TIMEZONE:-Asia/Shanghai}
export LOG_LEVEL=${LOG_LEVEL:-info}
export FAKE_STREAM_ENABLED=${FAKE_STREAM_ENABLED:-true}
export STREAM_OPTIMIZER_ENABLED=${STREAM_OPTIMIZER_ENABLED:-false}
export PROXIES=${PROXIES:-'[]'}
export VERTEX_API_KEYS=${VERTEX_API_KEYS:-'[]'}
export THINKING_MODELS=${THINKING_MODELS:-'[]'}
export CUSTOM_HEADERS=${CUSTOM_HEADERS:-'{}'}

# 显示配置信息
echo "数据库类型: $DATABASE_TYPE"
echo "使用端口: $PORT"
echo "API Keys 长度: $(echo $API_KEYS | wc -c) 字符"
echo "环境变量设置完成"

# 启动应用
echo "启动 uvicorn 服务器..."
uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1 --log-level info
