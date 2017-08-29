# import 库
让我们自定义一个简单的 Python 模块 `my_module.py`, 通过引用这个库来看一下 Python 中 import 的使用方法

    @@@ python
    # 首先在行首输出一段内容
    print("imported my_module...")

    # 定义一个变量
    test = 'Test String'

    # 定义一个简单的函数, 用来搜索列表中是否存在某个特定的值
    def find_index(to_search, target):
        for i, value in enumerate(to_search):
            if value == target:
                return i

        # 如果没有找到, 则返回 -1
        return -1

并且在当前目录下定义另一个 Python 文件 `intro.py`

    @@@ python
    # 首先在这个文件中定义一个列表
    courses = ['History', 'Math', 'Physics']

现在, 如果我们想要使用 my_module 中的 find_index 方法. 必须使用 `import` 语句将这个模块导入到我们当前代码中.

    @@@ python
    # 使用 import 语句来引入这个模块
    import my_module

当我们使用 `import` 语句导入某个模块时, 实际上被导入的这个模块中的代码会被全部执行, 所以当我们执行代码后, 会看到 `my_module` 中的这条输出语句, 这也是为什么 `import` 语句可以导入其他模块中的变量和方法的原理. 实际上就是执行了一遍被导入模块中的方法.

当我们通过这种方式来导入一个模块之后, 并不能直接调用被导入模块中的方法或变量, 而是必须要通过`模块名.函数/变量` 的方式来使用.

    @@@ python
    # 输出 test 变量
    print(my_module.test)

    # 调用 find_index() 函数
    index = my_module.find_index(courses, 'Math')
    print(index)

## 通过 as 设定别名
如果我们在代码中需要调用很多次 `find_index()`  方法, 每次都要使用 `my_module.find_index()` 的方式来访问这个函数, 或是当前代码中定义了 `my_module` 变量, 比如:

    @@@ python
    my_module = 5

这时候在使用 `my_module.find_index()` 的方式访问这个变量时, 就会提示错误.

解决方法就是为这个模块指定别名, 在使用 `import` 语句导入一个模块时, 我们同时还可以使用 `as` 给这个模块指定一个别名, 如:

    @@@ python
    import my_module as mm
    # 这时候, 我们就可以使用 mm 来代替 my_module 了

    # 修改 my_module 为 mm
    print(mm.test)
    print(mm.find_index(courses, 'Math'))
    # 现在一切就有正常了

# `from ... import ...`
除了上面这种方式外, Python 还支持我们只导入模块中的某一个或某些方法或变量, 格式为 `from...import...`, 如:

    @@@ python
    # 更改 import 语句
    from my_module import find_index

    # 通过这种方式导入的方法或变量
    # 我们可以在代码中直接使用
    # 而不需要在使用模块名或别名作为前缀了
    # 修改 mm.find_index()
    # 删掉 mm
    print(test)
    index = find_index(courses, 'Math')

    # 执行代码
    # 提示我们一个错误, 说 test 是未定义变量
    # 这说明通过这种方式导入模块中的方法或是变量时
    # 只有指定的方法或是变量才会被导入进来

    # 把 test 变量追加到 import 语句中
    # 多个变量和方法之间, 使用逗号分隔开
    from my_module import find_index, test
    # 再次执行, 代码可以被成功执行了

其实我们还可以让代码变的更简单一些, 还是通过 as 设定别名的方式:

    @@@ python
    # 给 find_index 函数设置一个别名
    from my_module import find_index as fi, test

    # 替换掉 find_index
    index = ff(courses, 'Math')

## import *
使用 `from...import...` 这种方式时, 如果我们想要从模块中的很多方法或是变量时, 必须得把所有这些需要导入进来的方法和函数名全都写到 import 语句中, 其实还有一种更简单的方式, 使用 `*` 来导入模块中的所有方法和变量, 

    @@@ python
    # 使用 * 来调用所有
    from my_module import *

但是尽量不要使用这种方式, 如果被导入的库很大的话, 很容易造成混乱, 或者是造成命名冲突.

## __all__

    @@@ python
    # 在 my_module.py 中使用
    __all__ = ['find_index', 'test']

# 模块查找路径
当我们导入一个模块时, Python 是怎么找到这些模块的呢? 或者说 Python 在哪些路径下查找这些模块呢?

如果我们引用的一个模块不是 Python 的内置模块, Python 会按照 `sys.path` 中的顺序依次查找库

    @@@ python
    import sys
    print(sys.path)

可以看到, Python 第一个查找路径是当前 python 脚本所在的路径, 这个跟在哪个目录下执行的这个脚本没有关系, 无论是在那个路径下执行的, 得到的都是一样的结果.

我们可以通过向这个路径附加一些路径信息来增加查找路径:

    @@@ python
    sys.path.append('/Users/gbyukg/Desktop')

但是这样写对代码的可移植性造成影响. 另一个可行的方法是设置 `PYTHONPATH` 环境变量.

在 Python 中, 重复导入模块多次, 或是回环导入模块(比如模块A中引入了模块B, 而在模块B中又引用了模块A)不会引起任何问题, 因为 Python 在每次导入模块之前会首先查看模块是否已经被导入过, 一旦确定某个模块在当前生命周期中已经被导入, 则不会再次导入该模块了.

# `__name__`
当我们在看 Python 源码的时候, 发现很多文件最下面都有类似这样的代码:

    @@@ python
    if __name__ == '__main__':
        suite

当 Python 解释器解释执行一段源码文件前, 首先会定义一些特殊的变量, `__name__` 就是其中的一个属性, 我们可以直接打印出这个属性.

    @@@ python
    print(__name__)
    # 执行代码, 输出结果是 `__main__`

现在同样在 `my_module.py` 文件中输出这句话, 看一下结果是什么?

    @@@ python
    # 为了便于观察, 多输出一些信息
    print('the value of name in my_module is: {}'.format(__name__))

再次执行 `intro.py` 程序, 可以看到输出结果是 `the value of name in my_module is: my_module`. `__name__` 的值有两种结果:

- 当 Python 文件直接被执行时, 它的值是 `__main__`
- 当 Python 文件被当做一个模块引用时, 它的值就是模块名

所以这个判断的意思就是: 当这个文件被 Python 直接调用执行时, 就执行判断里的语句. 这段代码里面一般都是用来测模块的测试用例的.

# Python 引用模块流程
如果我们查看当前文件夹下的文件, 会发现多了一个 `.pyc` 的文件.

当 python 引入一个模块时, 首先会查找模块编译后的字节码文件 `模块名.pyo`, 这是一个优化后的模块的字节码文件, 如果找到该文件, 并且该文件的修改日期大于模块源文件(即.py)文件的修改日期, 则直接导入这个 pyo 文件.  
如果没有发现该文件, 则继续尝试查找名为 `模块名.pyc` 文件, 这是一个没有经过优化的模块的字节码文件, 如果找到该文件, 并且该文件的修改日期大于模块源文件的修改日期, 则直接引入该文件.  
如果没有发现该文件, Python 则尝试编译模块源文件来生成 `pyc` 或是 `pyo`, 最终引用编译后的字节码文件.

Python 之所以要先编译成字节码文件, 就是为了性能, 字节码文件可以直接被 Python 拿来运行, 免去了编译那一步, 并且字节码文件放到任何有相同版本的 Python 机器上, 都可以直接运行. 可以查看一下这个字节码文件的内容.

# 编译 python 源码文件
我们也可以手动编译一个 Python 文件: `python -O -m python_file.py`, `-O` 指定在生成字节码文件的同时进行优化, 也可以通过设置 `PYTHONOPTIMIZE` 环境变量达到同样的效果.  
如果指定了`-B` 参数将不会在磁盘上保存生成的字节码文件, 设置 `PYTHONDONTWRITEBYTECODE` 环境变量可以达到同样的效果.

使用编译后的字节码文件最大的优势就是提高执行速度, Python 在引入这些文件后, 无需在经过编译过程, 而可以直接使用. 同时也可以保护 Python 源码不被泄漏(虽然也有反编译软件).