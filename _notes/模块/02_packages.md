# package

Python 中包的定义很简单, 就是一个目录, 首先这个目录下必须存在一个 `__init__.py` 的文件, 这个文件中的内容可以为空, 剩下就是一些 Python 的模块文件了, 在一个 包 中还可以包含多个子包.

包的作用就是把一系列相关功能放到一起, 这样维护是使用起来就比较方便了.

我这准备好了一个 `arithmetic` 目录, 结构很简单, 包含了一个 `__init__.py` 文件和一些 python 文件, 这些 python 中的代码非常简单, 都是只包含了一个简单函数的文件. 这就是一个包了, 可以看一下 `__init__.py`, 现在这个文件是一个空文件.

我在创建一个 `packages.py` 的文件用来使用这个包

    @@@ python
    # 引用一个包跟引用一个模块语法完全一样
    # 使用 import 语句
    import arithmetic

    # 当引入这个包后
    # 我们可以用 dir() 内置函数观察一下当前文件中有哪些东西
    print(dir())
    # 从输出中可以看到, 多了一个 `arithmetic`, 就是我们上面刚刚引入的这个包

    # 我们可以使用另一个内置函数 help() 查看这个包中有哪些属性
    print(help('arithmetic'))
    # 查看包中的某个模块信息
    print(help('arithmetic.add'))
    # 可以看到有一个 add 方法

    # 调用这个模块中的 add 方法
    # 这里一定要注意, 第一个add 是包下的模块,
    # 第二个 add 才是模块下的方法
    result = arithmetic.add.add(1, 2)
    # 打印出结果
    print(result)
    # 使用除法
    # 注意这里模块名和方法名不同
    result = arithmetic.divide.division(5, 2)

我们也可以导入包中的一个或多个模块

    @@@ python
    import arithmetic.add
    # 这样我们就只能使用 add 模块中的方法了.
