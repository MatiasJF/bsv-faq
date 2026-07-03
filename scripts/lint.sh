#!/usr/bin/env bash
# lint.sh — structural check for every faq/**/*.md against schema/question.md
set -uo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."
FAILS=0
fail() { echo "FAIL  $1"; FAILS=$((FAILS+1)); }

# collect all ids for cross-reference checking
ALL_IDS=$(find faq -name "*.md" -exec basename {} .md \;)

while IFS= read -r f; do
  base=$(basename "$f" .md)
  dir=$(basename "$(dirname "$f")")
  fm=$(awk '/^---$/{c++;next} c==1{print} c==2{exit}' "$f")

  for field in id question category tags level updated; do
    echo "$fm" | grep -q "^$field:" || fail "$f: missing frontmatter '$field'"
  done

  id=$(echo "$fm" | awk '/^id:/{print $2; exit}')
  cat=$(echo "$fm" | awk '/^category:/{print $2; exit}')
  [ "$id" = "$base" ] || fail "$f: id '$id' != filename '$base'"
  [ "$cat" = "$dir" ] || fail "$f: category '$cat' != folder '$dir'"

  body_first=$(awk '/^---$/{c++;next} c==2 && NF{print; exit}' "$f")
  echo "$body_first" | grep -q '^\*\*Short answer\.\*\*' || fail "$f: body must start with '**Short answer.**'"

  if [ "$dir" = "30-regulation" ] || [ "$dir" = "70-incidents" ]; then
    echo "$fm" | grep -A2 '^sources:' | grep -q 'http' || fail "$f: $dir requires at least one source"
  fi

  # cross-references resolve
  for ref in $(grep -oE '\[\[[a-z0-9-]+\]\]' "$f" | tr -d '[]' | sort -u); do
    echo "$ALL_IDS" | grep -qx "$ref" || fail "$f: cross-reference [[$ref]] does not resolve"
  done
done < <(find faq -name "*.md")

COUNT=$(find faq -name "*.md" | wc -l | tr -d ' ')
echo
[ "$FAILS" -eq 0 ] && echo "PASS — $COUNT question file(s) clean" || { echo "FAILED: $FAILS problem(s) across $COUNT file(s)"; exit 1; }
