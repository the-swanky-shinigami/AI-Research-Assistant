import subprocess
import time
from pathlib import Path

from core.execution_result import ExecutionResult


class Executor:
    """
    Executes Python scripts and captures execution details.
    """

    def __init__(self, timeout=600):
        self.timeout = timeout

    def run(self, file_path):

        file_path = Path(file_path)

        start = time.perf_counter()

        try:

            result = subprocess.run(

                ["python", str(file_path)],

                capture_output=True,

                text=True,

                timeout=self.timeout,

            )

            runtime = time.perf_counter() - start

            return ExecutionResult(

                success=result.returncode == 0,

                exit_code=result.returncode,

                runtime=runtime,

                stdout=result.stdout,

                stderr=result.stderr,

            )

        except subprocess.TimeoutExpired:

            runtime = time.perf_counter() - start

            return ExecutionResult(

                success=False,

                exit_code=-1,

                runtime=runtime,

                stdout="",

                stderr="Execution timed out.",

            )