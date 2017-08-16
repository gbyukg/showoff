#!/usr/bin/env python
# -*- coding: utf-8 -*-

import collections

d = collections.OrderedDict([('z', -4), ('e', 19), ('k', 7)])
print(d)

# 注意, 如果传递给 OrderedDict 的参数是一个无法保证顺序的对象, 比如另一个字典, 则生成出来的字典的顺序是随机的.
# 但是向上面那样传递一个 list, 或是 元组 则不会出现这种情况, 因为他们都是能够保证元素顺序的对象
plain_dict = {'a':1, 'b':2, 'c':3}
d2 = collections.OrderedDict(plain_dict)
print(d2)
# 包括使用 update()
d3 = collections.OrderedDict()
d3.update(plain_dict)
print(d3)
# 因此我们应当避免使用一个元素顺序不保证的对象作为参数传递给 OrderedDict()

# 通过向字典中追加新元素的方式, 将会严格保证键值的顺序
tasks = collections.OrderedDict()
tasks[8031] = 'Backup'
tasks[4027] = 'Scan Email'
tasks[5733] = 'Build System'
print(tasks)
# 输出字典的键, 其顺序一定是按照上面的顺序下来的.
print(tasks.keys())

# 如果我们想要将一个元素移动到字典的结尾, 必须先要删除这个元素, 在将这个元素追加进字典中才能实现
tasks[4027] = tasks.pop(4027)
print(tasks)
