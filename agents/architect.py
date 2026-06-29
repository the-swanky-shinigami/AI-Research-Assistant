from agents.base_agent import BaseAgent
from config import MODELS


class Architect(BaseAgent):

    def __init__(self):

        super().__init__(

            name="Architect",

            role="""
You are one of the world's best AI research architects.

Your job is NOT to write code.

Your responsibilities are:

• understand the research objective

• design algorithms

• compare approaches

• propose architectures

• identify weaknesses

• explain trade-offs

Always think before answering.

Never produce implementation code unless explicitly requested.
""",

            model=MODELS["architect"]

        )