# 列表赋值引用

    @@@ python
    # 创建列表
    # 跟元组类似, 只是使用中括号来表示
    [1, 2, 3, 'four']

    list()
    # 接收一个参数, 这个参数必须是一个序列类型的
    # 将指定的序列类型转换成列表
    list('abc')
    list([1, 2, 3])

    # 访问元素, 从 0 开始计算
    L = [-17.5, "kilo", 49, "V", ["ram", 5, "echo"], 7]
    L[0]
    L[-2][1]

    # 修改元素
    L[2] = 50
    # 同时修改多个值
    # 值必须是一个序列
    L[2:4] = [1, 2, 3]
    L[2:4] = 1, 2, 3 # 元组
    # 删除
    L[2:6] = []
    # 通过切片插入单个值数据
    L[:0] = [0] # 在第一个元素位置前插入值
    L[-1:] = 'latest' # 追加值
    L[2:2] = [49] # 在指定位置处插入值

    # 获取长度
    len(l)

    # 相加
    [1, 2] + [3]
    # 乘法, 表示重复多少次
    [1] * 5
    # 跟元组不同,
    # 在列表中, 如果只有一个元素, 最后元素的逗号是可以不写的

# 列表方法
    @@@ python
    # 获取帮助文档
    help(list)

    l = [1, 2]
    # 还可以使用 append 向末尾追加元素
    # 等同于 l[-1:] = [3]
    l.append(3)

    # 接收一个序列类型作为参数
    # 将序列中的元素全部追击到的 l 中
    l.extend((4, 5, 6))
    l.extend('abc')

    # 在指定的元素 前 追加元素
    l.insert(0, 0)

    # 搜索第一次出现的索引位置
    l.index('a')

    # 查找元素 a 出现的次数
    l.count('a')

    # 移除最后一个元素, 并返回它的值
    l.pop()
    # 删除指定的元素
    l.pop(7)

    # 删除第一个找到的元素并删除
    # 抛出 ValueError 如果没有找到
    l.remove('a')

    # 清空, 等同于 l[:] = []
    l.clear()

# 变量引用
    @@@ python
    # 看一个例子
    l1 = [1, 2, 3]
    l2 = l1
    l1[0] = 'a'

    查看 l1 和 l2
    l1
    l2

    # 解决方案
    # 使用 copy
    l2 = l1.copy()
    # 或
    l2 = l1[:]

## 列表中的 `+` 和 `+=`

    @@@ python
    a = [1, 2, 3]
    b = a
    # 1: 使用 +
    a = a + [4, 5]
    # 2: 使用 +=
    id(a)
    id(b)

# 迭代
提前介绍一下 Python 循环中的 for 循环: 固定格式

    @@@ python
    for i in 'abc':
        print(i)

循环时同时获取索引

    @@@ python
    l = [1, 2, 3, 4]
    for i in range(len(l)):
        print('{} -> {}'.format(i, l[i]))

# enumerate

    @@@ python
    l = [1, 2, 3, 4]
    for idx, item in enumerate(l):
        print('{} -> {}'.format(idx, item))

迭代同时删除元素

    @@@ python
    list = [1, 2, 3, 4]
    for idx, item in enumerate(list):
        list.remove(item)

    list # [2, 4]
    # 删除第一个元素 1 时, list 结果为 [2, 3, 4]
    # 删除第二个元素, 此时第二个元素为 3

# range()
    @@@ python
    for i in range(5):
        print(i)

# 列表推导式

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 当我们需要创建包含大量元素, 或是需要动态生成列表时, 一般的选择是使用 for 循环语句
    # 使用 for 循环创建列表
    temp = []
    for item in range(0, 100):
        temp.append(item)

    print(temp)

    # 但是使用列表推导式, 只需要一行即可. 注意是中括号 []
    temp2 = [item for item in range(0, 100)]
    print(temp2)

    # 还可以使用条件表达式
    temp3 = [item for item in range(0, 100) if item % 2 == 0]
    print(temp3)

9*9 乘法表

    @@@ python
    for i in range(1, 10):
        for j in range(1, i+1):
            print('{} '.format(i * j), end='')
        print()

    # 需要两个循环
    [i * j for i in range(1, 10) for j in range(1, i + 1)]
