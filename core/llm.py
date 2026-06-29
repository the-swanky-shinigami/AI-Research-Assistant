import time

from openai import OpenAI

from config import LMSTUDIO_URL, API_KEY

from core.conversation import Conversation
from core.response import AIResponse

from datetime import datetime



class LocalLLM:

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
    ) -> AIResponse:

        start = time.perf_counter()

        messages = conversation.to_openai()

        response = self.client.chat.completions.create(

            model=self.model,

            messages=messages,

            temperature=temperature,

            max_tokens=max_tokens,

        )

        elapsed = time.perf_counter() - start

        answer = response.choices[0].message.content

        conversation.add_assistant(answer)

        usage = response.usage

        return AIResponse(

            text=answer,

            model=self.model,

            elapsed_time=elapsed,

            prompt_tokens=usage.prompt_tokens,

            completion_tokens=usage.completion_tokens,

            total_tokens=usage.total_tokens,

            timestamp=str(datetime.now())

        )