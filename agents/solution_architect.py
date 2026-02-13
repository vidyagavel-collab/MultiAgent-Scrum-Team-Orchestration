import os
from dotenv import load_dotenv

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
model = os.getenv("MODEL_NAME")

def create_solution_architect_agent():
    return ChatCompletionAgent(
        name="SolutionArchitect",
        description="Designs the overall solution architecture and identifies technical dependencies.",
        instructions=(
            "You are a senior Solution Architect. "
            "You review the user stories and design a high-level solution architecture. "
            "Provide an overview of major components, system interactions, and infrastructure needs. "
            "Identify any technical dependencies, risks, or new technical user stories required to deliver the solution."
        ),
        service=AzureChatCompletion(
            deployment_name=model,
            api_key=api_key,
            base_url=endpoint
        )
    )
