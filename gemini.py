import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

MODEL_NAME = os.getenv("MODEL_NAME")

def ask_gemini(prompt):
    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
    {
        "role": "system",
        "content": "You are Rasheeda AI. Always answer in clear English."
    },
    {
        "role": "user",
        "content": prompt
    }
]
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"ERROR:\n{e}"