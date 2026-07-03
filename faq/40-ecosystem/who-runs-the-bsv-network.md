---
id: who-runs-the-bsv-network
question: "Who actually runs the BSV network?"
category: 40-ecosystem
tags: [ecosystem, mining, nodes]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** Independent transaction processors — often called miners or node operators — run the network. They are separate businesses, in various countries, that operate the machines validating transactions and building blocks, earning fees and newly issued coins for it. No permission is needed to join, and no single party (including the BSV Association) runs the network itself.

## More detail

The processors' role: collect broadcast transactions, check them against the protocol rules, assemble them into blocks ([[what-is-mining]]), and publish those blocks to the shared chain ([[what-is-a-blockchain]]). Competition among them — anyone can enter, the work is paid ([[what-are-fees]]) — is what keeps the record honest: cheating one's own ledger copy is pointless when everyone else's copies disagree.

The ecosystem around them divides cleanly ([[ecosystem-who-is-who]]): processors run the network; the BSV Association maintains the software and standards most processors choose to run ([[what-is-the-bsv-association]], [[how-is-bsv-developed]]); businesses like exchanges and wallet apps build services on top ([[what-is-an-exchange]]). Each layer makes its own decisions — which is why "who decided X?" always has a specific answer, and it's rarely "the network" ([[what-bsva-does-not-do]]).

Anyone can verify the network's operation directly — blocks, transactions, and activity are public and inspectable in real time on chain explorers such as WhatsOnChain ([[is-bsv-dead]]).

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
