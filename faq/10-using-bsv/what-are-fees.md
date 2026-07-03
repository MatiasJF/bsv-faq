---
id: what-are-fees
question: "What are transaction fees, and what do they cost on BSV?"
category: 10-using-bsv
tags: [using, fees, transactions]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A fee is the small amount you pay the network's transaction processors to include your transaction in the blockchain. On BSV, fees are typically a few satoshis ([[what-is-a-satoshi]]) — well under a cent — and they stay low by design, because the network's capacity grows with demand instead of rationing limited space.

## More detail

Fees exist because processing transactions costs real resources — machines, bandwidth, electricity. The operators who batch transactions into blocks ([[what-is-mining]]) are compensated through these fees plus newly issued coins.

Why fees differ so much between chains comes down to capacity ([[what-is-scaling]]). On a network with a small fixed block size, users compete for limited space, so fees rise when the network is busy. BSV removed the protocol-level cap, so space stays abundant and fees stay flat and tiny regardless of load — the trade-off being that processing very large blocks requires industrial-scale infrastructure, a cost carried by the network's professional operators ([[who-runs-the-bsv-network]]).

The practical consequence isn't just cheaper payments; it's a different set of possible applications. When a transaction costs 1/100th of a cent, it becomes economical to pay per article read, per game move, or per data record written ([[data-on-chain]]) — patterns that are impossible when each transaction costs dollars.

Fees are set by market dynamics between users and processors, not by any authority — the BSV Association doesn't set or collect them ([[what-bsva-does-not-do]]).

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
