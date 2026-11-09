#!/usr/bin/env python3
"""Build the public reader pages for the book site.

Usage:
  python3 tools/build_reader.py --site PATH_TO_SITE_CHECKOUT [--book PATH_TO_BOOK_REPO]

Writes, inside the site checkout:
  book/foreword/index.html   the foreword draft
  book/poetic/index.html     poetic track, V001-V251
  book/technical/index.html  technical track, V001-V251
  book/index.html            refreshes the "full draft" accordion between
                             <!-- full-draft:start --> and <!-- full-draft:end -->

Harness scores were dropped from the process (2026-11-09). The site build hides
leftover score, cap, and confidence lines from entry files and renders; the
entry files themselves are unchanged until a cleanup pass.

Needs the `markdown` package (pip install markdown).
"""
from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path

import markdown

GH = "https://github.com/neuresthetics/freedom_of_necessity/blob/main/"
DR_REL = "candidates/core_v3/variant_sets/set_20261025_B1/dual_render"
SCORE_NOTE_IDS = {"D-collider", "D-certainty-grades", "D-declared-reading"}
SCORE_NOTE = "*(Historical: numeric scores were dropped from the process on 2026-11-09; entries are judged by dependency checks, citations, and coherence.)*"

SCORE_RE = re.compile(
    r"\b(scor(e|es|ed|ing)|unscored|confidence|collider|caps? nothing|caps? =|cap =|cap\b|caps\b|min\(|1\.0)",
    re.I,
)


# ---------- text cleanup (site only) ----------

def clean_mirror_labels(t: str) -> str:
    t = t.replace("**Mirror (outside / inside; A2(b) reading, unscored).**",
                  "**Mirror (outside / inside; A2(b), declared reading).**")
    t = t.replace(" One event, two descriptions; part of A2's declared reading (b). Unscored: adds no confidence and changes no cap.",
                  " One event, two descriptions; part of A2's declared reading (b).")
    return t


def drop_score_sentences(par: str) -> str:
    """Remove sentences that only carry score/cap/confidence talk."""
    parts = re.split(r"(?<=[.;])\s+(?=[A-Z*(])", par)
    keep = [p for p in parts if not SCORE_RE.search(p)]
    return " ".join(keep).strip()


PHRASES = [
    ("**Label note (unscored; adds no confidence).**", "**Label note.**"),
    ("(declared reading, unscored)", "(declared reading)"),
    (", unscored)", ")"),
    ("; unscored", ""),
    (" is rescored", " is re-checked"),
    ("**Confidence 1.0.**", "**Certainty.**"),
]


def clean_block(text: str, keep_sentences: bool = False) -> str:
    text = clean_mirror_labels(text)
    for a, b in PHRASES:
        text = text.replace(a, b)
    out = []
    for line in text.split("\n"):
        s = line.strip()
        # whole-line displays
        if re.match(r"^(- )?\*\*Cap[.:]\*\*", s):
            continue
        if re.match(r"^\*\*Confidence", s):
            continue
        # header lines like **Kind:** x · **Confidence:** y · **Cap:** z
        if s.startswith("**Kind:**"):
            segs = [g for g in line.split(" · ") if not re.search(r"\*\*(Confidence|Cap):\*\*", g)]
            out.append(" · ".join(segs)); continue
        if keep_sentences and (s.startswith(("**Statement.**", "**Claim (entry).**")) or not s.startswith(("**", "- "))):
            out.append(line); continue
        if s.startswith(("**Cites.**", "**Rests on:**", "**Supports", "- **Rests on", "- **Supports")):
            out.append(line); continue
        if SCORE_RE.search(s) and not s.startswith(("Seen from", "- *Outside", "- *Inside", "#")):
            if s.startswith("- "):
                body = drop_score_sentences(s[2:])
                if body: out.append("- " + body)
                continue
            lead = re.match(r"^(\*\*[^*]+\*\*\s*)", s)
            if lead:
                body = drop_score_sentences(s[lead.end():])
                if body or not lead.group(1).startswith("**Failure"):
                    out.append((lead.group(1) + body).rstrip())
                continue
            body = drop_score_sentences(s)
            if body: out.append(body)
            continue
        out.append(line)
    return "\n".join(out)


def abs_links(text: str, rel_dir: str) -> str:
    def fix(m):
        label, url = m.group(1), m.group(2)
        if url.startswith(("http", "#", "mailto:")):
            return m.group(0)
        parts = (rel_dir.rstrip("/") + "/" + url).split("/") if rel_dir else url.split("/")
        stack = []
        for p in parts:
            if p in ("", "."): continue
            if p == "..":
                if stack: stack.pop()
            else: stack.append(p)
        return f"{label}({GH}{'/'.join(stack)})"
    return re.sub(r"(\[[^\]]*\])\(([^)\s]+)\)", fix, text)


def md(text: str, nl2br: bool = False) -> str:
    # python-markdown needs a blank line before a list
    text = re.sub(r"(?m)^((?![-*] |\s*$).+)\n(- )", r"\1\n\n\2", text)
    return markdown.markdown(text, extensions=["extra"] + (["nl2br"] if nl2br else []))


# ---------- sources ----------

def render_sections(book: Path, track: str):
    out = []
    for fn in ("BASE.md", "expansion.md"):
        t = (book / DR_REL / track / fn).read_text(encoding="utf-8")
        for block in re.split(r"(?m)^(?=## V\d{3} · |# Group )", t)[1:]:
            if block.startswith("# Group"):
                g = re.match(r"# Group `?([^`\n]+)`?", block).group(1)
                out.append(("group", g, None, None, None))
                continue
            m = re.match(r"## (V\d{3}) · `([^`]+)` — (.*)\n", block)
            body = re.sub(r"\n---\s*$", "", block[m.end():].strip()).strip()
            out.append(("v", m.group(1), m.group(2), m.group(3), body))
    return out


def entry_files(book: Path):
    core = book / "candidates/core_v3"
    sys.path.insert(0, str(core / "tools"))
    import dep_check  # noqa: E402
    return dep_check.load_live(), core


def strip_frontmatter(t: str) -> str:
    return re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)


# ---------- page shell ----------

def shell(index_html: str, title: str, desc: str, url: str, depth: int):
    head = index_html.split('<main id="main">')[0]
    foot = "<footer" + index_html.split("<footer", 1)[1]
    head = re.sub(r"<title>.*?</title>", f"<title>{html.escape(title)} · Freedom of Necessity · Neuresthetics</title>", head)
    head = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + html.escape(desc), head)
    head = head.replace('content="https://neuresthetics.github.io/book/"', f'content="https://neuresthetics.github.io/book/{url}"')
    if depth:
        head = head.replace('href="../', 'href="../../').replace('src="../', 'src="../../')
    return head, foot


def track_page(book, site, index_html, track, other):
    secs = render_sections(book, track)
    toc, body = [], []
    for kind, a, b, title, txt in secs:
        if kind == "group":
            body.append(f'<h2 class="grp">{html.escape(a.replace("_", " "))}</h2>')
            continue
        toc.append(f'<a href="#{a}">{a}</a>')
        t = clean_block(txt, keep_sentences=b in SCORE_NOTE_IDS)
        if b in SCORE_NOTE_IDS:
            t += "\n\n" + SCORE_NOTE
        body.append(
            f'<section class="v" id="{a}"><h3><a href="#{a}">{a}</a> · <code>{html.escape(b)}</code> — {html.escape(title)}</h3>'
            f'{md(abs_links(t, DR_REL + "/" + track), nl2br=True)}<p class="twin"><a href="../{other}/#{a}">{other} {a} →</a></p></section>')
    name = track.capitalize()
    intro = ("Plain modern lines, one verse per entry. Where someone is there to be described from within, a verse ends with a mirrored couplet: seen from without, seen from within."
             if track == "poetic" else
             "The joints: kind, what each entry rests on, and the claim. Where a person is there to be described from within, the entry also carries an outside / inside pair (A2’s declared reading).")
    head, foot = shell(index_html, f"{name} track", f"Freedom of Necessity, {track} track, V001–V251.", f"{track}/", 1)
    page = head + f'''<main id="main">
  <div class="wrap">
    <article class="construct reader {track}">
      <div class="fly">
        <p class="eyebrow">Freedom of Necessity · dual render</p>
        <h1>{name} track</h1>
        <p class="tag"><span class="k">V001–V251</span><span class="v">one chain · two doors</span></p>
        <p class="lead">{intro}</p>
        <p class="pitch">Same numbers and entry ids as the <a href="../{other}/">{other} track</a>. Start with the <a href="../foreword/">foreword</a>. Source: <a href="{GH.replace("/blob/", "/tree/")}{DR_REL}">dual render on GitHub</a>.</p>
        <nav class="vtoc" aria-label="Verses">{" ".join(toc)}</nav>
      </div>
      {"".join(body)}
    </article>
    <p class="back"><a href="../">← Book</a></p>
  </div>
</main>

''' + foot
    d = site / "book" / track
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")


def foreword_md(book):
    t = (book / "drafts/foreword_origin.md").read_text(encoding="utf-8").split("\n", 1)[1]
    return abs_links(clean_block(t), "drafts")


def foreword_page(book, site, index_html):
    head, foot = shell(index_html, "Foreword", "Foreword: how this text came to be.", "foreword/", 1)
    page = head + f'''<main id="main">
  <div class="wrap">
    <article class="construct reader foreword">
      <div class="fly">
        <p class="eyebrow">Freedom of Necessity</p>
        <h1>Foreword</h1>
        <p class="tag"><span class="k">draft</span><span class="v">how this text came to be</span></p>
      </div>
      {md(foreword_md(book))}
      <p class="pitch">Next: the <a href="../poetic/">poetic track</a> or the <a href="../technical/">technical track</a>. Source: <a href="{GH}drafts/foreword_origin.md">foreword on GitHub</a>.</p>
    </article>
    <p class="back"><a href="../">← Book</a></p>
  </div>
</main>

''' + foot
    d = site / "book" / "foreword"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page, encoding="utf-8")


def full_draft(book) -> str:
    """Foreword + all 251 entries in chain order (V001-V251), full entry text."""
    E, core = entry_files(book)
    order = [(a, b) for kind, a, b, _, _ in render_sections(book, "technical") if kind == "v"]
    poems = {b: body for kind, a, b, _, body in render_sections(book, "poetic") if kind == "v"}
    parts = ['<section class="dv" id="draft-foreword"><h3 class="did">Foreword</h3>', md(foreword_md(book)), "</section>"]
    for vnum, eid in order:
        e = E[eid]
        rel_dir = e["path"].parent.relative_to(book).as_posix()
        t = strip_frontmatter(e["text"])
        t = re.sub(r"\n## Hyper-connect\n.*\Z", "", t, flags=re.S)   # index block, not draft text
        t = re.sub(r"(?m)^\*\*(BASE \(locked\)|Expansion from BASE[^*]*)\.\*\*.*\n?", "", t)
        t = re.sub(r"(?m)^\*\*[^*\n]+\*\* \*\((?:[^)]*id: [^)]*)\)\*\.\s*\n", "", t)  # repeated title line
        t = clean_block(t, keep_sentences=eid in SCORE_NOTE_IDS)
        if eid in SCORE_NOTE_IDS:
            t += "\n\n" + SCORE_NOTE
        title = html.escape(e["title"])
        parts.append(f'<section class="dv" id="draft-{vnum}"><h3 class="did"><span class="sc">{vnum} · {html.escape(eid)}</span> {title}</h3>'
                     f'{md(abs_links(t, rel_dir))}'
                     f'<blockquote class="dverse"><p class="vl">Verse</p>{md(clean_block(poems.get(eid, ""), keep_sentences=eid in SCORE_NOTE_IDS), nl2br=True)}</blockquote></section>')
    return "\n".join(parts)


def accordion(book, site):
    p = site / "book" / "index.html"
    t = p.read_text(encoding="utf-8")
    block = f'''<!-- full-draft:start -->
    <details class="full-draft" id="full-draft">
      <summary>Open the full draft, as it is: foreword and all 251 entries in chain order</summary>
      <div class="draft-body">
{full_draft(book)}
      </div>
    </details>
    <!-- full-draft:end -->'''
    if "<!-- full-draft:start -->" in t:
        t = re.sub(r"<!-- full-draft:start -->.*?<!-- full-draft:end -->", lambda m: block, t, flags=re.S)
    else:
        t = t.replace("<h2>Start here</h2>", block + "\n\n        <h2>Start here</h2>", 1)
    p.write_text(t, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--site", required=True, help="path to the site checkout (contains book/index.html)")
    ap.add_argument("--book", default=str(Path(__file__).resolve().parents[1]), help="path to this book repo")
    a = ap.parse_args()
    book, site = Path(a.book), Path(a.site)
    index_html = (site / "book" / "index.html").read_text(encoding="utf-8")
    track_page(book, site, index_html, "poetic", "technical")
    track_page(book, site, index_html, "technical", "poetic")
    foreword_page(book, site, index_html)
    accordion(book, site)
    print("built: book/foreword, book/poetic, book/technical, full-draft accordion")


if __name__ == "__main__":
    sys.exit(main())
