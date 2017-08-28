# `__name__`

## 创建 first_module.py

    @@@ python
    # 当我们在看别人编写的代码时, 经常会看到这样的判断
    def main():
        pass

    if __name__ == '__main__':
        main()

    # 这个是什么意思呢?
    # 首先让我们注释掉这段代码
    # 直接输出 __name__ 看看结果是什么

    print(__name__)
    # 可以看到执行的结果就是 __main__
    # 当 Python 在执行一段代码前
    # 会提前设置好一些特殊变量
    # 其中 __name__就是其中的一个特殊变量
    # 当我们直接执行一个 Python 文件时
    # __name__ 变量的值就会被设置为 __main__
    # 而当我们将一个 Python 文件作为一个模块来导入时
    # __name__ 的值就会被设置为文件名

## 创建 second_module.py

    @@@ python
    #!/usr/bin/env python
    # encoding: utf-8
    # 新增加一个文件: second_module.py
    import first_module
    # 修改第一个文件内容:
    print('First module\'s Name: {}'.format(__name__))
    # 执行代码
    # 结果显示 first module 为 first_module
    # 这是因为 first_module 文件时通过 seconde_module 文件执行的
    # 这种情况下, __name__ 就被设置成了 文件名

    # 在 second_module.py 文件中增加
    print('Second module\'s Name: {}'.format(__name__))
    # 执行脚本
    # 此时 second module 为 __main__
    # 因为这个文件时直接通过 Python 来执行的.

## 说明

    @@@ python
    # 删掉这段代码的注释
    def main():
        pass

    if __name__ == '__main__':
        main()
    # 现在我们就应该清楚了
    # 这段代码的意思就是
    # 当这个文件时直接被 Python 执行
    # 而不是以模块的形式被其他文件引入的时候
    # 执行 main() 这个函数
    # 因此把代码
    # print('First module\'s Name: {}'.format(__name__))
    # 放到 main() 函数中
    def main():
        print('First module\'s Name: {}'.format(__name__))
    # 再次执行 first_module.py 文件
    # 可以看到输出
    # 当执行 second_module.py 文件时
    # first_module 中的输出语句将不再被执行了.
    # 当我们开发一个模块的时候
    # 经常使用这种方式来写一些测试用例
    # 或者是只有被 Pyton 直接执行的时候才想要运行的语句
    # 都可以放到这个判断里