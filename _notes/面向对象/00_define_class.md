# 定义类
比如说当前我们有一个公司, 公司下面有很多的员工, 这个时候我们可以创建一个员工的类, 因为员工都共有相同的属性, 比如员工姓名, emai地址, 工资等, 当我们创建一个员工的类后,就可以为每个员工创建自己的实例了.

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 创建类很简单, 使用 class 关键字即可
    class Employee:
        pass

我们可以简单的放一个 pass 语句, 告诉Python这个类什么都不做, 但是即使是这样, 我们也成功地创建出了一个类, 当我们创建好一个类之后, 就可以为这个类创建任意多个实例.  
简单来说 class 就相当于一个蓝图, 而实例就是根据这个蓝图创建出来的一个一个的实体.

# 定义实例
当我们创建好一个类之后, 就可以为这个类创建实例了

    @@@ python
    # 在Python中创建一个实例不需要使用 `new` 关键字
    emp_1 = Employee()
    emp_2 = Employee()

    # 打印出实例, 可以看到他们都属于 Employee 的实例
    print(emp_1)
    print(emp_2)

# 定义实例属性
在面向对象这方面, Python 跟其它编程语言最大的不同, 当我们创建好一个类的实例后, 可以自由地为这个实例创建任何想要的属性. 而不用必须在类中提前预定好这些属性, 然后严格按照这些预定要的属性为每个实例设置这些属性.  
这就看出来 Python 的思想, 比较自由奔放, 风骚一点.

    @@@ python
    class Employee(object):
    pass

    emp_1 = Employee()
    emp_2 = Employee()
    # 比如添加一个 first 属性
    # 格式: 实例名 点 属性名
    emp_1.first = 'Test1'
    emp_1.last = 'User1'
    # 访问也是通过这样的方式
    emp_1.email = "{}.{}@mail.com".format(emp_1.first, emp_1.last)
    emp_1.pay = 5000
    print(emp_1.email)
    print(emp_1.pay)

    # 通过这种方式定义的属性我们叫做实例属性
    # 实例属性被每个实例所拥有
    # 各个实例之间的属性是相互分离的, 互不影响的.

    # 用同样的方式为emp_2 创建属性
    emp_2.first = 'Test2'
    emp_2.last = 'User2'
    emp_2.email = "{}.{}@mail.com".format(emp_2.first, emp_2.last)
    emp_1.pay = 6000
    print(emp_2.email)
    print(emp_2.pay)
    # 可以看到输出值是不同的

# 构造函数
虽然这段代码运行正常, 但是这种方式非常不好, 因为如果我们需要创建很多个实例, 每个实例都应该有这些属性: f/l name, pay, email. 如果每创建一个实例都要手动为这些实例添加这些属性, 不但代码量多, 而且容易出错, 比如拼写错误, 因为即使拼写错误, Python 也不知道, 因为我们可以自由的为实例创建人和属性.

这时候我们就可以使用类的构造函数了, 构造函数在创建一个类实例时会被自动调用, 将这些属性设置放到构造函数中, 这样每次声明一个实例后, 就会自动为我们创建这些属性了.

    @@@ python
    class Employee(object):
        # 现在修改我们的类,
        # 增加一个构造函数
        # 无论是定义构造函数, 还是类中的方法
        # 跟之前讲过的函数定义是一样的
        # 都使用 def 关键字
        # Python 中的构造函数名是固定的, __init__
        def __init__(self, first, last, pay): # 这里需要一个 self 参数
            # 无论是定义构造函数
            # 还是定义类中的其他实例方法
            # (后面会讲什么是实例方法, 这里暂时理解为类中的所有方法)
            # 都必须至少接受一个参数, 我们一般使用 self 内置变量来接收
            # self 的含义就是
            # 当我们用一个实例调用类中的一个方法时,
            # self 代表了这个实例自己
            # 可以简单理解为 Java 中的 this 关键字
            # 只不过在 Java 中定义方法时不用明确指定方法接收实例自身
            # 并把它赋值给 this 关键字
            # 而在 Python 中定义方法时
            # 需要明确指定接收的第一个参数是实例自身

            # 在这个类里, 构造函数要做的就是
            # 设置 first, last, email 和 pay 这些属性
            # 所以我们的构造函数还得接收这些参数
            # email 可以拼接, 所以不需要通过参数传递了
            self.first = first
            self.last = last
            self.pay = pay
            self.email = "{}.{}@mail.com".format(self.first, self.last)

    emp_1 = Employee('Test1', 'User1', 5000)
    # 当 Python 执行到这段代码时
    # 会调用 Employee 中的构造函数
    # 并把这些参数传递给构造函数
    # 这时的 self 参数就是 emp_1
    # 但是构造函数明明是接收 4 个参数
    # 并且第一个参数是实例自身
    # 而我们只传递了3个参数
    # 这是因为Python会自动将实例自身作为第一个参数传递给构造函数
    # 而不用我们手动传递它
    # 也就是说, 我们只管定义一个参数来接收它就行
    # 剩下的 Python 就会为我们做了
    # 注意哈, self 在类中所有的工作模式都是这样的
    # 而不仅仅是构造函数

    emp_2 = Employee('Test2', 'User2', 6000)
    print(emp_1.email)

# 方法

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    # 继续我们的例子
    # 现在考虑下面的情况,
    # 我们希望能够获取到员工的全名
    # 使用 first 和 last 拼接起来的名字
    # 最简单的的方式就是:
    # 直接使用 first 和 last 拼接然后打印出来
    print('{} {}'.format(emp_1.first, emp_2.last))

    # 但是如果每次都这样获取全名, 很麻烦, 并且也会增加代码量
    # 我们可以通过在类中定义一个方法,
    # 在方法体内实现全名的拼接
    # 以后我们只需要调用这个方法, 就可以获取到全名了
    # 虽然也可以向 email 那样在构造函数中直接拼接出来
    # 但是它也是有弊端的,我们会在后面讲到
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
            # 这时我们就可以直接调用这个方法来获取员工的全名了
            return '{} {}'.format(first, last)
            # 尝试执行这段代码时, 报错
            # 提示没有找到全局变量.
            # 这是对的, 因为first 和 last 存在于实例中,
            # 我们并没有在这个方法体内定义这两个变量
            # 我们需要的是获取实例中的这两个属性
            # 所以我们需要用代表当前实例的 self 变量来获取他们的值
            # 将代码修改代码为
            return '{} {}'.format(self.first, self.last)

    # 现在我们就可以通过类实例来访问 fullname() 方法
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

## 通过类名访问实例方法

    @@@ python
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
    # 虽然这两种方式都可以调用类中的方法
    # 但明显第一种更简洁易懂
