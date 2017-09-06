# 装饰器

    @@@ python
    def logger(func):
        def log_func(*args):
            print("Running {} with arguments {}".format(func.__name__, args))
            return func(*args)
        return log_func

    @logger
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    # 重命名 add_logger -> add
    add = logger(add)
    add(3, 4)

    # 重命名 sub_logger -> sub
    # sub = logger(sub)
    sub(7, 5)

## 定义装饰器函数
    @@@ python
    # 一个将闭包函数作为返回值的函数
    # Python 会自动将 add 函数作为参数传递给 logger() 函数
    @logger
    def add(x, y):
        ...

    @logger
    def sub(x, y):
        ...

    add(3, 4)
    # 此时 add 已经被替换
    # 输出 add 函数名
    print(add.__name__)

    sub(7, 5)
    print(add.__name__)

## functools
    @@@ python
    from functools import wraps
    def logger(func):
        # 使用 wraps
        @wraps(func)
        def log_func(*args):
            print("Running {} with arguments {}".format(func.__name__, args))
            return func(*args)
        return log_func


## 执行时间
如果给一个函数定义了一个装饰器函数, 这个装饰器函数在 Python 解释源码时就遇到函数的定义时就已经被执行了.

    @@@ python
    def logger(func):
        print(func.__name__)
        ...

    # 相当于执行了
    add = logger(add)
    sub = logger(sub)

# 带参数装饰器

    @@@ python
    def logger(level):
        def wrap(func):
            def log_func(*args):
                print("{}: Running {} with arguments {}".format(level, func.__name__, args))
                return func(*args)
            return log_func
        return wrap

    @logger('Info')
    def add(x, y):
        return x + y

    @logger('Warning')
    def sub(x, y):
        return x - y

    #  add_logger = logger(add)
    #  add_logger(3, 4)

    # 等价于
    #  unnamed_func = logger('info')
    #  add_logger = unnamed_func(add)
    #  add_logger(3, 4)

    add(3, 4)
    sub(5, 2)
