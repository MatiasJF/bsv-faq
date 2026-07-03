# Contributing — the neutrality charter

Every answer in this repository follows these rules. They are what make the content reusable in any flavour, quotable by anyone, and durable when things get heated.

## The charter

1. **Facts carry sources.** Any claim about an event, a regulation, or another party links a source — primary wherever possible (the party's own announcement, the regulation text, the chain itself). No source, no claim.
2. **No blame, no defense.** Describe what happened and who decided what. Let responsibility follow from facts, not adjectives. This includes not defending BSVA — state what it does and doesn't do, and stop.
3. **No price talk.** No price levels, predictions, "opportunities", or investment framing of any kind. Also: it's the "BSV Blockchain", never "BSV coin" or "BSV cryptocurrency".
4. **Plain language.** Target a smart reader with zero crypto background. Every term of art gets a one-line explanation on first use, or a link to the question that explains it. If a sentence needs re-reading, rewrite it.
5. **Say what is unknown.** When facts are unresolved (an appeal pending, an unconfirmed report), the answer says so explicitly in a "What we don't know yet" note rather than guessing.
6. **Each party in its own words first.** Incident explainers quote or closely paraphrase the involved parties' own statements before any context is added.
7. **Date everything.** Every file carries an `updated:` date; time-sensitive answers state their as-of date in the text. Stale is worse than absent — an answer that can't be maintained shouldn't be added.

## Mechanics

- One question per file, format per `schema/question.md`. File name = the `id`.
- Short answer must stand alone (chatbots may surface only that).
- Run `bash scripts/lint.sh` before committing — it enforces the structural rules (frontmatter completeness; sources required for `30-regulation` and `70-incidents`).
- New categories: only when ≥3 questions genuinely don't fit existing ones.

## Review gates

Content is Internal until reviewed. Anything moving to Public goes through the owner sign-off and the publish checklist (accuracy, voice, classification flip) — no exceptions, including "small fixes" to already-public answers.
