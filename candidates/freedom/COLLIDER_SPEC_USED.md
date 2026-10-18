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
