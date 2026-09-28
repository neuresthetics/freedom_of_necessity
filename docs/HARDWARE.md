# Reproduction hardware

Results in this repo were produced on:

- CPU: AMD Ryzen 7 9700X (8 cores)
- RAM: 64 GB DDR5-6000, non-ECC
- GPU: NVIDIA RTX 4000 Ada 20 GB (ECC capable, off during runs to date), driver 580, CUDA 13.0
- OS: Ubuntu 24.04
- Model: Qwen3.8-27B q4_K_M via Ollama, 32K context, about 16 tok/s

## Footnote: memory errors

A minor note, not a central concern. The runs use non-ECC system memory and GPU ECC was off, so a random bit flip would go uncorrected. Using field rates from Schroeder, Pinheiro & Weber (2009), the chance that a flip silently alters a saved score on a given night is roughly one in a billion or less. Flips that crash a job or garble a reply show up as parse failures and are retried. Run-to-run variation of the model is a much larger source of error, and any surprising result should be rerun.
