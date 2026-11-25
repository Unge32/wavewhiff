#!/usr/bin/env python3
"""WAVEWHIFF -- one invented English word and its one-line definition.

The program reads word.json (the word's data file) and writes the
word + definition line to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt on the grader, or ./out/entry.txt by hand).
Pure Python 3 standard library, no network, fully deterministic.

The line is 84 characters, inside the 1-140 gate. Wavewhiff is the
named hook: the wave you return to a stranger who was never waving
at you -- they were waving at someone behind you.
"""

import json
import os
import sys

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "word.json")


def main():
    if not os.path.isfile(DATA_FILE):
        print("error: word.json missing next to main.py", file=sys.stderr)
        sys.exit(1)
    with open(DATA_FILE, encoding="utf-8") as f:
        data = json.load(f)
    word = data["word"]
    definition = data["definition"]
    line = "%s \u2014 %s." % (word, definition)
    assert 1 <= len(line) <= 140, "line outside the 1-140 gate"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or (
        "/output" if os.path.isdir("/output") else "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify: the entry on disk must be exactly the line.
    with open(path, encoding="utf-8") as f:
        if f.read() != line:
            print("error: entry.txt on disk does not match the line", file=sys.stderr)
            sys.exit(1)
    print("wrote %s %d characters" % (path, len(line)))


if __name__ == "__main__":
    main()
