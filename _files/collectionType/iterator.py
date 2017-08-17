#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 先让我们看一下迭代器
# 迭代器就是一个包含了 __next__() 方法的对象
# 我们可以使用内置函数 iter() 将一个可迭代的对象转换成一个迭代器返回
# a = [1, 2, 3]
# 通过 help(a) 我们可以看到, 它存在一个 __getitem__ 方法, 说明它是一个可迭代对象
# 通过 iter() 函数来返回一个迭代器
# ai = iter(a)
# 此时在通过 help(ai) 查看, 发现有 next() 方法
# 说明此时 ai 是一个迭代器
# 迭代器可以作为内置函数 nexit() 的参数, 返回迭代器中的一个元素
# next(ai), 当迭代到最后一个元素后, 迭代器会抛出 StopIteration 异常.
# 迭代器也可以被 for 循环使用, for 循环会自动处理 StopIteration 异常
#  for i in (iter(1, ,2, 3)):
    #  print(i)
# 迭代器只能被迭代一次

# ==================================

# 现在我们看一下如何自定义迭代器对象
class IteratorObj(object):
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __getitem__(self, i):
        print('__getitem__')
        return self.data[i]

    def __iter__(self):
        print('__iter__')
        # 该函数必须返回一个迭代器, 包含了 next 方法的对象
        # 所以这里我们直接返回 self
        return self

    def next(self):
        print('next')
        if self.index == 0:
            raise StopIteration()
        self.index -= 1
        return self.data[self.index]

#  a = IteratorObj('spam')
#  print(next(a))
#  print(next(a))
#  print(next(a))
#  print(next(a))
# 此时当我们在使用 next() 尝试打印出下一个元素时
# 就会抛出 StopIteration 异常
# print(next(a))

# 当我们尝试使用 for 来迭代该迭代器时
# 提示 TypeErro 错误, 说这个对象不是一个可迭代的对象.
# 这说明使用 for 时, 它首先会去判断这个对象是不是可迭代对象.
# 现在我们需要将这个对象转换成可迭代对象.
# 刚才我们讲到了 __getitem__ 方法可以让一个对象编程可迭代对象.
# 我们添加 __getitem__ 对象, 再次执行, 看似一切运行正常.
# 添加 print('__getitem__') 和 print('next') 再次执行for循环
# 发现 for 循环只是调用了 __getitem__方法, 然后就返回了,
# 其实从代码中我们也可以看出, 最后的 return 语句直接退出.
# 刚才我们还提及到了另一个方法 __iter__() 这个函数的返回结果必须是一个迭代器, 否则报错
# 添加 __iter__() 方法, 再次执行
# 可以看出, __iter__ 输出一次, 之后的每次循环都会输出 next
# 这是, 我们才真正的创建了一个迭代对象
#
for i in IteratorObj('spam'):
    print(i)

