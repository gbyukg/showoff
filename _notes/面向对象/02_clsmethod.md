# classmethod

    @@@ python
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

# 添加类方法 set_raise_amount()

    @@@ python
    # 继续修改我们的这个类
    # 我们已经有了类属性 raise_amount,
    # 现在我们希望可以有个方法能够修改这个值
    # 创建一个新的类方法 set_raise_amount
    # 这个方法应该能接收一个数值作为参数,
    # 用来更新 raise_amount 的值

    @classmethod
    # 当我们调用类方法时, Python 会自动将类本身作为第一个参数传递给类方法
    # 这里我们使用 cls 来接收这个参数
    def set_raise_amount(cls, amount):
        # 在这里编写更新 raise_amount 值的代码
        # 我们可以用传递过来的 cls 参数来引用类属性
        cls.raise_amount = amount

# 类名调用类方法

    @@@ python
    # 当定义好类方法后, 我们可以直接通过类名来调用类方法
    Employee.set_raise_amount(1.05)
    # 输出 raise_amount
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    # 效果是一样的
    Employee.raise_amount = 1.05

# 类实例调用类方法

    @@@ python
    # 现在让我们尝试直接用实例去调用这个方法
    emp_1.set_raise_amount(1.08)
    print(Employee.raise_amount)
    print(emp_1.raise_amount)
    print(emp_2.raise_amount)
    # 使用实例调用类方法没有任何问题
    # 并且也正确修改了类变量
    # 说明类方法既可以被类调用, 也可以直接被实例调用

# 继续完善

    @@@ python
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
