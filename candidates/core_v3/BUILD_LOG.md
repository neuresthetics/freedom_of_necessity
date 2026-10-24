# Build log — core v3 restart

Times are Pacific (America/Los_Angeles). Newest steps at the bottom. Input commit when reading began: `1188c7376abe1e37e661e0a8096be49b04abf7ef` (HEAD after `git pull --ff-only`, 2026-10-23).

---

## 2026-10-23 ~21:15 PT — Task intake

- Author: **A1 = I exist. That is the only axiom now. Begin.**
- Via parent: pull; read A1 / D-I / D-exist / README / METHOD; rebuild from scratch with A1 sole axiom; new folder `candidates/core_v3/`; do not delete core_v2; do not push; commit locally if clean.
- Standing rules applied: no rewrite of A1's root wording beyond coherence; one unified chain; Spinoza by part and proposition only; no Kisner; no push.

---

## 2026-10-23 21:15 PT — Inputs read

| Path | sha256 (at read) |
|---|---|
| `candidates/core_v2/A1.md` | `936412de1483a478b4045a8a3878a17a9a690a192bb73389e6f3e31980f78c7e` |
| `candidates/core_v2/D-I.md` | `9cc283b617549a53e7fd257788e29f055c53d510bb49718daceb393e83c3a798` |
| `candidates/core_v2/D-exist.md` | `d876a8bf513d51021208daf5f060b3acad058f4f76b2f5e3a234e8fb91cf23e7` |
| `entries/A1.md` | `b697e5eb97baf35beb325f5ff478eefd1b717d95e3d9d110924c13573ef102fa` |
| `entries/D-I.md` | `413d9599a0cc0b5c74a1bdcd12ec7f384f8c7db08dd0b9b9eed2789e78a3ab29` |
| `entries/D-exist.md` | `0c617fa46a92cbd97564c64485de10eb79059b2b5ad30873ce8d5f45f9c48986` |
| `METHOD.md` | `94487db81b6997aac304ed145ac095f191ad5c8717a749273e764410fc45b2eb` |
| `candidates/core_v2/README.md` | (skimmed; order and caps) |

Also skimmed: `candidates/freedom/BUILD_LOG.md` (log format), `LOG.md` (newest-first convention).

---

## 2026-10-23 21:16 PT — Decisions

### D1 — Keep D-I and D-exist
- **Chose:** keep both as live definitions ahead of A1.
- **Why:** A1's own text states itself in those two defined terms; METHOD and HOW treat definitions before claims. Without them, "I" and "exist" are unbound.
- **Rejected:** A1 alone with no defs (loses the thin reading that blocks Spinoza's strongest sense of exist, and loses Lichtenberg's second clause for "I").

### D2 — Park the rest; do not delete
- **Chose:** park A2–A4, PR1, P1, P2, D-work, D-whole, D-Nature (and leave freedom candidates where they are).
- **Why:** author said A1 is the only axiom now; rebuild from that. Core v2 is the record.
- **Rejected:** wipe `entries/` or delete core_v2 (author and brief: do not delete core_v2; promotion change needs separate OK).

### D3 — Base text
- **Chose:** start from promoted `entries/` wording of A1 / D-I / D-exist (slightly tighter than the core_v2 copies), then trim forward cites to the retired chain.
- **Why:** `entries/` is what was in force; A1's root sentence stays "I exist."

### D4 — Coherence edits only
- Removed "Cited by A2" / "splits at A2" / "What the author's I is, A2 says" and the "Where else it is used" list that named parked entries.
- Dropped Kisner edition lines from references (standing rule: Spinoza by part and proposition only).
- Scholia that said "AI" now say "digital intelligence" where they name a possible next thinker (book-page wording preference applied lightly in scholia titles).
- **Did not** change the root sentence, the certainty argument, or the thin scope of A1.

---

## 2026-10-23 21:17 PT — Files written

- `candidates/core_v3/D-I.md`
- `candidates/core_v3/D-exist.md`
- `candidates/core_v3/A1.md`
- `candidates/core_v3/README.md`
- `candidates/core_v3/PARKED.md`
- `candidates/core_v3/BUILD_LOG.md` (this file)
- `notes/2026-10-23-core-v3-restart.md`
- `LOG.md` entry (newest first)

`entries/` not modified. `candidates/core_v2/` not modified. No push.

---

## 2026-10-23 21:18 PT — Human-readable labels

- **Author:** Make axiom labels human readable friendly.
- **Chose:** keep machine `id` and filenames (`A1.md`, `D-I.md`, `D-exist.md`) for harness / later promotion; put clear English in `title` and lead every heading and index with that title; id secondary in parentheses or a column.
- **Titles now:**
  - A1 → *I exist* (unchanged)
  - D-I → *What "I" names* (was "I")
  - D-exist → *What exists* (was "Exist, last"; lasting stays in the definition body)
- **Also:** README live-chain table and mermaid; PARKED tables (title first, using archive titles for parked entries); body openings on the three live files.
- **Filenames:** unchanged.
- No push.

---

## 2026-10-23 ~22:30 PT — Seed saved

- Author: **save those three as the seed.**
- *I exist* (A1), *What "I" names* (D-I), *What exists* (D-exist) are now named **the seed** of the restarted chain. No wording change to the entries; README gains a "The seed" section.
- Not pushed.

---

## 2026-10-23 ~22:32 PT — Grow from the seed: A2

- **Author:** "ok, now, start with that, and go" (seed already pushed as `f52911c`).
- **Brief:** from A1 alone, derive the next entry by geometric method; prefer body/mind over Nature; do not blindly copy core_v2; human-readable title; commit locally only; no push.

### Inputs read (this step)

| Path | Role |
|---|---|
| `candidates/core_v3/{A1,D-I,D-exist,README,BUILD_LOG,PARKED}.md` | live seed |
| `candidates/core_v2/A2.md` / `entries/A2.md` | parked reference (same text) |
| `METHOD.md`, `HOW_THIS_BOOK_IS_BUILT.md` | kinds, caps, declared reading |
| `candidates/core_v2/README.md` (order + Group 1) | why A2 sat after A1 historically |

### Decision D5 — Next entry is A2 (body/mind), not Nature

- **Chose:** write *A human body, and its mind* (A2) as the next live axiom after the seed.
- **Why (geometric):** A1 explicitly leaves open what the I is. The next load-bearing claim is an answer to that question. It cannot be deduced from A1; it is a new empirical axiom that cites A1 for its subject. Nature, wholes, and society each need more than one body or a measure of wholeness, which this chain does not have yet. Body/mind is the direct fill of A1's gap.
- **Rejected:** Nature first (needs plurality / D-Nature apparatus). Wholes first (needs D-work / D-whole). A bare "I think" proposition (already inside A1's defined-terms restatement). Blind copy of core_v2 A2 (forward cites to D-work and P1 would re-attach parked chain).

### Decision D6 — Rebuild, not copy

- Kept: two-clause structure; (a) scored empirical / (b) declared reading unscored; lesion + cell evidence; Spinoza cites by part and proposition; hard-problem limit; A1 cite caps nothing.
- Changed for v3: no forward cites to D-work, D-whole, or P1; "digital intelligence" in Scholium 1; open forks named in Scholium 2; `scored_as` and status fields for harness; "Why this follows the seed" section; sameness explicitly not claimed here.
- Inline stipulations for organization / mind / first–third person left inline (fork: extract as definitions later).

### Decision D7 — Confidence

- **Chose:** `pending (collider)`. No self-score this step.
- **Why:** METHOD / standing practice for empirical axioms until the collider runs.

### Files written or updated

- `candidates/core_v3/A2.md` (new)
- `candidates/core_v3/README.md` (live chain + mermaid + caps + open forks)
- `candidates/core_v3/PARKED.md` (A2 marked returned to live)
- `candidates/core_v3/BUILD_LOG.md` (this step)
- `notes/2026-10-23-core-v3-restart.md` (growth note)
- `LOG.md` (newest-first entry)

`entries/` not modified. `candidates/core_v2/` not modified. No push.

---

## 2026-10-23 ~22:35 PT — Group 2 block: work, whole, A3, PR1

- **Author:** "go" — keep deriving; one unified entry; scores pending; do not stop for forks unless a wrong guess breaks the method; coherent next block then stop for review; no full-core rebuild; commit locally; no push.

### Decision D8 — Next block is wholes apparatus, not Nature or society

- **Chose:** D-work → D-whole → A3 → PR1 as one block.
- **Why (geometric):** After A2, the chain has a body and an organization but no measure of wholeness. To say whether this body (or anything) is a whole, and to prepare levels/society later, the book needs (i) a definition of work and the seven works, (ii) a definition of whole/degree/member/self-production/sameness, (iii) a model axiom that the seven-work measure agrees with self-production where both can be checked, (iv) an explaining principle that adds no score. Nature is outside D-whole's finite domain and was a separate collision — leave parked. Society (A4) and P1/P2 need A3's measure first — leave for the next block after review.
- **Rejected:** jump to A4/P1 (missing measure); Nature first (not required by A1+A2; domain note in D-whole is enough); full core rebuild in one pass (brief: stop for review).

### Decision D9 — Adapt archive text, do not invent a new seven-work scheme

- **Chose:** rebuild from core_v2 D-work / D-whole / A3 / PR1 with v3 coherence edits.
- **Why:** those texts already embed the collisions (nature domain, sameness Def 12, Mossio (b), robot hard case). Rewriting the measure from scratch would break method without new evidence.
- **Edits:** human titles; `status: candidate (core v3)`; `scored_as` on A3/PR1; no Kisner; "digital intelligence"; drop live forward dependence on A4/P1/P2/D-Nature; archive collision links kept as `../core_v2/...`; A2 pointed at D-work for "organization"; A2 open-fork scholium replaced by defaults already chosen.

### Files

- new/updated: `D-work.md`, `D-whole.md`, `A3.md`, `PR1.md`, `A2.md` (coherence), `README.md`, `PARKED.md`, this log, note, `LOG.md`
- untouched: `entries/`, `candidates/core_v2/`, freedom candidates
- no push

---

## 2026-10-23 ~22:40 PT — Kiln the axioms

- **Author:** "kiln the axioms" — fire/harden the live core_v3 chain; fix only what makes the chain more coherent without rewriting the core thesis; human-readable titles kept; commit locally; no push.

### Stress checklist (METHOD)

| Check | Finding |
|---|---|
| Soft / stale wording | A1 still said nothing in this folder cites it, and that the next step was unfixed; D-I/A1 said what the I is "waits for a later claim" after A2 was live. Fixed. |
| Missing supports | Caps intact: A1=1.0 caps nothing; A2 cites A1; A3 cites nothing; PR1 adds nothing. Definitions carry no confidence. |
| Circularity | A3 still tests seven works against Def 11 (self-production without the seven). PR1 still stated about self-producers, not wholes. No new cycles. |
| Undeclared readings | A2 (a)/(b) already split. A3's multicellular-as-self-producing was only a body caution — elevated to declared reading in frontmatter and body. |
| Confidence caps | Unchanged numerically; A2/A3 still `pending (collider)`. |
| Coherence with METHOD | Explanation adds nothing (PR1); stated sense / declared reading kept distinct; organization no longer looks forward from A2 to D-work for its sense. |

### Hardened (coherence only)

1. **A1** — Cite note now names A2; "what I am" points to A2; Scholium 1 names A2 as next live step and leaves digital-intelligence evidence open.
2. **D-I** — "What the I is" points to A2.
3. **A2** — Organization sense fixed inline; no load-bearing forward cite to D-work; Scholium 2 says D-work adopts A2's sense.
4. **D-work** — Def 3 adopts A2's organization wording and generalizes it; `scored_as` added; collective-mind forward line does not claim society.
5. **D-whole** — `scored_as` added (parity with other definitions).
6. **A3** — Multicellular self-production named declared reading (unscored); "arguably" on bacterial transport replaced with "under one reading of as one".
7. **PR1** — "In the core" → "In this chain".

### Still soft (not faked hard)

- A2 (a) and A3 unscore until the collider runs.
- A3 F1 risk on bacterial transport; F2 if Def 3(b) is loosened; F3 grader disagreement (e.g. red-blood-cell memory).
- Seven-work list is a revisable selection (Miller + defense).
- PR1: some requirements hold only in some circumstances; memory-as-requirement is nearly empty; tension with A3's "all seven" for tiny self-producers is the F1 hard case, not resolved by wording.
- Hard problem left open (A2 limit).
- Nature, society (A4), P1/P2, freedom still parked.
- `entries/` and core_v2 untouched; harness may still read promoted copies until promotion.

### Files touched

- `A1.md`, `D-I.md`, `A2.md`, `D-work.md`, `D-whole.md`, `A3.md`, `PR1.md`, `README.md`, this log, `notes/2026-10-23-core-v3-restart.md`, `LOG.md`

No push. No thesis rewrite. Titles unchanged.

---

## 2026-10-23 ~23:37 PT — Group 3: Nature, society, levels (D-Nature, A4, P1, P2)

- **Author:** "Now grow them out"
- **Brief:** extend core_v3 past kilned set (through PR1); next coherent block D-Nature → A4 → P1 → P2; human-readable titles + machine ids; one unified chain; scores pending; use parked core_v2 as reference, do not blindly copy; update README, PARKED, BUILD_LOG; commit locally; do NOT push; stop after P2 for review (no freedom unless it must follow in the same block — prefer stop after P2).

### Inputs read (this step)

| Path | Role |
|---|---|
| `candidates/core_v3/{README,PARKED,BUILD_LOG,A2,A3,D-work,D-whole,PR1}.md` | live chain style + kiln |
| `candidates/core_v2/{D-Nature,A4,P1,P2}.md` | parked reference |
| METHOD / standing rules | caps, declared readings, no Kisner, no push |

### Decision D10 — Next block is Nature + society + levels, not freedom

- **Chose:** D-Nature → A4 → P1 → P2 as one block; stop before freedom.
- **Why (geometric):** After A3/PR1 the chain has a measure of wholeness for finite things but (i) no fixed sense of what lies outside that domain, (ii) no claim that a larger organization I belong to is a whole, (iii) no demonstration that I am whole-at-one-level and part-at-the-next, (iv) no naming of society's control/signaling/memory as a collective mind in the book's thin sense. Freedom (A5/D-free/P3) needs A5 (every event is caused) as a new model axiom and does not depend on P2 specifically; it can follow as its own block after review.
- **Rejected:** freedom in the same commit (brief: prefer stop after P2); jump to A4 without D-Nature (P1's stop-short-of-Nature scholium and D-whole domain need the definition live); blind copy of core_v2 (forward language and Kisner lines would re-attach archive habits).

### Decision D11 — Adapt archive text with v3 coherence

- Kept: D-Nature thin vs declared reading; A4 seven-row take-apart + membership cites A2; P1 demonstration steps; P2 thin "collective mind" (activity only, no feeling).
- Changed for v3: human titles lead; `status: candidate (core v3)`; `scored_as` on all four; no Kisner; "Why this follows…" sections; cross-refs by live titles; D-Nature Scholium 4 foreshadows freedom without claiming it; D-whole domain and Def 10 notes updated now that Nature/society are live; D-work forward lines point to A4/P2.

### Caps (unchanged numerically)

- A4 pending: min(weakest row, A2)
- P1 pending: min(A2, A3, A4)
- P2 pending: min(A4 control/signaling/memory, A2 via A4)
- D-Nature: definition, adds nothing

### Files

- new: `D-Nature.md`, `A4.md`, `P1.md`, `P2.md`
- updated: `D-whole.md`, `D-work.md`, `README.md`, `PARKED.md`, this log, note, `LOG.md`
- untouched: `entries/`, `candidates/core_v2/`, `candidates/freedom/`
- no push

---

## 2026-10-23 ~23:48 PT — Save chain file; Spinoza-ground extension (Groups 4–5)

- **Author:** "Save that to file, then continue to evolve it according to all the ground Spinoza covered, but as extending from this."
- **Brief:** write CHAIN.md; map Ethics ground vs live chain; pull A5/D-free/P3 into core_v3 with human titles; draft next defs/props for Parts III–V ground; update README/PARKED/BUILD_LOG; commit locally; do NOT push.

### Inputs read (this step)

| Path | Role |
|---|---|
| `candidates/core_v3/{README,PARKED,BUILD_LOG,A2,P2,D-Nature}.md` | live style through Group 3 |
| `candidates/freedom/{A5,D-free,P3,README}.md` | freedom drafts to promote into v3 |
| `METHOD.md` | caps, declared readings |
| Ethics loci (by memory + freedom/D-Nature cites) | substance, causality, mind-body, affects, bondage, blessedness |

### Decision D12 — Snapshot first, then extend

- **Chose:** write [CHAIN.md](CHAIN.md) as the clear live-set file (title, id, kind, one-line, confidence, cites); dated note under `notes/`.
- **Why:** author asked to save the set to file before evolving further.

### Decision D13 — Pull freedom into core_v3 (Group 4)

- **Chose:** copy A5, D-free, P3 into `candidates/core_v3/`; add "Why this follows…" leads; `status: candidate (core v3)`; human titles (*Every event is caused*; *Freedom, strict and by degree*; *Freedom by degrees under necessity*); point D-Nature Scholium 4 at the live freedom block.
- **Why (geometric):** title claim needs necessity + degree-freedom after P2; drafts already existed and match METHOD.
- **Rejected:** leave freedom only under `candidates/freedom/` (author: continue evolving the live chain); rewrite freedom from scratch (would drop collider-ready wording).
- Archive under `candidates/freedom/` kept as collision record.

### Decision D14 — Extend Parts III–V ground from this chain (Group 5)

- **Chose:** draft D-strive, D-affect, P4, P5 — conatus, affect, bondage, blessedness restated in seven-work / degree-freedom language.
- **Why:** Spinoza's remaining load-bearing ground after freedom; must extend from D-work/D-free/P3, not import a second psychology.
- **Rejected:** copy Ethics proposition order as new axioms; score substance/attributes; invent three-kinds-of-knowledge entry this pass; Kisner; "fractal".
- Gaps left explicit in [SPINOZA_GROUND.md](SPINOZA_GROUND.md).

### Caps (Group 4–5)

- A5 pending (cites nothing)
- P3 pending: min(A2, A5)
- P4 pending: min(A2, A5, P3)
- P5 pending: min(A2, A5, P3)
- D-strive, D-affect, D-free: definitions, add nothing

### Files

- new: `CHAIN.md`, `SPINOZA_GROUND.md`, `A5.md`, `D-free.md`, `P3.md`, `D-strive.md`, `D-affect.md`, `P4.md`, `P5.md`
- updated: `D-Nature.md` (Scholium 4 foreshadow → live), `README.md`, `PARKED.md`, this log
- notes: `notes/2026-10-23-core-v3-chain-and-spinoza-ground.md`; restart note appended; `LOG.md`
- untouched: `entries/`, `candidates/core_v2/`, freedom collision archive
- no push

---

## 2026-10-24 ~05:30 PT — Volume expansion (author: expand as much as possible)

- **Author (from machine):** worry less about accuracy; focus on expanding as much as possible.
- **Brief:** grow live chain aggressively from 19; cover remaining Spinoza ground + consciousness/levels/causality; prefer volume; human titles; one chain; pending/rough OK; no Kisner; no "fractal"; public-safe; update CHAIN/SPINOZA_GROUND/README/BUILD_LOG; commit locally; **do not push**.

### Decision D15 — Volume over polish

- **Chose:** draft ~73 new lighter entries (definitions, model axioms, props, one open problem, one principle) extending from the seed in Groups 6–13, rather than kilning Groups 1–5 further.
- **Why:** author explicitly de-prioritized accuracy for coverage this turn.
- **Rejected:** only filling SPINOZA_GROUND gaps with a handful of polished props; copying Ethics proposition order as new root axioms; inventing non-Spinoza sources; Kisner; "fractal".

### New groups

| Group | Theme | New ids (sample) |
|---|---|---|
| 6 | Substance, attribute, mode | D-substance, D-attribute, D-mode, D-infinite-mode, D-essence, A6, P6 |
| 7 | Causality variants | D-adequate-cause, D-necessity, D-contingent, A7, A9, P7 |
| 8 | Ideas / kinds of knowledge | D-idea…D-knowledge, D-experience, D-sign, P8, P9 |
| 9 | Named affects | D-joy…D-wonder, D-named-affects, D-power, D-activity, PR2, P10, P11 |
| 10 | Good, bad, virtue | D-good, D-bad, D-useful, D-perfection, D-virtue, D-bondage, D-blessedness, P12, P13 |
| 11 | Politics / state | D-right, D-state, D-law, D-sovereign, A8, P14, P15 |
| 12 | Eternity of mind | D-eternity, P16, P17, P20 |
| 13 | Consciousness / levels / open | OP1, D-consciousness, D-level, P18, P19, P21 |

### Counts

- Before: **19** live chain entries
- After: **92** live chain entries (+73)

### Files

- new: 73 entry markdown files under `candidates/core_v3/`
- updated: `CHAIN.md`, `SPINOZA_GROUND.md`, `README.md`, `PARKED.md`, this log
- generator scratch: `tmp/gen_expand.py` (box only; not part of the book)
- untouched: `entries/`, `candidates/core_v2/`, freedom collision archive
- **no push**

---

## 2026-10-24 ~05:41 PT — Kiln the live chain (92)

- **Author:** "Kiln it" (from machine).
- **Brief:** fire for coherence — soft wording, missing supports, circular cites, undeclared readings, confidence caps, METHOD; prefer harden over shrink; update CHAIN/BUILD_LOG/README; commit locally; **do NOT push**.

### Stress checklist (METHOD)

| Check | Finding |
|---|---|
| Soft / stale wording | A9 "rough" + grammar ("organization works has"); P16 "rough"; D-contingent/P7 "maybe"; P10/P11 "agent own"; D-consciousness/D-necessity missing possessives; P4 "unclearknown". Fixed. |
| Missing supports | A7 and A9 named A5 as companion but cited nothing — now cite A5; caps `min(own, A5)`. Thin props lacked stated sense / how-it-fails / Cap prose — added without inventing new claims. |
| Circularity | No mutual cite cycles. D-bondage / D-blessedness pointed at P4/P5 while defining the words those props use — reversed: defs stand alone on D-free/D-power; props derive. D-level terms no longer list P1 as a term-dep. |
| Undeclared readings | P17 God=Nature bulk already declared; reinforced METHOD rule 6. D-consciousness ties first-person side to A2(b) as unscored. A6 uniqueness remains weaker than full E1P14 (stated). |
| Confidence caps | A7/A9 updated in CHAIN caps table. P21 stays conjecture-grade. A1=1.0 only scored number. Definitions/PR1/PR2/OP1 add nothing. |
| YAML / harness | A3 `scored_as` had unescaped `A4's` (parser break) — fixed. All 92 frontmatters parse. |
| Coherence with METHOD | Explanation adds nothing (PR2 Limit); stated sense vs declared reading kept; open problem (OP1) remains unscored. |

### Hardened (coherence only; count still 92)

1. **A3** — YAML-safe `scored_as`.
2. **A6** — clearer why-follows (uniqueness slot, not full E1P14).
3. **A7** — cites A5; Cap = min(own, A5).
4. **A8** — stated sense, what-would-lower, Cap prose.
5. **A9** — grammar; drop "rough"; cites A5; stated sense; Cap = min(own, A5).
6. **P4** — "unclearly known".
7. **P6–P21** (thin expansion props) — stated sense and/or how-it-fails and Cap prose; P10/P11 possessive; P16 drop rough; P17 declared bulk reinforced; P21 conjecture-grade kept explicit.
8. **D-bondage, D-blessedness** — stand before props; no definitional dependence on P4/P5.
9. **D-contingent, D-consciousness, D-necessity, D-level, D-named-affects, OP1, PR2** — soft wording / order / Limit / METHOD notes.
10. **CHAIN.md** — regenerated from frontmatter; kiln banner; A7/A9 caps; 92 rows.
11. **README.md** — kiln status + rule 7.

### Still soft (not faked hard)

- A2–A9 and P1–P21 pending collider (only A1 = 1.0).
- A3 hard cases (bacterial transport F1, robot F2, RBC memory F3) unchanged.
- A6 weaker than full Part I geometric sequence; P16/P17/P20 eternity/intellectual-love remain candidate / declared-heavy.
- P21 conjecture-grade collective freedom.
- Named-affect catalog (D-named-affects) not separately collided.
- OP1 hard problem open.
- Promotion into `entries/` still needs a separate author OK.
- Volume-era defs (many Group 6–13 D-* files) stay thin by design; kiln clarified order and METHOD, did not expand them into full scholia.

### Files touched

- Entries: A3, A6–A9, P4, P6–P21, D-bondage, D-blessedness, D-contingent, D-consciousness, D-necessity, D-level, D-named-affects, OP1, PR2 (and YAML escape cleanups on A9/P10/D-blessedness/D-consciousness).
- Indexes: `CHAIN.md`, `README.md`, this log.
- Untouched: `entries/`, `candidates/core_v2/`, freedom collision archive, thesis/verse drafts.
- **no push**

---

## 2026-10-24 ~06:45 PT — Prune to strongest + hyper-connect

- **Author:** "Prune to strongest and then hyper connect." (from machine; via parent).
- **Brief:** keep load-bearing ~15–20 (seed, A2, wholes/degree, freedom under necessity, blessedness/bondage, strong hinges); move rest to PARKED_VOLUME (do not delete); hyper-connect kept set (cites, terms, cross-links, Caps, CHAIN graph); human titles; update README/BUILD_LOG; commit locally; **do NOT push**.

### Kept (20)

| # | Id | Title |
|---|---|---|
| 1 | D-I | What "I" names |
| 2 | D-exist | What exists |
| 3 | A1 | I exist |
| 4 | A2 | A human body, and its mind |
| 5 | D-work | Work, and the seven works |
| 6 | D-whole | Whole, degree, member, level, self-production, sameness |
| 7 | A3 | The seven works sort things the way self-production does |
| 8 | A4 | The society I live in is a whole to a degree |
| 9 | P1 | A whole at one level, a part at the next |
| 10 | P2 | A collective mind happens |
| 11 | A5 | Every event is caused |
| 12 | D-free | Freedom, strict and by degree |
| 13 | P3 | Freedom by degrees under necessity |
| 14 | D-affect | Affect, and change of power |
| 15 | D-bondage | Bondage |
| 16 | D-blessedness | Blessedness |
| 17 | P4 | Bondage is acting from what is outside |
| 18 | P5 | Blessedness is the power itself |
| 19 | P19 | Degree of whole tracks degree of freedom only loosely |
| 20 | P21 | Society can be freer without feeling |

### Parked

- **72** entry files → `PARKED_VOLUME/` (+ `PARKED_VOLUME/INDEX.md`).
- Not deleted. Includes substance/mode, knowledge ladder, named affects, politics, eternity, OP1/P18, PR1, D-Nature, D-strive, thin props, etc.

### Hyper-connect

- Each kept file: `cites` / `terms` restricted to the live set; **Hyper-connect** block with Rests on / Supports / Cap / link to CHAIN.
- P21 no longer cites P18 (feeling-not-required folded into statement; Cap = min(P2,P3,A4)).
- D-free carries a short **Nature (inline)** note; full D-Nature parked.
- D-affect / P4 / P5 no longer depend on live D-strive or D-power (power via D-affect; strive → works continuing).
- `CHAIN.md` regenerated: 20-row table, Caps, mermaid dependency graph, Cap-chain ASCII.
- `README.md`, `PARKED.md` updated.

### Counts

- Before prune: **92** live
- After: **20** live + **72** parked volume

### Untouched

- `entries/`, `candidates/core_v2/`, freedom collision archive, thesis/verse drafts
- **no push**

---

## 2026-10-24 ~06:51 PT — Lock BASE (20 seed-spine)

- **Author:** "Lock in that base chain, save it, and then radical expand from it."
- **Action:** Freeze the pruned 20 as **BASE**. Snapshot [BASE.md](BASE.md). Mark each file `status: base (locked)` + BASE badge. Update [CHAIN.md](CHAIN.md) / [README.md](README.md).
- **Counts:** **20** BASE locked. PARKED_VOLUME still 72. Expansion comes in the next commit.
- **Untouched:** `entries/`, `candidates/core_v2/`, freedom collision archive.
- **no push** (lock commit only; expand follows).

---

## 2026-10-24 ~06:55 PT — Radical expand from BASE

- **Author:** "Lock in that base chain, save it, and then radical expand from it."
- **Prior:** BASE lock commit (20 frozen + BASE.md).
- **Action:** Grow **109** new expansion entries in `expansion/` across 9 groups, each citing BASE hinges (and other expansion ids when chaining). Volume over polish. Human titles. Indexes: expansion/INDEX.md, group READMEs, CHAIN.md section, README.
- **Not done:** Blind unpark of PARKED_VOLUME (72 still parked). No collider scores. No push.
- **Counts:** BASE **20** locked + expansion **109** = **129** in play; parked volume **72** separate.
- **Untouched:** `entries/`, `candidates/core_v2/`, BASE entry bodies beyond lock badges.

---

## 2026-10-24 ~06:56 PT — Radical expand batch 2

- **Author:** "Expand further."
- **Action:** Keep BASE 20 locked. Add **139** new expansion entries in 11 new groups under `expansion/`. Rebuild [expansion/INDEX.md](expansion/INDEX.md). Update CHAIN/README/BUILD_LOG.
- **Counts:** BASE **20** + expansion **248** (was 109) = **268** in play; PARKED_VOLUME **72** untouched.
- **New groups:** time_identity, edge_cases, language_comm, economy_tech, affects_more, practices, conflict_peace, error_illusion, digital_mind, cosmology_value, biology_deep.
- **no push**

## 2026-10-24 PT — kiln expansion to strongest half

- BASE 20 remains locked ([BASE.md](BASE.md)).
- Expansion was 248; kept **122** live (~half of 248); parked **126** under [expansion/PARKED/](expansion/PARKED/).
- Hyper-connected survivors (rests-on, BASE hinges, supports cite graph).
- Snapshots: [KILNED.md](KILNED.md), [CHAIN.md](CHAIN.md), [expansion/INDEX.md](expansion/INDEX.md).
- Prefer kept: freedom/wholes/mind, P19/P21 bridges, seed-novel pressure tests. Cut: thin Spinoza restates, affect catalog, thin practices/economy/language.
- Not pushed.

---

## 2026-10-24 ~07:10 PT — Dependency management + further connect

- **Author:** "Further connect. Dependency management is required."
- **Action:**
  1. Added stdlib checker [`tools/dep_check.py`](tools/dep_check.py) (validate live cites, cycles, rests-on, caps; `--fix-orphans`, `--sync-hc`, `--write-docs`).
  2. **Orphan cites:** 19 parked-target cites across 14 live expansion entries → remapped to live BASE/expansion ids (0 cycles before/after).
  3. Synced Hyper-connect on all **142** live entries (BASE Supports kept; **Supports (expansion)** filled; expansion reverse links).
  4. Wrote [`DEPS.md`](DEPS.md) (reverse index), [`CAPS.md`](CAPS.md) (cap rules), refreshed CHAIN expansion mermaid + links.
  5. Regenerated [`expansion/INDEX.md`](expansion/INDEX.md) cites/supports columns.
- **Cycles found:** 0. **Cycles fixed:** 0 (none present).
- **Orphan cites fixed:** 19 (all pointed at `expansion/PARKED/` or equivalent parked ids).
- **Counts:** BASE **20** locked + expansion **122** = **142** in play. Parks untouched.
- **BASE lock:** titles/ids/cap rules unchanged; Hyper-connect Supports (expansion) is connective tissue only.
- **no push**

