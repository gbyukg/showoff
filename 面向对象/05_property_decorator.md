<!SLIDE>
# 属性装饰器

属性装饰器可以让我们想访问对象中的属性那样调用某个方法, 而不用在调用方法的时候使用括号(`()`)来执行方法.

创建属性装饰器非常简单, 只需要在定义方法的上一行使用 `@property` 即可.

    @@@ python
    @property
    def func(self):
        suite

# setter 装饰器

通过属性装饰器, Python 允许我们像访问属性那样调用对象中的方法, 而通过 setter decoraotr, Python 允许我们像为属性赋值那样使用赋值语句来调用某个方法, 并将赋值语句右边的值作为参数传递给这个方法.

    @@@ python
    @func_name.setter
    def func_name(self, val):
        suite

调用 `func_name` 方法时看起来就像: `obj.func_name = 'value'`

# deleter 装饰器

与 setter 装饰器对应的, 还有一个 deleter 装饰器, 如果为某个方法设置了 deleter 装饰器, 当使用 `del obj.func_name` 时, 名为 `func_name` 的方法就会被调用.

    @@@ python
    @func_name.deleter
    def func_name(self):
        suite