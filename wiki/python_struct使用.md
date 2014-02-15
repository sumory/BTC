***
struct模块中最主要的三个函数式pack()、unpack()、calcsize():
```
pack(fmt, v1, v2, ...)  ------ 根据所给的fmt描述的格式将值v1，v2，...转换为一个字符串。
unpack(fmt, bytes)      ------ 根据所给的fmt描述的格式将bytes反向解析出来，返回一个元组。
calcsize(fmt)           ------ 根据所给的fmt描述的格式返回该结构的大小。
```

### 对照表

<table cellspacing="1" cellpadding="1" width="500px" style="border:1px solid #fff">
    <tbody>
        <tr>
            <td> Format</td>
            <td>          C Type</td>
            <td>              Python</td>
            <td>    字节数</td>
        </tr>
        <tr>
            <td>         x</td>
            <td>    pad byte</td>
            <td>    no value</td>
            <td>         1</td>
        </tr>
        <tr>
            <td>         c</td>
            <td>    char</td>
            <td>bytes of length 1</td>
            <td>         1</td>
        </tr>
        <tr>
            <td>         b</td>
            <td>    signed char</td>
            <td>    integer</td>
            <td>         1</td>
        </tr>
        <tr>
            <td>         B</td>
            <td>   unsigned char</td>
            <td>    integer</td>
            <td>         1</td>
        </tr>
        <tr>
            <td>         ?</td>
            <td>   _Bool</td>
            <td>    bool</td>
            <td>         1</td>
        </tr>
        <tr>
            <td>         h</td>
            <td>
               short
            </td>
            <td>    integer</td>
            <td>         2</td>
        </tr>
        <tr>
            <td>         H</td>
            <td>   unsigned short</td>
            <td>    integer</td>
            <td>         2</td>
        </tr>
        <tr>
            <td>         i</td>
            <td>   int</td>
            <td>    integer</td>
            <td>         4</td>
        </tr>
        <tr>
            <td>         I</td>
            <td>   unsigned int</td>
            <td>    integer</td>
            <td>         4</td>
        </tr>
        <tr>
            <td>         l</td>
            <td>   long</td>
            <td>    integer</td>
            <td>         4</td>
        </tr>
        <tr>
            <td>         L</td>
            <td>   unsigned long</td>
            <td>    integer</td>
            <td>         4</td>
        </tr>
        <tr>
            <td>        q</td>
            <td>   long long</td>
            <td>    integer</td>
            <td>         8</td>
        </tr>
<tr>
<td> Q</td>
<td> unsigned long long</td>
<td> integer</td>
<td> 8</td>
</tr>
<tr>
<td>f</td>
<td> float</td>
<td>float</td>
<td> 4</td>
</tr>
<tr>
<td>d</td>
<td> double</td>
<td> float</td>
<td> 8</td>
</tr>
<tr>
<td> s</td>
<td> char[]</td>
<td> bytes</td>
<td> 1</td>
</tr>
<tr>
<td> p</td>
<td> char[]</td>
<td> bytes</td>
<td> 1</td>
</tr>
<tr>
<td> P</td>
<td> void *</td>
<td> integer</td>
<td></td>
</tr>
</tbody>
</table>

注1. q和Q只在机器支持64位操作时有意思  
注2. 每个格式前可以有一个数字，表示个数  
注3. s格式表示一定长度的字符串，4s表示长度为4的字符串，但是p表示的是pascal字符串  
注4. P用来转换一个指针，其长度和机器字长相关  
注5. 最后一个可以用来表示指针类型的，占4个字节  

### 关于对齐方式
可以用格式中的第一个字符来改变对齐方式.定义如下：
<table cellspacing="1" cellpadding="1" width="500px" style="border:1px solid #fff">
    <thead valign="bottom">
        <tr>
            <th>Character</th>
            <th>Byte order</th>
            <th>Size and alignment</th>
        </tr>
    </thead>
    <tbody valign="top">
        <tr>
            <td>@</td>
            <td>native</td>
            <td>native            凑够4个字节</td>
        </tr>
        <tr>
            <td>=</td>
            <td>native</td>
            <td>standard        按原字节数</td>
        </tr>
        <tr>
            <td>&lt;</td>
            <td>little-endian</td>
            <td>standard        按原字节数</td>
        </tr>
        <tr>
            <td>></td>
            <td>big-endian</td>
            <td>standard       按原字节数</td>
        </tr>
        <tr>
            <td>!</td>
            <td>network (= big-endian)</td>
            <td>standard       按原字节数</td>
        </tr>
    </tbody>
</table>

### 例子

**例一**：比如有一个报文头部在C语言中是这样定义的  
```
struct header
{
    unsigned short  usType;
    char[4]         acTag;
    unsigned int      uiVersion;
    unsigned int      uiLength;
};
```
在C语言对将该结构体封装到一块缓存中是很简单的，可以使用memcpy()实现。在Python中，使用struct就需要这样：  
```
str = struct.pack('B4sII', 0x04, 'aaaa', 0x01, 0x0e)
```
`'B4sII'`:有一个unsigned short、char[4], 2个unsigned int。其中s之前的数字说明了字符串的大小。  
type, tag, version, length = struct.unpack('B4sll', str)


**例二**：一个结构体，通过socket.recv接收到了一个上面的结构体数据，存在字符串s中，现在需要把它解析出来，可以使用unpack()函数.

```
struct Header
{
    unsigned short id;
    char[4] tag;
    unsigned int version;
    unsigned int count;
}

# python:
import struct
id, tag, version, count = struct.unpack("!H4s2I", s)
```
上面的格式字符串中，!表示我们要使用网络字节顺序解析，因为我们的数据是从网络中接收到的，在网络上传送的时候它是网络字节顺序的.后面的H表示 一个unsigned short的id,4s表示4字节长的字符串，2I表示有两个unsigned int类型的数据.  

同样，也可以很方便的把本地数据再pack成struct格式.  
```
ss = struct.pack("!H4s2I", id, tag, version, count);
```

**例三**  
```
a,=struct.unpack('i',bytes)
# 注意，unpack返回的是tuple

# 所以如果只有一个变量的话：
bytes=struct.pack('i',a)

# 那么，解码的时候需要这样
a,=struct.unpack('i',bytes) 
# 或
(a,)=struct.unpack('i',bytes)

#如果直接用a=struct.unpack('i',bytes)，那么 a=(12.34,) ，是一个tuple而不是原来的浮点数了
```


**例四**：二进制文件处理时会碰到的问题  
  
处理二进制文件时，需要用如下方法
```
binfile=open(filepath,'rb')    读二进制文件
binfile=open(filepath,'wb')    写二进制文件
```

那么和binfile=open(filepath,'r')的结果到底有何不同呢？

不同之处有两个地方：

第一，使用'r'的时候如果碰到'0x1A'，就会视为文件结束，这就是EOF。使用'rb'则不存在这个问题。即，如果你用二进制写入再用文本读出的话，如果其中存在'0X1A'，就只会读出文件的一部分。使用'rb'的时候会一直读到文件末尾。

第二，对于字符串x='abc\ndef'，我们可用len(x)得到它的长度为7，\n我们称之为换行符，实际上是'0X0A'。当我们用'w'即文本方式写的时候，在windows平台上会自动将'0X0A'变成两个字符'0X0D'，'0X0A'，即文件长度实际上变成8.。当用'r'文本方式读取时，又自动的转换成原来的换行符。如果换成'wb'二进制方式来写的话，则会保持一个字符不变，读取时也是原样读取。所以如果用文本方式写入，用二进制方式读取的话，就要考虑这多出的一个字节了。'0X0D'又称回车符。linux下不会变。因为linux只使用'0X0A'来表示换行。
