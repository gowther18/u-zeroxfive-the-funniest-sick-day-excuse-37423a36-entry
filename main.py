#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — make.fun entry.

Writes one sick-day excuse (135 characters, one line) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The excuse is fixed and deterministic: every run writes the exact same
bytes, with no trailing newline, so the two grading runs agree.
"""

import os
import sys

EXCUSE = (
    # One breath, one line: the symptom is real (an eye twitch), the
    # punchline lands on the last words ("stop flirting with the clients"),
    # and nothing in it is a worn excuse — no fever, no dog, no dead
    # grandmother, no sneezed-out back. 135 characters, no trailing newline.
    "Can't come in today — my eye is twitching so hard it keeps winking "
    "at strangers, and HR has asked me to stop flirting with the clients."
)


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
