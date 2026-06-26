# Robert Greene — Hermes Skill

![Header banner — Robert Greene Skill](assets/header.jpg)

> Las 48 Leyes del Poder empaquetadas como skill de [Hermes Agent](https://hermes-agent.nousresearch.com).

[![Skill](https://img.shields.io/badge/hermes-skill-blue)]()
[![License](https://img.shields.io/badge/license-MIT-green)]()
[![Leyes](https://img.shields.io/badge/leyes-48%2F48-purple)]()

## ¿Qué es esto?

Esta skill convierte el compendio [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder) en una **skill consultable** por cualquier sesión de Hermes. Cuando se carga, el agente puede:

- Citar cualquier ley con contexto
- Recomendar la ley adecuada para una situación
- Explicar tensiones entre leyes complementarias
- Señalar trampas éticas de aplicación

> ⚠️ **Estado actual:** Este repo está publicado para **análisis y revisión** de la estructura de la skill. **NO está instalado** en `~/.hermes/skills/` del autor ni de nadie más. Si quieres probarlo en tu instalación de Hermes, sigue las instrucciones de abajo.

## Instalación (opcional, manual)

### Opción A: Symlink al loader de Hermes

```bash
git clone https://github.com/ooovenenoso/robert-greene-skill.git
mkdir -p ~/.hermes/skills/self-improvement
ln -s "$(pwd)/robert-greene-skill/skills/self-improvement/robert-greene" \
      ~/.hermes/skills/self-improvement/robert-greene
```

Después de esto, en una sesión **nueva** de Hermes:

```
skill_view(name='robert-greene')
```

> Nota: el loader de Hermes está cacheado por sesión, así que la skill solo será visible en sesiones iniciadas **después** del symlink.

### Opción B: Carga directa desde path absoluto

Pasar la ruta absoluta a `skill_view()` cuando el loader lo soporte.

## Estructura

```
skills/self-improvement/robert-greene/
├── SKILL.md                      # Entry point (<= 20k chars, peer-matched)
├── references/
│   ├── 00-glossary.md            # Vocabulario recurrente
│   ├── 01-categories.md          # Las 6 categorias consolidadas
│   ├── 02-laws-01-08.md         # Bloque 1: Autoridad y Presencia
│   ├── 03-laws-09-16.md         # Bloque 2: Estrategia y Tiempo
│   ├── 04-laws-17-24.md         # Bloque 3: Continuacion
│   ├── 05-laws-25-32.md         # Bloque 4: Reputacion y Psicologia
│   ├── 06-laws-33-40.md         # Bloque 5: Autodefensa
│   ├── 07-laws-41-48.md         # Bloque 6: Cierre
│   ├── 08-compendiums.md         # resumen + mapa de leyes
│   ├── 09-historical-figures.md  # ~25 personajes citados
│   ├── 10-bibliography.md        # Greene + obras complementarias
│   └── 11-how-to-study.md        # Metodo de 4 niveles
└── scripts/
    ├── list_laws.py               # Indice navegable
    ├── search_by_category.py      # Busqueda por palabra clave
    └── validate_skill.py          # Validador CLI
```

`assets/` contiene la imagen de banner del README (`header.jpg`, 1280x511).

## Uso

Una vez instalada, en cualquier sesión de Hermes:

```
Usuario: "¿Qué ley aplica cuando quiero pedir un aumento?"
Hermes: [carga skill robert-greene → recomienda Ley 13 + Ley 45 + Ley 9]
```

## Scripts incluidos

```bash
# Listar las 48 leyes
python3 skills/self-improvement/robert-greene/scripts/listar_leyes.py

# Buscar por palabra clave
python3 skills/self-improvement/robert-greene/scripts/buscar_por_categoria.py silencio

# Validar estructura (sin pytest)
python3 skills/self-improvement/robert-greene/scripts/validar_skill.py
```

## Tests

```bash
pip install pytest pyyaml
python3 -m pytest tests/ -v
```

## Licencia

MIT — ver [`LICENSE`](LICENSE).

## Crítica

El material es **inspirado** en la obra de Robert Greene; el texto completo de cada ley es **original** de este repo y del compendio [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder). El SKILL.md incluye un marco ético obligatorio (🟢 defensivo / 🟡 aplicado / 🔴 tóxico) para guiar el uso del agente.

## Repo relacionado

- Compendio fuente: [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder)
- Esta skill: [`ooovenenoso/robert-greene-skill`](https://github.com/ooovenenoso/robert-greene-skill)
