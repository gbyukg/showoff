<!SLIDE>
# 字典(dict)

字典的定义使用大括号 `{}`, 其中元素以 `键:值` 的形式存在.

与元组和列表不同, 字典是非顺序的, 这意味着字典中元素的位置是不可确定的, 可能与我们创建字典是指定的顺序或插入的顺序不符.

字典中的键可以是任何可序列化的对象, 可序列可以化简单理解为任何其值为不可变的对象, 比如: 数字, 字符串, 元组等都是可序列化对象.

字典对应的内置函数为 `dict()`

    @@@ python
    d1 = dict()

    d2 = dict(id=1948, name="Washer", size=3)

    d3 = dict(d2)

    d4 = dict([['id', 1948], ('name', 'Washer'), ('size', 3)])

    d5 = {"root": 17, 'blue': [75, 'R', 2], 21:'venus', -14:None, 'mars':'rover', (4,11):18, 0:45}

## `zip()`
可将传递给他的可迭代对象参数按顺序依次解压, 将每个参数中相同位置的元组合并成一个元组, 最终返回一个可迭代的 `zip` 类, 通过 循环 或内置函数 `next` 依次读取这些元组.

    @@@ python
    z = zip(('id', 'name', 'size'), (1948, 'Washer', 3))
    next(z)

    for i in z:
        print(z)

    # 通过 zip 创建字典对象
    d4 = dict(zip(('id', 'name', 'size'), (1948, 'Washer', 3)))

<!SLIDE transition=turnUp>
# 字典中的方法

语法 | 说明
 -- | ---
d.clear()          | 清空字典中的所有元素
d.copy()           | 返回一个新的字典对象 `d` 的拷贝对象
d.fromkeys(s, v)   | 返回一个新的字典对象, 字典的 key 为可迭代对象 `s` 中的所有元素, 如果指定了参数 `v`, 则所有 `key` 的值为 `v`, 否则所有 `key` 的值为 `None`
d.get(k)           | 返回字典中键 `k` 对应的值, 如果不存在 `k`, 则返回 `None`
d.get(k, v)        | 同上, 但是如果不存在 `k` 键, 则返回给定的值 `v`
d.items()          | 将字典中所有的元素以 (key, value) 的形式保存到 字典视图 中, 并返回这个视图
d.keys()           | 返回一个字典视图, 包含了字典中所有的键
d.values()         | 返回一个字典视图, 包含了字典中所有的值
d.pop(k)           | 返回字典中键 `k` 对应的值, 并将该键从字典中移除, 如果字典中不存在键 `k`, 则抛出 KeyError 异常
d.pop(k, v)        | 返回字典中键 `k` 对应的值, 并将该键从字典中移除, 如果字典中不存在键 `k`, 则返回 `v`
d.popitem()        | 从字典中删除随意一个键值对, 并返回被删除的键值对, 当对一个空的字典进行 popitem() 操作时, 将会抛出 `KeyError` 异常
d.setdefault(k, v) | 如果字典中存在键 `k`, 则返回它在字典中对应的值, 如果不存在该键, 则向该字典中插入值为 `v` 的键 `k`, 并返回值 `v`
d.update(a)        | 更新字典, 该方法接收三种形式的参数: 一个字典; 或是一个可迭代对象, 每次迭代返回的都是一个包含两个元素的对象分别作为 key 和 value; 或是向该函数传递关键字参数

<!SLIDE transition=turnUp>
# 字典视图

字典视图是一个只读的可迭代对象, 可用来保存字典中的键, 或值, 或键值对

我们可以通过调用调用 `d.keys()`, `d.values()` 还是 `d.items()` 来分别获取这些值.

字典视图是动态的, 能够实时反映出字典的变化.

字典视图还支持 `set` 类型的集合操作

- `v & x` 交集
- `v | x` 并集
- `v - x` 差集
- `v ^ x` 对称差集

.callout.warning 在 Python2 中, `items()`, `keys()` 与 `values()` 函数返回的结果都是从源字典中拷贝出来的, 如果被操作的字典包含大量元素, 这将会导致内存的大量浪费, 相应的, 我们可以使用 `iteritems()`, `iterkeys()` 和 `itervalues()`, 这些函数返回一个可迭代对象, 可以对这些可迭代对象进行 `for` 循环获取其中的内容, 在循环可迭代对象时, 之后当前被处理的元素才会被保存到内存当中, 当处理完成以后, 就会从内存当中删除.

.callout.warning 在 Python3 中, 对 `items()`, `keys()` 与 `values()` 这3个函数进行了重新处理, 他们全部返回 字典视图(directory view) 对象, 并且移除了 `iteritems()`, `iterkeys()` 和 `itervalues()` 这3个函数.

<!SLIDE transition=turnUp>
# 字典推导式

列表推导式两种格式:

- `{keyexpression: valueexpression for key, value in iterable}`
- `{keyexpression: valueexpression for key, value in iterable if condition}`

获取当前目录下所有文件的大小, 其中键为文件名, 值为文件的大小

    @@@ python
    import os

    # 列出当前文件所在目录下的所有文件的大小
    file_size = {name: os.path.getsize(name) for name in os.listdir('.') if os.path.isfile(name)}
    print(file_size)

<!SLIDE transition=turnUp>
# Default Dictionaries
Default Dictionaries 与 普通的字典完全一样, 唯一的不同是在当我们访问一个 Default Dictionaries 中不存在的键时, 它都会自动将这个键添加到字典中, 并且为这个键设置一个指定的默认值, 同时返回这个默认值.

Default Dictionaries 存在于 `collections` 包中, 默认不会被 Python 解释器引入, 因此在使用 Default Dictionaries 之前需要引入该包: `import collections`

    @@@ python
    words = collections.defaultdict(int)
    print(words['a'])

    sentences = collections.defaultdict(tuple)
    print(sentences['word'])

defaultdict 需要一个工厂函数作为参数传递给它. 一个工厂函数就是当我们调用一个函数时, 这个函数能够返回给我们一个特定类型的对象. 所有 Python 内置的数据类型都可以被当做一个工厂函数来使用.  
比如前面我们讲解到的 `str()`, 能够返回一个字符串, `int()`, `float()`, `tuple()`, `set()`, `dict()` 都是工厂函数.

<!SLIDE transition=turnUp>
# 有序的字典

与普通的字典不同, 有序字典严格保留了创建字典是键的顺序, 当向字典中插入新的元素时, 新插入的元素一定是字典中的最后一个元素.

使用 `collections.OrderedDict()` 来创建一个有序字典

    @@@ python
    import collections
    d = collections.OrderedDict([('z', -4), ('e', 19), ('k', 7)])

    tasks = collections.OrderedDict()
    tasks[8031] = 'Backup'
    tasks[4027] = 'Scan Email'
    tasks[5733] = 'Build System'
