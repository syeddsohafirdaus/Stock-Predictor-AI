import os
import json
import requests


def get_gemini_response(prompt: str) -> str:
    """Send a prompt to Google Gemini API and return the response text.

    The function expects the environment variable `GEMINI_API_KEY` to be set with a valid API key.
    It uses the "gemini-pro" model endpoint.
    """
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise RuntimeError('GEMINI_API_KEY not set in environment')

    url = f'https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={api_key}'
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [
            {"role": "user", "parts": [{"text": prompt}]}
        ]
    }
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        data = response.json()
        # Extract the text response
        candidates = data.get('candidates', [])
        if not candidates:
            return 'Gemini returned no candidates.'
        parts = candidates[0].get('content', {}).get('parts', [])
        if not parts:
            return 'Gemini response missing parts.'
        # Assuming first part has the text
        return parts[0].get('text', 'Gemini response empty.')
    except requests.RequestException as e:
        # Log the error and return a friendly message
        print(f'Error contacting Gemini API: {e}')
        return f'Error contacting Gemini API: {e}'
