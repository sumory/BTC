***
> 可以参考http://qinxuye.me/article/details-about-time-module-in-python/  

**struct_time**

tm_year（年）	 比如2011   
tm_mon（月）	 1 - 12  
tm_mday（日）	 1 - 31  
tm_hour（时）	 0 - 23  
tm_min（分）	 0 - 59  
tm_sec（秒）	 0 - 61  
tm_wday（weekday）	 0 - 6（0表示周日）  
tm_yday（一年中的第几天）	 1 - 366  
tm_isdst（是否是夏令时）	 默认为-1  


**time.strftime(format[, t])**：把一个代表时间的元组或者struct_time（如由time.localtime()和time.gmtime()返回）转化为格式化的时间字符串。如果t未指定，将传入time.localtime()。如果元组中任何一个元素越界，ValueError的错误将会被抛出。

格式	含义
%a	本地（locale）简化星期名称	 
%A	本地完整星期名称	 
%b	本地简化月份名称	 
%B	本地完整月份名称	 
%c	本地相应的日期和时间表示	 
%d	一个月中的第几天（01 - 31）	 
%H	一天中的第几个小时（24小时制，00 - 23）	 
%I	第几个小时（12小时制，01 - 12）	 
%j	一年中的第几天（001 - 366）	 
%m	月份（01 - 12）	 
%M	分钟数（00 - 59）	 
%p	本地am或者pm的相应符	
%S	秒（01 - 61）	
%U	一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周。	
%w	一个星期中的第几天（0 - 6，0是星期天）	
%W	和%U基本相同，不同的是%W以星期一为一个星期的开始。	 
%x	本地相应日期	 
%X	本地相应时间	 
%y	去掉世纪的年份（00 - 99）	 
%Y	完整的年份	 
%Z	时区的名字（如果不存在为空字符）	 
%%	‘%’字符