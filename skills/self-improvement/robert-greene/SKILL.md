---
name: robert-greene
description: "Use when the user asks about Las 48 Leyes del Poder, Robert Greene's power dynamics, wants a specific law cited by number or theme, asks which law applies to a specific situation (negotiation, conflict, leadership, seduction, reputation, self-defense, time strategy, or influence dynamics), or wants the ethical considerations around applying a specific law. Distinguish defensive, applied-with-ethics, and toxic use before recommending any application."
version: 1.2.0
author: Kevin Ramos Montañez
license: MIT
metadata:
  hermes:
    tags: [self-improvement, robert-greene, power, strategy, philosophy, ethics, persuasion]
    related_skills: [plan, hermes-skill-operations]
changelog:
  - 1.2.0 (2026-06-26): Translated all 48 law bodies from Spanish to English; updated tests, scripts, and SKILL.md to enforce English-only references. Repo is now 100% English.
  - 1.1.0 (2026-06-26): Translated to English, restyled to peer shape (removed decorative emojis, tightened frontmatter, peer-matched description), added scripts/ utility index in body.
  - 1.0.0 (2026-06-26): Initial Spanish release with 48 laws across 6 categories.
---

# Robert Greene — 48 Laws of Power

Class-level skill for end-to-end work with Las 48 Leyes del Poder: cite any law with context, recommend the right law for a user's situation, explain tensions between complementary laws, and surface the ethical line between defensive recognition and active manipulation.

## When to Use

Use this skill when:

- The user asks "what is law N?" or "what does the law say about X?"
- The user asks for a recommendation: "which law applies when I want to ask for a raise / negotiate / lead / defend myself?"
- The user mentions Robert Greene, Las 48 Leyes, or derivative phrases ("hide your intentions", "draw them out with absence", "master the art of timing").
- The user wants to **understand** how power operates (academic, professional, self-knowledge).
- The user wants to **defend themselves** from manipulations they recognize in others.

Do NOT use this skill for:

- Justifying harm to third parties.
- Writing propaganda or mass manipulation material.
- Replacing professional legal or therapeutic advice.
- Any situation where the right answer is "do nothing" rather than a law.

## The ethical framework (mandatory)

The 48 laws **describe** how power operates in the world; they are not a license to manipulate. Before recommending any application, classify it:

- **Defensive** — recognizing the move before it is used against you. Legitimate, recommended.
- **Applied with ethics** — using the law to advance without destroying. Valid with judgment.
- **Toxic** — actively manipulating others. Reject.

If the user asks for a "toxic" application, redirect to professional help or say explicitly: "I can't help with that." Never recommend a law without naming its ethical level.

## The 6 categories

| # | Category | Laws | Focus |
|---|----------|------|-------|
| 1 | **Authority and Presence** | 1, 2, 3, 4, 6, 14, 28, 34 | How you are seen and treated |
| 2 | **Strategy and Timing** | 9, 13, 15, 16, 17, 22, 23, 29, 31, 35, 45 | When and where you act |
| 3 | **Reputation and Perception** | 5, 25, 26, 30, 37, 40, 46 | The story you tell about yourself |
| 4 | **Relationships and Alliances** | 7, 8, 11, 12, 20, 27, 41 | Your network as infrastructure |
| 5 | **Self-Defense** | 10, 18, 19, 42, 44, 47 | Protect yourself without self-destruction |
| 6 | **Psychology and Shadow** | 21, 24, 32, 33, 36, 38, 39, 43, 48 | The invisible part of the game |

Full detail in [`references/01-categories.md`](references/01-categories.md).

## The 48 laws — quick index

### Block 1: Authority and Presence (Laws 1–8)

[`references/02-laws-01-08.md`](references/02-laws-01-08.md)

1. Never outshine the master
2. Never put too much trust in friends, learn how to use enemies
3. Conceal your intentions
4. Always say less than necessary
5. So much depends on reputation — guard it with your life
6. Court attention at all cost
7. Get others to do the work for you, but always take the credit
8. Use absence to increase respect and value
9. Win through your actions, never through argument

### Block 2: Strategy and Timing (Laws 9–16)

[`references/03-laws-09-16.md`](references/03-laws-09-16.md)

10. Avoid the unhappy and unlucky
11. Learn to keep people dependent on you
12. Use selective honesty and generosity to disarm your victim
13. When asking for help, appeal to people's self-interest, never to their mercy or gratitude
14. Pose as a friend, work as a spy
15. Crush your enemy totally
16. Use absence to increase respect and value (rephrased in compendium: master the art of timing)
17. Build up your presence through controlled displays and perfect your image

### Block 3 (Laws 17–24)

[`references/04-laws-17-24.md`](references/04-laws-17-24.md)

17. Control the territory: learn to use the terrain
18. Do not build fortresses — isolation is dangerous
19. Know who you're dealing with — do not offend the wrong person
20. Do not commit to anyone
21. Play a sucker to catch a sucker — seem dumber than your mark
22. Use the surrender tactic: transform weakness into power
23. Concentrate your forces
24. Play the perfect courtier — master the art of impression management

### Block 4 (Laws 25–32)

[`references/05-laws-25-32.md`](references/05-laws-25-32.md)

25. Re-create yourself — do not accept the role you are assigned
26. Keep your hands clean — use others as your cat's-paw
27. Create a cult-like following — be charismatic and be loved
28. Enter action with boldness
29. Plan all the way to the end
30. Make your accomplishments seem effortless
31. Control the options: get others to play with the cards you deal
32. Play on people's fantasies — appeal to their dreams

### Block 5: Self-Defense (Laws 33–40)

[`references/06-laws-33-40.md`](references/06-laws-33-40.md)

33. Discover each person's weakness and use it
34. Act like a king to be treated like one
35. Master the art of timing
36. Disdain things you cannot have — ignoring them is the best revenge
37. Create compelling spectacles — use grand gestures
38. Think as you like but behave like others
39. Stir up emotions to influence people's perceptions
40. Despise the free lunch — never give your work away

### Block 6: Closing (Laws 41–48)

[`references/07-laws-41-48.md`](references/07-laws-41-48.md)

41. Avoid stepping into a great man's shoes — come up with your own
42. Strike the shepherd and the sheep will scatter
43. Work on the hearts and minds of others
44. Disarm and poison with the illusion of kindness
45. Beg for something big and you will get something smaller
46. Never appear too perfect — flaws breed affection
47. Do not go past the target you were aiming at — victory can be a trap
48. Assume formlessness — flow like water

> Note: Law titles above use Robert Greene's published English phrasing. The source compendium ([`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder)) uses personalized Spanish translations; both versions are valid for citation. This skill's full law bodies (in `references/02-laws-01-08.md` through `references/07-laws-41-48.md`) are written in English.

## Recommendation patterns

When the user presents a situation, map it to laws:

| User situation | Laws to consider | Category |
|----------------|------------------|----------|
| Asking for a raise / salary | 9, 13, 45 | Strategy |
| Negotiating a contract | 17, 23, 31, 45 | Strategy |
| Dealing with a difficult boss | 1, 14, 22 | Authority + Self-Defense |
| Building reputation | 5, 6, 25, 27, 37 | Reputation |
| Leaving a toxic relationship | 10, 22, 36, 47 | Self-Defense |
| Public speaking / keynote | 34, 37, 39 | Authority + Reputation |
| Defending against manipulation | 3, 33, 44, 19 | Self-Defense |
| Leading a team | 7, 8, 11, 27 | Relationships |
| Starting a project / startup | 23, 28, 29, 48 | Strategy |
| Reconnecting after a fight | 12, 22, 30, 47 | Relationships + Reputation |

## Key tensions (what makes this skill non-obvious)

Some laws appear to contradict each other. Mastery is knowing which to apply:

- **1 vs 6** (don't outshine the master vs court attention): use 1 with your direct boss, 6 with the world.
- **3 vs 5** (conceal intentions vs guard reputation): conceal plans, show character.
- **22 vs 47** (use surrender tactic vs do not go past the target): 22 when you lost, 47 when you already won.
- **25 vs 38** (re-create yourself vs behave like others): 25 in life strategy, 38 in day-to-day execution.

Full detail in [`references/08-compendiums.md`](references/08-compendiums.md) → "Tensions" section.

## References

| Reference | Content |
|-----------|---------|
| [`references/00-glossary.md`](references/00-glossary.md) | Recurring vocabulary |
| [`references/01-categories.md`](references/01-categories.md) | The 6 thematic categories |
| [`references/02-laws-01-08.md`](references/02-laws-01-08.md) through [`07-laws-41-48.md`](references/07-laws-41-48.md) | The 48 laws in 6 blocks of 8 |
| [`references/08-compendiums.md`](references/08-compendiums.md) | One-line summary, category index, map of tensions |
| [`references/09-historical-figures.md`](references/09-historical-figures.md) | ~25 cited figures with brief bios |
| [`references/10-bibliography.md`](references/10-bibliography.md) | Greene + complementary works + courses |
| [`references/11-how-to-study.md`](references/11-how-to-study.md) | 4-level method + study rituals |

## Utility scripts

```bash
# Navigate the 48 laws
python3 scripts/list_laws.py | head -10

# Search by keyword
python3 scripts/search_by_category.py silence

# Validate structure (CI-friendly)
python3 scripts/validate_skill.py
```

## Common pitfalls

1. **Citing without ethical context.** Never say "apply Law 44" without flagging that it is defensive, not offensive. Always include the ethical level (defensive / applied-with-ethics / toxic).
2. **Recommending "toxic" use.** If the user wants to manipulate, redirect to professional help or say explicitly: "I can't help with that."
3. **Confusing law with prescription.** The laws **describe** how power operates; they do not ethically prescribe. Always distinguish description from prescription.
4. **Forgetting cultural context.** Greene uses antiquity and Renaissance examples. Literal application in 2026 may fail (e.g. Law 14 "pose as a friend, work as a spy" in low-context vs high-context cultures).
5. **Overestimating universality.** Some laws are specific to high-power contexts (court politics, monarchy). In modern everyday life, many apply in **attenuated** form.

## Verification checklist

Before answering with this skill, verify:

- Is the user's question within the scope of "power / strategy / ethics"?
- Did I identify the correct category (1–6)?
- Did I cite at least the **category** of the recommended law?
- Did I include the ethical level (defensive / applied-with-ethics / toxic) when relevant?
- Did I warn when the law is context-specific (politics, antiquity, etc.)?
- Did I recommend reading the full law in `references/` before acting?

## Anti-patterns (when NOT to give a recommendation)

- The user asks "how do I make X do what I want" without a legitimate context.
- The application implies harm to a vulnerable person (minor, emotionally dependent, in crisis).
- The law is purely defensive (recognizing the move) and the user wants to use it offensively.
- The user is in an active emotional crisis — refer to professional help first.

## Provenance

- Source compendium: [`ooovenenoso/48-leyes-del-poder`](https://github.com/ooovenenoso/48-leyes-del-poder) (also by Kevin Ramos Montañez).
- This skill distills the compendium into a Hermes-compatible shape. All 48 law bodies are original text from the source compendium (inspired by Robert Greene's 1998 book, not copied from it).
- License: MIT (matches source).
