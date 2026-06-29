from agents.architect import Architect


def main():

    architect = Architect()

    response = architect.think(

        task="""
Design a neural network that learns
relationships between SNP genotypes
and clinical phenotypes using
contrastive learning.
"""

    )

    print(response)


if __name__ == "__main__":
    main()