import google.generativeai as genai
from utils.config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)

models = genai.list_models()
print("Available models:")
for model in models:
    print(model.name)
