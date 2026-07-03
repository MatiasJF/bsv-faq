---
id: what-is-mining
question: "What is mining?"
category: 50-technology
tags: [technology, mining, proof-of-work]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** Mining is the competitive work of bundling transactions into blocks and attaching them to the chain. Processors race to solve a costly computational puzzle; the winner publishes the next block and collects the reward — transaction fees plus newly issued coins. The cost is the security: rewriting history would mean redoing that work against the whole network's ongoing effort.

## More detail

The puzzle ("proof of work") has no meaning in itself — its point is to be expensive to solve and instant to verify. That asymmetry turns electricity and hardware into a security budget: an attacker wanting to alter a past block would need to redo its work *and* outpace everyone else building forward ([[what-is-a-blockchain]]), which gets more hopeless with every added block. That's why more confirmations mean more settled ([[how-do-transactions-work]]).

Economically, mining is a business, not a hobby: industrial operators ([[who-runs-the-bsv-network]]) invest in hardware and power, and are paid in fees plus a per-block issuance of new coins that halves on a fixed schedule — meaning fee revenue must carry the system long-term. BSV's design bets on that explicitly: huge transaction volumes at tiny per-transaction fees ([[what-is-scaling]], [[what-are-fees]]) rather than few transactions at high fees.

"Mining" is a mildly misleading name — nothing is dug up. It's transaction processing with a built-in security deposit, and the coins are issuance on a schedule, not treasure found.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
