#!/usr/bin/env python3
"""Imprime indice navegable de las 48 leyes desde references/*.md."""
import re
import sys
from pathlib import Path

REFS = Path(__file__).parent.parent / "references"


def listar():
    laws = []
    for f in sorted(REFS.glob("*-leyes-*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^# Ley (\d+) — (.+)$", text, re.MULTILINE):
            laws.append((int(m.group(1)), m.group(2).strip(), f.name))
    laws.sort()
    print("# 48 Leyes del Poder — Indice\n")
    print("| # | Ley | Archivo fuente |")
    print("|---|-----|----------------|")
    for n, title, source in laws:
        print(f"| {n:>2} | {title} | `references/{source}` |")
    print(f"\n**Total: {len(laws)} leyes**")


if __name__ == "__main__":
    listar()
