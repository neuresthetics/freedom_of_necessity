# set_20261025_B1 — hardness-to-vary drafts (B0+B1)

**Status:** first variant batch generated for analysis. **No winner yet. No dual render yet.**
**Unit:** one combined technical+structure chain (entry files + technical face).  
**Plan:** [notes/2026-10-25-hardness-to-vary-draft-plan.md](../../../../notes/2026-10-25-hardness-to-vary-draft-plan.md)

## Source

| Field | Value |
|---|---|
| Live tip | `378eeb522805116f35af64c81870a97a2c76c26f` |
| Tag `core-v3-snapshot-v1` | `fa11703510a1b7d15a8942ff99f85d7d6ed20009` |
| Golden | [`../golden/`](../golden/) |
| Manifest | [`manifest.json`](manifest.json) |
| Lint vs meaning table | [`reports/compare.md`](reports/compare.md) |

## Counts

- **Variants:** 85
- **By dim:** {"D1": 40, "D2": 20, "D3": 10, "D4": 10, "D5": 5}
- **dep_check pass / fail:** 74 / 11

## Layout

```
variants/<id>/D1_A.md …     ← combined entry body variant
variants/<id>/D1_*.technical_face.md  ← golden technical verse sidecar (D1)
reports/dep_check/<id>_<dim>_<n>.txt
reports/compare.md
winner/                     ← empty until pick
dual_render/                ← empty until after winner
```

## Defaults for plan §8 (Jason had not answered; chosen to unblock)

1. **Scope:** B0+B1 only.  
2. **Folder:** `candidates/core_v3/variant_sets/` (as proposed).  
3. **Meaning-drift judge:** TBD — table ready for Jason skim; second-model pass parked.  
4. **D4 soft:** free enough to fail often (signal).  
5. **V013 Jason lines:** freeze verbatim in eventual winner + both dual tracks; this batch may rephrase P3 frame but keeps CHDO / necessity thesis.  
6. **Collider:** skip this round.  
7. **Push:** local only until Jason says push.  
8. **Winner grain:** one winner for whole BASE band (later).

## Do not

- Score poetic vs technical as rival arms  
- Dual-render before winner  
- Treat D4/D5 failures as bugs to fix — they are the measurement  
- Mutate live `candidates/core_v3/*.md` from these drafts without an explicit promote step  
