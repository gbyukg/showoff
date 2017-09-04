<!SLIDE>
# 装饰器

装饰器是 Python 中的语法糖, 对某个函数定义一个装饰器函数, 在我们调用这个函数时, Python 会自动为我们调用这个装饰器函数, 并将函数名作为装饰器函数参数自动传递给装饰器函数. 并且装饰器函数必须返回一个函数.

在 Python 中通过使用 `@func_name` 为一个函数定义一个装饰器函数.

    @@@ python
    @decorator_func
    def my_func():
        pass

示例

    @@@ python
    def logger(func):
        def log_func(*args):
            print("Running {} with arguments {}".format(func.__name__, args))
            return func(*args)
        return log_func

    @logger
    def add(x, y):
        return x + y

    @logger
    def sub(x, y):
        return x - y

    print(add(4, 5))

## 带参数的装饰器

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

    add(3, 4)
    sub(5, 2)
