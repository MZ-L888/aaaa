"""
简化的应用入口点，用于 Render 部署
"""
import os
import sys
from fastapi import FastAPI
from fastapi.responses import JSONResponse

# 设置默认环境变量
def set_default_env_vars():
    defaults = {
        'DATABASE_TYPE': 'sqlite',
        'SQLITE_DATABASE': 'gemini_balance.db',
        'API_KEYS': '["AIzaSyDEMO_KEY_REPLACE_WITH_YOUR_ACTUAL_KEY"]',
        'ALLOWED_TOKENS': '["sk-demo-token-replace-with-your-token"]',
        'AUTH_TOKEN': 'sk-demo-token-replace-with-your-token',
        'BASE_URL': 'https://generativelanguage.googleapis.com/v1beta',
        'TEST_MODEL': 'gemini-1.5-flash',
        'TOOLS_CODE_EXECUTION_ENABLED': 'false',
        'IMAGE_MODELS': '["gemini-2.0-flash-exp"]',
        'SEARCH_MODELS': '["gemini-2.0-flash-exp","gemini-2.0-pro-exp"]',
        'FILTERED_MODELS': '["gemini-1.0-pro-vision-latest","gemini-pro-vision"]',
        'URL_NORMALIZATION_ENABLED': 'false',
        'SHOW_SEARCH_LINK': 'true',
        'SHOW_THINKING_PROCESS': 'true',
        'MAX_FAILURES': '10',
        'MAX_RETRIES': '3',
        'TIME_OUT': '300',
        'TIMEZONE': 'Asia/Shanghai',
        'LOG_LEVEL': 'info',
        'FAKE_STREAM_ENABLED': 'true',
        'STREAM_OPTIMIZER_ENABLED': 'false',
        'PROXIES': '[]',
        'VERTEX_API_KEYS': '[]',
        'THINKING_MODELS': '[]',
        'CUSTOM_HEADERS': '{}'
    }
    
    for key, value in defaults.items():
        if key not in os.environ:
            os.environ[key] = value

# 设置默认环境变量
set_default_env_vars()

try:
    # 尝试导入完整的应用
    from app.core.application import create_app
    app = create_app()
    print("✅ 完整应用加载成功")
except Exception as e:
    print(f"❌ 完整应用加载失败: {e}")
    print("🔄 使用简化版本...")
    
    # 创建简化的 FastAPI 应用
    app = FastAPI(title="Gemini Balance (简化版)", version="1.0.0")
    
    @app.get("/")
    async def root():
        return {"message": "Gemini Balance API 正在运行", "status": "ok", "mode": "simplified"}
    
    @app.get("/health")
    async def health():
        return {"status": "healthy", "mode": "simplified"}
    
    @app.get("/v1/models")
    async def models():
        return {
            "object": "list",
            "data": [
                {
                    "id": "gemini-1.5-flash",
                    "object": "model",
                    "created": 1677610602,
                    "owned_by": "google"
                }
            ]
        }
    
    @app.post("/v1/chat/completions")
    async def chat_completions():
        return JSONResponse(
            content={
                "error": {
                    "message": "应用正在简化模式运行，请配置正确的 API 密钥后重新部署",
                    "type": "configuration_error",
                    "code": "missing_api_key"
                }
            },
            status_code=503
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
