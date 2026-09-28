# Freedom of Necessity

**Working title:** Freedom of Necessity: God, Brain, and the Order of the Mind

A geometric, Ethics-style axiomatic book, with a harness that checks each entry against its citations. This repo is public so anyone can read the book and verify the checks.

## What belongs here

- The book entries (definitions, axioms, propositions)
- The harness that runs the checks
- Model and hardware specs needed to reproduce a run (model name and quant, context length, KV cache, approximate VRAM, generation speed class)

## What does not belong here

Personal machine setup, paths, network, security, or home-lab notes. Those live in a separate private repo. The harness code lives here; personal run configs stay out of this repo.

## Status

Scaffolding. Entries and harness not yet committed.

## Reproduce (placeholder)

Will list:

- Model: `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`
- Context: 32K, flash attention on
- KV cache: q8_0
- GPU: ~20 GB VRAM class
- Speed: ~16–17 tok/s on that class

Details will be filled in when the harness lands.
