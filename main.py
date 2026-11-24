#!/usr/bin/env python3
"""The Houseplant Out-of-Office.

Writes one out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Deterministic, no network, no input.
"""

import os
import sys

ENTRY = "Out of office: I'm the fern. Unwatered since March, I've unionised with the dust bunnies. Your email is now compost."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
