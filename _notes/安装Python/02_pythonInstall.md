当确定好 Python 版本后, 就可以安装 Python 了.

作为一名 DevOps, 平时接触最多的操作系统就是 类Unix系统了. 大部分自动化运维脚本都是在这些系统上跑的. 所以安装主要是针对 类 Linux/Unix 系统的
对于基于Windows和Mac上的Python非常简单, 一直下一步下一步就可以了.

虽然一般大部分系统主流操作系统中都已经预先安装好了 Python, 但某些情况下, 如预安装的 Python 版本不符合我们的要求, 或在系统上运行的多个 Python 项目使用了不同的 Python 版本等.

在Linux系统上使用包管理工具(如 yum, apt)安装也很简单, 这里也不多做介绍了.

我们主要介绍一下从源码安装 Python, python的源码可以从官网下载到, 也可以从 github 上下载到.

`wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz`  
`tar -Jxvf Python-3.6.2.tar.xz`

在编译Python源码之前, 我们首先要安装一些库文件, 这些库是安装 Python 时所依赖的库, 但并不是必须的, 当编译 Python 时, 只有开启某些功能时, 才会需要相应的库, 或者说只有某些库存在时, 才会开启Python的某些功能. 比如要使用 ssl 功能, 系统就要先与装好 openssl 的 dev 库

执行 `configure` 和 `make` 命令开始编译和安装 Python 源码  

这里对 configure 和 make 做一下简单的说明:  
这种安装方式不止是针对 Python, 对大部分 C 编写的软件都适用, 之所以说是大部分, 是那些使用了 `autotools` 工具来管理源码安装的, 有些 C 工具或 C 库并不使用 `autotools` 而是其他工具, 比如 `cmake`, 这时候 `configure` 和 `make` 就有可能不生效了

当安装好python 后, 可以执行 `python -V` 查看 python 版本信息

python 也支持交互模式, 直接输入 `python` 命令就可进入, 输入 `exit()` 退出交互模式, 或直接使用快捷键 `CTRL-D`, `CTRL-D` 是什么意思?

---

从源码安装虽然是一种可行的方式.