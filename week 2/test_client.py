
from llm_client import LLMClient, OllamaProvider

# Initialize local Ollama provider
provider = OllamaProvider(model="llama3.2")

# Create common LLM client
client = LLMClient(provider)

# Generate response
prompt = "What is Artificial Intelligence? Explain in simple words."

response = client.generate(prompt)

print("\nLLM Response:")
print(response)
