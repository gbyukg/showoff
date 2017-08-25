#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = '{}.{}@company.com'.format(first, last)

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)

# 当我们定义方法时, 必须传递一个 self 作为第一个参数给这个方法
# 但是如果我们没有传递这个参数, 会有什么结果呢?
# 删掉 fullname() 方法中的 self,
# 和 print(emp_1.fullname())
# 没有任何错误
# 但是当我们添加
print(emp_1.fullname())
# 提示错误, fullname() 没有参数, 但是传递了一个参数
# 这个参数就是 Python 自动传递的 self 参数

# 我们还可以通过 Employee 类直接调用 fullname 方法
# 但是当我们用类名直接调用实例方法时
# Python 不知道使用的是哪个实例
# 我们就需要手动传递一个类实例作为参数传递给他
print(Employee.fullname(emp_1))

# 所以最终的结论就是
# 当我们用实例调用一个类中的方法时
# Python 会自动将这个实例作为方法的第一个参数自动传递给我们要调用的方法
# 而我们用类名调用方法时, Python并不知道我们要使用哪个实例
# 因此需要手动传递一个实例作为参数传递给方法
