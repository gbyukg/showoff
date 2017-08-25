#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 而 `object` 类是所有类的总父类, 也就是说, Python 中的所有类都继承自 `object` 类
class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        print(dir(self))
        print(self)
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)
        print(dir(self))

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    # 我们先将类留空, 什么也不做
    #  pass # 1
    raise_amount = 1.10 # 2

    # 增加新的属性  prog_lang
    def __init__(self, first, last, pay, prog_lang):
        # 在父类中, 我们已经实现了名字和工资功能
        # 因此我们不应该再重复编写这些代码
        # python 3
        #  super().__init__(first, last, pay)
        # python 2
        super(Developer, self).__init__(first, last, pay)
        # 这里有很多种方式来实现调用父类构造函数
        # 比如直接通过类名来调用
        # 如果使用这种方式来写的话,
        # 当我们的类名发生变化时
        # 这里也需要作出相应的变更
        #  Employee.__init__(self, first, last, pay)

        self.prog_lang = prog_lang

# developers
#  dev_1 = Developer('Corey', 'Schafer', 5000)
#  dev_2 = Developer('Test', 'User', 6000)
#  print(dev_1.email)
#  print(dev_2.email)
# 可以看到, 即使我们的 Develoer 类中什么都没写
# 还是可以像使用 Employee 那样使用这两个实例
# 通过help内置函数可以查看到 Developer 类中的所有属性
#  print(help(Developer))
# 可以看到 Developer 类中包含了所有 Employee 中的属性
# 这些属性都是通过继承而来的

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

# 此时我们就可以获取到Develper的编程语言技能了
print(dev_1.prog_lang)


#########################################
# manager

class Manager(Employee):
    # 注意, 不要使用一个可变类型对象作为默认值
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            print('ttt')
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->{}'.format(emp.fullname()))

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

#################################
# isinstance()
print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))
# issubclass
print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))

# 而 `object` 类是所有类的总父类, 也就是说, Python 中的所有类都继承自 `object` 类
