# Everything related to talking to LLMs, client wrapper, prompt templates
from app.config import DEFAULT_TEMPERATURE, DEFAULT_MAX_TOKENS
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_API_TOKEN"],
)
MODEL = "meta-llama/Meta-Llama-3-8B-Instruct"


# creating the wrapper to call the llm
# instead of always calling openai.ChatCompletion.create ----> we call the call_llm to call the llm
def call_llm(prompt: str, max_tokens: int = DEFAULT_MAX_TOKENS) -> str:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=DEFAULT_TEMPERATURE,
    )

    message = response.choices[0].message
    print(message, "message output")
    # Structured content
    if isinstance(message.content, list) and len(message.content) > 0:
        return message.content[0].get("text", "").strip()

    # Plain text
    if isinstance(message.content, str):
        return message.content.strip()

    # Reasoning-only fallback (VERY important)
    if message.reasoning:
        return message.reasoning.strip()

    return "⚠️ No response generated."

