import ollama

response = ollama.generate(
    model="deepseek-v3.1:671b-cloud",
    prompt="Can hearing impaired people to play piano?"
)

print(response.response)
exit(0)


# brew install ollama是不行，只能用pip3 install ollama