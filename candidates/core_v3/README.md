# Core v3 (candidate): restart from "I exist" alone

**Status: candidate only.** Nothing here is in `entries/`. Nothing here has been promoted. Core v2 stays untouched at [candidates/core_v2/](../core_v2/) and in `entries/` until the author says otherwise.

**Restart (2026-10-23 PT).** At the author's word: **I exist** is the only root axiom. The chain is rebuilt from the seed outward. Definitions needed to ground claims stay ahead of the claims that use them.

**Labels.** Each entry has a human title first. Machine ids stay in front matter and filenames. In tables below, read the title column; the id is secondary.

**Chain file.** Full table with confidence and cites: [CHAIN.md](CHAIN.md). Spinoza map: [SPINOZA_GROUND.md](SPINOZA_GROUND.md).

## The seed

*I exist* (A1), *What "I" names* (D-I), *What exists* (D-exist). Saved as the seed at the author's word (2026-10-23 PT); pushed as `f52911c`.

## Live chain

### Group 1 — the I

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 1 | [What "I" names](D-I.md) | D-I | definition | "I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself. | (definition) |
| 2 | [What exists](D-exist.md) | D-exist | definition | An activity exists at a time when it is going on at that time; for anything else "exists" is taken as understood; a thing lasts when it goes on existing (duration, E2D5). | (definition) |
| 3 | [I exist](A1.md) | A1 | root, **1.0** | I exist. | nothing: doubting it is a case of it; uses What "I" names, What exists |
| 4 | [A human body, and its mind](A2.md) | A2 | axiom, empirical, **pending** | I am a human body made of cells, and my mind is that same body's organization described in the first person. | A1 (subject; caps nothing) + own evidence for clause (a); identity and mind-as-organization declared, unscored |

### Group 2 — wholes

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 5 | [Work, and the seven works](D-work.md) | D-work | definition | A work helps keep an organization going and is carried out by structures that organization produces or maintains; seven works named by test questions; "as one" fixed by the take-apart test. | uses What exists |
| 6 | [Whole, degree, member, level, self-production, sameness](D-whole.md) | D-whole | definition | For finite things: grade each work 0/1/2; degree = lowest grade; whole if degree > 0; member; level; self-production (without the seven works); same whole later. | uses What exists, Work |
| 7 | [The seven works sort things the way self-production does](A3.md) | A3 | axiom, model, **pending** | Self-producing things perform all seven as one; things that last without producing themselves fail at least one. | anchors, controls, hard cases; uses Work, Whole |
| 8 | [Pattern by requirement](PR1.md) | PR1 | principle | Where the same requirement holds, the same work turns up, in forms that differ from level to level. | explains; **adds no confidence** |

### Group 3 — Nature, society, levels

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 9 | [Nature taken as one](D-Nature.md) | D-Nature | definition | Everything that exists, taken together, with nothing besides it; not finite; in Nature ≠ member of. | uses What exists, Whole (domain) |
| 10 | [The society I live in is a whole to a degree](A4.md) | A4 | axiom, model, **pending** | The society I live in performs each of the seven works as one, at least in part, and I am one of its members. | cites A2 (membership); graded one row at a time; PR1 explains, adds nothing |
| 11 | [A whole at one level, a part at the next](P1.md) | P1 | proposition, **pending** | I am a whole at one level and a part at the next. | cites A2, A3, A4; levels stop short of Nature |
| 12 | [A collective mind happens](P2.md) | P2 | proposition, **pending** | Control as one, with signaling and memory, happens in the society I live in; an activity, not a claim that the society feels. | cites A4 (three rows); A2 via A4 membership |

### Group 4 — Freedom under necessity

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 13 | [Every event is caused](A5.md) | A5 | axiom, model, **pending** | Every event is caused, a choice included. | model; weaker than E1P29; cites nothing |
| 14 | [Freedom, strict and by degree](D-free.md) | D-free | definition | Strict: exists and acts from own nature alone (Nature only, E1D7). Degree: from own organization and clear knowledge of causes. | (definition); could-have-done-otherwise not required |
| 15 | [Freedom by degrees under necessity](P3.md) | P3 | proposition, **pending** | Degree-freedom compatible with A5; freer from own organization and knowledge of causes. | cites A1, A2, A5; cap min(A2, A5) |

### Group 5 — Strive, affect, bondage, blessedness (Spinoza Parts III–V ground)

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 16 | [Striving to persist](D-strive.md) | D-strive | definition | Continuing the works that keep an organization going; striving is those works, not a second force. | restates E3P6–P7 pattern in work-language |
| 17 | [Affect, and change of power](D-affect.md) | D-affect | definition | Affect = change in power of acting (= degree of the works) while striving, with ideas of that change. | E3D3 pattern; active/passive via D-free |
| 18 | [Bondage is acting from what is outside](P4.md) | P4 | proposition, **pending** | Bondage rises as action follows outside causes or unclearknown affects; inverse of degree-freedom. | cites A2, A5, P3 |
| 19 | [Blessedness is the power itself](P5.md) | P5 | proposition, **pending** | Blessedness is not a reward after freedom but power of acting as it rises with degree-freedom. | cites A2, A5, P3; E5P42 pattern; amor Dei declared report |

```mermaid
graph TD
  DI["What \"I\" names\n(D-I)"]
  DE["What exists\n(D-exist)"]
  A1["I exist\n(A1, 1.0)"]
  A2["A human body, and its mind\n(A2, pending)"]
  DW["Work, and the seven works\n(D-work)"]
  DH["Whole...\n(D-whole)"]
  A3["Seven works ↔ self-production\n(A3, pending)"]
  PR1["Pattern by requirement\n(PR1, explains)"]
  DN["Nature taken as one\n(D-Nature)"]
  A4["Society is a whole to a degree\n(A4, pending)"]
  P1["Whole at one level, part at next\n(P1, pending)"]
  P2["A collective mind happens\n(P2, pending)"]
  A5["Every event is caused\n(A5, pending)"]
  DF["Freedom, strict and by degree\n(D-free)"]
  P3["Freedom by degrees under necessity\n(P3, pending)"]
  DS["Striving to persist\n(D-strive)"]
  DA["Affect, and change of power\n(D-affect)"]
  P4["Bondage is acting from what is outside\n(P4, pending)"]
  P5["Blessedness is the power itself\n(P5, pending)"]
  DI -.-> A1
  DE -.-> A1
  DI -.-> A2
  A1 --> A2
  DE -.-> DW
  DE -.-> DH
  DE -.-> DN
  DW -.-> DH
  DW -.-> A3
  DH -.-> A3
  DH -.-> DN
  PR1 -. explains .-> A3
  PR1 -. explains .-> A4
  A2 --> A4
  DW -.-> A4
  DH -.-> A4
  A2 --> P1
  A3 --> P1
  A4 --> P1
  DN -.-> P1
  A4 --> P2
  DW -.-> P2
  A5 --> P3
  A2 --> P3
  A1 --> P3
  DF -.-> P3
  DN -.-> DF
  DW -.-> DF
  DS -.-> DA
  DW -.-> DS
  DA -.-> P4
  DF -.-> P4
  A5 --> P4
  A2 --> P4
  P3 --> P4
  P3 --> P5
  A5 --> P5
  A2 --> P5
  DA -.-> P5
```

**Caps.** A1 = 1.0. A2 = clause (a) once scored (A1 caps nothing). A3 = own score once scored (cites nothing). PR1 adds nothing. A4 = min(weakest row, A2). P1 = min(A2, A3, A4). P2 = min(A4 control/signaling/memory rows, A2 via A4). A5 = own score. P3 = min(A2, A5). P4 = min(A2, A5, P3). P5 = min(A2, A5, P3). Definitions add nothing.

## Rules for this restart

1. **Root:** *I exist* (A1) at 1.0.
2. **One chain.** No split tracks. Declared readings stay inside their entries and are unscored.
3. **Scores pending** until the collider runs (except A1).
4. **Extend from this seed.** Spinoza's ground is covered by extending outward, not by copying the *Ethics* part-order as axioms.
5. **Not pushed** for rebuild steps after the seed unless the author says so.

## Kiln (2026-10-23 PT)

Fired for coherence against METHOD on Groups 1–2. Thesis wording unchanged. Scores still pending the collider (except A1). Details in [BUILD_LOG.md](BUILD_LOG.md).

## What this chain does not yet settle

- Why anything is felt (A2's limit; also open for the society in P2).
- Substance / attribute apparatus as scored claims (declared in D-Nature / A2 only).
- Three kinds of knowledge as their own entry (P3/P5 use clear knowledge of causes without the full ladder).
- Full emotion taxonomy; good/bad definitions; political right; eternity of mind.
- Promotion into `entries/` (needs a separate author OK).
- Freedom collider numbers (spec under `candidates/freedom/`; not rerun for this commit).

## Logs

- [CHAIN.md](CHAIN.md)
- [SPINOZA_GROUND.md](SPINOZA_GROUND.md)
- [BUILD_LOG.md](BUILD_LOG.md)
- [PARKED.md](PARKED.md)
- [notes/2026-10-23-core-v3-restart.md](../../notes/2026-10-23-core-v3-restart.md)
- [notes/2026-10-23-core-v3-chain-and-spinoza-ground.md](../../notes/2026-10-23-core-v3-chain-and-spinoza-ground.md)
