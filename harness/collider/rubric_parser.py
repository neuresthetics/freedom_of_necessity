"""Strict parser for the judge's machine-readable verdict block.

Only the block between BEGIN_VERDICT and END_VERDICT (last occurrence) is read.
Scores must be exactly one of the five rubric values; verdicts must be exactly
one of the three falsifier verdicts. Anything else is recorded as "unparsed"
with the raw text kept. Nothing is guessed, rounded, or inferred from prose.
"""
import re

RUBRIC_VALUES = (0.85, 0.70, 0.50, 0.25, 0.10)
RUBRIC_LABELS = {
    0.85: "survives",
    0.70: "survives, damaged",
    0.50: "undecided",
    0.25: "refuted in part",
    0.10: "refuted",
}
VERDICTS = ("NOT TRIGGERED", "PARTLY TRIGGERED", "TRIGGERED")

_THINK_RE = re.compile(r"<think>.*?</think>", re.DOTALL | re.IGNORECASE)
_NUM_RE = re.compile(r"^(?:0?\.\d{1,2}|0\.\d{1,2}0*)$")
_LINE_RE = re.compile(r"^(VERDICT|SCORE)\s+([A-Za-z0-9_()\-]+)\s*[:=]\s*(.*?)\s*$")


def strip_think(text):
    """Remove <think>...</think> reasoning blocks some local models emit."""
    if text is None:
        return ""
    return _THINK_RE.sub("", text).strip()


def _clean(line):
    return line.strip().strip("*`_>").replace("**", "").replace("`", "").strip()


def parse_score(raw):
    """Return a rubric value, or None if raw is not exactly one of them."""
    s = _clean(raw)
    if not _NUM_RE.match(s):
        return None
    v = float(s)
    for r in RUBRIC_VALUES:
        if abs(v - r) < 1e-9:
            return r
    return None


def parse_verdict_value(raw):
    s = " ".join(_clean(raw).upper().split())
    return s if s in VERDICTS else None


def parse_judge(text, verdict_labels, score_keys):
    """Parse a judge reply.

    Returns {"block_found": bool, "verdicts": {label: entry}, "scores": {key: entry}}
    where entry = {"status": "parsed"|"unparsed"|"missing", "value": ..., "raw": ...}.
    """
    t = strip_think(text)
    out = {
        "block_found": False,
        "verdicts": {l: {"status": "missing", "value": None, "raw": None} for l in verdict_labels},
        "scores": {k: {"status": "missing", "value": None, "raw": None} for k in score_keys},
    }
    start = t.rfind("BEGIN_VERDICT")
    if start < 0:
        return out
    end = t.find("END_VERDICT", start)
    if end < 0:
        return out
    out["block_found"] = True
    seen = {}
    for line in t[start + len("BEGIN_VERDICT"):end].splitlines():
        m = _LINE_RE.match(_clean(line))
        if not m:
            continue
        kind, key, raw = m.group(1), m.group(2).upper(), m.group(3)
        if kind == "VERDICT" and key in out["verdicts"]:
            slot, val = out["verdicts"][key], parse_verdict_value(raw)
        elif kind == "SCORE" and key in out["scores"]:
            slot, val = out["scores"][key], parse_score(raw)
        else:
            continue
        ident = (kind, key)
        if ident in seen:
            if seen[ident] != val or val is None:
                slot.update(status="unparsed", value=None,
                            raw=(slot["raw"] or "") + " | " + raw.strip(),
                            note="conflicting duplicate lines")
            continue
        seen[ident] = val
        if val is None:
            slot.update(status="unparsed", value=None, raw=raw.strip())
        else:
            slot.update(status="parsed", value=val, raw=raw.strip())
    return out
