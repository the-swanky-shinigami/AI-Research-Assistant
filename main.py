from agents.architect import Architect

from core.logger import ResearchLogger
from core.workspace import Workspace
from core.research_state import ResearchState


def main():

    state = ResearchState(

        goal="""
Design a contrastive learning model
for SNP classification.
"""
    )

    logger = ResearchLogger()

    workspace = Workspace()

    architect = Architect()

    state.set_agent("Architect")

    state.next_attempt()

    attempt = workspace.new_attempt()

    logger.section("Experiment")

    logger.write(

f"""
Goal:

{state.goal}

Current Attempt:

{state.attempt}

Current Agent:

{state.current_agent}
"""

    )

    response = architect.think(state.goal)

    state.set_architecture(response.text)

    workspace.write_file(

        attempt,

        "architecture.md",

        response.text

    )

    state.success()

    logger.section("Architect")

    logger.write(response.text)

    logger.section("Statistics")

    logger.write(

f"""
Model:
{response.model}

Elapsed:
{response.elapsed_time:.2f}

Prompt Tokens:
{response.prompt_tokens}

Completion Tokens:
{response.completion_tokens}

Total Tokens:
{response.total_tokens}

Successful Runs:
{state.successful_runs}

Failed Runs:
{state.failed_runs}
"""

    )

    print(response.text)

    print()

    print("Experiment State")

    print(state)


if __name__ == "__main__":

    main()