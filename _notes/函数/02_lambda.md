# 匿名函数

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    s = lambda x: "" if x == 1 else "s"

    # 创建一个匿名函数, 并将这个匿名函数赋给变量 s
    # 通过调用 s 可以像调用正常函数那样调用匿名函数
    print(s(1))
    print(s(0))

    # 直接使用在其他函数内
    count = 3
    print("{0} file{1} processed".format(count, s(count)))

# map()

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 当前我们有一个由数字构成的列表
    l = [1, 2, 3]
    # 如果我们想将这个列表中的所有元素做平方操作
    # 然后返回一个新的列表
    # 通常做法是循环这个列表, 获取其中的每个元素一次做平方操作

    new_l = []
    for i in l:
        new_l.append(i ** 2)
    print(new_l)

    # 这样类似的操作平时遇到的几率很大,
    # 对一个可迭代对象中的每个元素做一些特殊处理后返回一个新的对象
    # python 为我们提供了内置函数 map() 就是专门用于类似操作的.
    # map() 函数可以接收两个或多个参数,
    # 第一个参数是一个函数, 剩余参数均为可迭代对象
    # 它的作用就是将可迭代对象中的每个元素以参数的形式传递给第一个参数指定的函数
    # 这个函数需要一个返回值, 返回做完特殊处理后的值
    # 最后整个 map 函数返回一个新的列表对象, 包含了所有被应用到函数上后返回的新值
    # 如:
    def sqr(x):
        return x ** 2

    new_l2 = map(sqr, l)
    print(new_l2)

    # 还可以同时传递多个序列,
    # 当传递多个序列时, 每个序列中的元素会同时一起传递给函数作为参数
    # 这时, 相应的第一个参数指向的函数也需要修改它可接收的参数个数.
    def sqr(x, y, z):
        return (x+y+z) ** 2
    l2 = [4, 5, 6]
    l3 = [7, 8, 9]
    new_l3 = map(sqr, l, l2, l3)
    print(new_l3)

    # 如果传递给map的函数比较简单, 我们就可以使用匿名函数来代替
    new_l4 = map(lambda x: x ** 2, l)
    print(new_l4)

# filter()

    @@@ python
    # filter 函数与 map 函数类似, 接收一个函数和一个序列作为参数
    # 这个函数需要返回一个 bool 值
    # filter 会将序列中的每个元素一次应用到函数中,
    # 当函数返回 True 时, 会将这个序列中的这个元素返回到新的序列中,
    # 如果函数返回 False, 则抛弃这个元素
    l = (1, 2, 3, 4, 5, 6)
    filter_val = filter(lambda x: True if x % 2 == 0 else False, l)
    print(filter_val)
