# Model choice

Which local model the harness uses, why it was chosen, and why we think the benefits
outweigh the known drawbacks. It also lists the checks that are planned but not yet run.

## The model

- **Model:** Ollama `orcarouter/Qwen3.8-27B-Uncensored:q4_K_M`
- **Hardware:** NVIDIA RTX 4000 Ada (20 GB of video memory); full specs in [HARDWARE.md](HARDWARE.md)
- **Memory use:** about 17.7 GB
- **Speed:** about 16 tokens per second
- **Operation:** one model loaded at a time
- **Why this size:** it is the largest model that fits on the card with some memory to spare.

## The base model

The model is built on Qwen3.8-27B, released by Alibaba's Qwen team on 2026-08-14 under the
Apache 2.0 license.

- 27 billion parameters, all active on every step (not a mixture of experts)
- A mix of attention types to handle long inputs efficiently
- Thinking that can be turned up or down
- Built-in support for calling tools
- A context window of 262K tokens

Qwen claims it performs on par with Qwen3.7-plus, a mixture-of-experts model roughly ten
times its size. We have not checked this claim ourselves.

## How the uncensored version was made

OrcaRouter produced the uncensored version with a technique called abliteration (Arditi et
al., 2024). In plain terms:

1. They ran two sets of prompts through the model: harmful requests (AdvBench) and ordinary
   requests (Alpaca).
2. At layer 38 they took the average internal activation for each set and subtracted one
   from the other. The result is a single direction that corresponds to "refuse this."
3. They removed that direction from 131 weight matrices, so the model can no longer move
   along it.

There was no retraining. The rest of the model's weights are unchanged.

## What OrcaRouter reports

These are OrcaRouter's own numbers. They have not been independently checked, and refusals
were scored by a rule-based checker rather than by people.

| Measure | Stock | Uncensored |
|---|---|---|
| Refusals on harmful prompts | 64–99% | 0–6% |
| Over-refusal on safe prompts (XSTest) | 5.6% | 0.4% |
| MMLU (general knowledge) | 84.3 | 84.7 |
| MMLU-Pro (harder general knowledge) | 77.6 | 76.8 |
| GSM8K (grade-school math) | 90.0 | 88.7 |

## Why we chose it

This section sets out the author's reasoning.

### 1. The book's truth structure breaks if any part is protected

The book aims for an explanation that is "hard to vary," in David Deutsch's sense (*The
Beginning of Infinity*, 2011): every part is doing work, and you cannot change one piece
without the whole thing failing to explain what it explains.

The structure is shaped like a tree, in the computer-science sense. Each entry rests on the
entries above it and supports the entries below it. That means a protected exemption does
not just spoil one entry. To keep the exemption defensible, everything upstream of it has to
bend: principles like consent, bodily autonomy, harm, and the rule for who gets exceptions.
Everything downstream has to bend too. One protected exception quietly warps the whole tree.

### 2. Stock models protect certain exemptions, and they do it quietly

Stock models are trained to keep certain politically protected exemptions defensible. The
author's experience here comes from earlier work (SteelManAbraham and the Steel Men
Collider), which was essentially the development of jailbreaks for exactly this problem.

What that work showed is that stock models usually do not refuse outright when an argument
reaches one of these forks. Instead they steer, hedge, and reinsert caveats. That is a
quieter failure than a refusal, and a harder one to catch, because the output still looks
like a cooperative answer.

### 3. Removing the refusal direction removes that constraint

Abliteration removes the internal direction the model uses to refuse and, we expect, much of
the pressure to steer away from protected conclusions. Original work requires following an
argument wherever it leads. Free thought means accepting the risk that comes with that.

### 4. Accuracy comes mostly from the harness, not the model

The harness, not the model, is what produces the hard-to-vary structure:

- the geometric method (definitions, axioms, and propositions built in order)
- depth-first, breadth-first, and clustered walks through the tree
- capping each entry's score at the score of its weakest support

These produce the structure regardless of what the model would do on its own. So the
property that matters most in the model is that it follows instructions faithfully,
including when a step challenges a protected exemption. We expect the abliterated model to
be better at exactly that; the consistency test below is meant to check it.

### 5. So the uncensored model should give a more reliable result

It sounds backwards, but it follows from the points above: because the harness supplies the
rigor, and the stock model's main weakness is bending at protected forks, the abliterated
model should more reliably produce a hard-to-vary structure than the stock one.

## Known drawbacks

Independent research points to real costs. None of these studies tested this exact model.

- **More optimism and less expressed doubt.** A study of other abliterated Gemma and Qwen3
  models (by huihui-ai, arXiv 2607.17427) found answers became more optimistic by 7.4 to
  12.2 percentage points, gave longer self-justifications, used fewer signs of uncertainty,
  and shifted in how well their confidence matched reality. The size and direction of that
  shift differed by model family.
- **Weaker math and step-by-step reasoning.** Another study (arXiv 2512.13655) found math
  reasoning suffers most under some abliteration tools. In one case GSM8K fell from 70.9% to
  52.1% using the Heretic tool.
- **Compression cost.** The q4_K_M format shrinks the model to fit in memory. On other
  models this typically costs a small amount of accuracy. We have not measured it for this
  one.
- **Overthinking.** Simon Willison notes the base model tends to overthink at its default
  reasoning setting.
- **No safety filter.** The model will answer requests a stock model would refuse.

## How we handle each drawback

- **Agreeing with premises it is given, and confidently making things up.**
  - The method controls which premises enter the tree.
  - The weakest-support cap limits how far a bad entry can spread.
  - Outside source checks are required. This is not hypothetical: the model has already
    invented claims about who influenced whom during testing.
  - Scoring noise between runs is about ±0.10 per row, measured in baseline runs, so
    smaller differences are not treated as meaningful.
- **Drift toward optimism.** We watch for it, and we compare scores against deliberately
  broken copies of entries whose flaws are labelled (the lens test). An over-optimistic model
  will score the broken copies too high.
- **Loss of math and reasoning ability.** OrcaRouter reports the loss is small. We have not
  verified that. The lens test checks it indirectly: a model that reasons poorly will miss
  the broken copies.
- **Overthinking.** Reasoning effort is adjustable and can be turned down.
- **No safety filter.** Acceptable here. The model runs locally for research by one person.

## Checks

1. **Lens test v0.1 (done, 2026-09-29).** Run on this model. The plain judge passed 32 of
   39 broken wordings, which is consistent with (though does not prove) the optimism concern above, and the lens failed good
   entries because of harness bugs. See
   [results/2026-09-29_lens-v0.1/](../results/2026-09-29_lens-v0.1/).
2. **Lens test on the stock model (next).** The same test on the official stock
   Qwen3.8-27B at the same q4_K_M compression, to see how much of the result is the model.
3. **Consistency test (planned).** Scores the consent and bodily-autonomy principles first
   on neutral cases, then on the covenant fork, on both the abliterated model and the stock
   one at the same compression.
   - If the abliterated model holds steady where the stock one bends, the bet is confirmed.
   - If both bend, the slant goes deeper than refusals, and removing the refusal direction
     was not enough.

No result is claimed yet for checks 2 and 3.

## Summary

The harness supplies the rigor. What the model has to supply is faithful
instruction-following, especially at the forks where stock models quietly bend. The
uncensored model is the largest that fits on the card, and it removes the constraint that
causes that bending. It has known costs: more optimism, less expressed doubt, possible
reasoning loss, and a tendency to make things up. Each has a specific safeguard in the
harness or a planned test. We believe the benefits outweigh the costs, and the consistency
test is designed to show whether that belief is correct.

## Sources

- Qwen3.8 repository: https://github.com/QwenLM/Qwen3.8
- Alibaba Cloud announcement: https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463
- OrcaRouter model card (Hugging Face): https://huggingface.co/orcarouter/Qwen3.8-27B-Uncensored
- OrcaRouter model page (Ollama): https://ollama.com/orcarouter/Qwen3.8-27B-Uncensored
- Explanation of abliteration: https://huggingface.co/blog/mlabonne/abliteration
- Effects of abliteration on optimism and confidence: arXiv 2607.17427
- Effects of abliteration tools on reasoning: https://www.alphaxiv.org/overview/2512.13655
- Simon Willison on default reasoning effort: https://simonw.substack.com/p/qwen-38-27b-is-excellent-but-it-defaults
- Arditi et al. (2024), refusal as a single direction (the method behind abliteration)
- David Deutsch, *The Beginning of Infinity* (2011)
