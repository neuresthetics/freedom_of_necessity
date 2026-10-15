# Coherence check 5: core v2 proofs, v12 verses, and v12 notes against v11

*Fifth, independent pass, 2026-10-15. Own pass done first without reading passes 1–4; compared afterwards. Targets: (1) each core v2 entry step by step (proof steps, terms before use, circularity, confidence caps); (2) the v12 verses for anything passes 1–4 missed; (3) v12's notes and `v12_changes.md` against v11, with every claimed verbatim keep diffed mechanically. Draft, local only. Verse file and core not edited; core issues are flagged for Jason.*

## Verdict

The core proofs are mostly sound. P1's demonstration follows step by step given its premises, P2's follows given its name, and every stated cap matches what the entry cites (P1 min(A2, A3, A4), with the first half min(A2, A3); P2 its three rows plus A2 through A4; A4 its weakest row plus A2; A1 1.0 capping nothing). No definition is circular. But there is one new structural conflict inside the core, **between A3 and PR1** (K1). PR1 says three of the seven works are required only in some circumstances, while A3 says every self-producing thing performs all seven. The verses inherit it (61 against 75). There is also a terminology split: "declared reading" means opposite things in METHOD.md and in the entries (K2).

Verbatim check: of the 41 v11 verses `v12_changes.md` lists as "kept verbatim", 38 are exact. Two differ in ways the list discloses (143's second half, and 157's "people" → "society"). One differs without being disclosed (130 → 143). Three verses listed as "rewritten" are actually verbatim.

**New issues: 20. 1 high, 4 medium, 15 low.** 9 are core-level and flag-only.

## A. Core entries (flag only; Jason's call)

| # | Sev. | Where | Current | Problem | Suggested fix |
|---|---|---|---|---|---|
| K1 | High | A3 axiom vs PR1, "Holding in some circumstances" and "What would count against it" | A3: "A thing that produces itself … performs all seven as one." PR1: transport, signaling and defense are required only "where a condition is met", and "a self-producing thing that lacks a conditional work where the condition is absent counts against neither." | A self-producing thing with no transport (a small cell living by diffusion, as PR1 itself says) is an F1 failure of A3, yet PR1 says it counts against nothing. The two can't both hold. A3 already anticipates this case (bacterial transport, F1) as a risk; PR1 treats it as expected. | Pick one, in one chain: (a) A3 says "performs all seven as one, the three conditional works wherever their condition holds", with F1 restated to match. Or (b) PR1 drops "counts against neither" and says such a case is an F1 failure of A3. (a) is the more coherent; it also settles A3's bacterial-transport hard case. |
| K2 | Med | METHOD.md rule 5 vs A2 (b), D-Nature, A4 | METHOD rule 5: the entry "states which [reading] it claims, and it is scored on that reading only." A2 (b) and D-Nature: a declared reading is "not scored" and "adds no confidence". A4's heading "Declared reading" introduces a stipulated definition of "society" (METHOD's sense). | One term, two opposite meanings: the reading an entry is scored *on*, and a reading that is *not* scored. A4 uses the first, A2 and D-Nature the second. | Keep "declared reading" for the unscored sense (as the verses use it), and rename METHOD rule 5's sense and A4's heading "stated sense" or "scope". Or reword METHOD rule 5 to cover both. |
| K3 | Low | A1, "In defined terms" | "An activity cannot go on while what does it, if anything does, fails to exist; this is taken as evident with the root." | A second premise rides inside the one entry held at 1.0, without being named as such. It's harmless (it's conditional on a doer), but the root should be one claim. | Move the sentence to D-exist's explanation as part of what "activity" is taken to mean, or say in A1: "the only premise beside the root". |
| K4 | Low | D-whole, Scholium 1 | "(\"with its members often working against it\")" | It misquotes Definition 7, which says "with its *components* often working against it". | Quote Definition 7 exactly, or change Definition 7 to "members" (members are the more apt word for conflict). |
| K5 | Low | D-whole, Domain | "This remark is not used by Definitions 7–12. It is not graded, not even 0." | Garbled: grammatically, "it" is the remark. | "Definitions 7–12 do not use this remark. Nature is not graded, not even 0." |
| K6 | Low | P1, step 6 | "its organization has lasted with no full stop, and no other whole carries it on from it" | It cites Definition 12, but "no full stop" is not one of Definition 12's three conditions; condition 2 is "no time at which it performed none of its works". The non-branching condition is asserted with no evidence named. Pass 4 C2 would change condition 2, so align the step after it. | Restate the step in Definition 12's own three conditions, and add the evidence for non-branching: a human body does not divide. |
| K7 | Low | A4, axiom; P1 frontmatter | A4: "…and I am one of its members." | Pass 4 C3 lists the unmarked identity in A2 and in D-whole Definitions 9 and 10. It is also in A4's statement, though A4's own Membership paragraph says the member is the body. | "…and the body this thinking goes with (A2) is one of its members." Or keep "I", with "(as A2 is scored)". |
| K8 | Low | P2, step 4 | "…to the degree of the lowest of their three grades, by the same rule as D-whole, Definition 8." | Definition 8 defines a whole's degree. Applying it to three works is a stipulation about the name, not a consequence of it. | "Stipulated: the collective mind happens to the degree of the lowest…, on the pattern of Definition 8." |
| K9 | Low | P2, Cap | "A2's clause (a) rests on cell theory, so this second cap is not expected to bind." | A2 (a) also rests on "goes with" (the lesion and first-person evidence) and on "human". The cap rests on all of it, and "not expected to bind" is a prediction made before scoring. | "…rests mainly on cell theory and on ordinary first-person evidence; whether the cap binds is for the collider." |

Checked and sound: the terms dependencies (D-I, D-exist → A1 → A2; D-work → D-whole → D-Nature; A3 and PR1 use only definitions; A4 → A2; P1 → A2, A3, A4; P2 → A4) form no loop. D-whole's mention of D-Nature is declared unused. Every term is defined before use, or explicitly "taken as understood". "Must" occurs in no entry but PR1.

## B. Verses (anything passes 1–4 missed)

| # | Sev. | Verse | Current | Fix |
|---|---|---|---|---|
| V1 | Med | 61 vs 75 | 61: "Whatever makes and replaces its own components does all seven as one." 75: "Where materials lie farther than diffusion reaches, it must carry… Where harm is present, it must defend." | This is K1 in verse. Until the core is settled, make 61: "…does all seven as one, wherever each is called for." Or add after 75: "Where the condition is absent, A3 still asks for the work, and the test decides." |
| V2 | Med | 120 | "We have begun to, and have begun to build minds." | It contradicts 11, 69 and 118 (whether a machine thinks is undecided; A3 grades today's AI no whole), and it isn't marked as a reading. Fix: "…and have begun to build machines that say 'I'." |
| V3 | Low | 101 | "The levels stop short of Nature, which is not a whole and has no members." | 55 and D-Nature say "neither a whole nor a non-whole". "Not a whole" reads as a grade of zero, the false zero D-Nature withdrew. Fix: "…Nature, which is neither a whole nor a non-whole, and has no members." |
| V4 | Low | 137 | "Freedom that is only an inner cause at work…" | It is Kant's phrase, but "inner" brings back the inside/outside picture that house rule 3 retires. Fix: "…only a cause in the agent at work…", or quote Kant directly. |

Checked, with nothing new: "fractal" appears nowhere in v12, in v12_changes or in core. The "inside" uses are only the ones already listed (IV header, 120, 142), plus 66, which is literal. "Part" is used for member only, except in reports (50, 117). The 0/1/2 grades and the lowest-grade rule are consistent.

## C. Notes and v12_changes.md against v11

| # | Sev. | Location | Current | Fix |
|---|---|---|---|---|
| N1 | Med | v12 notes, house rule (5); note for 152 | "A declared reading adds no confidence (METHOD rule 5)"; "152. METHOD rule 5." | METHOD rule 5 says the opposite kind of thing (K2). Cite A2 (b) and D-Nature for "adds no confidence", or fix K2 first. |
| N2 | Low | changes, Kept verbatim: "130 (→143)" | v11 130: "A people may be freer…"; v12 143: "A society may be freer…" | The change is not disclosed (157's is). Fix: "130 (→143, 'people' → 'society')". |
| N3 | Low | changes, Rewritten: "60 (→23)", "103 (→91)", "132 (→162)" | Listed as rewritten. | All three are word for word. Move them to Kept verbatim. |
| N4 | Low | changes, v11 accounting | — | v11 15 ("Once joined, parts and whole shape each other…") and v11 98 ("A sign means through its differences…") appear in no list. Add both, probably under "No entry carries the fact". |
| N5 | Low | changes, Dropped | "Norm verses 49, 128, 139 and 159 are dropped…" | 128, 139 and 159 also appear under "Folded elsewhere or redundant" (in "128–129", "139" and "159"). List each once. |
| N6 | Low | note 133 | "133. *D-Nature Scholium 4; D-whole.*" | D-Nature Scholium 4 says every graded whole is constrained, which is the opposite of "free by degrees". Fix with pass 1 H1: cite Scholium 4 for the first sentence only, and the thesis for the rest. |
| N7 | Low | note 57 | "…and in Nature is not member of." | Garbled. Fix: "…and being in Nature is not being a member of it (D-Nature)." |

Also verified correct: the notes' v11 sources for 9 (v11 149), 12 (57), 24 (61), 41 (13), 46 (14), 50 (24), 52 (22), 70 (153), 78 (152), 105 (115), 119 (138), 135 (90), 136 (91), 153 (154 minus its last sentence, which is in 115 as said), 157 (148 shortened), 163 (160) and 165 (161). The v11 verse count is 162.

## Comparison with passes 1–4

- **Confirmed:** both highs (H1 132/133, H2 freedom without entry), pass 3 N1, and pass 4 C1–C3. K1 is new and is a different conflict from C1. C1 is A3 against A4 (societies). K1 is A3 against PR1 (conditional works), and it applies to cells too.
- **Disagree, pass 4 "Checked and fine":** it said the core had no further internal problems. K1, K2, K4 and K5 are core-internal and were missed.
- **Disagree, pass 3 N2 (verse 62, "not wholly independent" because Definition 11 names the edge):** overstated. Definition 11 asks that the edge's components be *made*. The boundary work asks that the edge *sort*. PR1 itself separates the two ("The requirement is in the sorting"). The tests share a word, not a criterion. A note is enough; no rewording is needed.
- **Disagree, pass 2 N12 (157 "garbled"):** "a whole's term ending" is plain enough. If 156 is fixed under pass 4 C6, 157 can stay.
- **Agree, pass 4 C7:** P1's unclosed `**References.` is still there.
- **Agree, pass 4:** merge the fixes before editing.

## Convergence

New finds per pass: 19 → 18 → 14 → ~18 (mostly core and fix conflicts) → 20 here, but the severity is concentrated. At verse level this pass found only 4, two of them medium. The notes and change log yielded 7, all bookkeeping, now done mechanically and complete. The core still yielded one genuine high (K1) and one real terminology split (K2). These come from reading the entries against each other, not the verses.

To be honest about it: **another pass on the unchanged text is not useful.** The verse layer and the change log are exhausted, and the core has now had two dedicated reads. The remaining value is in decisions: K1, K2, C1–C3 and freedom. After those, apply the merged fixes and run one final check on the revised text.
