<!SLIDE >
# Python 代码

    @@@ python
    #!/usr/bin/env python
    # encoding: utf-8

    # Copyright 2015 The TensorFlow Authors. All Rights Reserved.
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    # ==================================================================

    """当前模块说明文档."""

    foo = 'foo'

    class FooClass(object):
        """
        Foo class 文档说明.
        """

        def __init__(self, name):
            """构造函数
            用于做类的初始化操作
            """
            self.name = name

        def get_name(self):
            # 当名字被定义时, 打印出名字
            if self.name:
                print(self.name)
            else:
                print("No name.")

        def get_character_of_name(self):
            for c in self.name:
                print(c)

    # 实例化类, 并传递一个名字字符串给 FooClass 类
    myFoo = FooClass('Smith')

    # 调用实例方法 get_name()
    myFoo.get_name()
    myFoo.get_character_of_name()