# virtualenv

最后在介绍一个更炫酷的工具 virtualenv

现在大家想象一下, 你当前维护了多个不同的 Python 项目, 而这些项目中既有 Python2 开发的, 又有 Python3 开发的, 即使是使用相同 Python 版本开发的, 这些 Python 项目不可能会使用完全一样的库, 甚至会出现不同的项目使用同一个库的不同版本.

这时我们就需要为每个项目创建一个相对独立的开发环境, 而 virtualenv 就是为我们提供一个虚拟的开发环境, 它能在同一台电脑上创建多个 Python 的虚拟开发环境, 每个虚拟环境都是相互独立的,(说到虚拟环境, 大家一定要与虚拟机的那个虚拟区别开来, virtualenv中的虚拟仅仅是作用在文件夹层级的, 说白了就是每个虚拟环境仅仅是一个目录罢了. 它只是通过设定一些环境变量指向这个目录). 当启用一个虚拟环境时, 执行 python 的所有命令都将来自于这个虚拟环境, 并且所安装的所有扩展库也都将安装到这个虚拟环境中, 这样就达到了多个虚拟环境以及和系统之间相互隔离的目的.

安装 `virtualenv` 非常简单, 使用 `pip` 命令就可以直接安装了.

安装好以后, `pip show --verbose virtualenv` 查看详细信息

安装好 `virtualenv` 后就可以使用了, 首先第一个命令就是创建一个虚拟的环境, 格式为 `virtual proj1`, 该命令会在当前目录下创建一个名为 `proj1` 的子目录, 也可以加上 `-v` 参数显示详细信息.

该命令会在当前目录下创建一个新目录 proj1, 并包含以下子目录:

- `include` 包含了 Python 的头文件
- `lib` 包含了 Python 中的库文件, 新安装的库将全部存放在 lib/pythonXX/site-packages/ 目录下
- `bin` 生成的一些可执行文件, 包括 Python, pip 等等

## 激活环境

在初始化好一个虚拟环境后, 要想使用这个虚拟环境, 首先需要进行激活. 使用 `. proj1/bin/activate`. 在激活前, 先让我们看一下当前系统中安装了哪些库: `pip list`. 激活后在看一下, 发现系统中的那些库并没有显示被安装, 这正是我们需要的.

激活 proj1 项目, 可以看到 shell 提示符已经发生了变化, 查看当前使用了那个 Python: `command -v python` 和 `pip` 命令.  
在我们的虚拟环境中安装一些第三方库: `pip install psutil`, 安装完以后, `pip show psutil` 查看详细信息, 可以发现安装位置在 proj1 目录下.

使用 `export` 可以看到 `PATH`, `PS1` 都被修改了, 并增加了一个新的环境变量 `VIRTUAL_ENV`, 指向了当前项目目录  
当激活了一个环境以后, 通过 `pip` 安装的新库文件将全部被安装到 `lib/pythonXX/site-packages/` 路径下.

> `PS4` 简单介绍一下

## 取消激活
我们还可以使用 `deactivate` 命令来取消当前 Python 虚拟环境的激活.

在刚才的例子中, 我们创建 proj1 项目时, 直接使用了系统当前默认的 Python 版本, 有时候我们需要使用一个特定的 python 版本, 在初始化项目时, 通过指定 `--python` 选项, 来指定一个明确的 python 版本信息.

    @@@ bash
    virtualenv proj2 --python/-p /root/.pyenv/versions/2.7.13/bin/python
    # 激活 proj2 项目
    . proj2/bin/activate
    # 查看 python 版本
    python -V
    # 可以看到已经是我们指定的 python 版本了

# pyenv 中的 virtualenv 插件
我们还可以将 `virtualenv` 以插件的形式集成到 `pyenv` 中, 这样我们就可以使用 `pyenv` 命令方便的使用 `virtualenv` 了.

安装 `virtualenv` 插件非常简单, 安装完插件以后, 需要重新激活shell.

在安装完插件以后, 首先需要通过 pyenv 提前创建好我们需要的 virtualenv 环境:  
`pyenv virtualenv 2.7.13 proj-2.7.13`

查看当前系统中预设了哪些 virtualenv:  
`pyenv virtualenvs`

激活 virtualenv:  
`pyenv activate proj-2.7.13`

取消激活:  
`pyenv deactivate`

为某个路径设定特定的 virtualenv
    @@@ bash
    mkdir proj1
    pyenv local proj-2.7.13
    # 这样, 当我们每次进入到 proj1 目录后
    # 就会自动激活 proj-2.7.13
    # 退出这个目录后, 就会取消自动激活