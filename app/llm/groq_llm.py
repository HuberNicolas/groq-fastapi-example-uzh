import os

from dotenv import load_dotenv
from groq import Groq

# Read GROQ_API_KEY (and optionally GROQ_MODEL) from a .env file in the working directory or from the environment.
load_dotenv()

api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set. Copy .env.example to .env and add your key.")

# llama3-8b-8192, the model this example used in 2024, was shut down by Groq on 2025-08-30
# (see https://console.groq.com/docs/deprecations).
model = os.environ.get("GROQ_MODEL", "openai/gpt-oss-20b")

client = Groq(
    api_key=api_key,
)
