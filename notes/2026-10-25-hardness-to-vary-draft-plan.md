# Draft plan — hardness-to-vary (next rendition)

**Date:** 2026-10-25 PT (America/Los_Angeles)  
**Updated:** same day — Jason: no split-track analysis; one combined winner; winner gets **dual render** (technical + poetic).  
**Repo:** `neuresthetics/freedom_of_necessity`  
**Status:** B0+B1 drafts started 2026-10-25 — see `candidates/core_v3/variant_sets/set_20261025_B1/` (§8 defaults taken; local only).  
**Baseline:** snapshot tag `core-v3-snapshot-v1` · live set 251 · combined chain in `candidates/core_v3/` (+ technical face in `drafts/verses_v3/technical/`)

---

## 0. Clarification (Jason)

**No split track for analysis.** We do **not** score poetic vs technical in parallel, and we do **not** treat dual tracks as the analysis unit.

| Phase | Unit | Role |
|---|---|---|
| **Vary + analyze** | **One combined chain** — entry files + deps/caps + technical statement face | Measure hardness-to-vary |
| **Pick** | **Single winner** set (same V### / entry labels) | The rendition that wins |
| **Then dual render** | **Both tracks** from that winner — technical + poetic | Same V### / labels; not an analysis fork |

The winner gets the **dual render treatment**. Existing `drafts/verses_v3/{technical,poetic}/` are prior mirrors; a fresh dual pass follows the winning combined set. Analysis never scores the two tracks against each other.

---

## 1. Goal

Build **controlled variant sets of the combined technical+structure chain** so we can measure **structural hardness-to-vary**: what stays fixed when we paraphrase, reorder, swap synonyms, or remap deps — and what breaks.

**Question we want answered**

> Which parts of the *combined* chain are load-bearing (hard to vary without breaking deps, caps, or meaning), and which are surface (easy to reword)?

**Not the goal (this pass)**

- Parallel poetic-vs-technical scoring  
- Cross-track desync as a primary metric  
- A prettier book for readers (dual render comes *after* the winner)  
- Full collider scores on all 251  
- Replacing `entries/` or promoting core v3  

---

## 2. What stays fixed vs what we vary

### Held constant (control)

| Hold | Why |
|---|---|
| **A1 root** ("I exist", score 1.0) | Pure root; caps nothing; not paraphrased away |
| **Entry ids** (`A1`, `D-I`, `P3`, …) | Index labels; graph nodes |
| **V### numbers** (V001–V251) | Join key for INDEX and later dual render |
| **Live set membership** | Same 251 ids as SNAPSHOT-v1 (no silent park/revive) |
| **Combined unit** | One chain per variant set — not a poetic fork in parallel |
| **Snapshot tip** | Variants fork from a frozen commit / tag, not a moving main |

### Allowed to vary (treatment) — on the combined chain only

| Vary | Surface or structure? |
|---|---|
| Wording inside an entry statement / technical verse | Surface |
| Examples and clarifying asides | Surface |
| Order of clauses inside one entry | Surface → can become structure |
| Synonym swaps for non-defined terms | Surface |
| Which ids appear in `cites` / `terms` / Hyper-connect | **Structure** |
| Cap text (if it changes the min-chain) | **Structure** |

**Rule of thumb:** if `dep_check.py` can see it, it is structure. If only a reader notices, it is surface.

**Out of analysis scope:** treating poetic (or technical verse) as a competing analysis arm. Both tracks are rendered **once from the winner**.

---

## 3. Variation dimensions

Run **small bands first** (BASE spine), then expand. Do not vary all 251 × all dimensions in one go.

### Bands

| Band | Entries / V### | Role |
|---|---|---|
| **B0** | V003 · A1 only | Sanity: root must refuse harmful variation |
| **B1** | BASE V001–V020 (20) | Spine; highest value for hardness |
| **B2** | One expansion group (~15–30) | Stress-test connective tissue |
| **B3** | Full 251 | Only after B1 metrics look stable |

### Dimensions (D1–D5) — combined chain

| ID | Dimension | What we change | Variants per item | Notes |
|---|---|---|---|---|
| **D1** | Paraphrase | Same claim, new wording on entry + technical face | **2** (A/B) | Keep ids + cites untouched |
| **D2** | Synonym swap | Non-defined content words only | **1** | Ban swaps of defined terms (`whole`, `work`, `affect`, …) |
| **D3** | Clause reorder | Shuffle sentence order inside one entry | **1** | Flag if deps cited mid-proof move |
| **D4** | Dep remap (soft) | Replace a cite with a sibling that *seems* related | **1** | Expect many dep_check fails — that *is* signal |
| **D5** | Dep remap (hard) | Drop a required rests-on or point at parked id | **1** on B1 only | Negative control; should always fail lint |

~~Former D4 “cross-track rewrite” removed~~ — tracks are not analysis arms; they are post-winner dual render.

### Counts for the first rendition (proposed)

Focus = **B1 (BASE 20)** + **B0**.

| Dimension | Items | Variants | Total artifacts |
|---|---|---|---|
| D1 paraphrase | 20 | ×2 | 40 |
| D2 synonym | 20 | ×1 | 20 |
| D3 reorder | 10 (odd V###) | ×1 | 10 |
| D4 soft remap | 10 (props/axioms only) | ×1 | 10 |
| D5 hard remap | 5 (incl. attempt on A1) | ×1 | 5 |
| **Sum** | | | **~85** |

Plus **golden copy**: frozen combined BASE (`candidates/core_v3/` BASE files + matching technical BASE verses) under `variant_sets/golden/`.

Keep expansion (B2+) for a later pass once B1 numbers are logged.

---

## 4. Scoring / analysis — what “hard to vary” means

For each variant of the **combined** chain, record a small row. **Hard to vary** = high break rate under surface-looking edits, or meaning drift even when lint passes.

### Automated signals (cheap)

| Signal | Tool / check | Fail means |
|---|---|---|
| Orphan cite / term / rest | `dep_check.py` | Structure broke |
| Cycle | `dep_check.py` | Structure broke |
| Missing rests (non-root) | `dep_check.py` | Structure broke |
| Missing cap | `dep_check.py` | Cap chain broke |
| Exit code ≠ 0 | `dep_check.py` | Variant is structurally invalid |
| INDEX drift | V### ↔ entry id mismatch | Numbering contract broke |

### Soft signals (human or model, logged separately)

| Signal | How | Fail means |
|---|---|---|
| **Meaning drift** | Side-by-side: golden vs variant; “same claim?” Y/N + note | Surface edit changed the thesis |
| **Cap story drift** | Cap still matches `CAPS.md` / BASE_CAPS | Confidence story no longer honest |
| **Jason-line damage** | V013 · P3 must keep the preserved freedom lines | Author lines not optional surface |
| **Collider disagreement** | Optional: run collider on A5/D-free/P3 family only | Steel-man sides flip vs golden |

### Hardness score (simple, first pass)

Per entry, across its combined-chain variants:

```
hardness ≈ (# variants that break dep_check or meaning)
           / (# variants attempted)
```

- **High hardness (≈1):** almost any edit breaks something → load-bearing  
- **Low hardness (≈0):** edits pass lint + meaning stay → surface / decorative  

Also track **false soft**: lint passes but meaning drifts (dangerous — looks fine, isn’t).

### Special cases

- **A1:** D1–D3 should preserve “I exist” as the claim; D4–D5 that touch A1’s root status should fail.  
- **Definitions (D-\*):** expect high hardness on *definiendum* words; lower on examples.  
- **P3 / Jason lines:** treat verbatim blocks as frozen; paraphrase only the surrounding frame if at all.

### Picking the single winner

After B0+B1 (or the agreed band) are scored:

1. Prefer variants that **pass** dep_check and show **no** meaning drift.  
2. Among those, use hardness insight: keep load-bearing wording stable; allow low-hardness surface polish where useful.  
3. Assemble **one** winning combined set (full band or full 251 when ready) — not a mix of track-specific winners.  
4. **Only then** give that winner the **dual render** (technical + poetic; next section).

---

## 5. Pipeline steps

```
vary / analyze combined chain  →  pick single winner  →  dual render (technical + poetic)
```

Worktree or folder (suggested):

```
candidates/core_v3/variant_sets/
  README.md                 ← pointer to this plan
  golden/                   ← frozen combined BASE (entries + technical face)
  set_<YYYYMMDD>_B1/        ← one analysis rendition
    manifest.json           ← dimension, seed, source commit
    variants/<id>/<dim>_n.md
    reports/dep_check/      ← one log per variant or batched
    reports/compare.md      ← hardness table (combined only)
    winner/                 ← chosen combined set (after pick)
    dual_render/
      technical/            ← post-winner technical track (same V### / labels)
      poetic/               ← post-winner poetic track (same V### / labels)
```

### Step-by-step

1. **Freeze baseline**  
   - Note commit SHA + tag `core-v3-snapshot-v1`.  
   - Copy BASE entry files + `drafts/verses_v3/technical/BASE.md` into `golden/` (combined control).  
   - Do **not** put poetic into the analysis golden set.

2. **Generate variants (combined only)**  
   - For each (band × dimension × item), write one variant of the entry / technical face.  
   - Manifest row: `id, V###, dim, n, source_sha, notes`.  
   - Generator may be Grok (digital intelligence) with a fixed prompt template; temperature logged.

3. **Lint / dep_check**  
   - Apply variant into a **temp copy** of `candidates/core_v3/` (never dirty the live tree blindly).  
   - Run: `python3 candidates/core_v3/tools/dep_check.py`  
   - Save stdout + exit code under `reports/dep_check/`.  
   - Optional: `--write-docs` only inside the temp copy for graph diffs.

4. **Compare (combined)**  
   - Diff statement / technical verse vs golden (ignore whitespace).  
   - Fill meaning-drift Y/N (human or separate model call; keep judge ≠ generator when possible).  
   - Write hardness table — **no poetic column**.

5. **Pick single winner**  
   - Choose one combined set for the band (rules in §4).  
   - Write it under `winner/` with the same V### / entry labels.  
   - Record why it won in `reports/compare.md`.

6. **Dual render (after winner only)**  
   - From `winner/`, produce **both** tracks for each V### — same numbering and index labels:  
     - **Technical:** deps, rests-on / supports, caps, entry ids, refs.  
     - **Poetic:** Dhammapada-plain; analogy only when it helps.  
   - Store under `dual_render/{technical,poetic}/`; later merge into `drafts/verses_v3/` only if Jason OKs.  
   - Dual-render quality is **not** fed back into hardness scores for this rendition.

7. **Collide (optional, narrow)**  
   - Only if Jason wants signal on freedom spine:  
     `harness/collider/run_collider.py` on A5 / D-free / P3 family.  
   - Compare against a golden collider run if one exists; not full-book scores.

8. **Log**  
   - Append a short dated section to `LOG.md`.  
   - Local commit the variant set + reports + winner + dual_render. **Push only if Jason asks.**

### Do not

- Score poetic and technical as rival analysis arms  
- Mutate live `candidates/core_v3/*.md` in place without a branch/worktree  
- Renumber V###  
- “Fix” D4/D5 failures — failures are the measurement  
- Mix v11/v12 verse numbers into this analysis  
- Generate either track render *before* a winner is picked  

---

## 6. Success criteria (next rendition)

**Done enough to learn from when:**

1. B0 + B1 generated under a single `manifest.json` with source SHA (combined chain only).  
2. Every variant has a dep_check exit code logged.  
3. Hardness table exists for BASE 20 (per-id + per-dimension) — **no split-track columns**.  
4. At least three **false soft** candidates flagged (lint OK, meaning drift) — or a clear note that none appeared.  
5. A1 and V013 · P3 have explicit rows (root + Jason lines).  
6. **One winner** written under `winner/` with stated pick reasons.  
7. **Dual render** of that winner exists for the band — technical + poetic, same V### / labels, clearly marked post-winner.  
8. Open questions below answered or parked by Jason.  
9. Live tree still matches pre-run `dep_check` (exit 0) on the golden tip.

**Stretch (not required):** one expansion group (B2) + one optional collider compare on P3.

---

## 7. Tie to existing tools

| Asset | Role in this plan |
|---|---|
| [`candidates/core_v3/tools/dep_check.py`](../candidates/core_v3/tools/dep_check.py) | Structural lint on the combined chain |
| [`candidates/core_v3/SNAPSHOT-v1.md`](../candidates/core_v3/SNAPSHOT-v1.md) + tag `core-v3-snapshot-v1` | Frozen baseline counts + clean dep_check reference |
| [`candidates/core_v3/DEPS.md`](../candidates/core_v3/DEPS.md) / [`CAPS.md`](../candidates/core_v3/CAPS.md) / [`CHAIN.md`](../candidates/core_v3/CHAIN.md) | Graph + cap story to diff against |
| [`drafts/verses_v3/technical/`](../drafts/verses_v3/technical/) | Technical face usable in analysis golden; also post-winner dual-render slot |
| [`drafts/verses_v3/poetic/`](../drafts/verses_v3/poetic/) | Post-winner dual-render slot (not an analysis arm) |
| [`drafts/verses_v3/INDEX.md`](../drafts/verses_v3/INDEX.md) | Shared V### ↔ entry id labels for winner + dual render |
| [`harness/collider/`](../harness/collider/) | Optional narrow collide (freedom family); not the main metric |
| [`LOG.md`](../LOG.md) | Dated record of each variant-set run |
| `PURE_ROOTS` / `BASE_CAPS` inside dep_check | Encode what must not quietly change |

---

## 8. Open questions for Jason

1. **Scope OK?** First rendition = B0 + B1 (~85 combined variants) only, expansion later?  
2. **Where to write variants?** `candidates/core_v3/variant_sets/` (proposed) — OK?  
3. **Meaning-drift judge:** you skim the hardness table, or allow a second model pass with a fixed rubric?  
4. **D4 soft remap:** constrain to “same BASE_CAPS parents only,” or free enough to fail often?  
5. **V013 Jason lines:** freeze verbatim always in the combined winner (and thus in both dual-render tracks)?  
6. **Collider this round:** skip, or run once on A5/D-free/P3 golden vs one paraphrase set?  
7. **Public / push:** keep variant sets local until you say push (default: local only)?  
8. **Winner grain:** one winner for the whole BASE band, or per-entry winners assembled into one set?

---

## 9. Suggested first commands (after OK)

```bash
# from repo root — confirm golden tip is clean
python3 candidates/core_v3/tools/dep_check.py

# after a temp combined variant tree is built (example)
python3 candidates/core_v3/tools/dep_check.py
# exit code + stdout → variant_sets/set_…/reports/dep_check/
```

No generation in this commit — plan only.
