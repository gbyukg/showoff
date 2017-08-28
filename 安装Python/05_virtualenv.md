<!SLIDE>
# virtualenv

[virtualenv](https://virtualenv.pypa.io/en/stable) 可以让我们很方便的创建 Python 的虚拟开发环境.

## 安装 `virtualenv`
使用 `pip` 安装 virtualenv

    @@@ bash
    pip install virtualenv

## 创建虚拟环境

    @@@ bash
    virtualenv proj1

该命令会在当前目录下创建一个新目录 proj1, 并包含以下子目录:

- `include` 包含了 Python 的头文件
- `lib` 包含了 Python 中的库文件, 新安装的库将全部存放在 lib/pythonXX/site-packages/ 目录下
- `bin` 生成的一些可执行文件, 包括 Python, pip 等等

## 指定 Python 版本

    @@@ bash
    virtualenv proj2 --python /root/.pyenv/versions/2.7.13/bin/python

## 激活环境

    @@@ bash
    . proj1/bin/activate

## 取消激活

    @@@ bash
    . proj1/bin/activate

<!SLIDE bullets incremental transition=fade>
# `pyenv` 与 `virtualenv`

通过使用 `pyenv` 提供 `virtualenv` 插件, 能够让我们更方便的使用 `virtualenv`.

## 安装 `virtualenv` 插件

    @@@ bash
    # 下载插件到 pyenv 的 plugin 目录中
    git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
    # 使 virtualenv 支持 pyenv 中类似 local 的功能
    echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile

## 使用 `virtualenv` 插件

在安装完插件以后, 首先需要通过 pyenv 提前创建好我们需要的 virtualenv 环境:  
`pyenv virtualenv 2.7.13 proj-2.7.13`

查看当前系统中预设了哪些 virtualenv:  
`pyenv virtualenvs`

激活 virtualenv:  
`pyenv activate proj-2.7.13`

取消激活:  
`pyenv deactivate`

为某个路径设定特定的 virtualenv
`pyenv local proj-2.7.13`