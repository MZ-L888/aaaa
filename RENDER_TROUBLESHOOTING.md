# Render 部署故障排除指南

## 当前问题分析

您遇到的错误表明应用在启动时崩溃了。我已经创建了一个简化的解决方案。

## 🚀 立即解决方案

### 方案 1：使用简化启动模式（推荐）

我已经创建了一个简化的应用入口点 `app/simple_main.py`，它会：
1. 自动设置所有必需的默认环境变量
2. 如果完整应用加载失败，会启动一个简化版本
3. 提供基本的健康检查和错误信息

**在 Render 中的配置：**
- **Start Command**: `uvicorn app.simple_main:app --host 0.0.0.0 --port $PORT`

### 方案 2：最小化配置

如果方案 1 仍有问题，使用最基本的配置：

**在 Render 环境变量中只设置这些必需项：**
```
API_KEYS=["AIzaSyYOUR_ACTUAL_GEMINI_API_KEY"]
ALLOWED_TOKENS=["sk-your-token"]
AUTH_TOKEN=sk-your-token
DATABASE_TYPE=sqlite
```

## 🔧 分步修复指南

### 步骤 1：更新 Render 配置

1. 登录 Render 控制台
2. 找到您的服务
3. 进入 "Settings" 页面
4. 更新 **Start Command** 为：
   ```
   uvicorn app.simple_main:app --host 0.0.0.0 --port $PORT
   ```

### 步骤 2：设置最小环境变量

在 Environment Variables 部分，确保至少有：

```bash
# 必需的 API 配置
API_KEYS=["AIzaSyYOUR_ACTUAL_GEMINI_API_KEY"]
ALLOWED_TOKENS=["sk-your-custom-token"]
AUTH_TOKEN=sk-your-custom-token

# 数据库配置
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance.db

# 基本配置
BASE_URL=https://generativelanguage.googleapis.com/v1beta
TEST_MODEL=gemini-1.5-flash
LOG_LEVEL=info
```

### 步骤 3：手动部署

点击 "Manual Deploy" 按钮重新部署。

### 步骤 4：检查日志

部署后，查看日志应该看到：
- ✅ "完整应用加载成功" 或
- 🔄 "使用简化版本..."

## 🔍 验证部署

### 检查应用状态
访问您的应用 URL，应该看到：
```json
{
  "message": "Gemini Balance API 正在运行",
  "status": "ok",
  "mode": "simplified"
}
```

### 检查健康状态
访问 `/health` 端点：
```json
{
  "status": "healthy",
  "mode": "simplified"
}
```

### 检查模型列表
访问 `/v1/models` 端点应该返回可用模型列表。

## 🐛 常见问题

### Q: 仍然看到启动错误
A: 
1. 检查 Python 版本是否为 3.10+
2. 确认所有环境变量格式正确（特别是 JSON 数组）
3. 尝试删除所有环境变量，只保留最基本的几个

### Q: 应用启动但 API 不工作
A: 这是正常的，简化模式下需要配置正确的 API 密钥才能完全工作。

### Q: 如何切换回完整模式
A: 配置正确的 Gemini API 密钥后，将 Start Command 改回：
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

## 📋 完整环境变量列表（可选）

如果您想要完整功能，可以设置所有这些变量：

```bash
DATABASE_TYPE=sqlite
SQLITE_DATABASE=gemini_balance.db
API_KEYS=["AIzaSyYOUR_ACTUAL_GEMINI_API_KEY"]
ALLOWED_TOKENS=["sk-your-token"]
AUTH_TOKEN=sk-your-token
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

## 🆘 紧急联系

如果所有方法都失败了：
1. 检查 Render 的部署日志
2. 确认 GitHub 仓库中的代码是最新的
3. 尝试创建一个全新的 Render 服务

---

**记住：** 简化模式是为了确保应用能够启动。一旦启动成功，您就可以逐步添加更多配置！
