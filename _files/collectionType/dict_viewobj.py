#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'user': 'Smith', 'address': ['USA', 'Littleton'], 'Level': 10, 'size': 15}

keys = d.keys()
values = d.values()
items = d.items()

# 删除其中某个元素
del d['user']

print(d)

# keys he  values 都能够正确反映出变更
print(keys)
print(values)
print(items)
