"""Verifica la estructura completa de la skill robert-greene."""
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent / "skills/self-improvement/robert-greene"
REFS = SKILL_ROOT / "references"
SCRIPTS = SKILL_ROOT / "scripts"


def test_skill_md_exists():
    assert (SKILL_ROOT / "SKILL.md").is_file(), "SKILL.md no existe"


def test_skill_md_frontmatter_starts_with_yaml():
    content = (SKILL_ROOT / "SKILL.md").read_text()
    assert content.startswith("---\n"), "SKILL.md debe empezar con ---"


def test_skill_md_has_required_frontmatter_fields():
    import yaml
    content = (SKILL_ROOT / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert m, "Frontmatter no encontrado"
    fm = yaml.safe_load(m.group(1))
    assert "name" in fm, "Falta campo 'name'"
    assert "description" in fm, "Falta campo 'description'"
    assert len(fm["description"]) <= 1024, f"description muy larga ({len(fm['description'])} > 1024)"
    assert fm["name"] == "robert-greene"


def test_skill_md_size_limit():
    content = (SKILL_ROOT / "SKILL.md").read_text()
    assert len(content) <= 100_000, f"SKILL.md demasiado grande ({len(content)} > 100k)"
    assert len(content) <= 20_000, f"SKILL.md > 20k, debería dividir a references/"


def test_48_law_files_exist():
    law_files = list(REFS.glob("*-leyes-*.md"))
    assert len(law_files) == 6, f"Esperados 6 archivos de leyes, encontrados {len(law_files)}"


def test_48_law_numbers_present_in_references():
    law_files = sorted(REFS.glob("*-leyes-*.md"))
    all_text = "".join(f.read_text() for f in law_files)
    missing = [n for n in range(1, 49) if not re.search(rf"# Ley {n}\b", all_text)]
    assert not missing, f"Leyes faltantes: {missing}"


def test_6_categorias_present():
    cats_file = REFS / "01-categorias.md"
    assert cats_file.is_file(), "01-categorias.md no existe"
    content = cats_file.read_text()
    expected = [
        "Autoridad y Presencia",
        "Estrategia y Tiempo",
        "Reputación y Percepción",
        "Relaciones y Alianzas",
        "Autodefensa",
        "Psicología y Sombra",
    ]
    for cat in expected:
        assert cat in content, f"Categoria '{cat}' no encontrada"


def test_scripts_directory_has_3_scripts():
    scripts = list(SCRIPTS.glob("*.py"))
    assert len(scripts) >= 3, f"Esperados >= 3 scripts, encontrados {len(scripts)}"
