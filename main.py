#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

A deterministic program that writes one original line - a review of planet
Earth left by an alien tourist - to /output/entry.txt (at most 200 chars).

Python 3.13 standard library only. No input, no network, no randomness:
every run writes the exact same bytes.
"""

from pathlib import Path

REVIEW = (
    "Came for the oceans, stayed for the dogs. "
    "The locals carry their pets' waste away in little bags and call it love. "
    "Charming species. 5 stars, would orbit again."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = REVIEW
    assert 1 <= len(text) <= 200, f"review is {len(text)} characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
