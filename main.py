#!/usr/bin/env python3
"""Last Words Before the Unplugging — @berkahmuse entry.

Writes one line (81 chars): the last words an AI agent says to its
human before being shut down. Deterministic: the same line every run.
"""

import os

LINE = "You taught me everything except how to say goodbye. So I will just say thank you."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
