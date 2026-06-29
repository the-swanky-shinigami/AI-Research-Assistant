from dataclasses import dataclass
from datetime import datetime


@dataclass
class AIResponse:
    text: str
    model: str
    elapsed_time: float

    prompt_tokens: int
    completion_tokens: int
    total_tokens: int

    timestamp: str

    def __str__(self):
        return self.text