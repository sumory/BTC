
***

### 文件服务器
使用如下一行代码即可构建一个html预览
```
while true; do { echo -e 'HTTP/1.1 200 OK\r\n'; cat index.html; } | nc -l 8080; done
```

### 传文件
避免使用`scp`不方便的问题
```
机器A上： nc -l 端口号 < 待传输文件名
机器B上： nc 机器A的IP 端口号 > 待传输文件名
```