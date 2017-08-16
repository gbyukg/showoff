#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 当我们访问一个字典中不存在的 键 时, 会抛出 KeyError 异常.
# 这是正确的行为, 因为我们需要知道这个键不存在某个字典中

# 但有些时候我们希望当键不存在时, 可以自动将这个键添加进去, 虽然上面我们提及了字典的 `setdefault()` 方法可以帮助我们达到这一目的.
# 但使用 default dictionaies 将会更加方便.

import collections

# defaultdict 接收一个工厂函数. 一个工厂函数就是当我们调用一个函数时, 这个函数能够返回给我们一个特定类型的对象.
# 所有 Python 内置的数据类型都可以被当做一个工厂函数来使用
# 比如前面我们讲解到的 `str()`, 能够返回一个字符串, `int()`, `float()`, `tuple()`, `set()`, `dict()` 都是工厂函数.
words = collections.defaultdict(int)
print(words['a'])
print(words)

sentences = collections.defaultdict(tuple)
print(sentences['word'])
print(sentences)

# 自定义默认值
cus_type = collections.defaultdict(lambda: [0, 0, 0])
print(cus_type['a'])
print(cus_type)
