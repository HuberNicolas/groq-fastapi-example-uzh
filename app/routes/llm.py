import logging
from fastapi import APIRouter

import json
from app.llm.groq_llm import client as gclient


log = logging.getLogger(__name__)


router = APIRouter(
    prefix="/llm",
    tags=["llm"],
    responses={
        404: {"description": "Not found"},
        403: {"description": "Forbidden"},
        401: {"description": "Unauthorized"},
    },
)
    
@router.get("/groq/poem/{country}")
def get_groq_poem(country: str):
    client_instance = gclient
    file_path = './app/llm/prompts/groq_api_poem.json'

    try:
        with open(file_path, 'r') as file:
            messages_data = json.load(file)

        # Replace the {country} placeholder with the actual country
        for message in messages_data["messages"]:
            message["content"] = message["content"].replace("{country}", country)

        # Generate the poem using the modified messages
        chat_completion = client_instance.chat.completions.create(
            model="llama3-8b-8192",
            messages=messages_data["messages"]
        )

        poem = chat_completion.choices[0].message.content.strip()
        return {"poem": poem}
    except Exception as e:
        detail = str(e)
        return {"error": detail}