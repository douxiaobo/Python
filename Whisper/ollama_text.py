import ollama

response = ollama.generate(
    model="llama3:latest",
    prompt="Can hearing impaired people to play piano?"
)

print(response.response)
exit(0)