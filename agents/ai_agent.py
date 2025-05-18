"""
ai_agent.py  —  Talks to Groq Llama‑3‑70B
"""

from openai import OpenAI
from utils.config import GROQ_API_KEY

# Groq uses OpenAI client with a custom base_url
client = OpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)

MODEL_NAME = "llama3-70b-8192"   # fastest large model on Groq

def generate_prompt(df):
    sample = df.head(3).to_string()
    stats = df.describe().to_string()

    return f"""
You are a senior data analyst. Study the dataset and give concise insights.

Sample rows:
{sample}

Statistical summary:
{stats}

Respond in bullet points (max 12 bullets), highlight trends, outliers,
and interesting correlations.
"""

def query_ai(prompt: str) -> str:
    try:
        chat = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return chat.choices[0].message.content
    except Exception as e:
        return f"⚠️ Groq error: {e}"
