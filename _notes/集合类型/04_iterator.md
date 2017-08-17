# 可迭代对象

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 可迭代对象
    # 只要包含 __iter__() 或 __getitem__() 中的任意一个方法,
    # 这个对象就是可迭代对象.
    # 我们就可以使用 for 循环语句来一次循环获取这个对象中的每一个元素
    # for 的原理就是: 首先判断这个对象是否是迭代对象

    # 首先看一下 __getitem__() 函数
    # 这个函数需要返回对象中的一个元素
    class IterableObj(object):
        def __init__(self):
            self.count = 0
            # 我们还可以使用序列类型
            #  self.lst = [1, 2, 3, 4, 5]

        # 该函数需要一个整数参数
        def __getitem__(self, i):
            if self.count < 5:
                self.count += 1
                return i
            else:
                self.count = 0
                # 当循环结束后, 我们可以通过抛出一个异常来通知我们循环已经达到极限
                # 这里我们选择使用 StopIteration 异常.
                # 因为这个异常能够被 for 循环自动处理.
                # 如果是自己编写的代码, 而不是使用 for 语句
                # 需要我们对这个异常作出处理, 异常会在后面的章节中讲解到
                raise StopIteration()

        #  def __getitem__(self, i):
            #  return self.lst[i]

    # 创建一个这个类的实例
    a = IterableObj()
    for i in a:
        print(i)


    # 如果定义了 __getiter__ 方法,
    # 我们不仅可以使用 for 循环来获取元素
    # 还可以使用索引的方式来获取
    b = IterableObj()
    print(b[0])
    print(b[1])
    print(b[2])
    print(b[3])
    print(b[4])

# 迭代器

    @@@ python
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



# 迭代通用方法

    @@@ python
    ######################## + ########################
    # 注意这里是序列类型, 序列类型包括字符串, 元组 和 列表
    print([1, 2] + [3, 4])

    ######################## in ########################
    print(1 in [1, 2, 3])
    # 使用 not in
    print(1 not in [1, 2, 3])
    print('x' in ('a', 'b', 'c'))


    ######################## all ########################
    print('all')
    print(all((1, 2, 3)))
    print(all((0, 2, 3)))
    print(any((0, 2, 3)))

    ######################## max() ########################
    lst = [-2, -1, 0, 1]
    print('======= max =======')
    print(max(lst))

    def cus_max(v):
        abs(v)
    print(max(lst, key=cus_max))

    ######################## range() ########################
    print("========== range ==========")
    # range 可以接受 1 至 3 个参数
    # 当我们只传递一个参数5时, 生成的结果 0~5
    #  for i in range(5):

    # 当传递2个参数时(3, 5), 则范围 3~4
    #  for i in range(3, 5):

    # 当传递3个参数时, 最后一个参数则是步长
    for i in range(1, 10, 2):
        print(i)

    ######################## reversed() ########################
    print("========== reversed() ==========")
    for i in reversed((1, 2, 3)):
        print(i)

    ######################## enumerate() ########################
    lst = ['left', 'right', 'up', 'down']
    # 当我们想要输出每个元素的时候, 可以用 for 循环
    for i in lst:
        print(i)

    # 但是当我们想要同时输出每个元素的索引呢?
    for i in range(len(lst)):
        print(i, lst[i])

    # 使用 enumerate(), 也可以指定索引起始位置
    for i, v in enumerate(lst, 2):
        print(i, v)


    ######################## zip() ########################
    a1 = (1, 2, 3)
    a2 = (4, 5, 6)
    a3 = ('a', 'b', 'c')
    # 增加2个元素的元组, 结果每个元组中都包含2个元素
    a4 = ('x', 'y')
    a = zip(a1, a2, a3, a4)
    print(a)

    # 生成字典
    d = {}
    b1 = ('a', 'b', 'c')
    b2 = (1, 2, 3)
    for key, val in zip(b1, b2):
        d[key] = val
    print(d)
