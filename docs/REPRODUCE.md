# Reproducing a test

Each folder in [results/](../results/) records what is needed to rerun its test. This page
says what those pieces are and where to find them.

**The harness code is not public yet.** It will be released here at MVP, along with the lens
prompt files. Until then you can check the inputs and the recorded outputs, but not rerun
the harness yourself.

## What pins a run

- **Model.** Name and quantization as served by Ollama. For lens test v0.1:
  `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`. Its Ollama digest was not recorded for that
  run; later runs will record it. The stock model planned for comparison is
  `qwen3.8:27b-q4_K_M` (digest `25b843619e94`).
- **Settings.** Temperature 0, seed 42, 32K context. Any extra seeds are listed in the run's
  README (v0.1's arm 4 used seeds 42 to 45).
- **Book commit.** The entries are read from a pinned commit of this repo, not from the
  working tree. For v0.1: `69687ee` (`69687ee9b0997534d4388fc711b39d8e64aba29e`). To see the
  exact text that was judged: `git show 69687ee:entries/A3.md`.
- **Lens hash.** A sha256 over the lens prompt files. For v0.1:
  `5c61586e68e00aa76dc503628a10025299d8e9dd5c66ce35be647df32fb00c6c`. When the prompt files
  are published, a rerun should check this hash before it starts.
- **Broken twins.** The pairs in [lens_test/pairs/](../lens_test/pairs/). Each pair has a
  `pair.yaml` naming the planted flaw and three wordings, `broken_1.md` to `broken_3.md`.
- **Hardware.** See [HARDWARE.md](HARDWARE.md). Different hardware can change results
  slightly even at temperature 0.

## What to compare

- `report.md` in the results folder: catches per twin, real-entry verdicts, and cost.
- `items.json`: the full per-item records.
- The raw calls log, once it is added to the folder (see its README).

A rerun with the same model, settings, book commit, lens hash and pairs should give the same
verdicts. In v0.1, identical reruns of 4 items per arm gave 0 flips. If yours differ, please
open an issue with your hardware and Ollama version.
