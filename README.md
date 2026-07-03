# BSV Plain Answers

A neutral, plain-language FAQ about the BSV Blockchain. Written for people with no crypto background, and for anyone who needs a straight answer without hype, blame, or jargon.

## Why this exists

When something happens in the BSV ecosystem — an exchange closes, a regulation lands, a rumor spreads — there is no canonical place that answers "what actually happened, in plain words, and who is responsible for what." Confusion fills the gap. This repository fills it instead.

## What this is (and isn't)

- **It is**: factual answers, in simple language, with sources, kept current.
- **It is not**: marketing, price commentary, advocacy, or a rebuttal machine. Answers describe; they don't sell or blame.

## How it's organized

One question per file, grouped by category under `faq/`:

| Category | Contents |
|---|---|
| `00-basics` | What BSV is, how it differs, keys and wallets in plain words |
| `10-using-bsv` | Getting, storing, sending; what fees are |
| `20-exchanges-access` | Listings, on/off-ramps, what happens when an exchange closes |
| `30-regulation` | MiCA and friends in plain words; who regulates what |
| `40-ecosystem` | Who's who: BSV Association, EB Labs, independent companies — and what each does *not* do |
| `50-technology` | Scaling, SPV, data on chain — beginner level |
| `60-misconceptions` | Common myths, neutrally corrected |
| `70-incidents` | Explainers for specific events, each from primary sources |

Every file follows the format contract in `schema/question.md`: YAML frontmatter (id, question, category, tags, level, updated, sources) + a short answer + a longer answer + sources.

## Flavours

This repo is the **single source of truth**; skins consume it:

- **Chatbot**: one file per question = one retrieval chunk. See `flavours/chatbot.md`.
  A working retrieval-only demo lives in `flavours/chatbot-demo/` (`python3 build.py && open index.html`).
- **Branded versions** (EB Labs, partner sites, marketing): may restyle, may select subsets, may never alter facts or neutrality. Rules in `flavours/branding.md`.

## Editing rules

See `CONTRIBUTING.md` — the neutrality charter is short and non-negotiable. Run `bash scripts/lint.sh` before committing.

## Status & license

Content is maintained as a draft for internal review; the proposed license for public release is **CC BY 4.0** (attribution, remix-friendly — fits the flavour model). License choice requires owner sign-off before publication.
