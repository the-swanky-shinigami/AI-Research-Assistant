from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Task:

    title: str

    objective: str

    assigned_to: str

    input_files: list[str] = field(default_factory=list)

    output_file: str = ""

    status: str = "pending"

    created: str = field(
        default_factory=lambda:
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    attempts: int = 0

    notes: str = ""