from agents.architect import Architect

from core.logger import ResearchLogger
from core.workspace import Workspace
from core.research_state import ResearchState
from core.task import Task


def main():

    # Create research state
    state = ResearchState(
        goal="""
Design a contrastive learning model
for SNP classification.
"""
    )

    # Infrastructure
    logger = ResearchLogger()
    workspace = Workspace()

    # Agent
    architect = Architect()

    # Update state
    state.set_agent("Architect")
    state.next_attempt()

    # Create attempt folder
    attempt_dir = workspace.new_attempt()

    # Create task
    task = Task(
        title="Architecture Design",
        objective=state.goal,
        assigned_to="Architect",
        output_file="architecture.md",
    )

    logger.section("Experiment")
    logger.write(
f"""
Goal:
{state.goal}

Attempt:
{state.attempt}

Current Agent:
{state.current_agent}
"""
    )

    # Run architect
    response = architect.think(task)

    state.set_architecture(response.text)
    state.success()

    # Save architecture
    workspace.write_file(
        attempt_dir,
        "architecture.md",
        response.text,
    )

    logger.section("Architect")
    logger.write(response.text)

    logger.section("Statistics")
    logger.write(
f"""
Model:
{response.model}

Elapsed:
{response.elapsed_time:.2f} sec

Prompt Tokens:
{response.prompt_tokens}

Completion Tokens:
{response.completion_tokens}

Total Tokens:
{response.total_tokens}
"""
    )

    print(response.text)
    print("\nExperiment completed successfully.")


if __name__ == "__main__":
    main()