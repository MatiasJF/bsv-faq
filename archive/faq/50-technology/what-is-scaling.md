---
id: what-is-scaling
question: "What does 'scaling' mean, and what is BSV's approach?"
category: 50-technology
tags: [technology, scaling, blocks]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
---

**Short answer.** "Scaling" means a payment system's ability to handle more and more payments as it grows. BSV's approach: payments are added to the record in bundles, and BSV puts no fixed limit on how big a bundle can be. Capacity grows with demand and with better computers, and fees stay tiny at any volume. Other chains cap the bundle size and send the extra traffic elsewhere. That disagreement is what created BSV in the first place.

## More detail

The trade-off is simple arithmetic. Bundles are added at a roughly steady rhythm, so the bundle size sets how many payments per second the system can handle. Keep bundles small and the system is light to run, but space runs short — when it's busy, users bid against each other and fees rise. Let bundles grow and there is room for everyone, so fees stay near zero ([[what-are-fees]]) — but handling big bundles takes serious equipment, so the network ends up run by professional data-center companies ([[who-runs-the-bsv-network]]).

That trade-off split the original Bitcoin community ([[how-did-bsv-start]]). BTC chose small bundles, with extra systems layered on top. BSV chose unlimited room on the chain itself, accepting professional infrastructure as the cost ([[bitcoin-vs-bsv]]). BSV's current engineering project, called Teranode, aims at capacity in the range of a million payments per second — enough for payment-network use and for record-keeping ([[data-on-chain]]).

Why this matters to an ordinary user: capacity decides what the chain is *for*. Chains where a payment costs dollars suit large, occasional transfers. Chains where a payment costs under a cent make tiny payments and everyday record-keeping affordable. Different tools — shaped by that one design choice.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
