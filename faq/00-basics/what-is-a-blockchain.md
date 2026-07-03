---
id: what-is-a-blockchain
question: "What is a blockchain, in plain words?"
category: 00-basics
tags: [basics, technology]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A blockchain is a shared record book kept by many independent computers at the same time. Everyone sees the same entries, new entries are added in batches ("blocks"), and once added, entries are practically impossible to alter without everyone noticing. That's the whole trick: a public record no single party controls.

## More detail

Think of a ledger — a book of "who paid whom, when." Normally one institution keeps it, and you trust that institution. A blockchain distributes that job: thousands of computers each hold a full copy, and they follow shared rules to agree on every new entry.

New transactions are collected into a block, and each block is cryptographically linked to the previous one — hence "chain." Changing an old entry would break the links and be immediately obvious to every other participant, which is what makes the record tamper-evident.

Adding blocks is the job of specialized operators ([[what-is-mining]]) who are paid in fees and newly issued coins for doing the work honestly. The result is a record that is public, append-only, and not dependent on trusting any single company — the property everything else ([[what-is-bsv]], [[data-on-chain]]) builds on.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
