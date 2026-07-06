---
id: is-blockchain-anonymous
question: "Are blockchain payments anonymous?"
category: 60-misconceptions
tags: [misconceptions, privacy, transactions]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
---

**Short answer.** No — in fact, closer to the opposite. Every BSV payment is public and permanent. The amounts, the addresses, and the timing can be seen by anyone, forever ([[how-do-transactions-work]]). What the public record leaves out is your *name* next to your address — until something connects the two. The accurate word is "pseudonymous": a bit like writing under a pen name. And that pen name gives thinner cover than most people expect.

## More detail

How does a name get connected to an address in practice? Licensed exchanges check your identity ([[why-do-licenses-matter]]). So when coins move between your verified account and your own addresses, anyone with lawful access to the exchange's records can connect the dots. Shops connect addresses to deliveries and invoices. And there is a whole mature industry that traces the public trail of payments on behalf of investigators. Every address you reuse builds up a visible history. One identification later, that becomes *your* visible history.

The practical rule for privacy is simple: treat anything you do on the blockchain as done in public. There are lawful ways to keep some privacy. You can use a fresh address for each payment. You can keep sensitive information off the blockchain, storing only a digital fingerprint of it there ([[data-on-chain]]). But the public record is not a hiding place, and investigators do make use of how traceable it is.

BSV's stated position is to keep this openness rather than hide it. Being easy to audit, and fitting with regulation, are treated as goals of the system ([[what-is-bsv]]). Other blockchain projects make different choices about privacy. Describing that range is beyond what this FAQ covers.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
