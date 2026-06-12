import os

def get_ai_chat_response(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return 'Please enter a valid question about stock prediction or market analysis.'

    # Try Gemini API if API key is set
    gemini_key = os.getenv('GEMINI_API_KEY')
    if gemini_key:
        try:
            from .gemini_chat import get_gemini_response
            gemini_answer = get_gemini_response(prompt.strip())
            if gemini_answer:
                return gemini_answer
        except Exception as e:
            # Log and fallback
            print(f'Gemini integration error: {e}')

    return "To use the AI Chat assistant, please set up the GEMINI_API_KEY environment variable in your Vercel project settings."
