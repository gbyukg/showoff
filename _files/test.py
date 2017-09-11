#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Employee(object):

    raise_amount = 1.04

    def __init__(self, first, last, pay): # 这里需要一个 self 参数
        self.first = first
        self.last = last
        self.pay = pay
        self.email = "{}.{}@mail.com".format(self.first, self.last)

    def fullname(self):
        return '{} {}'.format(a.first, a.last)

    def apply_raise(self):
        return self.pay * Employee.raise_amount

emp_1 = Employee('Test1', 'User1', 5000)
emp_2 = Employee('Test2', 'User2', 6000)
#  print(Employee.fullname(emp_2))
print(emp_1.pay)
print(emp_1.apply_raise())
print(emp_1.raise_amount)
print(Employee.raise_amount)
print(emp_1.__dict__)
print(Employee.__dict__)
