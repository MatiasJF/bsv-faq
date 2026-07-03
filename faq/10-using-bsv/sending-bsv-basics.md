---
id: sending-bsv-basics
question: "How do I send and receive BSV?"
category: 10-using-bsv
tags: [using, wallets, transactions]
level: beginner
updated: 2026-07-03
sources:
  - https://bsvblockchain.org/
---

**Short answer.** Receiving: open your wallet, share the address or QR code it shows. Sending: paste or scan the recipient's address, enter the amount, confirm. The transaction reaches the recipient in seconds and costs a fraction of a cent. The one rule that matters: verify the address and the network before confirming, because blockchain payments cannot be reversed.

## More detail

Addresses are long strings precisely so that typos are detectable — but wrong-but-valid addresses (from a mispaste, or malware that swaps clipboard contents) are not. Good habits: scan QR codes rather than typing, check the first and last few characters after pasting, and send a small test amount first when the sum is significant.

**Irreversibility** is a feature of the system, not a missing safety net: no company can claw a confirmed transaction back ([[how-do-transactions-work]]). That's what makes the network trustworthy for recipients — and unforgiving of sender mistakes.

**Network check**: BSV addresses look similar to those of related chains ([[bitcoin-vs-bsv]]). Sending BSV to an address on a different network typically loses the coins. Wallets and exchanges label the network — read the label.

Some BSV wallets also support human-readable payment handles (built on standards like Paymail) so you can pay a name instead of a string — same rules apply: verify before confirming.

## Sources

- [BSV Blockchain — official site](https://bsvblockchain.org/)
