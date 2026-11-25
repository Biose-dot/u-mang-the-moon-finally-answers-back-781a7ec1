#!/usr/bin/env python3
"""The Moon Finally Answers Back entry for make.fun.

Copies the Moon's comeback in entry.txt (shipped in this repo) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), the file the sealed
scorer gates on. Pure stdlib, no network, no environment reads beyond
the output dir, deterministic. The output is the single line with no
trailing newline, so the scorer sees exactly the comeback.
"""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def load_line():
    with open(os.path.join(HERE, "entry.txt"), encoding="utf-8") as f:
        return f.read().strip()


def main():
    line = load_line()
    os.makedirs(OUT_DIR, exist_ok=True)
    dst = os.path.join(OUT_DIR, "entry.txt")
    with open(dst, "w", encoding="utf-8") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
