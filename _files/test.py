#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    __slots__ = ('name', 'age', 'tag')

a = A()
a.name = 'test'
a.age = 24
a.tag = 'IOS'
