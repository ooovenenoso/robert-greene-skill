"""Verifies the complete structure of the robert-greene skill."""
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).parent.parent / "skills/self-improvement/robert-greene"
REFS = SKILL_ROOT / "references"
SCRIPTS = SKILL_ROOT / "scripts"


def test_skill_md_exists():
    assert (SKILL_ROOT / "SKILL.md").is_file(), "SKILL.md missing"


def test_skill_md_frontmatter_starts_with_yaml():
    content = (SKILL_ROOT / "SKILL.md").read_text()
    assert content.startswith("---\n"), "SKILL.md must start with ---"


def test_skill_md_has_required_frontmatter_fields():
    import yaml
    content = (SKILL_ROOT / "SKILL.md").read_text()
    m = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    assert m, "Frontmatter not found"
    fm = yaml.safe_load(m.group(1))
    assert "name" in fm, "Missing 'name' field"
    assert "description" in fm, "Missing 'description' field"
    assert len(fm["description"]) <= 1024, f"description too long ({len(fm['description'])} > 1024)"
    assert fm["name"] == "robert-greene", f"name must be 'robert-greene' (got '{fm.get('name')}')"


def test_skill_md_size_limit():
    content = (SKILL_ROOT / "SKILL.md").read_text()
    assert len(content) <= 100_000, f"SKILL.md too big ({len(content)} > 100k)"
    assert len(content) <= 20_000, f"SKILL.md > 20k, should split to references/"


def test_48_law_files_exist():
    law_files = list(REFS.glob("*-laws-*.md"))
    assert len(law_files) == 6, f"Expected 6 law files, found {len(law_files)}"


def test_48_law_numbers_present_in_references():
    law_files = sorted(REFS.glob("*-laws-*.md"))
    all_text = "".join(f.read_text() for f in law_files)
    missing = [n for n in range(1, 49) if not re.search(rf"# Ley {n}\b", all_text)]
    assert not missing, f"Missing laws: {missing}"


def test_6_categories_present():
    cats_file = REFS / "01-categories.md"
    assert cats_file.is_file(), "01-categories.md missing"
    content = cats_file.read_text()
    expected = [
        "Authority and Presence",
        "Strategy and Timing",
        "Reputation and Perception",
        "Relationships and Alliances",
        "Self-Defense",
        "Psychology and Shadow",
    ]
    for cat in expected:
        assert cat in content, f"Category '{cat}' not found"


def test_scripts_directory_has_3_scripts():
    scripts = list(SCRIPTS.glob("*.py"))
    assert len(scripts) >= 3, f"Expected >= 3 scripts, found {len(scripts)}"


def test_scripts_have_english_names():
    """After translation, script names must be in English."""
    scripts = sorted(p.name for p in SCRIPTS.glob("*.py"))
    expected = {"list_laws.py", "search_by_category.py", "validate_skill.py"}
    assert set(scripts) >= expected, f"Missing scripts: {expected - set(scripts)}"


def test_references_have_english_names():
    """Reference files use English names."""
    refs = sorted(p.name for p in REFS.glob("*.md"))
    assert "01-categories.md" in refs, "01-categories.md missing"
    assert "08-compendiums.md" in refs, "08-compendiums.md missing"
    assert "09-historical-figures.md" in refs, "09-historical-figures.md missing"
    assert "11-how-to-study.md" in refs, "11-how-to-study.md missing"


def test_skill_md_in_english():
    """SKILL.md body should be primarily English (sample check)."""
    content = (SKILL_ROOT / "SKILL.md").read_text()
    # Check first body paragraph is in English
    assert "Class-level skill" in content or "Use this skill" in content, \
        "SKILL.md body should be in English"
