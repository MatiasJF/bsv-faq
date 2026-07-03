---
id: keeping-bsv-safe
question: "How do I keep my BSV safe?"
category: 10-using-bsv
tags: [using, security, scams]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** Three habits cover most of the risk: guard your recovery phrase offline (never type it into websites, apps, or "support" chats — that request is always a scam), verify addresses and networks before sending (payments are irreversible), and treat unsolicited investment or "recovery" offers as hostile by default.

## More detail

Almost all losses come from people, not from broken cryptography. The recurring patterns:

- **Phrase phishing.** Fake wallet updates, fake support agents, fake "validation" sites — anything that asks for your recovery phrase or private keys ([[what-are-private-keys]]). No legitimate party ever needs them. Rule with zero exceptions: the phrase goes into a wallet app you installed yourself, and nowhere else, ever.
- **Send-to-wrong-place.** Clipboard-swapping malware, look-alike addresses, wrong network ([[sending-bsv-basics]]). Verify a few characters at both ends; send a test amount when it matters.
- **Too-good offers.** "Guaranteed returns", giveaway doublers, urgent insider tips. Blockchain payments are irreversible, which makes them the scammer's favorite rail — skepticism is your refund policy.
- **Recovery scams.** After any loss, "recovery services" appear. Recovering keyless coins is impossible ([[lost-keys-recovery]]); paying them adds a second loss.

Structural choices that reduce risk: keep meaningful holdings in self-custody rather than on exchanges ([[custodial-vs-own-wallet]], [[exchange-closes-my-funds]]), keep the recovery phrase on paper in two places, and use a dedicated device or profile for significant amounts.

If you're ever unsure whether something is legitimate, the safe default is: it isn't. Verify through the official channel you already know, never through the channel that contacted you.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
