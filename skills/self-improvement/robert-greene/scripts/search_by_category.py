#!/usr/bin/env python3
"""Searches laws by keyword in the title."""
import re
import sys
from pathlib import Path

REFS = Path(__file__).parent.parent / "references"


def search(query: str):
    query_lower = query.lower()
    results = []
    for f in sorted(REFS.glob("*-laws-*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^# Ley (\d+) — (.+)$", text, re.MULTILINE):
            n, title = int(m.group(1)), m.group(2).strip()
            if query_lower in title.lower():
                results.append((n, title, f.name))
    return sorted(results)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: search_by_category.py <keyword>")
        print("Example: search_by_category.py silence")
        sys.exit(1)
    results = search(sys.argv[1])
    print(f"# Search: '{sys.argv[1]}' — {len(results)} results\n")
    if not results:
        print("(no results)")
    else:
        for n, title, source in results:
            print(f"  Law {n:>2}: {title}  `references/{source}`")
