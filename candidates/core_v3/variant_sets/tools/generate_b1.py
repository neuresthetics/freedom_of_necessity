#!/usr/bin/env python3
"""Generate B0+B1 hardness-to-vary variant drafts (combined chain only).

Follows notes/2026-10-25-hardness-to-vary-draft-plan.md
Do NOT push. Do NOT dual-render. Do NOT mutate live core_v3 in place.
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import textwrap
from copy import deepcopy
from datetime import datetime
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # freedom_of_necessity
CORE = REPO / "candidates" / "core_v3"
VS = CORE / "variant_sets"
SET_ID = "set_20261025_B1"
SET = VS / SET_ID
GOLDEN = VS / "golden"
TECH_BASE = REPO / "drafts" / "verses_v3" / "technical" / "BASE.md"

BASE_ORDER = [
    "D-I", "D-exist", "A1", "A2", "D-work", "D-whole", "A3", "A4", "P1", "P2",
    "A5", "D-free", "P3", "D-affect", "D-bondage", "D-blessedness", "P4", "P5",
    "P19", "P21",
]
V_OF = {e: f"V{i:03d}" for i, e in enumerate(BASE_ORDER, 1)}
ODD_V = [e for e in BASE_ORDER if int(V_OF[e][1:]) % 2 == 1]  # D3
# D4 soft remap: props/axioms only (not pure defs / not pure roots as primary)
D4_IDS = ["A2", "A3", "A4", "A5", "P1", "P2", "P3", "P4", "P5", "P19"]
# D5 hard remap negative controls
D5_IDS = ["A1", "P3", "P1", "A4", "P5"]

# Defined / load-bearing terms — ban from D2 synonym swaps
BANNED = {
    "i", "exist", "exists", "existing", "existence", "whole", "work", "works",
    "affect", "affects", "freedom", "free", "freer", "bondage", "blessedness",
    "mind", "body", "organization", "cause", "caused", "causes", "degree",
    "member", "level", "self-production", "power", "acting", "necessity",
    "necessities", "activity", "thinking", "thinker", "nature", "control",
    "signal", "signaling", "memory", "cells", "cell", "human", "society",
    "collective", "strict", "definition", "axiom", "proposition",
}

# ---------------------------------------------------------------------------
# Claim anchors + paraphrases (D1 A/B) — keep ids/cites; same thesis
# ---------------------------------------------------------------------------
# Each value: (exact_substring_in_file, paraphrase_A, paraphrase_B)
# If exact missing, generator records error for that variant.

PARAPHRASE: dict[str, tuple[str, str, str]] = {
    "D-I": (
        '"I", used in a thought, names the thinker of that thought, if there is a thinker distinct from the thinking, and otherwise the thinking itself.',
        '"I", said inside a thought, picks out the one who thinks that thought when thinker and thinking come apart, and otherwise picks out the thinking.',
        'In a thought, the word "I" refers to the thinker of that thought if such a thinker is distinct from the thinking; if not, it refers to the thinking itself.',
    ),
    "D-exist": (
        "An activity *exists* at a time when it is going on at that time.",
        "An activity *exists* at a time just when it is underway at that time.",
        "For activities, to *exist* at a time is nothing more than to be going on then.",
    ),
    "A1": (
        "**I exist** *(root, id: A1)*.",
        "**I exist** *(root, id: A1)* — the root claim, unchanged in force.",
        "**I exist** *(root, id: A1)*.",  # B keeps surface; surrounding frame may shift via second replace below
    ),
    "A2": (
        "**Axiom.** I am a human body made of cells, and my mind is that same body's organization described in the first person.",
        "**Axiom.** This thinking goes with a human body of cells; my mind is that body's organization told in the first person.",
        "**Axiom.** I am this cell-built human body, and mind here means that same organization under a first-person description.",
    ),
    "D-work": (
        "A *work* of a thing is an activity of that thing which (a) contributes to keeping the thing's *organization* going, and (b) is carried out by structures that the thing's organization itself produces or maintains.",
        "A *work* of a thing is an activity that (a) helps keep that thing's *organization* going and (b) is done by structures the organization itself produces or keeps up.",
        "Call *work* any activity of a thing that both sustains its *organization* and is performed by structures that organization makes or maintains.",
    ),
    "D-whole": (
        "For any finite thing X and each of the seven works (D-work, Definition 6), X's *grade* on that work is:",
        "Take any finite thing X and any one of the seven works (D-work, Definition 6). X's *grade* on that work is:",
        "Given finite X and each work among the seven (D-work, Definition 6), the *grade* of X on that work is:",
    ),
    "A3": (
        "**Axiom.** The seven works sort things the way self-production does. A thing that produces itself (D-whole, Definition 11) performs all seven as one; a thing that lasts without producing itself fails at least one.",
        "**Axiom.** Ranking by the seven works tracks self-production: what produces itself (D-whole, Definition 11) does all seven as one; what merely lasts without self-production misses at least one.",
        "**Axiom.** The seven works order things as self-production does — full self-producers (D-whole, Definition 11) perform all seven together; non-self-producers that only last fail at least one.",
    ),
    "A4": (
        "**Axiom.** The society I live in is a whole to a degree, judged one work at a time: it performs each of the seven works as one, at least in part, and I am one of its members.",
        "**Axiom.** The society I inhabit is a whole by degrees, scored work by work: it carries out each of the seven works jointly, at least partly, and I am a member of it.",
        "**Axiom.** My society is a graded whole under the seven works: for each work it acts as one to some extent, and I count among its members.",
    ),
    "P1": (
        "**Proposition 1.** I am a whole at one level and a part at the next.",
        "**Proposition 1.** At one level I am a whole; at the next level I am a part.",
        "**Proposition 1.** I count as a whole on one level and as a part on the level above it.",
    ),
    "P2": (
        "**Proposition 2.** A collective mind, in the sense defined here, happens in the society I live in.",
        "**Proposition 2.** In the society's sense defined here, a collective mind occurs where I live.",
        "**Proposition 2.** The society I live in hosts a collective mind under this entry's definition.",
    ),
    "A5": (
        "**Axiom.** Every event is caused, a choice included.",
        "**Axiom.** Nothing happens without a cause; choices are not exempt.",
        "**Axiom.** Each event has a cause — including every choice.",
    ),
    "D-free": (
        "A thing is *free* in the strict sense when it exists solely by the necessity of its own nature, and when its action is determined by itself alone (E1D7).",
        "In the strict sense a thing is *free* only if it exists by its own nature's necessity alone and its action is fixed by itself alone (E1D7).",
        "Strict *freedom* (E1D7): existence solely from the necessity of one's own nature, action determined by oneself alone.",
    ),
    "P3": (
        "**Proposition 3.** Freedom, in the book's degree sense (D-free, Definition 15), is compatible with every event being caused (A5). The body this thinking goes with (A1, A2 as scored) is freer to the degree that what it does follows from its own organization and from clear knowledge of the causes of what it does. Freedom does not require that the agent could have done otherwise, given all that came before.",
        "**Proposition 3.** Degree-freedom (D-free, Definition 15) fits with universal causation (A5). The body this thinking goes with (A1, A2 as scored) is freer insofar as its doings follow from its own organization and from clear knowledge of their causes. Could-have-done-otherwise, given the total prior state, is not required.",
        "**Proposition 3.** Under D-free Definition 15, freedom-by-degree is compatible with A5 (every event caused). For the body this thinking goes with (A1, A2 scored), freer means: action from own organization plus clear knowledge of causes. Libertarian could-have-done-otherwise is not part of the claim.",
    ),
    "D-affect": (
        "An *affect* is a change in an organization's *power of acting*, together with the ideas of that change.",
        "An *affect* is a shift in an organization's *power of acting*, plus the ideas of that shift.",
        "Call *affect* any change of *power of acting* in an organization, taken with the ideas of that change.",
    ),
    "D-bondage": (
        "*Bondage* (servitude) is the condition in which what an agent does follows from outside causes or from affects whose causes are unclear — the inverse of degree-freedom (*Freedom, strict and by degree*, D-free, Definition 15).",
        "*Bondage* (servitude) names the state where an agent's doings track outside causes or unclear affects — the downside inverse of degree-freedom (D-free, Definition 15).",
        "*Bondage* is servitude: action from outer causes or from affects with unclear causes; it is degree-freedom (D-free, Definition 15) read downward.",
    ),
    "D-blessedness": (
        "*Blessedness*, in this chain's working sense, is power of acting (*Affect, and change of power*, D-affect) as it rises with degree-freedom (*Freedom, strict and by degree*, D-free) — not a prize paid after virtue.",
        "*Blessedness* here means power of acting (D-affect) rising with degree-freedom (D-free), not a later reward for virtue.",
        "In this chain, *blessedness* is the rising power of acting itself (D-affect with D-free), never a payoff added afterward.",
    ),
    "P4": (
        "**Proposition 4.** A finite agent (the body this thinking goes with, as *A human body, and its mind*, A2, is scored) is in *bondage* to the degree that what it does follows from causes outside its own organization, or from affects whose causes remain unclear.",
        "**Proposition 4.** The finite agent scored under A2 (the body this thinking goes with) is in *bondage* insofar as its actions follow outer causes or unclear affects.",
        "**Proposition 4.** Bondage rises for the A2-scored body when doings issue from outside its organization or from affects with causes still unclear.",
    ),
    "P5": (
        "**Proposition 5.** Blessedness, in the book's working sense, is not a reward added after freedom, but the power of acting itself (*Affect, and change of power*, D-affect) as that power rises with freedom in *Freedom, strict and by degree* (D-free) / *Freedom by degrees under necessity* (P3).",
        "**Proposition 5.** Blessedness is not a prize after freedom; it is power of acting (D-affect) rising with degree-freedom (D-free) under P3.",
        "**Proposition 5.** Working blessedness = the power of acting itself (D-affect) as freedom (D-free, P3) rises — never a deferred reward.",
    ),
    "P19": (
        "**Proposition 19.** The degree of being a whole (*Whole, degree, member, level, self-production, sameness*, D-whole; *A whole at one level, a part at the next*, P1) and the degree of freedom (*Freedom, strict and by degree*, D-free; *Freedom by degrees under necessity*, P3) track each other only loosely.",
        "**Proposition 19.** Whole-degree (D-whole, P1) and freedom-degree (D-free, P3) move together only loosely — not as one scale.",
        "**Proposition 19.** How whole something is (D-whole; P1) does not lockstep with how free it is (D-free; P3); the coupling is loose.",
    ),
    "P21": (
        "**Proposition 21 (conjecture-grade).** The society of *The society I live in is a whole to a degree* (A4), with collective control as in *A collective mind happens* (P2), can be freer in the degree sense (P3) as what it does follows from its own organization and from clearer common knowledge of causes — without any claim that the society feels (feeling not required; parked P18 folded here).",
        "**Proposition 21 (conjecture-grade).** A4's society, with P2's collective control, can rise in P3 degree-freedom when action follows its organization and clearer shared knowledge of causes — no claim that society feels (feeling not required; parked P18 folded here).",
        "**Proposition 21 (conjecture-grade).** Society (A4) under collective control (P2) may be freer by P3 when doings track own organization and clearer common causal knowledge; feeling is not required (parked P18 folded here).",
    ),
}

# Extra A1 D1-B: paraphrase a non-root frame sentence while keeping "**I exist**"
A1_FRAME_B = (
    "To doubt that I exist is to be doubting. The doubting is going on, so something exists: at the least, the doubting itself.",
    "Doubt that I exist is already doubting; that doubting is going on, so at least the doubting exists.",
)

# Soft synonym map (D2) — only non-banned content words
SYNONYMS = {
    "sentence": "statement",
    "claim": "assertion",
    "certain": "sure",
    "certainty": "sureness",
    "doubt": "hesitation",  # careful — may hit Descartes; still surface
    "doubting": "hesitating",
    "revised": "altered",
    "evidence": "grounds",
    "reader": "audience",
    "wording": "phrasing",
    "snapshot": "freeze-frame",
    "seed-spine": "seed-chain",
    "pending": "awaiting",
    "compatible": "consistent",
    "require": "demand",
    "requires": "demands",
    "required": "demanded",
    "follows": "issues",
    "clear": "plain",
    "unclear": "opaque",
    "outside": "external",
    "inverse": "counterpart-down",
    "reward": "prize",
    "loosely": "weakly",
    "conjecture-grade": "hypothesis-grade",
}

# Soft remap suggestions (D4): replace one cite with a "sibling-ish" id
# Expect many dep_check / meaning issues — that is the measurement.
SOFT_REMAP: dict[str, tuple[str, str, str]] = {
    # id: (from_cite, to_cite, note)
    "A2": ("A1", "P3", "swap subject-root cite toward later freedom prop"),
    "A3": ("D-whole", "P1", "terms/dep: point model axiom at later prop"),
    "A4": ("A2", "P21", "society axiom cites conjecture instead of A2"),
    "A5": ("D-exist", "D-free", "causation axiom leans on freedom def"),
    "P1": ("A3", "P19", "levels prop cites anti-collapse instead of A3"),
    "P2": ("A4", "P5", "collective mind cites blessedness"),
    "P3": ("A5", "P4", "freedom prop cites bondage prop (near-cycle risk)"),
    "P4": ("P3", "P21", "bondage cites society conjecture"),
    "P5": ("P3", "A3", "blessedness cites works-sort axiom"),
    "P19": ("P1", "A1", "anti-collapse cites root instead of P1"),
}

# Hard remap (D5): drop required rest or point at parked
HARD_REMAP: dict[str, dict] = {
    "A1": {
        "mode": "parked_cite_clear_terms",
        "add_cite": "PR1",
        "note": "hard: cite parked PR1 + clear terms (orphan expected)",
    },
    "P3": {
        "mode": "parked_cite",
        "add_cite": "D-Nature",
        "note": "cite parked D-Nature (orphan)",
    },
    "P1": {
        "mode": "strip_all_rests",
        "note": "hard: clear cites+terms+HC rests (missing rests expected)",
    },
    "A4": {
        "mode": "parked_cite",
        "add_cite": "P18",
        "note": "cite parked P18 (orphan)",
    },
    "P5": {
        "mode": "strip_all_rests",
        "note": "hard: clear cites+terms+HC rests (missing rests expected)",
    },
}


def sh(*args: str, cwd: Path | None = None) -> str:
    r = subprocess.run(args, cwd=cwd or REPO, capture_output=True, text=True)
    return (r.stdout or "") + (r.stderr or "")


def git_sha() -> str:
    return sh("git", "rev-parse", "HEAD").strip()


def freeze_golden(source_sha: str, snapshot_sha: str) -> None:
    g_ent = GOLDEN / "entries"
    g_tech = GOLDEN / "technical"
    g_ent.mkdir(parents=True, exist_ok=True)
    g_tech.mkdir(parents=True, exist_ok=True)
    for eid in BASE_ORDER:
        shutil.copy2(CORE / f"{eid}.md", g_ent / f"{eid}.md")
    shutil.copy2(TECH_BASE, g_tech / "BASE.md")
    shutil.copy2(CORE / "BASE.md", GOLDEN / "BASE.md")
    shutil.copy2(CORE / "CAPS.md", GOLDEN / "CAPS.md")
    (GOLDEN / "SOURCE.md").write_text(
        textwrap.dedent(
            f"""\
            # Golden combined BASE (analysis control)

            **Frozen:** {datetime.now().strftime("%Y-%m-%d %H:%M")} America/Los_Angeles (PDT)
            **Live tip SHA:** `{source_sha}`
            **Snapshot tag `core-v3-snapshot-v1`:** `{snapshot_sha}`
            **Unit:** combined chain only — BASE entry files + technical BASE face
            **Not included:** poetic track (post-winner dual render only)

            ## Contents
            - `entries/` — {len(BASE_ORDER)} BASE files (D-I … P21)
            - `technical/BASE.md` — verses V001–V020 technical face
            - `BASE.md`, `CAPS.md` — spine + cap rules pointers

            Live `candidates/core_v3/` was **not** mutated to build this freeze.
            """
        )
    )


def load_entry(eid: str) -> str:
    return (GOLDEN / "entries" / f"{eid}.md").read_text(encoding="utf-8")


def replace_once(text: str, old: str, new: str) -> tuple[str, bool]:
    if old not in text:
        return text, False
    return text.replace(old, new, 1), True


def apply_synonyms(text: str) -> tuple[str, list[str]]:
    """Word-boundary synonym swap; skip banned lemmas; skip fenced/frontmatter ids."""
    # Only transform body after frontmatter
    if not text.startswith("---"):
        body_start = 0
        head, body = "", text
    else:
        parts = text.split("---", 2)
        head = "---" + parts[1] + "---"
        body = parts[2]
        body_start = 1

    changed: list[str] = []

    def repl_word(m: re.Match) -> str:
        w = m.group(0)
        low = w.lower()
        if low in BANNED:
            return w
        if low in SYNONYMS:
            syn = SYNONYMS[low]
            # preserve caps
            if w.isupper():
                out = syn.upper()
            elif w[0].isupper():
                out = syn[0].upper() + syn[1:]
            else:
                out = syn
            if out != w:
                changed.append(f"{w}→{out}")
            return out
        return w

    # Avoid replacing inside **Rests on** / id tokens like A1, D-free by only
    # swapping whitelist synonyms via word boundary on letters.
    new_body = re.sub(r"\b[A-Za-z][A-Za-z\-]*\b", repl_word, body)
    # Cap number of swaps for readability signal
    if len(changed) > 40:
        # re-apply more conservatively: first 25 unique only
        pass
    return head + new_body if body_start else new_body, changed


def reorder_clauses(text: str, eid: str) -> tuple[str, str]:
    """Reorder demonstration steps or major **Why/** sections."""
    # Prefer numbered demonstration steps "1. …\n2. …"
    dem = re.search(
        r"(\*\*Demonstration\.\*\*\n\n)((?:\d+\.\s[\s\S]*?)(?:\n\n|\n(?=\*\*)|\Z))",
        text,
    )
    if dem:
        prefix, block = dem.group(1), dem.group(2)
        steps = re.findall(r"(\d+\.\s[\s\S]*?)(?=\n\d+\.\s|\Z)", block)
        if len(steps) >= 3:
            # rotate: last -> first
            new_steps = [steps[-1]] + steps[:-1]
            # renumber
            renum = []
            for i, s in enumerate(new_steps, 1):
                renum.append(re.sub(r"^\d+\.", f"{i}.", s, count=1))
            new_block = "".join(renum)
            if not new_block.endswith("\n"):
                new_block += "\n"
            return text[: dem.start()] + prefix + new_block + text[dem.end() :], "rotated demonstration steps"

    # Else: swap first two **Section** blocks after title (Why / Axiom|Proposition)
    parts = re.split(r"(?=\n\*\*[A-Z][^*]{2,80}\*\*)", text)
    if len(parts) >= 4:
        # parts[0] = preamble; swap parts[1] and parts[2] if both are sections
        parts[1], parts[2] = parts[2], parts[1]
        return "".join(parts), "swapped first two **section** blocks"
    # Fallback: reverse paragraph order in body
    if text.startswith("---"):
        fm, body = text.split("---", 2)[1], text.split("---", 2)[2]
        paras = re.split(r"\n\n+", body.strip())
        if len(paras) >= 4:
            mid = paras[1:-1]
            mid = list(reversed(mid))
            new_body = "\n\n".join([paras[0]] + mid + [paras[-1]]) + "\n"
            return "---" + fm + "---\n\n" + new_body, "reversed middle paragraphs"
    return text, "NO_REORDER_APPLIED"


def parse_fm_list(fm: str, key: str) -> list[str]:
    m = re.search(rf"^{key}:\s*\[(.*?)\]", fm, re.M)
    if not m:
        return []
    inner = m.group(1).strip()
    if not inner:
        return []
    return [x.strip() for x in inner.split(",") if x.strip()]


def set_fm_list(text: str, key: str, values: list[str]) -> str:
    parts = text.split("---", 2)
    fm = parts[1]
    new_val = "[" + ", ".join(values) + "]"
    if re.search(rf"^{key}:\s*\[", fm, re.M):
        fm2 = re.sub(rf"^{key}:\s*\[.*?\]", f"{key}: {new_val}", fm, count=1, flags=re.M)
    else:
        fm2 = fm.rstrip() + f"\n{key}: {new_val}\n"
    return "---" + fm2 + "---" + parts[2]


def apply_soft_remap(text: str, eid: str) -> tuple[str, str]:
    frm, to, note = SOFT_REMAP[eid]
    parts = text.split("---", 2)
    fm = parts[1]
    cites = parse_fm_list(fm, "cites")
    terms = parse_fm_list(fm, "terms")
    where = None
    if frm in cites:
        cites = [to if x == frm else x for x in cites]
        text = set_fm_list(text, "cites", cites)
        where = "cites"
    elif frm in terms:
        terms = [to if x == frm else x for x in terms]
        text = set_fm_list(text, "terms", terms)
        where = "terms"
    else:
        # force into cites
        cites = cites + [to]
        text = set_fm_list(text, "cites", cites)
        where = "cites(appended)"
    # Also tweak Hyper-connect Rests on line if present (structure signal)
    text2, ok = replace_once(
        text,
        f"({frm})",
        f"({to})",
    )
    if ok:
        text = text2
    return text, f"{where}: {frm}→{to}; {note}"


def apply_hard_remap(text: str, eid: str) -> tuple[str, str]:
    spec = HARD_REMAP[eid]
    mode = spec["mode"]
    if mode == "clear_terms":
        text = set_fm_list(text, "terms", [])
        return text, spec["note"]
    if mode == "parked_cite_clear_terms":
        text = set_fm_list(text, "terms", [])
        cites = parse_fm_list(text.split("---", 2)[1], "cites")
        add = spec["add_cite"]
        if add not in cites:
            cites.append(add)
        text = set_fm_list(text, "cites", cites)
        return text, spec["note"]
    if mode == "strip_all_rests":
        text = set_fm_list(text, "cites", [])
        text = set_fm_list(text, "terms", [])
        text = re.sub(
            r"(- \*\*Rests on:\*\*).*",
            r"\1 (stripped for D5 hard remap)",
            text,
            count=1,
        )
        return text, spec["note"]
    if mode == "clear_cites":
        text = set_fm_list(text, "cites", [])
        text = re.sub(
            r"(- \*\*Rests on:\*\*).*",
            r"\1 (stripped for D5 hard remap)",
            text,
            count=1,
        )
        return text, spec["note"]
    if mode == "drop_cite":
        cites = parse_fm_list(text.split("---", 2)[1], "cites")
        drop = spec["drop"]
        cites = [c for c in cites if c != drop]
        text = set_fm_list(text, "cites", cites)
        return text, spec["note"]
    if mode == "parked_cite":
        cites = parse_fm_list(text.split("---", 2)[1], "cites")
        add = spec["add_cite"]
        if add not in cites:
            cites.append(add)
        text = set_fm_list(text, "cites", cites)
        return text, spec["note"]
    return text, "unknown hard mode"


def tech_face_snippet(eid: str) -> str:
    """Pull V### section from technical BASE for golden pairing note."""
    raw = (GOLDEN / "technical" / "BASE.md").read_text(encoding="utf-8")
    v = V_OF[eid]
    m = re.search(
        rf"(## {v} · `{re.escape(eid)}`[\s\S]*?)(?=\n---\n\n## V|\Z)",
        raw,
    )
    return m.group(1).strip() if m else ""


def write_variant_md(
    path: Path,
    *,
    eid: str,
    dim: str,
    n: str,
    note: str,
    body: str,
    source_sha: str,
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = textwrap.dedent(
        f"""\
        <!--
        variant_meta:
          id: {eid}
          V: {V_OF[eid]}
          dim: {dim}
          n: {n}
          band: B1
          source_sha: {source_sha}
          note: {note.replace(chr(10), ' ')}
          unit: combined_chain
        -->
        """
    )
    path.write_text(header + body, encoding="utf-8")


def run_dep_check_with_variant(eid: str, variant_body: str, work: Path) -> tuple[int, str]:
    """Swap one entry in work tree, run that tree's dep_check, restore."""
    target = work / f"{eid}.md"
    # strip variant header comment for live-shaped file
    body = variant_body
    if body.lstrip().startswith("<!--"):
        body = re.sub(r"^<!--.*?-->\n?", "", body, count=1, flags=re.S)
    target.write_text(body, encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(work / "tools" / "dep_check.py")],
        cwd=work,
        capture_output=True,
        text=True,
    )
    out = (proc.stdout or "") + (proc.stderr or "")
    # restore golden entry
    shutil.copy2(GOLDEN / "entries" / f"{eid}.md", target)
    return proc.returncode, out


def main() -> int:
    source_sha = git_sha()
    snap = sh("git", "rev-parse", "core-v3-snapshot-v1").strip()

    print("Freezing golden…")
    freeze_golden(source_sha, snap)

    # Fresh set dir
    if SET.exists():
        shutil.rmtree(SET)
    (SET / "variants").mkdir(parents=True)
    (SET / "reports" / "dep_check").mkdir(parents=True)
    (SET / "winner").mkdir(parents=True)
    (SET / "dual_render" / "technical").mkdir(parents=True)
    (SET / "dual_render" / "poetic").mkdir(parents=True)
    (SET / "dual_render" / "README.md").write_text(
        "# dual_render — empty until single winner is picked\n\n"
        "Do not generate technical/poetic tracks here before winner selection.\n"
    )

    manifest = {
        "set_id": SET_ID,
        "created": datetime.now().isoformat(timespec="seconds"),
        "timezone": "America/Los_Angeles",
        "source_sha": source_sha,
        "snapshot_tag": "core-v3-snapshot-v1",
        "snapshot_sha": snap,
        "band": ["B0", "B1"],
        "unit": "combined_chain",
        "plan": "notes/2026-10-25-hardness-to-vary-draft-plan.md",
        "defaults_for_open_questions": {
            "scope": "B0+B1 only (~85)",
            "folder": "candidates/core_v3/variant_sets/",
            "meaning_drift_judge": "TBD — Jason skim; second-model pass parked",
            "d4_soft": "free enough to fail often",
            "v013_jason_lines": "freeze verbatim in winner; D1 may rephrase frame but keep CHDO/necessity thesis",
            "collider": "skip this round",
            "push": "local only until Jason says push",
            "winner_grain": "one winner for whole BASE band (later)",
        },
        "variants": [],
    }

    # Prepare work tree once (full core copy for dep_check)
    work = Path("/tmp/fon_core_v3_htv_work")
    if work.exists():
        shutil.rmtree(work)
    print("Copying core_v3 → work tree for dep_check…")
    shutil.copytree(
        CORE,
        work,
        ignore=shutil.ignore_patterns("variant_sets", "__pycache__", "*.pyc"),
    )

    # Sanity: work dep_check clean
    proc = subprocess.run(
        [sys.executable, str(work / "tools" / "dep_check.py")],
        capture_output=True,
        text=True,
    )
    (SET / "reports" / "dep_check" / "00_worktree_baseline.txt").write_text(
        f"exit={proc.returncode}\n\n{(proc.stdout or '')}{(proc.stderr or '')}"
    )
    if proc.returncode != 0:
        print("BASELINE dep_check FAILED in work tree — abort")
        print(proc.stdout, proc.stderr)
        return 1

    rows = []

    def record(eid, dim, n, note, body, applied_ok=True):
        vpath = SET / "variants" / eid / f"{dim}_{n}.md"
        write_variant_md(
            vpath, eid=eid, dim=dim, n=n, note=note, body=body, source_sha=source_sha
        )
        # Also write technical face sidecar for D1 (combined face), surface-only note
        if dim == "D1":
            tech = tech_face_snippet(eid)
            side = SET / "variants" / eid / f"{dim}_{n}.technical_face.md"
            side.write_text(
                f"# Technical face pair — {V_OF[eid]} · `{eid}` · {dim}_{n}\n\n"
                f"Note: {note}\n\n"
                f"Golden technical verse (control; entry body is what dep_check sees):\n\n"
                f"{tech}\n",
                encoding="utf-8",
            )
        code, out = run_dep_check_with_variant(eid, body, work)
        logp = SET / "reports" / "dep_check" / f"{eid}_{dim}_{n}.txt"
        logp.write_text(f"exit={code}\nnote={note}\napplied_ok={applied_ok}\n\n{out}")
        row = {
            "id": eid,
            "V": V_OF[eid],
            "dim": dim,
            "n": n,
            "path": str(vpath.relative_to(VS)),
            "dep_check_exit": code,
            "note": note,
            "applied_ok": applied_ok,
            "band": "B0" if eid == "A1" and dim in {"D1", "D5"} else "B1",
        }
        manifest["variants"].append(row)
        rows.append(row)
        flag = "FAIL" if code != 0 else "ok"
        print(f"  [{flag}] {eid} {dim}_{n} exit={code} — {note[:60]}")

    print("Generating D1 paraphrases (×2)…")
    for eid in BASE_ORDER:
        raw = load_entry(eid)
        if eid not in PARAPHRASE:
            record(eid, "D1", "A", "NO_PARAPHRASE_DEFINED", raw, False)
            record(eid, "D1", "B", "NO_PARAPHRASE_DEFINED", raw, False)
            continue
        old, a, b = PARAPHRASE[eid]
        body_a, ok_a = replace_once(raw, old, a)
        body_b, ok_b = replace_once(raw, old, b)
        if eid == "A1":
            # D1-B: keep "**I exist**" claim; paraphrase certainty frame
            body_b, ok_b2 = replace_once(raw, A1_FRAME_B[0], A1_FRAME_B[1])
            ok_b = ok_b2
            note_b = "A1 frame paraphrase; root claim 'I exist' held fixed"
        else:
            note_b = "paraphrase B; cites/terms/ids untouched"
        record(eid, "D1", "A", "paraphrase A; cites/terms/ids untouched" if ok_a else f"ANCHOR_MISS: {old[:60]}", body_a, ok_a)
        record(eid, "D1", "B", note_b if ok_b else f"ANCHOR_MISS", body_b, ok_b)

    print("Generating D2 synonym swaps…")
    for eid in BASE_ORDER:
        raw = load_entry(eid)
        body, ch = apply_synonyms(raw)
        note = f"synonym swaps ({len(ch)}): " + ", ".join(ch[:12]) + ("…" if len(ch) > 12 else "")
        if not ch:
            note = "synonym: no whitelist hits (low surface malleability)"
        record(eid, "D2", "A", note, body, True)

    print("Generating D3 clause reorder (odd V)…")
    for eid in ODD_V:
        raw = load_entry(eid)
        body, note = reorder_clauses(raw, eid)
        record(eid, "D3", "A", note, body, note != "NO_REORDER_APPLIED")

    print("Generating D4 soft remaps…")
    for eid in D4_IDS:
        raw = load_entry(eid)
        body, note = apply_soft_remap(raw, eid)
        record(eid, "D4", "A", note, body, True)

    print("Generating D5 hard remaps…")
    for eid in D5_IDS:
        raw = load_entry(eid)
        body, note = apply_hard_remap(raw, eid)
        record(eid, "D5", "A", note, body, True)

    # B0 explicit marker file
    (SET / "variants" / "A1" / "B0_README.md").write_text(
        "# B0 — A1 sanity\n\n"
        "B0 uses A1's D1_A/D1_B (root claim must hold) and D5_A (must fail lint or be flagged).\n"
        "See reports/dep_check/A1_*.txt and reports/compare.md.\n"
    )

    manifest["counts"] = {
        "total_variants": len(rows),
        "by_dim": {},
        "dep_check_fail": sum(1 for r in rows if r["dep_check_exit"] != 0),
        "dep_check_pass": sum(1 for r in rows if r["dep_check_exit"] == 0),
        "applied_ok_false": sum(1 for r in rows if not r["applied_ok"]),
    }
    for r in rows:
        manifest["counts"]["by_dim"][r["dim"]] = manifest["counts"]["by_dim"].get(r["dim"], 0) + 1

    (SET / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")

    # compare.md skeleton with hardness table (lint-only; meaning drift TBD)
    lines = [
        f"# Compare — {SET_ID} (combined chain)",
        "",
        f"**Source SHA:** `{source_sha}`  ",
        f"**Snapshot:** `core-v3-snapshot-v1` = `{snap}`  ",
        f"**Variants:** {len(rows)}  ",
        f"**dep_check fail:** {manifest['counts']['dep_check_fail']}  ",
        f"**dep_check pass:** {manifest['counts']['dep_check_pass']}  ",
        "",
        "Meaning-drift Y/N is **TBD** (Jason skim or later judge). Dual render not started.",
        "",
        "## Per-variant lint",
        "",
        "| V | Id | Dim | n | dep_check | applied | Note |",
        "|---|---|---|---|---|---|---|",
    ]
    for r in rows:
        lines.append(
            f"| {r['V']} | `{r['id']}` | {r['dim']} | {r['n']} | "
            f"{r['dep_check_exit']} | {'Y' if r['applied_ok'] else 'N'} | {r['note'][:70].replace('|','/')} |"
        )

    # hardness by id (lint-break rate only for now)
    lines += ["", "## Hardness (lint-break rate; meaning drift pending)", "",
              "| Id | V | n_var | n_fail | hardness_lint |",
              "|---|---|---|---|---|"]
    by_id: dict[str, list] = {}
    for r in rows:
        by_id.setdefault(r["id"], []).append(r)
    for eid in BASE_ORDER:
        rs = by_id.get(eid, [])
        if not rs:
            continue
        fails = sum(1 for r in rs if r["dep_check_exit"] != 0)
        h = fails / len(rs) if rs else 0
        lines.append(f"| `{eid}` | {V_OF[eid]} | {len(rs)} | {fails} | {h:.2f} |")

    lines += [
        "",
        "## Special rows",
        "",
        "### A1 (B0)",
        "- D1 must keep claim **I exist**; lint should pass; meaning drift if claim altered.",
        "- D5 should fail or show missing-rest / structure break.",
        "",
        "### V013 · P3 (Jason lines)",
        "- Combined-chain D1 paraphrases keep CHDO-not-required + freedom-under-necessity thesis.",
        "- Verbatim poetic Jason lines (v12 143/144) are **not** in this analysis arm; freeze at dual-render from winner.",
        "",
        "## False soft (lint OK, meaning drift)",
        "",
        "_None flagged yet — awaiting human/model meaning pass._",
        "",
        "## Winner",
        "",
        "_Not picked this turn. See `winner/` (empty) and plan §4._",
        "",
    ]
    (SET / "reports" / "compare.md").write_text("\n".join(lines) + "\n")

    # Set README
    (SET / "README.md").write_text(
        textwrap.dedent(
            f"""\
            # {SET_ID} — hardness-to-vary drafts (B0+B1)

            **Status:** first variant batch generated for analysis. **No winner yet. No dual render yet.**
            **Unit:** one combined technical+structure chain (entry files + technical face).  
            **Plan:** [notes/2026-10-25-hardness-to-vary-draft-plan.md](../../../../notes/2026-10-25-hardness-to-vary-draft-plan.md)

            ## Source

            | Field | Value |
            |---|---|
            | Live tip | `{source_sha}` |
            | Tag `core-v3-snapshot-v1` | `{snap}` |
            | Golden | [`../golden/`](../golden/) |
            | Manifest | [`manifest.json`](manifest.json) |
            | Lint vs meaning table | [`reports/compare.md`](reports/compare.md) |

            ## Counts

            - **Variants:** {len(rows)}
            - **By dim:** {json.dumps(manifest['counts']['by_dim'])}
            - **dep_check pass / fail:** {manifest['counts']['dep_check_pass']} / {manifest['counts']['dep_check_fail']}

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
            """
        )
    )

    print(f"Done. {len(rows)} variants. Manifest → {SET / 'manifest.json'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
