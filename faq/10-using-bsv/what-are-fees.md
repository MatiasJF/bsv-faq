---
id: what-are-fees
question: "What are transaction fees, and what do they cost on BSV?"
category: 10-using-bsv
tags: [using, fees, transactions]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A fee is a small amount you pay to the companies that process payments, so your payment gets written into the blockchain — a bit like postage on a letter. On BSV, a fee is typically a few satoshis ([[what-is-a-satoshi]]) — well under a cent. Fees stay low because the network's capacity grows with demand, instead of rationing limited space.

## More detail

Fees exist because processing payments costs real money — machines, internet capacity, electricity. The companies that gather payments into blocks ([[what-is-mining]]) are paid through these fees plus newly issued coins.

Why do fees differ so much between blockchains? It comes down to capacity ([[what-is-scaling]]). On a network where each block has a small fixed size, users compete for limited room, so fees rise when the network is busy. BSV removed that built-in size limit, so room stays plentiful and fees stay flat and tiny no matter how busy it gets. The trade-off: handling very large blocks takes industrial-scale equipment, a cost carried by the network's professional operators ([[who-runs-the-bsv-network]]).

The practical result is not just cheaper payments — it is a whole new set of things you can do. When a payment costs 1/100th of a cent, it becomes affordable to pay per article you read, per move in a game, or per record you save ([[data-on-chain]]). None of that is possible when each payment costs dollars.

No authority sets the fees. They are worked out in the open market between users and processors — the BSV Association does not set or collect them ([[what-bsva-does-not-do]]).

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
