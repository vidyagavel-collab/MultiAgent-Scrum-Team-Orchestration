from openai import AzureOpenAI
import os

class BaseAgent:
    def __init__(self, name: str, role_prompt: str):
        self.name = name
        self.role_prompt = role_prompt

        self.client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_KEY"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            api_version="2024-02-01"
        )

    async def run(self, input_text: str) -> str:
        messages = [
            {"role": "system", "content": self.role_prompt},
            {"role": "user", "content": input_text}
        ]

        resp = self.client.chat.completions.create(
            model=os.getenv("MODEL_NAME"),
            messages=messages,
            temperature=0.2
        )

        return resp.choices[0].message.content
