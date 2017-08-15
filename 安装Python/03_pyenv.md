<!SLIDE center subsection>

# pyenv

https://github.com/pyenv/pyenv

<!SLIDE transition=turnUp>

# 从 pyenv 安装Python

pyenv 主要是用 `SHELL` 编写的工具, 它可以然我们在系统中同时安装多个 Python 版本, 在已安装的 Python 版本中随意地进行切换.

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

## 使用 pyenv

查看 `pyven` 版本信息

    @@@ Shell execute
    pyenv -v

获取帮助信息

    @@@ Shell execute
    pyenv -h

获取子命令帮助信息

    @@@ Shell execute
    pyenv install -h

查看可以安装的 Python 版本

    @@@ Shell execute
    pyenv install -l

安装指定的 Python 版本

    @@@ bash
    pyenv install 3.6.2

<!SLIDE transition=turnUp>

# pyenv 常用命令

查看系统中安装了哪些 Python 版本

    @@@ Shell execute
    pyenv versions

查看当前 pyenv 使用的 Python 版本

    @@@ Shell execute
    pyenv version

设置默认的 Python 版本

    @@@ bash
    pyenv global 3.6.2

为当前目录设置 Python 版本

    @@@ bash
    pyenv local 3.6.2

显示当前使用的 pyenv 的路径信息

    @@@ Shell execute
    pyenv which python
