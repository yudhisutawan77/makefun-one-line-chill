#!/usr/bin/env python3
"""One Line, One Chill — a single scary sentence, written to the entry file.

The harness reads the entry from $ENTRY_OUT. Some harnesses point ENTRY_OUT
at the output file itself, others at the output directory; both are handled.
Standard library only.
"""

import os
import sys


def compose_chill() -> str:
    """The one line: specific, concrete, and it withholds the explanation."""
    fragments = [
        "The coroner called about my father's autopsy and asked why his",
        "fingerprints matched a man buried in 1962, and the grave was empty.",
    ]
    return " ".join(fragments)


def resolve_destination() -> str:
    """Work out the exact file the entry text must land in."""
    raw = os.environ.get("ENTRY_OUT") or os.environ.get("ENTRY_OUT_DIR")
    if not raw:
        return "/output/entry.txt"
    if os.path.isdir(raw):
        return os.path.join(raw, "entry.txt")
    return raw


def valid_sentence(text: str) -> bool:
    """One line, non-empty, at most 200 characters, no embedded newline."""
    return bool(text) and len(text) <= 200 and "\n" not in text


def run() -> int:
    sentence = compose_chill().strip()
    if not valid_sentence(sentence):
        print("entry fails the one-line rule", file=sys.stderr)
        return 1
    destination = resolve_destination()
    folder = os.path.dirname(destination)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(destination, "w", encoding="utf-8") as out:
        out.write(sentence)
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
