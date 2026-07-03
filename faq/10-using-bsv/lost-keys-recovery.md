---
id: lost-keys-recovery
question: "I lost access to my wallet. Can my coins be recovered?"
category: 10-using-bsv
tags: [using, wallets, security, recovery]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** It depends entirely on what you lost. Lost the *device* but have your recovery phrase → yes, fully recoverable in any compatible wallet. Lost the *recovery phrase and keys* themselves → no; nobody can recover self-custodied coins, not the wallet vendor, not an exchange, not the BSV Association. Lost access to an *exchange account* → contact the exchange; that's an account-recovery process like any online service.

## More detail

The three scenarios, untangled:

1. **Broken/lost phone, recovery phrase safe.** Your coins were never on the phone — they're on the blockchain, and the phrase regenerates your keys ([[what-are-private-keys]]). Install a wallet on a new device, restore from the phrase, done.
2. **Recovery phrase and keys gone.** The coins remain visible on the public ledger forever, but nothing can move them without the keys. There is no back door — the absence of an override is precisely what makes self-custody trustworthy the rest of the time ([[custodial-vs-own-wallet]]). Anyone claiming they can "recover" such coins for a fee is running a scam, and this recovery-scam industry specifically targets people in your situation ([[keeping-bsv-safe]]).
3. **Exchange account lockout.** Custodial balances are the company's ledger entry, so their support can restore *account* access through identity verification — a customer-service matter, not a blockchain one.

Prevention beats all of this: write the recovery phrase on paper (or metal), store it in two safe places, never photograph it or type it into anything online.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
