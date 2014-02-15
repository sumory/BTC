**1. 安装package controll**
```
import urllib2,os; pf='Package Control.sublime-package'; ipp=sublime.installed_packages_path(); os.makedirs(ipp) if not os.path.exists(ipp) else None; urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler())); open(os.path.join(ipp,pf),'wb').write(urllib2.urlopen('http://sublime.wbond.net/'+pf.replace(' ','%20')).read()); print 'Please restart Sublime Text to finish installation'
```

**2. ctrl + shit + p 调出安装工具**

**3. go环境配置**

GoSublime(Preferences菜单下，找到Package Settings，然后找到 GoSublime，再往下找到 Settings - Default配置go path)、SidebarEnhancements和Go Build

安装gocode
```
go get github.com/nsf/gocode
go install github.com/nsf/gocode
```

ctrl + b 打开go控制台运行程序

**4. 安装JsFormat**

https://github.com/jdc0589/JsFormat  
格式化javascript,ctrl + alt + f

**5. DocBlockr**

用于注释,类似eclipse /**/

**6. BracketHighlighter**

用于高亮成对符号（引号、括号、标签）的工具

**7. livereload**

安装插件LiveReload  
在chrome里安装插件https://chrome.google.com/extensions/detail/jnihajbhpnppcggbcgedagnkighmdlei  
并在扩展程序里设置该插件允许文件url

**8. 运行nodejs**

选择菜单 Tools --> Build System --> new Build System... 
将文件保存为 JavaScript.sublime-build
文件内容为：

{  
        "cmd": ["node", "$file"],  
        "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",  
        "selector": "source.javascript"  
}  

重新启动 Sublime Text 2  
勾选菜单 Tools --> Build System --> JavaScript  
可以使用 Ctrl + b 来执行JavaScript 程序