# 装饰器

    @@@ python
    def logger(func):
        def log_func(*args):
            print("Running {} with arguments {}".format(func.__name__, args))
            return func(*args)
        return log_func

    # 一个将闭包函数作为返回值的函数
    # Python 会自动将 add 函数作为参数传递给 logger() 函数
    @logger
    def add(x, y):
        return x + y

    @logger
    def sub(x, y):
        return x - y

    #  add_logger = logger(add)
    #  add_logger(3, 4)
    #  sub_logger = logger(sub)

    #  print(add_logger(3, 4))
    #  print(sub_logger(5, 2))

    print(add(4, 5))

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
