

 - rsync
```
#运行这个命令以后，foo bar 这两个文件夹的内容就递归神同步了，内容没有变化的文件不会被同步，bar 里多余的文件会删除
#可以支持在后台默默运行或者在本地和远程机器上做同步
rsync -rc --delete foo/. bar/. 
```
 - date
```
date --date="1 hours ago" +%Y.%m.%d.%H
```

 - 杀进程
```
#!/bin/bash
kill `ps -ef | grep hudson.war | grep -v grep | awk '{ print $2 }'`
```

 - 查找文件
```
find . -maxdepth 1 -name "@*" 
find /  -type f -size +500M
```

 - 查看文件大小
```
du -h git --max-depth=1|sort -n
```

 - nohup运行
```
nohup ./<script_name> >/dev/null 2>&1 &
同时，可以通过：ps axl | grep <script_name>来监视程序是否在仍后台运行
```


 - `awk`执行命令
```
awk '{count++;print count" "$1;cmd="bitcoind addnode "$1" onetry";cmd|getline;}' ip2.txt
```


 - 当前目录下每个文本文件的第1-3列内容，输入到上层文件夹的同名文件
```
ls *.txt | xargs -i -n 1 sh -c "cut -f 1-3 {} > ../{}"
```

 - 生成序列
```
for i in `seq 1 5`; do echo $i; done
```

 - 查找目录下大文件
```
du -sk * .??* | sort -rn | head
```

 - lsof
```
lsof是linux最常用的命令之一，通常的输出格式为：
 
引用
COMMAND     PID   USER   FD      TYPE     DEVICE     SIZE       NODE NAME
 
常见包括如下几个字段：更多的可见manual。
> COMMAND
默认以9个字符长度显示的命令名称。可使用+c参数指定显示的宽度，若+c后跟的参数为零，则显示命令的全名
> PID：进程的ID号
> PPID
父进程的IP号，默认不显示，当使用-R参数可打开。
> PGID
进程组的ID编号，默认也不会显示，当使用-g参数时可打开。
> USER
命令的执行UID或系统中登陆的用户名称。默认显示为用户名，当使用-l参数时，可显示UID。
> FD
是文件的File Descriptor number  

lsof -i #用以显示符合条件的进程情况，语法: lsof -i[46] [protocol][@hostname|hostaddr][:service|port]
lsof -i :22 #查看22端口

lsof -p 1 #看进程号为1的进程打开了哪些文件

lsof +d /home/oracle #依照文件夹/home/oracle来搜寻，但不会打开子目录，用来显示目录下被进程开启的文件
```

 - 查看端口、程序使用情况
```
lsof -Pnl +M -i4
COMMAND     PID     USER   FD   TYPE   DEVICE SIZE/OFF NODE NAME
ntpd       1055      104   16u  IPv4     8372      0t0  UDP *:123 
ntpd       1055      104   18u  IPv4     8379      0t0  UDP 127.0.0.1:123 
ntpd       1055      104   19u  IPv4     8380      0t0  UDP 10.144.1.107:123 
ntpd       1055      104   20u  IPv4     8381      0t0  UDP 115.28.10.145:123 
python    12310        0   19u  IPv4 10066800      0t0  TCP 127.0.0.1:59344->127.0.0.1:8332 (ESTABLISHED)
python    12310        0   21u  IPv4  9186767      0t0  TCP *:8888 (LISTEN)
python    12310        0   22u  IPv4 12818777      0t0  TCP 115.28.10.145:8888->123.126.133.82:40155 (ESTABLISHED)
python    12310        0   26u  IPv4 12818779      0t0  TCP 115.28.10.145:8888->123.126.133.82:40156 (ESTABLISHED)
python    12310        0   27u  IPv4 12818781      0t0  TCP 115.28.10.145:8888->123.126.133.82:40157 (ESTABLISHED)
python    12310        0   30u  IPv4 12854984      0t0  TCP 115.28.10.145:8888->123.126.133.81:46161 (ESTABLISHED)
python    12310        0   32u  IPv4 12714830      0t0  TCP 115.28.10.145:8888->123.126.133.83:33566 (ESTABLISHED)
python    12310        0   33u  IPv4 12714832      0t0  TCP 115.28.10.145:8888->123.126.133.83:33567 (ESTABLISHED)
python    12310        0   34u  IPv4 12714834      0t0  TCP 115.28.10.145:8888->123.126.133.83:33568 (ESTABLISHED)
python    12310        0   35u  IPv4 12753641      0t0  TCP 115.28.10.145:8888->123.126.133.83:47047 (ESTABLISHED)
python    12310        0   36u  IPv4 12753642      0t0  TCP 115.28.10.145:8888->123.126.133.83:47048 (ESTABLISHED)
python    12310        0   37u  IPv4 12753644      0t0  TCP 115.28.10.145:8888->123.126.133.83:47049 (ESTABLISHED)

-P : This option inhibits the conversion of port numbers to port names for network files. Inhibiting the conver-
sion may make lsof run a little faster. It is also useful when port name lookup is not working properly.
-n : This option inhibits the conversion of network numbers to host names for network files. Inhibiting conversion may make lsof run faster. It is also useful when host name lookup is not working properly.
-l : This option inhibits the conversion of user ID numbers to login names. It is also useful when login name lookup is working improperly or slowly.
+M : Enables the reporting of portmapper registrations for local TCP and UDP ports.
-i4 : IPv4 listing only
-i6 : IPv6 listing only


netstat -npl
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:6881            0.0.0.0:*               LISTEN     6908/python
tcp        0      0 127.0.0.1:631           0.0.0.0:*               LISTEN     5562/cupsd
tcp        0      0 127.0.0.1:3128          0.0.0.0:*               LISTEN     6278/(squid)
tcp        0      0 127.0.0.1:25            0.0.0.0:*               LISTEN     5854/exim4
udp        0      0 0.0.0.0:32769           0.0.0.0:*                          6278/(squid)
udp        0      0 0.0.0.0:3130            0.0.0.0:*                          6278/(squid)
udp        0      0 0.0.0.0:68              0.0.0.0:*                          4583/dhclient3
udp        0      0 0.0.0.0:6881            0.0.0.0:*                          6908/python   

-t : TCP port
-u : UDP port
-l : Show only listening sockets.
-p : Show the PID and name of the program to which each socket / port belongs
-n : No DNS lookup (speed up operation)
```
