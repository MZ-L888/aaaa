#!/bin/bash

# Render构建脚本
echo "开始构建Gemini Balance应用..."

# 安装Python依赖
echo "安装Python依赖..."
pip install --upgrade pip
pip install -r requirements.txt

# 创建必要的目录
echo "创建必要的目录..."
mkdir -p app/log
mkdir -p app/database

# 设置权限
echo "设置文件权限..."
chmod +x build.sh

echo "构建完成！"
