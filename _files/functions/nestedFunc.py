#!/usr/bin/env python
# -*- coding: utf-8 -*-

from functools import wraps

#  def logger(func):
    #  #  @wraps(func)
    #  def log_func(*args):
        #  print("Running {} with arguments {}".format(func.__name__, args))
        #  return func(*args)
    #  return log_func

def logger(level):
    def wrapper(func):
        def log_func(*args):
            print("{} Running {} with arguments {}".format(level, func.__name__, args))
            return func(*args)
        return log_func
    return wrapper

#  @logger('Info')
def add(x, y):
    return x + y

#  @logger('Warning')
def sub(x, y):
    return x - y

unnamed_func = logger('Info')
add = unnamed_func(add)
add(3, 4)
#  add = logger(add)
#  add(3, 4)
