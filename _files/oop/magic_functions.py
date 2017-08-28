#!/usr/bin/env python
# encoding: utf-8

"""
documentation
"""

class Employee(object):

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        #  self.email = '{}.{}@company.com'.format(first, last)

        Employee.num_of_emps += 1

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

class Developer(Employee):
    raise_amount = 1.10 # 2

    def __init__(self, first, last, pay, prog_lang):
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super(Manager, self).__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

        self.index = 0

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->{}'.format(emp.fullname()))

    def __str__(self):
        return 'str'

    def __repr__(self):
        return 'repr'

    def __len__(self):
        return len(self.employees)

    #  def __getitem__(self, i):
        #  print('getitem')
        #  return self.employees[i]

    def next(self):
        if self.index < len(self):
            item = self.employees[self.index].fullname()
            self.index += 1
            return item
        raise StopIteration()

    def __iter__(self):
        return self

    def __getattr__(self, name):
        return 'getattr'

    #  def __setattr__(self, name, val):
        #  print('setattr {} = {}'.format(name, val))
        #  if not self.name:
            #  self.name = val

    #  def __getattribute__(self, name):
        #  return 'attribute'

dev_1 = Developer('Dev1', 'User1', 5000, "Python")
dev_2 = Developer('Dev2', 'User2', 6000, "Java")

mgr_1 = Manager('Sue', 'Smith', 9000, [dev_1])
mgr_1.add_emp(dev_2)
print(mgr_1.fullname)
mgr_1.fullname = 'John Smith'
del mgr_1.fullname
print(mgr_1.first)
print(mgr_1.last)
print(mgr_1.email)
#  mgr_1.print_emps()
#  print(len(mgr_1))
#  print(mgr_1[0].fullname())
#  for i in mgr_1:
    #  print(i)
#  print(next(mgr_1))
#  print(next(mgr_1))
#  print(next(mgr_1))
#  print(mgr_1.firsts)
#  mgr_1.age = 24
#  mgr_1.ages = 45
