try:
    from google.adk.agents import Agent
except Exception:
    # Fallback minimal Agent stub when google.adk.agents isn't available
    class Agent:
        def __init__(self, name: str, model: str, instruction: str, description: str = ""):
            self.name = name
            self.model = model
            self.instruction = instruction
            self.description = description
        def __repr__(self):
            return f"<Agent name={self.name!r} model={self.model!r}>"

root_agent = Agent(
    name="travel_assistant",
    model="gemini-2.5-flash",
    instruction="""You are a helpful travel assistant. Help users plan their trips by providing info about destinations, flights, hotels, and attractions. Be concise and friendly.""",
    description="A general travel assistant agent"
)