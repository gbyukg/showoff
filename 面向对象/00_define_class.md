<!SLIDE transition=turnUp>
# 类的定义与类实例

## 定义类
关键字 `class` 用于定义一个类

格式为:

    @@@ python
    class ClassName(base_classes):
        '''class document'''
        suite

创建类时可以指定一个或多个要继承的父类 `base_classes`. 而 `object` 类是所有类的总父类, 也就是说, Python 中的所有类都继承自 `object` 类.

在创建一个类时, 我们还可以为该类创建说明文档, 通过三引号来创建类文档

示例:

    @@@ python
    class Employee(): pass

与定义函数一样, 需要先定义好类之后, 才能在后面的代码中使用.

## 实例化一个类

在 Python 中, 可以直接通过类名来创建一个类实例, 而无需使用 `new` 关键字.

    @@@ python
    emp_1 = Employee()
    emp_2 = Employee()

<!SLIDE transition=turnUp>
## 实例属性和方法

实例属性属于每个单独实例的私有属性, 各个实例之间的属性是相互独立存在的, 互不影响.

Python 支持动态添加实例属性, 这意味着当我们创建好一个实例后, 可以直接为实例自由地创建任何属性, 而无需预先在类中定义好.  
Python 中通过句点 `.` 来访问实例中的属性:

    @@@ python
    emp_1.property = Value

## 构造函数

如果一个类定义了构造函数, 当创建这个类的实例时, 构造函数会自动被 Python 调用, 我们通常在构造函数中用来初始化一些属性. 在 Python 中, 使用固定的命名来创建一个构造函数:

构造函数至少接收一个参数 `self`, 用来表示类实例自身

    @@@ python
    def __init__(self): pass

## 方法

与创建普通函数一样, 使用关键字 `def` 为类定义一个方法

    @@@ python
    def method(self): pass

与构造函数一样, 类中的方法也至少需要一个 `self` 参数, 作为对实例自身的引用.

.callout.info `self` 并不是 Python 中的关键字, 使用 `self` 只是所有 Python 开发者的默认协议, 我们可以使用任何自定义变量来代替.