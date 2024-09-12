import json
from app.llm.groq_llm import client

client = client

with open('app/llm/prompts/groq_poem.json', 'r') as file:
    messages_data = json.load(file)

try:
    chat_completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=messages_data["messages"]
    )

    poem = chat_completion.choices[0].message.content
    print({"poem": poem})
except Exception as e:
    detail = str(e)
    print(detail)
