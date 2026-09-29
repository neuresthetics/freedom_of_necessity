# Spinoza, *Ethics* — fixed reference texts (frozen 2026-09-28 PT)

## Purpose and authority
The **authoritative Ethics for the book is the Cambridge Texts in the History of Philosophy edition edited by Matthew J. Kisner** (the user's physical copy; under copyright; **not to be digitized**). Citations in the book use part/proposition (e.g. **E1P15**) plus Kisner page number.

The files here exist **only** to check Kisner quotations against (a) the Latin and (b) a public-domain comparison translation (Elwes 1883). They are not to be quoted as the book's primary text.

## Main files
- `ethica_latin.txt` — Latin, all five parts, UTF-8, LF. **Edition not stated by source** (see below).
- `ethics_elwes_1883.txt` — Elwes English translation, Gutenberg header/footer stripped, UTF-8 (pure ASCII), LF.
- `raw/` — untouched downloads (including a Gebhardt 1925 vol. II OCR as supplementary witness).

## Edition caveat (Latin)
The Latin Library transcription does **not** say which edition it follows. It is therefore recorded as *edition unstated*, not Gebhardt. Other options checked:
- la.wikisource `Ethica`: its header says the Latin is transcribed from Appuhn's bilingual *Éthique*, Paris: Garnier, 1913 (source cited: sacred-texts.com); talk page marks it "Textus non paratus". Not downloaded.
- archive.org has a genuine Gebhardt 1925 vol. II scan, but only raw OCR (kept as `raw/archive_…_djvu.txt`). For any contested reading, check against Gebhardt (G II page/line) rather than trusting `ethica_latin.txt`.

## Normalization performed (all of it)
**ethica_latin.txt** (from the 5 raw HTML pages, via `html_to_text.py`):
1. Two stray legacy (non-UTF-8) bytes mapped: `0x83` → `°` (ordinal marker as in "I°", 21 occurrences, parts 1 & 5; part 2 encodes the same with `&#176;`), `0x99` → `œ` (in "pœnitentia/pœnitet", 7 occurrences, part 3; part 4 encodes œ as `&oelig;`). No other non-ASCII bytes were present.
2. HTML entities decoded (`&aelig;`→æ, `&AElig;`→Æ, `&oelig;`→œ, `&#176;`→°).
3. HTML tags removed; block elements → line breaks; runs of whitespace inside a paragraph collapsed to one space (browser-rendering equivalent); paragraphs separated by a blank line; LF line endings.
4. Site navigation links (Neo-Latin / The Latin Library / The Classics Page) removed.
5. Five parts concatenated in order, separated by two blank lines. Each part keeps its own "SPINOZAE ETHICA / ORDINE GEOMETRICO DEMONSTRATA / ET IN QUINQUE PARTES DISTINCTA" page title as served. No words altered or added.

**ethics_elwes_1883.txt** (from `raw/pg3800_raw_download.txt`):
1. CRLF → LF (raw file is entirely CRLF).
2. Kept only lines strictly between `*** START OF THE PROJECT GUTENBERG EBOOK ETHICS ***` (raw line 29) and `*** END OF THE PROJECT GUTENBERG EBOOK ETHICS ***` (raw line 9782).
3. Removed the PG production credit line at the top of the body ("Produced by Tom Sharpe.  HTML version by Al Haines.") and leading/trailing blank lines. Nothing else changed (PG's `--` dashes, spacing, footnote markers retained).

## Sanity checks (run 2026-09-28 PT)
Proposition headings counted (`PROPOSITIO <roman>` in Latin; `PROP. <roman>.` in Elwes), checked for gaps, duplicates and order:

| Part | Expected | Latin | Elwes |
|---|---|---|---|
| I | 36 | 36 | 36 |
| II | 49 | 49 | 49 |
| III | 59 | 59 | 59 |
| IV | 73 | 73 | 73 |
| V | 42 | 42 | 42 |

No missing numbers, no duplicates, all in order, in both files. All five part headings present in both (Latin: PARS PRIMA…QUINTA, each ending "Finis …"; Elwes: PART I … PART V).

Spot check E1P15:
- Latin (`ethica_latin.txt` line 129): "PROPOSITIO XV: Quicquid est, in Deo est et nihil sine Deo esse neque concipi potest."
- Gebhardt OCR (raw, line 2651): "Quicquid  eft,  in  Deo  eft,  &  nihil  fine  Deo  effe,  neque  con¬[cipi potest]" — same words; Gebhardt has more punctuation.
- Elwes (`ethics_elwes_1883.txt` line 477): "PROP. XV.  Whatsoever is, is in God, and without God nothing can / be, or be conceived."

## Files, sizes, hashes
Verify with `sha256sum -c SHA256SUMS` from this directory. (MANIFEST.md itself is listed in SHA256SUMS but cannot contain its own hash.)

### `ethica_latin.txt`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica1.html … spinoza.ethica5.html (converted by html_to_text.py)
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Latin original. The Latin Library pages give NO statement of the underlying edition (no mention of Gebhardt, Van Vloten & Land, or the 1677 Opera Posthuma anywhere on the index or part pages). Edition: UNSTATED — do not cite as Gebhardt. Punctuation is lighter than Gebhardt (e.g. E1P15 lacks the commas Gebhardt prints).
- License / PD basis: Latin text by Spinoza (d. 1677): public domain. Transcription is a plain rendering of a PD text; The Latin Library offers it free for non-commercial use.
- Size: 457077 bytes
- sha256: `e6b04bcafca0eb92854ec0e08407859f6edfd433aa3f8392ab82689e73c0c167`

### `ethics_elwes_1883.txt`
- Source URL: https://www.gutenberg.org/cache/epub/3800/pg3800.txt (body extracted from raw/pg3800_raw_download.txt)
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: English translation by R. H. M. Elwes (PG eBook #3800, "Ethics", release 2003-02-01, most recently updated 2021-01-09; produced by Tom Sharpe). The PG file itself does not print a publication year; 1883 is the date of Elwes's translation (Bohn's Library, Chief Works of Spinoza vol. II). Includes Elwes's footnotes (some cite Van Vloten, Bruder, Pollock, Camerer).
- License / PD basis: Public domain in the USA (translation published 1883; Elwes d. 1929, also PD by life+70). Gutenberg trademark/license text removed per PG terms for stripped copies.
- Size: 502049 bytes
- sha256: `5f914a762ee19f73c9d22c5f01299364cf93e38d63ba5979d9a3ef9eec7d5b67`

### `html_to_text.py`
- Source URL: (local) conversion script written for this set
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Documents and reproduces the exact HTML→text conversion for ethica_latin.txt (`python3 html_to_text.py | cmp - ethica_latin.txt`).
- License / PD basis: Local script.
- Size: 2156 bytes
- sha256: `32d609d5f1a0907011b349d0bf0f351a23d5eb7f42781bcad7c92de5564d644a`

### `raw/latinlib_spinoza_index.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw index page (server Last-Modified 2006-09-15).
- License / PD basis: As above.
- Size: 998 bytes
- sha256: `15beed7af722fc7ddf2c956618f38ac10e9fc8f306e0100e99d752c1560e129e`

### `raw/spinoza.ethica1.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica1.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw download, Pars prima, byte-for-byte as served (server Last-Modified 2006-09-15).
- License / PD basis: Latin text PD (see ethica_latin.txt).
- Size: 79682 bytes
- sha256: `c65bb57c293035832dbf1dce005ae7ff9ec35b7bc9e42939a9b00d9f38003783`

### `raw/spinoza.ethica2.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica2.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw download, Pars secunda, byte-for-byte as served (server Last-Modified 2006-09-15).
- License / PD basis: Latin text PD (see ethica_latin.txt).
- Size: 97092 bytes
- sha256: `fd196374a72a12e8e0cab95fc4360b22c33dfc334d2ef93df90e10076777f020`

### `raw/spinoza.ethica3.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica3.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw download, Pars tertia, byte-for-byte as served (server Last-Modified 2006-09-15).
- License / PD basis: Latin text PD (see ethica_latin.txt).
- Size: 125787 bytes
- sha256: `7e735cd417131351c2eb9de0be5cb5dc9029415bc62d25fac68c9a1637ab577d`

### `raw/spinoza.ethica4.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica4.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw download, Pars quarta, byte-for-byte as served (server Last-Modified 2006-09-15).
- License / PD basis: Latin text PD (see ethica_latin.txt).
- Size: 127689 bytes
- sha256: `3e12d1424864b3c07c25942a178dedeaabed5acde9973f2c9cb2014cad998de5`

### `raw/spinoza.ethica5.html`
- Source URL: https://www.thelatinlibrary.com/spinoza.ethica5.html
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw download, Pars quinta, byte-for-byte as served (server Last-Modified 2006-09-15).
- License / PD basis: Latin text PD (see ethica_latin.txt).
- Size: 59198 bytes
- sha256: `a41a43d2804ba93ec1ef3df81865bc97361e943afed449dc94d273ae48e01e71`

### `raw/pg3800_raw_download.txt`
- Source URL: https://www.gutenberg.org/cache/epub/3800/pg3800.txt
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: Raw Gutenberg download incl. header/license, CRLF line endings, byte-for-byte as served (server Last-Modified 2026-09-02).
- License / PD basis: PD translation; file contains the Project Gutenberg License.
- Size: 531667 bytes
- sha256: `c549e5146cc820899acbed30f9c4e28e7bb8cd26046a98a977800ae62f856214`

### `raw/archive_operaimauftragde0000spin_a9g0_djvu.txt`
- Source URL: https://archive.org/download/operaimauftragde0000spin_a9g0/operaimauftragde0000spin_a9g0_djvu.txt  (item page https://archive.org/details/operaimauftragde0000spin_a9g0)
- Retrieved: 2026-09-28 ~22:31–22:33 PT (2026-09-29 05:31–05:33 UTC)
- Edition / translator: SUPPLEMENTARY WITNESS ONLY. Internet Archive automatic OCR of Spinoza, Opera, ed. Carl Gebhardt, Heidelberg: Carl Winter, [1925], Band II (Tractatus de intellectus emendatione / Ethica; Ethica begins p. 41). Title page OCR confirms "HERAUSGEGEBEN VON CARL GEBHARDT" and vol. II; date 1925 is from IA metadata. OCR is noisy (long-s read as f, line numbers, apparatus, page heads mixed in; many PROPOSITIO headings mangled) — usable for looking up Gebhardt readings by eye, NOT as a clean text. Scan from Trent University Library, digitized 2019.
- License / PD basis: Published 1925 → public domain in the USA since 2021-01-01. (Gebhardt d. 1932, so life+70 PD elsewhere too.) IA metadata sets no access restriction.
- Size: 935889 bytes
- sha256: `3311bdf43f057dcb8536a254aa6b594d0aa6f9af52e93a97ea3f3ba027a50a7b`

## Repository copy

This folder holds the two clean texts, the conversion script, and this manifest. The raw downloads listed above (web pages, Gutenberg raw file, Gebhardt scan OCR) are not included; their hashes above let anyone re-download and verify them. Verify these files with `sha256sum -c SHA256SUMS`.
