***
> 转自 http://javascript.ruanyifeng.com/library/underscore.html

## 概述

[Underscore.js](http://underscorejs.org/)是一个很精干的库，压缩后只有4KB。它提供了几十种函数式编程的方法，大大方便了Javascript的编程。MVC框架backbone.js就是基于这个库。

它定义了一个下划线（_）对象，函数库的所有方法都属于这个对象。这些方法大致上可以分成：集合（collection）、数组（array）、函数（function）、对象（object）和工具（utility）五大类。

## 在node.js下安装

Underscore.js不仅可以用于浏览器环境，还可以用于node.js。安装命令如下：

```

npm install underscore

```

但是，node.js不能直接使用_作为变量名，因此要用下面的方法使用underscore.js。

```

var u = require("underscore");

```

## 与集合有关的方法

Javascript语言的数据集合，包括两种结构：数组和对象。以下的方法同时适用于这两种结构。

### map

该方法对集合的每个成员依次进行某种操作，将返回的值依次存入一个新的数组。

```

_.map([1, 2, 3], function(num){ return num * 3; });
// [3, 6, 9]

_.map({one : 1, two : 2, three : 3}, function(num, key){ return num * 3; });
// [3, 6, 9]

```

### each

该方法与map类似，依次对集合的每个成员进行某种操作，但是不返回值。

```

_.each([1, 2, 3], alert);

_.each({one : 1, two : 2, three : 3}, alert);

```

### reduce

该方法依次对集合的每个成员进行某种操作，然后将操作结果累计在某一个初始值之上，全部操作结束之后，返回累计的值。

该方法接受三个参数。第一个参数是被处理的集合，第二个参数是对每个成员进行操作的函数，第三个参数是累计用的变量。

```

_.reduce([1, 2, 3], function(memo, num){ return memo + num; }, 0);
// 6

```

reduce方法的第二个参数是操作函数，它本身又接受两个参数，第一个是累计用的变量，第二个是集合每个成员的值。

### filter 和 reject

filter方法依次对集合的每个成员进行某种操作，只返回操作结果为true的成员。

```

_.filter([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
// [2, 4, 6]

```

reject方法只返回操作结果为false的成员。

```

_.reject([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
// [1, 3, 5]

```

### every 和 some

every方法依次对集合的每个成员进行某种操作，如果所有成员的操作结果都为true，则返回true，否则返回false。

```

_.every([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
// false

```

some方法则是只要有一个成员的操作结果为true，则返回true，否则返回false。

```

_.some([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
// true

```

### find

该方法依次对集合的每个成员进行某种操作，返回第一个操作结果为true的成员。如果所有成员的操作结果都为false，则返回undefined。

```

_.find([1, 2, 3, 4, 5, 6], function(num){ return num % 2 == 0; });
// 2

```

### contains

如果某个值在集合内，该方法返回true，否则返回false。

```

_.contains([1, 2, 3], 3);
// true

```

### countBy

该方法依次对集合的每个成员进行某种操作，将操作结果相同的成员算作一类，最后返回一个对象，表明每种操作结果对应的成员数量。

```

_.countBy([1, 2, 3, 4, 5], function(num) {
  return num % 2 == 0 ? 'even' : 'odd';
});
// {odd: 3, even: 2}

```

### shuffle

该方法返回一个打乱次序的集合。

```

_.shuffle([1, 2, 3, 4, 5, 6]);
// [4, 1, 6, 3, 5, 2]

```

### size

该方法返回集合的成员数量。

```

_.size({one : 1, two : 2, three : 3});
// 3

```

## 与对象有关的方法

### toArray

该方法将对象转为数组。

```

 _.toArray({a:0,b:1,c:2});
// [0, 1, 2]

```

### pluck

该方法将多个对象的某一个属性的值，提取成一个数组。

```

var stooges = [{name : 'moe', age : 40}, {name : 'larry', age : 50}, {name : 'curly', age : 60}];

_.pluck(stooges, 'name');
// ["moe", "larry", "curly"]

```

## 与函数相关的方法

### bind

该方法绑定函数运行时的上下文，作为一个新函数返回。

```

_.bind(function, object, [*arguments]) 

```

请看下面的实例。

```

var o = {
	p: 2,
	m: function (){console.log(p);}
};

o.m()
// 2

_.bind(o.m,{p:1})()
// 1

```

### bindAll

该方法将某个对象的所有方法（除非特别声明），全部绑定在该对象上面。

```

var buttonView = {
  label   : 'underscore',
  onClick : function(){ alert('clicked: ' + this.label); },
  onHover : function(){ console.log('hovering: ' + this.label); }
};

_.bindAll(buttonView);

```

### partial

该方法绑定将某个函数与参数绑定，然后作为一个新函数返回。

```

var add = function(a, b) { return a + b; };

add5 = _.partial(add, 5);

add5(10);
// 15

```

### memoize

该方法缓存一个函数针对某个参数的运行结果。

```

var fibonacci = _.memoize(function(n) {
  return n < 2 ? n : fibonacci(n - 1) + fibonacci(n - 2);
});

```

如果一个函数有多个参数，则需要提供一个hashFunction，用来生成标识缓存的哈希值。

### delay

该方法可以将函数推迟指定的时间再运行。

```

var log = _.bind(console.log, console);

_.delay(log, 1000, 'logged later');
// 'logged later'

```

### defer

该方法可以将函数推迟到待运行的任务数为0时再运行，类似于setTimeout推迟0秒运行的效果。

```

_.defer(function(){ alert('deferred'); });

```

### throttle

该方法返回一个函数的新版本。连续调用这个新版本的函数时，必须等待一定时间才会触发下一次执行。

```

// 返回updatePosition函数的新版本
var throttled = _.throttle(updatePosition, 100);

// 新版本的函数每过100毫秒才会触发一次
$(window).scroll(throttled);

```

### debounce

该方法也是返回一个函数的新版本。每次调用这个新版本的函数，必须与上一次调用间隔一定的时间，否则就无效。它的典型应用是防止用户双击某个按钮，导致两次提交表单。

```

$("button").on("click", _.debounce(submitForm, 1000));

```

### once

该方法返回一个新版本的函数，使得这个函数只能被运行一次。主要用于对象的初始化。

```

var initialize = _.once(createApplication);
initialize();
initialize();
// Application只被创造一次

```

### after

该方法返回一个新版本的函数，这个函数只有在被调用一定次数后才会运行，主要用于确认一组操作全部完成后，再做出反应。

```

var renderNotes = _.after(notes.length, render);
_.each(notes, function(note) {
  note.asyncSave({success: renderNotes});
});
// 所有的note都被保存以后，renderNote才会运行一次

```

### wrap

该方法将一个函数作为参数，传入另一个函数，最终返回前者的一个新版本。

```

var hello = function(name) { return "hello: " + name; };
hello = _.wrap(hello, function(func) {
  return "before, " + func("moe") + ", after";
});
hello();
// 'before, hello: moe, after'

```

### compose

该方法接受一系列函数作为参数，由后向前依次运行，上一个函数的运行结果，作为后一个函数的运行参数。也就是说，将f(g(),h())的形式转化为f(g(h()))。

```

var greet    = function(name){ return "hi: " + name; };
var exclaim  = function(statement){ return statement + "!"; };
var welcome = _.compose(exclaim, greet);
welcome('moe');
// 'hi: moe!'

```

## 工具方法

### template

该方法用于编译HTML模板。它接受三个参数。

```

_.template(templateString, [data], [settings]) 

```

三个参数的含义如下：

- templateString：模板字符串
- data：输入模板的数据
- settings：设置

#### templateString

模板字符串templateString就是普通的HTML语言，其中的变量使用<%= … %>的形式插入；data对象负责提供变量的值。

```

var txt = "<h2><%= word %></h2>";

_.template(txt, {word : "Hello World"})
// "<h2>Hello World</h2>"

```

如果变量的值包含五个特殊字符（& < > " ' /），就需要用<%- ... %>转义。

```

var txt = "<h2><%- word %></h2>";

_.template(txt, {word : "H & W"})
// <h2>H &amp; W</h2>

```

JavaScript命令可以采用<% … %>的形式插入。下面是判断语句的例子。

```

var txt = "<% var i = 0; if (i<1){ %>"
		+ "<%= word %>"
		+ "<% } %>";

_.template(txt, {word : "Hello World"})
// Hello World

```

常见的用法还有循环语句。

```

var list = "<% _.each(people, function(name) { %> <li><%= name %></li> <% }); %>";

_.template(list, {people : ['moe', 'curly', 'larry']});
// "<li>moe</li><li>curly</li><li>larry</li>"

```

如果template方法只有第一个参数templateString，省略第二个参数，那么会返回一个函数，以后可以向这个函数输入数据。

```

var t1 = _.template("Hello <%=user%>!");  

t1({ user: "<Jane>" }) 
// 'Hello <Jane>!'

```

#### data

templateString中的所有变量，在内部都是obj对象的属性，而obj对象就是指第二个参数data对象。下面两句语句是等同的。

```

_.template("Hello <%=user%>!", { user: "<Jane>" })
_.template("Hello <%=obj.user%>!", { user: "<Jane>" })

```

如果要改变obj这个对象的名字，需要在第三个参数中设定。

```

_.template("<%if (data.title) { %>Title: <%= title %><% } %>", null,
                { variable: "data" });

```

因为template在变量替换时，内部使用with语句，所以上面这样的做法，运行速度会比较快。

## 参考链接

- [Using Underscore.js's debounce() to filter double-clicks](http://eng.wealthfront.com/2012/12/using-underscorejss-debounce-to-filter.html)i
- Dr. Axel Rauschmayer, [A closer look at Underscore templates](http://www.2ality.com/2012/06/underscore-templates.html)