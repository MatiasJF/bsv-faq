---
id: how-do-transactions-work
question: "What happens when I send a transaction?"
category: 50-technology
tags: [technology, transactions]
level: beginner
updated: 2026-07-06
sources:
  - https://bsvblockchain.org/
  - https://protocol.bsvblockchain.org/
---

**Short answer.** Your wallet writes a short message — "move this money to that person" — and signs it with your secret key to prove it really came from you. It then sends the message out to the network. Independent companies check that the money is yours and hasn't been spent, accept the payment within seconds, and soon add it to the permanent public record. No bank sits in the middle.

## More detail

Step by step, in plain terms:

1. **Prepare**: your wallet picks the money you will spend. Digital coins exist as separate pieces, like banknotes that can be any value. The wallet also works out any change to send back to you.
2. **Sign**: your private key ([[what-are-private-keys]]) creates a signature. The signature proves you approved the payment — without ever revealing the key itself.
3. **Send**: the wallet passes the payment to the companies that run the network ([[who-runs-the-bsv-network]]). They check the signature, check the money hasn't already been spent, and from then on treat it as spent. On BSV this takes seconds, which is why most sellers accept the payment at this point.
4. **Record**: one of those companies writes the payment into the permanent record ([[what-is-mining]]). Each later addition buries it deeper, making it ever harder to undo. This is what "confirmations" count.

Two things follow from this design. **Payments are final**: nobody can undo a confirmed payment. That protects the person being paid, but it is unforgiving if you make a mistake ([[sending-bsv-basics]]). **Payments are public**: anyone can see them in the shared record ([[is-blockchain-anonymous]]) — you can even watch your own payment go through, live, on a public viewing website.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
- [BSV protocol documentation](https://protocol.bsvblockchain.org/)
