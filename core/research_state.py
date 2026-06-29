from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ResearchState:

    goal: str

    status: str = "running"

    attempt: int = 0

    current_agent: str = ""

    architecture: str = ""

    generated_code: str = ""

    review: str = ""

    execution_output: str = ""

    best_score: float = 0.0

    successful_runs: int = 0

    failed_runs: int = 0

    history: list[str] = field(default_factory=list)

    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    def log(self, message):

        self.history.append(message)

    def next_attempt(self):

        self.attempt += 1

    def success(self):

        self.successful_runs += 1

    def failure(self):

        self.failed_runs += 1

    def set_agent(self, name):

        self.current_agent = name

    def set_architecture(self, text):

        self.architecture = text

        self.log("Architecture updated.")