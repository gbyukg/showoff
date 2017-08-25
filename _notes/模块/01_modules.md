# request 库

    @@@ python
    #!/usr/bin/env python
    # encoding: utf-8

    # http://www.python-requests.org/en/master/
    # requests 是python的一个第三方库
    # 它提供了很多方法, 可以让我们很方便的发送一个 HTTP 请求
    # 要是使用这个库, 我们需要先导入这个库
    # 最简单的方式就是:
    import requests
    # 一旦导入这个库后, 我们就可以使用这个库里的所有方法了
    # requests 库中提供了一个 get() 方法
    # 这个方法用来向指定的 URL 发送一个 HTTP 请求
    # 调用 requests 中的 get() 方法
    requests.get('https://api.github.com')
    # get() 方法返回一个对象, 包含了很多属性
    # 其中有一个叫 text 的属性
    # 保存了 URL 返回的信息
    # 我们可以将 get() 返回的对象付给一个变量
    response = requests.get('https://api.github.com')
    # 在打印出 text 里的内容
    print(response.text)

# 一行中同时引用多个模块
    @@@ python
    import requests, os
    # 之后就可以使用 os 库中的方法了
    print(os.path)

    # 但是不建议这么写, 最好是每行引入一个模块
    # 这样看起来比较清晰
    # 而且在引用包的时候
    # 一般是先引用 Python 自带的库
    # 在引用第三方库
    # 最后引用自定义的模块或包

# request.api

    @@@ python
    # 我们还可以指定引用包中的某个模块
    # 比如:
    import requests.api
    # 只引用 requests 包中的 api 模块
    # 这样我们只能访问 requests 包中的 api 模块下的方法
    # get() 方法就是存在于 api 模块下的
    # 同时需要修改调用 get() 方法的方式
    # 因为我们引用的是 requests.api
    # 所以调用的时候也要使用 requests.api 来调用
    response = requests.api.get('https://api.github.com')
    print(response.text)

# 别名

    @@@ python
    # 但是每次这样写很麻烦
    # 在引用完一个模块后
    # 我们还可以为它设置一个别名
    import requests.api as rapi
    # 当我们设置完别名后
    # 就可以使用别名来引用模块中的方法了
    response = rapi.get('https://api.github.com')
    print(response.text)
    # 可以看到是同样的效果

    # 也可以为 os 模块设置别名
    import requests.api as rapi, os as sysos

    @@@ python
    # 只能引用到模块级别, 而不能指定模块中的方法
    import requests.api.get
    # 将会报错, 提示无法找到 get 模块

# `from...import` 语句

    @@@ python
    # Python 也允许我们使用 from...import 语句来只导入某个模块中的某个或多个特定方法
    # 如果是通过这种方式导入的方法
    # 在我们的程序中就可以直接调用导入的这个方法, 而不用再使用包名或模块名来引用了.
    # 比如:
    from requests import get
    # 这句话告诉Python从requests包中引入 get() 方法
    # 这样在我们的代码中就可以直接调用 get() 方法了
    response = get('https://api.github.com')
    print(response.text)

    # 当然我们也可以同时引用多个方法
    from requests import get, post

# `from...import` 别名

    @@@ python
    from requests import get
    # 在引入某个特定方法时, 还可以为这个要引入的方法指定一个别名

    # 在这个例子中, 我们直接将 requests 库中的 get() 方法引入到了我们的文件中
    # 这就相当于将 requests 中的 get() 的定义引入到了我们的代码中
    # 但是如果当前我们的文件中也有一个 get() 方法, 会怎么样呢?
    # 编写一个自己的 get() 函数
    def get(url):
        print('url')

    response = get('https://api.github.com')
    print(response.text)
    # 执行程序
    # 输出了 'url'
    # 这说明我们自定义的 get() 函数覆盖了 requests 中的 get() 方法

## 别名

    @@@ python
    # 为了不让我们引入的方法与我们现有的方法发生冲突
    # 在引入包中的方法时, 我们可以同时为这个方法指定一个别名
    from requests import get as r_get
    # 这样在下面的代码中
    # 我们就可以使用 r_get 当做 requests 中的get方法的别名来调用了
    def get(url):
        print('url')
    # 修改 get->r_get
    response = r_get('https://api.github.com')
    print(response.text)

## 引用所有方法
    @@@ python
    # 我们还可以在 import 后面使用*来表示引用模块中的所有方法
    from requests import *
    response = get('https://api.github.com')
    print(response.text)

# 库路径查找

当我们引用一个模块时, 如果不是 Python 的内置模块, Python 会按照 `sys.path` 中的顺序依次查找库

在 Python 中, 重复导入模块多次, 或是回环导入模块(比如模块A中引入了模块B, 而在模块B中又引用了模块A)不会引起任何问题, 因为 Python 在每次导入模块之前会首先查看模块是否已经被导入过, 一旦确定某个模块在当前生命周期中已经被导入, 则不会再次导入该模块了.

# Python 引用模块流程
当 python 引入一个模块时, 首先会查找模块编译后的字节码文件 `模块名.pyo`, 这是一个优化后的模块的字节码文件, 如果找到该文件, 并且该文件的修改日期大于模块源文件(即.py)文件的修改日期, 则直接导入这个 pyo 文件.  
如果没有发现该文件, 则继续尝试查找 `模块名.pyc` 文件, 这是一个没有经过优化的模块的字节码文件, 如果找到该文件, 并且该文件的修改日期大于模块源文件的修改日期, 则直接引入该文件.  
如果没有发现该文件, Python 则尝试编译模块源文件来生成 `pyc` 或是 `pyo`, 最终引用编译后的字节码文件.

# 编译 python 源码文件
我们也可以手动编译一个 Python 文件: `python -O -m python_file.py`, `-O` 指定在生成字节码文件的同时进行优化, 也可以通过设置 `PYTHONOPTIMIZE` 环境变量达到同样的效果.  
如果指定了`-B` 参数将不会在磁盘上保存生成的字节码文件, 设置 `PYTHONDONTWRITEBYTECODE` 环境变量可以达到同样的效果.

使用编译后的字节码文件最大的优势就是提高执行速度, Python 在引入这些文件后, 无需在经过编译过程, 而可以直接使用. 同时也可以保护 Python 源码不被泄漏(虽然也有反编译软件).