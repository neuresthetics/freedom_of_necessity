# Draft plan — hardness-to-vary (next rendition)

**Date:** 2026-10-25 PT (America/Los_Angeles)  
**Repo:** `neuresthetics/freedom_of_necessity`  
**Status:** plan only — do not generate variants until Jason OKs the open questions at the end.  
**Baseline:** snapshot tag `core-v3-snapshot-v1` · live set 251 · dual tracks in `drafts/verses_v3/`

---

## 1. Goal

Build **controlled variant sets** of the dual-track / core_v3 chain so we can measure **structural hardness-to-vary**: what stays fixed when we paraphrase, reorder, swap synonyms, rewrite poetic ↔ technical, or remap deps — and what breaks.

**Question we want answered**

> Which parts of the chain are load-bearing (hard to vary without breaking deps, caps, meaning, or cross-track sync), and which are surface (easy to reword)?

**Not the goal (this pass)**

- A prettier book for readers  
- Full collider scores on all 251  
- Replacing `entries/` or promoting core v3  

---

## 2. What stays fixed vs what we vary

### Held constant (control)

| Hold | Why |
|---|---|
| **A1 root** ("I exist", score 1.0) | Pure root; caps nothing; not paraphrased away |
| **Entry ids** (`A1`, `D-I`, `P3`, …) | Index labels; graph nodes |
| **V### numbers** (V001–V251) | Shared across tracks; INDEX is the join key |
| **Live set membership** | Same 251 ids as SNAPSHOT-v1 (no silent park/revive) |
| **Pairing rule** | Every V### has both poetic + technical, or neither |
| **Snapshot tip** | Variants fork from a frozen commit / tag, not a moving main |

### Allowed to vary (treatment)

| Vary | Surface or structure? |
|---|---|
| Wording inside a verse / entry statement | Surface |
| Analogy / example lines (poetic) | Surface |
| Order of clauses inside one entry | Surface → can become structure |
| Synonym swaps for non-defined terms | Surface |
| Poetic ↔ technical rewrite of the *same* claim | Cross-track surface |
| Which ids appear in `cites` / `terms` / Hyper-connect | **Structure** |
| Cap text (if it changes the min-chain) | **Structure** |

**Rule of thumb:** if `dep_check.py` can see it, it is structure. If only a reader notices, it is surface.

---

## 3. Variation dimensions

Run **small bands first** (BASE spine), then expand. Do not vary all 251 × all dimensions in one go.

### Bands

| Band | Verses / entries | Role |
|---|---|---|
| **B0** | V003 · A1 only | Sanity: root must refuse harmful variation |
| **B1** | BASE V001–V020 (20) | Spine; highest value for hardness |
| **B2** | One expansion group (~15–30) | Stress-test connective tissue |
| **B3** | Full 251 | Only after B1 metrics look stable |

### Dimensions (D1–D6)

| ID | Dimension | What we change | Variants per item | Notes |
|---|---|---|---|---|
| **D1** | Paraphrase | Same claim, new wording | **2** per verse (A/B) | Keep ids + cites untouched |
| **D2** | Synonym swap | Non-defined content words only | **1** | Ban swaps of defined terms (`whole`, `work`, `affect`, …) |
| **D3** | Clause reorder | Shuffle sentence order inside one entry | **1** | Flag if deps cited mid-proof move |
| **D4** | Cross-track rewrite | Poetic → technical style, or reverse, same V### | **1** each direction on sample | Pair must still match INDEX claim |
| **D5** | Dep remap (soft) | Replace a cite with a sibling that *seems* related | **1** | Expect many dep_check fails — that *is* signal |
| **D6** | Dep remap (hard) | Drop a required rests-on or point at parked id | **1** on B1 only | Negative control; should always fail lint |

### Counts for the first rendition (proposed)

Focus = **B1 (BASE 20)** + **B0**.

| Dimension | Items | Variants | Total artifacts |
|---|---|---|---|
| D1 paraphrase | 20 | ×2 | 40 |
| D2 synonym | 20 | ×1 | 20 |
| D3 reorder | 10 (odd V###) | ×1 | 10 |
| D4 cross-track | 10 (even V###) | ×1 dir | 10 |
| D5 soft remap | 10 (props/axioms only) | ×1 | 10 |
| D6 hard remap | 5 (incl. attempt on A1) | ×1 | 5 |
| **Sum** | | | **~95** |

Plus **golden copies**: frozen poetic + technical BASE as `variant_set/golden/`.

Keep expansion (B2+) for a later pass once B1 numbers are logged.

---

## 4. Scoring / analysis — what “hard to vary” means

For each variant, record a small row. **Hard to vary** = high break rate under surface-looking edits, or meaning drift even when lint passes.

### Automated signals (cheap)

| Signal | Tool / check | Fail means |
|---|---|---|
| Orphan cite / term / rest | `dep_check.py` | Structure broke |
| Cycle | `dep_check.py` | Structure broke |
| Missing rests (non-root) | `dep_check.py` | Structure broke |
| Missing cap | `dep_check.py` | Cap chain broke |
| Exit code ≠ 0 | `dep_check.py` | Variant is structurally invalid |
| Cross-track desync | Script: same V### claim hash / shared key phrases | Tracks no longer say the same thing |
| INDEX drift | V### ↔ entry id mismatch | Numbering contract broke |

### Soft signals (human or model, logged separately)

| Signal | How | Fail means |
|---|---|---|
| **Meaning drift** | Side-by-side: golden vs variant; “same claim?” Y/N + note | Surface edit changed the thesis |
| **Cap story drift** | Cap still matches `CAPS.md` / BASE_CAPS | Confidence story no longer honest |
| **Jason-line damage** | V013 · P3 must keep the preserved freedom lines | Author lines not optional surface |
| **Collider disagreement** | Optional: run collider on A5/D-free/P3 family only | Steel-man sides flip vs golden |

### Hardness score (simple, first pass)

Per entry, across its variants:

```
hardness ≈ (# variants that break dep_check or desync or meaning)
           / (# variants attempted)
```

- **High hardness (≈1):** almost any edit breaks something → load-bearing  
- **Low hardness (≈0):** edits pass lint + meaning stay → surface / decorative  

Also track **false soft**: lint passes but meaning drifts (dangerous — looks fine, isn’t).

### Special cases

- **A1:** D1–D4 should preserve “I exist” as the claim; D5–D6 that touch A1’s root status should fail.  
- **Definitions (D-\*):** expect high hardness on *definiendum* words; lower on examples.  
- **P3 / Jason lines:** treat verbatim blocks as frozen; paraphrase only the surrounding frame if at all.

---

## 5. Pipeline steps

Worktree or folder under the repo (suggested):

```
candidates/core_v3/variant_sets/
  README.md                 ← pointer to this plan
  golden/                   ← copy of SNAPSHOT tip texts used as control
  set_<YYYYMMDD>_B1/        ← one rendition
    manifest.json           ← dimension, seed, source commit
    variants/<id>/<dim>_n.md
    reports/dep_check/      ← one log per variant or batched
    reports/compare.md      ← hardness table
    reports/desync.md       ← cross-track mismatches
```

### Step-by-step

1. **Freeze baseline**  
   - Note commit SHA + tag `core-v3-snapshot-v1`.  
   - Copy BASE entry files + `drafts/verses_v3/{poetic,technical}/BASE.md` into `golden/`.

2. **Generate**  
   - For each (band × dimension × item), write one variant file.  
   - Manifest row: `id, V###, dim, n, source_sha, notes`.  
   - Generator may be Grok (digital intelligence) with a fixed prompt template; temperature logged.

3. **Lint / dep_check**  
   - Apply variant into a **temp copy** of `candidates/core_v3/` (never dirty the live tree blindly).  
   - Run:  
     `python3 candidates/core_v3/tools/dep_check.py`  
   - Save stdout + exit code under `reports/dep_check/`.  
   - Optional: `--write-docs` only inside the temp copy for graph diffs.

4. **Compare**  
   - Diff statement / verse body vs golden (ignore whitespace).  
   - Cross-track: for D1–D4, check poetic ↔ technical still share the same claim for that V###.  
   - Fill meaning-drift Y/N (human or separate model call; keep judge ≠ generator when possible).

5. **Collide (optional, narrow)**  
   - Only if Jason wants signal on freedom spine:  
     `harness/collider/run_collider.py` on A5 / D-free / P3 family (existing harness).  
   - Compare verdict block to a golden collider run if one exists; do not treat as full-book scores.

6. **Log**  
   - Append a short dated section to `LOG.md`.  
   - Write `reports/compare.md` hardness table.  
   - Local commit the variant set + reports. **Push only if Jason asks.**

### Do not

- Mutate live `candidates/core_v3/*.md` in place without a branch/worktree  
- Renumber V###  
- “Fix” D5/D6 failures — failures are the measurement  
- Mix v11/v12 verse numbers into this analysis  

---

## 6. Success criteria (next rendition)

**Done enough to learn from when:**

1. B0 + B1 generated under a single `manifest.json` with source SHA.  
2. Every variant has a dep_check exit code logged.  
3. Hardness table exists for BASE 20 (per-id + per-dimension).  
4. At least three **false soft** candidates flagged (lint OK, meaning drift) — or a clear note that none appeared.  
5. A1 and V013 · P3 have explicit rows (root + Jason lines).  
6. Open questions below answered or parked by Jason.  
7. Live tree still matches pre-run `dep_check` (exit 0) on the golden tip.

**Stretch (not required):** one expansion group (B2) + one optional collider compare on P3.

---

## 7. Tie to existing tools

| Asset | Role in this plan |
|---|---|
| [`candidates/core_v3/tools/dep_check.py`](../candidates/core_v3/tools/dep_check.py) | Structural lint: orphans, cycles, rests, caps |
| [`candidates/core_v3/SNAPSHOT-v1.md`](../candidates/core_v3/SNAPSHOT-v1.md) + tag `core-v3-snapshot-v1` | Frozen baseline counts + clean dep_check reference |
| [`candidates/core_v3/DEPS.md`](../candidates/core_v3/DEPS.md) / [`CAPS.md`](../candidates/core_v3/CAPS.md) / [`CHAIN.md`](../candidates/core_v3/CHAIN.md) | Graph + cap story to diff against |
| [`drafts/verses_v3/`](../drafts/verses_v3/) (INDEX, poetic/, technical/) | Dual-track surface; D4 + desync checks |
| [`harness/collider/`](../harness/collider/) | Optional narrow collide (freedom family); not the main metric |
| [`LOG.md`](../LOG.md) | Dated record of each variant-set run |
| `PURE_ROOTS` / `BASE_CAPS` inside dep_check | Encode what must not quietly change |

---

## 8. Open questions for Jason

1. **Scope OK?** First rendition = B0 + B1 (~95 variants) only, expansion later?  
2. **Where to write variants?** `candidates/core_v3/variant_sets/` (proposed) vs `drafts/verses_v3/variants/`?  
3. **Meaning-drift judge:** you skim the hardness table, or allow a second model pass with a fixed rubric?  
4. **D5 soft remap:** should soft remaps be constrained to “same BASE_CAPS parents only,” or free enough to fail often?  
5. **V013 Jason lines:** freeze verbatim always, or allow poetic-frame paraphrase outside the two italic blocks?  
6. **Collider this round:** skip, or run once on A5/D-free/P3 golden vs one paraphrase set?  
7. **Public / push:** keep variant sets local until you say push (default: local only)?

---

## 9. Suggested first commands (after OK)

```bash
# from repo root — confirm golden tip is clean
python3 candidates/core_v3/tools/dep_check.py

# after a temp variant tree is built (example)
python3 candidates/core_v3/tools/dep_check.py
# exit code + stdout → variant_sets/set_…/reports/dep_check/
```

No generation in this commit — plan only.
