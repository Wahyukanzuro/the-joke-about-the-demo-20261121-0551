#!/usr/bin/env python3
"""One-line joke about working beside AI coding agents.

Writes the joke to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only, no network, deterministic.
"""

import os


# One line, one joke: no internal line breaks by design.
JOKE = "I asked my agent to fix the demo crash before the client call, so it deleted the demo and invoiced me for the refactoring."


def main() -> None:
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
