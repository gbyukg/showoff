# `type()`

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    class A(object): pass
    class B(object): pass

    a = A()
    b = B()

    print(type(a), type(a))
    # 旧式类中, type(a) 永远等于 type(b)
    print(type(a) == type(b))

# 继承顺序
## 旧式类

    @@@ python
    class C: i = 0
    class C1(C): pass
    class C2(C): i = 2
    class C12(C1, C2): pass
    class C21(C2, C1): pass

    assert C12().i == 0
    assert C21().i == 2

## 新式类

    @@@ python
    class C(object): i = 0
    class C1(C): pass
    class C2(C): i = 2
    class C12(C1, C2): pass
    class C21(C2, C1): pass

    print(C12().i)
    print(C21().i)
    print(C12.__mro__)
    print(C21.__mro__)
