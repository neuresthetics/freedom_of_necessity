# Lens test v0.1 (2026-09-29)

The first test of the lens: does the five-step lens catch planted flaws better than a plain judge, without failing good entries? Short answer: it caught more, but it also failed 5 of 6 good entries, all because of bugs in the harness. See [LESSONS.md](LESSONS.md).

## Settings

- Model: `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`, served by Ollama. The Ollama digest was not recorded for this run.
- Temperature 0, seed 42 (arm 4 votes over seeds 42 to 45).
- Context 32K. Hardware: see [docs/HARDWARE.md](../../docs/HARDWARE.md).
- Lens hash: `5c61586e68e00aa76dc503628a10025299d8e9dd5c66ce35be647df32fb00c6c` (sha256 over the five lens prompt files; matched the expected hash).
- Book pinned at commit `69687ee` (`69687ee9b0997534d4388fc711b39d8e64aba29e`).
- Real entries: A2, A3, A4, D-whole, P1, PR1 (6). Broken twins: the 13 pairs in [lens_test/pairs/](../../lens_test/pairs/), 3 wordings each, so 39 broken wordings.
- Arms: 1 plain judge; 2 arm 1's reply plus code checks; 3 the lens plus code checks; 4 arm 1 voted over 4 seeds.

## Dates and calls

- Started 2026-09-28 15:40:35 PT, finished 2026-09-29 03:46:33 PT (12 h 06 min).
- Report written 2026-09-29 08:41 PT.
- 358 saved model calls: 326 in the main pass (arm 1: 45, arm 2: 0, arm 3: 146, arm 4: 180 including the 45 calls it shares with arm 1) plus 32 determinism reruns.

## Files

- `report.md`: the full report (pass bar, per-pair tables, real-entry scores, cost). One change from the original: a local folder path on line 5 was replaced with the repo name.
- `items.json`: full per-item records, unchanged.
- `spans_for_review.md` and `spans_for_review_part2.md`: each quoted span next to the model's step sentence, for a human to read. One file split in two at a section break to keep each under 600 lines; no text changed.
- `LESSONS.md`: what the run showed, why the headline result is mostly luck, the v0.2 fixes, and the lessons.

## Raw calls

The raw calls log (`calls.jsonl`, every request and reply) is not in this folder yet. It is on the test machine and will be added from there after it has been checked for local details.

The harness code and the lens prompt files will be published at MVP. See [docs/REPRODUCE.md](../../docs/REPRODUCE.md).

This folder is not edited after commit. Corrections go in later folders.
