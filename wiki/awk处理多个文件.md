***
**awk**在linux/unix下可以非常方便地处理文本和数据，可以在命令行使用，但更多的是作为一种脚本语言使用。  
相关处理命令有`NR`、`FNR`、`ARGIND`、`ARGV` 和`FILENAME`


变量释义如下：

 - NR：整个脚本当前已经读过的记录数，就是行号，从1开始。随着所读文件的数目，一直累加。
 - FNR：同NR，不过是相对于当前在读的文件记录数。每开始读一个文件时，从1开始累加，相当于行号。读完一个文件后就会清0，新的文件又会从1
 - ARGIND：命令行中当前文件的位置，从0开始。
 - ARGV：包含命令行参数的数组
 - FILENAME：当前文件名
 
 
 
### NR和FNR可用于处理两个文件
当处理两个文件时，常用的方法有三种：  

```
awk 'NR==FNR{ block1; next} { block2 }' file1 file2
awk 'NR==FNR{ block1 } NR>FNR{ block2 }' file1 file2
awk 'NR==FNR{ block1 } NR!=FNR{ block2 }' file1 file2
```
  处理file1时，NR和FNR随着所读行数增加而递增，一直满足NR==FNR，从而先执行前一个命令块block1。对于1，由于此block1之后中有next命令，会直接读取file1的下一行，后面的命令块block2就不会执行。2和3中一直满足NR==FNR，后面的命令块block2就不会执行。直到读取file1结束

  处理file2时，FNR随着行数增加从1开始计数，而NR会从读完file1是的计数继续递增，因此从读取file2开始，满足NR>FNR，也满足NR!=FNR，1、2和3中的条件NR==FNR都不满足，前面的语句块block1就不会执行，后面的语句块block2开始执行。直到file2处理完毕。

### ARGIND和ARGV都是和命令行相关  

 - ARGV存储的是awk的所有命令行参数，从做到右存放，但是ARGV[0]是’awk‘，之后才是传入的参数
 - ARGIND可以看作是ARGV的下标，ARGIND==0时相当于ARGV[0]

`FILENAME`代表的是当前处理的文件名，可以和`ARGIND`及`ARGV`中的值想比较进行条件判断

```
awk 'ARGIND==1{ block1 } ARGIND==2{ block2 } ARGIND==3{ block3 }' file1 file2 file3
awk 'FILENAME==ARGV[1]{ block1 } FILENAME==ARGV[2]{ block2 } FILENAME==ARGV[3]{ block3 }' file1 file2 file3
awk 'FILENAME=="file1"{ block1 }FILENAME=="file2"{ block2 }FILENAME=="file3"{ block3 }' file1 file2 file3
```
ARGIND的值分别为1、2和3时，对应的语句块block1、block2和block3处理的文件分别是file1、file2和file3。

ARGV[1]的值为file1，FILENAME==ARGV[1]，表示当前处理的文件时file1。此时，ARGV[1]和“file1”等价，满足条件判断即执行相应的语句块。