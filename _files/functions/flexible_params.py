#!/usr/bin/env python
# -*- coding: utf-8 -*-

def product(a, b=1, *args, **kargs):
    print('a: {}'.format(a))
    print('b: {}'.format(b))
    # 除去前两个参数 a 和 b
    # 所有剩余的未命名的参数全部存储到 args 变量中
    # 而所有带参数名的参数将全部传递给 kargs 变量中
    for arg in args:
        print(arg)
    for key,val in kargs.items():
        print('{}: {}'.format(key, val))

#  product(1, 2, 3, 4, x='5', y='6', z='7')

# 还可以将元组和字典直接作为参数传递给函数
param1 = ('a', 'b', 'c')
param2 = {'m': 'm', 'n': 'n'}
product(1, 2, *param1, **param2)
# 如果没有指定 a, b 两个参数
product(*param1, **param2)
