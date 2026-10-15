# Method: what the confidence numbers mean

The book proceeds in the geometric manner: definitions and axioms first, then propositions derived from them. Each entry carries a confidence between 0 and 1. This note says what those numbers are, and what they are not.

## A ranking, not a probability

Confidences are an ordering with a cap chain. They tell a reader which claims are weaker than which, and where each weakness comes from. They are not calibrated probabilities. No entry is scored yet (every v2 entry is pending the collider), so take a hypothetical: if A3 were scored 0.55, that would not mean a 55% chance that A3 is true; it would mean A3 is weaker than anything scored higher, and that its weakest support sets its limit.

The numbers are judged by a model, and nothing yet checks them against outcomes. Until something does, they should be read as relative strength only.

## The rules

1. **Cap.** An entry can be no more confident than its weakest support. Its effective confidence is the minimum of its own score and the effective confidence of everything it cites, all the way down the chain. A multi-row entry such as A4 is capped by its weakest row.
2. **Ordering.** Evidence that raises a claim lowers its negation. The two move in opposite directions; they are not required to sum to 1.
3. **Undecided.** A claim and its negation are each capped by their own supports, so both can come out low. That is not a contradiction. It records that the stack does not yet settle the question, and the book says so openly. In a geometric work, "not yet derived" is a real state.
4. **Explanation adds nothing.** A principle that explains why claims line up (for example PR1, pattern by requirement) does not raise their confidence. Checking, stripping, and auditing may hold a score or lower it, never raise it.
5. **Stated sense.** Where a key word has a strong and a weak sense (mind, organism, cell, society), the entry states which one it claims, and it is scored in that sense only. A claim and its negation are compared within the same sense, not across senses. Each entry's header field `scored_as:` gives the claim in its stated sense, as it is scored.
6. **Declared reading.** A *declared reading* is different: an interpretation the book adopts that the evidence cannot tell apart from its rivals (for example, that I am this body, A2 (b), or that Nature is God, D-Nature). It is stated openly, it is not scored, and it adds no confidence to anything.

## What a reader should be able to verify

For any entry: the claim as checked, the evidence or cited entries that carried it, the one link that capped its confidence, and reasoning that actually reaches the verdict. If any of these is missing, the score should not be trusted.
