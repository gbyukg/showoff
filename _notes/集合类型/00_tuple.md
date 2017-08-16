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