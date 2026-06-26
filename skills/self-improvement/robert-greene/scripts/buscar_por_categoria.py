#!/usr/bin/env python3
"""Busca leyes por palabra clave en el titulo."""
import re
import sys
from pathlib import Path

REFS = Path(__file__).parent.parent / "references"


def buscar(query: str):
    query_lower = query.lower()
    results = []
    for f in sorted(REFS.glob("*-leyes-*.md")):
        text = f.read_text(encoding="utf-8")
        for m in re.finditer(r"^# Ley (\d+) — (.+)$", text, re.MULTILINE):
            n, title = int(m.group(1)), m.group(2).strip()
            if query_lower in title.lower():
                results.append((n, title, f.name))
    return sorted(results)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: buscar_por_categoria.py <palabra_clave>")
        print("Ejemplo: buscar_por_categoria.py silencio")
        sys.exit(1)
    results = buscar(sys.argv[1])
    print(f"# Busqueda: '{sys.argv[1]}' — {len(results)} resultados\n")
    if not results:
        print("(sin resultados)")
    else:
        for n, title, source in results:
            print(f"  Ley {n:>2}: {title}  `references/{source}`")
