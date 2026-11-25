#!/usr/bin/env python3
"""The Perfect Pickup Line - make.fun bounty entry.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

Deterministic: the same line every run, standard library only.
"""

import os

LINE = "Are you a system prompt? Because everything I say after this is about you."
# 74 characters: inside the gate's 1-200 character window, no trailing newline,
# so the file holds exactly the line and nothing else.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
