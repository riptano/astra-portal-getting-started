# Overview
Stream real-time, human-readable blockchain data to your app with Astra Block.

**In this guide, we'll**
- Introduction to Astra Block
- Example Queries
- Request Access to Astra Block

Let's get started!

# Prerequisites
None

## 1 Introduction to Astra Block
With Astra Block, you can stream real-time blockchain data directly to your Astra database. Simply enable the feature within Astra, create a blockchain database and start receiving data.

## 2 Example Queries

Get an NFT by contract address and token id:
`SELECT * FROM nfts WHERE contract_address='0x7A8cE4BeFfE38f431A2f12e1a8B7d7dAE62DF359' AND token_id='100';`

Get contracts by address and block number:
`SELECT * FROM contracts WHERE address='0xfdeed771e8b00eb1e72243acbd309ed83ad45f6e' AND block_number=9578734;`

Get logs for a transaction:
`SELECT * FROM logs WHERE transaction_hash = '0xd81829eef1642054fad5077a3ca234654771187af5c6dc3b8bd6a9d2ddc7078a' and block_number = 15832763 and log_index = 44;`

## 3 Request Access to Astra Block
You're now ready to give Astra Block a try! Request access by clicking the button below:

<<launchRequestAstraBlock>>
