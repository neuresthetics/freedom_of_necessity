# variant_sets — hardness-to-vary (combined chain)

**Plan:** [`notes/2026-10-25-hardness-to-vary-draft-plan.md`](../../../notes/2026-10-25-hardness-to-vary-draft-plan.md)

Analysis runs on **one combined technical+structure chain** (entry files + technical face).  
Poetic is **not** an analysis arm. **Dual render (technical + poetic) happens only after a single winner is picked.**

## Layout

```
variant_sets/
  README.md                 ← this file
  golden/                   ← frozen BASE control (entries + technical BASE)
  set_20261025_B1/          ← first rendition (B0 + B1)
    manifest.json
    variants/<id>/<dim>_n.md
    reports/dep_check/
    reports/compare.md
    winner/                 ← empty until pick
    dual_render/            ← empty until after winner
  tools/generate_b1.py      ← generator used for this set
```

## Current set

| Field | Value |
|---|---|
| Set | [`set_20261025_B1/`](set_20261025_B1/) |
| Band | B0 (A1 sanity) + B1 (BASE V001–V020) |
| Variants | **85** (D1×40, D2×20, D3×10, D4×10, D5×5) |
| dep_check | see set README / `reports/compare.md` |
| Winner | not picked |
| Dual render | not started |
| Push | **local only** until Jason says push |

## Defaults taken for plan §8

Jason had not answered the open questions; these defaults unblocked the first drafts (also in the set README + manifest):

1. Scope = B0+B1 only  
2. Folder = `candidates/core_v3/variant_sets/`  
3. Meaning-drift judge = TBD (Jason skim; second-model parked)  
4. D4 soft = free enough to fail often  
5. V013 Jason lines = freeze verbatim in eventual winner + both dual tracks  
6. Collider = skip this round  
7. Push = local only  
8. Winner grain = one winner for whole BASE band (later)

## Rule

Do not mutate live `candidates/core_v3/*.md` from a variant without an explicit promote / winner step. Always apply variants in a temp copy and run `tools/dep_check.py` there.
