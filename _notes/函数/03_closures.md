# 函数对象 
在 Python 中, 一切皆对象, 当然包括函数

    @@@ python
    def foo():
        print('hello')

    # 既然是对象, 就可以将它赋值给一个变量
    bar = foo
    type(bar)

    # 打印出函数名字
    print(bar.__name__)

    # 通过调用这个变量来调用函数
    bar()

    # 也可以将它作为参数传递给另一个函数
    

# 闭包
## 步骤1:

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    def outer_func():
        message = 'Hi'

        def inner_func():
            print(message)

        return inner_func()

    outer_func()

首先看一下这段代码, 我们定义了一个函数 outer_func(), 它不接受任何参数, 在这个函数内, 第一行语句定义了 `message` 变量, 值 `Hi`.  
下面我们又定义了一个函数 `inner_func`, 同样不接受任何参数. `inner_func` 所做的就是打印出 `message` 这个变量, 这一这个变量我们名没有在 `inner_func` 函数体内定义, 所以它使用的是外层的 `message` 变量.  
最后我们执行 `inner_func()` 函数, 并把它的结果作为返回值返回给我们. 所以当我们执行 `outer_func` 函数时, 实际上执行了 `inner_func` 函数, 所以我们可以看到输出结果为 `Hi`.

## 步骤 2

现在修改一下代码, 在 `outer_func` 函数的最后, 我们直接执行了 `inner_func` 函数, 并返回这个函数的执行结果.

    @@@ python
    def outer_func():
        message = 'Hi'

        def inner_func():
            print(message)

        # 替换执行 inner_func 函数
        # 我们可以直接将这个函数作为 outer_func 返回值直接返回
        return inner_func

    # outer_func() 执行后没有任何输出, 说明 inner_func 没有被执行

    # 但是既然 outer_func() 函数将 inner_func 函数作为返回值给返回回来了
    # 我们当然可以使用另一个变量接收它的返回值
    my_func = outer_func() # 没有任何输出

    # 查看 my_func 类型, 确实是一个函数
    print(type(my_func))
    # 打印出函数的名字
    print(my_func.__name__)

    # 既然是一个函数, 我们就可以调用这个函数
    my_func()
    # 可以看到我们正确输出了 `Hi` 这条信息

    # 虽然我们已经从 outer_func 函数返回了,
    # 但是通过调用 inner_func 函数, 我们仍然可以访问到 outter_func 函数内的变量 message
    # 这就是 闭包 函数的能力

    # 我们也可以调用多次 my_func, 结果都是同样的.
    my_func()
    my_func()
    my_func()

## 步骤3
添加参数

    @@@ python
    def outer_func(msg):
        message = msg

        def inner_func():
            print(message)

        return inner_func

    say_hi = outer_func('hi')
    say_hello = outer_func('hello')

    say_hi()
    say_hello()
    # 可以看到这两个函数都能记住各自的 message 变量的值

## 步骤4
为 inner_func 添加参数

    @@@ python
        def outer_func(msg):
        message = msg

        def inner_func(name):
            print("{}, {}".format(message, name))

        return inner_func

    say_hi = outer_func('hi')
    say_hello = outer_func('hello')

    say_hi('zhang san')
    say_hello('li si')