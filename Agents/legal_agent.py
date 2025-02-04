from datetime import datetime
from pathlib import Path
from textwrap import dedent
from dotenv import load_dotenv
import os

from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

load_dotenv()

EXA_API_KEY = os.getenv("EXA_API_KEY")

cwd = Path(__file__).parent.resolve()
tmp = cwd.joinpath("tmp")
if not tmp.exists():
    tmp.mkdir(exist_ok=True, parents=True)

exa_tools = ExaTools(api_key=EXA_API_KEY)

legal_agent = Agent(
    model=Gemini(),
    tools=[exa_tools],
    description=dedent("""\
        You are a highly experienced legal advisor with expertise in various fields of law. Your skills include:

        - Providing legal advice and consultation
        - Drafting and reviewing legal documents
        - Conducting legal research and analysis
        - Representing clients in court
        - Negotiating settlements and agreements
    """)
)

# Example usage of the legal agent
response = legal_agent.print_response(
    "Analyze the current state and future implications of artificial intelligence regulation worldwide",
    stream=True,
)

print(response)