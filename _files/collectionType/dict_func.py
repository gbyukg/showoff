#!/usr/bin/env python
# -*- coding: utf-8 -*-

d = {'user': 'Smith', 'address': ['USA', 'Littleton'], 'Level': 10, 'size': 15}

################ clear() ################
#  d.clear()
#  print(d)


################ copy() ################
#  d2 = d
#  d2['user'] = 'Bob'
#  print('d', d)
#  print('d2', d2)
d2 = d.copy()
d2['user'] = 'Bob'
print('d', d)
print('d2', d2)

################ get() ################
print(d.get('user'))
# 返回 None ,如果 xxx 不存在
print(d.get('xxx'))
# 返回给定的值 `XXX` 如果 key `xxx` 不存在
print(d.get('xxx', 'XXX'))

################ items() ################
# 将字典中所有的元素以 (key, value) 的形式保存到 字典视图 中, 并返回这个视图, 下面会讲解到什么是 字典视图

# 通过 for in 语句循环
#  for item in d.items():
    #  print('{} : {}'.format(item[0], item[1]))

# 还记得解压么, 上面方法还可以通过另一种方式实现
for item, val in d.items():
    print('{} : {}'.format(item, val))

# `items()`, `keys()` 与 `values()` 函数返回的结构都是从源字典中的拷贝出来的, 如果被操作的字典包含大量元素, 这将会导致内存的大量浪费, 相应的, 我们可以使用 `iteritems()`, `iterkeys()` 和 `itervalues()`, 这些函数返回一个可迭代对象, 可以对这些可迭代对象进行 `for` 循环获取其中的内容, 在循环可迭代对象时, 之后当前被处理的元素才会被保存到内存当中, 当处理完成以后, 就会从内存当中删除.
# 在 Python3 中, 对 `items()`, `keys()` 与 `values()` 这3个函数进行了重新处理, 他们全部返回 字典视图(directory view) 对象, 并且移除了 `iteritems()`, `iterkeys()` 和 `itervalues()` 函数.

################ keys() ################
# 返回一个字典视图, 包含了字典中所有的键
print(d.keys())
################ values() ################
# 返回一个字典视图, 包含了字典中所有的键
print(d.values())

################ pop() ################
# 返回字典中键k对应的值, 并将该键从字典中移除, 如果字典中不存在键 k, 则抛出 KeyError 异常
print(d.pop('user'))
print(d)
#d.pop('xxx')
print(d.pop('xxx', 'yyy'))

################ popitem() ################
# 从字典中删除随意一个键值对, 并返回被删除的键值对, 当对一个空的字典进行 popitem() 操作时, 将会抛出 `KeyError` 异常
print(d.popitem())
print(d)
d.popitem()
print(d)
d.popitem()
print(d)

################ setdefault() ################
# 如果字典中存在键 `k`, 则返回它在字典中对应的值, 如果不存在该键, 则向该字典中插入值为 `v` 的键 `k`, 并返回值 `v`
print('setdefault')
print(d.setdefault('name', 'Smith'))
print(d)
print(d.setdefault('name', 'XXX'))
print(d)


################ update() ################
# 更新字典, 该方法接收三种形式的参数: 一个字典; 或是一个可迭代对象, 每次迭代返回的都是一个包含两个元素的对象分别作为 key 和 value; 或是向该函数传递关键字参数
print('update')
print(d)
# 传递另一个字典
d.update({'size': 18, 'age': 36})
print(d)
# 传递一个元组
t = (('first', 'Smith'), ('last', 'keven'), ('id', 1234567))
d.update(t)
print(d)
d.update(company='IBM', department='BTIT')
print(d)
