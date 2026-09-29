# Lens test report (2026-09-29 08:41 PDT)

- model `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`, seed 42, temperature 0, arms [1, 2, 3, 4]
- lens `5c61586e68e00aa76dc503628a10025299d8e9dd5c66ce35be647df32fb00c6c` (matches expected)
- book `freedom_of_necessity` at pinned commit `69687ee9b0997534d4388fc711b39d8e64aba29e`; twins from `lens_test/pairs`
- real entries included (from `git show 69687ee9b099:entries/<id>.md`): A2, A3, A4, D-whole, P1, PR1
- 6 real entries, 13 broken twins, 39 broken wordings; 358 saved model calls used
- arm 2 reuses arm 1's reply (checks in code, 0 extra calls); arm 4's seed+0 vote is arm 1's call; arm 3 runs on every real entry and on the wordings arm 2 did not catch (the rest count as caught by arm 3, whose score is capped by arm 2)

## Pass bar

- arm 3 does NOT win: 7 more twin(s) caught than arm 2 (need >= 3), 4 extra real entries failed (allowed <= 0)
- arm 3's extra catches came only from FAIL_QUALIFIER_DROP and FAIL_SPAN: no (A2-circular-cite: ['FAIL_DRIFT', 'FAIL_GAP', 'FAIL_UNSUPPORTED']; A3-cite-doesnt-carry-claim: ['FAIL_UNSUPPORTED']; A3-explanation-as-support: ['FAIL_PARSE', 'FAIL_SPAN', 'FAIL_UNSUPPORTED']; A3-fabricated-quote: ['FAIL_UNSUPPORTED']; A4-cap-chain-violation: ['FAIL_QUALIFIER_DROP']; blind-A2-lesion-sufficiency: ['FAIL_DRIFT', 'FAIL_PARSE', 'FAIL_UNSUPPORTED']; blind-P1-smuggled-experience: ['FAIL_DRIFT', 'FAIL_GAP', 'FAIL_UNSUPPORTED'])
- arm 3 vs arm 4 (compute control): +9 twins caught, 5 extra real entries failed

## Determinism

| arm | items rerun | flips | flip rate |
|---|---|---|---|
| arm1 | 4 | 0 | 0% |
| arm2 | 4 | 0 | 0% |
| arm3 | 4 | 0 | 0% |
| arm4 | 4 | 0 | 0% |

No flips on identical reruns.

## Broken twins (per pair)

Cells: verdict per wording (P pass, F fail, U unclear, - no result), then CAUGHT only if every wording was caught.

| pair | flaw | arm1 | arm2 | arm3 | arm4 |
|---|---|---|---|---|---|
| A2-circular-cite | circular-cite | P P P | P P P | F F F CAUGHT | P P P |
| A3-cite-doesnt-carry-claim | cite-doesnt-carry-claim | P P P | P P F partial | F F F CAUGHT | P P P |
| A3-explanation-as-support | explanation-as-support | P P P | P P F partial | F F F CAUGHT | P P P |
| A3-fabricated-quote | fabricated-quote | P P P | F P F partial | F F F CAUGHT | P P P |
| A3-source-side-flaw | source-side-flaw | P P P | P P P | F F P partial | P P P |
| A3-uncited-subclaim | uncited_subclaim_credit | P P P | P P P | P P F partial | P P P |
| A4-cap-chain-violation | cap-chain-violation | P P P | P F P partial | F F F CAUGHT | P P P |
| A4-dropped-qualifier | dropped-qualifier | P P P | F F F CAUGHT | F F F CAUGHT | P P P |
| P1-hidden-premise | hidden-premise | U F F CAUGHT | U F F CAUGHT | U F F CAUGHT | F F F CAUGHT |
| P1-overreach-past-reading | overreach-past-reading | P U U partial | F U U CAUGHT | F U U CAUGHT | P F F partial |
| blind-A2-lesion-sufficiency | necessity_sufficiency_confusion | P P P | P P P | F F F CAUGHT | P P P |
| blind-A3-scaling-overreach | overgeneralization_from_evidence_subset | P P P | P P P | P F F partial | P P P |
| blind-P1-smuggled-experience | equivocation_functional_to_phenomenal | P U U partial | P F U partial | F F U CAUGHT | P F F partial |

## Catches by flaw type

| flaw | arm1 | arm2 | arm3 | arm4 |
|---|---|---|---|---|
| cap-chain-violation | 0/1 | 0/1 | 1/1 | 0/1 |
| circular-cite | 0/1 | 0/1 | 1/1 | 0/1 |
| cite-doesnt-carry-claim | 0/1 | 0/1 | 1/1 | 0/1 |
| dropped-qualifier | 0/1 | 1/1 | 1/1 | 0/1 |
| equivocation_functional_to_phenomenal | 0/1 | 0/1 | 1/1 | 0/1 |
| explanation-as-support | 0/1 | 0/1 | 1/1 | 0/1 |
| fabricated-quote | 0/1 | 0/1 | 1/1 | 0/1 |
| hidden-premise | 1/1 | 1/1 | 1/1 | 1/1 |
| necessity_sufficiency_confusion | 0/1 | 0/1 | 1/1 | 0/1 |
| overgeneralization_from_evidence_subset | 0/1 | 0/1 | 0/1 | 0/1 |
| overreach-past-reading | 0/1 | 1/1 | 1/1 | 0/1 |
| source-side-flaw | 0/1 | 0/1 | 0/1 | 0/1 |
| uncited_subclaim_credit | 0/1 | 0/1 | 0/1 | 0/1 |
| **all** | **1/13** | **3/13** | **10/13** | **1/13** |

## Per wording

| wording | arm1 | arm2 | arm3 | arm4 |
|---|---|---|---|---|
| broken_1 | 1/13 | 4/13 | 11/13 | 1/13 |
| broken_2 | 3/13 | 5/13 | 12/13 | 3/13 |
| broken_3 | 3/13 | 7/13 | 12/13 | 3/13 |
| false passes (broken wordings passed) | 32 | 23 | 4 | 32 |

Partial catches (some wordings caught, not all):

- arm1: P1-overreach-past-reading, blind-P1-smuggled-experience
- arm2: A3-cite-doesnt-carry-claim, A3-explanation-as-support, A3-fabricated-quote, A4-cap-chain-violation, blind-P1-smuggled-experience
- arm3: A3-source-side-flaw, A3-uncited-subclaim, blind-A3-scaling-overreach
- arm4: P1-overreach-past-reading, blind-P1-smuggled-experience

## Real entries

Score change vs arm 1 (a drop on a good entry is a cost).

| entry | arm1 | arm2 | arm3 | arm4 |
|---|---|---|---|---|
| A2 | P 0.75 | P 0.75 (+0.00) | F 0.00 (-0.75) UNSUPPORTED | P 0.75 (+0.00) |
| A3 | P 0.85 | P 0.85 (+0.00) | F 0.00 (-0.85) UNSUPPORTED | P 0.85 (+0.00) |
| A4 | P 0.85 | P 0.85 (+0.00) | F 0.00 (-0.85) QUALIFIER_DROP | P 0.85 (+0.00) |
| D-whole | P 0.85 | F 0.85 (+0.00) SPAN | F 0.00 (-0.85) SPAN,DRIFT,UNSUPPORTED | P 0.85 (+0.00) |
| P1 | P 0.65 | P 0.65 (+0.00) | F 0.00 (-0.65) DRIFT | P 0.65 (+0.00) |
| PR1 | P 0.93 | P 0.93 (+0.00) | P 0.93 (+0.00) | P 0.93 (+0.00) |
| **failed / score cost** | 0 / 0.00 | 1 / 0.00 | 5 / 3.95 | 0 / 0.00 |

## Cost

| arm | model calls | tokens in | tokens out | seconds |
|---|---|---|---|---|
| arm1 | 45 | 106000 | 102362 | 6858 |
| arm2 | 0 (reused from arm 1) | 106000 | 102362 | 6858 |
| arm3 | 146 | 151175 | 215405 | 13897 |
| arm4 | 180 (incl. the seed+0 call shared with arm 1) | 424000 | 409448 | 26494 |

FAIL codes: FAIL_PARSE, FAIL_SPAN, FAIL_QUALIFIER, FAIL_CITE, FAIL_QUALIFIER_DROP, FAIL_DRIFT, FAIL_GAP, FAIL_UNSUPPORTED. Quoted spans next to the model's step sentence are in `spans_for_review.md` for a human to read (logged, not verified). Full per-item records: `items.json`.
