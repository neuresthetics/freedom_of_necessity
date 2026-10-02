# Freedom of Necessity

*God, Brain, and the Order of the Mind*

<br>

> There is one order, and it has no outside. Whatever is, is in it. Call it God, or Nature.
>
> — *Axioms of Necessity*, verse 1

<br>

This is a book written in Spinoza's geometric manner: definitions, axioms and propositions, each standing on the ones before it. Its subject is a pantheism in modern terms: there is one order of things, called God or Nature, and the brain and its society belong to it. Freedom, as the book follows Spinoza in understanding it, is acting from knowledge of necessity rather than escaping it.

The working title is *Freedom of Necessity: God, Brain, and the Order of the Mind*. The repo is public so that anyone can read the book and check the work behind it.

---

## Start here

**1. The rough draft.** [*Axioms of Necessity*, v11](drafts/verses/axioms_of_necessity_v11.md) is the verse companion: the whole book in 162 short verses, from "There is one order, and it has no outside" to Spinoza's last line. It is a rough draft, readable in one sitting, and you can open it anywhere. This draft is frozen as the tag [`keeper-2026-10-01`](https://github.com/neuresthetics/freedom_of_necessity/tree/keeper-2026-10-01), so it can still be read exactly as it was after later revisions. Changes from v10 are in [v11_changes.md](drafts/verses/v11_changes.md).

**2. How the book is built.** [HOW_THIS_BOOK_IS_BUILT.md](HOW_THIS_BOOK_IS_BUILT.md) says what each kind of entry is, how derivations work, and where the method departs from Spinoza.

**3. The axioms underneath.** [candidates/core_v2/](candidates/core_v2/README.md) is a candidate rebuild of the core, starting from "I exist", with "human" moved into A2. It is not yet promoted.

<br>

## The arc

The book begins with an I that exists, and only that is beyond revision. It then finds, on evidence, that this I is a human body made of cells. It shows that such a body is a whole, doing the works of lasting as one. And it finds that this whole is also a member of something larger, a society that is itself a whole to a degree. Freedom, Nature and the collective mind are worked out from there.

---

## Status

**Working seed.** The entries in [`entries/`](entries/) are the committed working base, and they are the ones in force. They can still be edited. The candidate core in [candidates/core_v2/](candidates/core_v2/README.md) replaces them only if the author promotes it; until then `entries/` is unchanged. The verse companion in [drafts/verses/](drafts/verses/) is unscored and not part of `entries/`.

| Entry | Claim | Note |
|---|---|---|
| **A1** | "I, a human, exist." | The root. |
| **A2** | I am a body made of cells, and their organization produces my mind. | Empirical; cites nothing; its evidence is in its own text. |
| **A3** | Society shows organism-level properties across seven rows (boundary, control, energy, transport, signaling, defense, memory) at three levels: cell, person, society. | Each row has its own evidence. |
| **A4** | I function in society as a unit analogous to a cell. | |
| **P1** | A collective mind happens in society: integration, decision, and memory emerge from feedback among its members and work as one system. | A process, not a thing, and explicitly not a claim that society is conscious. |

<br>

### How checking works

A local open-weights model judges each entry against the entries it cites, or, if it cites nothing, against its own evidence. A3 is scored row by row, and its score is its weakest row. An entry can be no more confident than its weakest support, all the way down the chain.

Full rules: [METHOD.md](METHOD.md). Confidences are a ranking with a cap chain, not probabilities.

### Scores: none valid right now

Every entry except A1 is **unscored**. The earlier numbers (A2 0.80; A3 0.50; A4 and P1 0.72, capped at 0.50 by A3) came from the first check and the five-step lens, which has been retired after an outside review found problems in the run (see [LOG.md](LOG.md), 2026-09-29, "Back to the drawing board"). They are kept in [results/](results/) as history, not as results. New scores will be recorded only after the collider below has run.

### Next: the collider

A minimal collider replaces the lens. For each entry, the model builds a steel man of the entry and the strongest counter steel man, both in the book's geometric form, and judges them side by side. Code checks citations and quoted spans; the model does not check its own citations. Planned runs: a clean control and the collider, each on the uncensored and the stock model, on the same entries and broken twins.

---

## For readers checking the work

**Records.**

- [LOG.md](LOG.md): dated record of tests and changes, newest first.
- [results/](results/): one folder per test run, with its settings, report and lessons. Never edited after commit.
- [docs/](docs/): [hardware](docs/HARDWARE.md), [model choice](docs/MODEL_CHOICE.md), and [how to reproduce a run](docs/REPRODUCE.md).

**What belongs here.** The book entries (definitions, axioms, propositions); the harness that runs the checks; and the model and hardware specs needed to reproduce a run (model name and quant, context length, KV cache, approximate VRAM, generation speed class).

**What does not.** Personal machine setup, paths, network, security, or home-lab notes. The harness code lives here; personal run configs stay out of this repo.

**Reproduce (placeholder).** Model: Qwen3.8-27B, q4_K_M, served by Ollama on an NVIDIA RTX 4000 Ada (20 GB). A full recipe will list:

- Model: `Qwen3.8-27B, q4_K_M, via Ollama`
- Context: 32K, flash attention on
- KV cache: q8_0
- GPU: NVIDIA RTX 4000 Ada (20 GB)
- Speed: ~16–17 tok/s

Details will be filled in when the harness lands.

<br>

[MIT License](LICENSE)
