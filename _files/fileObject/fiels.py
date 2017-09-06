#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# open 至少接受一个参数: 要打开的文件
# 文件默认是以只读的方式打开的
# 也可以指定文件的打开方式
f = open('test.txt', 'r')
with open('test.txt', 'r') as f:
    f_contents = f.read(100)
    print(f_contents)
    print(f.tell())
