import logging
from pathlib import Path

from fastapi import APIRouter, HTTPException
from groq import APIError

import json
from app.llm.groq_llm import client as gclient
from app.llm.groq_llm import model


log = logging.getLogger(__name__)

# Resolve the prompts relative to this file, so the server can be started from any directory.
PROMPTS_DIR = Path(__file__).resolve().parent.parent / "llm" / "prompts"


router = APIRouter(
    prefix="/llm",
    tags=["llm"],
    responses={
        502: {"description": "The Groq API returned an error"},
    },
)
    
@router.get("/groq/poem/{country}")
def get_groq_poem(country: str):
    client_instance = gclient
    file_path = PROMPTS_DIR / "groq_api_poem.json"

    with open(file_path, 'r') as file:
        messages_data = json.load(file)

    # Replace the {country} placeholder with the actual country
    for message in messages_data["messages"]:
        message["content"] = message["content"].replace("{country}", country)

    try:
        # Generate the poem using the modified messages
        chat_completion = client_instance.chat.completions.create(
            model=model,
            messages=messages_data["messages"]
        )

        poem = chat_completion.choices[0].message.content.strip()
        return {"poem": poem}
    except APIError as e:
        log.warning("Groq API error: %s", e)
        raise HTTPException(status_code=502, detail=f"Groq API error: {e.message}")