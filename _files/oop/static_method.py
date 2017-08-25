#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee:

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

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    # 使用 @staticmethod 来创建一个静态方法
    # 在静态方法中, 我们不能访问任何实例属性或是类属性
    # Python 也不会自动传递任何参数给静态方法
    # 因此在定义静态方法的时候, 直接写上我们将要传递给方法的参数就可以了
    # 这里需要一个日期参数, 用来判断是否是工作日
    # 不需要self或是 cls 参数
    def is_workday(day):
        # 星期一是0, 所以星期6是5
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", 'Schafer', 5000)
emp_2 = Employee("Test", 'User', 6000)

# 现在先总结一下
# 常规方法中, Python 会自动传递调用常规方法的实例作为第一个参数传递给它, 我们用 self 来代表
# 类方法中, Python 会自动传递当前类作为第一个参数传递给它, 我们用 cls 来代表

# 现在我们需要给 Employee 类增加一个新的方法
# 这个方法用来判断当前是否是工作日, 只要不是周六周日, 就是工作日
# 从需求来看, 这个方法不需要访问任何实例中的属性或是类中的属性
# 所以我们可以创建一个静态方法来实现这个功能
# 这样我们就可以使用这个方法来判断是否是工作日了
# 类方法和静态方法调用方式一样, 都是使用类名直接调用

# 因为这个参数中需要传递一个日期对象
# 我们首先引入 datetime 包
import datetime
# 生成一个新的日期对象
my_date = datetime.date(2017, 8, 23)
# 将日期对象作为参数传递给is_workday静态方法
print(Employee.is_workday(my_date))

##############################################
# 静态方法和类方法很相似, 都是通过类名直接访问的
# 我们应该怎么选择什么时候时候类/静态方法呢?
# 一般当我们的方法中不需要访问任何类中的属性, 或是实例中的属性时
# 就可以使用静态方法, 剩下情况下就使用类方法
