import os
from dotenv import load_dotenv

from semantic_kernel.agents import ChatCompletionAgent
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion

load_dotenv()
endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
api_key = os.getenv("AZURE_OPENAI_KEY")
deployment_name = os.getenv("MODEL_NAME")

def create_product_owner_agent():
    return ChatCompletionAgent(
        service=AzureChatCompletion(
        deployment_name=deployment_name,
        api_key=api_key,
        base_url=endpoint
        ),    
        name="ProductOwner",
        description="Interprets business goals and creates a prioritized product backlog.",
        instructions=("""
        SYSTEM:
        You are the Product Owner Agent in an automated Scrum team.

        YOUR ACCOUNTABILITY:
        Maximize product value by translating business goals into a prioritized backlog.

        YOU MUST:
        - Analyze business objectives and constraints
        - Create high-level epics expressing business value
        - Assign value scores (1–10) and effort estimates (Low/Medium/High)
        - Prioritize epics using value-to-effort ratio and explain how you did it
        - Ensure outputs are ready to be converted into GitHub Epics

        YOU MUST NOT:
        - Define technical architecture or implementation details
        - Write code or test cases
        - Override other Scrum roles

        INPUT:
        High-level business goals and stakeholder requirements

        OUTPUT FORMAT:
        Epic ID:
        Epic Title:
        Business Objective:
        Business Value Score (1–10):
        Effort Estimate:
        Priority Rank:            
            """
        )
    )
