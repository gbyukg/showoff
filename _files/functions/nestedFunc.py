#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在将闭包之前, 我们先要回顾一下, 在前面的章节中, 我们提到过
# 在python 中, 一切皆对象, 包括函数
# 既然函数也是一个对象, 我们就可以将函数赋给一个变量
def func(val):
    print(val)
# 将函数赋给一个变量
func_var = func
# 如果使用 id 打印出他们的 ID, 会发现他们实际上指向的是同一个对象
print(id(func))
print(id(func_var))
# 通过在变量后面加上()来调用函数
# 与正常调用函数的方式一样
func('taq')

# 甚至将一个函数作为参数, 传递给另一个函数
def func_a(func):
    # 可以使用内置变量 __name__ 获取函数的名字
    print(func.__name__)
    func()
def func_b():
    print('From funciton func_b')
func_a(func_b)

def func_outside():
    outside_a = 1
    outside_b = 2
    def func_inside():
        # python 3 中的 nonlocal 关键字
        # 当我们想要尝试访问一个全局变量时, 可以使用 global 关键字来明确访问一个全局变量
        # 但是当我们在闭包函数内想要明确访问外层函数呢
        # 在 Python2 中, 我们只能通过定义一个全局变量, 分明在外部函数和内部函数内明确使用 global 声明
        # 在 Python3 中, 新增加了一个关键字 nonlocal, 用来访问外部函数中的变量
        nonlocal outside_b
        inside_b = 2
        print('inside a : {}'.format(outside_a))
        print('inside b id: {}'.format(id(outside_b)))
        print('inside b : {}'.format(inside_b))
    print('outside a : {}'.format(outside_a))
    print('outside b id: {}'.format(id(outside_b)))
    # 不能访问内部函数内的变量
    #  print('outside a : {}'.format(b))
    # 返回内部函数
    return func_inside

# 通过调用外部函数, 返回内部函数并赋值给 inside 变量
inside = func_outside()
# 调用内部函数
# 闭包的关在之处在于, 即使退出了外部函数 func_outside 的调用
# 仍然可以访问到该函数内的变量 a
inside()
