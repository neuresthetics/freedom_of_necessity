# Core v3 (candidate): restart from "I exist" alone

**Status: candidate only.** Nothing here is in `entries/`. Nothing here has been promoted. Core v2 stays untouched at [candidates/core_v2/](../core_v2/) and in `entries/` until the author says otherwise.

**Restart (2026-10-23 PT).** At the author's word: **I exist** is the only axiom now. Everything else on the old axiom and proposition list is retired from this chain and will be rebuilt. Definitions needed to ground that sentence's two words stay.

**Labels.** Each entry has a human title first. Machine ids (`A1`, `D-I`, `D-exist`) stay in front matter and filenames so the harness and later promotion keep a stable key. In tables below, read the title column; the id is secondary.

## The seed

These three entries are **the seed** of the restarted chain: one axiom, *I exist* (A1), and the two definitions that ground its words, *What "I" names* (D-I) and *What exists* (D-exist). Saved as the seed at the author's word (2026-10-23 PT). Everything rebuilt later grows from these three and cites back to them.

## Live chain (seed)

| # | Title | Id | Kind | Statement (one line) | Rests on |
|---|---|---|---|---|---|
| 1 | [What "I" names](D-I.md) | D-I | definition | "I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself. | (definition) |
| 2 | [What exists](D-exist.md) | D-exist | definition | An activity exists at a time when it is going on at that time; for anything else "exists" is taken as understood; a thing lasts when it goes on existing (duration, E2D5). | (definition) |
| 3 | [I exist](A1.md) | A1 | root, **1.0** | I exist. (In defined terms: this thinking is going on now, and so its thinker, if it has one distinct from it, exists now.) | nothing: doubting it is a case of it; uses What "I" names, What exists |

```mermaid
graph TD
  DI["What \"I\" names\n(D-I, definition)"]
  DE["What exists\n(D-exist, definition)"]
  A1["I exist\n(A1, root, 1.0)"]
  DI -.-> A1
  DE -.-> A1
```

## Rules for this restart

1. **Only axiom:** *I exist* (A1) at confidence 1.0.
2. **Definitions kept only to ground that sentence's terms:** *What "I" names* (D-I) and *What exists* (D-exist). They carry no confidence.
3. **Parked, not deleted:** the former A2–A4, PR1, P1, P2, D-work, D-whole, D-Nature, and the freedom candidates. See [PARKED.md](PARKED.md). The core v2 files and `entries/` copies are the archive.
4. **No rewrite of the root wording.** Surrounding text was trimmed of forward cites to the retired chain so this folder is coherent on its own.
5. **Not pushed** until the author says so. Local commit only.

## What this does not yet settle

*I exist* says that I exist and nothing about what I am. The next claim after it is open. Body, mind, Nature, wholes, society, freedom: all wait to be rebuilt, if they return at all.

## Logs

- [BUILD_LOG.md](BUILD_LOG.md) — this restart.
- [notes/2026-10-23-core-v3-restart.md](../../notes/2026-10-23-core-v3-restart.md) — dated note for the author.
