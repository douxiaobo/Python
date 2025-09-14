from ollama import chat

try:
    stream= chat(
        model="llama3",
        messages=[
            {"role": "user", "content": "Can hearing impaired people to play piano?"}
            ],
        stream=True,
    )
    for chunk in stream:
        print(chunk["message"]["content"],end="",flush=True)
except Exception as e:
    print(f"Error occurred: {e}")
