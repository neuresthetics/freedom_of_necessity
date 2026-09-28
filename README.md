# Freedom of Necessity

**Working title:** Freedom of Necessity: God, Brain, and the Order of the Mind

A geometric, Ethics-style axiomatic book, with a harness that checks each entry against its citations. This repo is public so anyone can read the book and verify the checks.

## What belongs here

- The book entries (definitions, axioms, propositions)
- The harness that runs the checks
- Model and hardware specs needed to reproduce a run (model name and quant, context length, KV cache, approximate VRAM, generation speed class)

## What does not belong here

Personal machine setup, paths, network, security, or home-lab notes. Those live in a separate private repo. The harness code lives here; personal run configs stay out of this repo.

## Status: working seed

The seed entries below are the stable working base. They can still be edited.

### Seed entries

- **A1**: "I, a human, exist." The root.
- **A2**: I am a body made of cells, and their organization produces my mind. Empirical; cites nothing; its evidence is in its own text.
- **A3**: Society shows organism-level properties across seven rows (boundary, control, energy, transport, signaling, defense, memory) at three levels: cell, person, society. Each row has its own evidence.
- **A4**: I function in society as a unit analogous to a cell.
- **P1**: Society has a functional collective mind: it integrates information, decides, and remembers as one system. This is explicitly not a claim that society is conscious.

### How checking works

A local open-weights model judges each entry against the entries it cites, or, if it cites nothing, against its own evidence. A3 is scored row by row, and its score is its weakest row. An entry can be no more confident than its weakest support, all the way down the chain.

### Results so far

- **A2**: evidence check 0.80.
- **A3**: 0.50. Six rows score 0.80; defense is unclear at 0.50 because the backbone source (Miller, *Living Systems*, 1978) has no defense subsystem. A revision with added defense sources is pending.
- **A4**: passes, 0.72.
- **P1**: passes with a model score of 0.72, but its effective confidence is capped at 0.50 by A3.

### Next phase

A lens applied to every check, being designed now. The checking code will be published here when it reaches MVP.

### Reproducibility

Model: Qwen3.8-27B, q4_K_M, served by Ollama on an NVIDIA RTX 4000 Ada (20 GB).

## Reproduce (placeholder)

Will list:

- Model: `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`
- Context: 32K, flash attention on
- KV cache: q8_0
- GPU: ~20 GB VRAM class
- Speed: ~16–17 tok/s on that class

Details will be filled in when the harness lands.
