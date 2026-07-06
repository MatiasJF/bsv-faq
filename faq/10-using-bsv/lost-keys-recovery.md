---
id: lost-keys-recovery
question: "I lost access to my wallet. Can my coins be recovered?"
category: 10-using-bsv
tags: [using, wallets, security, recovery]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
---

**Short answer.** It depends on what you lost. Lost the *device* but still have your recovery phrase? Yes — you can get everything back in any compatible wallet. Lost the *recovery phrase and keys* themselves? No. Nobody can recover coins you held yourself — not the wallet maker, not an exchange, not the BSV Association. Lost access to an *exchange account*? Contact the exchange. That works like getting back into any other online account.

## More detail

There are three different situations here. Let's untangle them:

1. **Broken or lost phone, recovery phrase safe.** Your coins were never on the phone. They are on the blockchain, and your phrase recreates your keys ([[what-are-private-keys]]). Install a wallet on a new device, restore from the phrase, and you're done.
2. **Recovery phrase and keys gone.** The coins stay visible in the public record forever, but nothing can move them without the keys. There is no back door. That missing override is exactly what makes holding your own coins trustworthy the rest of the time ([[custodial-vs-own-wallet]]). Anyone who claims they can "recover" such coins for a fee is running a scam — and this recovery-scam industry targets people in exactly your situation ([[keeping-bsv-safe]]).
3. **Locked out of an exchange account.** Your balance there is an entry in the company's own records. Their support team can restore access to the *account* after checking your identity. That is a customer-service matter, not a blockchain one.

Prevention beats all of this. Write the recovery phrase on paper (or metal), keep it in two safe places, and never photograph it or type it into anything online.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
