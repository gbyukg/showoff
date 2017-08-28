当确定好 Python 版本后, 就可以安装 Python 了.

虽然一般大部分系统主流操作系统中都已经预先安装好了 Python, 但某些情况下, 比如说预安装的 Python 版本不符合我们的要求, 或在系统上运行的多个 Python 项目使用了不同的 Python 版本等, 我们就需要安装符合的 Python 版本了.

对于Windows和Mac上的Python非常简单, 一直下一步下一步就可以了. 这里就不介绍了. 这里主要说一下 linux 上的源码编译安装.

我们主要介绍一下从源码安装 Python, python的源码可以从官网下载到, 也可以从 github 上下载到.

在编译Python源码之前, 我们首先要安装一些库文件, 这些库是安装 Python 时所依赖的库, 但并不是必须的, 当编译 Python 时, 只有开启某些功能时, 才会需要相应的库, 或者说只有某些库存在时, 才会开启Python的某些功能. 比如要使用 ssl 功能, 系统就需要预先安装好 openssl 的 dev 库

编译之前首先是要下载源码, 到 Python 的官网上就可以找到所有版本的源代码.

`wget https://www.python.org/ftp/python/3.6.2/Python-3.6.2.tar.xz`  
`tar -Jxvf Python-3.6.2.tar.xz`

执行 `configure` 和 `make` 命令开始编译和安装 Python 源码  

# autotools
在编译的时候, 我简单说一下 `configure` 和 `make` 命令, 在 Linux 下, 几乎所有的编译安装都会用到这套流程, `configure`->`make`->`make install`, 而不仅仅是安装 Python.  
`configure` 其实就是一个 shell 脚本, 这个脚本是由 `autotools` 系列工具生成出来的.

# 查看 Python 版本信息
当安装好python 后, 可以通过执行 `python -V` 查看 python 版本信息