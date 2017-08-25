<!SLIDE transition=turnUp>
# 类属性

不同于实例属性, 类属性可以被所有实例和类方法所共享, 在类的方法外定义的变量都是类属性.

    @@@ python
    class ClassName():
        kls_attr = value;
        ...

类属性既可以通过类名来访问, 还可以通过某个实例名访问

    @@@ python
    ClassName.kls_attr
    instanceName.kls_attr
