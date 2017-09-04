# 函数

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    def cal_sum(a, b, c):
        return a + b + c

    # 一旦定义了一个函数, 我们就可以使用 函数名+括号的形式调用这个函数了.
    # 注意, 传递给函数的参数个数一定要与函数定义的个数一样,
    # 否则会抛出 TypeError 异常
    print(cal_sum(1, 2, 3))
    # 这种情况下, 参数的传递是靠位置来确定的.
    # 所以这个传递给这个函数的参数的值分别是:
    # a = 1, b = 2, c = 3

    # 在定义函数的时候, 还可以为参数提供默认值.
    # 这样, 我们就可以在调用函数的地方忽略这些有默认值的参数
    #  def cal_sum(a, b, c=5):
    #  print(cal_sum(1, 2))
    # 但是, 如果定义函数时提供了有默认值的参数,
    # 带默认值的参数一定要放到没有默认值的参数的后面.
    # 否则会提示语法错误
    # def cal_sum(a=5, b, c) 将会提示错

    ###################### 小心使用可变类型的对象作为参数的默认值 #################
    # 我们想实现一个函数, 它可以接受 2 个参数, 一个整数值和一个列表
    # 如果传递给函数的整数值是一个偶数, 则把这个整数追加到第二个参数指定的列表中
    # 如果没有传递列表, 则创建一个空列表.
    # 最后返回这个列表
    def append_if_event(x, lst=None):
        '''append_if_even help message'''
        if lst is None:
            lst = []
        if x % 2 == 0:
            lst.append(x)
        return lst
    print(append_if_event(2))
    print(append_if_event(3))
    print(append_if_event(4))
    print(append_if_event(6, []))
    # 前三次使用默认值的方式调用函数时, 他们共用了一个 lst 列表变量.
    # 第四次指定了一个默认的 lst 变量, 表现正常

    # 当我们第一次调用这个函数的时候, 没有给该函数传递 lst 变量,
    # 函数将创建一个空列表,
    #      print('func', lst)
    # 因此它自己创建了一个空 lst 列表, 而这个 lst 是作为一个全局变量存在的.



    # 这个函数既然
    #  print(cal_sum(c=5, b=1, a=3))

    print(append_if_event.__doc__)
    print(dir(append_if_event))

# 定义参数可变的函数
在前面讲解列表和字典的时候我们已经见过了, 可以使用一个 `*` 号来解压多个值到一个变量中, python 中的函数参数也可以使用类似的方式

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 全局变量
    a = 1
    #  id(a)
    l = [0, 1]

    def set_a():
        # 与所有编程语言一样, 如果定义了本地变量, 则会调用本地的变量
        # 全局变量没有影响
        #  a = 2
        # 但是我们应该如何修改全局变量呢?
        # 直接给 a 赋值导致定义了一个函数体内的局部变量
        # 可以使用 global 关键字明确指定这是一个全局变量
        #  global a
        #  id(a)
        #  a = 3

        # a 是一个数值类型, 我们已经讲过, 在 Python 中, 数值类型属于不可变类型
        # 但是当我们修改一个可变类型中的元素时, 比如列表, 字典等, 我们却可以直接修改其中的元素
        #  l[0] = 'x'
        # 这是因为当我们修改一个不可变类型时,
        # Python 会重新生成一个新的对象,并将这个新对象重新赋值给变量
        # 而修改一个可变类型变量时, python 不会重新为这个变量赋值一个新的对象
        # 虽然可变类型中的元素变量, 但是变量指向的对象没有变化
        print('inside: {}'.format(a))
        print('inside: {}'.format(l))

    set_a()
    print('outside: {}'.format(a))
    print('outside: {}'.format(l))