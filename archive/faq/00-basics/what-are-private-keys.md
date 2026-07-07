---
id: what-are-private-keys
question: "What are private keys, and why do they matter so much?"
category: 00-basics
tags: [basics, wallets, security]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
---

**Short answer.** A private key is the secret code that controls coins on a blockchain. Think of it as the only key to a safe: whoever knows it can spend the coins — full stop. There is no "forgot password" button, and no administrator who can reset it. That makes your key both the source of your independence and the one thing that can undo everything if it goes wrong.

## More detail

Every blockchain address comes with a matching private key; the two are created as a pair. The address is like a mailbox slot — safe to share, because people use it to send coins *to* you. The private key is what approves payments going *out*. The network only checks that the approval is genuine, not who you are: a valid approval from the key is all the permission that exists.

Two things follow from this, and most beginner disasters trace back to forgetting one of them:

1. **Lose the key, lose the coins.** No company — not an exchange, not a wallet maker, not the BSV Association — can recover coins when a key is lost ([[lost-keys-recovery]]).
2. **Leak the key, lose the coins.** Anyone who sees it can spend your coins at once, and there is no undo. That is why no honest service will ever ask for your private key or recovery phrase. Such a request is the tell-tale sign of a scam ([[keeping-bsv-safe]]).

Most wallets wrap your keys in a **recovery phrase** — a list of 12 or 24 ordinary words. That phrase *is* your keys, just in a form people can read. Guard it the same way: write it down, keep it offline, and never type it into a website or a "support" chat.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
