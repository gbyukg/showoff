# 类属性

## 硬编码编写 apply_raise(self) 方法

    @@@ python
    class Employee():
        ...
    # 继续使用这个例子
    # 公司每年都会为员工涨工资,
    # 涨幅后的工资等于当前工资乘以涨幅百分比
    # 在这里我们假定所有的员工工资涨幅度都是一样的
    # 要获取员工涨薪后的工资
    # 可以定义一个新的方法
    def apply_raise(self):
        self.pay = int(self.pay * 1.04) # 1

    # 这时我们就可以将涨幅度设置成一个类属性来使用.
    # 但是在使用类变量之前, 我们先用硬编码的形式来实现这个功能
    # 增加一个新方法 apply_raise(self)
    # 这个方法用来返回员工当前工资*加薪后的工资

    # 现在我们来输出员工的工资
    # 首先输出加薪前的工资
    print(emp_1.pay)
    emp_1.apply_raise()
    print(emp_1.pay)

## 定义类变量
虽然现在运行起来一切正常, 但是有许多地方需要改进, 首先我们应该能通过某个变量来够获取到工资的涨幅, 类似一些这样的变量 `emp_1.raise_amount`, 因为我们假定所有的员工涨幅都一样, 所以每个员工获取到的值都应该是一样的, 甚至我们还应该可以通过类名来获取到这个百分比, 像是 `Employee.raise_amount`

但是当前类中并不存在 raise_amount 这个变量, 所以我们还无法获取到这个值, 而且如果这个值在类中被很多地方使用时, 当涨幅度发生变化后, 我们应该能够很容易的修改这个值, 而不是像上面定义的那个函数那样, 需要修改所有出现 1.04 这个值的地方

为了达到以上这些要求, 我们可以使用类变量, 一个类变量可以被该类的所有实例所共享, 这意味着任何一个类实例都可以访问类变量, 定义类变量非常简单, 在类中所有方法外定义的变量, 就是一个类变量, 而且类变量一般都定义在类中的最上面.

    @@@ python
    class Employee():
        raise_amount = 1.04
        # 一旦定义好一个类变量后, 我们就可以使用这个类变量了
        ...
    # 当定义好一个类变量后
    # 我们既可以用某个实例去访问类变量
    print(emp_1.raise_amount)

    # 也能使用类名来访问这个实例变量
    print(Employee.raise_amount)

    # 这是因为当我们尝试访问一个实例中的属性时,
    # Python首先会在这个实例对象中查找这个属性
    # 如果没有在当前实例对象中找到这个属性
    # 则它将尝试到类中查找, 如果仍然没有找到, 将继续在类的父类中查找这个属性
    # 直到查找到最上层, 如果仍然没有找到, 则程序报错退出


## 更新 apply_raise() 方法

    @@@ python
    # 现在修改我们的 apply_raise 函数, 使用类变量名来替换
    # 修改代码
    # 用类名 Employee 来访问 raise_amount 属性
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)

    # 执行代码, 可以正常使用
    # 在这个例子中, 我们使用 类名 来访问类属性

    # 现在尝试使用实例 self 来访问这个属性
    self.pay = int(self.pay * self.raise_amount)
    # 当我们尝试用实例去访问 raise_amount 变量时,
    # 实例中并不存在这个属性, 所以Python自动在Employee类中查找这个变量
    # 最终发现了这个变量的定义, 并返回这个变量的值

    # 我们可以通过打印出实例中的所有属性来看看到底是什么情况
    # Python中, 每个实例都有一个特殊的属性 __dict__,
    # 这是一个字典类型, 保存了实例中的所有属性信息
    print(emp_1.__dict__)
    # 我们发现在输出的结果中并没有发现 raise_amount 这个属性
    # 使用同样的方法来获取类中的属性
    print(Employee.__dict__)
    # 可以看到类中存在这个属性

## 通过类名修改类属性

    @@@ python
    # 现在我们将尝试用类来修改这个类变量
    Employee.raise_amount = 1.05
    # 再次输出这个值
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    # 发现每个实例中的值也跟着发生了变化
    # 说明他们都共享了同一个变量

## 通过实例修改类属性

    @@@ python
    # 但是如果我们尝试使用实例去更新这个值会怎么样呢
    emp_1.raise_amount = 1.05
    # 再次输出这个值
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    # 会发现只有 emp_1 中的值发生了变化
    # 这是因为当我们使用 emp_1.raise_amount = 1.05 去更新这个值的时候
    # 实际上是为 emp_1 实例创建了一个新的实例属性
    # 再次打印出实例中的所有属性
    print(emp_1.__dict__)
    # 会发现实例中已经多了一个 raise_amount 属性

    # 现在在让我们返回到 apply_raise() 方法
    # 虽然使用类名和self都可以获取到 raise_amount 这个属性
    # 但是我们更倾向于使用 self,
    # 因为这样我们就可以为不同的员工设置不同的涨幅度了
    # 而使用类名 Employee 将总是获取类中的这个属性值

## 何时使用类名获取类属性

    @@@ python
    #################################################
    # 但是并不是什么时候使用self都是一个好的选择
    # 现在我们想要获取员工的数量
    # 我们通过增加一个新的类变量 num_if_emps, 用来表示当前员工数
    # 而这个员工数对于所有员工来说获取到的值应该都是一样的
    # 当定义好这个类变量后
    # 修改构造函数, 增加 Employee.num_of_emps += 1
    class Employee():
        num_of_emps = 0
        def __init__(self):
            ...
            # 当每当实例化一个新实例对象时, 就会自动加 1
            Employee.num_of_emps += 1
    # 这样每当我们实例化一个实例后, 类属性 num_of_emps 就会加1
    # 这里我们更倾向于使用类名来访问这个属性, 因为我们不想让实例属性来覆盖这个变量
    print(Employee.num_of_emps)

## 程序
    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    class Employee():
        num_of_emps = 0 # 2
        raise_amount = 1.04 # 1

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = '{}.{}@company.com'.format(first, last) # 3

            Employee.num_of_emps += 1

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            #  self.pay = int(self.pay * 1.04) # 1
            #  self.pay = int(self.pay * raise_amount) # 2
            self.pay = int(self.pay * self.raise_amount)

    emp_1 = Employee('Corey', 'Schafer', 5000)
    emp_2 = Employee('Test', 'User', 6000)

刚才我们提到了, 类中的属性有两种, 实例属性和类属性, 上面的例子中, 我们讲解了实例变量. 实例变量是属于单个实例的,他们之间相互分离, 互不影响, 但有些时候, 我们需要一些所有实例可以共享的变量, 这可以通过创建类变量来达到我们的目的.因为类变量可以被类的所有实例共享.
