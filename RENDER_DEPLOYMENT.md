# Gemini Balance - Render部署指南

## 概述
本指南将帮助您在Render平台上部署Gemini Balance应用程序。

## 前置要求
1. GitHub账户（项目已上传到：https://github.com/MZ-L888/aaaa）
2. Render账户（免费注册：https://render.com）
3. Google Gemini API密钥

## 部署步骤

### 方法一：使用render.yaml自动部署（推荐）

1. **登录Render控制台**
   - 访问 https://render.com
   - 使用GitHub账户登录

2. **创建新的Web Service**
   - 点击 "New +" 按钮
   - 选择 "Web Service"
   - 连接您的GitHub仓库：`MZ-L888/aaaa`

3. **配置部署设置**
   - **Name**: `gemini-balance`
   - **Environment**: `Python 3`
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `chmod +x start.sh && ./start.sh`
   - **Plan**: `Free`

4. **设置环境变量**
   在Environment Variables部分添加以下变量：

   ```
   DATABASE_TYPE=sqlite
   SQLITE_DATABASE=gemini_balance.db
   API_KEYS=["your_gemini_api_key_here"]
   ALLOWED_TOKENS=["your_auth_token_here"]
   AUTH_TOKEN=your_auth_token_here
   BASE_URL=https://generativelanguage.googleapis.com/v1beta
   TEST_MODEL=gemini-1.5-flash
   TOOLS_CODE_EXECUTION_ENABLED=false
   IMAGE_MODELS=["gemini-2.0-flash-exp"]
   SEARCH_MODELS=["gemini-2.0-flash-exp","gemini-2.0-pro-exp"]
   URL_NORMALIZATION_ENABLED=false
   SHOW_SEARCH_LINK=true
   SHOW_THINKING_PROCESS=true
   LOG_LEVEL=info
   TIMEZONE=Asia/Shanghai
   FAKE_STREAM_ENABLED=true
   ```

   **重要**: 请将 `your_gemini_api_key_here` 和 `your_auth_token_here` 替换为您的实际密钥！

### 方法二：使用Blueprint部署

1. **Fork仓库到您的GitHub账户**
2. **点击Deploy to Render按钮**（如果可用）
3. **或者在Render中选择Blueprint部署**
   - 选择您的GitHub仓库
   - Render会自动读取 `render.yaml` 配置

## 配置API密钥

### 获取Gemini API密钥
1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 创建新的API密钥
3. 复制密钥并保存

### 在Render中设置密钥
1. 进入您的服务设置页面
2. 找到 "Environment Variables" 部分
3. 更新以下变量：
   - `API_KEYS`: `["您的Gemini API密钥"]`
   - `ALLOWED_TOKENS`: `["您的认证令牌"]`
   - `AUTH_TOKEN`: `您的认证令牌`

## 部署后验证

1. **检查部署状态**
   - 在Render控制台查看部署日志
   - 确保没有错误信息

2. **访问应用**
   - 使用Render提供的URL访问您的应用
   - 格式通常为：`https://gemini-balance.onrender.com`

3. **测试API**
   ```bash
   curl -X POST "https://your-app.onrender.com/v1/chat/completions" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer your_auth_token_here" \
     -d '{
       "model": "gemini-1.5-flash",
       "messages": [{"role": "user", "content": "Hello!"}]
     }'
   ```

## 常见问题

### 1. 部署失败
- 检查构建日志中的错误信息
- 确保所有环境变量都已正确设置
- 验证API密钥的有效性

### 2. 应用无法启动
- 检查启动日志
- 确保端口配置正确（Render会自动设置$PORT）
- 验证数据库连接

### 3. API请求失败
- 检查API密钥是否正确
- 验证认证令牌设置
- 查看应用日志了解详细错误

## 免费版限制

Render免费版有以下限制：
- 750小时/月的运行时间
- 应用在无活动时会休眠
- 512MB RAM
- 无持久化存储（重启后数据丢失）

## 升级建议

对于生产环境，建议：
1. 升级到付费计划获得更好的性能
2. 使用外部数据库（如PostgreSQL）
3. 配置自定义域名
4. 设置监控和告警

## 支持

如果遇到问题：
1. 查看Render官方文档
2. 检查项目的GitHub Issues
3. 联系技术支持

---

**注意**: 请确保妥善保管您的API密钥，不要在公开场所分享！
