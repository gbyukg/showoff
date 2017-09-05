# 创建
前面讲的都是通过索引获取元素中的值, 虽然使用命名元组可以为元素定义名字, 但它并不是元组特有的属性, 而且不是很方便

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 返回一个空字典
    d1 = dict()
    print("d1", d1)

    # 传递参数
    d2 = dict(id=1948, name="Washer", size=3)
    # 这里注意字典打印的顺序, 与我们给定的顺序是不同的
    print("d2", d2)

    # 传递另一个字典作为参数
    d3 = dict(d2)
    print("d3", d3)

    # 传递一个可迭代对象, 可以是一个元组, 也可以是一个列表
    # 迭代对象中每个元素又是另一个包含2个元素的可迭代对象, 元素0->key, 元素 1->value
    d5 = dict([['id', 1948], ('name', 'Washer'), ('size', 3)])
    print("d5:", d5)

    # 也可以直接通过 大括号 创建字典
    d = {'a': 1, 'b': 2}
    # 在看一个例子
    d = {"root": 17, 'blue': [75, 'R', 2], 21:'venus', -14:None, 'mars':'rover', (4,11):18, 0:45}
    # 字典中的键可以是任何可哈希(hash)的对象, 可哈希对象简单理解就是其值不可改变的对象, 数字, 字符串, 元组就是可可哈希的对象
    # 可以使用内置函数 `hash()` 判断一个对象是否是可哈希的
    # hash((1, 2, 3))
    # hash((1, 2, [3, 4])) 包含列表, 不可哈希
    # 字典中的键值要保证是唯一的, 否则后面出现的键将会覆盖前面先出现的键

    # 迭代字典中的元素
    for i in d:
        # 每次迭代返回是键
        print(i)
        # 同时获取 键 和 值
        print('{}->{}'.format(i, d[i]))

## zip

    @@@ python
    # 使用 zip
    # zip 是Python的一个内置函数
    # 他接收任意个可迭代对象作为参数
    # 它返回一个迭代器
    z = zip('abc', (1, 2, 3))
    for i in z:
        print(i)

    d4 = dict(zip(('id', 'name', 'size'), (1948, 'Washer', 3)))
    print("d4:", d4)

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

## 访问字典元素

    @@@ python
    # 通过键值获取元素
    d['root']
    d['blue']
    d[-14]
    d[(4,11)]
    # 当访问一个不存在的键时, 会抛出 KeyError 异常
    #  d['x']

    # 新曾元素, 因为字典是非顺序的, 所以新增的元素不一定会被追加到字典的结尾
    d['x'] = 59
    d

    # 可以像之前讲解变量时那样, 使用 del 删除字典中的一个元素
    del d['x']
    d

    # 我们可以使用内置函数 len() 来获取字典的长度
    len(d)

# 字典方法

    @@@ python
    d = {'user': 'Smith', 'address': ['USA', 'Littleton'], 'Level': 10, 'size': 15}

    ################ get() ################
    # 上面提到我们可以通过键名直接获取字典中的元素
    # 还可以使用 字典的 get() 方法获取
    d.get('user')
    # 上面提到了, 当访问一个不存在的键时, 会抛出 KeyError 异常.
    # 但是返回 None ,如果 xxx 不存在
    d['users'] # 报错 KeyError 异常
    d.get('users', 'NULL') # 返回 NULL 字符串

    # 还可以指定第二个参数
    # 返回给定的值 `XXX` 如果 key `xxx` 不存在
    d.get('users', 'users')

    ################ pop() ################
    # 返回字典中键k对应的值, 并将该键从字典中移除
    # 如果字典中不存在键 k, 则抛出 KeyError 异常
    d.pop('user')
    d.pop('user') # 报错
    d.pop('user', 'NULL') # 返回 NULL 字符串

    ################ popitem() ################
    # 从字典中删除随意一个键值对, 并返回被删除的键值对
    d.popitem()
    # 当对一个空的字典进行 popitem() 操作时, 将会抛出 `KeyError` 异常
    d.popitem()

    ################ setdefault() ################
    # 它的作用首先是返回指定键的值
    # 如果不存在该键, 则向该字典中插入值为 `v` 的键 `k`, 并返回值 `v`
    d.setdefault('user', 'Smith')
    d.setdefault('address', ['USA', 'Littleton'])
    d
    # 如果没有指定第二个参数, 则默认插入 None

    ################ update() ################
    # 更新字典, 该方法接收三种形式的参数:
    # 传递另一个字典
    d.update({'size': 18, 'age': 36})
    print(d)

    # 或是一个可迭代对象
    # 每次迭代返回的都是一个包含两个元素的对象分别作为 key 和 value; 或是向该函数传递关键字参数
    # 传递一个元组
    d.update((('first', 'Smith'), ('last', 'Keven')))
    # 也可以将参数保存到一个变量中
    t = (('first', 'Smith'), ('last', 'Keven'), ('id', 1234567))
    d.update(t)

    # 或是通过指定一个参数名字和值的方式
    d.update(company='IBM', department='BTIT')

    ################ clear() ################
    # 清空字典
    d.clear()

    ################ copy() ################
    d1 = {'a':1, 'b':2}
    d2 = d1
    d1['a'] = 0
    d1
    d2

    d2 = d1.copy()
    id(d1)
    id(d2)
    # 或
    d2 = dict(d1)

# 字典视图

    @@@ python
    d = {'a': 1, 'b': 2, 'c': 3}

    d_k = d.keys()
    d_v = d.values()
    d_i = d.items()
    d_k
    d_v
    d_i

    d.setdefault('d', 4)
    d
    d_k
    d_v
    d_i

    # 因为 items 返回的是一个列表
    # 并且每个元素都是一个有 key 和 value 组成的元组
    # 索引我们可以直接循环它来获取 key 和 value
    for item, val in d.items():
        print('{} : {}'.format(item, val))

    # `items()`, `keys()` 与 `values()` 函数返回的结构都是从源字典中的拷贝出来的, 如果被操作的字典包含大量元素, 这将会导致内存的大量浪费, 相应的, 我们可以使用 `iteritems()`, `iterkeys()` 和 `itervalues()`, 这些函数返回一个可迭代对象, 可以对这些可迭代对象进行 `for` 循环获取其中的内容, 在循环可迭代对象时, 之后当前被处理的元素才会被保存到内存当中, 当处理完成以后, 就会从内存当中删除.
    # 在 Python3 中, 对 `items()`, `keys()` 与 `values()` 这3个函数进行了重新处理, 他们全部返回 字典视图(directory view) 对象, 并且移除了 `iteritems()`, `iterkeys()` 和 `itervalues()` 函数.

# 字典推导式
前面讲解列表时, 我们讲过了 列表推导式, 字典同样也存在推导式-> 字典推导式

    @@@ python
    import os

    # 列出当前文件所在目录下的所有文件的大小
    # os.listdir() 返回指定目录下的文件列表
    # os.path.isfile 判断是否是文件
    file_size = {name: os.path.getsize(name) for name in os.listdir('.') if os.path.isfile(name)}
    print(file_size)

# default dictionary

    @@@ python
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

# ordereddict

    @@@ python
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
