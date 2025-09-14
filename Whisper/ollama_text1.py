from ollama import chat

try:
    response = chat(
        model="llama3",  # 简化模型名称
        messages=[{"role": "user", "content": "Can hearing impaired people to play piano?"}],
    )
    print(response.message.content)
except Exception as e:
    print(f"Error occurred: {e}")