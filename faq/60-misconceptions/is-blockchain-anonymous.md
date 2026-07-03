---
id: is-blockchain-anonymous
question: "Are blockchain payments anonymous?"
category: 60-misconceptions
tags: [misconceptions, privacy, transactions]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** No — closer to the opposite. Every BSV transaction is public and permanent: amounts, addresses, and timing are visible to anyone, forever ([[how-do-transactions-work]]). What the chain omits is your *name* next to the address — until something links them. The accurate word is "pseudonymous," and the pseudonym is thinner than most people assume.

## More detail

Where the linkage comes from in practice: licensed exchanges verify identity ([[why-do-licenses-matter]]), so coins moving between your verified account and your addresses connect the dots for anyone with lawful access to exchange records; merchants link addresses to deliveries and invoices; and chain analysis — following the public graph of transactions — is a mature industry serving investigators. Any address you reuse accumulates a visible history that's one identification away from being *your* visible history.

The practical framing for privacy: treat on-chain activity like activity in public. Lawful privacy practices exist — fresh addresses per payment, keeping sensitive data off-chain with only fingerprints anchored ([[data-on-chain]]) — but the ledger is not a hiding place, and investigators do use its traceability.

BSV's stated design position is to keep this transparency rather than obscure it, treating auditability and compatibility with regulation as goals of the system ([[what-is-bsv]]). Other blockchain projects make different design choices about privacy; describing that spectrum is beyond this FAQ's scope.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
