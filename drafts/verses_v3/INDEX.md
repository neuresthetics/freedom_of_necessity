# Verses v3 — shared INDEX (dual track)

**Core:** `candidates/core_v3/` at snapshot `core-v3-snapshot-v1` (`ce3d91a`).
**Tracks:** [technical/](technical/) · [poetic/](poetic/)
**Rule:** same verse number **Vnnn** and same index label (**entry id**) in both tracks. A number exists in both or in neither.

## Numbering

| Field | Rule |
|---|---|
| **Verse number** | `V001`–`V251` — zero-padded, stable |
| **Index label** | Entry id (`A1`, `D-I`, `P3`, `P-choice-caused`, …) |
| **Order** | BASE locked spine **V001–V020** (exactly [BASE.md](../../candidates/core_v3/BASE.md) order), then live expansion **V021–V251** by group (CHAIN / expansion INDEX order), id ascending within group |
| **Pairing** | One primary verse per live entry (251 pairs when complete) |
| **Tags (both tracks)** | End or header carries `[id]`; technical also carries kind, rests-on, cap, confidence |

Groups after BASE: `body_mind`, `wholes`, `society`, `necessity_freedom`, `affects_end`, `nature_knowledge`, `bridges`, `politics_ethics`, `method`, `time_identity`, `edge_cases`, `language_comm`, `economy_tech`, `affects_more`, `practices`, `conflict_peace`, `error_illusion`, `digital_mind`, `cosmology_value`, `biology_deep`.

## Track roles

1. **Technical** — dependency analysis, rests-on / supports, confidence caps, entry ids, Spinoza by part/prop only (no Kisner pages), public-safe wording, "digital intelligence" where A1/D-I speak of machines.
2. **Poetic** — Dhammapada-like, modern plain language, short lines, analogy only when it clarifies; readable without jargon; no score tables.

Standing constraints (both): one unified chain; A1 = "I exist" only axiom root; collision record is the book; public-safe.

## Progress

| Block | Verse range | Technical | Poetic |
|---|---|---|---|
| BASE (locked) | V001–V020 | done | done |
| Expansion | V021–V251 | first pass | first pass |

See [PROGRESS.md](PROGRESS.md).

## Prior verse drafts (do not renumber those files)

- `drafts/verses/axioms_of_necessity_v10.md` … `v12.md` — old numbering; **v12 numbering ≠ this INDEX**.
- This dual track is a **new** numbering keyed to core_v3 live ids.

## Author-written lines (Jason) — mapping

| Old (v12) | Text (summary) | Maps into v3 |
|---|---|---|
| **143** | Freedom doesn't need could-have-done-otherwise; needs that what you did came from you | **V013 · P3** (poetic track preserves verbatim; technical credits) |
| **144** | Understand a cause = know origin; freedom is knowing and acting, not escaping | **V013 · P3** (same) |
| **86** | An explanation is a lamp, not a proof… | **Open:** PR1 is parked (`PARKED_VOLUME/PR1.md`). Closest live homes: **V050 · PR-same-requirement** (pattern/requirement) and **V125 · D-collider** (scoring/evidence). Not forced into a number until Jason picks. |
| **80** (pattern line) | "function follows necessity/requirement" | **V050 · PR-same-requirement** (note open word choice) |
| **53** (v12) | "There is one order…" | Nature-one / reading territory — **V101 · D-Nature-one**; keep as reading, not BASE |

## Full label table (251)

| V# | Id | Title | Kind | Group |
|---|---|---|---|---|
| 001 | `D-I` | What "I" names | definition | BASE |
| 002 | `D-exist` | What exists | definition | BASE |
| 003 | `A1` | I exist | self-evident | BASE |
| 004 | `A2` | A human body, and its mind | empirical | BASE |
| 005 | `D-work` | Work, and the seven works | definition | BASE |
| 006 | `D-whole` | Whole, degree, member, level, self-production, sameness | definition | BASE |
| 007 | `A3` | The seven works sort things the way self-production does | model | BASE |
| 008 | `A4` | The society I live in is a whole to a degree | model | BASE |
| 009 | `P1` | A whole at one level, a part at the next | derived | BASE |
| 010 | `P2` | A collective mind happens | derived | BASE |
| 011 | `A5` | Every event is caused | model | BASE |
| 012 | `D-free` | Freedom, strict and by degree | definition | BASE |
| 013 | `P3` | Freedom by degrees under necessity | derived | BASE |
| 014 | `D-affect` | Affect, and change of power | definition | BASE |
| 015 | `D-bondage` | Bondage | definition | BASE |
| 016 | `D-blessedness` | Blessedness | definition | BASE |
| 017 | `P4` | Bondage is acting from what is outside | derived | BASE |
| 018 | `P5` | Blessedness is the power itself | derived | BASE |
| 019 | `P19` | Degree of whole tracks degree of freedom only loosely | derived | BASE |
| 020 | `P21` | Society can be freer without feeling | derived | BASE |
| 021 | `D-brain` | Brain as control gear of the body | definition | body_mind |
| 022 | `D-cell` | Cell as member of the body | definition | body_mind |
| 023 | `D-death` | Death of the body | definition | body_mind |
| 024 | `D-first-person` | First person | definition | body_mind |
| 025 | `D-habit-body` | Bodily habit | definition | body_mind |
| 026 | `D-organism` | Organism | definition | body_mind |
| 027 | `OP-feeling` | Why anything is felt stays open | open | body_mind |
| 028 | `P-body-lasts` | This body lasts by its works going on | proposition | body_mind |
| 029 | `P-injury-lowers-degree` | Injury can lower whole-degree and freedom-degree together | proposition | body_mind |
| 030 | `P-mind-tracks-body` | Mind tracks the body's organization | proposition | body_mind |
| 031 | `P-other-bodies` | Other human bodies exist on evidence | proposition | body_mind |
| 032 | `P-sleep-and-A1` | A1 holds only while thinking goes on | proposition | body_mind |
| 033 | `D-member-degree` | Degree of membership | definition | wholes |
| 034 | `D-sameness-later` | Same whole later | definition | wholes |
| 035 | `D-work-F1` | Work: Boundary | definition | wholes |
| 036 | `D-work-F2` | Work: Intake | definition | wholes |
| 037 | `D-work-F3` | Work: Outflow | definition | wholes |
| 038 | `D-work-F4` | Work: Transform | definition | wholes |
| 039 | `D-work-F5` | Work: Repair | definition | wholes |
| 040 | `D-work-F6` | Work: Signal | definition | wholes |
| 041 | `D-work-F7` | Work: Memory | definition | wholes |
| 042 | `P-colony-whole` | A colony can be a whole above its members | proposition | wholes |
| 043 | `P-ecosystem-degree` | An ecosystem can be a whole to a degree | proposition | wholes |
| 044 | `P-levels-stack` | Levels can stack without a top in view | proposition | wholes |
| 045 | `P-machine-not-self-producer` | Most machines fail at least one work as one | proposition | wholes |
| 046 | `P-repair-raises-degree` | Repair can raise whole-degree | proposition | wholes |
| 047 | `P-take-apart-test` | Take-apart test for as-one | proposition | wholes |
| 048 | `P-tumor-edge` | A tumor is a whole that harms the higher whole | proposition | wholes |
| 049 | `P-weakest-work-rules` | The weakest work sets the degree | proposition | wholes |
| 050 | `PR-same-requirement` | Same requirement, same work | principle | wholes |
| 051 | `D-family-whole` | Family as a whole | definition | society |
| 052 | `D-firm` | Firm as a whole | definition | society |
| 053 | `D-institution` | Institution | definition | society |
| 054 | `D-public-affect` | Public mood is not corporate feeling | definition | society |
| 055 | `D-state-whole` | State as a whole | definition | society |
| 056 | `OP-group-mind-feel` | Whether any group feels as one stays open | open | society |
| 057 | `P-collective-freedom-rises` | Clear shared knowledge can raise collective freedom | proposition | society |
| 058 | `P-corporation-without-feeling` | A corporation can act freer without feeling | proposition | society |
| 059 | `P-exit-voice` | Exit and voice are member-level freedom gear | proposition | society |
| 060 | `P-internet-memory` | Networks can hold society-level memory | proposition | society |
| 061 | `P-law-as-memory` | Law is public memory with teeth | proposition | society |
| 062 | `P-market-signaling` | Prices can be society-level signaling | proposition | society |
| 063 | `P-member-vs-citizen` | Member and citizen can come apart | proposition | society |
| 064 | `P-propaganda-bondage` | Propaganda is bondage at society scale | proposition | society |
| 065 | `D-adequate-cause-here` | Adequate cause (in this chain) | definition | necessity_freedom |
| 066 | `D-cause` | Cause | definition | necessity_freedom |
| 067 | `D-clear-knowledge` | Clear knowledge of causes | definition | necessity_freedom |
| 068 | `D-confused-knowledge` | Confused knowledge of causes | definition | necessity_freedom |
| 069 | `D-power-of-acting` | Power of acting | definition | necessity_freedom |
| 070 | `D-strict-free` | Strict freedom (Nature alone) | definition | necessity_freedom |
| 071 | `P-addiction` | Addiction is a bondage pattern | proposition | necessity_freedom |
| 072 | `P-blame-reframed` | Blame tracks confused causes more than strict uncaused will | proposition | necessity_freedom |
| 073 | `P-choice-caused` | A choice is an event and so caused | proposition | necessity_freedom |
| 074 | `P-compulsion` | Compulsion is high bondage | proposition | necessity_freedom |
| 075 | `P-freer-knows-more-causes` | Freer action tracks clearer cause-maps | proposition | necessity_freedom |
| 076 | `P-habit-can-bond` | Habit can be bondage or stored freedom | proposition | necessity_freedom |
| 077 | `P-luck-is-incomplete` | Luck names causes we do not track | proposition | necessity_freedom |
| 078 | `P-prediction-not-freedom` | Predictability is not the freedom scale | proposition | necessity_freedom |
| 079 | `P-therapy-as-freedom-gear` | Therapy can be freedom gear | proposition | necessity_freedom |
| 080 | `D-bad-relative` | Bad (relative to organization) | definition | affects_end |
| 081 | `D-desire` | Desire | definition | affects_end |
| 082 | `D-fear-affect` | Fear | definition | affects_end |
| 083 | `D-good-relative` | Good (relative to organization) | definition | affects_end |
| 084 | `D-hate-affect` | Hate (as affect) | definition | affects_end |
| 085 | `D-hope-affect` | Hope | definition | affects_end |
| 086 | `D-joy` | Joy | definition | affects_end |
| 087 | `D-love-affect` | Love (as affect) | definition | affects_end |
| 088 | `D-sadness` | Sadness | definition | affects_end |
| 089 | `D-strive` | Striving to persist | definition | affects_end |
| 090 | `P-active-vs-passive` | Active affects follow from clearer causes | proposition | affects_end |
| 091 | `P-blessedness-not-afterlife` | Blessedness is not an afterlife payment | proposition | affects_end |
| 092 | `P-envy-lowers` | Envy lowers power | proposition | affects_end |
| 093 | `P-pity-mixed` | Pity can aid or bind | proposition | affects_end |
| 094 | `P-virtue-is-power` | Virtue is living from power of acting | proposition | affects_end |
| 095 | `D-Nature-one` | Nature taken as one | definition | nature_knowledge |
| 096 | `D-common-notion-here` | Common notion | definition | nature_knowledge |
| 097 | `D-imagination-know` | Imagination (first kind of knowing) | definition | nature_knowledge |
| 098 | `D-intuition-know` | Intuition (third kind of knowing) | definition | nature_knowledge |
| 099 | `D-mode-finite` | Finite mode | definition | nature_knowledge |
| 100 | `D-reason-know` | Reason (second kind of knowing) | definition | nature_knowledge |
| 101 | `D-substance-sketch` | Substance (sketch from this chain) | definition | nature_knowledge |
| 102 | `OP-why-nature` | Why Nature is this way stays open | open | nature_knowledge |
| 103 | `P-eternity-sketch` | Mind's eternity is organization under Nature, not endless time | proposition | nature_knowledge |
| 104 | `P-more-reason-freer` | More reason, freer — other things equal | proposition | nature_knowledge |
| 105 | `P-no-uncaused-will` | There is no uncaused will in Nature | proposition | nature_knowledge |
| 106 | `P-science-as-freedom-gear` | Science can be freedom gear | proposition | nature_knowledge |
| 107 | `D-degree-freedom-scale` | Degree-freedom scale | definition | bridges |
| 108 | `D-whole-degree-scale` | Whole-degree scale | definition | bridges |
| 109 | `P-ai-collective` | AI collectives can be wholes without feeling | proposition | bridges |
| 110 | `P-cult-bondage` | A cult can be a tight whole in bondage | proposition | bridges |
| 111 | `P-military-whole` | A military unit can be high-degree, mixed-freedom | proposition | bridges |
| 112 | `P-open-science-society` | Open science societies can rise on both scales | proposition | bridges |
| 113 | `P-robot-member` | A robot can be a member without being a self-producer | proposition | bridges |
| 114 | `P-strong-whole-low-freedom` | A strong whole can still be unfree | proposition | bridges |
| 115 | `P-title-claim` | Freedom of necessity is degree-freedom under A5 | proposition | bridges |
| 116 | `P-weak-whole-high-freedom` | A fragile whole can still be freer | proposition | bridges |
| 117 | `D-contract-signal` | Contract as binding signal | definition | politics_ethics |
| 118 | `D-justice-gear` | Justice as freedom gear | definition | politics_ethics |
| 119 | `D-right-power` | Right as power in a whole | definition | politics_ethics |
| 120 | `OP-best-regime` | Which regime maximizes freedom stays open | open | politics_ethics |
| 121 | `P-democracy-bet` | Democracy bets on distributed clear knowledge | proposition | politics_ethics |
| 122 | `P-punishment-cause` | Punishment under A5 is prevention and repair, not cosmic payback | proposition | politics_ethics |
| 123 | `P-solidarity` | Solidarity can raise joint power without erasing members | proposition | politics_ethics |
| 124 | `P-tyranny-bondage` | Tyranny maximizes some works while flooring freedom | proposition | politics_ethics |
| 125 | `D-collider` | Collider | definition | method |
| 126 | `D-declared-reading` | Declared reading | definition | method |
| 127 | `P-expansion-cites-base` | Expansion must rest on BASE | proposition | method |
| 128 | `PR-one-chain` | One chain | principle | method |
| 129 | `PR-park-not-delete` | Park, don't delete | principle | method |
| 130 | `D-duration` | Duration | definition | time_identity |
| 131 | `D-future-self` | Future self as projected organization | definition | time_identity |
| 132 | `D-habit-time` | Habit across duration | definition | time_identity |
| 133 | `D-memory-personal` | Personal memory | definition | time_identity |
| 134 | `D-narrative-self` | Narrative self | definition | time_identity |
| 135 | `P-aging` | Aging changes degree without ending A1 while thinking | proposition | time_identity |
| 136 | `P-amnesia` | Amnesia cuts memory-work, not existence | proposition | time_identity |
| 137 | `P-childhood-continuity` | Childhood continuity is organizational, not total recall | proposition | time_identity |
| 138 | `P-nostalgia` | Nostalgia mixes joy and confused cause-maps | proposition | time_identity |
| 139 | `P-promise` | A promise binds memory and future control | proposition | time_identity |
| 140 | `P-regret` | Regret is sadness over past causes now seen clearer | proposition | time_identity |
| 141 | `P-rehearsal` | Rehearsal stores freer patterns | proposition | time_identity |
| 142 | `P-brain-death` | Brain death floors organism-level control | proposition | edge_cases |
| 143 | `P-brain-organoid` | Brain organoids stress the mind clause | proposition | edge_cases |
| 144 | `P-chimera` | Chimeras mix member lineages in one organization | proposition | edge_cases |
| 145 | `P-coma` | Coma suspends clear first-person report | proposition | edge_cases |
| 146 | `P-conjoined` | Conjoined twins can share works across two first persons | proposition | edge_cases |
| 147 | `P-locked-in` | Locked-in can trap high mind-description with low outflow | proposition | edge_cases |
| 148 | `P-pregnancy-levels` | Pregnancy nests wholes | proposition | edge_cases |
| 149 | `P-prosthetic-member` | A prosthetic can become a member-tool | proposition | edge_cases |
| 150 | `P-split-brain` | Split brain challenges unity of first person | proposition | edge_cases |
| 151 | `P-swarm-robotics` | Swarm robots can fake colony wholes | proposition | edge_cases |
| 152 | `P-transplant` | Transplant swaps members, not the whole's id overnight | proposition | edge_cases |
| 153 | `P-virus-edge` | A virus sits at the edge of self-production | proposition | edge_cases |
| 154 | `D-art-signal` | Art as affective signaling | definition | language_comm |
| 155 | `D-language` | Language as shared signaling | definition | language_comm |
| 156 | `D-lie` | Lie | definition | language_comm |
| 157 | `D-teaching` | Teaching | definition | language_comm |
| 158 | `D-testimony` | Testimony | definition | language_comm |
| 159 | `P-naming` | Naming stabilizes common notions | proposition | language_comm |
| 160 | `P-rumor` | Rumor is confused society-level memory | proposition | language_comm |
| 161 | `P-translation` | Translation remaps signals across organizations | proposition | language_comm |
| 162 | `D-money` | Money as compressed signal | definition | economy_tech |
| 163 | `D-platform` | Platform as attention and signal whole | definition | economy_tech |
| 164 | `D-property` | Property as recognized control | definition | economy_tech |
| 165 | `D-tool` | Tool | definition | economy_tech |
| 166 | `OP-agi-freedom` | Whether AGI gets degree-freedom talk stays open | open | economy_tech |
| 167 | `P-advertising` | Advertising targets desire with outside causes | proposition | economy_tech |
| 168 | `P-automation` | Automation moves works without adding A1 | proposition | economy_tech |
| 169 | `P-crypto-memory` | Ledgers are brittle society memory | proposition | economy_tech |
| 170 | `P-debt-bondage` | Debt can be structured bondage | proposition | economy_tech |
| 171 | `P-energy-intake` | Energy systems are society-level intake | proposition | economy_tech |
| 172 | `P-open-source` | Open source is shared repair of knowledge-works | proposition | economy_tech |
| 173 | `P-supply-chain` | Supply chains are extended transform/intake | proposition | economy_tech |
| 174 | `P-surveillance` | Surveillance amplifies control-work | proposition | economy_tech |
| 175 | `D-compassion` | Compassion | definition | affects_more |
| 176 | `D-gratitude` | Gratitude | definition | affects_more |
| 177 | `D-pride-affect` | Pride | definition | affects_more |
| 178 | `D-shame` | Shame | definition | affects_more |
| 179 | `D-wonder` | Wonder | definition | affects_more |
| 180 | `P-anger-can-repair` | Anger can feed repair or bondage | proposition | affects_more |
| 181 | `P-compassion-freedom` | Compassion can raise joint freedom | proposition | affects_more |
| 182 | `P-pride-confused` | Confused pride resists clearer maps | proposition | affects_more |
| 183 | `D-courage-practice` | Courage as standing to feared causes | definition | practices |
| 184 | `D-education` | Education as long teaching | definition | practices |
| 185 | `D-friendship` | Friendship | definition | practices |
| 186 | `D-meditation` | Meditation as attention repair | definition | practices |
| 187 | `P-apprenticeship` | Apprenticeship transfers embodied habits | proposition | practices |
| 188 | `P-debate` | Debate tests cause-maps in public | proposition | practices |
| 189 | `P-exile` | Exile cuts membership mid-stream | proposition | practices |
| 190 | `P-habit-stack` | Stacked small habits compound degree-freedom | proposition | practices |
| 191 | `P-journal` | Journaling externalizes memory for clearer maps | proposition | practices |
| 192 | `D-peace` | Peace as stable non-destruction among wholes | definition | conflict_peace |
| 193 | `D-truce` | Truce | definition | conflict_peace |
| 194 | `D-war` | War as organized harm between wholes | definition | conflict_peace |
| 195 | `OP-abolish-war` | Whether war can end permanently stays open | open | conflict_peace |
| 196 | `P-arms-race` | Arms races raise boundary-work, often cut freedom | proposition | conflict_peace |
| 197 | `P-civil-war` | Civil war splits one society-whole | proposition | conflict_peace |
| 198 | `P-deterrence` | Deterrence is fear used as control signal | proposition | conflict_peace |
| 199 | `P-just-war-skeptical` | Just-war talk must still sit under A5 and P19 | proposition | conflict_peace |
| 200 | `P-police` | Police concentrate legitimate coercion | proposition | conflict_peace |
| 201 | `P-reconciliation` | Reconciliation repairs shared memory after harm | proposition | conflict_peace |
| 202 | `P-refugee` | Refugees are members cut from one whole seeking another | proposition | conflict_peace |
| 203 | `P-war-drops-degree` | War floors many works even for winners | proposition | conflict_peace |
| 204 | `D-certainty-grades` | Grades of certainty | definition | error_illusion |
| 205 | `D-doubt-method` | Doubt as method | definition | error_illusion |
| 206 | `D-error` | Error | definition | error_illusion |
| 207 | `D-illusion` | Illusion | definition | error_illusion |
| 208 | `P-bias` | Cognitive bias is patterned confusion | proposition | error_illusion |
| 209 | `P-final-causes-heuristic` | Final-cause talk is often heuristic imagination | proposition | error_illusion |
| 210 | `P-free-will-illusion` | The feeling of uncaused will is illusion under A5 | proposition | error_illusion |
| 211 | `P-gaslight` | Gaslighting attacks another's cause-maps | proposition | error_illusion |
| 212 | `P-miracle-denied` | Miracle as uncaused event is denied | proposition | error_illusion |
| 213 | `P-overconfidence` | Overconfidence is pride in confused maps | proposition | error_illusion |
| 214 | `P-superstition` | Superstition binds via fear and hope | proposition | error_illusion |
| 215 | `P-update` | Bayesian-ish update can be reason gear | proposition | error_illusion |
| 216 | `D-interface` | Interface | definition | digital_mind |
| 217 | `D-upload-sketch` | Upload sketch | definition | digital_mind |
| 218 | `OP-machine-feeling` | Whether machines feel stays open | open | digital_mind |
| 219 | `P-alignment-freedom` | Alignment is contested control over AI cause-maps | proposition | digital_mind |
| 220 | `P-bot-swarm-bondage` | Bot swarms can manufacture consent-looking signal | proposition | digital_mind |
| 221 | `P-copy-not-A1-transfer` | Copying a pattern does not transfer this A1 | proposition | digital_mind |
| 222 | `P-cyborg` | Cyborg membership blends tool and organism | proposition | digital_mind |
| 223 | `P-data-body` | Data traces are partial memory outside the skin | proposition | digital_mind |
| 224 | `P-digital-A1` | A digital system can utter A1; certainty is not settled by utterance | proposition | digital_mind |
| 225 | `P-latency` | Latency limits collective control | proposition | digital_mind |
| 226 | `P-llm-signal` | LLMs are high-bandwidth society signaling gear | proposition | digital_mind |
| 227 | `P-simulation-causes` | Simulation, if real, still sits under A5 | proposition | digital_mind |
| 228 | `D-contingent-here` | Contingent (in this chain) | definition | cosmology_value |
| 229 | `D-infinite-sketch` | Infinite (sketch) | definition | cosmology_value |
| 230 | `D-meaning-local` | Meaning as local significance for power | definition | cosmology_value |
| 231 | `D-sacred-sketch` | Sacred (sketch) | definition | cosmology_value |
| 232 | `OP-why-anything` | Why anything exists at all stays open | open | cosmology_value |
| 233 | `P-apparent-contingency` | Apparent contingency is incomplete knowledge | proposition | cosmology_value |
| 234 | `P-awe` | Awe is wonder plus vastness in the cause-map | proposition | cosmology_value |
| 235 | `P-death-and-meaning` | Death bounds duration, not the definition of blessedness | proposition | cosmology_value |
| 236 | `P-nihilism-confused` | Nihilism often confuses missing cosmic purpose with missing local good | proposition | cosmology_value |
| 237 | `P-no-miracle-ethics` | Ethics needs no miracles | proposition | cosmology_value |
| 238 | `P-plural-goods` | Goods can conflict across levels | proposition | cosmology_value |
| 239 | `P-tragedy` | Tragedy is high value colliding with necessity | proposition | cosmology_value |
| 240 | `D-gene-memory` | Genes as deep memory-work | definition | biology_deep |
| 241 | `D-homeostasis` | Homeostasis | definition | biology_deep |
| 242 | `D-immune` | Immune work as boundary/repair | definition | biology_deep |
| 243 | `P-cancer-defection` | Cancer is member defection into a rival whole | proposition | biology_deep |
| 244 | `P-development` | Development builds works-as-one over duration | proposition | biology_deep |
| 245 | `P-evolution` | Evolution is population-level transform of organization | proposition | biology_deep |
| 246 | `P-extinction` | Extinction is lineage memory ending | proposition | biology_deep |
| 247 | `P-fever` | Fever trades short pain for repair | proposition | biology_deep |
| 248 | `P-microbiome` | Microbiome members blur organism boundary | proposition | biology_deep |
| 249 | `P-pain` | Pain signals threat to works | proposition | biology_deep |
| 250 | `P-pleasure` | Pleasure often tracks rising power — not always | proposition | biology_deep |
| 251 | `P-symbiosis` | Symbiosis is mutual membership across organisms | proposition | biology_deep |

## File layout

```
drafts/verses_v3/
  INDEX.md                 ← this file (shared numbering)
  PROGRESS.md
  technical/BASE.md        ← V001–V020
  technical/expansion.md   ← V021–V251
  poetic/BASE.md           ← V001–V020
  poetic/expansion.md      ← V021–V251
```
