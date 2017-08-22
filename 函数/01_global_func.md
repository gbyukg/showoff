<!SLIDE transition=turnUp>
# 函数的定义

## 语法

    @@@ python
    def functionName(parameters):
        '''function help document'''
        suite

通过 Python 中的关键 `def` 来定义函数

    @@@ python
    def cal_sum(a, b, c):
        return a + b + c

一旦我们定义了一个函数后, 就可以在定义函数后的任何代码中调用该函数了, 格式为

    @@@ python
    func_name(parameters)

.callout.warning 由于 Python 是解释性语言, 解释顺序由上至下, 因此一定要先定义函数之后, 之可以调用这个函数.

## 函数帮助文档

在定义函数时, 可以使用 `'''` 为函数定义帮助文档信息.通过 `functionName.__doc__` 获取帮助文档信息.

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

## 小心可变类型作为参数的默认值

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
# 函数的返回值

在 Python 中, 所有的函数都有一个返回值, `return` 关键字用来终止函数的执行, 并将提供给 return 的参数返回给函数的调用者. 如果 `return` 后面没有提供任何参数, 或函数体中没有 `return` 关键字, 函数将返回 `None`.  
`None` 与其他编程语言中的 `null` 类似, 表示什么都没有.

<!SLIDE transition=turnUp>
# 定义参数可变的函数

    @@@ python
    def product(a, b=1, *args, **kargs):
        print('a: {}'.format(a))
        print('b: {}'.format(b))
        for arg in args:
            print(arg)
        for key,val in kargs.items():
            print('{}: {}'.format(key, val))

    product(1, 2, 3, 4, x='5', y='6', z='7')

- `*` 用来保存所有未命名的参数, 元组类型
- `**` 用来保存所有命名的参数, 字典类型, 格式为: {参数名:参数值}

<!SLIDE transition=turnUp>
# 变量作用范围

当我们在一个函数体内定义一个变量时, 只有在函数内才可以访问这个变量, 函数外是无法访问的.

函数体内定义的变量会覆盖全局变量

当访问一个函数体内没有定义的变量时, Python会尝试访问全局变量, 可以使用 `global` 关键字明确指定使用全局变量

    @@@ python
    a = 1
    print(id(a))
    b = 2
    print(id(b))
    l = [0, 1]

    def set_val():
        global a
        print(id(a))
        a = 3
        b = 3
        print(id(b))
        l[0] = 'x'
        print('inside: {}'.format(a))
        print('inside: {}'.format(l))

    set_val()
    print('outside: {}'.format(a))
    print('outside: {}'.format(l))

<!SLIDE transition=turnUp>
# 闭包

在 Python 中, 可以在一个函数体内定义另一个函数, 外部函数返回内部函数, 这就是闭包

    @@@ python
    def func_outside():
        outside_a = 1
        outside_b = 2
        def func_inside():
            nonlocal outside_b
            inside_b = 2
            print('inside a : {}'.format(outside_a))
            print('inside b id: {}'.format(id(outside_b)))
            print('inside b : {}'.format(inside_b))
        print('outside a : {}'.format(outside_a))
        print('outside b id: {}'.format(id(outside_b)))
        return func_inside

    inside = func_outside()
    inside()
