# SNAPSHOT-v1 — core_v3 rebuilt axiom set

**When:** 2026-10-24 Pacific (America/Los_Angeles).
**Tip at snapshot write:** `39324e6` (Core v3: revive parked kiln half one-by-one).
**Repo:** `neuresthetics/freedom_of_necessity` · path `candidates/core_v3/`.
**Local only** — this commit/tag is not pushed.

## Counts

| Measure | N |
|---|---|
| BASE (locked) | 20 |
| Live expansion | 231 |
| **In play (BASE + expansion)** | **251** |
| Revived this pass (from kiln park) | 109 |
| Still parked (kiln leftovers) | 17 |
| PARKED_VOLUME (earlier volume prune, untouched) | 72 |
| Prior kiln live expansion (for comparison) | 122 |
| Prior kiln kept set (BASE + 122) | 142 |

## dep_check

Command: `python3 candidates/core_v3/tools/dep_check.py`

```
live entries: 251
orphan cites: 0
orphan terms: 0
orphan rests: 0
missing rests (non-root): 0
missing cap: 0
missing hyper-connect: 0
cycles: 0
```

**Exit code: 0.** Zero cycles, zero orphans, caps and rests present.

## Pointer

Per-id merge/park reasons: [REVIVE_DECISIONS.md](REVIVE_DECISIONS.md). Narrative: [REVIVE.md](REVIVE.md). Prior kiln: [KILNED.md](KILNED.md).

## 1. Revived 109 (from kiln park)

Fields from YAML front matter. No `tier` key in these files; `group` listed instead.

| # | Id | Type | Group | Confidence | Kind | Title |
|---|---|---|---|---|---|---|
| 1 | D-adequate-cause-here | expansion | necessity_freedom | pending (collider) | definition | Adequate cause (in this chain) |
| 2 | D-art-signal | expansion | language_comm | pending (collider) | definition | Art as affective signaling |
| 3 | D-bad-relative | expansion | affects_end | pending (collider) | definition | Bad (relative to organization) |
| 4 | D-certainty-grades | expansion | error_illusion | pending (collider) | definition | Grades of certainty |
| 5 | D-common-notion-here | expansion | nature_knowledge | pending (collider) | definition | Common notion |
| 6 | D-contingent-here | expansion | cosmology_value | pending (collider) | definition | Contingent (in this chain) |
| 7 | D-contract-signal | expansion | politics_ethics | pending (collider) | definition | Contract as binding signal |
| 8 | D-courage-practice | expansion | practices | pending (collider) | definition | Courage as standing to feared causes |
| 9 | D-doubt-method | expansion | error_illusion | pending (collider) | definition | Doubt as method |
| 10 | D-duration | expansion | time_identity | pending (collider) | definition | Duration |
| 11 | D-family-whole | expansion | society | pending (collider) | definition | Family as a whole |
| 12 | D-fear-affect | expansion | affects_end | pending (collider) | definition | Fear |
| 13 | D-firm | expansion | society | pending (collider) | definition | Firm as a whole |
| 14 | D-future-self | expansion | time_identity | pending (collider) | definition | Future self as projected organization |
| 15 | D-gene-memory | expansion | biology_deep | pending (collider) | definition | Genes as deep memory-work |
| 16 | D-good-relative | expansion | affects_end | pending (collider) | definition | Good (relative to organization) |
| 17 | D-gratitude | expansion | affects_more | pending (collider) | definition | Gratitude |
| 18 | D-habit-body | expansion | body_mind | pending (collider) | definition | Bodily habit |
| 19 | D-habit-time | expansion | time_identity | pending (collider) | definition | Habit across duration |
| 20 | D-hate-affect | expansion | affects_end | pending (collider) | definition | Hate (as affect) |
| 21 | D-hope-affect | expansion | affects_end | pending (collider) | definition | Hope |
| 22 | D-immune | expansion | biology_deep | pending (collider) | definition | Immune work as boundary/repair |
| 23 | D-infinite-sketch | expansion | cosmology_value | pending (collider) | definition | Infinite (sketch) |
| 24 | D-institution | expansion | society | pending (collider) | definition | Institution |
| 25 | D-interface | expansion | digital_mind | pending (collider) | definition | Interface |
| 26 | D-intuition-know | expansion | nature_knowledge | pending (collider) | definition | Intuition (third kind of knowing) |
| 27 | D-love-affect | expansion | affects_end | pending (collider) | definition | Love (as affect) |
| 28 | D-meaning-local | expansion | cosmology_value | pending (collider) | definition | Meaning as local significance for power |
| 29 | D-meditation | expansion | practices | pending (collider) | definition | Meditation as attention repair |
| 30 | D-mode-finite | expansion | nature_knowledge | pending (collider) | definition | Finite mode |
| 31 | D-money | expansion | economy_tech | pending (collider) | definition | Money as compressed signal |
| 32 | D-platform | expansion | economy_tech | pending (collider) | definition | Platform as attention and signal whole |
| 33 | D-pride-affect | expansion | affects_more | pending (collider) | definition | Pride |
| 34 | D-property | expansion | economy_tech | pending (collider) | definition | Property as recognized control |
| 35 | D-right-power | expansion | politics_ethics | pending (collider) | definition | Right as power in a whole |
| 36 | D-sacred-sketch | expansion | cosmology_value | pending (collider) | definition | Sacred (sketch) |
| 37 | D-shame | expansion | affects_more | pending (collider) | definition | Shame |
| 38 | D-strict-free | expansion | necessity_freedom | pending (collider) | definition | Strict freedom (Nature alone) |
| 39 | D-substance-sketch | expansion | nature_knowledge | pending (collider) | definition | Substance (sketch from this chain) |
| 40 | D-teaching | expansion | language_comm | pending (collider) | definition | Teaching |
| 41 | D-testimony | expansion | language_comm | pending (collider) | definition | Testimony |
| 42 | D-truce | expansion | conflict_peace | pending (collider) | definition | Truce |
| 43 | D-upload-sketch | expansion | digital_mind | pending (collider) | definition | Upload sketch |
| 44 | D-wonder | expansion | affects_more | pending (collider) | definition | Wonder |
| 45 | OP-abolish-war | expansion | conflict_peace | pending (collider) | open | Whether war can end permanently stays open |
| 46 | OP-why-nature | expansion | nature_knowledge | pending (collider) | open | Why Nature is this way stays open |
| 47 | P-advertising | expansion | economy_tech | pending (collider) | proposition | Advertising targets desire with outside causes |
| 48 | P-aging | expansion | time_identity | pending (collider) | proposition | Aging changes degree without ending A1 while thinking |
| 49 | P-apprenticeship | expansion | practices | pending (collider) | proposition | Apprenticeship transfers embodied habits |
| 50 | P-arms-race | expansion | conflict_peace | pending (collider) | proposition | Arms races raise boundary-work, often cut freedom |
| 51 | P-automation | expansion | economy_tech | pending (collider) | proposition | Automation moves works without adding A1 |
| 52 | P-awe | expansion | cosmology_value | pending (collider) | proposition | Awe is wonder plus vastness in the cause-map |
| 53 | P-bias | expansion | error_illusion | pending (collider) | proposition | Cognitive bias is patterned confusion |
| 54 | P-brain-organoid | expansion | edge_cases | pending (collider) | proposition | Brain organoids stress the mind clause |
| 55 | P-childhood-continuity | expansion | time_identity | pending (collider) | proposition | Childhood continuity is organizational, not total recall |
| 56 | P-chimera | expansion | edge_cases | pending (collider) | proposition | Chimeras mix member lineages in one organization |
| 57 | P-colony-whole | expansion | wholes | pending (collider) | proposition | A colony can be a whole above its members |
| 58 | P-conjoined | expansion | edge_cases | pending (collider) | proposition | Conjoined twins can share works across two first persons |
| 59 | P-crypto-memory | expansion | economy_tech | pending (collider) | proposition | Ledgers are brittle society memory |
| 60 | P-cyborg | expansion | digital_mind | pending (collider) | proposition | Cyborg membership blends tool and organism |
| 61 | P-data-body | expansion | digital_mind | pending (collider) | proposition | Data traces are partial memory outside the skin |
| 62 | P-death-and-meaning | expansion | cosmology_value | pending (collider) | proposition | Death bounds duration, not the definition of blessedness |
| 63 | P-debate | expansion | practices | pending (collider) | proposition | Debate tests cause-maps in public |
| 64 | P-deterrence | expansion | conflict_peace | pending (collider) | proposition | Deterrence is fear used as control signal |
| 65 | P-development | expansion | biology_deep | pending (collider) | proposition | Development builds works-as-one over duration |
| 66 | P-ecosystem-degree | expansion | wholes | pending (collider) | proposition | An ecosystem can be a whole to a degree |
| 67 | P-energy-intake | expansion | economy_tech | pending (collider) | proposition | Energy systems are society-level intake |
| 68 | P-envy-lowers | expansion | affects_end | pending (collider) | proposition | Envy lowers power |
| 69 | P-eternity-sketch | expansion | nature_knowledge | pending (collider) | proposition | Mind's eternity is organization under Nature, not endless time |
| 70 | P-exile | expansion | practices | pending (collider) | proposition | Exile cuts membership mid-stream |
| 71 | P-extinction | expansion | biology_deep | pending (collider) | proposition | Extinction is lineage memory ending |
| 72 | P-fever | expansion | biology_deep | pending (collider) | proposition | Fever trades short pain for repair |
| 73 | P-gaslight | expansion | error_illusion | pending (collider) | proposition | Gaslighting attacks another's cause-maps |
| 74 | P-internet-memory | expansion | society | pending (collider) | proposition | Networks can hold society-level memory |
| 75 | P-journal | expansion | practices | pending (collider) | proposition | Journaling externalizes memory for clearer maps |
| 76 | P-just-war-skeptical | expansion | conflict_peace | pending (collider) | proposition | Just-war talk must still sit under A5 and P19 |
| 77 | P-latency | expansion | digital_mind | pending (collider) | proposition | Latency limits collective control |
| 78 | P-llm-signal | expansion | digital_mind | pending (collider) | proposition | LLMs are high-bandwidth society signaling gear |
| 79 | P-market-signaling | expansion | society | pending (collider) | proposition | Prices can be society-level signaling |
| 80 | P-member-vs-citizen | expansion | society | pending (collider) | proposition | Member and citizen can come apart |
| 81 | P-microbiome | expansion | biology_deep | pending (collider) | proposition | Microbiome members blur organism boundary |
| 82 | P-miracle-denied | expansion | error_illusion | pending (collider) | proposition | Miracle as uncaused event is denied |
| 83 | P-no-miracle-ethics | expansion | cosmology_value | pending (collider) | proposition | Ethics needs no miracles |
| 84 | P-nostalgia | expansion | time_identity | pending (collider) | proposition | Nostalgia mixes joy and confused cause-maps |
| 85 | P-open-source | expansion | economy_tech | pending (collider) | proposition | Open source is shared repair of knowledge-works |
| 86 | P-overconfidence | expansion | error_illusion | pending (collider) | proposition | Overconfidence is pride in confused maps |
| 87 | P-pity-mixed | expansion | affects_end | pending (collider) | proposition | Pity can aid or bind |
| 88 | P-pleasure | expansion | biology_deep | pending (collider) | proposition | Pleasure often tracks rising power — not always |
| 89 | P-plural-goods | expansion | cosmology_value | pending (collider) | proposition | Goods can conflict across levels |
| 90 | P-police | expansion | conflict_peace | pending (collider) | proposition | Police concentrate legitimate coercion |
| 91 | P-pride-confused | expansion | affects_more | pending (collider) | proposition | Confused pride resists clearer maps |
| 92 | P-prosthetic-member | expansion | edge_cases | pending (collider) | proposition | A prosthetic can become a member-tool |
| 93 | P-reconciliation | expansion | conflict_peace | pending (collider) | proposition | Reconciliation repairs shared memory after harm |
| 94 | P-refugee | expansion | conflict_peace | pending (collider) | proposition | Refugees are members cut from one whole seeking another |
| 95 | P-regret | expansion | time_identity | pending (collider) | proposition | Regret is sadness over past causes now seen clearer |
| 96 | P-rehearsal | expansion | time_identity | pending (collider) | proposition | Rehearsal stores freer patterns |
| 97 | P-rumor | expansion | language_comm | pending (collider) | proposition | Rumor is confused society-level memory |
| 98 | P-simulation-causes | expansion | digital_mind | pending (collider) | proposition | Simulation, if real, still sits under A5 |
| 99 | P-sleep-and-A1 | expansion | body_mind | pending (collider) | proposition | A1 holds only while thinking goes on |
| 100 | P-solidarity | expansion | politics_ethics | pending (collider) | proposition | Solidarity can raise joint power without erasing members |
| 101 | P-superstition | expansion | error_illusion | pending (collider) | proposition | Superstition binds via fear and hope |
| 102 | P-supply-chain | expansion | economy_tech | pending (collider) | proposition | Supply chains are extended transform/intake |
| 103 | P-swarm-robotics | expansion | edge_cases | pending (collider) | proposition | Swarm robots can fake colony wholes |
| 104 | P-symbiosis | expansion | biology_deep | pending (collider) | proposition | Symbiosis is mutual membership across organisms |
| 105 | P-therapy-as-freedom-gear | expansion | necessity_freedom | pending (collider) | proposition | Therapy can be freedom gear |
| 106 | P-tragedy | expansion | cosmology_value | pending (collider) | proposition | Tragedy is high value colliding with necessity |
| 107 | P-translation | expansion | language_comm | pending (collider) | proposition | Translation remaps signals across organizations |
| 108 | P-transplant | expansion | edge_cases | pending (collider) | proposition | Transplant swaps members, not the whole's id overnight |
| 109 | P-update | expansion | error_illusion | pending (collider) | proposition | Bayesian-ish update can be reason gear |

## 2. Still parked 17 (leftovers)

| Id | Group | Brief reason |
|---|---|---|
| D-anger | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-contempt | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-daring | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-emulation | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-humility-affect | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-jealousy | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| D-repentance | affects_more | thin affect catalog; live already has core affect spine (desire/joy/sadness/strive/active-passive) |
| P-unemployment-affect | economy_tech | theme already saturated in kept set |
| P-humor | language_comm | thin language/signal application; kept set already covers propaganda/language/signaling |
| P-manifesto | language_comm | thin language/signal application; kept set already covers propaganda/language/signaling |
| P-prayer-signal | language_comm | thin language/signal application; kept set already covers propaganda/language/signaling |
| P-silence | language_comm | thin language/signal application; kept set already covers propaganda/language/signaling |
| D-confession | practices | thin practice application; does not add a missing structural connection to kept set |
| P-exercise | practices | thin practice application; does not add a missing structural connection to kept set |
| P-fasting | practices | thin practice application; does not add a missing structural connection to kept set |
| P-sabbath | practices | thin practice application; does not add a missing structural connection to kept set |
| P-sleep-repair | practices | thin practice application; does not add a missing structural connection to kept set |

## 3. Kept 142 for comparison (pre-revive kiln live set)

BASE **20** + kilned expansion **122** = **142** that were in play at `2e82e88` / [KILNED.md](KILNED.md), against which the 126 parked were judged.

### 3a. BASE 20

| # | Id | Title | Kind |
|---|---|---|---|
| 1 | D-I | What "I" names | definition |
| 2 | D-exist | What exists | definition |
| 3 | A1 | I exist | root |
| 4 | A2 | A human body, and its mind | axiom, empirical |
| 5 | D-work | Work, and the seven works | definition |
| 6 | D-whole | Whole, degree, member, level, self-production, sameness | definition |
| 7 | A3 | The seven works sort things the way self-production does | axiom, model |
| 8 | A4 | The society I live in is a whole to a degree | axiom, model |
| 9 | P1 | A whole at one level, a part at the next | proposition |
| 10 | P2 | A collective mind happens | proposition |
| 11 | A5 | Every event is caused | axiom, model |
| 12 | D-free | Freedom, strict and by degree | definition |
| 13 | P3 | Freedom by degrees under necessity | proposition |
| 14 | D-affect | Affect, and change of power | definition |
| 15 | D-bondage | Bondage | definition |
| 16 | D-blessedness | Blessedness | definition |
| 17 | P4 | Bondage is acting from what is outside | proposition |
| 18 | P5 | Blessedness is the power itself | proposition |
| 19 | P19 | Degree of whole tracks degree of freedom only loosely | proposition |
| 20 | P21 | Society can be freer without feeling | proposition |

### 3b. Kilned live expansion 122

| # | Id | Title | Group | Kind |
|---|---|---|---|---|
| 1 | D-brain | Brain as control gear of the body | body_mind | definition |
| 2 | D-cell | Cell as member of the body | body_mind | definition |
| 3 | D-death | Death of the body | body_mind | definition |
| 4 | D-first-person | First person | body_mind | definition |
| 5 | D-organism | Organism | body_mind | definition |
| 6 | OP-feeling | Why anything is felt stays open | body_mind | open |
| 7 | P-body-lasts | This body lasts by its works going on | body_mind | proposition |
| 8 | P-injury-lowers-degree | Injury can lower whole-degree and freedom-degree together | body_mind | proposition |
| 9 | P-mind-tracks-body | Mind tracks the body's organization | body_mind | proposition |
| 10 | P-other-bodies | Other human bodies exist on evidence | body_mind | proposition |
| 11 | D-member-degree | Degree of membership | wholes | definition |
| 12 | D-sameness-later | Same whole later | wholes | definition |
| 13 | D-work-F1 | Work: Boundary | wholes | definition |
| 14 | D-work-F2 | Work: Intake | wholes | definition |
| 15 | D-work-F3 | Work: Outflow | wholes | definition |
| 16 | D-work-F4 | Work: Transform | wholes | definition |
| 17 | D-work-F5 | Work: Repair | wholes | definition |
| 18 | D-work-F6 | Work: Signal | wholes | definition |
| 19 | D-work-F7 | Work: Memory | wholes | definition |
| 20 | P-levels-stack | Levels can stack without a top in view | wholes | proposition |
| 21 | P-machine-not-self-producer | Most machines fail at least one work as one | wholes | proposition |
| 22 | P-repair-raises-degree | Repair can raise whole-degree | wholes | proposition |
| 23 | P-take-apart-test | Take-apart test for as-one | wholes | proposition |
| 24 | P-tumor-edge | A tumor is a whole that harms the higher whole | wholes | proposition |
| 25 | P-weakest-work-rules | The weakest work sets the degree | wholes | proposition |
| 26 | PR-same-requirement | Same requirement, same work | wholes | principle |
| 27 | D-public-affect | Public mood is not corporate feeling | society | definition |
| 28 | D-state-whole | State as a whole | society | definition |
| 29 | OP-group-mind-feel | Whether any group feels as one stays open | society | open |
| 30 | P-collective-freedom-rises | Clear shared knowledge can raise collective freedom | society | proposition |
| 31 | P-corporation-without-feeling | A corporation can act freer without feeling | society | proposition |
| 32 | P-exit-voice | Exit and voice are member-level freedom gear | society | proposition |
| 33 | P-law-as-memory | Law is public memory with teeth | society | proposition |
| 34 | P-propaganda-bondage | Propaganda is bondage at society scale | society | proposition |
| 35 | D-cause | Cause | necessity_freedom | definition |
| 36 | D-clear-knowledge | Clear knowledge of causes | necessity_freedom | definition |
| 37 | D-confused-knowledge | Confused knowledge of causes | necessity_freedom | definition |
| 38 | D-power-of-acting | Power of acting | necessity_freedom | definition |
| 39 | P-addiction | Addiction is a bondage pattern | necessity_freedom | proposition |
| 40 | P-blame-reframed | Blame tracks confused causes more than strict uncaused will | necessity_freedom | proposition |
| 41 | P-choice-caused | A choice is an event and so caused | necessity_freedom | proposition |
| 42 | P-compulsion | Compulsion is high bondage | necessity_freedom | proposition |
| 43 | P-freer-knows-more-causes | Freer action tracks clearer cause-maps | necessity_freedom | proposition |
| 44 | P-habit-can-bond | Habit can be bondage or stored freedom | necessity_freedom | proposition |
| 45 | P-luck-is-incomplete | Luck names causes we do not track | necessity_freedom | proposition |
| 46 | P-prediction-not-freedom | Predictability is not the freedom scale | necessity_freedom | proposition |
| 47 | D-desire | Desire | affects_end | definition |
| 48 | D-joy | Joy | affects_end | definition |
| 49 | D-sadness | Sadness | affects_end | definition |
| 50 | D-strive | Striving to persist | affects_end | definition |
| 51 | P-active-vs-passive | Active affects follow from clearer causes | affects_end | proposition |
| 52 | P-blessedness-not-afterlife | Blessedness is not an afterlife payment | affects_end | proposition |
| 53 | P-virtue-is-power | Virtue is living from power of acting | affects_end | proposition |
| 54 | D-Nature-one | Nature taken as one | nature_knowledge | definition |
| 55 | D-imagination-know | Imagination (first kind of knowing) | nature_knowledge | definition |
| 56 | D-reason-know | Reason (second kind of knowing) | nature_knowledge | definition |
| 57 | P-more-reason-freer | More reason, freer — other things equal | nature_knowledge | proposition |
| 58 | P-no-uncaused-will | There is no uncaused will in Nature | nature_knowledge | proposition |
| 59 | P-science-as-freedom-gear | Science can be freedom gear | nature_knowledge | proposition |
| 60 | D-degree-freedom-scale | Degree-freedom scale | bridges | definition |
| 61 | D-whole-degree-scale | Whole-degree scale | bridges | definition |
| 62 | P-ai-collective | AI collectives can be wholes without feeling | bridges | proposition |
| 63 | P-cult-bondage | A cult can be a tight whole in bondage | bridges | proposition |
| 64 | P-military-whole | A military unit can be high-degree, mixed-freedom | bridges | proposition |
| 65 | P-open-science-society | Open science societies can rise on both scales | bridges | proposition |
| 66 | P-robot-member | A robot can be a member without being a self-producer | bridges | proposition |
| 67 | P-strong-whole-low-freedom | A strong whole can still be unfree | bridges | proposition |
| 68 | P-title-claim | Freedom of necessity is degree-freedom under A5 | bridges | proposition |
| 69 | P-weak-whole-high-freedom | A fragile whole can still be freer | bridges | proposition |
| 70 | D-justice-gear | Justice as freedom gear | politics_ethics | definition |
| 71 | OP-best-regime | Which regime maximizes freedom stays open | politics_ethics | open |
| 72 | P-democracy-bet | Democracy bets on distributed clear knowledge | politics_ethics | proposition |
| 73 | P-punishment-cause | Punishment under A5 is prevention and repair, not cosmic payback | politics_ethics | proposition |
| 74 | P-tyranny-bondage | Tyranny maximizes some works while flooring freedom | politics_ethics | proposition |
| 75 | D-collider | Collider | method | definition |
| 76 | D-declared-reading | Declared reading | method | definition |
| 77 | P-expansion-cites-base | Expansion must rest on BASE | method | proposition |
| 78 | PR-one-chain | One chain | method | principle |
| 79 | PR-park-not-delete | Park, don't delete | method | principle |
| 80 | D-memory-personal | Personal memory | time_identity | definition |
| 81 | D-narrative-self | Narrative self | time_identity | definition |
| 82 | P-amnesia | Amnesia cuts memory-work, not existence | time_identity | proposition |
| 83 | P-promise | A promise binds memory and future control | time_identity | proposition |
| 84 | P-brain-death | Brain death floors organism-level control | edge_cases | proposition |
| 85 | P-coma | Coma suspends clear first-person report | edge_cases | proposition |
| 86 | P-locked-in | Locked-in can trap high mind-description with low outflow | edge_cases | proposition |
| 87 | P-pregnancy-levels | Pregnancy nests wholes | edge_cases | proposition |
| 88 | P-split-brain | Split brain challenges unity of first person | edge_cases | proposition |
| 89 | P-virus-edge | A virus sits at the edge of self-production | edge_cases | proposition |
| 90 | D-language | Language as shared signaling | language_comm | definition |
| 91 | D-lie | Lie | language_comm | definition |
| 92 | P-naming | Naming stabilizes common notions | language_comm | proposition |
| 93 | D-tool | Tool | economy_tech | definition |
| 94 | OP-agi-freedom | Whether AGI gets degree-freedom talk stays open | economy_tech | open |
| 95 | P-debt-bondage | Debt can be structured bondage | economy_tech | proposition |
| 96 | P-surveillance | Surveillance amplifies control-work | economy_tech | proposition |
| 97 | D-compassion | Compassion | affects_more | definition |
| 98 | P-anger-can-repair | Anger can feed repair or bondage | affects_more | proposition |
| 99 | P-compassion-freedom | Compassion can raise joint freedom | affects_more | proposition |
| 100 | D-education | Education as long teaching | practices | definition |
| 101 | D-friendship | Friendship | practices | definition |
| 102 | P-habit-stack | Stacked small habits compound degree-freedom | practices | proposition |
| 103 | D-peace | Peace as stable non-destruction among wholes | conflict_peace | definition |
| 104 | D-war | War as organized harm between wholes | conflict_peace | definition |
| 105 | P-civil-war | Civil war splits one society-whole | conflict_peace | proposition |
| 106 | P-war-drops-degree | War floors many works even for winners | conflict_peace | proposition |
| 107 | D-error | Error | error_illusion | definition |
| 108 | D-illusion | Illusion | error_illusion | definition |
| 109 | P-final-causes-heuristic | Final-cause talk is often heuristic imagination | error_illusion | proposition |
| 110 | P-free-will-illusion | The feeling of uncaused will is illusion under A5 | error_illusion | proposition |
| 111 | OP-machine-feeling | Whether machines feel stays open | digital_mind | open |
| 112 | P-alignment-freedom | Alignment is contested control over AI cause-maps | digital_mind | proposition |
| 113 | P-bot-swarm-bondage | Bot swarms can manufacture consent-looking signal | digital_mind | proposition |
| 114 | P-copy-not-A1-transfer | Copying a pattern does not transfer this A1 | digital_mind | proposition |
| 115 | P-digital-A1 | A digital system can utter A1; certainty is not settled by utterance | digital_mind | proposition |
| 116 | OP-why-anything | Why anything exists at all stays open | cosmology_value | open |
| 117 | P-apparent-contingency | Apparent contingency is incomplete knowledge | cosmology_value | proposition |
| 118 | P-nihilism-confused | Nihilism often confuses missing cosmic purpose with missing local good | cosmology_value | proposition |
| 119 | D-homeostasis | Homeostasis | biology_deep | definition |
| 120 | P-cancer-defection | Cancer is member defection into a rival whole | biology_deep | proposition |
| 121 | P-evolution | Evolution is population-level transform of organization | biology_deep | proposition |
| 122 | P-pain | Pain signals threat to works | biology_deep | proposition |

## 4. How 251 is composed

`251 = BASE 20 + (kilned live 122 + revived 109) = 20 + 231`.
Still parked kiln leftovers: 17. PARKED_VOLUME earlier prune: untouched.

