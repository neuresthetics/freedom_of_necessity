# Log

A dated record of what was tested and what changed, newest first. Times are Pacific (PT).

## 2026-10-24 ~05:41 PT — Core v3 kiln (92, no push)

Kilned live `candidates/core_v3/` after volume expand: coherence only, count still 92. A7/A9 cite A5; bondage/blessedness defs stand alone; thin props got Caps/stated sense. See `candidates/core_v3/BUILD_LOG.md`. Not pushed.

## 2026-10-23 — Core v3: chain file + Spinoza-ground Groups 4–5 (not pushed)

Saved live set to [candidates/core_v3/CHAIN.md](candidates/core_v3/CHAIN.md). Pulled A5 / D-free / P3 into core_v3. Drafted D-strive, D-affect, P4, P5 (conatus, affect, bondage, blessedness) extending from the seven-work chain. Map: [SPINOZA_GROUND.md](candidates/core_v3/SPINOZA_GROUND.md). Local commit only.

## 2026-10-23 — Core v3: Group 3 Nature / society / levels (not pushed)

After PR1, added D-Nature, A4 (pending), P1 (pending), P2 (pending). Freedom still parked. Stop for review. See [candidates/core_v3/](candidates/core_v3/README.md).

## 2026-10-23 — Core v3: kiln the axioms (not pushed)

Fired the live chain (seed through PR1) for soft wording, supports, circularity, undeclared readings, caps, METHOD fit. Coherence fixes only; A2/A3 still pending collider. See [candidates/core_v3/BUILD_LOG.md](candidates/core_v3/BUILD_LOG.md).

## 2026-10-23 — Core v3: Group 2 wholes block (not pushed)

After A2, added D-work, D-whole, A3 (pending), PR1 (explains, no score). Nature / society / freedom still parked. Stop for review. See [candidates/core_v3/](candidates/core_v3/README.md).

## 2026-10-23 — Core v3: grow from seed with A2 (not pushed)

After the seed (*I exist*, *What "I" names*, *What exists*), added [*A human body, and its mind*](candidates/core_v3/A2.md) (A2): empirical axiom citing A1; clause (a) pending collider; clause (b) declared reading. Body/mind before Nature. See [candidates/core_v3/BUILD_LOG.md](candidates/core_v3/BUILD_LOG.md).

## 2026-10-23 — Core v3: human-readable labels (not pushed)

Titles lead (*I exist*, *What "I" names*, *What exists*); machine ids and filenames unchanged. See `candidates/core_v3/BUILD_LOG.md`.

## 2026-10-23 — Core v3 restart: A1 alone (not pushed)

At the author's word ("A1 = I exist. That is the only axiom now"), a new candidate chain was opened under [candidates/core_v3/](candidates/core_v3/README.md):

- **Live:** D-I, D-exist, A1 (1.0). Definitions kept only to ground A1's terms.
- **Parked:** A2, A3, A4, PR1, P1, P2, D-work, D-whole, D-Nature (still in core_v2 and `entries/`); freedom candidates untouched under `candidates/freedom/`.
- Core v2 not deleted. `entries/` not demoted. Local commit only; no push.
- Note: [notes/2026-10-23-core-v3-restart.md](notes/2026-10-23-core-v3-restart.md). Build log: [candidates/core_v3/BUILD_LOG.md](candidates/core_v3/BUILD_LOG.md).

## 2026-10-18 — Collider harness for a truly separated freedom run (not pushed)

- [harness/collider/](harness/collider/README.md): `run_collider.py` (Python 3 stdlib only) reruns the freedom collision from the saved run_2026-10-18 prompts, rubric and controls, with each side, the bad-entry control, the judge and the label-swap judge as separate stateless model calls. Backends: Ollama or any OpenAI-compatible endpoint, with a model per role. Keys come from an environment variable only; the local config is gitignored.
- Writes RUN_SPEC.md, spec.json and INPUTS.sha256 to a new `candidates/freedom/run_<date_time>/` before any call, and prints the commit command so the spec can be committed first. `--run-dir` refuses to start if the models or inputs changed since the spec.
- Judge replies are parsed strictly to the five rubric values (unparsed if not exact). P3 effective = min(P3 own, A5, A2(a) pending), with the arithmetic shown. `--runs N` uses different seeds and reports spread and byte-identical repeats. Optional GPU temperature pause.
- Verified here by `--dry-run` (payloads only, no model) and parser unit tests. No model run yet, so no new numbers.

## 2026-10-18 — Freedom collider: first separated, judged run (not pushed)

- [candidates/freedom/run_2026-10-18/](candidates/freedom/run_2026-10-18/RESULT.md): spec committed before any output; questions and falsifiers verbatim from 2026-10-17.
- Book side survives, damaged; H's falsifier partly triggered; L's not. A5 0.70, P3 own 0.70; P3 effective pending (A2(a) untested), ceiling 0.70.
- Controls: bad entry failed (0.10); label swap unchanged. Both weak.
- Limits: same assistant for all sides and judge; separation procedural, no model API; no human rater. H's falsifier may be unable to fail and needs rewording.

## 2026-10-17 — Form note: the collision record is the book; collider spec disclosed (not pushed)

- [notes/2026-10-17-the-collision-record-is-the-book.md](notes/2026-10-17-the-collision-record-is-the-book.md): per-entry layout (statement, supports, cap, demonstration, collision record, scholium); sample chapter from candidates/freedom. All outcomes **unscored, collider not run**.
- [candidates/freedom/COLLIDER_SPEC_USED.md](candidates/freedom/COLLIDER_SPEC_USED.md): exact shape used for the freedom collision. Written in one pass by a Grok-based assistant from a brief; no automated harness ran. Parts taken from earlier collision files and METHOD.md are cited; parts improvised in that run are listed.

## 2026-10-17 — Freedom candidates drafted (not promoted, not pushed)

External review noted that freedom (the title claim) has no derived core entry. Drafted a candidate chain under [candidates/freedom/](candidates/freedom/README.md):

- **A5** — every event is caused (model axiom; pending; weaker than E1P29; carries verse 135‡).
- **D-free** — freedom in the strict sense (E1D7 / D-Nature Scholium 4) and by degree (own organization + knowledge of causes; CHDO not required).
- **P3** — freedom by degrees under necessity; derived from A1, A2, A5; cap = min(A2, A5); first-person "mine" on A2(b) declared, not scored.
- **collision_freedom.md** — libertarian (Kane-style), hard-incompatibilist (Pereboom-style), and book sides; falsifiers recorded before arguments; **unscored, collider not run**.
- Logs: [BUILD_LOG.md](candidates/freedom/BUILD_LOG.md), [COLLISION_LOG.md](candidates/freedom/COLLISION_LOG.md).

Nothing in `entries/` or the verses was changed. Local commit only; no push; no scores.

## 2026-10-15 — Core v2 promoted to `entries/`

At the author's decision, core v2 is now the core in force.

- **Promoted.** The twelve core v2 entries (D-I, D-exist, A1, A2, D-work, D-whole, D-Nature, A3, PR1, A4, P1, P2) were copied into `entries/`. Only their status lines and the relative links to the collision files changed. No claim wording, definition, axiom text or confidence changed: A1 stays 1.0, the rest stay "pending (collider)". [candidates/core_v2/](candidates/core_v2/README.md) stays as the record of how they were built.
- **Old core kept.** The previous entries (A1–A4, D-whole, P1, PR1) moved to [history/entries_v1/](history/entries_v1/README.md). The tag `keeper-2026-10-01` still freezes them as they were.
- **Verse 149** now reads "Only the start is beyond revision: I exist," matching A1 ([v11_changes.md](drafts/verses/v11_changes.md)).
- **No scores.** Nothing was scored; there are still no valid scores until the collider runs.

## 2026-09-29 — Entry wording fixes (after the review)

Book content only; nothing new was promoted into `entries/`.

- **A3, performed vs must perform.** The claim now says each function is *performed* at all three levels, matching its reading. Why the seven should recur (they are what a whole must do to last) is PR1's thesis and adds no confidence.
- **A3, failure case.** A row fails if society does the work only through members acting separately; A3 fails if any row fails; the rows are too loose if something D-whole rules out passes all seven. Proposed negative controls: a stone, a hurricane, an archive.
- **Sweep.** Every entry was checked for "must perform" vs "performed". The same slip was in A3's caveat 3 and PR1's Method section; both now judge by what is performed. A2, A4 and P1 were clean. D-whole's "admits what the whole needs" is part of a definition and was left as is.
- **PR1** is now "Pattern by requirement": requirement (what a whole must do to last) is kept apart from necessity (modal), which stays in the title.
- **D-whole** vantage now reads "from among its members / from a distance"; "inside" is kept for the felt side.
- **P1** now says a collective mind *happens* in society: a process emerging from feedback, not a thing the society has.

## 2026-09-29 — Back to the drawing board

An outside review of the v0.1 record, checked against the raw data, found problems serious enough that no baseline will be taken until they are fixed.

- **Arm 4 was mislabeled.** At temperature 0, the four seeded votes returned byte-identical outputs, reasoning included. So arm 4 repeated one answer four times; it was not four times the compute. The v0.1 claim that "compute alone doesn't help" is not supported by that run.
- **A3 may not be able to fail.** If any lasting institution passes all seven rows, A3 sorts things rather than discovering anything. A3 needs a stated failure case before it is scored again.
- **"Must perform" vs "performed"** is a real gap in the book, not only a harness bug, and may appear in other entries. Every entry will be checked for it.
- **The five-step lens is retired.** It will be replaced by a minimal collider: the model builds a steel man of each entry and the strongest counter steel man, both in the book's geometric form, and judges them side by side. Code checks citations and quoted spans; the model does not check its own citations.

Next: four runs on the same entries and broken twins. A clean control and the collider, each on the uncensored model and on the stock model.

The freeze on `entries/` is lifted, since the test it waited on has run and is being redone.

## 2026-09-29 — Lens test v0.1 (uncensored model)

We tested whether the five-step lens catches planted flaws better than a plain judge.

- The lens caught 10 of 13 broken twins (every wording of the twin failed).
- Code checks alone, run on the plain judge's reply, caught 3. The plain judge caught 1.
- The same plain judge voted over 4 seeds also caught 1. (Correction, same day: those votes were identical, so this was a repetition, not extra compute. See the entry above.)
- But the lens also failed 5 of 6 real entries. Every one of those failures came from a bug in the harness (its code checks or its lens prompts), not from a flaw in the book. So the lens did not pass the bar set before the run.
- It found one real issue in the book: A3's claim says each row names a function a whole "must perform", but A3's reading says to judge whether each function is "performed". These set different bars.

Details are in [results/2026-09-29_lens-v0.1/](results/2026-09-29_lens-v0.1/).

Next, the same test runs on the stock model, then v0.2 fixes the bugs.

## 2026-09-28 — Spinoza reference texts

Added frozen copies of Spinoza's *Ethics* in [sources/spinoza/](sources/spinoza/): the Latin text (its source does not say which edition it follows) and the Elwes 1883 English translation, with a sha256 manifest. They exist only to check quotations from the Kisner edition that the book cites; they are not quoted as the main text. Commit 3bd3520, 22:57 PT.
