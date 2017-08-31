<!SLIDE>
# `__future__` 模块

`__future__` 模块可以让我们在一个较低的 Python 版本中使用高版本中才有的某些功能, 或是将要在未来 Python 中增加的功能.

    @@@ python
    from __future__ import print_function
    print('no new line', end='')