# Chatbot demo — reference implementation

A working chatbot over the FAQ corpus, in one self-contained HTML file. It is the
reference implementation of the rules in [`../chatbot.md`](../chatbot.md).

**Design choice: retrieval-only, no language model.** The bot matches the question
against the corpus and returns the vetted answer *verbatim* — short answer first,
full detail on demand, sources attached. It cannot hallucinate because it cannot
generate. That makes this demo safe to show before any AI-governance questions are
settled, and it doubles as the ground truth for what a future LLM-backed bot must
say.

## Build & run

```bash
python3 build.py            # internal build — gated answers included, badged
python3 build.py --public   # excludes publication-gated answers (REVIEW GATE files)
open index.html             # no server, no network, no dependencies
```

`index.html` is generated — edit `template.html` and the corpus, never the output.
Rebuild on every corpus change (the flavour contract's "re-ingest on every commit").

## What the demo implements (from the flavour contract)

| Rule | Implementation |
|---|---|
| Answer only from corpus | No generation; below a score threshold it says "I don't have a vetted answer" |
| Cite sources | Source list rendered under every answer that has one |
| No price talk | Price/investment wording routes to the `no-price-talk` answer |
| Surface freshness | "As of `updated`" line under every answer |
| Cross-refs as follow-ups | `[[refs]]` render as clickable question chips, inline and under the answer |

Plus one rule from the publication gates: files carrying a `REVIEW GATE` comment
are excluded from `--public` builds and badged "internal — publication-gated" in
internal builds.

## Upgrade path to an LLM-backed bot

When a conversational bot is wanted (paraphrasing, multi-turn, typo tolerance),
keep this exact corpus as the grounding source and use
[`system-prompt.md`](system-prompt.md) as the system prompt. The retrieval demo
then becomes the regression baseline: for any question it answers, the LLM bot
must convey the same facts and cite the same sources.

## Status

Internal demo. Same tier as the corpus (Internal until the FAQ's human gates in
`HANDOFF.md` are cleared). A branded/skinned version is a flavour decision — see
[`../branding.md`](../branding.md).
