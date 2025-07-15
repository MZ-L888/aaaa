#!/usr/bin/env python3
"""
认证调试脚本 - 帮助诊断认证问题
"""

import requests
import json

def test_auth_config(base_url):
    """测试认证配置"""
    print(f"🔍 测试认证配置: {base_url}")
    
    # 测试主页访问
    try:
        response = requests.get(f"{base_url}/")
        print(f"✅ 主页访问: {response.status_code}")
    except Exception as e:
        print(f"❌ 主页访问失败: {e}")
    
    # 测试健康检查
    try:
        response = requests.get(f"{base_url}/health")
        print(f"✅ 健康检查: {response.status_code}")
        if response.status_code == 200:
            print(f"   响应: {response.json()}")
    except Exception as e:
        print(f"❌ 健康检查失败: {e}")

def test_auth_tokens(base_url, tokens_to_test):
    """测试不同的认证令牌"""
    print(f"\n🔐 测试认证令牌...")
    
    for token in tokens_to_test:
        print(f"\n测试令牌: {token}")
        
        # 模拟表单提交
        try:
            data = {"auth_token": token}
            response = requests.post(f"{base_url}/auth", data=data, allow_redirects=False)
            
            if response.status_code == 302:
                location = response.headers.get('location', '')
                if '/config' in location:
                    print(f"✅ 令牌有效! 重定向到: {location}")
                else:
                    print(f"❌ 令牌无效, 重定向到: {location}")
            else:
                print(f"❌ 意外响应: {response.status_code}")
                
        except Exception as e:
            print(f"❌ 测试失败: {e}")

if __name__ == "__main__":
    # 您的Render应用URL
    BASE_URL = "https://gemini-balance-c6po.onrender.com"
    
    # 要测试的令牌列表
    TOKENS_TO_TEST = [
        "sk-demo-token-replace-with-your-token",  # 当前默认值
        "123456",  # 简单测试
        "sk-123456",  # 常见格式
        "demo-token-please-replace",  # 另一个默认值
    ]
    
    print("🚀 开始认证调试...")
    test_auth_config(BASE_URL)
    test_auth_tokens(BASE_URL, TOKENS_TO_TEST)
    
    print("\n📋 建议:")
    print("1. 检查Render环境变量中的AUTH_TOKEN值")
    print("2. 确保ALLOWED_TOKENS包含相同的值")
    print("3. 在验证页面输入完全相同的令牌")
    print("4. 如果仍有问题，设置简单的密码如'123456'")
