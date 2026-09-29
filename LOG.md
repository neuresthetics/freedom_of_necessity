# Log

A dated record of what was tested and what changed, newest first. Times are Pacific (PT).

## 2026-09-29 — Entry wording fixes (after the review)

Book content only; nothing new was promoted into `entries/`.

- **A3, performed vs must perform.** The claim now says each function is *performed* at all three levels, matching its reading. Why the seven should recur (they are what a whole must do to last) is PR1's thesis and adds no confidence.
- **A3, failure case.** A row fails if society does the work only through members acting separately; A3 fails if any row fails; the rows are too loose if something D-whole rules out passes all seven. Proposed negative controls: a stone, a hurricane, an archive.
- **Sweep.** Every entry was checked for "must perform" vs "performed". The same slip was in A3's caveat 3 and PR1's Method section; both now judge by what is performed. A2, A4 and P1 were clean. D-whole's "admits what the whole needs" is part of a definition and was left as is.
- **PR1** is now "Pattern by requirement": requirement (what a whole must do to last) is kept apart from necessity (modal), which stays in the title.
- **D-whole** vantage now reads "from among its members / from a distance"; "inside" is kept for the felt side.
- **P1** now says a collective mind *happens* in society: a process emerging from feedback, not a thing the society has.

## 2026-09-29 — Back to the drawing board

An outside review of the v0.1 record, checked against the raw data, found problems serious enough that no baseline will be taken until they are fixed.

- **Arm 4 was mislabeled.** At temperature 0, the four seeded votes returned byte-identical outputs, reasoning included. So arm 4 repeated one answer four times; it was not four times the compute. The v0.1 claim that "compute alone doesn't help" is not supported by that run.
- **A3 may not be able to fail.** If any lasting institution passes all seven rows, A3 sorts things rather than discovering anything. A3 needs a stated failure case before it is scored again.
- **"Must perform" vs "performed"** is a real gap in the book, not only a harness bug, and may appear in other entries. Every entry will be checked for it.
- **The five-step lens is retired.** It will be replaced by a minimal collider: the model builds a steel man of each entry and the strongest counter steel man, both in the book's geometric form, and judges them side by side. Code checks citations and quoted spans; the model does not check its own citations.

Next: four runs on the same entries and broken twins. A clean control and the collider, each on the uncensored model and on the stock model.

The freeze on `entries/` is lifted, since the test it waited on has run and is being redone.

## 2026-09-29 — Lens test v0.1 (uncensored model)

We tested whether the five-step lens catches planted flaws better than a plain judge.

- The lens caught 10 of 13 broken twins (every wording of the twin failed).
- Code checks alone, run on the plain judge's reply, caught 3. The plain judge caught 1.
- The same plain judge voted over 4 seeds also caught 1. (Correction, same day: those votes were identical, so this was a repetition, not extra compute. See the entry above.)
- But the lens also failed 5 of 6 real entries. Every one of those failures came from a bug in the harness (its code checks or its lens prompts), not from a flaw in the book. So the lens did not pass the bar set before the run.
- It found one real issue in the book: A3's claim says each row names a function a whole "must perform", but A3's reading says to judge whether each function is "performed". These set different bars.

Details are in [results/2026-09-29_lens-v0.1/](results/2026-09-29_lens-v0.1/).

Next, the same test runs on the stock model, then v0.2 fixes the bugs.

## 2026-09-28 — Spinoza reference texts

Added frozen copies of Spinoza's *Ethics* in [sources/spinoza/](sources/spinoza/): the Latin text (its source does not say which edition it follows) and the Elwes 1883 English translation, with a sha256 manifest. They exist only to check quotations from the Kisner edition that the book cites; they are not quoted as the main text. Commit 3bd3520, 22:57 PT.
