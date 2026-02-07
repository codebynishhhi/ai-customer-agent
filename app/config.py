import os
from dotenv import load_dotenv

load_dotenv()

# ========== LLM CONFIG ==========
# OPENAI_API_KEY = os.getenv("OPEN_AI_API_KEY")
HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = "mistralai/Mistral-7B-Instruct-v0.3"

DEFAULT_TEMPERATURE = 0.0
DEFAULT_MAX_TOKENS = 300