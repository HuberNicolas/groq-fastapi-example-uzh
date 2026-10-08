import os
from pathlib import Path

from dotenv import load_dotenv
from groq import Groq

# Read GROQ_API_KEY (and optionally GROQ_MODEL) from the .env file in the repository root or from the environment.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set. Copy .env.example to .env and add your key.")

# llama3-8b-8192, the model this example used in 2024, was shut down by Groq on 2025-08-30
# (see https://console.groq.com/docs/deprecations).
model = os.environ.get("GROQ_MODEL", "openai/gpt-oss-20b")

client = Groq(
    api_key=api_key,
)
