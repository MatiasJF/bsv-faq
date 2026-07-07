# Hand-off — what needs a human decision before publication

Status: **curated core of 11 questions live** (lint clean, consumer-bank voice); 29 further drafted answers parked in `archive/` awaiting deliberate promotion. **Internal** classification. The following gates stand between this repo and any public flavour:

## 1. Owner sign-off on content (blocking)

A human owner reads the live core — 11 files, a short read — and approves. Highest-risk among them:
- `faq/00-basics/bitcoin-vs-bsv.md` — the BTC/BSV neutrality stance
- `faq/40-ecosystem/what-is-the-bsv-association.md` — speaks for what BSVA does/doesn't do; the Association should confirm its own description
- `faq/20-exchanges-access/exchange-closes-my-funds.md` — practical guidance to affected customers

Archived answers get their own sign-off if and when they are promoted (see `archive/README.md`).

## 2. License decision (blocking)

CC BY 4.0 is **proposed**, not decided. It permits commercial reuse and modification with attribution — that's what enables the flavour model (agency materials, partner sites, chatbot). If Legal prefers no-derivatives or non-commercial, the flavour rules in `flavours/branding.md` need rewriting to match. Route through Legal.

**Note:** the GitHub repo was initialized with an MIT LICENSE file (a software license — wrong instrument for a content corpus). Treat it as a placeholder: replace it with whatever Legal decides before the repo goes public.

## 3. Publication mechanics (after 1 & 2)

- Run the publish gate (accuracy, voice, classification flip Internal→Public) on the whole corpus, not per-file.
- Create the public GitHub repo; push; tag v1.0.
- Only then: point flavours at it (chatbot ingestion per `flavours/chatbot.md`; agency/Bopper handover per `flavours/branding.md`).

## 4. Maintenance commitment (decide who)

The charter promises dated, current answers — someone must own updates. Immediate known follow-up: the Orange Gateway appeal outcome. Its explainer now sits in `archive/faq/70-incidents/orange-gateway-mica.md` and must be refreshed before any promotion (their 60-day withdrawal window ends ~29 August 2026).

## Non-blocking suggestions

- Native-language reviews before translating any flavour.
- Consider `bsv_search` (BSV Academy MCP) spot-checks on technology answers as an extra accuracy layer beyond the QA review.
