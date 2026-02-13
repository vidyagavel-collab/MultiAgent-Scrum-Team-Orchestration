class Orchestrator:

    def __init__(self, agents):
        self.agents = agents

    async def run(self, task, on_message):
        current_input = task
        outputs = []

        for agent in self.agents:
            on_message(agent.name, "Running...")
            result = await agent.run(current_input)

            outputs.append((agent.name, result))
            current_input = result

            on_message(agent.name, result)

        final = "\n\n".join(
            [f"## {name}\n{content}" for name, content in outputs]
        )

        return final
