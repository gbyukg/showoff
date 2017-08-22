#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 全局变量
a = 1
l = [0, 1]

def set_a():
    # 与所有编程语言一样, 如果定义了本地变量, 则会调用本地的变量
    # 全局变量没有影响
    #  a = 2
    # 但是我们应该当如何修改全局变量呢?
    # 直接给 a 赋值导致定义了一个函数体内的局部变量
    # 可以使用 global 关键字明确指定这是一个全局变量
    #  global a
    #  a = 3

    # a 是一个数值类型, 我们已经讲过, 在 Python 中, 数值类型属于不可变类型
    # 但是对于可变类型, 比如列表, 字典等, 我们却可以直接修改其中的元素
    #  l[0] = 'x'
    # 这是因为当我们修改一个不可变类型时,
    # Python 会重新生成一个新的对象,并将这个新对象重新赋值给变量
    # 而修改一个可变类型变量时, python 不会重新为这个变量赋值一个新的对象
    print('inside: {}'.format(a))
    print('inside: {}'.format(l))

set_a()
print('outside: {}'.format(a))
print('outside: {}'.format(l))
