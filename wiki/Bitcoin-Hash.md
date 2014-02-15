
***

**散列**：bitcoin在计算散列时一般会计算2次。第一轮总是使用SHA-256散列，而第二次在大多数情况下，也是使用SHA-256散列，但用于生成较短的散列(例如生成 bitcoin接收地址的时候)会用RIPEMD-160散列。

```
hello
 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 ( sha-256)
 9595c9df90075148eb06860365df33584b75bff782a510c6cd4883a419833d50 (sha-256)
```

生成比特币地址时(RIPEMD-160)：
```
hello
 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824 (sha-256)
 b6a9c8c230722b7c748331a8b450f05566dc7d0f (ripemd-160)
```

Addresses: Bitcoin Address是ECDSA公钥(public key)的散列，计算方法如下：  
```
if 正式网络
    Version=0x00
else if 测试网络
    Version=0x6F
end

key_hash=Version+RIPEMD-160(SHA-256(public_key))
Checksum = SHA-256(SHA-256(Key hash))[0..3]  #取两次散列值后的前4位
Bitcoin_Address = Base58Encode(Key_hash+Checksum)
#Base58编码做了特殊处理，与通用的base58有一些区别：转换的时候
#前面的0被作为单个0保留。
```


