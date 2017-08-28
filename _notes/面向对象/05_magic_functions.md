# 魔术方法

    @@@ python
    #!/usr/bin/env python
    # encoding: utf-8

    class Employee:
            def __init__(self, first, last, pay):
                self.first = first
                self.last = last
                self.pay = pay
                self.email = '{}.{}@company.com'.format(first, last)

            def fullname(self):
                return '{} {}'.format(self.first, self.last)

    emp_1 = Employee('Test1', 'User1', 5000)
    emp_2 = Employee('Test2', 'User2', 6000)

    # 我们知道, 在 Python 中, 一切皆对象
    # 包括数字和字符串
    # 但是当我们执行
    print(1 + 2)
    # 表示两个数字对象做相加操作
    # Python 能够正确为我们计算出结果

    # 甚至是让2个字符串相加
    print('str1' + 'str2')
    # 执行代码
    # 可以看到两个字符串能够正确拼接到一起
    # 不同的对象对 + 有不同的操作
    # 数字类型对象是做数学运算
    # 字符串类型是做字符串的拼接

    # 在让我们列举一个例子
    # 删除这两个 print 语句
    # 现在我们尝试打印 Employee 实例
    print(emp_1)
    # 发现 Python 可以正确打印出结果
    # 虽然输出的信息对我们的帮助不是很大
    # 但是如果我们能够自定义这些信息, 那是最好不过的了.
    # 那么 Python 是如何实现这些功能的呢?
    # 答案就是魔术方法
    # Python 中提供了大量的 魔术方法
    # 这些方法全是是以 双下划线开头和结尾的.

    # 到现在为止, 其实我们已经接触过Python中的魔术方法了
    # 就是 __init__ 方法
    # 当我们实例化一个类时
    # python 会自动为我们调用 init 方法
    # 这样我们可以将我们的初始化代码放到 init 方法中了.

    # 跟 init 方法类似,
    # Python 还提供了很多其他的魔术方法
    # 当我们对一个对象做一些特殊操作, 或是调用特定方法时
    # 特定的魔术方法就会被调用.

# `__repr__` 和 `__str__`

    @@@ python
    # 先让我们看一下两个最常用的魔术方法
    # `repr` 和 `str`
    # 当我们尝试打印一个对象的时
    # Python 首先会查看对象中是否定义了这两个方法
    # 如果定义了, 则调用这两个方法
    # 如果没有定义这两个魔术方法
    # Python 则采用默认规则来打印出对象信息
    # 如:
    print(emp_1)
    # 或是直接调用 repr() 函数
    print(repr(emp_1))
    # 和 str 函数时
    print(str(emp_1))
    # 这两个魔术方法同样被调用

## `__repr__`

    @@@ python
    # 我们先定义一个 repr 方法
        def __repr__(self):
            # Python 规定
            # 这方方法需要返回一个字符串
            # 所以我们需要一个 return 语句
            # 然后返回一个字符串
            # 注释掉 repr(emp_1) 和 str(emp_1) 这两个方法
            # 运行脚本
            # 在运行之前, 大家看一下当前我们输出实例时的结果
            return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

## `__str__`

    @@@ python
    def __str__(self):
        # 我们希望输出员工的全名和 emai 地址信息
        return '{}, {}'.format(self.fullname(), self.email)
        # 执行代码
        # 发现 print 语句的输出发生了变量
        # 输出结果是我们在 __str__ 中定义的字符串

## `__len__`

    @@@ python
    # 当我们调用 len() 来获取某个对象的长度时
    # __len__() 方法就会被调用
    # 给 Manager 添加该方法
    # 用来表示Manager下有多少开发人员
    def __len__(self):
        return len(self.employees)
    # 这样我们就可以使用 len() 方法来获取manager下员工的数量了
    print(len(mgr_1))

    # 我们在 __len__ 方法内还是使用了 len() 函数来获取列表的长度
    # 如果我们将这个长度作为一个实例属性保存在实例中
    # 每次增加或删改的时候, 都相应的改变这个值
    # 那我们在 __len__ 函数中就可以直接返回这个属性的值
    # 而不用每次在重新计算这个长度了
    # 这样无论这个对象下有多少长度,
    # 每次获取这个长度的时候都是一样的
    # 因为只需要返回这个值就可以了
    # 因此返回这个对象的时间复杂度为 1: O(1)
    # 实际上这也是列表内部获取元素长度的方式
    # 因此我们无需在手动添加这个变量了

## `__getitem__`

    @@@ python
    # 还记得上面讲过的可迭代对象么,
    # 其中一点就是
    # 如果对象中有 `__getitem__` 方法
    # 那么这个对象就叫做可迭代的对象
    # 当我们用 for 语句循环对象时
    # 就是尝试调用这个方法
    # 当我们用索引或者键名访问对象中的某个元素时
    # Python就会为我们自动调用这个方法
    # 这个方法应该返回对象中的某个元素
    # 我们为 Manager 添加这个方法
    # 根据索引位置来返回程序员
    def __getitem__(self, i):
        # 除了 self 之外
        # 还需要一个数值作为参数
        # 来返回指定索引位置的员工
        return self.employees[i]
    # 这样我们就可以对 manger 实例使用索引了
    # 获取员工的全名
    print(mgr_1[0].fullname())
    # 也可以使用 for 循环来获取所有员工信息
    for i in mgr_1:
        print(i.fullname())

## `__next__`

    @@@ python
    def next(self):
        if self.index < len(self):
            item = self.employees[self.index].fullname()
            # 在构造函数中增加一个变量
            # self.index = 0
            # 用来记录 next 中的索引
            self.index += 1
            return item
        # 当没有更多的元素时, 抛出 StopIteration 异常
        # 至于为什么要抛出 StopIteration 异常
        # 一会会在后面说到
        raise StopIteration()

    print(next(mgr_1))
    print(next(mgr_1))
    # 再次使用 next() 方法, 则抛出 StopIteration 异常
    #  print(next(mgr_1))


## `__iter__`

    @@@ python
    # 为 Manger 类增加
    def __iter__(self):
        # print('iter')
        # 该方法必须返回一个迭代器
        # 即一个含有 __next__ 方法的对象
        # 因为我们的 Manager 类中已经包含了 next 方法
        # 所以此处就可以直接 self
        return self
    # 含有 `__iter__`方法的对象可以通过 for 循环来一次获取其中的元素
    for i in mgr_1:
        print(i)
    # 在刚才讲解 next 方法时, 我们提到了
    # 当对象中没有更多的元素可以被 next() 方法调用时
    # 应当抛出 StopIteration 异常
    # 这个异常主要是为 for 提供的
    # 当使用 for 语句迭代一个元素时
    # 如果遇到了 StopIteration 异常
    # 说明没有更多的元素可以获取了
    # 并且 for 语句会自动处理 StopIteration 异常
    # 所以我们的程序不会因为遇到了异常而报错退出

## `__getattr__`

