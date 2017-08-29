<!SLIDE transition=turnUp>
# 模块

为了能够在我们的代码中使用其他库中的代码, 必须先要在我们的代码中引用这些库, 在 Python 中, 引用一个模块一共有两种主要语法:

## `import`

- `import importable`
- `import importable1, importable2, ..., importableN`
- `import importable as preferred_name`

`importable` 可以是一个模块名, 包名, 或是模块下的某一个包.

    @@@ python
    import requests
    import requests.api

.callout.info import 后只能引用到模块级别. 而不能引用模块中的某个方法

## `from...import...`

- `from importable import object1, object2, ..., objectN`
- `from importable import object as preferred_name`
- `from importable import *`

## 模块查找路径

当我们引用一个 Python 模块时, python 会在默认的路径下查找我们要引用的库, 可以通过 `sys.path` 打印出这些路径信息.

    @@@ python execute
    import sys
    print(sys.path)

我们可以通过设定环境变量 `PYTHONPATH` 来曾加搜索路径, `PYTHONPATH` 应该指向一个目录.

    @@@ bash
    export PYTHONPATH=/home/zlock/custom/modules

这样 `/home/zlock/custom/modules` 路径就会被放到 Python 的查找路径中, 它的位置紧跟在当前路径的下一个查找路径.

.callout.info 我们可以通过 `python -c 'import requests'` 语句快速检测一个模块是否存在.

## `__name__`

    @@@ python
    if __name__ == '__main__':
        suite

<!SLIDE transition=turnUp>
## Python 引用模块流程

当我们引用一个模块时, Python 首先查找 `模块名.pyo` 文件, 如果存在则引入该文件, 不存在, 则继续查找 `模块名.pyc` 文件, 存在则引入该文件, 若不存在, 则编译模块文件, 并引入模块.

![import modules](../_images/modules/import_modules.png)

## 编译 python 源码文件

我们可以使用 Python 的 `-m` 参数来手动编译 Python 源文件来生成一个字节码文件:

    @@@ shell
    python -m filename.py

如果指定了 `-O` 参数, 或是设置了 `PYTHONOPTIMIZE` 环境变量, 则在编译的过长中尝试进行优化操作.

如果指定了 `-B` 参数, 或是设置了 `PYTHONDONTWRITEBYTECODE` 环境变量, 则不会将生成的字节码文件保存到磁盘中.