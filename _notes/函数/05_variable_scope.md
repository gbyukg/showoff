# 变量的可见度

    @@@ python
    x = 'global x'
    pwd = 'zzl'

    def test():
        y = 'local y'

        # 2: 局部变量的定义覆盖全局变量
        #  x = 'local x'

        # 3: 指明要访问的是全局变量
        # 从这段代码可以看出, 当直接访问变量 x 时, 调用的其实是全局变量 x,
        # 但是当重新为 x 赋值后, 实际是定义了一个新的局部变量 x.
        # 当我们想要在函数内明确指定要修改一个全局变量时
        # 可以使用 global 关键字先明确声明这个变量是一个全局变量
        #  global x
        #  x = 'local x'

        # 3: 修改全局变量
        x = 'local x'
        print(x)
        print(y)

    test()
    print(x)

    # 访问局部变量, 报错
    #  print(y)

# locals() 和 globals()

    @@@ python
    x = 'global x'

    def test():
        y = 'local y'
        print(locals())
        print(globals()['x'])

        # 2: 还可以直接向里面添加元素
        globals()['name'] = 'zzl'

    test()
    # print(name)
