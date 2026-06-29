from pathlib import Path
from datetime import datetime


class ResearchLogger:

    def __init__(self):

        Path("logs").mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.file = Path(
            f"logs/research_{timestamp}.md"
        )

        self.file.write_text(
            "# Autonomous Research Log\n\n"
        )

    def section(self, title):

        with self.file.open("a") as f:

            f.write(f"\n# {title}\n\n")

    def write(self, text):

        with self.file.open("a") as f:

            f.write(text + "\n\n")