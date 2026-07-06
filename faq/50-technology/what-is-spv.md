---
id: what-is-spv
question: "What is SPV, and why does it matter?"
category: 50-technology
tags: [technology, spv, verification]
level: intermediate
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
  - https://protocol.bsvblockchain.org/
---

**Short answer.** SPV ("Simplified Payment Verification") is the method that lets a wallet check a payment is real without downloading the blockchain's entire history. Think of it as checking your receipt without asking the whole bank to reopen its books. The wallet checks a small proof that the payment sits in the official record. That is what makes an ordinary phone wallet trustworthy on a chain whose full history is far too big for a phone — essential on a large chain like BSV.

## More detail

The problem SPV solves: a chain built for worldwide volume ([[what-is-scaling]]) grows enormous. If everyone had to store all of it, only data centers could take part. SPV, described in the original Bitcoin white paper, splits the jobs. The big processing companies keep the full record ([[who-runs-the-bsv-network]]). Everyone else checks only the payments that concern them.

How it works, roughly: each bundle of payments comes with a compact summary of everything inside it. A wallet keeps only a tiny running list of those summaries — a few kilobytes per day. Given a payment plus a short proof, the wallet can confirm the payment is genuinely part of the official record ([[what-is-a-blockchain]]). Faking such a proof would mean redoing the costly processing work that secures the whole chain ([[what-is-mining]]) — the same cost that protects everything else.

The practical payoff: payments checkable person to person in milliseconds, wallets that run on any device, and businesses that can accept these payments without running heavy equipment of their own. In BSV's design, SPV is not a compromise — it is how the original design meant everyday users to take part ([[how-do-transactions-work]]).

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
- [BSV protocol documentation](https://protocol.bsvblockchain.org/)
