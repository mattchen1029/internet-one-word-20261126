#!/usr/bin/env python3
"""The Internet in One Word — make.fun entry.

Writes a single word describing the whole internet to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The word is "unhinged": one word, funny on its own, true of the whole
internet rather than one site or mood, surprising instead of the obvious
pick, and short enough to land in one beat.
"""

import os

WORD = "unhinged"

MIN_CHARS = 1
MAX_CHARS = 30
OUTPUT_NAME = "entry.txt"


def validate_word(word):
    if not (MIN_CHARS <= len(word) <= MAX_CHARS):
        raise ValueError("word must be %d-%d chars, got %d" % (MIN_CHARS, MAX_CHARS, len(word)))
    if len(word.split()) != 1:
        raise ValueError("word must be a single word, got %r" % word)
    if not word.strip():
        raise ValueError("word must not be only whitespace")


def write_entry(word, out_dir):
    validate_word(word)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, OUTPUT_NAME)
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    # The grader collects outputs as another user: leave it world-readable.
    os.chmod(path, 0o644)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(WORD, out_dir)
    print(f"Wrote {len(WORD)} characters to {path}")


if __name__ == "__main__":
    main()
