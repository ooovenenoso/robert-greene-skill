#!/usr/bin/env python3
"""Valida la estructura completa de la skill robert-greene.

Uso: python3 validar_skill.py
Exit code: 0 si todo OK, 1 si hay errores.
"""
import re
import sys
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent
SKILL_MD = SKILL_ROOT / "SKILL.md"
REFS = SKILL_ROOT / "references"
SCRIPTS = SKILL_ROOT / "scripts"

ERRORS = []
OK = []


def check(cond, msg):
    (OK if cond else ERRORS).append(msg)


# Frontmatter
if SKILL_MD.is_file():
    content = SKILL_MD.read_text()
    check(content.startswith("---\n"), "SKILL.md empieza con ---")
    m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if m:
        import yaml
        try:
            fm = yaml.safe_load(m.group(1))
            check("name" in fm, "frontmatter tiene 'name'")
            check("description" in fm, "frontmatter tiene 'description'")
            if "description" in fm:
                check(len(fm["description"]) <= 1024,
                      f"description <= 1024 chars ({len(fm['description'])})")
            check(fm.get("name") == "robert-greene", f"name == 'robert-greene'")
        except yaml.YAMLError as e:
            ERRORS.append(f"YAML invalido: {e}")
    check(len(content) <= 100_000, f"SKILL.md <= 100k chars ({len(content)})")
else:
    ERRORS.append("SKILL.md no existe")


# References
if REFS.is_dir():
    refs = list(REFS.glob("*.md"))
    check(len(refs) >= 11, f">= 11 archivos en references/ (encontrados: {len(refs)})")

    law_files = sorted(REFS.glob("*-leyes-*.md"))
    check(len(law_files) == 6, f"6 archivos de leyes (encontrados: {len(law_files)})")

    all_text = "".join(f.read_text() for f in law_files)
    missing = [n for n in range(1, 49) if not re.search(rf"# Ley {n}\b", all_text)]
    check(not missing, f"48 leyes presentes (faltan: {missing or 'ninguna'})")
else:
    ERRORS.append("references/ no existe")


# Scripts
if SCRIPTS.is_dir():
    scripts = list(SCRIPTS.glob("*.py"))
    check(len(scripts) >= 3, f">= 3 scripts (encontrados: {len(scripts)})")
else:
    ERRORS.append("scripts/ no existe")


# Resumen
print(f"\n{'='*50}\nValidacion: {len(OK)} OK | {len(ERRORS)} errores\n{'='*50}\n")
for msg in OK:
    print(f"  [OK] {msg}")
for msg in ERRORS:
    print(f"  [ERR] {msg}")

sys.exit(1 if ERRORS else 0)
