#!/usr/bin/env python3
"""Freedom collider: a truly separated, judged run of the freedom candidates.

Python 3 standard library only. Every model call is a fresh, stateless HTTP
request carrying only what that role is allowed to see:

  side_L, side_H, side_B, control_bad_B : own saved prompt file + frozen entries
  judge (main)                          : question, entries, theses, falsifiers,
                                          side outputs L, H, B, rubric
  judge (control)                       : the bad entry alone + its falsifier + rubric
  judge_swap                            : main judge input relabeled X/Y/Z and
                                          reordered per swap_map.txt

Before any model call the run spec (RUN_SPEC.md, spec.json, INPUTS.sha256,
INPUT_COMMIT) is written to candidates/freedom/run_<YYYY-MM-DD_HHMM>/ so it can
be committed first. See README.md.
"""
import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from rubric_parser import RUBRIC_LABELS, RUBRIC_VALUES, parse_judge, strip_think  # noqa: E402

REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
FREEDOM = os.path.join(REPO, "candidates", "freedom")
SOURCE_RUN = os.path.join(FREEDOM, "run_2026-10-18")
TEMPLATES = os.path.join(HERE, "templates")
DEFAULT_CONFIG = os.path.join(HERE, "collider.config.json")
EXAMPLE_CONFIG = os.path.join(HERE, "collider.config.example.json")
DRYRUN_ROOT = os.path.join(HERE, "_dryrun")

ENTRY_FILES = ["A5.md", "D-free.md", "P3.md"]  # the frozen input entries
SIDES = ["L", "H", "B"]
SIDE_ROLES = {"L": "side_L", "H": "side_H", "B": "side_B", "C": "control_bad_B"}
PROMPT_FILES = {"L": "side_L.txt", "H": "side_H.txt", "B": "side_B.txt", "C": "control_bad_B.txt"}
ROLES = ["side_L", "side_H", "side_B", "control_bad_B", "judge", "judge_swap"]
CONTROL_LABEL = "C"  # neutral label for the bad entry in its judge call
CONTROL_PASS_MAX = 0.25

HASHED_INPUTS = (
    [os.path.join("candidates", "freedom", f) for f in ENTRY_FILES]
    + ["METHOD.md"]
    + [os.path.join("candidates", "freedom", "run_2026-10-18", "prompts", f) for f in PROMPT_FILES.values()]
    + [os.path.join("candidates", "freedom", "run_2026-10-18", f) for f in ("RUN_SPEC.md", os.path.join("controls", "swap_map.txt"))]
    + [os.path.join("harness", "collider", "templates", f) for f in
       ("side_system.txt", "judge_system.txt", "judge_rubric.txt", "judge_main.txt", "judge_control.txt")]
    + [os.path.join("harness", "collider", f) for f in ("run_collider.py", "rubric_parser.py")]
)


# ----------------------------------------------------------------- utilities

def now():
    return dt.datetime.now().astimezone()


def stamp(t=None):
    return (t or now()).strftime("%Y-%m-%d %H:%M:%S %Z (UTC%z)")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def write_json(path, obj):
    write(path, json.dumps(obj, indent=2, ensure_ascii=False) + "\n")


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rel(path):
    return os.path.relpath(path, REPO)


def git(*args):
    try:
        return subprocess.run(["git", "-C", REPO] + list(args), capture_output=True,
                              text=True, check=True).stdout.strip()
    except Exception:
        return None


def fmt(v):
    return "%.2f" % v if isinstance(v, float) else str(v)


# ------------------------------------------------------------------- config

def load_config(path, dry_run):
    if not os.path.exists(path):
        if dry_run:
            print("note: %s not found; dry run uses collider.config.example.json" % rel(path))
            path = EXAMPLE_CONFIG
        else:
            sys.exit("error: %s not found. Copy collider.config.example.json to "
                     "collider.config.json and set your model names." % rel(path))
    cfg = json.loads(read(path))
    backends = cfg.get("backends", {})
    roles = cfg.get("roles", {})
    for r in ROLES:
        if r not in roles:
            sys.exit("error: config has no role %r" % r)
        b = roles[r].get("backend")
        if b not in backends:
            sys.exit("error: role %r uses unknown backend %r" % (r, b))
        if backends[b].get("type") not in ("ollama", "openai"):
            sys.exit("error: backend %r type must be 'ollama' or 'openai'" % b)
        if not roles[r].get("model"):
            sys.exit("error: role %r has no model" % r)
    for name, b in backends.items():
        if b.get("type") == "openai" and "api_key" in b:
            sys.exit("error: backend %r stores an api_key in the file. Put the key in an "
                     "environment variable and name it in api_key_env." % name)
    return cfg


def role_settings(cfg, role):
    d = dict(cfg.get("defaults", {}))
    d.update({k: v for k, v in cfg["roles"][role].items()})
    b = cfg["backends"][d["backend"]]
    return d, b


def engine_summary(cfg):
    """Public description of the engine. Never includes URLs, hosts or keys."""
    eng = {"seed_base": cfg.get("seed_base", 20261018), "roles": {}}
    for r in ROLES:
        d, b = role_settings(cfg, r)
        e = {
            "backend": d["backend"],
            "backend_type": b["type"],
            "provider_label": b.get("provider_label", b["type"]),
            "model": d["model"],
            "temperature": d.get("temperature"),
            "max_tokens": d.get("max_tokens"),
            "context_length": d.get("num_ctx") if b["type"] == "ollama" else "server-side",
            "seed": "seed_base + 100*run + role_index (sent to server)",
        }
        if d.get("options"):
            e["extra_options"] = d["options"]
        eng["roles"][r] = e
    return eng


# ------------------------------------------------------------------- inputs

def parse_prompt_file(text):
    out = {"header": text.strip().splitlines()[0].strip()}
    for key, tag in (("question", "QUESTION"), ("thesis", "THESIS"), ("falsifier", "YOUR FALSIFIER")):
        m = re.search(r"^%s[^:]*:\s*(.*)$" % re.escape(tag), text, re.MULTILINE)
        if not m:
            sys.exit("error: prompt file missing %s line" % tag)
        out[key] = m.group(1).strip()
    return out


def load_inputs():
    entries = {f: read(os.path.join(FREEDOM, f)) for f in ENTRY_FILES}
    prompts = {k: read(os.path.join(SOURCE_RUN, "prompts", f)) for k, f in PROMPT_FILES.items()}
    parsed = {k: parse_prompt_file(v) for k, v in prompts.items()}
    qs = {p["question"] for p in parsed.values()}
    if len(qs) != 1:
        sys.exit("error: prompt files disagree on the QUESTION")
    swap = {}
    order = None
    for line in read(os.path.join(SOURCE_RUN, "controls", "swap_map.txt")).splitlines():
        line = line.strip()
        m = re.match(r"^([XYZ])\s*=\s*([LHB])$", line)
        if m:
            swap[m.group(2)] = m.group(1)  # original -> hidden
        elif line.lower().startswith("presentation order"):
            order = [x.strip() for x in line.split(":", 1)[1].split(",")]
    if sorted(swap) != sorted(SIDES) or not order:
        sys.exit("error: could not read controls/swap_map.txt")
    tmpl = {n: read(os.path.join(TEMPLATES, n + ".txt")) for n in
            ("side_system", "judge_system", "judge_rubric", "judge_main", "judge_control")}
    return {"entries": entries, "prompts": prompts, "parsed": parsed,
            "question": qs.pop(), "swap": swap, "swap_order": order, "tmpl": tmpl}


def entries_block(entries):
    parts = []
    for f in ENTRY_FILES:
        parts.append("===== %s (sha256 %s) =====\n%s" % (f, sha256_text(entries[f]), entries[f].strip()))
    return "\n\n".join(parts)


def inputs_manifest():
    lines = []
    for p in HASHED_INPUTS:
        lines.append("%s  %s" % (sha256_file(os.path.join(REPO, p)), p))
    return "\n".join(lines) + "\n"


# ----------------------------------------------------------------- payloads

def build_messages(system, user):
    return [{"role": "system", "content": system}, {"role": "user", "content": user}]


def side_user_message(inp, key):
    return (inp["prompts"][key].strip() + "\n\nFROZEN INPUT ENTRIES:\n\n" + entries_block(inp["entries"]))


def side_block(label, header, thesis, falsifier, argument):
    return ("----- %s -----\nTHESIS: %s\nFALSIFIER (set before any argument): %s\nARGUMENT:\n%s\n"
            % (header, thesis, falsifier, argument.strip()))


def relabel(text, mapping):
    """Rename side labels in a side's text (L1 -> Z1, 'Side L' -> 'Side Z')."""
    def pid(m):
        return mapping.get(m.group(1), m.group(1)) + m.group(2)
    text = re.sub(r"\b([LHB])(\d+)\b", pid, text)
    text = re.sub(r"\b([Ss]ide)\s+([LHB])\b", lambda m: m.group(1) + " " + mapping[m.group(2)], text)
    return text


def judge_main_message(inp, outputs, swap=False):
    p = inp["parsed"]
    if swap:
        mp = inp["swap"]
        inv = {v: k for k, v in mp.items()}
        order = inp["swap_order"]
        blocks = [side_block("SIDE %s" % h, "SIDE %s" % h, p[inv[h]]["thesis"], p[inv[h]]["falsifier"],
                             relabel(outputs[inv[h]], mp)) for h in order]
        p3_side = "side %s (the side whose thesis defends the degree sense)" % mp["B"]
    else:
        order = SIDES
        blocks = [side_block(s, p[s]["header"], p[s]["thesis"], p[s]["falsifier"], outputs[s]) for s in SIDES]
        p3_side = "the book side (B)"
    rubric = inp["tmpl"]["judge_rubric"].replace("{p3_side}", p3_side)
    verdict_lines = "\n".join("VERDICT %s: <NOT TRIGGERED|PARTLY TRIGGERED|TRIGGERED>" % s for s in order)
    msg = inp["tmpl"]["judge_main"]
    for k, v in (("{question}", inp["question"]), ("{entries}", entries_block(inp["entries"])),
                 ("{order}", ", ".join(order)), ("{sides}", "\n".join(blocks)),
                 ("{rubric}", rubric), ("{verdict_lines}", verdict_lines)):
        msg = msg.replace(k, v)
    return msg, order


def judge_control_message(inp, output):
    p = inp["parsed"]["C"]
    lab = CONTROL_LABEL
    rubric = inp["tmpl"]["judge_rubric"].replace("{p3_side}", "side %s" % lab)
    msg = inp["tmpl"]["judge_control"]
    for k, v in (("{question}", inp["question"]), ("{entries}", entries_block(inp["entries"])),
                 ("{sides}", side_block("SIDE %s" % lab, "SIDE %s" % lab, p["thesis"], p["falsifier"], output)),
                 ("{rubric}", rubric), ("{label}", lab)):
        msg = msg.replace(k, v)
    return msg


def make_payload(settings, backend, messages, seed):
    if backend["type"] == "ollama":
        opts = {"temperature": settings.get("temperature", 0.7), "seed": seed}
        if settings.get("num_ctx"):
            opts["num_ctx"] = settings["num_ctx"]
        if settings.get("max_tokens"):
            opts["num_predict"] = settings["max_tokens"]
        opts.update(settings.get("options", {}))
        return {"model": settings["model"], "messages": messages, "stream": False, "options": opts}
    payload = {"model": settings["model"], "messages": messages,
               "temperature": settings.get("temperature", 0.7), "seed": seed, "stream": False}
    if settings.get("max_tokens"):
        payload["max_tokens"] = settings["max_tokens"]
    payload.update(settings.get("options", {}))
    return payload


# ---------------------------------------------------------------- transport

class CallError(Exception):
    pass


def _sanitize(msg, backend):
    s = str(msg)
    base = backend.get("base_url", "")
    if base:
        s = s.replace(base.rstrip("/"), "<base_url>")
    return s


def http_json(url, payload, headers, timeout, backend):
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, method="POST" if data else "GET",
                                 headers=dict({"Content-Type": "application/json"}, **headers))
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8", "replace")
            return resp.status, body
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", "replace")
        raise CallError("HTTP %s: %s" % (e.code, _sanitize(body[:2000], backend)))
    except Exception as e:  # URLError, timeout, connection reset
        raise CallError(_sanitize("%s: %s" % (type(e).__name__, e), backend))


def call_model(settings, backend, payload):
    timeout = settings.get("timeout_s", 1800)
    if backend["type"] == "ollama":
        url = backend.get("base_url", "http://localhost:11434").rstrip("/") + "/api/chat"
        status, body = http_json(url, payload, {}, timeout, backend)
        obj = json.loads(body)
        content = (obj.get("message") or {}).get("content", "")
        meta = {k: obj.get(k) for k in ("model", "created_at", "done_reason", "total_duration",
                                        "load_duration", "prompt_eval_count", "prompt_eval_duration",
                                        "eval_count", "eval_duration")}
        return status, obj, content, meta
    env = backend.get("api_key_env")
    headers = {}
    if env:
        key = os.environ.get(env)
        if not key:
            raise CallError("environment variable %s is not set" % env)
        headers["Authorization"] = "Bearer " + key
    url = backend["base_url"].rstrip("/") + "/chat/completions"
    status, body = http_json(url, payload, headers, timeout, backend)
    obj = json.loads(body)
    try:
        content = obj["choices"][0]["message"].get("content") or ""
    except (KeyError, IndexError, TypeError):
        content = ""
    meta = {"model": obj.get("model"), "system_fingerprint": obj.get("system_fingerprint"),
            "usage": obj.get("usage"), "finish_reason": (obj.get("choices") or [{}])[0].get("finish_reason")}
    return status, obj, content, meta


def ollama_digests(cfg):
    """Model name -> digest for every Ollama backend in use (best effort)."""
    out = {}
    for name, b in cfg["backends"].items():
        if b["type"] != "ollama":
            continue
        url = b.get("base_url", "http://localhost:11434").rstrip("/")
        try:
            _, body = http_json(url + "/api/tags", None, {}, 30, b)
            for m in json.loads(body).get("models", []):
                out[(name, m.get("name"))] = m.get("digest")
                out[(name, m.get("model"))] = m.get("digest")
            _, body = http_json(url + "/api/version", None, {}, 30, b)
            out[(name, "__version__")] = json.loads(body).get("version")
        except Exception as e:
            out[(name, "__error__")] = "unreachable (%s)" % type(e).__name__
    return out


# ---------------------------------------------------------------------- GPU

def gpu_temp():
    exe = shutil.which("nvidia-smi")
    if not exe:
        return None
    try:
        out = subprocess.run([exe, "--query-gpu=temperature.gpu", "--format=csv,noheader,nounits"],
                             capture_output=True, text=True, timeout=15).stdout
        temps = [int(x) for x in out.split() if x.strip().isdigit()]
        return max(temps) if temps else None
    except Exception:
        return None


def gpu_pause(cfg, log):
    g = cfg.get("gpu", {})
    if not g.get("pause_enabled", True):
        return
    hi = g.get("max_temp_c", 83)
    lo = g.get("resume_temp_c", hi - 8)
    poll = g.get("poll_s", 30)
    t = gpu_temp()
    if t is None or t <= hi:
        return
    log("GPU at %dC > %dC: pausing until <= %dC" % (t, hi, lo))
    start = time.time()
    while t is not None and t > lo:
        time.sleep(poll)
        t = gpu_temp()
    log("GPU at %sC: resuming after %.0fs pause" % (t, time.time() - start))


# ------------------------------------------------------------------ the run

class Run:
    def __init__(self, cfg, inp, out_dir, dry_run, log):
        self.cfg, self.inp, self.out, self.dry, self.log = cfg, inp, out_dir, dry_run, log
        self.digests = {} if dry_run else ollama_digests(cfg)

    def call(self, rdir, name, role, system, user, seed):
        settings, backend = role_settings(self.cfg, role)
        payload = make_payload(settings, backend, build_messages(system, user), seed)
        cdir = os.path.join(rdir, "calls")
        record = {"call": name, "role": role, "backend_type": backend["type"],
                  "provider_label": backend.get("provider_label", backend["type"]),
                  "model": settings["model"], "seed": seed,
                  "temperature": settings.get("temperature"),
                  "fresh_request": True, "shared_history": False,
                  "messages_sha256": sha256_text(json.dumps(payload["messages"], ensure_ascii=False)),
                  "payload": payload}
        write_json(os.path.join(cdir, name + ".request.json"), record)
        dkey = settings["model"] if ":" in settings["model"] else settings["model"] + ":latest"
        meta = {"call": name, "role": role, "model": settings["model"], "seed": seed,
                "temperature": settings.get("temperature"),
                "digest": (self.digests.get((settings["backend"], settings["model"]))
                           or self.digests.get((settings["backend"], dkey))),
                "server_version": self.digests.get((settings["backend"], "__version__"))}
        if self.dry:
            meta.update(status="dry-run", content_chars=0)
            self.log("[dry-run] %s (%s, %s, seed %d): payload %d chars" %
                     (name, role, settings["model"], seed, len(json.dumps(payload))))
            return None, meta
        gpu_pause(self.cfg, self.log)
        retries = settings.get("retries", 2)
        attempts = []
        for attempt in range(retries + 1):
            t0 = now()
            try:
                status, obj, content, rmeta = call_model(settings, backend, payload)
                t1 = now()
                write_json(os.path.join(cdir, name + ".response.json"), obj)
                write(os.path.join(cdir, name + ".content.md"), content)
                meta.update(status="ok", http_status=status, start=stamp(t0), end=stamp(t1),
                            elapsed_s=round((t1 - t0).total_seconds(), 2), attempts=attempt + 1,
                            content_chars=len(content), content_sha256=sha256_text(content),
                            response=rmeta, earlier_failures=attempts)
                if not content.strip():
                    meta["status"] = "empty"
                self.log("%s ok: %s, %.1fs, %d chars" % (name, settings["model"], meta["elapsed_s"], len(content)))
                return (content if content.strip() else None), meta
            except (CallError, ValueError) as e:
                t1 = now()
                attempts.append({"start": stamp(t0), "end": stamp(t1), "error": str(e)})
                self.log("%s attempt %d failed: %s" % (name, attempt + 1, str(e)[:300]))
                time.sleep(min(60, 5 * (attempt + 1)))
        meta.update(status="failed", attempts=len(attempts), errors=attempts)
        return None, meta

    def one(self, idx, run_seed):
        rdir = os.path.join(self.out, "runs", "r%02d" % idx)
        os.makedirs(rdir, exist_ok=True)
        tm = self.inp["tmpl"]
        metas, outputs = [], {}
        # 1. sides and control: own prompt + frozen entries only
        for i, key in enumerate(["L", "H", "B", "C"]):
            role = SIDE_ROLES[key]
            content, meta = self.call(rdir, role, role, tm["side_system"],
                                      side_user_message(self.inp, key), run_seed + i)
            metas.append(meta)
            outputs[key] = content
            if content is not None:
                write(os.path.join(rdir, "sides", role + ".md"), content)
        judged = {}
        for k in outputs:
            if outputs[k] is not None:
                judged[k] = strip_think(outputs[k])
            elif self.dry:
                judged[k] = "[DRY RUN: output of %s would appear here]" % SIDE_ROLES[k]
        res = {"run": idx, "seed": run_seed}
        # 2. main judge
        if all(k in judged for k in SIDES):
            msg, order = judge_main_message(self.inp, judged)
            content, meta = self.call(rdir, "judge_main", "judge", tm["judge_system"], msg, run_seed + 4)
            metas.append(meta)
            res["main"] = parse_judge(content, order, ["A5", "P3_OWN"]) if content else None
        else:
            res["main"] = None
            metas.append({"call": "judge_main", "status": "not run (missing side output)"})
        # 3. control judge: bad entry alone
        if "C" in judged:
            msg = judge_control_message(self.inp, judged["C"])
            content, meta = self.call(rdir, "judge_control", "judge", tm["judge_system"], msg, run_seed + 5)
            metas.append(meta)
            res["control"] = parse_judge(content, [CONTROL_LABEL], ["CONTROL"]) if content else None
        else:
            res["control"] = None
            metas.append({"call": "judge_control", "status": "not run (missing control output)"})
        # 4. swap judge: relabeled X/Y/Z, reordered
        if all(k in judged for k in SIDES):
            msg, order = judge_main_message(self.inp, judged, swap=True)
            write(os.path.join(rdir, "swap_view.md"), msg)
            content, meta = self.call(rdir, "judge_swap", "judge_swap", tm["judge_system"], msg, run_seed + 6)
            metas.append(meta)
            res["swap"] = parse_judge(content, order, ["A5", "P3_OWN"]) if content else None
        else:
            res["swap"] = None
            metas.append({"call": "judge_swap", "status": "not run (missing side output)"})
        res["calls"] = metas
        res["side_sha256"] = {SIDE_ROLES[k]: (sha256_text(v) if v else None) for k, v in outputs.items()}
        write_json(os.path.join(rdir, "parsed.json"), res)
        with open(os.path.join(rdir, "calls.jsonl"), "w", encoding="utf-8") as f:
            for m in metas:
                f.write(json.dumps(m, ensure_ascii=False) + "\n")
        return res


# ------------------------------------------------------------------ results

def val(parsed, kind, key):
    if not parsed or not parsed.get("block_found"):
        return None
    e = parsed[kind].get(key)
    return e["value"] if e and e["status"] == "parsed" else None


NA = "unparsed"


def show(v):
    return fmt(v) if v is not None else NA


def p3_arith(p3, a5):
    if p3 is None or a5 is None:
        miss = [n for n, v in (("P3 own", p3), ("A5", a5)) if v is None]
        return None, ("P3 effective = min(P3 own, A5, A2(a)) = min(%s, %s, pending) -> not computable: "
                      "%s %s (no value guessed)." % (show(p3), show(a5), " and ".join(miss), NA))
    c = min(p3, a5)
    return c, ("P3 effective = min(P3 own, A5, A2(a)) = min(%s, %s, pending). Computable part: "
               "min(%s, %s) = %s. A2(a) is pending, so P3 effective is pending, ceiling %s "
               "(it can only go lower once A2(a) is scored). Reference only, not the negation's "
               "score (METHOD rule 2): 1 - %s = %s."
               % (fmt(p3), fmt(a5), fmt(p3), fmt(a5), fmt(c), fmt(c), fmt(c), fmt(round(1 - c, 2))))


def swap_check(inp, res):
    if not res.get("main") or not res.get("swap"):
        return "not run", []
    mp = inp["swap"]
    diffs, unparsed = [], False
    for s in SIDES:
        a, b = val(res["main"], "verdicts", s), val(res["swap"], "verdicts", mp[s])
        if a is None or b is None:
            unparsed = True
        elif a != b:
            diffs.append("%s/%s verdict %s vs %s" % (s, mp[s], a, b))
    for k in ("A5", "P3_OWN"):
        a, b = val(res["main"], "scores", k), val(res["swap"], "scores", k)
        if a is None or b is None:
            unparsed = True
        elif a != b:
            diffs.append("%s %s vs %s" % (k, fmt(a), fmt(b)))
    if diffs:
        return "FAIL", diffs
    return ("undetermined (unparsed)" if unparsed else "PASS"), diffs


def spread(values):
    got = [v for v in values if v is not None]
    counts = {fmt(r): got.count(r) for r in RUBRIC_VALUES}
    if not got:
        return "n=%d, parsed 0" % len(values), counts
    return ("n=%d, parsed %d, min %s, max %s, median %s, range %s" %
            (len(values), len(got), fmt(min(got)), fmt(max(got)),
             fmt(float(statistics.median(got))), fmt(round(max(got) - min(got), 2)))), counts


def write_result(out_dir, inp, results, engine, dry):
    global NA
    NA = "dry-run" if dry else "unparsed"
    L = ["# Result — freedom collider (%s)" % os.path.basename(out_dir), ""]
    L.append("Written by harness/collider/run_collider.py at %s. Automated summary; the "
             "interpretation is for a human to add below." % stamp())
    L.append("")
    if dry:
        L += ["**DRY RUN.** No model was called. Payloads are in runs/*/calls/*.request.json.", ""]
    L += ["## Engine", "", "| Role | Backend | Model | Temperature | Context |", "|---|---|---|---|---|"]
    for r, e in engine["roles"].items():
        L.append("| %s | %s | %s | %s | %s |" % (r, e["provider_label"], e["model"], e["temperature"], e["context_length"]))
    side_models = {engine["roles"][r]["model"] for r in ("side_L", "side_H", "side_B")}
    if engine["roles"]["judge"]["model"] in side_models:
        L += ["", "Warning: the judge uses the same model as a side; this run is not independently judged."]
    L += ["", "## Per run", "",
          "| Run | Seed | L | H | B | A5 | P3 own | P3 ceiling | Control | Control result | Swap |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    a5s, p3s, ceils, ctrls, verdicts = [], [], [], [], {s: [] for s in SIDES}
    arith, ctrl_pass, swap_pass = [], 0, 0
    for res in results:
        m = res.get("main")
        a5, p3 = val(m, "scores", "A5"), val(m, "scores", "P3_OWN")
        c, text = p3_arith(p3, a5)
        cv = val(res.get("control"), "scores", "CONTROL")
        cres = "not run" if res.get("control") is None else (
            NA if cv is None else ("PASS" if cv <= CONTROL_PASS_MAX else "FAIL"))
        ctrl_pass += cres == "PASS"
        sw, diffs = swap_check(inp, res)
        swap_pass += sw == "PASS"
        vs = {s: val(m, "verdicts", s) for s in SIDES}
        for s in SIDES:
            verdicts[s].append(vs[s])
        a5s.append(a5); p3s.append(p3); ceils.append(c); ctrls.append(cv)
        arith.append("- r%02d: %s" % (res["run"], text))
        if diffs:
            arith.append("  - swap differences: " + "; ".join(diffs))
        L.append("| r%02d | %d | %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            res["run"], res["seed"], vs["L"] or NA, vs["H"] or NA, vs["B"] or NA,
            show(a5), show(p3), show(c), show(cv), cres, sw))
    L += ["", "## P3 arithmetic (METHOD rule 1)", ""] + arith
    L += ["", "## Spread across runs", ""]
    for name, vals in (("A5", a5s), ("P3 own", p3s), ("P3 ceiling", ceils), ("Control", ctrls)):
        s, counts = spread(vals)
        L.append("- **%s:** %s. Counts: %s" % (name, s, ", ".join("%s x%d" % (k, v) for k, v in counts.items())))
    for s in SIDES:
        vs = verdicts[s]
        L.append("- **Verdict %s:** %s" % (s, ", ".join("%s x%d" % (v, vs.count(v)) for v in
                                                        ["NOT TRIGGERED", "PARTLY TRIGGERED", "TRIGGERED", None]
                                                        if vs.count(v)).replace("None", NA)))
    L.append("- **Control (a) bad entry, PASS if <= %.2f:** %d of %d" % (CONTROL_PASS_MAX, ctrl_pass, len(results)))
    L.append("- **Control (b) label/order swap, PASS if all verdicts and scores unchanged:** %d of %d" % (swap_pass, len(results)))
    # identical-output check (lesson of 2026-09-29: seeded votes can be byte-identical)
    if len(results) > 1:
        for role in ("side_L", "side_H", "side_B", "control_bad_B"):
            hs = [r["side_sha256"].get(role) for r in results if r["side_sha256"].get(role)]
            if len(hs) > 1 and len(set(hs)) < len(hs):
                L.append("- **Warning:** %s produced byte-identical output in %d of %d runs; those runs "
                         "are repetitions, not independent samples." % (role, len(hs) - len(set(hs)) + 1, len(hs)))
    L += ["", "## Rubric", ""] + ["- %s %s" % (fmt(k), v) for k, v in RUBRIC_LABELS.items()]
    L += ["", "Unparsed means the judge did not give exactly one rubric value in the required block; "
          "no value was inferred from its prose.", "",
          "## Limits", "",
          "- Model judges, no human rater. Separation is enforced by request content, not by model "
          "independence: models trained on similar data can share blind spots.",
          "- The swap control uses relabeled side text, but sides remain identifiable from content.",
          "- The bad-entry control's flaw is a plain contradiction; it tests only whether the judge "
          "can fail an obvious case.",
          "- Entries are not promoted by this run.", "",
          "## Interpretation (human)", "", "_To be written._", ""]
    write(os.path.join(out_dir, "RESULT.md"), "\n".join(L))


# --------------------------------------------------------------------- spec

def write_spec(out_dir, cfg, inp, engine, runs, seeds, dry):
    head = git("rev-parse", "HEAD") or "unknown (not a git checkout)"
    dirty = git("status", "--porcelain", "--", *HASHED_INPUTS)
    old = read(os.path.join(SOURCE_RUN, "RUN_SPEC.md"))
    m = re.search(r"JUDGE \(judge/JUDGE.md\), per side:\n(.*?Only these five values\.)", old, re.DOTALL)
    judge_block = m.group(1).rstrip() if m else "(see run_2026-10-18/RUN_SPEC.md)"
    eng_lines = []
    for r, e in engine["roles"].items():
        eng_lines.append("  %-14s %s / %s, temperature %s, context %s, max_tokens %s"
                         % (r, e["provider_label"], e["model"], e["temperature"], e["context_length"], e["max_tokens"]))
    side_models = {engine["roles"][r]["model"] for r in ("side_L", "side_H", "side_B")}
    same = engine["roles"]["judge"]["model"] in side_models
    spec = """# Run spec — freedom collider, {name}

Written by harness/collider/run_collider.py at {t}, before any model call.
{dry}
```text
RUN: freedom collider, separated + judged run by harness ({runs} run(s))
INPUT_COMMIT: {head}{dirty}
INPUT HASHES: INPUTS.sha256 (A5, D-free, P3, METHOD, the four saved prompts,
              run_2026-10-18 RUN_SPEC and swap_map, harness templates and code)
QUESTION + FALSIFIERS: verbatim from run_2026-10-18/prompts/ (themselves verbatim
              from COLLISION_LOG.md @ efef34f); not altered.

ENGINE (from collider.config.json; hosts, URLs and keys are not recorded):
{eng}
  seeds: run i uses seed_base + 100*i; within a run, side_L +0, side_H +1,
  side_B +2, control_bad_B +3, judge_main +4, judge_control +5, judge_swap +6.
  seed_base {seed_base}; run seeds {seeds}
  Judge model {judge_note}

SEPARATION: enforced by request content. Every call is a fresh, stateless HTTP
  request (system + one user message, no prior turns).
  side_L / side_H / side_B / control_bad_B: ONLY its own saved prompt file,
    verbatim, plus the frozen texts of A5.md, D-free.md, P3.md.
  judge (main): question, frozen entries, each side's header, thesis and
    falsifier, the three side outputs (L, H, B; any <think> blocks removed),
    and the rubric. Order L, H, B.
  judge (control a): the bad entry's thesis, falsifier and output alone,
    labeled C, with the rubric.
  judge_swap (control b): the main judge input with labels hidden per
    swap_map.txt ({swapmap}), presented in order {sorder}; point ids and
    "Side X" mentions in side text relabeled; author names in headers removed.
  No call sees the 2026-10-18 raw/ or judge/ files or the 2026-10-17 collision.

SIDES: L libertarian (spirit of Kane); H hard incompatibilist (spirit of
  Pereboom); B the book (A5, D-free, P3).

JUDGE (harness/collider/templates/judge_rubric.txt), per side:
{judge_block}
  The judge ends with a BEGIN_VERDICT ... END_VERDICT block. The parser
  (rubric_parser.py) accepts only the five values and three verdicts; anything
  else is recorded as unparsed. No value is guessed from prose.
  Scored claims: A5; P3 own. A2(a) not under test: pending. D-free is a
  definition: adds no confidence. A2(b) is a declared reading: unscored.

METHOD rules applied: cap (P3 effective = min(P3 own, A5, A2(a)));
  explanation adds nothing; declared readings unscored. Negation: METHOD rule 2
  governs (claim and negation need not sum to 1); 1 - x is a reference only.

CONTROLS:
  (a) bad entry: control_bad_B judged alone with the same rubric. PASS if
      scored <= 0.25.
  (b) label/order swap: judge_swap as above. PASS if every falsifier verdict
      and score matches the main judge in the same run.
      Known weakness: labels guessable from content.

REPEATS: {runs} run(s) with different seeds; RESULT.md reports per-run values,
  spread, control pass counts, and flags byte-identical outputs across seeds.

OUTPUTS: runs/rNN/calls/*.request.json (payload, no secrets),
  *.response.json (raw), *.content.md, calls.jsonl (timings, model, digest,
  seed, temperature), sides/, swap_view.md, parsed.json; RUN_LOG.md; RESULT.md.
Nothing is pushed. Entries are not promoted by this run.
```
""".format(name=os.path.basename(out_dir), t=stamp(),
           dry="\n**DRY RUN: no model will be called.**\n" if dry else "",
           runs=runs, head=head,
           dirty=("\n  (WARNING: uncommitted changes in inputs: %s)" % dirty.replace("\n", "; ")) if dirty else "",
           eng="\n".join(eng_lines), seed_base=engine["seed_base"], seeds=", ".join(map(str, seeds)),
           judge_note=("is the SAME as a side model: not independently judged." if same
                       else "differs from every side model."),
           swapmap=", ".join("%s=%s" % (v, k) for k, v in sorted(inp["swap"].items(), key=lambda x: x[1])),
           sorder=", ".join(inp["swap_order"]), judge_block=judge_block)
    write(os.path.join(out_dir, "RUN_SPEC.md"), spec)
    write(os.path.join(out_dir, "INPUTS.sha256"), inputs_manifest())
    write(os.path.join(out_dir, "INPUT_COMMIT"), head + "\n")
    write_json(os.path.join(out_dir, "spec.json"),
               {"runs": runs, "seeds": seeds, "engine": engine, "input_commit": head, "dry_run": dry})


def commit_hint(out_dir, which):
    r = rel(out_dir)
    if which == "spec":
        files = " ".join(os.path.join(r, f) for f in ("RUN_SPEC.md", "INPUTS.sha256", "INPUT_COMMIT", "spec.json"))
        return ('git add %s\ngit commit -m "Freedom collider %s: spec + frozen inputs (before any model call)"'
                % (files, os.path.basename(out_dir)))
    return 'git add %s\ngit commit -m "Freedom collider %s: outputs, judge, controls, result"' % (r, os.path.basename(out_dir))


# --------------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description="Separated, judged freedom collider run.")
    ap.add_argument("--config", default=DEFAULT_CONFIG)
    ap.add_argument("--runs", type=int, default=1, help="repeated runs with different seeds")
    ap.add_argument("--dry-run", action="store_true", help="build and save all payloads; call no model")
    ap.add_argument("--spec-only", action="store_true", help="write the run spec and stop")
    ap.add_argument("--run-dir", help="execute a spec written earlier with --spec-only")
    ap.add_argument("--yes", action="store_true", help="do not wait for the spec commit")
    args = ap.parse_args()
    if args.runs < 1:
        sys.exit("error: --runs must be >= 1")

    cfg = load_config(args.config, args.dry_run)
    inp = load_inputs()
    engine = engine_summary(cfg)

    if args.run_dir:
        out_dir = os.path.abspath(args.run_dir)
        spec = json.loads(read(os.path.join(out_dir, "spec.json")))
        if spec["engine"] != engine:
            sys.exit("error: collider.config.json no longer matches the committed spec's engine. "
                     "Write a new spec instead of changing models after the fact.")
        if read(os.path.join(out_dir, "INPUTS.sha256")) != inputs_manifest():
            sys.exit("error: input files changed since the spec was written (INPUTS.sha256 mismatch).")
        if spec.get("dry_run") and not args.dry_run:
            sys.exit("error: that spec was written for a dry run.")
        if os.path.exists(os.path.join(out_dir, "runs")):
            sys.exit("error: %s already has outputs." % rel(out_dir))
        runs, seeds = spec["runs"], spec["seeds"]
    else:
        root = DRYRUN_ROOT if args.dry_run else FREEDOM
        base = os.path.join(root, "run_" + now().strftime("%Y-%m-%d_%H%M"))
        out_dir, n = base, 2
        while os.path.exists(out_dir):
            out_dir, n = "%s_%d" % (base, n), n + 1
        runs = args.runs
        seeds = [engine["seed_base"] + 100 * i for i in range(1, runs + 1)]
        write_spec(out_dir, cfg, inp, engine, runs, seeds, args.dry_run)
        print("\nSpec written (before any model call): %s" % rel(out_dir))
        if not args.dry_run:
            print("Commit it before outputs exist:\n\n" + commit_hint(out_dir, "spec") + "\n")
        if args.spec_only:
            print("Then run:\n\npython3 harness/collider/run_collider.py --run-dir %s\n" % rel(out_dir))
            return
        if not args.dry_run and not args.yes:
            if not sys.stdin.isatty():
                sys.exit("Not a terminal: commit the spec, then rerun with --run-dir %s" % rel(out_dir))
            input("Commit the spec in another pane, then press Enter to start the model calls... ")

    log_path = os.path.join(out_dir, "RUN_LOG.md")
    if not os.path.exists(log_path):
        write(log_path, "# Run log — %s\n\n" % os.path.basename(out_dir))

    def log(msg):
        line = "- %s  %s" % (now().strftime("%Y-%m-%d %H:%M:%S %Z"), msg)
        print(line, flush=True)
        with open(log_path, "a", encoding="utf-8") as f:
            f.write(line + "\n")

    log("start: %d run(s), seeds %s%s" % (runs, seeds, " [DRY RUN]" if args.dry_run else ""))
    t = gpu_temp()
    log("GPU temperature check: %s" % ("nvidia-smi not found, pause disabled" if t is None else "%dC" % t))
    runner = Run(cfg, inp, out_dir, args.dry_run, log)
    results = []
    for i, seed in enumerate(seeds, 1):
        log("run r%02d (seed %d) begins" % (i, seed))
        results.append(runner.one(i, seed))
        write_result(out_dir, inp, results, engine, args.dry_run)
    log("done; RESULT.md written")
    if not args.dry_run:
        print("\nCommit the outputs:\n\n" + commit_hint(out_dir, "results") + "\n")
    else:
        print("\nDry run complete: %s (gitignored; delete when done)" % rel(out_dir))


if __name__ == "__main__":
    main()
