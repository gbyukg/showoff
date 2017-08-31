<!SLIDE transition=turnUp>
# pyenv 的安装与使用

pyenv 是一个用 `SHELL` 编写的工具, 它可以让我们在系统中快速方便地安装多个 Python 版本, 并且在已安装的 Python 版本中随意地进行切换.

pyenv项目地址: https://github.com/pyenv/pyenv

## 安装 pyenv

    @@@ bash
    # 获取源码
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv

    # 设置 PVENV_ROOT 环境变量, 注意如果你使用的是其他shell, 如 ZSH, 请使用 .zshenv 代替 .bash_profile 文件.
    echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
    echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
    echo 'eval "$(pyenv init -)"' >> ~/.bash_profile

    # 使修改生效, 或重新登录shell
    . ~/.bash_profile

.callout.warning 以上我们是将pyenv安装到了当前用户下, 所以仅对当前用户生效.

<!SLIDE transition=turnUp>

# 使用 pyenv

    @@@ bash
    # 查看 pyenv 版本信息
    pyenv -v

    # 查看帮助信息
    pyenv -h
    pyenv install -h

    # 列出所有可用的 python 版本
    pyenv install -l

    # 安装一个指定的 python 版本
    pyenv install 3.6.2

    # 查看当前系统中安装了哪些 Python 版本
    pyenv versions

    # 设置某个版本作为系统的默认版本
    pyenv global 3.6.2
    # 查看当前系统默认版本信息
    pyenv global

    # 查看当前使用的 Python 版本
    pyenv version

    # 查看当前所使用的 Python 的路径信息
    pyenv which python

    # 为某个目录设置单独的 Python 版本
    pyenv local 3.6.2

    # 取消当前目录设定
    pyenv local --unset