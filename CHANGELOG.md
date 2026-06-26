# Changelog

## [1.0.0] - 2026-06-26

### Added
- Initial release of the `robert-greene` skill (Hermes-compatible)
- `SKILL.md` — peer-matched entry point (9.4k chars, < 20k target)
- `references/` — 12 files:
  - `00-glosario.md` — vocabulario recurrente
  - `01-categorias.md` — 6 categorias consolidadas
  - `02-leyes-01-08.md` through `07-leyes-41-48.md` — 48 laws in 6 blocks of 8
  - `08-compendios.md` — resumen + mapa de leyes + indice por categoria
  - `09-figuras-historicas.md` — ~25 personajes citados
  - `10-bibliografia.md` — Greene + obras complementarias + cursos
  - `11-como-estudiar.md` — metodo de 4 niveles + rituales
- `scripts/` — 3 utility scripts:
  - `listar_leyes.py` — indice navegable
  - `buscar_por_categoria.py` — busqueda por palabra clave
  - `validar_skill.py` — validador CLI
- `tests/test_estructura.py` — pytest suite (8 tests)
- Comprehensive README.md with installation instructions

### Frontmatter
- `name: robert-greene`
- `description`: 318 chars (limit 1024)
- `version: 1.0.0`
- `author: Kevin Ramos Montañez`
- `license: MIT`

### Notes
- Repo is **public** for analysis and review
- **NOT installed** in `~/.hermes/skills/` — installation is opt-in (manual symlink)
- Source compendium: [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder)
- All 48 law texts are original to this repo and the source compendium (inspired by, not copied from, Robert Greene's book)

### Verification
- 8/8 pytest tests pass
- 10/10 validar_skill.py checks pass
- SKILL.md frontmatter validated by smoke test
