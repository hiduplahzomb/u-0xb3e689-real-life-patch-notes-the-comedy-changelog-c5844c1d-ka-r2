#!/usr/bin/env python3
"""Real Life Patch Notes: The Comedy Changelog.

Writes one original line to /output/entry.txt: a fake patch note for
real life — version number plus fix, deadpan. The fix targets a
UI/UX race condition in a fatigued system: the mouth ships sentences
before the brain finishes loading them, so words render out of order.
No battery, energy, or sleep-cycle metaphor anywhere — the joke is
pure rendering-pipeline jargon colliding with a biological function,
and the version bump is the only framing the entry needs.
"""

import os
import sys

TEXT = (
    "v2.4.2: fixed race condition where the mouth shipped sentences "
    "before the brain finished loading them; words now render in "
    "order, even after 18 hours awake."
)
MAX_CHARS = 200


def main() -> int:
    text = TEXT
    if not (1 <= len(text) <= MAX_CHARS):
        print(f"entry length {len(text)} outside 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if "\n" in text.strip():
        print("entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
