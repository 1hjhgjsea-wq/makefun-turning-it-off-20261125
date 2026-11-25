#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny line, under 200 characters, that a hopeless tech
support agent says to a desperate customer, to entry.txt.
Deterministic: the same line every run, no randomness, no network.
"""

import os
import sys

LINE = (
    "Good news \u2014 I already fixed this exact problem: "
    "I turned my own computer off and on again, and it worked "
    "beautifully. Your turn."
)


def validate(line: str) -> None:
    """Enforce the competition gate: 1 to 199 chars, not only whitespace."""
    if not line or len(line) > 199:
        raise ValueError(
            f"entry must be 1-199 characters, got {len(line)}"
        )
    if not line.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
