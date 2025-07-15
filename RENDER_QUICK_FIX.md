# Render 部署快速修复指南

## 问题诊断
您遇到的错误是因为 `API_KEYS` 环境变量的 JSON 格式解析失败。

## 立即修复步骤

### 1. 在 Render 控制台中设置正确的环境变量

登录 Render 控制台，找到您的服务，进入 "Environment" 设置页面，确保以下环境变量格式正确：

```
API_KEYS=["AIzaSyYOUR_ACTUAL_GEMINI_API_KEY_HERE"]
ALLOWED_TOKENS=["sk-your-custom-auth-token-here"]
AUTH_TOKEN=sk-your-custom-auth-token-here
```

**重要提示：**
- 确保 JSON 数组格式正确，使用双引号
- 不要有多余的空格或换行符
- 替换为您的实际 API 密钥

### 2. 获取 Gemini API 密钥

1. 访问 [Google AI Studio](https://makersuite.google.com/app/apikey)
2. 点击 "Create API Key"
3. 复制生成的密钥（格式类似：AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX）

### 3. 设置自定义认证令牌

为了安全，请设置一个自定义的认证令牌：
```
ALLOWED_TOKENS=["sk-your-secret-token-123456"]
AUTH_TOKEN=sk-your-secret-token-123456
```

### 4. 完整的环境变量列表

在 Render 环境变量设置中，确保以下变量都已正确设置：

```
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance.db
API_KEYS=["AIzaSyYOUR_ACTUAL_GEMINI_API_KEY_HERE"]
ALLOWED_TOKENS=["sk-your-custom-auth-token-here"]
AUTH_TOKEN=sk-your-custom-auth-token-here
BASE_URL=https://generativelanguage.googleapis.com/v1beta
TEST_MODEL=gemini-1.5-flash
TOOLS_CODE_EXECUTION_ENABLED=false
IMAGE_MODELS=["gemini-2.0-flash-exp"]
SEARCH_MODELS=["gemini-2.0-flash-exp","gemini-2.0-pro-exp"]
FILTERED_MODELS=["gemini-1.0-pro-vision-latest","gemini-pro-vision"]
URL_NORMALIZATION_ENABLED=false
SHOW_SEARCH_LINK=true
SHOW_THINKING_PROCESS=true
MAX_FAILURES=10
MAX_RETRIES=3
TIME_OUT=300
TIMEZONE=Asia/Shanghai
LOG_LEVEL=info
FAKE_STREAM_ENABLED=true
STREAM_OPTIMIZER_ENABLED=false
PROXIES=[]
VERTEX_API_KEYS=[]
THINKING_MODELS=[]
CUSTOM_HEADERS={}
```

### 5. 重新部署

设置完环境变量后：
1. 在 Render 控制台点击 "Manual Deploy" 按钮
2. 或者推送一个新的提交到 GitHub 触发自动部署

### 6. 验证部署

部署成功后，您应该能够：
1. 访问应用的 URL（通常是 https://your-service-name.onrender.com）
2. 看到应用正常启动的日志
3. 测试 API 端点

### 7. 测试 API

使用以下命令测试您的 API：

```bash
curl -X POST "https://your-service-name.onrender.com/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-custom-auth-token-here" \
  -d '{
    "model": "gemini-1.5-flash",
    "messages": [{"role": "user", "content": "Hello, test message!"}]
  }'
```

## 常见问题

### Q: 仍然出现 JSON 解析错误
A: 检查环境变量值是否包含特殊字符或换行符，确保使用标准的 JSON 数组格式。

### Q: API 密钥无效
A: 确认您的 Gemini API 密钥是有效的，并且已启用相应的 API 服务。

### Q: 应用启动后立即崩溃
A: 检查 Render 日志，通常是环境变量配置问题或依赖项安装失败。

## 紧急联系

如果问题仍然存在，请：
1. 检查 Render 服务的日志输出
2. 确认所有环境变量都已正确设置
3. 验证 API 密钥的有效性

---

**安全提醒：** 请妥善保管您的 API 密钥，不要在公开场所分享！
