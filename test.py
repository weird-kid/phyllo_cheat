from  google import generativeai as genai
import os

# Configure your API key
# It's recommended to set it as an environment variable (GEMINI_API_KEY)
# or pass it directly: genai.configure(api_key="YOUR_API_KEY")
genai.configure(api_key=os.getenv("google_key"))

for m in genai.list_models():
    if "generateContent" in m.supported_generation_methods:
        print(f"Model Name: {m.name}")
        print(f"  Description: {m.description}")
        print(f"  Input Token Limit: {m.input_token_limit}")
        print(f"  Output Token Limit: {m.output_token_limit}")
        print(f"  Supported Generation Methods: {m.supported_generation_methods}\n")
