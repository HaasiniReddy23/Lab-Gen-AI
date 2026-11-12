
from llm_client import LLMClient, OllamaProvider, GeminiProvider
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Choose provider
choice = input("Choose LLM Provider (1. Ollama / 2. Gemini): ")

if choice == "1":
    provider = OllamaProvider(model="llama3.2")

elif choice == "2":
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("Gemini API key not found in .env file")

    provider = GeminiProvider(api_key=api_key)

else:
    raise ValueError("Invalid choice")

# Create common LLM client
client = LLMClient(provider)

# Get user prompt
prompt = input("\nEnter your prompt: ")

# Generate response
response = client.generate(prompt)

print("\nLLM Response:")
print(response)
