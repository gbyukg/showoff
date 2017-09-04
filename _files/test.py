#!/usr/bin/env python
# -*- coding: utf-8 -*-

x = 'global x'

def test():
    y = 'local y'
    print(locals())
    print(globals()['x'])
    globals()['name'] = 'zzl'

test()
print(name)

# 访问局部变量, 报错
#  print(y)
