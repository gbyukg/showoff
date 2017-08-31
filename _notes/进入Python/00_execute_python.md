# 执行 Python
    @@@ bash
    python

    >>> print("Hi, Python")
    >>> exit() # CTRL-D CTRL-C: SIGINT

---

想要执行一个 Python 代码, 可以有两种方式, 一种是通过使用Python shell, 一种交互模式的 Python 解释器, 被称作 iPython, 在里面我们可以直接运行 Python 代码.  
直接执行 python 命令, 不使用任何参数, 就打开了一个交互式的 python 解释器, 输入 `print('hi Python')` 执行 Python 代码. 要想退出 iPython, 可以调用 `exit()`['ɛɡzɪt] 函数, 或是直接使用 `CTRL-D` 命令.  
`CTRL-D` 代表的是文件结束符(end of file) `EOF`, 它跟 `CTRL-C` 并不一样, `CTRL-C` 是一个信号.

另一种方式就是将 Python 代码保存到一个以 `.py` 结尾的文件中, 通过 python 命令来运行这个脚本. 我们应该都知道, 在 Linux 下, 文件的后缀与文件的类型没有任何关系, 我们可以使用任何名字作为后缀, 但是为了便于阅读和维护, 一般都会选择 `.py` 作为 Python 代码的后缀.

http://blog.csdn.net/coder80/article/details/38510991

http://img.blog.csdn.net/20160630234148703

2 和 3 的不同: http://python3porting.com/differences.html, https://docs.python.org/3.1/whatsnew/3.0.html

[web 终端](https://www.tutorialspoint.com/codingground.htm)

[iterable](http://www.pythonabc.com/iterable-and-iterator/)
