from agents.architect import Architect
from core.logger import ResearchLogger


def main():

    logger = ResearchLogger()

    architect = Architect()

    task = """
Design a contrastive learning model
for SNP classification.
"""

    logger.section("Research Objective")

    logger.write(task)

    response = architect.think(task)

    logger.section("Architect")
    logger.write(response.text)

    logger.section("Statistics")

    logger.write(
        f"""
    Model: {response.model}

    Elapsed: {response.elapsed_time:.2f} sec

    Prompt Tokens: {response.prompt_tokens}

    Completion Tokens: {response.completion_tokens}

    Total Tokens: {response.total_tokens}
    """
    )

    print(response.text)

    print("\nResearch log saved successfully.")


if __name__ == "__main__":
    main()