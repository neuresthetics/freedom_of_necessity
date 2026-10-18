# The collision record is the book

**Date.** 2026-10-17 PT. **Status.** A note on form. Changes nothing in `entries/` or the verses. The sample chapter below uses candidate entries (`candidates/freedom/`) that are not in the core and not scored.

## The idea

In the *Ethics*, each proposition carries a demonstration and, where needed, a scholium. The demonstration shows the steps. The scholium says what the steps mean and answers objections. This book adds one thing to that shape: each entry also carries its **collision record**. That record poses the question up front, argues each rival side at full strength, sets each side's falsifier before any argument is written, and says where the collision lands. The collision is the method shown working, and it is what a reader can check.

## Per-entry layout

1. **Statement.** The axiom, definition or proposition, in plain words.
2. **Supports.** The entries it cites (`cites:`) and the terms it only borrows (`terms:`). Terms add no confidence (METHOD.md).
3. **Cap.** Confidence = the lowest confidence among cited supports (METHOD rule 1). Definitions, declared readings and explanations add nothing (rules 4, 6). Until the collider runs, the cap reads "pending (collider)." No number is made up.
4. **Demonstration.** Numbered steps, each naming what it rests on.
5. **Collision record.** Question; sides; falsifiers (set first); arguments; side-by-side table; outcome. Where no harness has run, the outcome reads **unscored, collider not run**.
6. **Scholium.** Reports (Spinoza by part and proposition, other authors by published position), the limits, and how the entry fails.

**Verses.** The verses stay the reader's book. Each verse that carries an entry's claim points to that entry, and the entry's collision record is what stands behind the verse. A verse never claims more than its entry's outcome. If the outcome is "unscored," the verse keeps its current tag.

**Declared readings.** A declared reading (for example A2's "I am this body," clause (b)) appears in its own marked paragraph inside the entry. It is never inside the scored demonstration, and it adds nothing to the cap. In the collision record, a side may attack a declared reading, but the outcome can only say whether the reading still stands as a reading, never give it a score.

**The external review's point: "the instrument hasn't measured anything."** That's true, and this form doesn't hide it. It makes the gap visible. Each entry shows its question, its falsifiers and its open objections even before a score exists, so a reader can see what a measurement would test and what result would sink the claim. When the collider runs, its result fills the outcome line that is already there, and the cap follows. Until then, every outcome line says "unscored, collider not run."

---

## Sample chapter: Freedom (candidate; unscored, collider not run)

### A5. Every event is caused (model axiom)

**Statement.** Every event is caused, a choice included.

**Supports.** None. Terms: D-exist. **Cap.** Pending (collider); nothing above caps it.

**Stated sense.** An event is anything that happens. A cause is a prior condition from which it follows (E1A3). A5 doesn't say every cause is known, adequate (E3D1), or first-personal. It's weaker than E1P29, which the book reports but doesn't need.

**Scholium.** E2P48 denies absolute or free will in the mind; A5 is the thinner stand-in. **How it fails:** uncaused events at the scale of choices. Those would add chance, not freedom.

### D-free. Freedom, strict and by degree (definition)

**Statement.** *Definition 14 (strict):* free is what exists and acts from the necessity of its own nature alone (E1D7). Only Nature meets it (D-Nature, Scholium 4). *Definition 15 (degree):* a finite agent is freer to the degree that (a) what it does follows from its own organization and (b) it knows the causes of what it does clearly.

**Cap.** None. It's a definition and adds no confidence. **Leaves out:** could-have-done-otherwise, feeling, ultimate responsibility, society's freedom.

**Scholium.** E3D1–D2 (adequate cause; acting versus being passive) give the pattern for degree. E4P66 Note (the free man) and E5P42 are reports.

### P3. Freedom by degrees under necessity (proposition)

**Statement.** Freedom in D-free's degree sense is compatible with every event being caused. The body this thinking goes with is freer to the degree that what it does follows from its own organization and from clear knowledge of its causes. Could-have-done-otherwise isn't required.

**Supports.** A1, A2, A5. Terms: D-I, D-work, D-free, D-Nature.

**Cap.** min(A1 = 1.0, A2 = pending, A5 = pending) = **pending (collider)**. A2(b) adds 0.

**Demonstration (as in `candidates/freedom/P3.md`, condensed).**
1. Thinking is going on now (A1); it goes with a body made of cells (A2(a)).
2. Every choice of that body has a cause (A5).
3. Strict freedom belongs to Nature only; this body takes energy from outside (D-free 14).
4. Degree-freedom's two clauses can rise while every event stays caused (D-free 15).
5. Control done as one is clause (a) in the body's own works; clear knowledge of causes is clause (b) (D-work, Definitions 3, 5, 6).
6. So P3 holds. On A2's declared reading, a caused choice can also be *mine* (declared, unscored). ∎

**Declared reading.** That the act is *mine* in the first person rests on A2(b). It's unscored.

**Collision record** (from `candidates/freedom/collision_freedom.md` and `COLLISION_LOG.md`).

- **Question.** Does freedom require could-have-done-otherwise, or is the degree sense enough, or is that name a relabeling?
- **Sides.** L, libertarian (in the spirit of Kane). H, hard incompatibilist (in the spirit of Pereboom). B, the book.
- **Falsifiers (set before the arguments):**
  - *L:* a coherent account of an agent who is free and responsible in the ordinary sense while every event is caused by the total prior state, without changing the subject.
  - *H:* a checkable difference that knowledge of causes makes in behavior or later control work, one that isn't just "more of the same chain."
  - *B:* (i) uncaused choice-scale events that ground responsibility better; (ii) proof that 15(b) never changes how the agent acts; (iii) a successful demand that "free" must mean could-have-done-otherwise.
- **Arguments.** L1–L4 (the intuition; undetermined but not chance; P3 changes the subject; Spinoza is a cost, not a proof). H1–H4 (the source problem; relabeling; knowledge is more chain; forward-looking norms survive). B1–B5 (two senses; chance is no third way; knowledge isn't idle; the first person without a ghost; desert versus degree).
- **Strongest live objections to B:** L3 (changes the subject), H2 (relabeling).
- **Strongest pressure on the rivals:** B2 (chance gap), B5 (desert isn't smuggled back in).
- **Outcome.** No winner, no scores, no promotion, no harness run. **Unscored, collider not run.**
- **Disclosure.** Written in one pass by a Grok-based assistant following the author's brief. The exact shape is in `candidates/freedom/COLLIDER_SPEC_USED.md`.

**Scholium.** E2P48; E3D1–D2; E4P66 Note; E5P3; E5P42 (reports, adding nothing). Kant's turnspit (*Critique of Practical Reason*, Ak. 5:96–97). P3's reply is 15(b), and it's left open for the collider. **How P3 fails:** if A5 fails; if 15(b) is idle (H); if freedom must mean could-have-done-otherwise (L).
