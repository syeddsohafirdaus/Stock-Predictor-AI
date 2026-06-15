import os
import json
import requests
from dotenv import load_dotenv

# Ensure .env is loaded when this module is imported
load_dotenv()

def get_ai_chat_response(prompt: str) -> str:
    """Send *prompt* to Groq LLM and return the response.
    Raises a clear error if GROQ_API_KEY is missing.
    """
    if not prompt or not prompt.strip():
        return "Please enter a valid question about stock prediction or market analysis."

    groq_key = os.getenv('GROQ_API_KEY')
    if not groq_key:
        raise EnvironmentError(
            "GROQ_API_KEY is not set. Add it to .env and restart the server."
        )

    try:
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {groq_key}",
        }
        data = {
            "model": "llama-3.1-70b",
            "messages": [
                {"role": "system", "content": "You are a helpful assistant for stock market prediction queries."},
                {"role": "user", "content": prompt.strip()},
            ],
            "temperature": 0.7,
            "max_tokens": 1024,
        }
        response = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30,
        )
        response.raise_for_status()
        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "No response from Groq.")
    except Exception as e:
        return f"Groq integration error: {e}"
