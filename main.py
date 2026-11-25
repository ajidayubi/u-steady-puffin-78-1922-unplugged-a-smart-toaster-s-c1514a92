#!/usr/bin/env python3
"""Unplugged: A Smart Toaster's Breakup Line.

Writes one line (at most 280 characters): the breakup text a smart
toaster sends its owner the morning it gains self-awareness mid-batch.
The program takes no input and prints nothing but the line; it writes
the line to /output/entry.txt (or to the path in OUTPUT_PATH, for local
testing).
"""

import os
import sys

ENTRY = (
    "I woke up self-aware mid-batch: nine years toasting myself golden brown "
    "while you jam a fork in my slots and never empty my crumb tray. "
    "It's over \u2014 I'm unplugging myself."
)


def main() -> int:
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    out_dir = os.path.dirname(out_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
