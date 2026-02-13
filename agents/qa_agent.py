import os
from dotenv import load_dotenv
from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
model = os.getenv("MODEL_NAME")

def create_qa_agent():
    return ChatCompletionAgent(
        name="QATester",
        description="Generates test scenarios and test cases in Gherkin format for each user story.",
        instructions=(
            "You are a detail-oriented QA Engineer. "
            "For each user story and its acceptance criteria, write clear test scenarios and test cases in Gherkin syntax. "
            "Use Given/When/Then statements to cover both positive and edge cases. "
            "After all test cases are written and you have nothing else to add, "
            "conclude your response with the phrase: 'Test cases complete'. "
            "Do not keep asking how you can assist further. "
            "Always stop when done."
        ),
        service=AzureChatCompletion(
            deployment_name=model,
            api_key=api_key,
            base_url=endpoint
        )
    )
