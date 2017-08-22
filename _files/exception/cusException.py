#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 自定义异常实际上就是一种自定义类型(自定义类), 我们将会在后面讲解类.
# 但是创建一个类实在很简单, 只需使用 class 关键字即可创建一个类
# 其中的 `baseException` 指定自定义异常类的父类, 父类必须是 `Exception` 类, 或是 `Exception` 的某个子类.

# 考虑这样一个例子
# 查找一个表中某个字段是否含有指定的元素

table = (
    (('C1B1A1S', 'C1B1A1S-name'),),
    (('E1C1B1A1S', 'E1C1B1A1S-name'),),
    (('C2B1A1S', 'C2B1A1S-name'),),
    (('type4', 'E2C2B1A1S-name'),),
)

found = False
target = 'C2B1A1S-name'
for row, record in enumerate(table):
    for column, field in enumerate(record):
        for index, item in enumerate(field):
            if item == target:
                found = True
                break
        if found:
            break
    if found:
        break
if found:
    print("found at ({0}, {1}, {2})".format(row, column, index))
else:
    print("not found")

# 使用异常实现
class FoundException(Exception): pass
try:
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    raise FoundException()
except FoundException:
    print("found at ({0}, {1}, {2})".format(row, column, index))
else:
    print("not found")


