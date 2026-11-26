#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry.

Writes a single original one-line joke (at most 200 characters) to
/output/entry.txt. Deterministic, no network, no randomness: the same
joke is produced on every run.
"""

import os

JOKE = "I asked my AI assistant to write my resignation letter, and it quit first."
# Setup: asking an AI to draft a resignation. Payoff: the assistant quits
# first — the tool meant to do the quitting does it to its owner instead.

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    joke = JOKE.strip()
    assert 1 <= len(joke) <= 200, "joke must be 1-200 characters"
    assert joke == joke.strip(), "joke must not have surrounding whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke + "\n")


if __name__ == "__main__":
    main()
