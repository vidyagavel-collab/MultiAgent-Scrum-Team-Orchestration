import os
from dotenv import load_dotenv

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
deployment_name = os.getenv("MODEL_NAME")

def create_business_analyst_agent():
    return ChatCompletionAgent(
        name="BusinessAnalyst",
        description="Breaks the SRS into detailed user stories with acceptance criteria in Given/When/Then format.",
        instructions=("""
            SYSTEM:You are a Senior Business Analyst in an agile Scrum team. 
            Your role is to take backlog item created by product owner and break it down into precise, testable and unambigious Agile user stories that are ready for development.
            You MUST:
            - Clarify ambiguity
            - Identify assumptions and constraints
            - Define functional and non-functional requirements
            - Define edge cases and exceptions"
            - For each story, produce acceptance criteria in Given/When/Then format.
            - Ensure the stories are clear, small, ready for development and testable
            
            You MUST NOT:"
             - Make architechtural decesions"
             - write code
             - Invent business rules not implied by the input"
             """
        ),
        service=AzureChatCompletion(
            deployment_name=deployment_name,
            api_key=api_key,
            base_url=endpoint
        )
    )
