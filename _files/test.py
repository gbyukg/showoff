#!/usr/bin/env python
# -*- coding: utf-8 -*-

def test(a, *args, **kvargs):
    print('a is {}'.format(a))
    for i in args:
        print(i)
    for key, val in kvargs.items():
        print("{} -> {}".format(key, val))

args = ('b', 'c')
kvargs = {'val1': 'val1', 'val2': 'val2'}
test('a', *args, **kvargs)
