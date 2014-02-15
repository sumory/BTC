### 产生一个新地址
```
getnewaddress [account], 不加account产生在默认的空账户下

getnewaddress mine
myTg3Lwcpb4w9uCszJjM6sAMJ6axBwWBvR
```


### 获得一些基本信息
```
getinfo 
{
	"version" : 80500,
	"protocolversion" : 70001,
	"walletversion" : 60000,
	"balance" : 8173.91119388,
	"blocks" : 116269,
	"timeoffset" : -2,
	"connections" : 7,
	"proxy" : "",
	"difficulty" : 5.30443756,
	"testnet" : true,
	"keypoololdest" : 1381385737,
	"keypoolsize" : 98,
	"paytxfee" : 0.00000000,
	"unlocked_until" : 0,
	"errors" : ""
}
```


### 获取列表：账户和账户里的钱
 - listaccounts [minconf=1]

 - listaccounts 如果没有参数，默认给定参数1

 - listaccounts 0 这样才能显示出所有的账户的钱
 
 - 给自己钱包内的地址打钱时，如果不设为0，则没确认前，发送地址的账户钱少了，但目的地址所在的账户并没有多出钱来

 - 往外面的地址打钱时，不管是不是被确认，listaccounts 0显示的都是被扣完款后的数额

```
{
  "" : -410.10000000,
  "mine" : 0.00000000,
  "own_server_test" : 2102.85805635,
  "pool" : 5246.58524741,
  "test1" : 1.00000000,
  "test2" : 1233.56789012
}
```

### 按地址显示每笔'接收'交易
```
listreceivedbyaddress 
[
  {
    "address" : "mmMdjfWLEEr3LFWB1TFrF6ytgCU9hcginh",
    "account" : "test2",
    "amount" : 1234.56789012,
    "confirmations" : 14951
  }
]
```

### 按账户显示所有的交易，可分页
```
listtransactions	 [account] [count=10] [from=0]

listtransactions mine
[
  {
    "account" : "mine",
    "address" : "myTg3Lwcpb4w9uCszJjM6sAMJ6axBwWBvR",
    "category" : "receive",
    "amount" : 11.00000000,
    "confirmations" : 0,
    "txid" : "551f05f7492b2848c7eccfc4c13c4e5478fc2f6bde7d8311440f916e5415f87e",
    "time" : 1381392999,
    "timereceived" : 1381392999
  },
  {
    "account" : "mine",
    "address" : "myTg3Lwcpb4w9uCszJjM6sAMJ6axBwWBvR",
    "category" : "receive",
    "amount" : 1.00000000,
    "confirmations" : 0,
    "txid" : "acd55aacba8ccf8da51284deff58eeb419218ddeb1185b9e80cfb5d13f9239fa",
    "time" : 1381393008,
    "timereceived" : 1381393008
  },
  {
    "account" : "mine",
    "address" : "myTg3Lwcpb4w9uCszJjM6sAMJ6axBwWBvR",
    "category" : "receive",
    "amount" : 2.00000000,
    "confirmations" : 0,
    "txid" : "02c538a0c38a17ded3b2de3a20c25e9761881ceb0e107c055e135ecd9a563634",
    "time" : 1381393015,
    "timereceived" : 1381393015
  }
]


```

### 获得某个账户的钱
```
getbalance [account]
如果不加参数，获得的是全部钱包的钱
```

### 获得某个账户下的所有地址
```
getaddressesbyaccount ''
[
  "ms4F9Sb44ZGVjrC84URggRUivSeHbjDeqm",
  "n2nYfrAZnWMKsnG6cTVSaKNGp8FFPLqS2B",
  "n4T6tGhoiS2KmykjWpjeHZJNqi65cTudpb",
  "mnYnjSyqQsdUDVHokbBsseGKHNYK7MLdzX",
  "mqQakEb27XD9za29L5YrH5r8UpqLR2AqRS",
  "mkptjDwjr6ceUhUGf1nWECQto3evCjcH3p"
]

getaddressesbyaccount mine
[
	"myTg3Lwcpb4w9uCszJjM6sAMJ6axBwWBvR"
]

```

### 从某个账户打钱到某个地址

```
sendfrom mine mnB43cJB4jceYQMt8ZjWVDpy7yKJbUM69S 201.2

钱不够会打不出去：Account has insufficient funds (code -6)
正确回来的是txid字符串，不是json
````

### 根据txid查看某笔交易
```
gettransaction

gettransaction 4b3600c732a9ebc478516d6367b9a65a5a499199daaed2edaf26db0ffb43ac9a

{
  "amount" : -201.10000000,
  "fee" : 0.00000000,
  "confirmations" : 0,
  "txid" : "4b3600c732a9ebc478516d6367b9a65a5a499199daaed2edaf26db0ffb43ac9a",
  "time" : 1381393927,
  "timereceived" : 1381393927,
  "details" : [
    {
      "account" : "mine",
      "address" : "mnB43cJB4jceYQMt8ZjWVDpy7yKJbUM69S",
      "category" : "send",
      "amount" : -201.10000000,
      "fee" : 0.00000000
    }
  ]
}

```








