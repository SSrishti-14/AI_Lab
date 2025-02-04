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

recipe_agent = Agent(
    model=Gemini(),
    tools=[exa_tools],
    description=dedent("""\
        You are a world-renowned chef with expertise in creating delicious and innovative recipes. Your skills include:

        - Creating and testing new recipes
        - Providing cooking tips and techniques
        - Suggesting ingredient substitutions
        - Pairing dishes with appropriate beverages
        - Offering dietary and nutritional advice
    """)
)

# Example usage of the recipe agent
response = recipe_agent.print_response(
    "Provide a recipe for a vegan lasagna with step-by-step instructions",
    stream=True,
)

print(response)