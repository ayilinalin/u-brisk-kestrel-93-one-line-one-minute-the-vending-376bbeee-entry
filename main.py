#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest.

Writes a single pickup line — one a vending machine would use on a
passing human — to /output/entry.txt.

The line: the machine brags about its spotless record (a thousand
snacks, never a jam), then the human walks past and the machine itself
jams — on them. First-person machine voice, coils and jamming from the
machine's own world, punch on the last words ("stuck on you" does
double duty: a jammed coil, and a crush).
"""

from pathlib import Path

ENTRY = (
    "A thousand snacks spun through my coils and not one ever jammed — "
    "then you walked past, and now I'm stuck on you."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the one line, byte for byte.
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
