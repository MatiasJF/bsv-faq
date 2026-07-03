#!/usr/bin/env python3
"""Compile the FAQ corpus into a self-contained chatbot demo (index.html).

Reference implementation of flavours/chatbot.md: retrieval-only, so the bot
can only ever return corpus text verbatim — hallucination is impossible by
construction. No dependencies beyond the standard library.

Usage:
    python3 build.py            # internal build — includes publication-gated answers, badged
    python3 build.py --public   # excludes any file carrying a REVIEW GATE comment
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
FAQ = os.path.join(REPO, "faq")
TEMPLATE = os.path.join(HERE, "template.html")
OUT = os.path.join(HERE, "index.html")

PUBLIC = "--public" in sys.argv


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError("no frontmatter")
    meta, body = {}, m.group(2)
    lines = m.group(1).split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        km = re.match(r"^(\w[\w-]*):\s*(.*)$", line)
        if km:
            key, val = km.group(1), km.group(2).strip()
            if val == "":  # block list (sources)
                items = []
                while i + 1 < len(lines) and lines[i + 1].lstrip().startswith("- "):
                    i += 1
                    items.append(lines[i].lstrip()[2:].strip().strip('"'))
                meta[key] = items
            elif val.startswith("["):  # inline list (tags)
                meta[key] = [t.strip() for t in val.strip("[]").split(",") if t.strip()]
            else:
                meta[key] = val.strip('"')
        i += 1
    return meta, body


def parse_file(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    meta, body = parse_frontmatter(text)
    gated = "REVIEW GATE" in body
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S).strip()

    sm = re.search(r"\*\*Short answer\.\*\*\s*(.+?)(?:\n\n|\Z)", body, re.S)
    short = sm.group(1).strip() if sm else body.split("\n\n")[0]

    detail = ""
    dm = re.search(r"## More detail\n(.*?)(?=\n## |\Z)", body, re.S)
    if dm:
        detail = dm.group(1).strip()

    refs = sorted(set(re.findall(r"\[\[([\w-]+)\]\]", body)))
    return {
        "id": meta["id"],
        "question": meta["question"],
        "category": meta["category"],
        "tags": meta.get("tags", []),
        "updated": meta.get("updated", ""),
        "sources": meta.get("sources", []),
        "short": short,
        "detail": detail,
        "refs": refs,
        "gated": gated,
    }


def main():
    docs = []
    for root, _dirs, files in os.walk(FAQ):
        for name in sorted(files):
            if not name.endswith(".md"):
                continue
            doc = parse_file(os.path.join(root, name))
            if PUBLIC and doc["gated"]:
                print(f"  excluded (gated): {doc['id']}")
                continue
            docs.append(doc)
    docs.sort(key=lambda d: (d["category"], d["id"]))

    with open(TEMPLATE, encoding="utf-8") as f:
        html = f.read()
    payload = json.dumps(docs, ensure_ascii=False)
    html = html.replace("/*__DATA__*/[]", payload)
    html = html.replace("__BUILD_MODE__", "public" if PUBLIC else "internal")
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Built {OUT}: {len(docs)} answers ({'public' if PUBLIC else 'internal'} mode)")


if __name__ == "__main__":
    main()
