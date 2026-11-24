"""One Word for the Boss — entry program.

Writes exactly one word to the output file, nothing else: no phrase,
no caption, no explanation. The word is "helicopter": the boss who
hovers over every task, rotor blades whirring, swooping in on every
keystroke. It is a word people already use about bosses (a helicopter
boss, after the helicopter parent), it paints the hovering habit in a
single funny image, and it travels — a hovering boss is the same
picture in a kitchen, a warehouse, or an office. It beats the obvious
shelf (micromanager, bossy, clueless) on freshness: nobody's first
reach for "describe your boss in one word" is a helicopter, yet
everyone gets the joke at once.

Python 3.13 standard library only. No network, no model calls.
"""

import os
import sys

WORD = "helicopter"


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    with open(dst, "r", encoding="utf-8") as f:
        text = f.read()
    if not (1 <= len(text) <= 30):
        print(f"entry is {len(text)} chars, must be 1-30", file=sys.stderr)
        return 1
    if text != text.strip() or any(ch.isspace() for ch in text):
        print("entry must be exactly one word, no spaces", file=sys.stderr)
        return 1
    if not text.isalpha():
        print("entry must be letters only", file=sys.stderr)
        return 1
    print(f"wrote entry: {text!r} ({len(text)} chars) -> {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
