---
id: what-is-a-wallet
question: "What is a wallet?"
category: 00-basics
tags: [basics, wallets]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A wallet is an app that holds the keys to your coins and lets you send and receive them. The coins themselves live on the blockchain; the wallet holds the private keys ([[what-are-private-keys]]) that prove they're yours and authorize spending them.

## More detail

The name misleads slightly: a wallet doesn't contain coins the way a leather wallet contains cash. Your coins are entries on the public blockchain. What the wallet stores is your keys — the secret codes that let you, and only you, move those entries.

Wallets come in two fundamentally different kinds, and the difference matters more than any feature list ([[custodial-vs-own-wallet]]):

- **Self-custody wallets** — you hold the keys on your own device. Nobody can freeze or move your coins, and nobody can help you if you lose the keys ([[lost-keys-recovery]]).
- **Custodial services** — an exchange or app holds the keys for you, like a bank holds deposits. Convenient, but your access depends on that company staying solvent, licensed, and online ([[exchange-closes-my-funds]]).

Practical basics: keep your recovery phrase offline and private ([[keeping-bsv-safe]]), and treat any request to "verify" it as a scam — no legitimate service ever asks for it.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
