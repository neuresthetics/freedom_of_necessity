# Freedom collider harness

Runs the freedom collision (candidates A5, D-free, P3) with **enforced separation**: each side and each judge is a separate, stateless model call that sees only what its role is allowed to see. It reuses the saved prompts, rubric and controls from [`candidates/freedom/run_2026-10-18/`](../../candidates/freedom/run_2026-10-18/RUN_SPEC.md), which was a hand-written, procedurally separated run.

Python 3 standard library only. No packages to install.

## What each call sees

| Call | Role in config | Sees |
|---|---|---|
| side_L, side_H, side_B | `side_L`, `side_H`, `side_B` | its own saved prompt file, verbatim, plus the frozen texts of A5.md, D-free.md and P3.md |
| control_bad_B | `control_bad_B` | the same, for the deliberately bad entry |
| judge_main | `judge` | the question, the frozen entries, each side's thesis and falsifier, the three side outputs, and the rubric |
| judge_control | `judge` | the bad entry's thesis, falsifier and output alone (labeled C), and the rubric |
| judge_swap | `judge_swap` | the judge_main input with labels hidden (X/Y/Z per `swap_map.txt`), reordered, with author names removed from headers |

No call sees the 2026-10-18 `raw/` or `judge/` files or the 2026-10-17 collision. Each request is a fresh HTTP request with a system message and one user message, and no earlier turns.

Use a **different model for the judge than for the sides**, ideally from a different model family. RUN_SPEC.md and RESULT.md both warn you if the judge model is the same as a side model.

## Files

- `run_collider.py`: the single entry point.
- `rubric_parser.py`: a strict parser for the judge's `BEGIN_VERDICT … END_VERDICT` block. It accepts only the five rubric values (0.85, 0.70, 0.50, 0.25, 0.10) and the three verdicts. Anything else is recorded as **unparsed**, and nothing is guessed from prose.
- `test_rubric_parser.py`: unit tests for the parser.
- `templates/`: the system messages, the judge rubric and the judge layouts. They are hashed into each run's INPUTS.sha256.
- `collider.config.example.json`: copy it to `collider.config.json`, which git ignores.

## Config

- `backends`: `ollama` (uses `/api/chat`), or `openai` for any OpenAI-compatible `/chat/completions` endpoint. The OpenAI-compatible backend reads its key from the environment variable named in `api_key_env`. The script refuses to run if a config file contains an `api_key`.
- `roles`: one entry per role, each with `backend` and `model`, plus optional `temperature`, `num_ctx`, `max_tokens`, `timeout_s`, `retries`, and `options` (extra Ollama options or request fields).
- `seed_base`: run *i* uses `seed_base + 100*i`, and each call within a run adds a fixed offset.
- `gpu`: if `nvidia-smi` exists, the script pauses before each call while the hottest GPU is above `max_temp_c` (default 83), until it cools to `resume_temp_c`.
- Sides need a temperature above 0, or repeated runs will repeat the same answer. RESULT.md flags side outputs that come back byte-identical across seeds.

Hosts, URLs and keys are never written into run outputs. Request files hold the payload only.

## Steps on the tower

Run these from the repository root.

1. Get the latest code.

```bash
git pull
```

2. Make your local config.

```bash
cp harness/collider/collider.config.example.json harness/collider/collider.config.json
```

3. Set the model names for each role: replace `SIDE_MODEL_NAME` and `JUDGE_MODEL_NAME`, and delete the `remote` backend if you don't use one.

```bash
nano harness/collider/collider.config.json
```

4. Check the exact Ollama model names to put in the config.

```bash
ollama list
```

5. If any role uses an OpenAI-compatible endpoint, enter its key for this shell only. It isn't echoed, and it isn't saved to a file.

```bash
read -rs COLLIDER_API_KEY && export COLLIDER_API_KEY
```

6. Run the parser tests.

```bash
python3 -m unittest discover -s harness/collider -p 'test_*.py' -v
```

7. Do a dry run. It builds and saves every payload without calling a model. The output goes to `harness/collider/_dryrun/`, which git ignores.

```bash
python3 harness/collider/run_collider.py --dry-run --runs 5
```

8. Start a tmux session, so the run survives a closed terminal.

```bash
tmux new -s collider
```

9. Write the run spec before any model call. This example uses 5 runs, each with its own seed. The script prints the new directory and the commit command.

```bash
python3 harness/collider/run_collider.py --spec-only --runs 5
```

10. Commit the spec before any output exists. Use the exact command the script printed. It has this shape:

```bash
git add candidates/freedom/run_YYYY-MM-DD_HHMM/RUN_SPEC.md candidates/freedom/run_YYYY-MM-DD_HHMM/INPUTS.sha256 candidates/freedom/run_YYYY-MM-DD_HHMM/INPUT_COMMIT candidates/freedom/run_YYYY-MM-DD_HHMM/spec.json
```

```bash
git commit -m "Freedom collider run_YYYY-MM-DD_HHMM: spec + frozen inputs (before any model call)"
```

11. Run the models against that committed spec. The script refuses to start if the config's models or settings, or any input hash, changed since the spec was written.

```bash
python3 harness/collider/run_collider.py --run-dir candidates/freedom/run_YYYY-MM-DD_HHMM
```

12. Detach and leave it running: press `Ctrl-b`, then `d`. To come back later:

```bash
tmux attach -t collider
```

13. Read the result.

```bash
less candidates/freedom/run_YYYY-MM-DD_HHMM/RESULT.md
```

14. Commit the outputs, as a second commit after the spec.

```bash
git add candidates/freedom/run_YYYY-MM-DD_HHMM
```

```bash
git commit -m "Freedom collider run_YYYY-MM-DD_HHMM: outputs, judge, controls, result"
```

15. Push when you're ready.

```bash
git push
```

You can also skip steps 9 to 11 with a single command, `python3 harness/collider/run_collider.py --runs 5`. It writes the spec, prints the commit command, and waits for Enter before calling any model. Commit from another tmux pane (`Ctrl-b` then `%`), then press Enter.

## Output layout

```text
candidates/freedom/run_YYYY-MM-DD_HHMM/
  RUN_SPEC.md  spec.json  INPUTS.sha256  INPUT_COMMIT   (written before any call)
  RUN_LOG.md                                            (timestamped steps, GPU pauses, errors)
  RESULT.md                                             (per run, P3 arithmetic, spread, controls)
  runs/rNN/calls/<call>.request.json                    (payload, model, seed, temperature; no secrets)
  runs/rNN/calls/<call>.response.json                   (raw server response)
  runs/rNN/calls/<call>.content.md                      (the model's text)
  runs/rNN/calls.jsonl                                  (timings, model digest if Ollama, status)
  runs/rNN/sides/  runs/rNN/swap_view.md  runs/rNN/parsed.json
```

## What RESULT.md reports

- For each run: the falsifier verdicts for L, H and B, the scores for A5 and P3 own, and the control results.
- P3 effective = min(P3 own, A5, A2(a)), with the arithmetic shown. A2(a) isn't under test, so P3 effective stays **pending**, with a ceiling of min(P3 own, A5). If either value is unparsed, the ceiling is reported as not computable.
- Spread across runs: min, max, median, range, and how many times each rubric value came up.
- Control (a) passes if the bad entry scores ≤ 0.25. Control (b) passes if every verdict and score in the swapped judgment matches the main judgment in the same run.

The numbers are steps on a fixed rubric, judged by models, with no human rater. Entries aren't promoted by a run.
