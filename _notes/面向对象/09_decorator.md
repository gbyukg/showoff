# 装饰器
1. 定义一个函数, 返回一个字符串

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    def get_python():
        return 'Python'

    # 1:
    #  print(get_python())

    # 2: 在所有的调用处都需要修改代码, 添加 h1 标签
    #  print("<h1>{}</h1>".format(get_python()))

    # 3: get_title 接收参数的方式 <h1>, 但是这样我们不得不修改 get_python 函数方法
    # 如果有很多类似这种的方法, 需要全部修改
    # 如果 get_python 很复杂, 里面有各种各样的判断, 返回不同的结果
    # 所有这些结果全部要修改成使用 <h1> 标签包围的效果

    # 4: 更好的解决方法
    # 首先我们知道 Python 中一切皆对象
    # 包括函数
    # 所以我们可以将一个函数赋值给一个变量
    get_python_var = get_python
    #  print(type(get_python_var))
    # 还可以输出它的 id
    #  print(id(get_python_var))
    # 通过这个变量调用函数
    #  print(get_python_var())

    # 我们当然也可以将这个变量作为参数传递给另一个函数
    def set_h1(func):
        return '<h1>{}</h1>'.format(func())
    # 调用
    #  print(set_h1(get_python_var))

