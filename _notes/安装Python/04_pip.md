# pip

至此我们已经安装好 Python 了, 有了基本的开发环境, 但这还不够, 在大部分开发过程中, 我们会使用很多 Python 的第三方库, Python 为我们提供了很好的包管理工具, 这就是 `pip`, 使用它, 我们可以快速地安装或更新 Python 库.

    @@@ bash
    # 第一步 查看pip的帮助文档信息
    pip help
    # 可以看到一系列的子命令

    # 同样也可以查看某个子命令的帮助信息
    pip help install
    # 或
    pip install -h

    # 现在我们想要安装 requests 库
    # 可以使用 search 命令查找这个库先
    pip search requests
    # 可以看到很多结果
    # 或是过滤一下查找结果
    pip search requests | grep -i '^requests '

    # 当找到我们需要的库时, 就可以使用 install 命令安装这个库了
    pip install requests

    # 使用 list 命令查看当前系统中安装了哪些库
    pip list

    # 使用 show 命令查看某个以安装库的信息
    pip show requests
    # 使用 -v 参数查看更多的详细信息
    pip show -v/--verbose requests

    # 使用 uninstall 命令来删除某个库
    pip uninstall requests
    # 删除以后, 可以再次使用 list 命令查看当前系统中的包, 发现已经没有了

    # 刚才我们使用 install 命令安装 request 库时,
    # pip 会默认为我们安装最新的版本
    # 其实我们在安装某个库的时候, 还可以安装特定的版本
    pip install requests==2.0.0
    pip list
    # 安装大于版本号大于 2.0.0 的版本
    pip install requests>=2.0.0

# requirement file

当我们开发的一个项目需要很多依赖库, 当把这个项目移植到一个新的环境下时, 或是一个新的开发者需要搭建一个这个项目的开发环境时, 就需要将这些库一个一个地全部安装到新环境下, 并且为了不出现 "这段代码在我电脑上运行没有问题啊" 这种问题, 应该在所有的环境下安装完全一样的版本.  
如果每次都要手动安装这些库, 不仅费事, 而且容易出错.  
pip 为我们提供了一种很方便的方法, 我们可以将所有这些依赖库以及版本信息写入到一个文件中, 在用 `pip install` 安装库的时候, 使用 `-r` 选项指定这个文件, 这样, 在该文件中的所有库都将被安装, 并且还可以把这个文件放到版本控制中, 方便追中依赖库的更新信息.

这个文件被叫做 `requirement file`

那应该如何编写`requirement file`? pip 为我们提供了 `freeze` 命令, 该命令会将当前系统上安装的所有依赖和版本信息都打印出来, 这些信息就可以作为 `install -r` 选项的输入文件. `pip freeze`, `pip freeze > requirements.txt`, `pip install -r requirements.txt`

刚才我们一直在使用 `pip list` 命令查看当前系统已安装的库信息, 它还有一个比较常用的选项 `-o/----outdated`, 可以使用 `pip help list` 查看帮助文档, 该参数会列出当前系统中可更新的库.  

如果发现有新版本可以使用时, 我们可以使用 `pip install` 的 `-U` 参数, 来更新某个库.  
如果当前系统中存在大量已经过期的库(或者说有更新的库), 想要安装这些库, 如果手动一个一个来更新就比较费时了, 这有一段代码可用来更新当前系统中的所有库. `pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U `