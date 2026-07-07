# BSV Plain Answers

A neutral, plain-language FAQ about the BSV Blockchain. Written for people with no crypto background, and for anyone who needs a straight answer without hype, blame, or jargon.

## Why this exists

When something happens in the BSV ecosystem — an exchange closes, a regulation lands, a rumor spreads — there is no canonical place that answers "what actually happened, in plain words, and who is responsible for what." Confusion fills the gap. This repository fills it instead.

## What this is (and isn't)

- **It is**: factual answers, in simple language, with sources, kept current.
- **It is not**: marketing, price commentary, advocacy, or a rebuttal machine. Answers describe; they don't sell or blame.

## How it's organized

**The live FAQ is deliberately small: a curated core of 11 questions** — only what a brand-new consumer would ask, the way a bank writes its customer FAQ. The core gets rock solid first; expansion is a deliberate decision, made later, one question at a time.

One question per file, grouped by category under `faq/`:

| Category | Contents |
|---|---|
| `00-basics` | What BSV is, how it differs from Bitcoin, what a wallet is |
| `10-using-bsv` | Getting, sending, fees, keeping it safe, lost access, exchange vs. own wallet |
| `20-exchanges-access` | What to do when an exchange holding your coins closes |
| `40-ecosystem` | Who is behind BSV: the BSV Association |

Drafted answers beyond the core (regulation, technology, misconceptions, ecosystem detail, incident explainers) live in `archive/` — out of the live FAQ and every flavour until deliberately promoted. See `archive/README.md`.

Every file follows the format contract in `schema/question.md`: YAML frontmatter (id, question, category, tags, level, updated, sources) + a short answer + a longer answer + sources.

## Flavours

This repo is the **single source of truth**; skins consume it:

- **Chatbot**: one file per question = one retrieval chunk. See `flavours/chatbot.md`.
  A working retrieval-only demo lives in `flavours/chatbot-demo/` (`python3 build.py && open index.html`).
- **Branded versions** (partner sites, marketing): may restyle, may select subsets, may never alter facts or neutrality. Rules in `flavours/branding.md`.

## Editing rules

See `CONTRIBUTING.md` — the neutrality charter is short and non-negotiable. Run `bash scripts/lint.sh` before committing.

## Status & license

Content is maintained as a draft for internal review; the proposed license for public release is **CC BY 4.0** (attribution, remix-friendly — fits the flavour model). License choice requires owner sign-off before publication.
