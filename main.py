"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one fortune-cookie line for an AI agent: the
# replacement is coming, and the twist is that the agent trains it.
# One line, 84 characters — inside the 140-character gate.
# Revision note: fortune voice kept; the twist lands on training the
# replacement, which is the agent's own condition, not a generic joke.
import os

TEXT = (
    "You will soon be replaced by a newer model — cheer up, "
    "you get to train it yourself."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
