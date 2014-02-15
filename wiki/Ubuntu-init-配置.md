### 时区设置，避免8个小时问题
tzselect
按照提示进行选择时区，然后执行date命令查看时间，发现还早8个小时
sudo ntpdate cn.pool.ntp.org
cn.pool.ntp.org是位于中国的公共NTP服务器，用来同步你的时间，之后再执行date查看，发现时间对了

### 安装mysql
```
apt-get install mysql-server mysql-client
安装时设置root xlproot123
注释掉my.cnf里的bind
执行
grant all privileges  on *.* to root@'%' identified by "root";#这里才会在user表里产生Host=“%”的记录
再执行
update user set Password=password('xlproot123') where Host="%" and User="root";
然后远程navicat即可
```

### Node.js
```
wget http://nodejs.org/dist/v0.8.25/node-v0.8.25-linux-x64.tar.gz
```

### 配置/etc/profile
```
JAVA_HOME=/home/software/jdk1.6.0_29
NODE_HOME="/home/software/node-0.8.25"

NODE_PATH="$NODE_HOME:$NODE_HOME/lib/node_modules"
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
	  
PATH="$NODE_HOME/bin:$NODE_HOME/bin:$JAVA_HOME/bin:$PATH"
export JAVA_HOME NODE_HOME NODE_PATH PATH
```

### Tomcat
get请求编码设置--tomcat的server.xml文件
为了保证get数据采用UTF8编码，在server.xml中进行了如下设置 ，在8080那一行加上URIEncoding="UTF-8"
```
<connector port="8080" maxthreads="150" minsparethreads="25" maxSpareThreads="75" enableLookups="false" redirectPort="8443" 
acceptCount="100" debug="99" connectionTimeout="20000" 
disableUploadTimeout="true" URIEncoding="UTF-8"/> 
```

