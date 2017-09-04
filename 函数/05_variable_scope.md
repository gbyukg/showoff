<!SLIDE transition=turnUp>
# 变量作用范围

无论是那种编程语言, 每个变量都有自己的访问范围, 如果在超出这个范围内代码段中访问变量, 则会提示变量未定义错误.

在 Python 中当引用一个变量时, 会使用 `LEGB` 规则的按顺序查找一个变量, 其中各个字母代表的含义是: 

- `Local`: 定义在一个函数中的变量
- `Enclosing`: 外部嵌套函数中定义的变量, 以及传递给函数的参数
- `Global`: 全局变量
- `Built-in`: Python 内置函数

## `global` 关键字

当我们在一个函数内想要明确访问一个全局变量时, 可以使用 `global` 声明该变量, 明确指定它是一个 全局变量

## 内置函数 `locals()` 和 `globals()`
Python 提供了两个内置函数 `locals()` 和 `globals()`, 可以让我们分别获取当前的 局部变量 和 全局变量.

    @@@ python
    x = 'global x'

    def test():
        y = 'local y'
        print(locals())
        print(globals()['x'])

    test()