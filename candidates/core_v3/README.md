# Core v3 (candidate): restart from "I exist" alone

**Status: candidate only.** Nothing here is in `entries/`. Nothing here has been promoted. Core v2 stays untouched at [candidates/core_v2/](../core_v2/) and in `entries/` until the author says otherwise.

**Restart (2026-10-23 PT).** At the author's word: **I exist** is the only axiom now. Everything else on the old axiom and proposition list is retired from this chain and will be rebuilt. Definitions needed to ground that sentence's two words stay.

**Labels.** Each entry has a human title first. Machine ids (`A1`, `A2`, `D-I`, `D-exist`) stay in front matter and filenames so the harness and later promotion keep a stable key. In tables below, read the title column; the id is secondary.

## The seed

These three entries are **the seed** of the restarted chain: one axiom, *I exist* (A1), and the two definitions that ground its words, *What "I" names* (D-I) and *What exists* (D-exist). Saved as the seed at the author's word (2026-10-23 PT). Everything rebuilt later grows from these three and cites back to them.

## Live chain

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 1 | [What "I" names](D-I.md) | D-I | definition | "I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself. | (definition) |
| 2 | [What exists](D-exist.md) | D-exist | definition | An activity exists at a time when it is going on at that time; for anything else "exists" is taken as understood; a thing lasts when it goes on existing (duration, E2D5). | (definition) |
| 3 | [I exist](A1.md) | A1 | root, **1.0** | I exist. (In defined terms: this thinking is going on now, and so its thinker, if it has one distinct from it, exists now.) | nothing: doubting it is a case of it; uses What "I" names, What exists |
| 4 | [A human body, and its mind](A2.md) | A2 | axiom, empirical, **pending** | I am a human body made of cells, and my mind is that same body's organization described in the first person. | A1 (subject; caps nothing) + own evidence for clause (a); identity and mind-as-organization are a declared reading, unscored |

```mermaid
graph TD
  DI["What \"I\" names\n(D-I, definition)"]
  DE["What exists\n(D-exist, definition)"]
  A1["I exist\n(A1, root, 1.0)"]
  A2["A human body, and its mind\n(A2, empirical, pending)"]
  DI -.-> A1
  DE -.-> A1
  DI -.-> A2
  A1 --> A2
```

**Caps.** A1 = 1.0. A2 cites A1 (caps nothing); effective confidence = score of clause (a) once the collider runs. Clause (b) adds none.

## Rules for this restart

1. **Root axiom:** *I exist* (A1) at confidence 1.0. It is the only self-evident entry.
2. **Seed definitions:** *What "I" names* (D-I) and *What exists* (D-exist). They carry no confidence.
3. **Next after the seed:** *A human body, and its mind* (A2). Body/mind before Nature, wholes, or society, because A1's open question is what this I is, and Nature needs more than one body.
4. **Parked, not deleted:** the former A3, A4, PR1, P1, P2, D-work, D-whole, D-Nature, and the freedom candidates. See [PARKED.md](PARKED.md). A2's archive copies in core_v2 and `entries/` stay as record; the live rewrite is this folder's A2.md.
5. **No rewrite of the root wording.** A1's sentence stays "I exist."
6. **Not pushed** until the author says so. Local commit only for rebuild steps after the seed push.

## What this does not yet settle

- Why anything is felt (A2's stated limit).
- Sameness of the I over time (not claimed in A2).
- Nature, wholes, society, freedom (still parked).
- Whether clause (b) holds for a digital intelligence (A2 Scholium 1).

## Open forks (for the author)

See A2, Scholium 2: pull out definitions of organization / mind / first person; keep (a) and (b) in one entry (default); score now or leave pending (default: pending).

## Logs

- [BUILD_LOG.md](BUILD_LOG.md) — this restart and each growth step.
- [notes/2026-10-23-core-v3-restart.md](../../notes/2026-10-23-core-v3-restart.md) — dated note for the author.
