<!SLIDE transition=turnUp>
# 创建

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

    d4 = dict(zip(('id', 'name', 'size'), (1948, 'Washer', 3)))
    print("d4:", d4)

    # 传递一个可迭代对象, 可以是一个元组, 也可以是一个列表
    # 迭代对象中每个元素又是另一个包含2个元素的可迭代对象, 元素0->key, 元素 1->value
    d5 = dict([['id', 1948], ('name', 'Washer'), ('size', 3)])
    print("d5:", d5)

    # 也可以直接通过 大括号 创建字典
    # 字典中的键值要保证是唯一的, 否则后面出现的键将会覆盖前面先出现的键
    # 字典中的键可以是任何可哈希(hash)的对象, 可哈希对象简单理解就是其值不可改变的对象, 数字, 字符串, 元组就是可可哈希的对象
    # 可以使用内置函数 `hash()` 判断一个对象是否是可哈希的
    # hash((1, 2, 3))
    # hash((1, 2, [3, 4])) 包含列表, 不可哈希
    d6 = {"root": 17, 'blue': [75, 'R', 2], 21:'venus', -14:None, 'mars':'rover', (4,11):18, 0:45}
    print("d6", d6)

    # 通过键值访问对应的元素
    print("d6:root", d6['root'])
    print("d6:blue", d6['blue'])
    print("d6:-14", d6[-14])
    print("d6:(4,11)", d6[(4,11)])
    # 当访问一个不存在的键时, 会抛出 KeyError 异常
    #  d6['x']

    # 新曾元素, 因为字典是非顺序的, 所以新增的元素不一定会被追加到字典的结尾
    d6['x'] = 59
    print('d6', d6)

    # 可以像之前讲解变量时那样, 使用 del 删除字典中的一个元素
    del d6['x']
    print('d6', d6)

    # 我们可以使用内置函数 len() 来获取字典的长度
    print(len(d6))

## zip

    @@@ python
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

# 字典方法

    @@@ python
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

# 字典视图
在上面的方法中我们提到了 `items()`, `keys()`, 和 `values()` 返回一个字典视图对象.

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    d = {'user': 'Smith', 'address': ['USA', 'Littleton'], 'Level': 10, 'size': 15}

    keys = d.keys()
    values = d.values()
    items = d.items()

    # python2
    view_keys = d.viewkeys()

    d.pop('user')
    print(keys)
    print(view_keys)
    print(values)
    print(items)
    print(d)


    d = {}.fromkeys('ABCD', 3)
    #  print(d)
    s = set('ACX')
    #  x = d.viewkeys() & s
    x = d.keys() & s
    print(x)

# 列表推导式

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

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
