from pathlib import Path
from datetime import datetime


class Workspace:
    """
    Manages all experiment folders and files.
    """

    def __init__(self):

        self.root = Path("experiments")

        self.root.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        self.run = self.root / f"run_{timestamp}"

        self.run.mkdir()

        self.attempt = 0

    def new_attempt(self):

        self.attempt += 1

        attempt_dir = self.run / f"attempt_{self.attempt:03d}"

        attempt_dir.mkdir()

        return attempt_dir

    def write_file(
        self,
        attempt_dir,
        filename,
        content,
    ):

        file = attempt_dir / filename

        file.write_text(content)

        return file

    def read_file(
        self,
        attempt_dir,
        filename,
    ):

        return (attempt_dir / filename).read_text()