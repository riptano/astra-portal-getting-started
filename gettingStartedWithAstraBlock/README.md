# Overview
Stream real-time, human-readable blockchain data to your app with Astra Block. Simply request access to the feature within Astra (we'll enable it for your account within 24 hours) and you can create a blockchain database that auto updates as new blocks are mined.

**In this guide, we'll**
- Explore how to stream real-time blockchain data into your Astra database
- Practice this new feature with example queries
- Request access to try Astra Block

Let's get started!

## 1 Introduction to Astra Block
With Astra Block, you can stream real-time blockchain data directly to your Astra database. 

We currently support Ethereum, with Polygon and Bitcoin coming soon. Interested in support for other chains? [Let us know](mailto:blockchain@datastax.com).

We also support the following data models:
- Assets
- Blocks
- Block numbers by date
- Contracts
- Dashboard Analytics
- Event signatures
- Logs
- NFTs
- Tokens
- Token Transfers
- Traces
- Transactions

Interested in support for other data? [Let us know](mailto:blockchain@datastax.com).

## 2 Example Queries
After creating your database, navigate to the CQL console and try the queries below:

Search for the first block number that occured on a date:
```sql
SELECT * FROM block_numbers_by_date WHERE date='2023-01-27' ORDER BY block_number ASC LIMIT 1;
```

Search for the last block number that occured on a date:
```sql
SELECT * FROM block_numbers_by_date WHERE date='2023-01-27' LIMIT 1;
```

Search 5 ETH Block entries from Block Group 134:
```sql
SELECT * FROM eth_blocks WHERE blocks_group=134 LIMIT 5;
```

Search ETH Blocks by block number:
```sql
SELECT * FROM eth_blocks WHERE blocks_group=154 AND number=15399999 AND hash='0x25201aacfffd0ffd04e63e02ef82b2e15149f1c5b2430e338c32bb8520d107d9';
```

Search Contracts by Address and Block_Number:
```sql
SELECT * FROM contracts WHERE address='0xfdeed771e8b00eb1e72243acbd309ed83ad45f6e' AND block_number=9578734;
```

Search Transactions by Block Hash, Transaction Index, and Hash:
```sql
SELECT * FROM transactions WHERE block_hash='0x57d1ad19c25804ab3941baccaa588a4ea0e6cd44b965a6ec4204c60b9e7ce34f' AND transaction_index=4 AND hash='0x1ffc4aff0d7b32694bd3e430f2a6b02621c3f9662f70b0b88afe558358fa0ee4';
```

Search Transactions by date:
```sql
SELECT * FROM transactions_by_date WHERE date='2023-01-27';
```

Search Transactions by hash:
```sql
SELECT * FROM transactions_by_hash WHERE hash='0x0c25a6099b2e9ae1858946ba017e3f12d01c124157b3ec4635fd71410deb421a';
```

Search Transactions by transaction sender:
```sql
SELECT * FROM transactions_by_address WHERE from_address='0xa53a13a80d72a855481de5211e7654fabdfe3526';
```

Search NFTs by contract_address and token_id:
```sql
SELECT * FROM nfts WHERE contract_address='0x7A8cE4BeFfE38f431A2f12e1a8B7d7dAE62DF359' AND token_id='100';
```

Search ERC20 Tokens by block_number and address:
```sql
SELECT * FROM tokens WHERE block_number=12613232 AND address='0x17c5134461f501b4c00ac8082d2d5a3ff0ba2d3e';
```

Search Token Transfers by transaction_hash, block_number, and log_index:
```sql
SELECT * FROM token_transfers WHERE transaction_hash='0x463396d2690820c2895df4838445d0dc009aa7f61ca09ba09298377d4da041b2' AND block_number=4967992 AND log_index=123;
```

Search Token Transfers by token address:
```sql
SELECT * FROM token_transfers_by_token_address WHERE SELECT * FROM token_transfers_by_token_address WHERE token_address='0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48';
```

Search Logs by block_number, transaction_hash, and log_index:
```sql
SELECT * FROM logs WHERE transaction_hash = '0xd81829eef1642054fad5077a3ca234654771187af5c6dc3b8bd6a9d2ddc7078a' and block_number = 15832763 and log_index = 44;
```

Search for decoded data by block_number, transaction_hash, and log_index:
```sql
SELECT decoded_data FROM logs WHERE transaction_hash = '0xd81829eef1642054fad5077a3ca234654771187af5c6dc3b8bd6a9d2ddc7078a' and block_number = 15832763 and log_index = 44;
```

Search asset historical balances by wallet or contract address:
```sql
SELECT * FROM assets where address='0xa53a13a80d72a855481de5211e7654fabdfe3526';
```

Search for human readable event signatures by event hash:
```sql
SELECT * FROM event_signatures WHERE event_hex='0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef';
```

## 3 Request Access to Astra Block
You're now ready to give Astra Block a try! Request access by clicking the button below:

<<launchRequestAstraBlock>>
