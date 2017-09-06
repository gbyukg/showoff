<!SLIDE transition=turnUp>
# 函数的定义
Python 中定义函数非常简单, 只需要使用 def 关键字即可

## 语法

    @@@ python
    def functionName(parameters):
        '''function help document'''
        suite

一旦我们定义了一个函数后, 就可以在定义函数后的任何代码中调用该函数了, 格式为

    @@@ python
    functionName(parameters)

.callout.warning 由于 Python 是解释性语言, 解释顺序由上至下, 因此在调用一个函数前一定要先定义好这个函数.

## 函数帮助文档

在定义函数时, 可以使用 `'''` 为函数定义帮助文档信息.通过 `functionName.__doc__` 可以获取帮助文档信息.

<!SLIDE transition=turnUp>
# 函数的返回值

当定义一个函数时, 我们无需声明函数返回值的类型,

在 Python 中, 所有的函数都有且只有一个返回值, `return` 关键字用来终止函数的执行, 并将 return 后的表达式结果(任意类型)作为函数的返回值返回给函数的调用者. 如果 `return` 后面没有提供任何参数, 或执行到函数体结尾时自动退出函数, 函数也将同样返回 `None`.  

.callout.info Python 中的 `None` 与其他编程语言中的 `null` 类似, 表示什么都没有.

<!SLIDE transition=turnUp>
# 函数的参数

定义函数时, 可以指定函数可以接收的参数, 参数个数可以为为 0 个, 也可以为多个, 各个参数之间用逗号(`,`)分隔.

调用函数时, 提供给函数的参数个数一定要与定义时的个数保持一致, 否则会抛出 `TypeError` 异常.

在这种情况下, 函数中的参数是通过参数的位置进行传递的.

## 带默认值的参数

    @@@ python
    def cal_sum(a, b, c=5): pass

在定义函数时, 如果指定了带默认值的参数, 则在调用该函数时, 带有默认值的参数可以忽略不写.

带默认值的参数一定要放到没有默认值的参数后面, 否则会报出语法错误.

.callout.warning 当定义函数时指定了带有默认值的参数时, 带默认值的参数必须放到没有默认值的参数后面.

<!SLIDE transition=turnUp>
# 小心可变类型作为参数的默认值

    @@@ python
    def append_if_event(x, lst=[]):
        if x % 2 == 0:
            lst.append(x)
        return lst
    print(append_if_event(2))
    print(append_if_event(3))
    print(append_if_event(4))
    print(append_if_event(6, []))

Python 中参数的默认值是在函数编译的时候就已经确定好了的, 而并不是在每次调用的时候重新创建的, 所以每次调用函数的时候指向的都是同一个在编译时定义好了的对象.  
当在函数体内修改这个可变类型参数的默认值时, 每次修改的都是同一个对象.  
而不可变类型在每次修改后都会重新生成一个新的对象, 所以不可变类型作为参数的默认值不会有任何问题.

解决

    @@@ python
    def append_if_event(x, lst=None):
        if lst is None:
            lst = []
        if x % 2 == 0:
            lst.append(x)
        return lst
    print(append_if_event(2))
    print(append_if_event(3))
    print(append_if_event(4))
    print(append_if_event(6, []))

<!SLIDE transition=turnUp>
# 定义参数可变的函数

- `*` 用来保存所有未命名的参数, 元组类型
- `**` 用来保存所有命名的参数, 字典类型, 格式为: {参数名:参数值}

示例:

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    def product(a, b=1, *args, **kargs):
        print('a: {}'.format(a))
        print('b: {}'.format(b))
        # 除去前两个参数 a 和 b
        # 所有剩余的未命名的参数全部存储到 args 变量中
        # 而所有带参数名的参数将全部传递给 kargs 变量中
        for arg in args:
            print(arg)
        for key,val in kargs.items():
            print('{}: {}'.format(key, val))

    #  product(1, 2, 3, 4, x='5', y='6', z='7')

    # 还可以将元组和字典直接作为参数传递给函数
    param1 = ('a', 'b', 'c')
    param2 = {'m': 'm', 'n': 'n'}
    product(1, 2, *param1, **param2)
    # 如果没有指定 a, b 两个参数
    product(*param1, **param2)