from openai import OpenAI
from config import LMSTUDIO_URL, API_KEY
from core.conversation import Conversation


class LocalLLM:
    """
    Wrapper around LM Studio's OpenAI-compatible API.
    Every AI agent in the system will use this class.
    """

    def __init__(self, model: str):
        self.model = model

        self.client = OpenAI(
            base_url=LMSTUDIO_URL,
            api_key=API_KEY,
        )

    def chat(
        self,
        conversation: Conversation,
        temperature=0.7,
        max_tokens=4096,
    ):
        response = self.client.chat.completions.create(
            model=self.model,
            messages=conversation.to_openai(),
            temperature=temperature,
            max_tokens=max_tokens,
        )

        answer = response.choices[0].message.content

        conversation.add_assistant(answer)

        return answer