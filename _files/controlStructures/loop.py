#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = 5

while num:
    # 当遇到 break 时, else 语句将不会被执行
    if num == 3:
        break
    print(num)
    num -= 1
else:
    print('end loop')

# elese 为可选语句
# 如果 while 语句正常退出, else 语句将总是被执行
# 但是如果在 while 语句中有 break, return,或是有异常抛出
# else 语句将不会被执行

# for
# for in 循环中的 else 语句与 whil 中的一样
for i in range(0, 5):
    print(i)
else:
    print('end for')
