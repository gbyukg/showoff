#!/usr/bin/env python
# -*- coding: utf-8 -*-

def logger(level):
    def wrap(func):
        def log_func(*args):
            print("{}: Running {} with arguments {}".format(level, func.__name__, args))
            return func(*args)
        return log_func
    return wrap

@logger('Info')
def add(x, y):
    return x + y

@logger('Warning')
def sub(x, y):
    return x - y

#  add_logger = logger(add)
#  add_logger(3, 4)

# 等价于
#  unnamed_func = logger('info')
#  add_logger = unnamed_func(add)
#  add_logger(3, 4)

add(3, 4)
sub(5, 2)
