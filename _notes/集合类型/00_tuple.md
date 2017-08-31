# 序列
整型, 浮点型, 布尔型都只有一个值, 不属于.  
但是字符串是, 包含了多个字符. `s = 'str'` 由 3 个字符组成.

- 向前面提到过, 可以用 `in` 和 `not in` 判断字符串
- `len(str)`, 注意调用方式, 跟之前使用string方法不太一样, 内置函数. string 方法是string类的方法

# 元组
    @@@ python
    # 最后一个元素可以加逗号, 也可以不加
    (1, 2, 3)
    (1, 'two', 3)

    # 也可以不使用括号
    a = 1, 2, 'three'
    type(a)
    # 只有一个元素时, 后面必须有逗号
    a = 1,

# 访问元素
    @@@ python
    t = (1, 2, ('venus', -28, 'green', '21', -28, 19.75), 'STG', 'SWG')
    t[1]
    t[-2]
    t[2][2]

    t = ('venus', -28, 'green', '21', -28, 19.75)
    t[2:]
    t[:2]
    t[::]
    t[::-1]

# 元组中的函数
    @@@ python
    t = ('venus', -28, 'green', 21, -28, 19.75)
    t.count(-28)
    t.index('green')

    # 获取长度
    len(t)

    # 相加
    (1,) + (2, 3)

    # 相乘
    (1,) * 5

    21 in t
    21 not in t

# 解压元组
    @@@ python
    # 左边数量大于右边, 则报错
    # 左边数量小于右边, 多出的则忽略
    first, last = ('Jims', 'Smith')

    # 在Python3中的新增加了一项功能, 可以使用 `*` 来代替剩余元素.
    tup_str = ('str1', 'str2', 'str3', 'str4')
    str1, str2, *str3 = tup_str
    str1, *str2, str3 = tup_str

# 命名元组

元组只能通过索引来访问, 可以使用 Python 的扩展功能创建一个命名元组, 它可以让我们通过名字来访问元组中的元素. 访问数据库时, 将列明作为命名元组.

    @@@ python
    # 使用前先要定义一个命名元组类型
    import collections
    # 第一个参数类名
    Sale = collections.namedtuple("Sale", "productid customerid date quantity price")
    # 查看
    dir()
    dir(Sale)
    help(Sale)

    # 创建命名元组实例
    s1 = Sale(432, 921, "2017-01-01", 3, 7.99)
    s2 = Sale(date='2017-01-01', productid=432, customerid=921, quantity=3, price=7.99)

    # 访问
    s1.productid
    s2.date

    # 返回一个元组, 包含了所有元素名
    s1._fields

    # 获取一个列表
    s1._asdict()

---

# 什么是可迭代对象

简单来说, 在 Python 中, 所有可直接作用到 `for` 循环上的对象, 都是可迭代对象

在讲解字符串的时候, 我们提到了 `in` 关键字, 用 `for...in` 结构可以循环迭代一个可迭代对象, 如:

    @@@ python
    for c in a:
        print(c)

所有的序列类型都是可迭代对象, 字符串也是可迭代对象.

    @@@ python
    t.count(-28)
    t.index(-28)

# 切片
    @@@ python
    eyes = ('brown', 'hazel', 'amber', 'green', 'blue', 'gray')
    hair = ("black", "brown", "blonde", "red")
    colors = (hair, eyes)
    colors[1][3:-1]

# 解压元组
解压元组中的元素时, 赋值左边的变量个数一定不能大于元组中元素的个数, 否则会报出错误, 如果变量数小于元组中的个数, 没有对应的元组中的元素将被忽略掉.

在Python3中的新增加了一项功能, 可以使用 `*` 来代替剩余元素.

# 定义命名元组

    @@@ python
    import collections
    Sale = collections.namedtuple("Sale", "productid customerid date quantity price")

在这个例子中, 我们创建了一个新的类 `Sale`, 它的类型为命名元组, 当我们通过 `type(Sale)` 来查看它的类型时, 会发现它是一个 `class`, 其实我们之前讲解的所有类型, 都是 class 对象. `type(1)`, `type(1,2)`, `type('abc')`, `type(())`, 并且可以使用 `help()` 查看他们的帮助文档.

`help(Sale)` 获取帮助信息, 会发现它是一个类, 并且我们传递给 `namedtuple` 的第二个参数中的每个元素都成为了该类中的一个属性, 该类继承与 `tuple`, 所以也存在 `count()` 和 `index()` 两个方法

    @@@ python
    # 此处的 Sale 是上面赋值语句左边的变量 Sale
    s1 = Sale(432, 921, "2017-01-01", 3, 7.99)
    s2 = Sale(productid=432, customerid=921, date='2017-01-01', quantity=3, price=7.99)

在查询数据库表时, 为每个表创建一个命名元组, 使用命名元组对应数据库表中的条目