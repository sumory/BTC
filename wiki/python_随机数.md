```
# -*- coding: utf-8 -*- 

import random
import struct

# random.randrange([start], stop[, step])，从指定范围内，按指定基数递增的集合中 获取一个随机数。
for i in range(5):
	print random.randrange(1 << 2)

# 0<= n <1.0
print random.random()

# 生成的随机数n: a <= n <= b
print random.randint(12, 20)  #生成的随机数n: 12 <= n <= 20  
print random.randint(20, 20)  #结果永远是20  


# random.shuffle的函数原型为：random.shuffle(x[, random])，用于将一个列表中的元素打乱。
list1=[1,2,3,4,5,6]
random.shuffle(list1)
print list1

# random.sample的函数原型为：random.sample(sequence, k)，从指定序列中随机获取指定长度的片断。sample函数不会修改原有序列。
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  
slice1 = random.sample(list2, 5)  #从list中随机获取5个元素，作为一个片断返回  
print slice1  
print list2 #原有序列并没有改变。 


#random.choice从序列中获取一个随机元素。其函数原型为：random.choice(sequence)。参数sequence表示一个有序类型。
#这里要说明 一下：sequence在python不是一种特定的类型，而是泛指一系列的类型。list, tuple, 字符串都属于sequence。
print random.choice("abPython")   
print random.choice(["JGood", "is", "a", "handsome", "boy"])  
print random.choice(("Tuple", "List", "Dict"))  
```