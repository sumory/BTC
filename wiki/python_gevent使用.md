
***


## linux下使用

#### 安装
* apt-get install python-dev
* apt-get install python-pip
* apt-get install libevent-dev
* pip install gevent
* pip install geventhttpclient

## windows下使用

#### 安装
* 安装python2.7
* 安装greenlet，http://www.lfd.uci.edu/~gohlke/pythonlibs/#greelet
* 安装gevent，http://www.lfd.uci.edu/~gohlke/pythonlibs/#gevent

#### 测试代码

```
import struct
import gevent
from gevent import socket

if __name__ == '__main__':
    str = struct.pack('>Ii',10,20)
    print struct.unpack('>Ii',str)

    urls = ['www.baidu.com','www.google.com']
    jobs = [gevent.spawn(socket.gethostbyname,url) for url in urls]
    gevent.joinall(jobs,timeout=2)
    print [job.value for job in jobs]
```