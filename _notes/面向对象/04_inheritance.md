# 继承

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 而 `object` 类是所有类的总父类, 也就是说, Python 中的所有类都继承自 `object` 类
    class Employee(object):

        num_of_emps = 0
        raise_amount = 1.04

        def __init__(self, first, last, pay):
            self.first = first
            self.last = last
            self.pay = pay
            self.email = '{}.{}@company.com'.format(first, last)

            Employee.num_of_emps += 1

        def fullname(self):
            return '{} {}'.format(self.first, self.last)

        def apply_raise(self):
            self.pay = int(self.pay * self.raise_amount)

# 定义 Developer 子类

    @@@ python
    # 在前面的例子中, 我们定义列 Employee 类,
    # 用来表示公司中的所有员工
    # 现在我们需要根据员工的职位来区分开来
    # 比如说所有的 developer.
    # 我们可以为 developer 设计一个类,
    # 一个专门针对所有 develper 的类
    class Developer():
        pass

    # 但是所有的 developer 又同时也属于公司的员工
    # 因此 Employee类中的这些方法, 在 Developer 类中也应该同样实现.
    # 我们可以把 Employee 中的所有代码拷贝一份到 Developer 类中
    # 但是这样做不仅效率低, 当 Employee 中新增或修改了某些方法
    # 也需要在 Developer 类中作出相应的修改
    # 而且如果还有其他职位的类被创建, 所有这些类都需要被修改.
    # 效率低下.
    # 这时我们应该使用类继承来实现我们的功能
    # 如果一个类(子列)继承了某个类(父类), 那么子类将拥有父类中的所有属性和方法

    class Developer(Employee): pass

    # 现在让我们创建 Developer() 类的实例了
    dev_1 = Developer('Test1', 'User1', 5000)
    dev_2 = Developer('Test2', 'User2', 6000)
    # 输出 dev_1 的全名
    print(dev_1.fullname())
    # 查看 dev_2 的 email 地址
    print(dev_2.email)
    # 可以看到, 即使我们的 Develoer 类中什么都没写
    # 还是可以像使用 Employee 那样使用这两个实例
    # 通过help内置函数可以查看到 Developer 类中的所有属性
    #  print(help(Developer))
    # 可以看到 Developer 类中包含了所有 Employee 中的属性
    # 这些属性都是通过继承而来的

## 增加 __init__() 方法

    @@@ python
    # 现在让我们为 Developer 类添加一些新的属性
    # 当我们创建 Developer 时, 需要为每个实例指定一个新的属性: 编程语言(prog_lang)
    # 用来确定这个 Developer 使用的是那种编程语言.
    # 我们需要重写父类中的 __init__(self) 方法, 来增加这个属性
    # 在最后追加一个属性 prog_lang
        def __init__(self, first, last, pay, prog_lang):
            # 在父类的构造函数中, 我们已经实现了名字和工资功能
            # 因此我们不应该再重复编写这些代码
            # 只要告诉Python, 我们需要调用父类的构造函数来帮我们初始化这些名字和工资这些属性
            # 可以通过类名的方式调用父类的构造方法
            Employee.__init__(self, first, last, pay)
            # 因为我们是通过类名直接调用的实例函数, 所以需要手动传递类实例参数 self.
            # 但是这样做的缺点就是, 一个是每次都需要手动传递 self 参数
            # 另一个是如果父类类名变了, 我们就得在所有使用类名调用的地方修改

            # 一个更好的方式是使用 super() 方法
            # 这个方法是专门用来调用父类中的方法的.

            # python 3
            #  super().__init__(first, last, pay)
            # python 2
            super(Developer, self).__init__(first, last, pay)
            # 这样我们就可以利用父类中的构造函数来帮助我们初始化 name 和 pay 属性了
            # 现在我们需要增加一个新的属性 prog_lang 给 Developer 类使用
            self.prog_lang = prog_lang

    # 修改我们的实例化类的代码, 增加新的参数.
    dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
    dev_2 = Developer('Test', 'User', 6000, "Java")
    # 此时我们就可以获取到Develper的编程语言技能了
    print(dev_1.prog_lang)
    print(dev_2.prog_lang)
    # 至此, 我们定义的子类 Developer 类就完成了.

    #########################################
    # 现在让我们自定义一些新的属性给 Developer 子类
    # 在 Employee 类中, 所有员工工资涨幅都是 1.04
    # 但是工资比较看重程序员, 对程序员的涨幅比较大
    # 我们可以直接在 Developer 类中定义同样的类变量
    # raise_amount = 1.10
    # 再次输出员工工资
    # 可以看到 dev_1 的工资已经发生了变化
    #  print(dev_1.pay)
    #  dev_1.apply_raise()
    #  print(dev_1.pay)
    #  print(dev_1.raise_amount)
    # 打印出 Employee 类的属性
    # 并没有改变, 说明修改子类中的属性, 并不会影响到父类
    #  print(Employee.raise_amount)

    # 当我们创建一个developer实例时
    # 我们希望不仅能体现出员工的姓名和工资
    # 同时还能指出developer使用的编程语言
    # 我们需要让 Developer 类使用自己的构造方法

    dev_1 = Developer('Corey', 'Schafer', 5000, 'Python')
    dev_2 = Developer('Test', 'User', 6000, "Java")
    print(dev_1.email)
    print(dev_2.email)

# 定义 Manager 子类

    @@@ python
    # 现在在让我们继续创建另一个子类 Manager 类, 用来创建 Manager
    # 作为一个 Manager, 他下面应该记录了他手下的员工信息
    # 我们应该可以方便的查看, 添加和删除 Manager 下的员工
    # 创建 Manager 类, 同样继承自 Employee 类.
    class Manager(Employee):
        # 注意, 不要使用一个可变类型对象作为默认值
        # 原因我们已经在 函数 那节讲过了.
        def __init__(self, first, last, pay, employees=None):
            super(Manager, self).__init__(first, last, pay)
            if employees is None:
                self.employees = []
            else:
                self.employees = employees

        # 需要一个方法, 用来向这个 Manager 中增加员工
        def add_emp(self, emp):
            if emp not in self.employees:
                self.employees.append(emp)

        # 用来删除员工的方法
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)

        # 打印出 Manager 名下的所有员工信息
        def print_emps(self):
            for emp in self.employees:
                print('-->{}'.format(emp.fullname()))

    # 创建一个 Manager 实例
    mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
    # 先尝试打印出 manager 的邮件地址
    print(mgr_1.email)
    # 因打印员工信息
    mgr_1.print_emps()
    # 增加一个新员工
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()
    mgr_1.remove_emp(dev_1)
    mgr_1.print_emps()

# 类方法

    @@@ python
    # isinstance()
    print(isinstance(mgr_1, Manager))
    print(isinstance(mgr_1, Employee))
    print(isinstance(mgr_1, Developer))
    # issubclass
    print(issubclass(Developer, Employee))
    print(issubclass(Manager, Employee))
    print(issubclass(Manager, Developer))

    # 而 `object` 类是所有类的总父类, 也就是说, Python 中的所有类都继承自 `object` 类
