# 定义
    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 使用 def 关键字, 并且无需指定函数的返回类型
    # 注意 冒号 和 缩进
    def test():
        # 可以使用 pass 表示这个函数什么都不做
        pass
        # 这里我们输出一个字符串
        print('hello')

    # 当定义好函数后, 就可以使用函数名后跟一个括号的方式调用这个函数了
    test()

还可以使用 `'''test function'''` 为函数添加文档. `test.__doc__` 获取帮助文档信息.

# 函数返回值
虽然定义参数时没有指定函数的返回值类型, 但是 Python 中所有的函数都有且只有一个返回值

    @@@ python
    # 我们可以将函数的返回值赋值给一个变量
    result = test()
    # 默认是 None
    # None 相当于其他语言中的 null, 表示什么都没有
    print(result)

可以使用 `return` 关键字来明确指定一个返回值, return 后可以跟着一个表达式, 当函数执行到 return 语句后, 会立即终止函数的执行, 并把这个表达式的结果作为函数的返回值返回给函数的调用者.

    @@@ python
    return True

    # 函数只能返回一个值
    # 但是值的类型是任意的
    # 可以是元组, 列表, 字典等
    return 1, 2, 3
    # 实际上这样就相当于我们返回了多个值

    # 将返回结果赋值给多个变量
    a, b, c = resutl()

# 带参数的函数

    @@@ python
    # 在定义函数时还可以指定接收的参数
    # 这样在调用函数时, 就可以向它传递自定义参数了
    def cal_sum(a, b, c):
        return a + b + c
    # 注意, 传递给函数的参数个数一定要与函数定义的个数一样,
    # 否则会抛出 TypeError 异常
    cal_sum(1, 2, 3)

    # 通过这种方式传递的参数是按照位置传递的
    def cal_sum(a, b, c):
        print(a)
        print(b)
        print(c)
        return a + b + c
    # 在调用函数时, 还可以直接指定参数名
    cal_sum(c=1, a=2, b=5)

# 默认值参数

    @@@ python
    # 在定义函数的时候, 还可以为参数提供默认值.
    def cal_sum(a, b, c=5):
    # 这样, 我们就可以在调用函数的地方忽略这些有默认值的参数
    print(cal_sum(1, 2))

    # 但是, 如果定义函数时提供了有默认值的参数
    # 带默认值的参数一定要放到没有默认值的参数的后面. 否则会提示语法错误
    # def cal_sum(a=5, b, c) 将会提示错

# 可变类型作为参数

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 两个参数: 一个整数和一个列表
    # 判断给定的参数 X 是否是偶数
    # 如果是偶数, 就把x追加到第二个参数指定的列表中
    # 并且在定义函数时, 第二个参数指定了一个空列表作为它的默认值.
    def append_if_event(x, lst=[]):
        #  print(id(lst))
        if x % 2 == 0:
            lst.append(x)
        return lst

    # 传递2个参数
    #  print(append_if_event(2, [100, 200]))
    # 也可以忽略第二个参数, 使用默认的空列表
    print(append_if_event(2))
    # 把 2 修改成 3, 结果也正常

同时调用多次

    @@@ python
    print(append_if_event(2))
    print(append_if_event(3))
    print(append_if_event(4))

    # 在指定一个list作为参数, 而不使用默认值
    print(append_if_event(6, []))

    # 前三次使用默认值的方式调用函数时, 他们共用了一个 lst 列表变量.
    # 第四次指定了一个默认的 lst 变量, 表现正常

    # 从结果可以看出, 前3次调用, 使用了同一个列表
    # 可以通过打印出列表的 id 查看一下
    print(id(lst))

    # 只有最后一次的调用, 使用了一个新的列表

    # 这是因为
    # Python 中参数的默认值是在函数编译的时候就已经确定好了的,
    # 而并不是在每次调用的时候重新创建的,
    # 所以每次调用函数的时候指向的都是同一个在编译时定义好了的对象.
    # 当在函数体内修改这个可变类型参数的默认值时, 每次修改的都是同一个对象.

    # 但是如果默认参数是一个不可变类型就不会发生这种现象
    # 这是因为不可变类型在每次修改后都会重新生成一个新的对象,
    # 在讲解整数的时候我们就已经讲过这个了.
    # 所以不可变类型作为参数的默认值不会有任何问题.

## 解决

    @@@ python
    # 不要将可变参数作为默认值
    # 而是在函数内每次都创建一个新的列表
    def append_if_event(x, lst=None):
        if lst is None:
            lst = []
        if x % 2 == 0:
            lst.append(x)
        return lst

# 定义参数可变的函数
前面将的函数, 接收的参数全是固定的, Python 还支持定义参数不固定的函数, 参数不固定只函数可以接收任意个数的参数.

在前面讲解列表和字典的时候我们已经见过了, 可以使用一个 `*` 号来解压多个值到一个变量中, python 中的函数参数也可以使用类似的方式

    @@@ python
    # 在参数前面使用一个星号
    # 所有的参数将全部保存到这个参数中
    def test(*args):
        for i in args:
            print(i)

    test('a', 'b', 'c')

## 带其它参数

    @@@ python
    # 参数列表中还可以指定一个或多个必要参数
    def test(a, *args):
        print('a is {}'.format(a))
        for i in args:
            print(i)

    # a 将传递给 a 参数
    # b和c将传递给 args 参数
    test('a', 'b', 'c')
    # 注意 a 和 *args 的顺序

## 字典参数
前面讲过了, 调用一个函数时, 我们还可以指定参数的名字. Python 同样可以接受任意个指定了名字的参数

    @@@ python
    # 通过使用两个星号来存储命名的参数.
    def test(a, *args, **kvargs):
        print('a is {}'.format(a))
        for i in args:
            print(i)
        for key, val in kvargs.items():
            print("{} -> {}".format(key, val))

    test('a', 'b', 'c', val1='val1', val2='val2')

## 将参数保存到元组和字典中

    @@@ python
    # 我们还可以直接传递一个元组和字典作为参数给函数
    args = ('b', 'c')
    kvargs = {'val1': 'val1', 'val2': 'val2'}
    # 传递的时候同样需要使用*和**解压元组的字典
    test('a', *args, **kvargs)