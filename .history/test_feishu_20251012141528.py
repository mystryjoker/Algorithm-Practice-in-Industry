import os
import json
import requests

# 从环境变量获取配置
FEISHU_URL = os.environ.get("FEISHU_URL", None)

def send_test_to_feishu():
    """发送测试消息到飞书"""
    if not FEISHU_URL:
        print("❌ 错误: FEISHU_URL 环境变量未设置")
        return False
    
    # 创建测试消息
    test_data = {
        "msg_type": "text",
        "content": {
            "text": "🧪 这是一条测试消息，用于验证飞书Webhook配置是否正确。如果您看到这条消息，说明配置成功！"
        }
    }
    
    try:
        # 发送请求
        headers = {"Content-Type": "application/json"}
        response = requests.post(url=FEISHU_URL, data=json.dumps(test_data), headers=headers)
        
        # 检查响应
        if response.status_code == 200:
            result = response.json()
            if result.get("code") == 0:
                print("✅ 飞书测试消息发送成功！")
                return True
            else:
                print(f"❌ 飞书返回错误: {result}")
                return False
        else:
            print(f"❌ HTTP请求失败，状态码: {response.status_code}")
            print(f"响应内容: {response.text}")
            return False
    except Exception as e:
        print(f"❌ 发送消息时出错: {e}")
        return False

if __name__ == "__main__":
    print("🚀 开始测试飞书配置...")
    success = send_test_to_feishu()
    if success:
        print("🎉 测试完成，飞书配置正确！")
    else:
        print("⚠️ 测试失败，请检查FEISHU_URL配置")