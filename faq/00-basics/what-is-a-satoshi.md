---
id: what-is-a-satoshi
question: "What is a satoshi?"
category: 00-basics
tags: [basics, units]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A satoshi is the smallest unit of BSV: one hundred-millionth of a coin (1 BSV = 100,000,000 satoshis). Applications and fees are usually denominated in satoshis, the way prices can be quoted in cents instead of euros.

## More detail

The unit is named after Satoshi Nakamoto, the pseudonymous author of the original Bitcoin design that BSV descends from ([[how-did-bsv-start]]).

Satoshis matter on BSV more than on most blockchains because fees are tiny ([[what-are-fees]]) — a typical transaction costs a handful of satoshis, far below one cent. Micro-amounts are the natural unit for the things BSV is often used for: paying per API call, per game action, or per kilobyte of data written to the chain ([[data-on-chain]]).

In code and technical documents you'll almost always see integer satoshis rather than decimal BSV — it avoids rounding errors, the same reason financial software counts cents.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
