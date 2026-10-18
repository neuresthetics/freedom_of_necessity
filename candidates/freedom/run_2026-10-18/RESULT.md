# Result — freedom collider, 2026-10-18

**Verdict.** The book side survives, damaged. No falsifier against B was triggered. H's falsifier was partly triggered. L's was not.

| Side | Falsifier | Status |
|---|---|---|
| L (Kane-style) | not triggered | survives, damaged (luck/chance objection unanswered) |
| H (Pereboom-style) | partly triggered | checkable difference shown; the "not more chain" half may be unable to fail |
| B (book) | not triggered | survives, damaged (H2 relabeling partly unanswered) |

**Numbers.** A5 = 0.70. P3 own = 0.70. A2(a) not tested (pending).
P3 effective = min(0.70, 0.70, pending) → **pending, ceiling 0.70**. Reference 1 − 0.70 = 0.30 is not the negation's score (METHOD rule 2: claim and negation need not sum to 1; the brief's sum-to-1 request was overridden by METHOD and disclosed in RUN_SPEC).

**Controls.** (a) Bad entry scored 0.10: PASS. (b) Label/order swap unchanged: PASS. Both are weak tests (see controls/CONTROLS.md).

**What broke.**
- H's falsifier, as written, may be unable to fail: any difference in a caused world can be called "more chain." It needs rewording before the next run.
- P3 cannot get a number until A2(a) is scored.
- The 0.70 values are rubric steps, not measurements.

**Limitations.**
- The same assistant wrote all three sides, the control and the judgment. No model API was available, so separation was procedural (separate prompt files and steps), not enforced. The assistant had already read the 2026-10-17 collision.
- Self-judging, no human rater, one run, no seeds.
- The controls show only that the judge fails an obvious contradiction and repeats itself under relabeling.

Read these numbers as a first ranking under the cap chain, not as validated confidence. Entries are not promoted.
