# pyenv 介绍

虽然从源码编译安装Python没有问题, 但是一些工具的出现将会大大提高我们的效率. `pyenv` 就是其中一个工具, 它是一个用 `shell` 编写的工具, 使用它我们可以快速安装一个 Python 到我们的系统中, 并且可以在多个 Python 版本中随意进行切换.

# 安装 pyenv
安装 pyenv 非常简单, 只需要将源码下载到本地, 并设置好一些环境变量即可.

# pyenv 使用
当 pyenv 安装好之后, 我们就可以通过命令 `pyenv` 来使用它了.

    @@@ bash
    # 查看 pyenv 的版本信息
    pyenv -v
    # 查看帮助文档
    pyenv -h
    # 或者是查看某个子命令的帮助文档信息
    pyenv install -h

    # 可以看到 install 有个 -l 选项
    # 用于列出有哪些可用的python版本
    pyenv install -l

    # 安装一个 python
    pyenv install 3.6.2
    # 安装完以后, 查看 Python 的版本
    python -V
    command -v python

    # 还可以查看当前系统中安装了哪些 python 版本
    pyenv versions

    # 设定某个版本作为默认的版本
    pyenv global 3.6.2

    # 查看当前默认的版本
    pyenv version

    # 使用 which 命令查看当前 python 的完整路径
    pyenv which python
    # 使用 pyenv 安装的所有 python
    # 全部被保存到了当前用户根目录下的 .pyenv/versions 目录下

    # 还可以为某个目录设定一个默认的python版本
    # 比如创建一个目录 /tmp/py2
    # 在这个目录下执行
    pyenv local 2.7.13
    # 此时查看 python 的版本
    pyenv version
    python -V
    # 当退出到这个目录后再次查看 python 的版本信息
    python -V
    # 再次进入到这个目录
    cd /tmp/py2
    python -V
    # 当我们使用 local 自命令时
    # 该命令会在当前目录下创建一个隐藏文件 .python-version
    # 通过 ls -a 命令可以看到这个文件
    ls -la
    # 打印出这个文件中的内容
    cat .python-version
    # 可以看到, 在该文件内记录了 Python 的版本信息
    # 就是我们执行 local 子命令时指定的版本信息
    # 每次当我们进入到这个目录内之后, pyenv 就会自动切换到这个文件中指定的 Python 版本
    # 有点像 linux 下 `automount` 的意思. 进入某个设定好的路径后, 进行自动挂载操作.
    # 当退出这个目录后, Python 又被设定成 `global` 中指定的 Python 版本了.

    # 取消对 local 环境的设定
    pyenv local --unset
    # 其实就是删除了 .python-version 文件
    ls -la