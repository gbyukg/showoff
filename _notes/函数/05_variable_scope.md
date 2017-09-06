# 变量的可见度
    @@@ python
    # 定义全局变量
    x = 'global x'

    def foo():
        # 定义局部变量
        y = 'local y'
        print(x)
        print(y)

    foo()
    print(x)
    # 如果输出 print(y) 报错
    # 不难理解

## 覆盖全局变量
    @@@ python
    def foo():
        # 局部变量覆盖了全局变量
        x = 'local x'
        y = 'local y'
        print(x)
        print(y)
    foo()
    # 但是不会影响全局变量
    print(x)

## 修改 x 变量
    @@@ python
    def foo():
        # 尝试修改代码
        x += ' change'
        # 或
        x = x + ' change'
        # 提示错误
        # 本地变量 x 在声明前被引用了(第二个x)
        # 这句话说明当前 x 是一个本地变量
        # 但是在等号右边我们使用了 x 变量
        # 这时候 x 还没有被赋值

## 使用 global 修改全局变量
    @@@ python
    def foo():
        # 明确声明, x 是全局变量
        global x

        x = x + ' change'
        # 因为此时 x 代表的已经是全局变量了
        # 所以这句话同时修改了全局变量

# locals() 和 globals()

    @@@ python
    x = 'global x'

    def test():
        y = 'local y'
        # 获取当前的局部变量
        print(locals())
        # 获取全局变量
        print(globals())

        print(globals()['x'])

        # 2: 还可以直接向里面添加元素
        globals()['name'] = 'test'

    test()
    print(globals()['name'])
    print(name)
