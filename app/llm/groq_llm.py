from groq import Groq
from dotenv import dotenv_values

config = dotenv_values(".env") 
api_key = config["GROQ_API_KEY"]


client = Groq(
    api_key=api_key,
)