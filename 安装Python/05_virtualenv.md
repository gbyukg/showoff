<!SLIDE center subsection>
# virtualenv

https://virtualenv.pypa.io/en/stable

<!SLIDE transition=turnUp>

# virtualenv 使用

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
