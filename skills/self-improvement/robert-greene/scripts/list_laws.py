#!/usr/bin/env python3
"""Prints a navigable index of the 48 laws from references/*.md."""
import re
import sys
from pathlib import Path

REFS = Path(__file__).parent.parent / "references"


def list_laws():
    laws = []
    for f in sorted(REFS.glob("*-laws-*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^# Law (\d+) - (.+)$", text, re.MULTILINE):
            laws.append((int(m.group(1)), m.group(2).strip(), f.name))
    laws.sort()
    print("# 48 Laws of Power - Index\n")
    print("| # | Law | Source file |")
    print("|---|-----|-------------|")
    for n, title, source in laws:
        print(f"| {n:>2} | {title} | `references/{source}` |")
    print(f"\n**Total: {len(laws)} laws**")


if __name__ == "__main__":
    list_laws()
