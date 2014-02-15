
***

## tag相关
```
git tag v0.1.0 c653d53f2832ab018224df620d87687014cec724 #为某次提交打tag

git tag #显示所有的tag
 
git show v0.1.0 #查看本地tag
 
git ls-remote -t #查看远程tag
 
git tag -d v0.1.0 #删除本地tag v0.1.0

git push origin :refs/tags/v0.1.0 #删除远程tag

git push origin v0.1.0 #把某个tag push到远程，默认的git push不会push tag信息
 
git push origin --tags #push所有的tag
```