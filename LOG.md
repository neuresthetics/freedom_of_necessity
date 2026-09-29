# Log

A dated record of what was tested and what changed, newest first. Times are Pacific (PT).

## 2026-09-29 — Lens test v0.1 (uncensored model)

We tested whether the five-step lens catches planted flaws better than a plain judge.

- The lens caught 10 of 13 broken twins (every wording of the twin failed).
- Code checks alone, run on the plain judge's reply, caught 3. The plain judge caught 1.
- The same plain judge voted over 4 seeds (four times the compute) also caught 1.
- But the lens also failed 5 of 6 real entries. Every one of those failures came from a bug in the harness (its code checks or its lens prompts), not from a flaw in the book. So the lens did not pass the bar set before the run.
- It found one real issue in the book: A3's claim says each row names a function a whole "must perform", but A3's reading says to judge whether each function is "performed". These set different bars.

Details are in [results/2026-09-29_lens-v0.1/](results/2026-09-29_lens-v0.1/).

Next, the same test runs on the stock model, then v0.2 fixes the bugs.

## 2026-09-28 — Spinoza reference texts

Added frozen copies of Spinoza's *Ethics* in [sources/spinoza/](sources/spinoza/): the Latin text (its source does not say which edition it follows) and the Elwes 1883 English translation, with a sha256 manifest. They exist only to check quotations from the Kisner edition that the book cites; they are not quoted as the main text. Commit 3bd3520, 22:57 PT.
