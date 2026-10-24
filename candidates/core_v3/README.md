# Core v3 (candidate): restart from "I exist" alone

**Status: candidate only.** Nothing here is in `entries/`. Nothing here has been promoted. Core v2 stays untouched at [candidates/core_v2/](../core_v2/) and in `entries/` until the author says otherwise.

**Restart (2026-10-23 PT).** At the author's word: **I exist** is the only root axiom. The chain is rebuilt from the seed outward. Definitions needed to ground claims stay ahead of the claims that use them.

**Labels.** Each entry has a human title first. Machine ids stay in front matter and filenames. In tables below, read the title column; the id is secondary.

## The seed

*I exist* (A1), *What "I" names* (D-I), *What exists* (D-exist). Saved as the seed at the author's word (2026-10-23 PT).

## Live chain

### Group 1 — the I

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 1 | [What "I" names](D-I.md) | D-I | definition | "I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself. | (definition) |
| 2 | [What exists](D-exist.md) | D-exist | definition | An activity exists at a time when it is going on at that time; for anything else "exists" is taken as understood; a thing lasts when it goes on existing (duration, E2D5). | (definition) |
| 3 | [I exist](A1.md) | A1 | root, **1.0** | I exist. | nothing: doubting it is a case of it; uses What "I" names, What exists |
| 4 | [A human body, and its mind](A2.md) | A2 | axiom, empirical, **pending** | I am a human body made of cells, and my mind is that same body's organization described in the first person. | A1 (subject; caps nothing) + own evidence for clause (a); identity and mind-as-organization declared, unscored |

### Group 2 — wholes (this block)

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 5 | [Work, and the seven works](D-work.md) | D-work | definition | A work helps keep an organization going and is carried out by structures that organization produces or maintains; seven works named by test questions; "as one" fixed by the take-apart test. | uses What exists |
| 6 | [Whole, degree, member, level, self-production, sameness](D-whole.md) | D-whole | definition | For finite things: grade each work 0/1/2; degree = lowest grade; whole if degree > 0; member; level; self-production (without the seven works); same whole later. | uses What exists, Work |
| 7 | [The seven works sort things the way self-production does](A3.md) | A3 | axiom, model, **pending** | Self-producing things perform all seven as one; things that last without producing themselves fail at least one. | anchors, controls, hard cases; uses Work, Whole |
| 8 | [Pattern by requirement](PR1.md) | PR1 | principle | Where the same requirement holds, the same work turns up, in forms that differ from level to level. | explains; **adds no confidence** |

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
  DI -.-> A1
  DE -.-> A1
  DI -.-> A2
  A1 --> A2
  DE -.-> DW
  DE -.-> DH
  DW -.-> DH
  DW -.-> A3
  DH -.-> A3
  PR1 -. explains .-> A3
```

**Caps.** A1 = 1.0. A2 = clause (a) once scored (A1 caps nothing). A3 = own score once scored (cites nothing). PR1 adds nothing.

## Rules for this restart

1. **Root:** *I exist* (A1) at 1.0.
2. **One chain.** No split tracks. Declared readings stay inside their entries and are unscored.
3. **Scores pending** until the collider runs (except A1).
4. **Parked for later blocks:** D-Nature, A4, P1, P2, freedom candidates. See [PARKED.md](PARKED.md).
5. **Not pushed** for rebuild steps after the seed unless the author says so.

## Kiln (2026-10-23 PT)

Fired for coherence against METHOD: stale forward claims removed, organization sense fixed in A2 then adopted by D-work, A3's multicellular self-production named as a declared reading, frontmatter `scored_as` on every definition. Thesis wording unchanged. Scores still pending the collider (except A1). Details in [BUILD_LOG.md](BUILD_LOG.md).

## What this block does not yet settle

- Nature taken as one (outside D-whole's finite domain; definition not live yet).
- Whether my society is a whole (needs its own axiom).
- Whole at one level / part at the next (needs society + demonstration).
- Freedom under necessity (candidates still under `candidates/freedom/`).
- Why anything is felt (A2's limit).

## Logs

- [BUILD_LOG.md](BUILD_LOG.md)
- [notes/2026-10-23-core-v3-restart.md](../../notes/2026-10-23-core-v3-restart.md)
