<!SLIDE transition=turnUp>
# 类方法

与定义类方法格式相同, 使用 `@staticmethod` 来定义一个静态方法

    @@@ python
    class ClassName():
        @staticmethod
        def static_method(params):
            suite

当调用类的静态方法时, Python 不会传递任何参数给它, 因此在定义静态方法时, 我们不需要定义任何特殊的参数

当我们定义的方法中不需要访问任何类属性或实例属性时, 就可以考虑使用静态方法来实现我们的需求了.