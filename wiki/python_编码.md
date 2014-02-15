***

> 在系统变量加入PYTHONIOENCODING，值填写utf-8

```
# -*- coding: utf-8 -*- 

# windows下需要gbk显示（'中文'.decode('utf-8').encode('gbk'),设置环境变量后不需要再如此显示中文）

# sublime运行正常,但在cmd里乱码
print '中文'
print '看看直接有没有问题乱码'

# cmd正常,sublime里出错：[Decode error - output not utf-8]
print '中文'.decode('utf-8').encode('gbk')
```

sublime text2里ctrl+b正常显示中文