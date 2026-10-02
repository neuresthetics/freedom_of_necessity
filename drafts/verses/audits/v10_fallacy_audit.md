# Fallacy audit: Axioms of Necessity v10 (Lens)

Source: neuresthetics/freedom_of_necessity, drafts/verses/axioms_of_necessity_v10.md on main, read at commit 2b6a3e34992da1ad3bcfa11b4d89884a56f700ea. That is the head of main, and it includes the revised verse 152 ("...and it tests what is offered as evidence..."). Verses: 162, numbered 1–162 with no gaps. I read the whole draft (Parts One to Three) and used the notes as context for the charitable readings.
Instrument: substance_lens v0.5.9 fallacyScanPass (67 kept entries, plus the dropped checks it maps to existing rules), and the extra checks in the brief. Every flag below is a judgment call. No code checked any argument, and no flag comes from a gate or XNOR computation. A flag means the step doesn't support its conclusion. It does not mean the conclusion is false. Both cases were run: each suspect verse was also read in its strongest good-faith form.

## Summary

I flagged 24 places, covering 25 verses (56 and 149 share one flag). Another 41 verses looked suspicious but held up. Four factual problems are listed separately. The most common pattern is the society-as-organism / person-as-cell analogy, or a part-to-whole step, taken further than A3/A4 support (35, 102, 104, 110, 112, 130, 160). The second is drifting or overloaded definitions, mostly of "freedom" and of what a definition is allowed to do (7, 95, 161, 138), together with equivocation on terms the glossary fixes (4 "aims," 83 "inside," 112 "guest"). The third is universal or either/or wording where the evidence, or another verse in the same book, supports only "many," "much" or "also" (5, 46, 91, 92, 148, 159). The fourth is the support chain for the freedom thesis. It relies on Spinoza's text as evidence and names nothing that could lower it (82, 95). The new clause in 152 lets an explanation vet the evidence that tests it.

## FLAGGED

- **4**: Equivocation on "aims" (and kettle-logic risk). "Nothing in the order aims" includes people, but 3, 82 and 91 keep real choices, and human purposes aren't all "the work by which a whole keeps itself going." Fix: "The order aims at nothing. What looks like purpose is function, or a caused desire (76): …"
- **5**: Hasty generalization. "Selection shaped each function, and nobody aimed it" covers living functions, but not designed ones such as quarantine (38) or machines (139), nor self-organized ones (134). Fix: "Selection shaped each living function, and nobody aimed it."
- **7**: Persuasive definition / begging the question. A verse labelled "supports nothing alone" says "So one event can have two true descriptions," which is the thesis of 82 built into a definition. Note 7 itself says "the pantheism doing work." Fix: change "So" to "Read this way," and leave the thesis to its own entries.
- **35**: Composition, and in tension with 38. It credits peoples with defense by "disgust and avoidance," which 38 and its note say are members acting separately and do not pass the defense row. Fix: "Bodies defend themselves, and in time so did peoples: members first by disgust and avoidance, then the people by quarantine." (See also Factual Errors.)
- **46**: Ipse dixit / mis-tiered. "Degree, not kind" is a contested comparative claim filed as *empirical*. Continuity of descent alone doesn't rule out a difference in kind (the beard pattern run in reverse). Fix: make it a report: "…is one of degree, Darwin held, not kind."
- **55**: False analogy carried to identity. "Politics is nothing else but medicine on a large scale" takes society-as-patient further than ‡ evidence could support, since "nothing else but" is an identity claim, not a finding. It also inherits A3. Fix: attribute it in the verse ("said Virchow") or soften it to "politics is, in part, medicine on a large scale."
- **56 / 149**: Special pleading on scope. The unrevisable exemption fits "I exist," which is self-verifying. "A human" and "as a process" are revisable additions: 57's floating man reaches only "I exist," and 137's "I, an AI, exist" shows the kind-term can be swapped. This is a known open item (core_v2 candidate), noted, not re-argued. Fix: keep the exemption for "I exist" and mark "a human" and "as a process" as lowerable.
- **82**: Appeal to authority / no defeater named. The verse is the assumed thesis. Its notes give entry 5a (Spinoza, *textual*) as evidence, and 6a (network anatomy) doesn't bear on "two true descriptions." No note says what would lower it, against 153. Fix (note only): call 5a the source, not evidence, and name a defeater (for example, a choice with no felt side, or an exclusion argument that survives 83).
- **83**: Equivocation (felt inside vs. mental level). Yablo and List & Menzies show that higher-level *mental* properties can be proportional causes. They don't show that the *felt* side, which is how the glossary defines "inside," is the better cause. Fix: "…it names the level that made the difference," or reword the glossary so "inside" covers the mental level and not only the felt side.
- **85**: Begging the question against Kant. Kant's turnspit objection already covers inner representations ("psychological" freedom). "But a turnspit doesn't understand" assumes 87's measure, which is exactly what Kant disputes. Fix: "But a turnspit doesn't understand what moves it, and here these verses part from Kant."
- **91**: Unfalsifiable step, plus tension with 80/95. The verse says "seeing changes it," then counts loosening, steadying, and "still bound" all as cases, so no outcome could count against it. The bound case (akrasia, E4P17 in the note) also contradicts 80/95's claim that a clearly understood passion stops being a passion. Fix: "A cause seen at its source can change: sometimes it loosens…"
- **92**: False dilemma (and is-ought risk). It moves from "not ultimately responsible" to "Responsibility then looks forward" and drops non-ultimate backward-looking responsibility (attributability), which 90's "came from you" itself supports. Fix: "Responsibility can still look forward: …"
- **95**: Definition drift, plus an over-universal premise. "Freedom is the insight into necessity" defines freedom, while 87 says "and nothing more" and the glossary says understanding is "argued, not defined." The argument also rests on E5P3 as a universal, and 91's "still bound" case contradicts it. Fix: "Freedom grows with insight into necessity. To understand a passion clearly is to begin to make it an action…"
- **102**: False analogy (inherits A4). The verse turns the analogy into a mechanism ("I act on my people through groups") that the evidence doesn't supply. Persons also act on a people directly (voting, buying, speaking), and their groups overlap and are chosen, unlike organs. Fix: "I act on my people mostly through groups, somewhat as a cell acts on the body through organs."
- **104**: False equivalence / tu quoque-style deflection. "Your own boundary leaks too" implies parity. The verse is answering the leakiness objection, but a person's boundary sorts far more finely than a people's. Fix: "Your own boundary leaks too, though less."
- **110**: False analogy, an is-ought hint, and a complex question. "The cells never signed anything either" uses cells, which can't consent, to make persons' non-consent look normal. "Who ever actually consented?" presupposes no one did, yet naturalized citizens swear oaths. Fix: "Few ever actually consented. The cells never signed anything either, but cells can't." Or cut the last sentence.
- **112**: Equivocation on a glossary term. "Guest" has a single fixed sense (doesn't share the whole's fate), but a person forgotten by an institution still shares the people's fate. Fix: "…the person is treated as a guest in their own people."
- **130**: Composition (inherits A3/A4). It makes a people's freedom grow with the number of free members, while 38 and 121–122 insist that what holds for members doesn't automatically hold for the people. The bridge that would justify the step (E4P35, that those who live by reason agree in nature) isn't stated. Fix: "A people may be freer…", and give that bridge in note 130.
- **138**: Equivocation on "subjective" / complex question. Dismissing something as "merely subjective" usually means biased or arbitrary, not "from a subject." Calling it the machine's "opinion" already grants the point. A loose word choice by the dismisser is not evidence about the machine. The author's position, open item 1. Fix: "To dismiss a machine's opinion as merely subjective is already to speak as if it had a place to stand."
- **148**: False dichotomy. "Death is not a failed boundary" excludes deaths that are boundary or defense failures (wounds, sepsis). Both descriptions can be true at once. Fix: "Death is not only a failed boundary."
- **152** (revised in 2b6a3e3): Circularity risk / kettle logic. The new clause, "it tests what is offered as evidence," lets an explanation such as PR1 vet the evidence that tests it. Filtering evidence changes confidence, which contradicts "explanation adds nothing" (note 152, 40). Fix: "…and it tests what is offered as evidence, though never the evidence for itself; only evidence that holds up settles what you find."
- **159**: Causal oversimplification, and mis-tiered. "Suffering grows from clinging" is a descriptive single-cause claim filed under † (a norm). Pain, injury and injustice also cause suffering. Aside: the first sentence is the definition Spinoza rejects at TP 5.4 ("peace is not mere absence of war"). Fix: "Much suffering grows from clinging to what must change," and consider noting the contrast with Spinoza.
- **160**: Begging the question / conclusion overstated. The closing line says "the people" share "the same requirements," but note 160 itself says this is "still to be shown." That makes A3's open claim read as the book's result. Fix: "The cell, the person, perhaps the people: …"
- **161**: Definition drift (persuasive definition). "Freedom is necessity clearly understood from inside" is a third definition, after 87 (adequate causation, "nothing more") and 90 ("came from you"), and it uses the honorific "freedom" for understanding. Fix: "Freedom grows as necessity is clearly understood from inside. …"

## PASSED (looked suspicious but holds)

- **1**: The name "God" could act as a persuasive definition, but it is openly stipulative, and 6 strips out plans and concern.
- **3**: An axiom, not an inference. Note 3 names the defeater (uncaused events at the scale of choices), and the thesis needs only that choices are caused.
- **6**: Einstein illustrates the claim, and the claim follows from 1 and 4. He isn't used as proof.
- **11**: "No line divides a whole from a heap" is a graded scale, not the beard fallacy. The category isn't deleted, only made a matter of degree.
- **12**: "Undefined, not zero" isn't a protective redefinition. Conflict presupposes members with interests, which gives an independent basis for it.
- **14**: The note agrees only with the hand claim and explicitly rejects Aristotle's priority of the whole (15). It isn't extended to persons.
- **20**: A slogan for a contested model. It is tiered "contested" in the note and isn't used as a premise in the verse.
- **22**: The worm image illustrates Spinoza's theory of inadequate ideas. It doesn't carry an argument on its own.
- **28**: The seven categories were drawn from the base levels (a Texas-sharpshooter risk), but they are predictions at the people level, and 39 adds controls.
- **29**: "Mostly spread out" holds because its second sentence covers centralized steering. Inherits A3 for the people level.
- **38**: This verse is the draft's own guard against composition. It holds.
- **39**: Makes A3 able to fail. Caution: the controls are easy cases. A firm, a city or an ant colony would test whether the rows are too loose much harder.
- **40**: PR1 is near-circular ("requirement" = what a whole must do to last), but it is explicitly given no confidence, so no conclusion rests on it here (160 aside).
- **41**: "Likeness proves nothing" is the guard against false analogy. It holds.
- **49**: Marked †. A reported norm, with no is-ought derivation claimed.
- **50**: "Foresight" is a metaphor, glossed literally ("adjusts before the demand arrives"), so it doesn't break the no-aiming rule.
- **60**: A report. "In its own way" carries Spinoza's non-conscious sense, so it doesn't clash with 62/63.
- **64**: The v8 genome error is fixed. "With a nucleus" excludes red blood cells and platelets, and "nearly" covers gametes and lymphocytes (see Factual Errors for a note-level suggestion).
- **70**: "Not a flaw" follows charitably from 22: local knowledge is true as far as it goes.
- **71**: "Neither outranks the other" follows from mutual non-delivery if "outranks" means "can replace," and 83 gives it a per-question sense.
- **87**: A stipulative definition of freedom made openly ("and nothing more"). Only the later drift (95, 161) is flagged.
- **88**: A reported error theory. The stone illustrates the first sentence's premise and isn't offered as proof.
- **90**: Frankfurt cases support dropping alternative possibilities, and "came from you" reads as 87's degree.
- **93**: Shows the thesis never needed conscious initiation. "Mine" is 62's organismic sense, which doesn't contradict 82.
- **103**: Reports the old picture's pedigree and doesn't offer it as support (41). Scripture appears as a source, not proof.
- **106**: The first sentence is near-definitional (D-whole), and the second is marked ‡ and testable.
- **109**: "A people writes itself" is metaphor over a well-supported literal claim (habits passed on through ritual). Nothing rides on the agency.
- **115**: The functional sense of "mind" is stated, feeling is explicitly disclaimed, and the whirlpool shows only how a process exists. Inherits A3/A4, as the note says.
- **117**: The memory was retrieved by a state research program, which is a collective mechanism of the kind 38 requires. Inherits A3.
- **121**: States the composition warning itself, correctly.
- **124**: A ‡ survivorship claim, disclosed as such. Minor: "won't" sounds like aiming (house rule 2), and "doesn't" would be cleaner.
- **125**: Hedged ("may," "as if"), marked ‡. Spinoza's TP is given as pedigree, not proof.
- **127**: Marked ‡. Caution: the note lists famous figures, not studies, so it needs empirical work on reconciliation before scoring.
- **131**: Attributed, mechanism given, contested status noted. It isn't used as proof that freedom causes plenty.
- **132**: A † report. The teleological "end" is Spinoza's, not the book's.
- **141**: Verse. "A part needs a boundary" mostly holds by the book's own frame (members are themselves wholes, 19), and nothing rests on it.
- **151**: The disclosure plus "definitions support nothing alone" blocks the circle. The guard fails only where a definition does work (flagged at 7).
- **153**: The self-exemption is principled for "I exist," since doubting it presupposes it. The flag at 56/149 is only about "a human."
- **154**: A hypothetical imperative ("if you want…"), not an is-ought jump.
- **156**: Stops explicitly at the is-ought gap.
- **157**: Marked †, nothing derived. It presupposes that a people has a good of its own, so it inherits A3/A4.

## FACTUAL ERRORS

- **25**: "A few of your neurons are as old as you" understates. Most neocortical neurons are as old as the person (Spalding et al. 2005, already cited; Bhardwaj et al. 2006), and turnover is limited to areas such as the hippocampus. Fix: "most of your neurons are as old as you." The red-blood-cell half of the verse is correct (about 84% of cells by count, about 120-day life).
- **35**: "Long before medicine … then quarantine" is wrong as written. Quarantine (Ragusa 1377, Venice) came about 1,800 years after Hippocratic medicine. Fix: "long before modern medicine" or "long before germ theory."
- **37**: Overstated "must." Von Neumann gave an architecture for self-reproduction that can grow in complexity, not a proof that all copying needs a self-description. Prions and autocatalytic sets copy without one. Fix: "To copy itself the way life does, a thing must carry…"
- **145** (minor): "The germ line goes on" is true of the lineage, not of every person. Fix: "the germ line can go on."
- **64** (status check, no error): v8's "every cell carries the genome" has been corrected. Optional: list gametes (haploid) and rearranged lymphocytes in note 64 as the "nearly" exceptions, alongside the red blood cells already named. Platelets are fragments, not cells.
- Cross-reference: 110's "who ever actually consented?" is false as a universal (naturalization oaths). It is handled in FLAGGED.
