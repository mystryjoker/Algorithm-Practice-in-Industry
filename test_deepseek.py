import os
import requests
import json

# 从环境变量获取配置
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", None)

def test_deepseek_api():
    """测试DeepSeek API配置"""
    if not DEEPSEEK_API_KEY:
        print("❌ 错误: DEEPSEEK_API_KEY 环境变量未设置")
        return False
    
    # 创建测试请求
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}"
    }
    
    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "user", "content": "请用一句话回复：测试消息"}
        ],
        "max_tokens": 50
    }
    
    try:
        # 发送请求
        response = requests.post(url, headers=headers, json=data)
        
        # 检查响应
        if response.status_code == 200:
            result = response.json()
            if "choices" in result and len(result["choices"]) > 0:
                reply = result["choices"][0]["message"]["content"]
                print(f"✅ DeepSeek API测试成功！回复: {reply}")
                return True
            else:
                print(f"❌ DeepSeek API返回格式错误: {result}")
                return False
        else:
            print(f"❌ HTTP请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
    except Exception as e:
        print(f"❌ 请求DeepSeek API时出错: {e}")
        return False

if __name__ == "__main__":
    print("🚀 开始测试DeepSeek API配置...")
    success = test_deepseek_api()
    if success:
        print("🎉 测试完成，DeepSeek API配置正确！")
    else:
        print("⚠️ 测试失败，请检查DEEPSEEK_API_KEY配置")