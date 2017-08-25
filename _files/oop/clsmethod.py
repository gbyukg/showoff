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
        # 修改类属性
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        # 创建一个新的实例
        # 并返回这个实例
        return cls(first, last, pay)

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'Employee', 6000)

# 创建一个新的类方法 set_raise_amount
# 与常规方法类似, 在常规方法中用 self 代表实例本身
# 而类方法中使用 `cls` 来表示类本身
# cls.raise_amount = amount
# 类方法需要使用类名来直接访问
# 传递一个参数
# 同样, Python 会自动将类本身作为类方法的第一个参数传递给它, 无需我们手动传递
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 效果是一样的
Employee.raise_amount = 1.05

##########################################
# 现在让我们尝用实例去调用一个类方法
emp_1.set_raise_amount(1.08)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
# 使用实例调用类方法没有任何问题
# 并且正确修改了类变量


##########################################
# 现在我们考虑下面情况
# 我们又如下字符串
emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'
emp_str_3 = 'Jane-Doe-9000'
# first name, last name 和 pay 都用-分割
# 现在要通过这些字符串来创建Employee实例
# 我们可以拆分这些字符串
# 并保存这些变量
first, last, pay = emp_str_1.split('-')
# 根据这些变量来生成实例
new_emp_1 = Employee(first, last, pay)
print(new_emp_1.email)
print(new_emp_1.pay)
# 可以正确输出

# 但是每次都要手动拆分字符串, 然后在创建实例
# 这时候我们可以创建一个 类 方法,
# 用来专门处理这种格式的字符串
# 并创建一个新的类示例
# 这样我们每次只需要调用这个类方法, 并把这个字符串作为参数传递给它, 就能创建一个新的实例
# 创建类方法 from_string
new_emp_3 = Employee.from_string(emp_str_3)
print(new_emp_3.email)

