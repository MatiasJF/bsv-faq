---
id: how-do-transactions-work
question: "What happens when I send a transaction?"
category: 50-technology
tags: [technology, transactions]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
  - https://protocol.bsvblockchain.org/
---

**Short answer.** Your wallet builds a small signed message — "move these coins to that address" — proves it with your key, and broadcasts it to the network. Independent processors check the signature and the coins' availability, accept it within seconds, and soon include it in a block, making it a permanent part of the public record. No bank, no business hours, no borders.

## More detail

Step by step, minus the math:

1. **Compose**: the wallet selects coins you control (blockchain coins exist as discrete spendable pieces, like digital banknotes of arbitrary denomination) and drafts outputs — the recipient's amount and any change back to you.
2. **Sign**: your private key ([[what-are-private-keys]]) produces a signature that proves authorization without revealing the key itself.
3. **Broadcast**: the wallet sends the transaction to network processors ([[who-runs-the-bsv-network]]), who verify it — valid signature, coins unspent, rules followed — and start treating those coins as spent. On BSV this takes seconds, which is why a payee typically accepts payment at this point.
4. **Confirm**: a processor includes the transaction in a block ([[what-is-mining]]); each subsequent block buries it deeper, making reversal computationally impractical. This is what "confirmations" count.

Two properties fall out of the design. **Irreversibility**: no operator can undo a confirmed transaction — protection for recipients, unforgiving of sender error ([[sending-bsv-basics]]). **Publicity**: the transaction is visible to anyone on the shared ledger ([[is-blockchain-anonymous]]) — you can watch your own payment confirm in real time on a chain explorer.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
- [BSV protocol documentation](https://protocol.bsvblockchain.org/)
