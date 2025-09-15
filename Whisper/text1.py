import requests
import json
import time

# 基础配置
OLLAMA_HOST = "http://localhost:11434"
MODEL_NAME = "llama3"  # 替换为你使用的模型

def advanced_stream_mode(prompt):
    """增强的流式处理，显示更多信息"""
    try:
        response = requests.post(
            f"{OLLAMA_HOST}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": True
            },
            stream=True
        )
    except requests.exceptions.ConnectionError:
        print("无法连接到Ollama服务器。请检查Ollama是否已启动并运行。")
        return ""
    except requests.exceptions.HTTPError as e:
        print(f"HTTP错误：{e}") 
        return ""
    except requests.exceptions.Timeout:
        print("请求超时。")
        return ""
    except requests.exceptions.RequestException as e:
        print(f"请求异常：{e}")
        return ""
    

    print("开始生成...")
    full_response = ""
    start_time = time.time()
    
    for line in response.iter_lines():
        if line:
            chunk = json.loads(line)
            
            # 显示生成进度
            if 'response' in chunk:
                print(chunk['response'], end='', flush=True)
                full_response += chunk['response']
            
            # 显示性能信息
            if 'eval_count' in chunk:
                tokens_per_second = chunk['eval_count'] / (time.time() - start_time)
                print(f"\n[性能: {tokens_per_second:.1f} tokens/秒]", end='\r')
            
            if chunk.get('done', False):
                break
    
    total_time = time.time() - start_time
    print(f"\n\n生成完成！总共耗时: {total_time:.2f}秒")
    return full_response

if __name__ == '__main__':
    prompt = "你好，欢迎来到 OllaMA！"
    response = advanced_stream_mode(prompt)
    print(response) # 输出生成的文本   
