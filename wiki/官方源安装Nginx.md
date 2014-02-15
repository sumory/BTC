
***

升级前先备份后自己的配置文件: `sudo cp -r /etc/nginx  /etc/nginx.bak`

Ubuntu 从官方源安装 Nginx (下面以12.04为例, precise 是12.04的版本代号):  
```
cd ~  
wget http://nginx.org/keys/nginx_signing.key  
sudo apt-key add nginx_signing.key  
sudo nano /etc/apt/sources.list     # 添加以下两句  
deb http://nginx.org/packages/ubuntu/ precise nginx  
deb-src http://nginx.org/packages/ubuntu/ precise nginx  
sudo apt-get update  
sudo apt-get install nginx 
```
#升级后平滑启动Nginx
``` 
sudo service nginx upgrade 
```