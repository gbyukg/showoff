#!/usr/bin/env python
# -*- coding: utf-8 -*-

def generator():
    print('a')
    yield 1
    yield 2
    yield 3
    yield 4

a = generator()

for i in a:
    print(i)
