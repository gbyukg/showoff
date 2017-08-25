#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(): pass

class B(object): pass

class NewException(Exception, object): pass

#  print(A.__class__)
print(B.__class__)
print(type(A), type(B))

#  raise NewException('ttt')
age = 35
print(age.__class__)
b = B()
print(type(b))
print(b.__class__)
