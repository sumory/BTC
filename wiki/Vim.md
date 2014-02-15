***

 - `ctr+w+h` 光标focus左侧树形目录，`ctrl+w+l` 光标focus右侧文件显示窗口。 
 - `ctrl+w+w`，光标自动在左右侧窗口切换 
 
 <br>
 
 - `gi` split一个新窗口打开选中文件，但不跳到该窗口 
 - `i` split一个新窗口打开选中文件，并跳到该窗口
 - `o` 在已有窗口中打开文件、目录或书签，并跳到该窗口
 - `go` 在已有窗口 中打开文件、目录或书签，但不跳到该窗口
 
 <br>
 - `!` 执行当前文件

 <br>
 - `o` 在已有窗口中打开文件、目录或书签，并跳到该窗口
 - `O` 递归打开选中结点下的所有目录
 - `x` 合拢选中结点的父目录
 - `X` 递归合拢选中结点下的所有目录
 
 <br>
 - 在vimrc下添加
```
set number

" 制表符统一缩进为4
set tabstop=4
set softtabstop=4
set shiftwidth=4

" 用空格代替制表符
set expandtab

" 设置history文件中需要记录的行数
set history=1000

" 高亮显示匹配的括号
set showmatch


" 继承前一行的缩进方式，特别适合注释
set autoindent

nnoremap <silent> <F5> :NERDTree<CR>
```