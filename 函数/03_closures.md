<!SLIDE>
# 函数对象
在 Python 中, 一切皆对象, 包括函数, 因此我们可以将函数赋值给一个变量, 也可以将一个函数变量作为参数传递给其他函数

    @@@ python
    def foo():
        print('foo')

    def bar(func):
        func()

    my_var = foo

    # 作为参数传递给其他函数
    bar(my_var)

<!SLIDE>
# 闭包

在 Python 中, 我们可以在一个函数体内定义另一个函数, 当这个外部函数将内部函数作为返回值返回时, 这就是闭包

    @@@ python
    def logger(func):
        def log_func(*args):
            print("Running {} with arguments {}".format(func.__name__, args))
            return func(*args)
        return log_func

    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    add_logger = logger(add)
    sub_logger = logger(sub)

    print(add_logger(3, 4))
    print(sub_logger(5, 2))

.callout.warning Python3 为我们提供了 `nonlocal` 关键字, 在闭包函数中, 通过 `nonlocal` 关键字可以明确声明一个变量是外部函数的变量.