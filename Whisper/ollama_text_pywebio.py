from pywebio.input import input,TEXT
from pywebio.output import put_text,put_error, put_markdown,put_html
import ollama
import httpx
import time # 引入time模块用于计时
import json

def ollama_text():
    your_question = input("What is your question? ", type=TEXT)

    # put_text(f"问题: {your_question}")
    # put_html(f'<p style="color: blue;">问题: {your_question}</p>')
    # put_markdown(f'<span style="color: blue">问题: {your_question}</span>')

    put_html(f'问题: <p style="color: blue;">{your_question}</p>')

    put_text("正在处理您的问题，请稍候...")  # 提供即时反馈

    start_time = time.time()  # 开始计时

    try:
        response=ollama.generate(
            model="gpt-oss:latest",
            prompt=your_question,
            options={
                # "timeout":600,
                # "num_predict":1000,
                "num_predict": -1,
                "temperature": 0.7,
                "top_p": 0.9,
            },
            keep_alive="5m"
        )
        end_time = time.time()  # 结束计时
        elapsed_time = end_time - start_time  # 计算运行时间

        # put_text(f"耗时: {elapsed_time:.2f}秒")
        put_markdown(f"耗时:<span style='color: red'>{elapsed_time:.2f}秒</span>")

        put_markdown("GPT-OSS回答: \n" + response.response)

        put_text(f"完整响应结构: {list(response.keys()) if hasattr(response, 'keys') else 'Not a dict'}")   # 输出完整的响应结构    这点没明白。
        put_text(f"完整响应内容: {json.dumps(dict(response), ensure_ascii=False, indent=2)}")

        if hasattr(response, 'keys'):
            put_text(f"响应字段: {list(response.keys())}")
        else:
            put_text(f"响应类型: {type(response).__name__}")

    except httpx.TimeoutException:
        put_text("GPT-OSS TimeoutException: Timeout")
        put_error("请求超时，请稍后重试")
    except Exception as e:
        put_text("GPT-OSS Exception: " + str(e))
        put_error(f"发生错误: {str(e)}")
    

if __name__ == '__main__':
    ollama_text()