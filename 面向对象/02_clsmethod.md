<!SLIDE transition=turnUp>
# 常规方法

一个常规方法就是定义在类中的一个普通方法, Python 会自动将实例本身作为第一个参数传递给常规方法, 我们用 `self` 来表示.  
可以通过类实例来调用方法.

    @@@ python
    def method(self):
        suite

<!SLIDE transition=turnUp>
# 类方法

定义类方法非常简单, 在常规方法声明的上面使用 `@classmethod` 即可定义了一个类方法.

    @@@ python
    class ClassName():
        @classmethod
        def cls_method(cls, params):
            suite

类方法即可以被类调用, 也可以被某个实例所调用.  
当一个类方法被调用时, Python 会自动将类自身作为第一个参数传递给这个方法, 因此类方法必须至少接受一个参数, 我们通常用 `cls` 来捕获.  
除了又 Python 自动传递的 `cls` 参数外, 类方法还可以接收 0 或任意个自定义参数.

    @@@ python
    ClassName.cls_method()

.callout.info 与 `self` 类似, `cls` 并不是 Python 中的关键字, 使用他只是 Python 程序员的一种默认规则.