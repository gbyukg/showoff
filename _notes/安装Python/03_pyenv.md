# pyenv 介绍

虽然从源码编译安装Python没有问题, 但是一些工具的出现将会大大提高我们的效率. `pyenv` 就是其中一个工具, 使用它我们可以快速的安装一个 Python.

安装 pyenv 非常简单, 只需要将源码下载到本地, 并设置好一些环境变量即可.

当 pyenv 安装好之后, 就可以使用了.

`pyenv local XXX` 该命令会在当前目录下创建一个隐藏文件 .python-version, 该文件内记录了 Python 的版本信息, 就是我们在命令行指定的这个参数, 每次当我们进入到这个目录内之后, pyenv 就会自动切换到这个文件中指定的 Python 版本, 有点 `automount` 的意思. 当退出这个目录后, Python 又被设定成 `global` 中指定的 Python 版本了.

`pyenv -v` 在安装好 pyenv 之后, 就可以使用 `-v` 参数查看我们安装好的 pyenv 的版本, 同时也可以验证我们是否正确的安装了 `pyenv`

如何查看我们可以安装哪些 Python 的版本呢? `pyenv install --list`

    @@@ bash

    # 列出所有可以安装的 Python 版本
    pyenv install --list

    # 安装 Python 3.6
    pyenv install 3.6.2

    # 查看当前使用的 Python 版本
    pyenv version
    # 查看系统已经安装好了的 Python 版本
    pyenv versions

    # 查看当前Python 版本
    python -V

    # 指定要使用的 Python 版本(全局)
    # ~/.pyenv/version
    pyenv global 3.6.2
    python -V

    # 为当前所在项目设置 Python 环境
    pyenv local 2.7.13
    python -V
    cat .python-version

    # 取消针对当前项目的设置
    pyenv local --unset