from core.llm import LocalLLM
from core.conversation import Conversation
from core.task import Task


class BaseAgent:
    """
    Parent class for every AI agent in the system.
    """

    def __init__(self, name, role, model):
        self.name = name
        self.role = role
        self.llm = LocalLLM(model)

    def think(self, task: Task):

        conversation = Conversation()

        conversation.add_system(self.role)

        prompt = f"""
TASK TITLE
{task.title}

OBJECTIVE
{task.objective}

INPUT FILES
{", ".join(task.input_files) if task.input_files else "None"}

EXPECTED OUTPUT
{task.output_file}
"""

        conversation.add_user(prompt)

        return self.llm.chat(conversation)