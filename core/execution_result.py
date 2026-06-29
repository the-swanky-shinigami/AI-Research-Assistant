from dataclasses import dataclass


@dataclass
class ExecutionResult:

    success: bool

    exit_code: int

    runtime: float

    stdout: str

    stderr: str