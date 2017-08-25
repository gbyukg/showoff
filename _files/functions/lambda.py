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

######################### map() 函数 ###############
# Python 中有个内置函数 map(), 它接收2个参数,
# 第一个参数是一个函数变量的引用
# 第二个参数是一个可迭代对象, 元组, 列表, 字符串等
# 该函数的作用是将可迭代对象中的每个元素作为参数传递个第一个参数指定的函数
# 当所有元素都迭代完后, 返回一个列表
def a(val):
    return val * 2
new_val = map(a, (1, 2, 3, 4, 5))
print(new_val)

# 这里函数 a 只是简单的将参数*2然后返回
# 因此我们可以使用匿名函数来代替
new_val = map(lambda val: val * 2, [1, 2, 3, 4, 5])
new_val = map(lambda val: val * 2, 'str')
print(new_val)
