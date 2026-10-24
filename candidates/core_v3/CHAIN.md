# Live chain — core v3

Human titles first; machine ids secondary. Snapshot of the live candidate set under `candidates/core_v3/`. Nothing here is in `entries/` until promoted. Scores pending the collider except A1.

Times are Pacific (America/Los_Angeles).

## Full live set

| # | Title | Id | Kind | Statement (one line) | Confidence | Cites |
|---|---|---|---|---|---|---|
| 1 | What "I" names | D-I | definition | "I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself. | (definition; unscored) | — |
| 2 | What exists | D-exist | definition | An activity exists at a time when it is going on at that time; lasting is going on existing (duration, E2D5). | (definition; unscored) | — |
| 3 | I exist | A1 | root | I exist. | **1.0** | — |
| 4 | A human body, and its mind | A2 | axiom, empirical | I am a human body made of cells, and my mind is that same body's organization described in the first person. | pending (collider); (b) declared unscored | A1 |
| 5 | Work, and the seven works | D-work | definition | A work helps keep an organization going; seven works named by test; "as one" by the take-apart test. | (definition; unscored) | — |
| 6 | Whole, degree, member, level, self-production, sameness | D-whole | definition | Grade each work 0/1/2; degree = lowest; whole if degree > 0; member; level; self-production; same whole later. | (definition; unscored) | — |
| 7 | The seven works sort things the way self-production does | A3 | axiom, model | Self-producing things perform all seven as one; non-producers fail at least one. | pending (collider) | — |
| 8 | Pattern by requirement | PR1 | principle | Same requirement → same work, forms differing by level. | explains; **adds no confidence** | — |
| 9 | Nature taken as one | D-Nature | definition | Everything that exists, taken together, with nothing besides it; not finite; in Nature ≠ member of. | (definition; unscored); God declared | — |
| 10 | The society I live in is a whole to a degree | A4 | axiom, model | The society I live in performs each of the seven works as one, at least in part, and I am one of its members. | pending (collider) | A2 |
| 11 | A whole at one level, a part at the next | P1 | proposition | I am a whole at one level and a part at the next. | pending (collider) | A2, A3, A4 |
| 12 | A collective mind happens | P2 | proposition | Control as one, with signaling and memory, happens in the society I live in; activity, not feeling. | pending (collider) | A4 |
| 13 | Every event is caused | A5 | axiom, model | Every event is caused, a choice included. | pending (collider) | — |
| 14 | Freedom, strict and by degree | D-free | definition | Strict: from own nature alone (Nature only, E1D7). Degree: from own organization and knowledge of causes. | (definition; unscored) | — |
| 15 | Freedom by degrees under necessity | P3 | proposition | Degree-freedom compatible with A5; freer from own organization and knowledge of causes; could-have-done-otherwise not required. | pending (collider) | A1, A2, A5 |
| 16 | Striving to persist | D-strive | definition | Continuing the works that keep an organization going; striving is those works, not a second force. | (definition; unscored) | — |
| 17 | Affect, and change of power | D-affect | definition | Affect = change in power of acting (= degree of the works) while striving, with ideas of that change. | (definition; unscored) | — |
| 18 | Bondage is acting from what is outside | P4 | proposition | Bondage rises as what the agent does follows from outside causes or unclearknown affects; inverse of D-free Def 15. | pending (collider) | A2, A5, P3 |
| 19 | Blessedness is the power itself | P5 | proposition | Blessedness is not a reward after freedom but power of acting as it rises with degree-freedom (E5P42 pattern). | pending (collider) | A2, A5, P3 |

## Caps (effective confidence)

| Entry | Cap rule |
|---|---|
| A1 | 1.0 |
| A2 | own score of clause (a); A1 caps nothing |
| A3 | own score (cites nothing) |
| PR1 | adds nothing |
| A4 | min(weakest row, A2) |
| P1 | min(A2, A3, A4) |
| P2 | min(A4 control/signaling/memory, A2 via A4) |
| A5 | own score (cites nothing) |
| D-* | definitions add nothing |
| P3 | min(A2, A5) |
| P4 | min(A2, A5, P3) |
| P5 | min(A2, A5, P3) |

## Groups

1. **The I** — #1–4 (seed + body/mind)
2. **Wholes** — #5–8
3. **Nature, society, levels** — #9–12
4. **Freedom under necessity** — #13–15
5. **Strive, affect, bondage, blessedness** — #16–19 (Spinoza Parts III–V ground, extended from this chain)

## Seed

*I exist* (A1), *What "I" names* (D-I), *What exists* (D-exist). Saved 2026-10-23 PT; pushed as `f52911c`.

## Related

- [README.md](README.md) — overview and mermaid
- [SPINOZA_GROUND.md](SPINOZA_GROUND.md) — Ethics map: covered vs gaps
- [PARKED.md](PARKED.md)
- [BUILD_LOG.md](BUILD_LOG.md)
- Dated note: [notes/2026-10-23-core-v3-chain-and-spinoza-ground.md](../../notes/2026-10-23-core-v3-chain-and-spinoza-ground.md)
