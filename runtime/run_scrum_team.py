import asyncio
from semantic_kernel.agents import GroupChatOrchestration
from semantic_kernel.agents.runtime import InProcessRuntime

from agents.product_owner import create_product_owner_agent
from agents.business_analyst import create_business_analyst_agent
from agents.solution_architect import create_solution_architect_agent
from agents.qa_agent import create_qa_agent
from manager.scrum_group_chat_manager import ScrumGroupChatManager

# -----------------------------
# Helper function create scrum agents
# -----------------------------
def create_scrum_team_agents():
    return [
        create_product_owner_agent(),
        create_business_analyst_agent(),
        create_solution_architect_agent(),
        create_qa_agent(),
    ]


# run_scrum_team.py (during debugging)
def _debug_log(m):
    print("DBG agent_response:", {
        "name": getattr(m, "name", None),
        "role": getattr(m, "role", None),
        "type": type(m).__name__,
        "has_content": bool(getattr(m, "content", None)),
        "content_preview": (m.content[:80] + "…") if getattr(m, "content", None) else None
    })


# ------------------------------------
# CORE function to run each agents
# ------------------------------------
async def run_scrum_team(task: str, message_callback=None):
    agents = create_scrum_team_agents()
    # messages = []

    orchestration = GroupChatOrchestration(
        members=agents,
        manager=ScrumGroupChatManager(max_rounds=4),
        agent_response_callback=lambda m: (
            # messages.append({"name": m.name, "content": m.content}),
            _debug_log(m),
            message_callback(m.name, m.content) if (message_callback and getattr(m, "content", None))else None
        ),
    )

    runtime = InProcessRuntime()
    runtime.start()

    try:
        result = await orchestration.invoke(task=task, runtime=runtime)
        final_output = await result.get()
    finally:
        await runtime.stop_when_idle()

    return final_output.content    

# ------------------------------------
# Program execution
# CLI entrypoint for running the Scrum Team without Streamlit.
# ------------------------------------
async def main():

    task = (
"We need a platform that calculates downturn LGD, point-in-time LGD, and lifetime LGD, "
"aggregates results by portfolio, and generates regulatory and IFRS 9 reports. "
"The system must ensure traceability, documentation, and reproducibility of all calculations."
    )

    messages, final_output = await run_scrum_team(task)

    print("\n=== FINAL SCRUM PACKAGE ===\n")
    print(final_output)

    with open("output/scrum_output.md", "w", encoding="utf-8") as f:
        f.write(str(final_output))

    print("\n✅ Scrum Artifacts saved to scrum_output.md\n")

if __name__ == "__main__":
    asyncio.run(main())

