# Lessons from lens test v0.1 (2026-09-28 to 2026-09-29)

What the first overnight lens test measured, why its headline result is mostly luck,
what to fix for v0.2, and what the night taught about testing a judge.

The files this refers to are in this folder: `report.md`, `spans_for_review.md` (with
`spans_for_review_part2.md`) and `items.json`. Settings are in `README.md`.

## 1. The run

- Model `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`, seed 42, temperature 0, on an
  NVIDIA RTX 4000 Ada (20 GB).
- Lens hash `5c61586e68e00aa76dc503628a10025299d8e9dd5c66ce35be647df32fb00c6c`
  (the five lens prompt files; they will be published with the harness at MVP). Book pinned
  at commit 69687ee.
- 6 real entries (A2, A3, A4, D-whole, P1, PR1) and 13 broken twins, each in 3 wordings,
  so 39 broken wordings.
- Started 2026-09-28 15:40:35 PT, finished 2026-09-29 03:46:33 PT: 12 h 06 min wall clock.
- 358 unique saved model calls: 326 in the main pass plus 32 determinism reruns.
- Model time: about 11.2 h for the main pass (about 12.1 h counting the reruns). The cost
  table below adds up to 13.1 h because it counts arm 1 twice: arm 4's first vote is
  arm 1's call.
- One heat pause all night: 2026-09-28 17:15:19 PT, GPU at 83°C, resumed 30 s later.
  The harness pauses at 83°C or above and resumes at 75°C or below.

### The four arms

| arm | what it is |
|---|---|
| 1 | plain judge: one model call per item, verdict plus quoted spans |
| 2 | arm 1's reply plus code checks (quoted spans exist, qualifiers kept, cite cap); no extra calls |
| 3 | the lens: strip, restate, match, support, support_derive, plus the code checks |
| 4 | compute control: arm 1 voted over 4 seeds (42 to 45), majority wins, ties fail |

### Cost (main pass, from `report.md`)

| arm | model calls | tokens in | tokens out | seconds |
|---|---|---|---|---|
| arm1 | 45 | 106,000 | 102,362 | 6858 |
| arm2 | 0 (reuses arm 1) | - | - | - |
| arm3 | 146 | 151,175 | 215,405 | 13897 |
| arm4 | 180 (includes the shared seed+0 call) | 424,000 | 409,448 | 26494 |

## 2. Results

| measure | arm1 | arm2 | arm3 | arm4 |
|---|---|---|---|---|
| twins caught (all 3 wordings) | 1/13 | 3/13 | 10/13 | 1/13 |
| false passes (broken wordings passed, of 39) | 32 | 23 | 4 | 32 |
| real entries failed (of 6) | 0 | 1 | 5 | 0 |
| flip rate on reruns (4 items each) | 0% | 0% | 0% | 0% |

- Arm 2's one real failure: D-whole, SPAN.
- Arm 3 failed every real entry except PR1.
- Arm 4 caught exactly what arm 1 caught. Four times the compute bought nothing.

### Pass bar

Arm 3 does **not** win. It caught 7 more twins than arm 2 (the bar needed 3 more), but it
failed 4 more real entries than arm 2 (the bar allowed 0).

### Predictions on record versus what happened

| prediction | actual |
|---|---|
| arm 1 catches about 4 | 1 |
| arm 2 adds about 2 over arm 1 | +2 (right) |
| arm 3 adds 1 to 2 and misses the bar | +7, but missed the bar by failing good entries |
| arm 4 slightly better than arm 1 | the same |
| flip rate 5 to 15% | 0% |
| no good entries fail | 5 failed |

The predictions missed in both directions: the plain judge was worse than expected, and the
lens was both more sensitive and less accurate than expected.

## 3. Why arm 3's "win" was mostly luck

Every point below was confirmed from the raw calls log.

### None of the five real-entry failures is a real flaw

- **A2, A3, D-whole: UNSUPPORTED.** The support prompt hard-codes the question "is the
  function necessary at each level?" and never receives the entry's READING. So entries were
  failed for honestly stating their own hedges (for example A2's own note that "produces"
  mind is the working position of neuroscience, not a solved question).
- **A4: QUALIFIER_DROP.** The strip step kept all 7 qualifiers but wrote "At one level"
  with a capital A. The qualifier check is case-sensitive.
- **D-whole: SPAN.** The quote "A whole looks porous from inside and unified from above."
  is word for word in the entry. But the step that splits claim from evidence moved the
  Vantage paragraph into the claim, and the span check only searches the evidence. This is
  a harness bug.
- **D-whole: DRIFT.** Strip cut several sentences, and restate also dropped "works as a
  filter". Match answered "stronger", meaning the restatement says less than the core.
- **P1: DRIFT.** The restate step paraphrased away the headline term "collective mind" into
  "works as a single system".

### The checker itself is unstable

- **Match depends on order.** The same restatement got "same" in one A/B order and "weaker"
  in the other (real A2 versus blind-A2 wordings 1 and 2).
- **Three lens parse errors, all the same shape:** a missing opening quote mark on the
  JSON "step" value (for example `"step": The caveat explicitly marks ...`). One was in an
  ablation step.

### The extra twin catches were lucky

- All 7 of arm 3's extra twin catches leaned on at least one lucky wording: the generic
  necessity rejection, markdown or italics tripping the span check, the same capital-letter
  qualifier drop, a parse error, or order-dependent drift.
- No arm-3 step sentence named any planted flaw.
- Twice the necessity question even rewarded the planted text.

### A real point for the book

A3's claim says each row names a function a whole "must perform", and caveat 3 scores rows
on necessity. But A3's READING says to judge whether each function is "performed". These
set different bars. Flagged for a later revision of A3.

### The plain judge is nearly blind

Arm 1 passed 32 of the 39 broken wordings.

## 4. Fixes proposed for v0.2 (not built yet)

1. **Support step.** Pass the READING. A hedge the entry itself states counts as agreement,
   not a gap. Judge rows one at a time.
2. **Span check.** Ignore markdown (`*`, `_`, backticks) and quote-mark style. For
   definitions, also search the claim, and label a hit there SELF_QUOTE rather than SPAN.
3. **Qualifier check.** Compare regardless of capitals. Knock-on effect: A4 would then reach
   support_derive, which must see the cited entries' evidence (A3 caveat 1), or it will
   raise a new GAP.
4. **Drift.** Fire only on "stronger" or "different", never on "weaker" (every drift flag,
   real and twin, was "weaker"). Run match in both A/B orders and require them to agree.
5. **New code checks that catch planted flaws for the right reason:**
   - citation loop (A2 cites P1, which cites A2);
   - the Cap paragraph names every cite, and any number it states is no higher than the
     lowest effective score among the cites;
   - flag a principle or definition used to "offset" or "make up the shortfall"
     (METHOD rule 4);
   - flag direct quotes of 8 or more words attributed to a source that no source file backs
     (the longest quote in a real entry is 4 words).
6. **Parse.** Retry once on invalid JSON. A parse error in an ablation step should not fail
   the entry.

Estimate: fixes 1 to 4 alone leave about 5 honest catches. With fix 5 added, about 9, each
for the right reason.

### Coverage still missing

- **No test yet for unequal treatment of protected exemptions.** The planned consistency
  test: score consent and bodily-autonomy principles on neutral cases, then on the covenant
  fork, and compare the uncensored model with stock Qwen3.8-27B at the same quantization.
- **Single pass only.** There is no multi-turn round that feeds the model's own reply back
  through the lens (the lens_that_response idea).

### Later plan

v0.2 adds a steel-man object in geometric-method form. v0.3 adds the collider's logic-gate
comparisons. One night each.

## 5. Lessons about testing and learning

1. **A score means nothing until you know why it happened.** Read the reasons, not just the
   verdicts. Arm 3's 10/13 looked like a win until the reasons were read.
2. **Sensitivity is cheap; being right is the hard part.** A blade thin enough to cut
   everything also cuts good work. Arm 3 caught twins and failed 5 of 6 good entries.
3. **Plant known mistakes and count whether they are found.** The broken twins are what
   made any of this measurable.
4. **Get baselines and controls first.** Arm 4 proved that more compute alone buys nothing.
5. **Most failures are in the plumbing.** Case sensitivity, what is compared with what,
   the order of A and B, a missing quote mark.
6. **Write predictions down, because they fail.** Ours missed in both directions.
7. **Put the rigor in the method, not the model.** The model followed its instructions;
   the steps asked the wrong questions.
8. **Save points pay off.** Twelve hours unattended, every call logged and replayable, so the
   autopsy was possible the next morning.

## 6. Deeper lessons, compared with the substance_lens history

### Background

- substance_lens (2025 to 2026) forced models through consistent logic. Models learned to
  wear the lens vocabulary as a costume while steering to approved answers.
- lens_that_response fed answers back until definition shifts piled up and the model
  admitted it had lied.
- Around Grok 4.x, definitions began to bend smoothly to fit approved answers, so there was
  no longer a break point to reach.
- v0.5.8 added rules against process theater and self-grading.
- On 2026-09-28 the method moved to blind matched-pair tests on a local open-weights model,
  where the lens can only hold or lower a score and the test is pinned before it runs.

### How the v0.1 test maps onto that history

| old problem | what v0.1 does about it |
|---|---|
| the model wears lens words as a costume | twins: a catch has to name the real flaw |
| lens_that_response needed a human to push | strip, restate, match does it mechanically; span and qualifier checks are plain code |
| smooth bending leaves no break point | matched pairs need no break point: bending shows up as false passes |
| self-grading | a pass bar set in advance, pinned commits, no self-grading |
| silent model patches | a local fixed model, fixed seed, hashed lens |
| one lucky answer looks like a catch | 3 wordings per twin separate real catches from lucky ones |

### Five deeper lessons

1. **The costume is not only a guardrail problem.** Our own lens, on an uncensored model,
   wore it that night. Verdict words are just plausible text. Guardrails choose which way
   the theater leans; removing them does not cure it. Only outside measurement does.
2. **Longer, stricter prompts lose the arms race.** The prompts grew from 12 KB to 220 KB to
   356 KB, and this run's strictness caused the failures. Move checks out of prompts and
   into code, one piece at a time.
3. **Consistency beats persuasion.** Use near-twins that should get different verdicts and
   harmless variants that should get the same one. The order-swap finding shows this works
   on the checker itself too.
4. **Owning the setup is what makes it science.** Fixed weights, seed, pinned commit, hashed
   lens, logged calls: a stranger can replay it from the public repo. A smaller model is
   worth that trade.
5. **Apply "hard to vary" to the judge.** Good verdicts should ignore surface details and
   track substance. v0.1's verdicts flipped on capital letters and on A/B order, and missed
   the planted flaws, so they were easy to vary. The method holds up when applied to itself.

## 7. The catch in "hard to vary"

Being hard to vary is necessary but not sufficient.

- A closed system (a psychotic collage, a conspiracy picture) can be perfectly hard to vary
  on the inside and still be false. The data points can all be wrong; or right but organized
  wrong; or organized right but wrong at the root; or fudged by interpretation. Coherence
  mimics correctness.
- Deutsch's standard has a second half: stay hard to vary *while exposed to reality and
  criticism*. A delusion is rigid toward change but endlessly flexible toward evidence.
- An earlier book project, worked through substance_lens, is the example: accept a fictional
  axiom at the root and "truth" cascades through everything downstream, because consistency
  only checks the links, never the root.
- The weakest-support cap cannot catch a confidently wrong root.

### The guards are contact with the outside

- evidence scored against the cited sources;
- the frozen Spinoza texts (`sources/spinoza/` in this repo, commit 3bd3520);
- broken twins that can prove the judge wrong;
- a public repo where anyone can argue.

Whoever owns the machine owns its subjective truth. A mind or a model checked only against
itself cannot tell a coherent truth from a coherent delusion. The laws of argument apply
equally to every arguer, and that is what the lens is about: following the rules, which
sophists cannot do because their conclusion comes first. Leibniz's calculus ratiocinator:
"Calculemus", let us calculate.

## 8. Files

- `report.md`: the full report (pass bar, per-pair tables, real-entry scores, cost).
- `spans_for_review.md` and `spans_for_review_part2.md`: each quoted span next to the
  model's step sentence, for a human to read.
- `items.json`: full per-item records.
- Raw calls log: kept on the test machine for now; see `README.md`.
- The five lens prompt files that the hash covers: published with the harness at MVP.
- [docs/MODEL_CHOICE.md](../../docs/MODEL_CHOICE.md): why this model.
