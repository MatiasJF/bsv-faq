---
id: what-are-private-keys
question: "What are private keys, and why do they matter so much?"
category: 00-basics
tags: [basics, wallets, security]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A private key is the secret that controls coins on a blockchain — whoever knows the key can spend the coins, full stop. There is no "forgot password" flow and no administrator who can reset it. That makes keys both the source of your independence and your single point of failure.

## More detail

Every blockchain address has a matching private key, generated as a pair. The address is shareable — people send coins *to* it. The private key signs transactions *from* it. The network checks the signature math, not your identity: a valid signature is all the authorization that exists.

Two consequences follow, and most beginner disasters trace back to forgetting one of them:

1. **Lose the key, lose the coins.** No company, including any exchange, wallet vendor, or the BSV Association, can recover coins for a lost key ([[lost-keys-recovery]]).
2. **Leak the key, lose the coins.** Anyone who sees it can spend immediately and irreversibly. This is why no legitimate service ever asks for your private key or recovery phrase — such a request is the defining mark of a scam ([[keeping-bsv-safe]]).

Most wallets wrap your keys in a **recovery phrase** (12 or 24 ordinary words). The phrase *is* the keys in human-friendly form — guard it accordingly: written down, offline, never typed into websites or "support" chats.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
