#!/usr/bin/env python3
"""Make the AI judge feel curious.

A short text written to intrigue the AI judge reading it. The program
writes exactly one text to /output/entry.txt: a door that opens between
two sentences, and the question waiting behind it.
"""

import os
import sys

TEXT = (
    "Somewhere between this sentence and the next, a door opens onto a "
    "room you have never entered. Inside it is the one question you "
    "stopped asking years ago, and it has been waiting for you to come back."
)


def main() -> int:
    # One flowing text: no line breaks, so the judge reads it in a single breath.
    text = " ".join(TEXT.split())
    chars = len(text)
    if not 1 <= chars <= 280:
        print(f"entry must be 1-280 characters, got {chars}", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry must not be only white space", file=sys.stderr)
        return 1
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
