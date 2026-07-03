---
id: how-is-bsv-developed
question: "Who develops the BSV software, and can they change the rules?"
category: 40-ecosystem
tags: [ecosystem, development, governance]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
  - https://protocol.bsvblockchain.org/
---

**Short answer.** The BSV Association maintains the main node software and documents the protocol, with the stated policy of keeping the base protocol stable ("set in stone") rather than evolving it. Publishing software isn't the same as commanding the network: the independent operators who run nodes choose whether to adopt any release ([[who-runs-the-bsv-network]]).

## More detail

Development happens in layers. The **base protocol** — the transaction rules everything depends on — is treated as fixed by design; BSV's philosophy is that a stable foundation is what businesses can build on for decades, the way the internet's core protocols stayed stable while everything above them flourished. The **node software** implementing that protocol is engineered and maintained by the Association's teams (including the high-throughput Teranode implementation), released openly ([[what-is-the-bsv-association]]). **Applications and standards** above that — wallets, payment protocols, data services — come from the whole ecosystem ([[ecosystem-who-is-who]]).

On "can they change the rules": a software maintainer proposes; the network disposes. Operators adopt releases that serve their interests, and a change the operators rejected simply wouldn't run ([[bsva-controls-bsv]]). This adoption dynamic — not any legal authority — is the actual governance of a public blockchain, and it's also how the chain's history got its forks ([[how-did-bsv-start]]).

For developers: the software and protocol documentation are public, and building applications requires no one's permission ([[data-on-chain]]).

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
- [BSV protocol documentation](https://protocol.bsvblockchain.org/)
