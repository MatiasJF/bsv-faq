# Question file format

Every file under `faq/` follows this exact shape. File name = `<id>.md`.

```markdown
---
id: what-is-bsv                 # kebab-case, unique across the whole repo
question: "What is BSV?"        # the question as a user would ask it
category: 00-basics             # must match the containing folder
tags: [basics, bitcoin]         # 1-5 lowercase tags
level: beginner                 # beginner | intermediate (default beginner)
updated: 2026-07-03             # ISO date of last substantive edit
sources:                        # required for 30-regulation and 70-incidents;
  - https://example.org/...     # strongly encouraged everywhere else
---

**Short answer.** Two or three sentences that fully stand alone. A chatbot may
show only this.

## More detail

Two to five short paragraphs in plain language. Terms of art get a one-line
explanation or a link to the question that explains them, written as
[[other-question-id]].

## What we don't know yet   <!-- optional; only when facts are unresolved -->

- Open point, stated plainly.

## Sources                   <!-- mirrors frontmatter, human-readable -->

- [Publisher — Title](https://example.org/...) (date)
```

Rules enforced by `scripts/lint.sh`:

- Frontmatter has all of: `id`, `question`, `category`, `tags`, `level`, `updated`.
- `id` matches the file name; `category` matches the folder.
- Body starts with `**Short answer.**`.
- Files in `30-regulation/` and `70-incidents/` have at least one source.
- `[[cross-references]]` point at ids that exist.
