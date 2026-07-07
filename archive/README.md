# Archive — drafted answers, not live

These answers were written and linted as part of the original 40-question corpus, then parked when the FAQ was cut down to a small curated core (July 2026). They are **not** part of the live FAQ: the lint script and every flavour (including the chatbot demo) read only `faq/`, never this folder.

Nothing here is deleted knowledge — it is a backlog. The live core gets rock solid first; expansion is a deliberate decision made later, question by question.

## Promoting a question back into the core

1. Move the file from `archive/faq/<category>/` back to `faq/<category>/` (recreate the category folder if needed).
2. Re-check its `[[cross-references]]` — they may point at questions still in the archive. Rewrite those into plain words or promote the target too.
3. Re-read it against the charter in `CONTRIBUTING.md` (grandmother test, sources, dates) and refresh `updated:`.
4. Run `bash scripts/lint.sh`, rebuild the chatbot demo (`python3 flavours/chatbot-demo/build.py`), commit.

## Maintenance note

Archived files are frozen at their `updated:` date and are **not** kept current. In particular, `faq/70-incidents/orange-gateway-mica.md` will be stale once the Orange Gateway appeal resolves (withdrawal window ends ~29 August 2026) — it must be updated before any promotion.
