import os
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

MODEL_NAME = os.getenv('AI_MODEL_NAME', 'microsoft/DialoGPT-medium')
DEVICE = 0 if os.getenv('CUDA_VISIBLE_DEVICES') else -1
_prompt_template = (
    "You are a helpful stock market assistant."
    "\n\nUser: {prompt}\nAssistant:"
)
_chat_pipeline = None


def get_chat_pipeline():
    global _chat_pipeline
    if _chat_pipeline is None:
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
        if tokenizer.pad_token_id is None:
            tokenizer.pad_token_id = tokenizer.eos_token_id
        model.config.pad_token_id = tokenizer.eos_token_id
        _chat_pipeline = pipeline(
            'text-generation',
            model=model,
            tokenizer=tokenizer,
            device=DEVICE,
            max_new_tokens=150,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            pad_token_id=tokenizer.eos_token_id,
        )
    return _chat_pipeline


def _format_response(output: str, prompt: str) -> str:
    response = output[len(_prompt_template.format(prompt=prompt)) :].strip()
    if not response:
        return 'I could not generate a response. Please try again with a different question.'
    return response


def get_ai_chat_response(prompt: str) -> str:
    if not prompt or not prompt.strip():
        return 'Please enter a valid question about stock prediction or market analysis.'

    # Try Gemini API if API key is set
    import os
    gemini_key = os.getenv('GEMINI_API_KEY')
    if gemini_key:
        try:
            from .gemini_chat import get_gemini_response
            gemini_answer = get_gemini_response(prompt.strip())
            if gemini_answer:
                return gemini_answer
        except Exception as e:
            # Log and fallback to local model
            print(f'Gemini integration error: {e}')

    # Fallback to local HuggingFace model
    try:
        chat = get_chat_pipeline()
        prompt_text = _prompt_template.format(prompt=prompt.strip())
        outputs = chat(prompt_text, max_new_tokens=150)
        if not outputs or not isinstance(outputs, list):
            return 'I could not generate a response. Please try again with a different question.'
        generated = outputs[0].get('generated_text', '')
        return _format_response(generated, prompt)
    except Exception as exc:
        return f'AI engine error: {str(exc)}'
