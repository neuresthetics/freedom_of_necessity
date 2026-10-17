![Inside a lattice of hairline edges and nodes that arches overhead toward one bright root node](assets/banner.jpg)

# Freedom of Necessity

*God, Brain, and the Order of the Mind*

<br>

> There is one order, and it has no outside. Whatever is, is in it. Call it God, or Nature.
>
> — *Axioms of Necessity*, verse 53

<br>

This is a book written in Spinoza's geometric manner: definitions, axioms and propositions, each standing on the ones before it. Its subject is a pantheism in modern terms: there is one order of things, called God or Nature, and the brain and its society belong to it. Freedom, as the book follows Spinoza in understanding it, is acting from knowledge of necessity rather than escaping it.

The working title is *Freedom of Necessity: God, Brain, and the Order of the Mind*. The repo is public so that anyone can read the book and check the work behind it.

---

## Start here

**0. The preface.** [On a Book Without Its Original](PREFACE.md): why there is no original *Ethics*, who holds the surviving copy, and where this book goes further than Spinoza, above all on freedom.

**1. The rough draft.** [*Axioms of Necessity*, v12](drafts/verses/axioms_of_necessity_v12.md) is the verse companion and the current rough draft: the whole book in 174 short verses in 18 chapters, derived fresh from core v2 and following its order. It is unscored, readable in one sitting, and you can open it anywhere. What changed from v11 is in [v12_changes.md](drafts/verses/v12_changes.md). The six coherence checks and the final check of the revised text are in [drafts/verses/](drafts/verses/) ([1](drafts/verses/v12_coherence_check.md), [2](drafts/verses/v12_coherence_check_2.md), [3](drafts/verses/v12_coherence_check_3.md), [4](drafts/verses/v12_coherence_check_4.md), [5](drafts/verses/v12_coherence_check_5.md), [6](drafts/verses/v12_coherence_check_6.md), [final](drafts/verses/v12_final_check.md)). How the field of consciousness theories maps onto the book so far is in [v12_consciousness_landscape.md](drafts/verses/v12_consciousness_landscape.md).

The previous draft, [v11](drafts/verses/axioms_of_necessity_v11.md) (162 verses), is frozen as the tag [`keeper-2026-10-01`](https://github.com/neuresthetics/freedom_of_necessity/tree/keeper-2026-10-01), so it can still be read exactly as it was.

**2. How the book is built.** [HOW_THIS_BOOK_IS_BUILT.md](HOW_THIS_BOOK_IS_BUILT.md) says what each kind of entry is, how derivations work, and where the method departs from Spinoza.

**3. The axioms underneath.** [`entries/`](entries/) holds the core in force: twelve definitions, axioms and propositions, starting from "I exist", with "human" in A2. It is core v2, promoted on 2026-10-15; how it was built (collisions, audits, proposals) is kept in [candidates/core_v2/](candidates/core_v2/README.md).

<br>

## The arc

The book begins with an I that exists, and only that is beyond revision. It then finds, on evidence, that this I is a human body made of cells. It shows that such a body is a whole, doing the works of lasting as one. And it finds that this whole is also a member of something larger, a society that is itself a whole to a degree. Freedom, Nature and the collective mind are worked out from there.

---

## Status

**Working seed.** The entries in [`entries/`](entries/) are the committed working base, and they are the ones in force. They can still be edited. They are core v2, promoted from [candidates/core_v2/](candidates/core_v2/README.md) on 2026-10-15; the earlier core is kept in [history/entries_v1/](history/entries_v1/README.md) and frozen by the keeper tag. The verse companion in [drafts/verses/](drafts/verses/) is unscored and not part of `entries/`.

| # | Entry | Claim | Note |
|---|---|---|---|
| 1 | **D-I** | "I" names the thinker of a thought, if there is one distinct from the thinking, and otherwise the thinking itself. | Definition. |
| 2 | **D-exist** | An activity exists when it is going on; a thing lasts when it goes on existing. Whether anything exists eternally is left open. | Definition. |
| 3 | **A1** | "I exist." | The root, 1.0: doubting it is a case of it. |
| 4 | **A2** | I am made of a human body made of cells, and go with that body; my mind is that body's organization described in the first person. | Empirical; cites A1. Scored as: made of this body, and this thinking goes with it. That I am this body, and the mind clause, are a declared reading. |
| 5 | **D-work** | A work keeps a thing's organization going and is carried out by structures that organization makes or maintains. Seven works: four general (boundary, energy, control, memory) and three conditional (transport, signaling, defense), each needed where its stated condition holds. | Definition. |
| 6 | **D-whole** | Each work that applies is graded 0, 1 or 2, and a thing is only as whole as its lowest grade. A member shares the whole's fate and takes part in its works. | Definition; finite things only. |
| 7 | **D-Nature** | Nature is everything that exists, taken together, with nothing outside it. | Definition; not graded. Calling it God is a declared reading. |
| 8 | **A3** | The seven works sort things the way self-production does, wherever self-production can be checked. | Model axiom. |
| 9 | **PR1** | Where the same requirement holds, the same work turns up, in different forms at each level. | Explains; adds no confidence. |
| 10 | **A4** | The society I live in is a whole to a degree, judged one work at a time, and I am one of its members. | Model axiom; capped by its weakest row and by A2. |
| 11 | **P1** | I am a whole at one level and a part at the next. | Derived from A2, A3, A4. |
| 12 | **P2** | A collective mind happens in the society: control performed as one, through signaling and memory. | Derived from A4. An activity, not a thing, and not a claim that society feels. |

<br>

### How checking works

The book is written and checked with Grok. Each entry is judged against the entries it cites, or, if it cites nothing, against its own evidence. A4 is judged row by row, and it stands no higher than its weakest row. An entry can be no more confident than its weakest support, all the way down the chain.

Full rules: [METHOD.md](METHOD.md). Confidences, once there are any, are a ranking with a cap chain, not probabilities.

### Scores: none valid right now

Every entry except A1 is **unscored**. The earlier numbers, for the old core now in [history/entries_v1/](history/entries_v1/README.md) and its own numbering (A2 0.80; A3 0.50; A4 and P1 0.72, capped at 0.50 by A3) came from the first check and the five-step lens, which has been retired after an outside review found problems in the run (see [LOG.md](LOG.md), 2026-09-29, "Back to the drawing board"). They are kept in [results/](results/) as history, not as results. New scores will be recorded only after the collider below has run.

### Next: the collider

A minimal collider replaces the lens. For each entry, the checker builds a steel man of the entry and the strongest counter steel man, both in the book's geometric form, and judges them side by side. Code checks citations and quoted spans; the checker does not check its own citations. Planned runs: a clean control and the collider, on the same entries and broken twins. There are no harness scores yet.

---

## For readers checking the work

**Records.**

- [LOG.md](LOG.md): dated record of tests and changes, newest first.
- [results/](results/): one folder per test run, with its settings, report and lessons. Never edited after commit.
- [docs/](docs/): earlier notes on hardware, model choice and reproducing a run, kept as history.

**What belongs here.** The book entries (definitions, axioms, propositions), the verse drafts, the checks run on them, and the harness once it lands.

**What does not.** Personal machine setup, paths, network, security, or home-lab notes.

<br>

[MIT License](LICENSE)
