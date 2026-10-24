# core_v3 dependency tools

## `dep_check.py` (stdlib)

Validates the live set (BASE 20 + kilned expansion):

- every `cites` / `terms` / Hyper-connect rests-on id is **live**
- no dependency cycles
- every non-root has ≥1 live rests-on (`D-I`, `D-exist`, `A1` may be roots)
- every entry documents a Cap

```bash
# from repo root
python3 candidates/core_v3/tools/dep_check.py
python3 candidates/core_v3/tools/dep_check.py --fix-orphans --sync-hc --write-docs
```

`--fix-orphans` remaps known parked cites to live replacements.
`--sync-hc` rewrites Hyper-connect Rests on / Supports from the graph.
`--write-docs` regenerates `DEPS.md`, `CAPS.md`, and the CHAIN expansion mermaid.
