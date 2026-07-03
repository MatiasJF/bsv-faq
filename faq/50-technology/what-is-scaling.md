---
id: what-is-scaling
question: "What does 'scaling' mean, and what is BSV's approach?"
category: 50-technology
tags: [technology, scaling, blocks]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** Scaling is a blockchain's ability to handle growing transaction volume. BSV's approach is "big blocks": no protocol-fixed limit on block size, so capacity grows with demand and hardware, keeping fees tiny at any volume. Other chains cap block size and route volume elsewhere — the design disagreement that produced BSV in the first place.

## More detail

The constraint is simple arithmetic: blocks arrive at a roughly fixed rhythm, so block size sets transactions-per-second. Keep blocks small and the chain stays light to run but space becomes scarce — users bid up fees when it's busy. Let blocks grow and capacity is abundant — fees stay near zero ([[what-are-fees]]) — but processing big blocks demands serious infrastructure, pushing network operation toward professional data-center operators ([[who-runs-the-bsv-network]]).

That trade-off split the original Bitcoin community ([[how-did-bsv-start]]): BTC chose small blocks with additional layers on top; BSV chose unbounded on-chain scale, accepting professionalized infrastructure as the cost ([[bitcoin-vs-bsv]]). BSV's current engineering effort, the Teranode node implementation, targets throughput in the range of a million transactions per second — capacity intended for payment-network and data workloads ([[data-on-chain]]).

Why a beginner should care at all: capacity determines what the chain is *for*. Dollar-fee chains suit large, infrequent settlements. Sub-cent-fee chains make micropayments and per-event data recording economical — different tools shaped by that one design choice.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
