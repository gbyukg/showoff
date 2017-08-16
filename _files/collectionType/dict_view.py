#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'user': 'Smith', 'address': ['USA', 'Littleton'], 'Level': 10, 'size': 15}

keys = d.keys()
values = d.values()
items = d.items()

# python2
view_keys = d.viewkeys()

d.pop('user')
print(keys)
print(view_keys)
print(values)
print(items)
print(d)


d = {}.fromkeys('ABCD', 3)
#  print(d)
s = set('ACX')
#  x = d.viewkeys() & s
x = d.keys() & s
print(x)

