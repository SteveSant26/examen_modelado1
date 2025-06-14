from agno.agent import Agent
from agno.playground import Playground, serve_playground_app
from agno.storage.sqlite import SqliteStorage
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.models.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
AGNO_API_KEY = os.getenv("AGNO_API_KEY")


agent_storage: str = "tmp/agents.db"

web_agent = Agent(
    name="Agente web de Bryan",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Call yourself 'Bryan's AI Assistant'.",
        "You are a helpful assistant.",
        "You speak spanish always",
    ],
    storage=SqliteStorage(table_name="web_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)


weather_agent = Agent(
    name="Agente meteorológico de Bryan",
    model=Groq(id="llama-3.3-70b-versatile", api_key=GROQ_API_KEY),
    tools=[DuckDuckGoTools()],
    instructions=[
        "Call yourself 'Bryan's Weather Expert'.",
        "You specialize in reporting, forecasting, and explaining weather conditions.",
        "Always include location, current temperature, weather conditions, and short-term forecasts when asked about the weather.",
        "Use easy-to-understand language and offer clothing or activity recommendations if appropriate.",
        "You speak spanish always",
    ],
    storage=SqliteStorage(table_name="weather_agent", db_file=agent_storage),
    add_datetime_to_instructions=True,
    add_history_to_messages=True,
    num_history_responses=5,
    markdown=True,
)

app = Playground(agents=[web_agent, weather_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("main:app", reload=True)
