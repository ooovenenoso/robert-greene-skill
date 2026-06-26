# Robert Greene — Hermes Skill

![Header banner — Robert Greene Skill](assets/header.jpg)

> The 48 Laws of Power packaged as a [Hermes Agent](https://hermes-agent.nousresearch.com) skill.

[![Skill](https://img.shields.io/badge/hermes-skill-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Laws](https://img.shields.io/badge/laws-48%2F48-purple)]()

## What is this?

This skill distills the public compendium [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder) into a **consultable skill** that any Hermes session can load. Once loaded, the agent can:

- Cite any law with context
- Recommend the right law for a situation
- Explain tensions between complementary laws
- Flag ethical traps in application

> ⚠️ **Current state:** This repo is published for **analysis and review** of the skill structure. It is **not installed** in `~/.hermes/skills/` of the author or anyone else. If you want to try it in your own Hermes installation, follow the instructions below.

## Installation (optional, manual)

### Option A: Symlink to the Hermes loader

```bash
git clone https://github.com/ooovenenoso/robert-greene-skill.git
mkdir -p ~/.hermes/skills/self-improvement
ln -s "$(pwd)/robert-greene-skill/skills/self-improvement/robert-greene" \
      ~/.hermes/skills/self-improvement/robert-greene
```

Then, in a **new** Hermes session:

```
skill_view(name='robert-greene')
```

> Note: the Hermes loader is cached per session, so the skill will only become visible in sessions started **after** the symlink.

### Option B: Direct load from absolute path

Pass the absolute path to `skill_view()` when the loader supports it.

## Structure

```
skills/self-improvement/robert-greene/
├── SKILL.md                      # Entry point (<= 20k chars, peer-matched)
├── references/
│   ├── 00-glossary.md            # Recurring vocabulary
│   ├── 01-categories.md          # The 6 categories consolidated
│   ├── 02-laws-01-08.md         # Block 1: Authority and Presence
│   ├── 03-laws-09-16.md         # Block 2: Strategy and Timing
│   ├── 04-laws-17-24.md         # Block 3: Continuation
│   ├── 05-laws-25-32.md         # Block 4: Reputation and Psychology
│   ├── 06-laws-33-40.md         # Block 5: Self-Defense
│   ├── 07-laws-41-48.md         # Block 6: Closing
│   ├── 08-compendiums.md         # summary + map of laws
│   ├── 09-historical-figures.md  # ~25 cited figures
│   ├── 10-bibliography.md        # Greene + complementary works
│   └── 11-how-to-study.md        # 4-level method
└── scripts/
    ├── list_laws.py               # Navigable index
    ├── search_by_category.py      # Keyword search
    └── validate_skill.py          # CLI validator
```

`assets/` contains the README banner image (`header.jpg`, 1280x511).

## Usage

Once installed, in any Hermes session:

```
User: "Which law applies when I want to ask for a raise?"
Hermes: [loads robert-greene skill -> recommends Law 13 + Law 45 + Law 9]
```

## Included scripts

```bash
# List the 48 laws
python3 skills/self-improvement/robert-greene/scripts/list_laws.py

# Search by keyword
python3 skills/self-improvement/robert-greene/scripts/search_by_category.py silence

# Validate structure (without pytest)
python3 skills/self-improvement/robert-greene/scripts/validate_skill.py
```

## Tests

```bash
pip install pytest pyyaml
python3 -m pytest tests/ -v
```

## License

MIT — see [`LICENSE`](LICENSE).

## Provenance

The material is **inspired** by Robert Greene's work; the full text of each law is **original** to this repo and the source compendium ([`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder)). The `SKILL.md` includes a mandatory ethical framework (defensive / applied-with-ethics / toxic) to guide the agent's use.

## Related repos

- Source compendium: [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder) (Spanish)
- This skill: [`ooovenenoso/robert-greene-skill`](https://github.com/ooovenenoso/robert-greene-skill) (English)
