# Hand-off — what needs a human decision before publication

Status: content complete (41 questions, lint clean), QA review run, **Internal** classification. The following gates stand between this repo and any public flavour:

## 1. Owner sign-off on content (blocking)

A human owner reads the corpus — at minimum the highest-risk files — and approves:
- `faq/70-incidents/orange-gateway-mica.md` — the incident framing (accuracy + tone; it names a company and a regulator)
- `faq/40-ecosystem/what-is-eb-labs.md` — **hard-blocked, strongest gate in the repo.** The QA review found NO citable public source for EB Labs' existence, structure, or mandate (no site, no announcement, and no "EB Labs AG" in the Swiss commercial register/Zefix as of 2026-07-03 — Exec/Legal must confirm the exact legal name and registration status). Publish this answer only after the EB Labs site (eb-labs-web project) is live and citable, and keep the two consistent
- `faq/00-basics/bitcoin-vs-bsv.md` and `how-did-bsv-start.md` — the BTC/BSV neutrality stance
- `faq/40-ecosystem/what-bsva-does-not-do.md` — speaks for what BSVA does/doesn't do; the Association should confirm its own description

## 2. License decision (blocking)

CC BY 4.0 is **proposed**, not decided. It permits commercial reuse and modification with attribution — that's what enables the flavour model (agency materials, partner sites, chatbot). If Legal prefers no-derivatives or non-commercial, the flavour rules in `flavours/branding.md` need rewriting to match. Route through Legal.

## 3. Publication mechanics (after 1 & 2)

- Run the publish gate (accuracy, voice, classification flip Internal→Public) on the whole corpus, not per-file.
- Create the public GitHub repo; push; tag v1.0.
- Only then: point flavours at it (chatbot ingestion per `flavours/chatbot.md`; agency/Bopper handover per `flavours/branding.md`).

## 4. Maintenance commitment (decide who)

The charter promises dated, current answers — someone must own updates. Immediate known follow-up: the Orange Gateway appeal outcome (file has a "What we don't know yet" section that will need resolving; their 60-day withdrawal window ends ~29 August 2026).

## Non-blocking suggestions

- Native-language reviews before translating any flavour.
- Consider `bsv_search` (BSV Academy MCP) spot-checks on technology answers as an extra accuracy layer beyond the QA review.
