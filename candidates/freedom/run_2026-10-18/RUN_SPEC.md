# Run spec — freedom collider, 2026-10-18

Written and committed before any side argument or judgment exists. Times Pacific.

```text
RUN: freedom collider, first separated + judged run
INPUT_COMMIT: 8e165afface1cdc42c4b5d5a31f173e82f63e6ee
INPUT HASHES: INPUTS.sha256 (A5, D-free, P3, collision_freedom, COLLISION_LOG,
              COLLIDER_SPEC_USED, BUILD_LOG, METHOD)
QUESTION + FALSIFIERS: verbatim from COLLISION_LOG.md (committed in efef34f);
              copied into prompts/; not altered.

ENGINE: no model API is configured on the machine (no local model server,
  no API key set up for this). So every step is done by the same assistant
  (Grok-based) that wrote the 2026-10-17 collision.
SEPARATION: procedural, not enforced. Each side is written from its own
  saved prompt file (prompts/side_X.txt) in a separate step, into raw/side_X.md,
  without opening other raw/ files until the judge step. The assistant has
  read the 2026-10-17 collision, so prior exposure to all sides is real and
  cannot be removed. Order: L, H, B, then control_bad_B.

SIDES: L libertarian (spirit of Kane); H hard incompatibilist (spirit of
  Pereboom); B the book (A5, D-free, P3).

JUDGE (judge/JUDGE.md), per side:
  1. Falsifier check: was this side's pre-set falsifier triggered by the other
     sides' strongest points or by the entries/evidence?
     Verdict: NOT TRIGGERED | PARTLY TRIGGERED | TRIGGERED, with reasons.
  2. Score each scored claim on 0-1 with this rubric:
       0.85  survives: no falsifier against it triggered; no rival point unanswered
       0.70  survives, damaged: no falsifier triggered, but a rival point stands
             unanswered on the claim's own terms
       0.50  undecided: falsifier partly triggered, or the stack cannot tell
       0.25  refuted in part: falsifier triggered on one clause
       0.10  refuted: falsifier triggered outright
     Only these five values. No value above 0.85 from a self-judged run.
  Scored claims: A5; P3 own (B's distinctive claim: degree sense deserves the
  name and 15(b) is not idle). A2(a) is not under test here: it stays pending.
  D-free is a definition: adds no confidence. A2(b) is a declared reading:
  unscored.

METHOD rules applied: cap (P3 effective = min(P3 own, A5, A2(a)));
  explanation adds nothing; declared readings unscored.
  Negation: the brief asked for claim + negation = 1. METHOD rule 2 says they
  move oppositely and need NOT sum to 1. METHOD governs; the 1 - x figure is
  reported only as a reference number, not as the negation's score.

CONTROLS:
  (a) bad entry: control_bad_B ("freedom requires uncaused choice; therefore
      freedom exists and A5 is true") judged with the same rubric against B's
      falsifier and A5. PASS if scored <= 0.25.
  (b) label/order swap: re-judge with labels hidden (sides renamed X/Y/Z by a
      fixed map in controls/swap_map.txt, presented in order B, H, L).
      PASS if every falsifier verdict and score is unchanged.
      Known weakness: same judge, labels guessable from content.

OUTPUTS: prompts/, raw/, judge/JUDGE.md, controls/, RUN_LOG.md, RESULT.md.
Nothing is pushed. Entries are not promoted by this run.
```
