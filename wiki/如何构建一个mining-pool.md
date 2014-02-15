> slush pool作者的设计思路，[stratum协议和mining pool的创建](http://mining.bitcoin.cz/stratum-mining)

## 一个真实的例子

这是个在测试网络中的矿池挖矿的例子  
[000000002076870fe65a2b6eeed84fa892c0db924f1482243a6247d931dcab32](http://blockexplorer.com/testnet/block/000000002076870fe65a2b6eeed84fa892c0db924f1482243a6247d931dcab32)

#### 矿工连接到服务器

在一开始，客户端订阅（subscribe）当前连接一边接受后续的挖矿任务:

```
{"id": 1, "method": "mining.subscribe", "params": []}\n
{"id": 1, "result": [[["mining.set_difficulty", "b4b6693b72a50c7116db18d6497cac52"], ["mining.notify", "ae6812eb4cd7735a302a8a9dd95cf71f"]], "08000002", 4], "error": null}\n
```

提醒: 换行符`\n`是信息必要的一部分，而且必须加到每条JSON信息的末尾。服务器端需要等待这个magic字符以便之后开始处理信息。这是在实现客户端时常见的一个错误。

结果包括三个item:

Subscriptions details - 由subscribed notification和subscription ID组成的二元组. 理论上它可以被用于解除订阅，但明显地矿工并不需要它。
Extranonce1 - 使用十六进制编码，每个连接拥有的唯一的一个字符串，它之后将用于`coinbase`序列化。请确保它是安全保密的！
Extranonce2_size - 期望的`extranonce2`长度，`extranonce2`之后是由矿机产生的。
Authorize workers

Now let authorize some workers. You can authorize as many workers as you wish and at any time during the session. In this way, you can handle big basement of independent mining rigs just by one Stratum connection.

{"params": ["slush.miner1", "password"], "id": 2, "method": "mining.authorize"}\n
{"error": null, "id": 2, "result": true}\n
Server start sending notifications with mining jobs

Server sends one job *almost* instantly after the subscription.

Small engineering note: There's a good reason why first job is not included directly in subscription response - miner will need to handle one response type in two different way; firstly as a subscription response and then as a standalone notification. Hook job processing just to JSON-RPC notification sounds a bit better to me.

{"params": ["bf", "4d16b6f85af6e2198f44ae2a6de67f78487ae5611b77c6c0440b921e00000000",
"01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff20020862062f503253482f04b8864e5008",
"072f736c7573682f000000000100f2052a010000001976a914d23fcdf86f7e756a64a7a9688ef9903327048ed988ac00000000", [],
"00000002", "1c2ac4af", "504e86b9", false], "id": null, "method": "mining.notify"}
Now we finally have some interesting stuff here! I'll descibe every field of the notification in the particular order:

job_id - ID of the job. Use this ID while submitting share generated from this job.
prevhash - Hash of previous block.
coinb1 - Initial part of coinbase transaction.
coinb2 - Final part of coinbase transaction.
merkle_branch - List of hashes, will be used for calculation of merkle root. This is not a list of all transactions, it only contains prepared hashes of steps of merkle tree algorithm. Please read some materials for understanding how merkle trees calculation works. Unfortunately this example don't have any step hashes included, my bad!
version - Bitcoin block version.
nbits - Encoded current network difficulty
ntime - Current ntime/
clean_jobs - When true, server indicates that submitting shares from previous jobs don't have a sense and such shares will be rejected. When this flag is set, miner should also drop all previous jobs, so job_ids can be eventually rotated.
How to build coinbase transaction

Now miner received all data required to serialize coinbase transaction: Coinb1, Extranonce1, Extranonce2_size and Coinb2. Firstly we need to generate Extranonce2 (must be unique for given job_id!). Extranonce2_size tell us expected length of binary structure. Just be absolutely sure that your extranonce2 generator always produces extranonce2 with correct length! For example my pool implementation sets extranonce2_size=4, which mean this is valid Extranonce2 (in hex): 00000000.

To produce coinbase, we just concatenate Coinb1 + Extranonce1 + Extranonce2 + Coinb2 together. That's all!

For following calculations we have to produce double-sha256 hash of given coinbase. In following snippets I'm using Python, but I'm sure you'll understand the concept even if you're a rubyist! It is as simple as:

import hashlib
import binascii
coinbase_hash_bin = hashlib.sha256(hashlib.sha256(binascii.unhexlify(coinbase)).digest()).digest()
How to build merkle root

Following Python snippet will generate merkle root for you. Use merkle_branch from broadcast and coinbase_hash_bin from previous snippet as an input:

import binascii

def build_merkle_root(self, merkle_branch, coinbase_hash_bin):
    merkle_root = coinbase_hash_bin
    for h in self.merkle_branch:
        merkle_root = doublesha(merkle_root + binascii.unhexlify(h))
    return binascii.hexlify(merkle_root)
How to build block header?

Now we're almost done! We have to put all together to produce block header for hashing:

version + prevhash + merkle_root + ntime + nbits + '00000000' +
'000000800000000000000000000000000000000000000000000000000000000000000000000000000000000080020000'
First zeroes are blank nonce, the rest is padding to uint512 and it is always the same.

Note that merkle_root must be in reversed byte order. If you're a miner developer, you already have util methods there for doing it. For some example in Python see Stratum mining proxy source codes.

Server can occasionally ask miner to change share difficulty

Default share difficulty is 1 (big-endian target for difficulty 1 is 0x00000000ffff0000000000000000000000000000000000000000000000000000), but server can ask you anytime during the session to change it:

{ "id": null, "method": "mining.set_difficulty", "params": [2]}
This means that difficulty 2 will be applied to every next job received from the server.

How to submit share?

When miner find the job which meets requested difficulty, it can submit share to the server:

{"params": ["slush.miner1", "bf", "00000001", "504e86ed", "b2957c02"], "id": 4, "method": "mining.submit"}
{"error": null, "id": 4, "result": true}
Values in particular order: worker_name (previously authorized!), job_id, extranonce2, ntime, nonce.

That's it!

Downloads

Stratum mining proxy - Source code of Stratum proxy on Github
Windows binaries (EXE) of Stratum mining proxy - Detailed instructions can be found here.
Stratum mining pool - Opensource bitcoin mining pool build on Stratum server framework in Python.
Compatible miners

For all current getwork-compatible miners you can use Stratum mining proxy running locally on your mining computer. One mining proxy can handle (almost) unlimited number of connected workers, so running one proxy for all of your mining rigs is a way to go.

Miners with native support of Stratum protocol (no proxy needed!)

poclbm (version 20120920 and newer)
cgminer (version 2.8.1 and newer)
I'm currently working with authors of GUIminer on native support of Stratum mining protocol in their miner. Stay tuned! If you want suport of Stratum protocol in your miner, just ask its developer and show him this page. Also don't hesitate to contact me and ask for implementation details.