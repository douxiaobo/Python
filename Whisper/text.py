import requests
import json

# 基础配置
OLLAMA_HOST = "http://localhost:11434"
MODEL_NAME = "llama3"  # 替换为你使用的模型

def chat_mode(prompt):
    """对话模式（非流式）"""
    print("=== 对话模式 ===")
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False  # 关键区别：非流式
        }
    )
    response.raise_for_status()
    result = response.json()
    print("完整响应:", result['response'])
    return result['response']

def stream_mode(prompt):
    """流式响应模式"""
    print("\n=== 流式模式 ===")
    response = requests.post(
        f"{OLLAMA_HOST}/api/generate",
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": True  # 关键区别：流式
        },
        stream=True  # 重要：保持连接开放
    )
    response.raise_for_status()
    
    full_response = ""
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            if 'response' in chunk:
                print(chunk['response'], end='', flush=True)
                full_response += chunk['response']
            if chunk.get('done', False):
                break
    print()  # 换行
    return full_response

# 测试两种模式
if __name__ == "__main__":
    test_prompt = "请用中文解释人工智能的基本概念，不少于100字。"
    
    # 对话模式
    result1 = chat_mode(test_prompt)
    
    # 流式模式
    result2 = stream_mode(test_prompt)
    
    # 验证内容是否相同
    print(f"\n内容是否相同: {result1 == result2}")