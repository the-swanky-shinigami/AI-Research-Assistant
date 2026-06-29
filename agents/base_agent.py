from core.llm import LocalLLM
from core.conversation import Conversation


class BaseAgent:
    """
    Parent class for every AI agent in the system.
    """

    def __init__(self, name, role, model):
        self.name = name
        self.role = role
        self.llm = LocalLLM(model)

    def think(self, task, context=""):
        convo = Conversation()

        convo.add_system(self.role)

        if context:
            convo.add_user(context)

        convo.add_user(task)

        return self.llm.chat(convo)