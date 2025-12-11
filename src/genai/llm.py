# llm.py

import os

# Optional examples for actual implementation:
# from openai import OpenAI
# client = OpenAI(api_key=os.getenv("LLM_API_KEY"))

LLM_API_KEY = os.getenv("LLM_API_KEY", None)


def call_llm_api(prompt: str):
    """
    Placeholder for LLM API call.
    Replace with actual code for OpenAI, Groq, Anthropic, etc.

    Example using OpenAI:
    ---------------------
    client = OpenAI(api_key=LLM_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4.1",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message['content']
    """
    raise NotImplementedError("Implement call_llm_api() to call a real LLM API.")
