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

Two honest framings follow. For privacy: treat on-chain activity like activity in public — lawful privacy practices exist (fresh addresses per payment, keeping sensitive data off-chain, [[data-on-chain]]), but the ledger is not a hiding place. For the "crypto is for criminals" narrative: a permanent public record that strengthens over time is, if anything, hostile terrain for crime — which is why the traceability of public blockchains keeps featuring in successful prosecutions.

BSV's design leans into this transparency deliberately — auditability and regulatory workability are treated as features of an honest payment system ([[what-is-bsv]]), not flaws to engineer away.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
