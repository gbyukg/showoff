# 定义类

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 当前我们有一个公司, 公司下面有很多的员工
    # 这个时候我们可以创建一个员工的类,
    # 因为员工都共有相同的属性, 比容名字, emai地址, 工资
    # 当我们创建一个员工的类后,
    # 就可以为每个员工创建自己的实例了.

    # 创建类很简单, 使用 class 关键字即可
    class Employee:
        pass
        # 我们可以简单的放一个 pass 语句
        # 告诉Python这个类什么都不做
        # 但是即使是这样, 我们也成功地创建出了一个类
        # 当我们创建好一个类之后
        # 就可以为这个类创建任意多个实例
        # 简单来说 class 就相当于一个蓝图
        # 而实例就是根据这个蓝图创建出来的一个一个的实体
    
    # 通过 type() 查来 Employee
    print(type(Employee))

# 定义实例

    @@@ python
    # 当我们创建好一个类之后, 接着就可以创建这个类的类实例了
    # 跟其他的编程语言有点不同的地方就是
    # 在Python中创建一个实例不需要使用 `new` 关键字
    emp_1 = Employee()
    emp_2 = Employee()

    # 打印出实例, 可以看到他们都属于 Employee 的实例
    print(emp_1)
    print(emp_2)

# 定义实例属性

    @@@ python
    # 在类中, 属性可以分为两种类型,
    #   实例属性
    #   类属性
    # 首先看一下实例属性
    # 实例属性被每个实例所拥有, 各个实例之间的属性是相互分离的, 互不影响的.
    # 为类实例添加属性非常简单
    # 当创建完一个类实例后, 可以直接通过实例名为这个实例添加任何属性
    # 而不用像大部分其它编程语言那样, 需要提前在类中定义好类实例的属性
    emp_1.first = 'Test1' # 这样我们就给实例 emp_1 添加了一个新属性 first
    emp_1.last = 'User1'
    emp_1.email = 'Test1.User1@company.com'
    emp_1.pay = 5000

    # 为第二个员工添加实例属性
    emp_2.first = 'Test2'
    emp_2.last = 'User2'
    emp_2.email = 'Test2.User2@company.com'
    emp_2.pay = 6000
    # 现在这两个实例都有了自己的实例属性
    # 输出实例属性
    print(emp_1.email)
    print(emp_2.email)

# 构造函数

    @@@ python
    class Employee:
        # 虽然这段代码运行正常, 但是如果我们需要创建很多个实例
        # 每个实例都应该有这些属性, f/l name, pay
        # 如果要像这样, 为每个实例手动添加这些属性, 将会非常低效
        # 应该有这样一种机制, 就是当我们创建一个新的实例时, 应该能自动为我们创建这些属性
        # 我们可以通过类的构造函数来解决这个问题.
        # 如果我们为一个类定义了构造函数
        # 每当为这个类创建一个新的实例时,
        # 构造函数就会被 Python 自动调用.
        # 我们可以将这些属性放到构造函数中, 让 Python 自动为我们新的实例添加这些属性
        # 现在修改我们的类,
        # 增加一个特殊的方法 __init__()
        # __init__ 就是类的构造方法
        # 定义方法与定义函数是一样的, 都使用 def 关键字
        # 构造函数至少需要接收一个参数: self
        # 当构造函数被调用的时, Python 会自动将实例对象作为第一个参数传递给构造函数
        # 我们用 self 代表被传递的这个实例自身.
        # 我们还可以给构造函数设置一些其它参数, 用来初始化属性
        # 比如增加其他3个参数: first/last name 和 pay
        def __init__(self, first, last, pay):
            # 在构造方法内, 将这些属性赋给当前实例
            self.first = first
            self.last = last
            self.pay = pay
            # 在这里我们为 self 定义了这些属性
            # 因为 self 代表了当前对这个实例的引用
            # 并且我们就是要为这个实例创建这些属性
            # 所以为 self 赋值

            # 通过first 和 last name 拼接邮箱地址
            self.email = '{}.{}@company.com'.format(first, last)

    # 2
    # 现在当我们创建 Employee 实例的时候
    # Employee 类需要接受三个参数, 
    # 就是我们在定义构造函数时指定的后3个参数first/last name 和 pay
    emp_1 = Employee('Corey', 'Schafer', 5000)
    emp_2 = Employee('Test', 'User', 6000)
    # 注意, 我们并没有传递 self 参数, 因为 self 是由 Python 自动传递的
    # 无需我们插手, 并且这个参数总是作为第一个参数
    # 其实不仅仅是构造函数, 类中的所有函数都需要接受 self 作为第一个参数

    # 定义完之后就可以直接访问实例属性了
    print(emp_1.email)
    print(emp_2.email)

# 方法

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 1
    # 继续我们的例子
    # 现在考虑下面的情况,
    # 我们希望能够获取到员工的全名
    # 第一个想到的方式就是:
    # 分别获取到实例的first name 和 last name
    # 然后拼接到一起打印出来
    print('{} {}'.format(emp_1.first, emp_2.last))

    # 但是如果每次都这样获取全名, 很麻烦, 并且也会增加代码量
    # 我们可以通过在类中定义一个方法,
    # 在方法体内实现全名的拼接
    # 以后我们只需要调用这个方法, 就可以获取到全名了
    class Employee:
        ...
        def fullname(self):
        # 2
        # 跟构造函数一样
        # Python 在调用类中的方法时, 同样会自动传递当前实例作为第一个参数给这个方法
        # 所以第一个参数仍然是 self
        # 在这个方法中, 当前实例是我们唯一需要的属性
        # 因此不再需要传递其他参数到这个方法
            # 注意这里的 self.first
            # 这是我们就可以直接调用这个方法来获取员工的全名了
            return '{} {}'.format(first, last)
            # 尝试执行这段代码时, 报错
            # 提示没有找到全局变量.
            # 这是对的, 因为first 和 last 存在于实例中,
            # 我们并没有在这个方法体内定义这两个变量
            # 我们需要的是获取实例中的这两个属性
            # 所以我们需要用代表当前实例的 self 变量来获取他们的值
            # 将代码修改代码为
            return '{} {}'.format(self.first, self.last)

    emp_1 = Employee('Corey', 'Schafer', 5000)
    emp_2 = Employee('Test', 'User', 6000)

    print(emp_1.email)
    print(emp_2.email)

    #  print('{} {}'.format(emp_1.first, emp_2.last))
    # 3
    # 最后我们在通过类实例来访问 fullname() 方法
    # 这是 emp_1 就是 Python 自动传递给 self 的那个实例
    # 注意最后的括号, 因为我们调用的是方法
    print(emp_1.fullname())
    print(emp_2.fullname())

## 不传递 self 参数

    @@@ python
    # 当我们定义方法时, 必须传递一个 self 作为第一个参数给这个方法
    # 但是如果我们没有传递这个参数, 会有什么结果呢?
    # 删掉 fullname() 方法中的 self,
    print(emp_1.fullname())
    # 提示错误, 
    # 在我们fullname() 没有参数, 但是传递了一个参数
    # 这个参数就是 Python 自动传递的 self 参数

    # 我们还可以通过 Employee 类直接来调用 fullname 方法
    # 但是当我们用类名直接调用实例方法时
    # Python 不知道使用的是哪个实例
    # 所以我们就需要手动传递一个类实例作为参数传递给他
    print(Employee.fullname(emp_1))
    # emp_1 实例将传递给 fullname() 方法的 self 参数

    # 所以最终的结论就是
    # 当我们用实例调用一个类中的方法时
    # Python 会自动将这个实例作为方法的第一个参数自动传递给我们要调用的方法
    # 而我们用类名调用方法时, Python并不知道我们要使用哪个实例
    # 因此需要手动传递一个实例作为参数传递给方法
