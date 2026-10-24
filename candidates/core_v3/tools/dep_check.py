#!/usr/bin/env python3
"""Dependency management for candidates/core_v3 (BASE + live expansion).

Stdlib only. Validates:
  - every cite/term/rests-on id exists in the live set (or is explicitly allowed root)
  - no dependency cycles
  - every non-root has at least one live rests-on (cites ∪ terms ∪ Hyper-connect)
  - every entry documents a Cap (Hyper-connect or frontmatter confidence for A1)

Can also:
  --fix-orphans   remap cites that point at PARKED ids to live replacements
  --sync-hc        rewrite Hyper-connect Rests on / Supports from the live graph
  --write-docs     write DEPS.md, CAPS.md; refresh CHAIN expansion mermaid section

Usage:
  python3 candidates/core_v3/tools/dep_check.py
  python3 candidates/core_v3/tools/dep_check.py --fix-orphans --sync-hc --write-docs
"""
from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # candidates/core_v3
SKIP_NAMES = {
    "BASE.md", "CHAIN.md", "KILNED.md", "BUILD_LOG.md", "README.md",
    "PARKED.md", "SPINOZA_GROUND.md", "INDEX.md", "DEPS.md", "CAPS.md",
}
# Pure roots: may have empty deps.
PURE_ROOTS = {"D-I", "D-exist", "A1"}
BASE_ORDER = [
    "D-I", "D-exist", "A1", "A2", "D-work", "D-whole", "A3", "A4", "P1", "P2",
    "A5", "D-free", "P3", "D-affect", "D-bondage", "D-blessedness", "P4", "P5",
    "P19", "P21",
]
BASE_CAPS = {
    "A1": "1.0; caps nothing",
    "A2": "own score of clause (a); A1 caps nothing",
    "A3": "own score (cites nothing scored)",
    "A4": "min(weakest work-row, A2)",
    "P1": "min(A2, A3, A4)",
    "P2": "min(A4 control/signaling/memory, A2 via A4)",
    "A5": "own score",
    "P3": "min(A2, A5)",
    "P4": "min(A2, A5, P3)",
    "P5": "min(A2, A5, P3)",
    "P19": "min(P1, P3)",
    "P21": "min(P2, P3, A4); conjecture-grade",
    "D-I": "definition; adds nothing",
    "D-exist": "definition; adds nothing",
    "D-work": "definition; adds nothing",
    "D-whole": "definition; adds nothing",
    "D-free": "definition; adds nothing",
    "D-affect": "definition; adds nothing",
    "D-bondage": "definition; adds nothing",
    "D-blessedness": "definition; adds nothing",
}

# Orphan (parked) cite remaps → live replacements. Applied by --fix-orphans.
ORPHAN_FIXES = {
    "D-compassion": {
        "cites": ["D-affect", "D-joy", "P4"],
        "statement_note": None,
        "statement_replace": (
            "Compassion is joy (D-joy) insofar as another's rise in power of acting "
            "(D-affect) moves us; confusion about that move is a bondage pattern (P4)."
        ),
    },
    "D-education": {
        "cites": ["P3", "D-clear-knowledge", "P-habit-can-bond"],
    },
    "D-friendship": {
        "cites": ["D-joy", "A2", "P5"],
    },
    "OP-why-anything": {
        "cites": ["A1", "D-Nature-one"],
    },
    "P-anger-can-repair": {
        "cites": ["D-affect", "P4", "P3"],
    },
    "P-apparent-contingency": {
        "cites": ["A5", "D-Nature-one", "D-clear-knowledge"],
    },
    "P-bot-swarm-bondage": {
        "cites": ["D-public-affect", "P-propaganda-bondage", "P21"],
    },
    "P-copy-not-A1-transfer": {
        "cites": ["A1", "P-other-bodies", "P-digital-A1"],
    },
    "P-debt-bondage": {
        "cites": ["P4", "D-bondage", "A4"],
    },
    "P-evolution": {
        "cites": ["A3", "A5", "D-work"],
    },
    "P-habit-can-bond": {
        "cites": ["P3", "P4", "D-work"],
    },
    "P-habit-stack": {
        "cites": ["P3", "P-habit-can-bond", "D-clear-knowledge"],
    },
    "P-naming": {
        "cites": ["D-language", "D-reason-know", "D-clear-knowledge"],
    },
    "P-nihilism-confused": {
        "cites": ["P5", "P-final-causes-heuristic", "D-blessedness"],
        "statement_replace": (
            "Rejecting final-cause cosmos does not erase blessedness as power of acting "
            "(P5, D-blessedness); missing cosmic purpose ≠ missing local power."
        ),
    },
}

ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_-]*$")


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, text
    block = text[4:end]
    body = text[end + 5 :]
    data = {}
    # Simple YAML subset: key: value / key: [a, b]
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.strip().startswith("#"):
            i += 1
            continue
        if ":" not in line:
            i += 1
            continue
        key, _, raw = line.partition(":")
        key = key.strip()
        raw = raw.strip()
        if raw == "" and i + 1 < len(lines) and lines[i + 1].startswith("  - "):
            items = []
            i += 1
            while i < len(lines) and lines[i].startswith("  - "):
                items.append(_unquote(lines[i][4:].strip()))
                i += 1
            data[key] = items
            continue
        if raw.startswith("[") and raw.endswith("]"):
            inner = raw[1:-1].strip()
            if not inner:
                data[key] = []
            else:
                data[key] = [_unquote(x.strip()) for x in inner.split(",")]
        else:
            data[key] = _unquote(raw)
        i += 1
    return data, body


def _unquote(s: str) -> str:
    if len(s) >= 2 and ((s[0] == s[-1] == "'") or (s[0] == s[-1] == '"')):
        return s[1:-1]
    return s


def format_cites_yaml(cites):
    if not cites:
        return "[]"
    return "[" + ", ".join(cites) + "]"


def extract_ids_from_line(line: str):
    """Pull ids from 'Title (ID)' or bare ID lists separated by ; or ,."""
    skip = {"none", "root", "see", "DEPS", "md", "CAPS", "CHAIN", "more"}
    ids = re.findall(r"\(([A-Za-z][A-Za-z0-9_-]*)\)", line)
    # Drop placeholder parens like (none)
    ids = [i for i in ids if i.lower() not in skip and i != "none"]
    if ids:
        return ids
    # strip markdown emphasis
    clean = re.sub(r"[*`]", "", line)
    # drop leading label remnants
    parts = re.split(r"[;,]", clean)
    out = []
    for part in parts:
        part = part.strip()
        if not part or part in {"—", "-", "(none)", "none"} or part.lower().startswith("(none"):
            continue
        # last token if "Title ID" without parens — take whole if id-shaped
        tok = part.split()[-1] if " " in part else part
        tok = tok.strip(" .")
        if tok.lower() in skip:
            continue
        if ID_RE.match(tok):
            out.append(tok)
    return out


def parse_hyper_connect(body: str):
    m = re.search(r"## Hyper-connect\n(.*?)(?:\n## |\Z)", body, re.S)
    if not m:
        return None
    block = m.group(1)
    rests, supports, cap = [], [], None
    for line in block.splitlines():
        if "**Rests on:**" in line:
            rests = extract_ids_from_line(line.split(":**", 1)[-1])
        elif line.strip().startswith("- **Supports"):
            supports = extract_ids_from_line(line.split(":**", 1)[-1])
        elif "**Cap:**" in line:
            cap = line.split(":**", 1)[-1].strip()
    return {"block": block, "rests": rests, "supports": supports, "cap": cap, "span": m.span(1)}


def iter_live_files():
    for p in sorted(ROOT.glob("*.md")):
        if p.name in SKIP_NAMES:
            continue
        yield p
    exp = ROOT / "expansion"
    if exp.exists():
        for p in sorted(exp.rglob("*.md")):
            if "PARKED" in p.parts:
                continue
            if p.name in SKIP_NAMES or p.name == "README.md":
                continue
            yield p


def load_parked_ids():
    parked = {}
    for park_root in (ROOT / "PARKED_VOLUME", ROOT / "expansion" / "PARKED"):
        if not park_root.exists():
            continue
        for p in park_root.rglob("*.md"):
            if p.name in SKIP_NAMES or p.name == "README.md":
                continue
            text = p.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(text)
            if fm and fm.get("id"):
                parked[fm["id"]] = p
    return parked


def load_live():
    entries = {}
    for p in iter_live_files():
        text = p.read_text(encoding="utf-8")
        fm, body = parse_frontmatter(text)
        if not fm or not fm.get("id"):
            continue
        eid = fm["id"]
        hc = parse_hyper_connect(body)
        cites = fm.get("cites") or []
        terms = fm.get("terms") or []
        if isinstance(cites, str):
            cites = [cites] if cites else []
        if isinstance(terms, str):
            terms = [terms] if terms else []
        rests_hc = hc["rests"] if hc else []
        # dependency edges: cites + terms + hyper rests
        deps = []
        for x in list(cites) + list(terms) + list(rests_hc):
            if x and x not in deps:
                deps.append(x)
        entries[eid] = {
            "id": eid,
            "path": p,
            "fm": fm,
            "body": body,
            "text": text,
            "title": fm.get("title") or eid,
            "type": fm.get("type"),
            "kind": fm.get("kind"),
            "cites": list(cites),
            "terms": list(terms),
            "hc": hc,
            "deps": deps,
            "cap": (hc or {}).get("cap"),
            "is_base": str(fm.get("status", "")).startswith("base"),
            "group": fm.get("group"),
        }
    return entries


def find_cycles(entries):
    ids = set(entries)
    deps = {e: [d for d in entries[e]["deps"] if d in ids] for e in entries}
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {k: WHITE for k in entries}
    stack = []
    cycles = []

    def dfs(u):
        color[u] = GRAY
        stack.append(u)
        for v in deps[u]:
            if color[v] == GRAY:
                i = stack.index(v)
                cycles.append(stack[i:] + [v])
            elif color[v] == WHITE:
                dfs(v)
        stack.pop()
        color[u] = BLACK

    for u in entries:
        if color[u] == WHITE:
            dfs(u)
    return cycles


def check(entries, parked):
    live = set(entries)
    orphan_cites = []
    orphan_terms = []
    orphan_rests = []
    missing_rests = []
    missing_cap = []
    missing_hc = []

    for eid, e in sorted(entries.items()):
        for c in e["cites"]:
            if c not in live:
                orphan_cites.append((eid, c, "parked" if c in parked else "missing"))
        for t in e["terms"]:
            if t not in live:
                orphan_terms.append((eid, t, "parked" if t in parked else "missing"))
        if e["hc"]:
            for r in e["hc"]["rests"]:
                if r not in live:
                    orphan_rests.append((eid, r, "parked" if r in parked else "missing"))
        else:
            missing_hc.append(eid)

        live_deps = [d for d in e["deps"] if d in live]
        if eid not in PURE_ROOTS and not live_deps:
            missing_rests.append(eid)

        if not e["cap"]:
            # A1 may rely on frontmatter confidence
            if eid == "A1" and e["fm"].get("confidence") is not None:
                pass
            else:
                missing_cap.append(eid)

    cycles = find_cycles(entries)
    return {
        "orphan_cites": orphan_cites,
        "orphan_terms": orphan_terms,
        "orphan_rests": orphan_rests,
        "missing_rests": missing_rests,
        "missing_cap": missing_cap,
        "missing_hc": missing_hc,
        "cycles": cycles,
    }


def ref(eid, entries):
    title = entries[eid]["title"] if eid in entries else eid
    return f"*{title}* ({eid})"


def rewrite_cites_in_text(text, new_cites):
    """Replace frontmatter cites: line and body **Cites.** line."""
    text2 = re.sub(
        r"(?m)^cites:\s*\[.*?\]\s*$",
        f"cites: {format_cites_yaml(new_cites)}",
        text,
        count=1,
    )
    cites_line = ", ".join(new_cites) if new_cites else "—"
    text2 = re.sub(
        r"(?m)^\*\*Cites\.\*\*.*$",
        f"**Cites.** {cites_line}.",
        text2,
        count=1,
    )
    return text2


def replace_statement(text, new_statement):
    return re.sub(
        r"(?m)^\*\*Statement\.\*\*.*$",
        f"**Statement.** {new_statement}",
        text,
        count=1,
    )


def fix_orphans(entries, parked):
    changed = []
    for eid, fix in ORPHAN_FIXES.items():
        if eid not in entries:
            continue
        e = entries[eid]
        old = list(e["cites"])
        new = list(fix["cites"])
        if old == new and "statement_replace" not in fix:
            continue
        text = e["path"].read_text(encoding="utf-8")
        text = rewrite_cites_in_text(text, new)
        if fix.get("statement_replace"):
            text = replace_statement(text, fix["statement_replace"])
        # Update Hyper-connect Rests on line to match new cites (titles when known)
        # Will be fully synced by --sync-hc; do a quick rests rewrite here too.
        rests_fmt = "; ".join(ref(c, entries) if c in entries else c for c in new)
        text = re.sub(
            r"(?m)^-\s*\*\*Rests on:\*\*.*$",
            f"- **Rests on:** {rests_fmt}",
            text,
            count=1,
        )
        # BASE hinges = intersection with BASE_ORDER
        hinges = [c for c in new if c in BASE_ORDER]
        if hinges:
            hinge_line = ", ".join(hinges)
            if re.search(r"(?m)^-\s*\*\*BASE hinges:\*\*", text):
                text = re.sub(
                    r"(?m)^-\s*\*\*BASE hinges:\*\*.*$",
                    f"- **BASE hinges:** {hinge_line}",
                    text,
                    count=1,
                )
            else:
                # insert after Rests on
                text = re.sub(
                    r"(?m)(^-\s*\*\*Rests on:\*\*.*\n)",
                    r"\1" + f"- **BASE hinges:** {hinge_line}\n",
                    text,
                    count=1,
                )
        e["path"].write_text(text, encoding="utf-8")
        changed.append((eid, old, new))
    return changed


def compute_graph(entries):
    """deps[e] = live ids e rests on; supports[e] = live ids that rest on e."""
    live = set(entries)
    deps = {}
    for eid, e in entries.items():
        # Prefer cites+terms as authoritative after orphan fix; union hyper rests that are live
        d = []
        for x in list(e["cites"]) + list(e["terms"]):
            if x in live and x not in d:
                d.append(x)
        if e["hc"]:
            for x in e["hc"]["rests"]:
                if x in live and x not in d:
                    d.append(x)
        deps[eid] = d
    supports = defaultdict(list)
    for eid, ds in deps.items():
        for d in ds:
            if eid not in supports[d]:
                supports[d].append(eid)
    # stable order: BASE order first, then alpha
    def sort_ids(ids):
        base_rank = {b: i for i, b in enumerate(BASE_ORDER)}
        return sorted(ids, key=lambda x: (0, base_rank[x]) if x in base_rank else (1, x))

    for k in list(supports):
        supports[k] = sort_ids(supports[k])
    return deps, supports


def sync_hyper_connect(entries):
    """Rewrite Rests on / Supports lines from cites∪terms and reverse graph.
    Preserves Cap, Group, Live indexes, BASE hinges (recomputed).
    Does not change thesis body. BASE files: keep BASE supports named;
    expansion supports listed under Supports (expansion).
    """
    # reload fresh after orphan fixes
    entries = load_live()
    deps, supports = compute_graph(entries)
    changed = []
    base_set = set(BASE_ORDER)

    for eid, e in entries.items():
        text = e["path"].read_text(encoding="utf-8")
        if "## Hyper-connect" not in text:
            continue
        dlist = deps[eid]
        slist = supports.get(eid, [])

        if eid in base_set:
            # BASE: rests with titles; supports split BASE vs expansion
            rests_fmt = "; ".join(ref(x, entries) for x in dlist) if dlist else "(none — root)"
            base_sup = [x for x in slist if x in base_set]
            exp_sup = [x for x in slist if x not in base_set]
            if base_sup:
                base_sup_fmt = "; ".join(ref(x, entries) for x in base_sup)
            else:
                base_sup_fmt = "(none)"
            # Compact expansion supports (ids) — full titles in DEPS.md
            if exp_sup:
                exp_fmt = ", ".join(exp_sup)
                if len(exp_fmt) > 500:
                    exp_fmt = ", ".join(exp_sup[:40]) + f", … (+{len(exp_sup) - 40} more; see DEPS.md)"
            else:
                exp_fmt = "—"

            cap = BASE_CAPS.get(eid) or (e["cap"] or "pending")
            new_hc = (
                f"- **Rests on:** {rests_fmt}\n"
                f"- **Supports:** {base_sup_fmt}\n"
                f"- **Supports (expansion):** {exp_fmt}\n"
                f"- **Cap:** {cap}\n"
                f"- **Live chain:** [CHAIN.md](CHAIN.md) · [DEPS.md](DEPS.md) · [CAPS.md](CAPS.md)\n"
            )
        else:
            rests_fmt = "; ".join(ref(x, entries) for x in dlist) if dlist else "(none)"
            hinges = [x for x in dlist if x in base_set]
            hinge_fmt = ", ".join(hinges) if hinges else "—"
            # supports: prefer expansion peers with titles; include BASE only if somehow reverse
            if slist:
                sup_fmt = "; ".join(ref(x, entries) for x in slist)
                if len(sup_fmt) > 600:
                    sup_fmt = "; ".join(ref(x, entries) for x in slist[:25]) + f"; … (+{len(slist) - 25})"
            else:
                sup_fmt = "—"
            cap = e["cap"] or "pending; ≤ weakest scored BASE hinge among rests-on"
            group = e.get("group") or e["path"].parent.name
            new_hc = (
                f"- **Rests on:** {rests_fmt}\n"
                f"- **BASE hinges:** {hinge_fmt}\n"
                f"- **Supports (live):** {sup_fmt}\n"
                f"- **Cap:** {cap}\n"
                f"- **Group:** [{group}/](./)\n"
                f"- **Live indexes:** [expansion/INDEX.md](../INDEX.md), [KILNED.md](../../KILNED.md), "
                f"[CHAIN.md](../../CHAIN.md), [DEPS.md](../../DEPS.md)\n"
            )

        def repl_hc(match):
            return match.group(1) + new_hc

        new_text, n = re.subn(
            r"(## Hyper-connect\n)(.*?)(?=\n## |\Z)",
            repl_hc,
            text,
            count=1,
            flags=re.S,
        )
        if n and new_text != text:
            e["path"].write_text(new_text, encoding="utf-8")
            changed.append(eid)
    return changed, load_live()


def write_deps_md(entries):
    deps, supports = compute_graph(entries)
    lines = []
    lines.append("# DEPS — live dependency index (core v3)")
    lines.append("")
    lines.append("Generated by `tools/dep_check.py`. Live set only (BASE + kilned expansion).")
    lines.append("Parked ids are not nodes. Edges = frontmatter `cites` ∪ `terms` (plus live Hyper-connect rests).")
    lines.append("")
    lines.append("## Rules")
    lines.append("")
    lines.append("1. Every `cites` / `terms` / Hyper-connect rests-on id must be **live**.")
    lines.append("2. No cycles in the rests-on graph.")
    lines.append("3. Non-roots (`D-I`, `D-exist`, `A1` excepted) need ≥1 live rests-on.")
    lines.append("4. Cap documented on every entry (see [CAPS.md](CAPS.md)).")
    lines.append("5. BASE titles/ids/cap rules stay locked; Supports (expansion) is connective tissue only.")
    lines.append("")
    lines.append("## BASE reverse index (who rests on each)")
    lines.append("")
    for bid in BASE_ORDER:
        if bid not in entries:
            continue
        kids = supports.get(bid, [])
        lines.append(f"### {bid} — {entries[bid]['title']}")
        lines.append("")
        lines.append(f"- **Rests on:** {', '.join(deps.get(bid, [])) or '—'}")
        lines.append(f"- **Cap:** {BASE_CAPS.get(bid, entries[bid].get('cap') or '—')}")
        base_kids = [k for k in kids if k in set(BASE_ORDER)]
        exp_kids = [k for k in kids if k not in set(BASE_ORDER)]
        lines.append(f"- **Supports (BASE):** {', '.join(base_kids) or '—'}")
        lines.append(f"- **Supports (expansion, {len(exp_kids)}):** {', '.join(exp_kids) or '—'}")
        lines.append("")
    lines.append("## Expansion edges (compact)")
    lines.append("")
    lines.append("| Id | Rests on (live) | Supports (live) |")
    lines.append("|---|---|---|")
    for eid in sorted(entries):
        if eid in set(BASE_ORDER):
            continue
        d = ", ".join(deps.get(eid, [])) or "—"
        s = ", ".join(supports.get(eid, [])) or "—"
        lines.append(f"| {eid} | {d} | {s} |")
    lines.append("")
    (ROOT / "DEPS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return ROOT / "DEPS.md"


def write_caps_md(entries):
    lines = []
    lines.append("# CAPS — effective confidence rules (core v3)")
    lines.append("")
    lines.append("Generated by `tools/dep_check.py`. Definitions add no score.")
    lines.append("Only A1 is scored today (1.0). Everything else pending collider.")
    lines.append("")
    lines.append("## BASE (locked)")
    lines.append("")
    lines.append("| Entry | Cap rule |")
    lines.append("|---|---|")
    for bid in BASE_ORDER:
        lines.append(f"| {bid} | {BASE_CAPS.get(bid, '—')} |")
    lines.append("")
    lines.append("## Expansion (policy)")
    lines.append("")
    lines.append("Until the collider runs, every expansion entry:")
    lines.append("")
    lines.append("- **Cap ≤** weakest scored BASE hinge among its live rests-on.")
    lines.append("- Definitions / opens add no score of their own.")
    lines.append("- Conjecture-grade claims (esp. under P21) stay labeled as such.")
    lines.append("")
    lines.append("## Cap chains (load-bearing)")
    lines.append("")
    lines.append("```")
    lines.append("A1 (1.0)")
    lines.append(" └── A2 (own)")
    lines.append("      ├── A4 = min(rows, A2)")
    lines.append("      │    ├── P1 = min(A2, A3, A4)")
    lines.append("      │    │    └── P19 = min(P1, P3)")
    lines.append("      │    ├── P2 = min(A4 rows, A2)")
    lines.append("      │    │    └── P21 = min(P2, P3, A4)  [conjecture]")
    lines.append("      │    └── expansion under A4/P2/P21 …")
    lines.append("      └── P3 = min(A2, A5)")
    lines.append("           ├── P4 = min(A2, A5, P3)")
    lines.append("           ├── P5 = min(A2, A5, P3)")
    lines.append("           ├── P19 = min(P1, P3)")
    lines.append("           ├── P21 = min(P2, P3, A4)")
    lines.append("           └── expansion under P3/P4/P5 …")
    lines.append("A3 (own) ──► P1 + wholes expansion")
    lines.append("A5 (own) ──► P3, P4, P5 + necessity expansion")
    lines.append("```")
    lines.append("")
    (ROOT / "CAPS.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    return ROOT / "CAPS.md"


def refresh_chain_mermaid(entries):
    """Replace the Expansion dependency sketch mermaid with a real load-bearing graph."""
    chain_path = ROOT / "CHAIN.md"
    text = chain_path.read_text(encoding="utf-8")
    deps, supports = compute_graph(entries)

    # Pick load-bearing expansion nodes: those that cite P19/P21/P3/A3/A2/P2 or are supported by many
    focus = []
    for eid, e in entries.items():
        if eid in set(BASE_ORDER):
            continue
        d = set(deps.get(eid, []))
        if d & {"P19", "P21", "P3", "A3", "P2", "A5", "A1", "P4", "P5"}:
            # keep if also has supports or is a known hinge name
            if supports.get(eid) or eid.startswith("P-") or eid.startswith("OP-"):
                focus.append(eid)
    # Prefer a readable subset
    preferred = [
        "P-weakest-work-rules", "P-take-apart-test", "P-tumor-edge", "P-machine-not-self-producer",
        "P-corporation-without-feeling", "P-propaganda-bondage", "P-law-as-memory", "P-collective-freedom-rises",
        "P-choice-caused", "P-freer-knows-more-causes", "P-habit-can-bond", "D-clear-knowledge",
        "P-cult-bondage", "P-military-whole", "P-ai-collective", "P-open-science-society",
        "P-strong-whole-low-freedom", "P-weak-whole-high-freedom",
        "P-split-brain", "P-digital-A1", "P-copy-not-A1-transfer", "OP-feeling",
        "P-apparent-contingency", "P-title-claim",
    ]
    nodes = [x for x in preferred if x in entries]
    for x in focus:
        if x not in nodes and len(nodes) < 40:
            nodes.append(x)

    # BASE hub nodes in expansion graph
    hub = ["A2", "A3", "A4", "A5", "P2", "P3", "P4", "P19", "P21"]

    def mid(eid):
        return re.sub(r"[^A-Za-z0-9]", "", eid)[:40]

    lines = ["```mermaid", "graph TD"]
    for h in hub:
        if h in entries:
            lines.append(f'  {mid(h)}["{entries[h]["title"]} ({h})"]')
    for n in nodes:
        title = entries[n]["title"]
        if len(title) > 42:
            title = title[:40] + "…"
        lines.append(f'  {mid(n)}["{title} ({n})"]')
    # edges from deps
    seen = set()
    for n in nodes:
        for d in deps.get(n, []):
            if d in hub or d in nodes:
                edge = (d, n)
                if edge not in seen:
                    seen.add(edge)
                    lines.append(f"  {mid(d)} --> {mid(n)}")
    # hub internal (BASE spine already in earlier mermaid; light touch)
    for a, b in [("A2", "A4"), ("A4", "P2"), ("A5", "P3"), ("P3", "P4"), ("P3", "P19"), ("P2", "P21"), ("P3", "P21"), ("A3", "P19")]:
        edge = (a, b)
        if edge not in seen and a in entries and b in entries:
            seen.add(edge)
            lines.append(f"  {mid(a)} --> {mid(b)}")
    lines.append("```")
    new_block = "\n".join(lines)

    pattern = r"(### Expansion dependency sketch.*?\n\n)```mermaid\n.*?```"
    if re.search(pattern, text, re.S):
        text2 = re.sub(pattern, r"\1" + new_block, text, count=1, flags=re.S)
    else:
        # append before end
        text2 = text.rstrip() + "\n\n### Expansion dependency sketch (load-bearing)\n\n" + new_block + "\n"

    # Ensure DEPS/CAPS linked under Related
    if "DEPS.md" not in text2:
        text2 = text2.replace(
            "- [BUILD_LOG.md](BUILD_LOG.md)",
            "- [BUILD_LOG.md](BUILD_LOG.md)\n- [DEPS.md](DEPS.md) — live dependency index\n- [CAPS.md](CAPS.md) — cap rules\n- [tools/dep_check.py](tools/dep_check.py) — checker",
        )
    # Note under expansion section
    if "Dependency management" not in text2:
        text2 = text2.replace(
            "**Totals:** BASE **20** locked + live expansion **122** = **142** in play (parks separate).",
            "**Totals:** BASE **20** locked + live expansion **122** = **142** in play (parks separate).\n\n"
            "**Dependency management:** run `python3 tools/dep_check.py` (stdlib). "
            "Full reverse index: [DEPS.md](DEPS.md). Caps: [CAPS.md](CAPS.md).",
        )
    chain_path.write_text(text2, encoding="utf-8")
    return chain_path


def report(result, n_live):
    print(f"live entries: {n_live}")
    print(f"orphan cites: {len(result['orphan_cites'])}")
    for row in result["orphan_cites"]:
        print(f"  CITE {row[0]} -> {row[1]} ({row[2]})")
    print(f"orphan terms: {len(result['orphan_terms'])}")
    for row in result["orphan_terms"]:
        print(f"  TERM {row[0]} -> {row[1]} ({row[2]})")
    print(f"orphan rests: {len(result['orphan_rests'])}")
    for row in result["orphan_rests"]:
        print(f"  REST {row[0]} -> {row[1]} ({row[2]})")
    print(f"missing rests (non-root): {len(result['missing_rests'])}")
    for eid in result["missing_rests"]:
        print(f"  NO_DEPS {eid}")
    print(f"missing cap: {len(result['missing_cap'])}")
    for eid in result["missing_cap"]:
        print(f"  NO_CAP {eid}")
    print(f"missing hyper-connect: {len(result['missing_hc'])}")
    print(f"cycles: {len(result['cycles'])}")
    for c in result["cycles"]:
        print("  CYCLE " + " -> ".join(c))
    bad = (
        result["orphan_cites"]
        or result["orphan_terms"]
        or result["orphan_rests"]
        or result["missing_rests"]
        or result["missing_cap"]
        or result["missing_hc"]
        or result["cycles"]
    )
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--fix-orphans", action="store_true")
    ap.add_argument("--sync-hc", action="store_true")
    ap.add_argument("--write-docs", action="store_true")
    ap.add_argument("--json-summary", action="store_true")
    args = ap.parse_args()

    parked = load_parked_ids()
    entries = load_live()

    fixed = []
    if args.fix_orphans:
        fixed = fix_orphans(entries, parked)
        print(f"fixed orphans: {len(fixed)}")
        for eid, old, new in fixed:
            print(f"  {eid}: {old} -> {new}")
        entries = load_live()

    synced = []
    if args.sync_hc:
        synced, entries = sync_hyper_connect(entries)
        print(f"synced hyper-connect: {len(synced)}")

    if args.write_docs:
        entries = load_live()
        p1 = write_deps_md(entries)
        p2 = write_caps_md(entries)
        p3 = refresh_chain_mermaid(entries)
        print(f"wrote {p1.relative_to(ROOT)}")
        print(f"wrote {p2.relative_to(ROOT)}")
        print(f"refreshed {p3.relative_to(ROOT)}")

    entries = load_live()
    result = check(entries, parked)
    code = report(result, len(entries))
    if args.json_summary:
        import json
        print(json.dumps({
            "live": len(entries),
            "orphan_cites": result["orphan_cites"],
            "cycles": result["cycles"],
            "fixed": fixed,
            "synced": len(synced),
            "ok": code == 0,
        }, indent=2))
    sys.exit(code)


if __name__ == "__main__":
    main()
