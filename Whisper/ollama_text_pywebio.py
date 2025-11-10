from pywebio.input import input,TEXT
from pywebio.output import put_text
import ollama
import httpx

def ollama_text():
    your_question = input("What is your question? ", type=TEXT)

    put_text("正在处理您的问题，请稍候...")  # 提供即时反馈

    try:
        response=ollama.generate(
            model="gpt-oss:latest",
            prompt=your_question,
            options={
                # "timeout":600,
                "num_predict":1000,
            },
            keep_alive="5m"
        )
        put_text("GPT-OSS: " + response.response)
    
    except httpx.TimeoutException:
        put_text("GPT-OSS TimeoutException: Timeout")
        put_error("请求超时，请稍后重试")
    except Exception as e:
        put_text("GPT-OSS Exception: " + str(e))
        put_error(f"发生错误: {str(e)}")
    

if __name__ == '__main__':
    ollama_text()