#!/usr/bin/env python3
"""Entry program for make.fun bounty u-steady-puffin-78-1922-one-star-written-in-sap-2ea1f4f4.

Writes a one-line 1-star review from a houseplant about its human owner
to entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""
import os

TEXT = "One star. Repotted me on Monday into a pot 2 sizes too small, then blamed my roots for not growing by Friday."

def main():
    # Gate (kit competition.yaml): UTF-8 text, 1-279 chars, not only
    # whitespace, one line.
    assert 1 <= len(TEXT) <= 279, f"entry is {len(TEXT)} chars"
    assert TEXT.strip(), "entry must not be only whitespace"
    assert "\n" not in TEXT, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
