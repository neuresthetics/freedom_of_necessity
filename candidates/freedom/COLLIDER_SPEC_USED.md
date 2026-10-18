# Collider spec used for the freedom collision (full disclosure)

**What actually happened.** The freedom collision (`collision_freedom.md`, `COLLISION_LOG.md`, committed in `efef34f`, 2026-10-17 PT) was written by a Grok-based assistant in one pass, following a brief from the author. No automated harness ran. No model was called per side, no judge was called, and no score was produced. The "falsifiers before arguments" order is the order the assistant followed while writing within that single pass; the only record of it is the log itself, and all files landed in one commit, so git does not independently prove the order.

The block below is the literal shape the run followed, reconstructed from the committed files. Provenance of each part:

- **From existing repo files:**
  - "Each side at its strongest; each point names what it stands on; then side by side" — `candidates/core_v2/collision_nature.md` (added in `2e3811f`, 2026-09-29) and `candidates/core_v2/collision_sameness.md` (added in `697b981`, 2026-09-29).
  - Spinoza by part and proposition, checked against `sources/spinoza/ethics_elwes_1883.txt` — same two files.
  - Cap = min over cited supports; definitions and declared readings add nothing — `METHOD.md` (rules 1, 4, 6; at `1c0886e`).
- **Improvised in the freedom run (not in any earlier repo file):**
  - Three sides (L / H / B) instead of two theses.
  - A falsifier per side, recorded before the arguments.
  - Point ids per side (L1–L4, H1–H4, B1–B5) and "counters left live."
  - Status label "unscored, collider not run" on every side and the outcome table.
  - **Dropped** from the earlier pattern: the named judging criteria (J1–J5/J6) and a judged verdict. The freedom collision has a side-by-side table but no judgment.

```text
COLLISION: <short title>
STATUS: candidate; scores nothing; changes nothing in entries/
INPUT_COMMIT: <HEAD hash when reading began>

1. QUESTION (fixed first)
   One sentence: what the candidate entries claim, and the rival question
   ("is that X, or a relabeling?").

2. SIDES (named before any argument)
   L  = <rival 1, "in the spirit of" a named published author>
   H  = <rival 2, "in the spirit of" a named published author>
   B  = the book (cite candidate entry ids)
   Each side: one-sentence thesis.

3. RULES
   - Each side at full strength.
   - Each point names what it stands on (entry id, verse, or source).
   - No scores.
   - Spinoza cited by part and proposition only, quotes checked against
     sources/spinoza/ethics_elwes_1883.txt.
   - Non-Spinoza authors characterized by published positions;
     no fabricated quotations.

4. FALSIFIERS (written BEFORE arguments, in order L, H, B)
   For each side: what would refute this side on its own terms.

5. ARGUMENTS (per side, in order L, H, B)
   <Side>1 (<label>). <point> [stands on: ...]
   <Side>2 ...
   Conclusion of <Side>.

6. COLLISION_LOG entry per side
   sources used (characterization) -> argument points written ->
   counters already noted in other sides (not scored) -> status

7. SIDE BY SIDE (no verdict scored)
   Table: rows = points of contention; columns = L | H | B.

8. OUTCOME
   Winner declared?   No
   Scores assigned?   No
   Entries promoted?  No
   Harness run?       No
   Strongest objections to B: <ids>
   Strongest pressure on rivals: <ids>
   Label: "unscored, collider not run"
```

## Appended 2026-10-18 — exact spec of the first judged run

Copied from run_2026-10-18/RUN_SPEC.md (committed before any output). The template above stays as the 2026-10-17 record.

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
