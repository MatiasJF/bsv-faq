# Flavour: chatbot ingestion

The repo is chunk-ready by construction — no transformation pipeline needed.

## Ingestion model

- **One file = one chunk.** Each `faq/**/*.md` file is a self-contained retrieval unit.
- **Frontmatter = metadata.** Map directly: `question` → title/embedding text, `category` + `tags` → filters, `updated` → freshness, `sources` → citation payload.
- **Embed** `question` + short answer (first paragraph) for retrieval; return the full body as the grounding context.
- **Short answer is the fallback response.** It's written to stand alone; a bot may quote it verbatim with the source list.

## Behavior rules for any bot built on this corpus

1. Answer ONLY from the corpus. If retrieval finds nothing relevant, say "I don't have a vetted answer for that" — never improvise on BSV topics; wrong-but-confident is the failure mode this corpus exists to fight.
2. Quote sources when the answer involves an event, regulation, or another party (categories 30/70 always).
3. Inherit the charter: no price talk, no blame, no speculation — even when the user pushes for it. Deflect price questions with the `no-price-talk` rationale, not silence.
4. Surface the `updated` date when an answer is time-sensitive ("as of July 2026...").
5. `[[cross-references]]` resolve to the referenced question — offer it as a follow-up.

## Sync

Re-ingest on every commit to `main` (the corpus is small; full re-index is cheap). The `id` field is the stable key across re-ingests.
