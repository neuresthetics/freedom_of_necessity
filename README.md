# Freedom of Necessity

**Working title:** Freedom of Necessity: God, Brain, and the Order of the Mind

A geometric, Ethics-style axiomatic book, with a harness that checks each entry against its citations. This repo is public so anyone can read the book and verify the checks.

## Read this first: the current rough draft

If you only skim one thing, skim [*Axioms of Necessity*, v11](drafts/verses/axioms_of_necessity_v11.md). It's the verse companion: the whole book in 162 short verses, from "There is one order, and it has no outside" to Spinoza's last line. It's a rough draft, readable in one sitting, and you can open it at any page. The axioms underneath it are in [candidates/core_v2/](candidates/core_v2/README.md).

This draft is frozen as the tag [`keeper-2026-10-01`](https://github.com/neuresthetics/freedom_of_necessity/tree/keeper-2026-10-01), so it can still be read exactly as it was after later revisions.

## Where to start

- [HOW_THIS_BOOK_IS_BUILT.md](HOW_THIS_BOOK_IS_BUILT.md): read first. What each kind of entry is, how derivations work, and where the method departs from Spinoza.
- [candidates/core_v2/](candidates/core_v2/README.md): a candidate rebuild of the core, starting from "I exist", with "human" moved into A2. Not yet promoted; `entries/` is unchanged until the author decides.
- [drafts/verses/](drafts/verses/): the verse companion, *Axioms of Necessity* (latest [v11](drafts/verses/axioms_of_necessity_v11.md); changes in [v11_changes.md](drafts/verses/v11_changes.md)). Unscored and not part of `entries/`.
- [LOG.md](LOG.md): dated record of tests and changes, newest first.
- [results/](results/): one folder per test run, with its settings, report and lessons. Never edited after commit.
- [docs/](docs/): [hardware](docs/HARDWARE.md), [model choice](docs/MODEL_CHOICE.md), and [how to reproduce a run](docs/REPRODUCE.md).

## What belongs here

- The book entries (definitions, axioms, propositions)
- The harness that runs the checks
- Model and hardware specs needed to reproduce a run (model name and quant, context length, KV cache, approximate VRAM, generation speed class)

## What does not belong here

Personal machine setup, paths, network, security, or home-lab notes. The harness code lives here; personal run configs stay out of this repo.

## Status: working seed

The seed entries below are the committed working base in `entries/`. They can still be edited. A candidate replacement for the core is being worked out in [candidates/core_v2/](candidates/core_v2/README.md); until it is promoted, the entries below are the ones in force.

### Seed entries

- **A1**: "I, a human, exist." The root.
- **A2**: I am a body made of cells, and their organization produces my mind. Empirical; cites nothing; its evidence is in its own text.
- **A3**: Society shows organism-level properties across seven rows (boundary, control, energy, transport, signaling, defense, memory) at three levels: cell, person, society. Each row has its own evidence.
- **A4**: I function in society as a unit analogous to a cell.
- **P1**: A collective mind happens in society: integration, decision, and memory emerge from feedback among its members and work as one system. A process, not a thing, and explicitly not a claim that society is conscious.

### How checking works

A local open-weights model judges each entry against the entries it cites, or, if it cites nothing, against its own evidence. A3 is scored row by row, and its score is its weakest row. An entry can be no more confident than its weakest support, all the way down the chain.

Full rules: [METHOD.md](METHOD.md). Confidences are a ranking with a cap chain, not probabilities.

### Scores: none valid right now

Every entry except A1 is **unscored**. The earlier numbers (A2 0.80; A3 0.50; A4 and P1 0.72, capped at 0.50 by A3) came from the first check and the five-step lens, which has been retired after an outside review found problems in the run (see [LOG.md](LOG.md), 2026-09-29, "Back to the drawing board"). They are kept in [results/](results/) as history, not as results. New scores will be recorded only after the collider below has run.

### Next phase

A minimal collider replaces the lens: for each entry the model builds a steel man of the entry and the strongest counter steel man, both in the book's geometric form, and judges them side by side. Code checks citations and quoted spans; the model does not check its own citations. Planned runs: a clean control and the collider, each on the uncensored and the stock model, on the same entries and broken twins.

### Reproducibility

Model: Qwen3.8-27B, q4_K_M, served by Ollama on an NVIDIA RTX 4000 Ada (20 GB).

## Reproduce (placeholder)

Will list:

- Model: `Qwen3.8-27B, q4_K_M, via Ollama`
- Context: 32K, flash attention on
- KV cache: q8_0
- GPU: NVIDIA RTX 4000 Ada (20 GB)
- Speed: ~16–17 tok/s

Details will be filled in when the harness lands.
