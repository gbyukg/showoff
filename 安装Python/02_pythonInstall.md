<!SLIDE>
# 从源码安装 Python

## 准备
    @@@ bash
    yum install -y \
        zlib-devel \
        readline-devel \
        bzip2-devel \
        libsq3-devel \
        openssl-devel 

## 编译&安装
    @@@ bash
    ./configure --prefix=/usr/local/python2.7 && \
    make && \
    make install

查看 Python 版本

    @@@ Shell execute
    /usr/local/python2.7/bin/python -V

<!SLIDE bullets incremental transition=fade>
## autotools

*configure 是由 autotools 系列工具生成出来的 SHELL 脚本文件, 该脚本最主要作用 检测安装环境(包括必要的库,头文件等是否存在); 软件的功能性的配置(打开/关闭 XXX功能) 以及生成 Makefile.*

> autotools 由一系列工具组成, 包括:

*  - `autoconf` 用于生成 configure shell 脚本 执行 `./configure -h` 查看帮助信息.
*  - `automake` 由 autoconf 调用, 生成 Makefile 文件
*  - `libtool` 根据配置生成共享库文件