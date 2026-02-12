import os
import requests
from config.schema import SCHEMA
from config.prompt import PROMPT_TEMPLATE
from dotenv import load_dotenv


load_dotenv()
# Use environment variable (DO NOT hardcode API key)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL_NAME = "llama-3.1-8b-instant"


def extract_structured_invoice(text: str) -> str:
    prompt = PROMPT_TEMPLATE.format(
        schema=SCHEMA,
        text=text
    )

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL_NAME,
        "messages": [
            {
                "role": "system",
                "content": "You are a structured data extraction assistant. Return strict JSON only."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "temperature": 0.0
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(
            f"Groq call failed: {response.status_code}\n{response.text}"
        )

    result = response.json()

    # Groq response format (OpenAI compatible)
    return result["choices"][0]["message"]["content"]


