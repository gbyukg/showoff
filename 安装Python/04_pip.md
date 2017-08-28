<!SLIDE>

# Python 包管理工具 pip

Python 中存在成千上万个第三方库, 当我们的程序中需要这些第三方库的时候, 可以通过python的包管理工具 [Python Package Manager](https://pypi.python.org/pypi/pip), 很容易的安装和更新这些第三方库.

## pip命令

    @@@ bash
    # 查看帮助信息
    pip help
    pip help install

    # 查找某个库
    pip search requests

    # 安装 package 库
    pip install requests

    # 安装指定版本
    pip install requests==2.0.0

    # 安装某个库时指定最小版本
    pip install requests>=2.18.3

    # 从文件安装
    pip install -r requirements.txt

    # 卸载库
    pip uninstall requests

    # 卸载 requirement.txt 文件中的所有包
    pip uninstall -r requirement.txt

    # 卸载时不提示确认信息
    pip uninstall -y requests

    # 列出当前已经安装的库
    pip list

    # 显示当前已安装库的详细信息
    pip show Pympler
    pip show --verbose Pympler

    # 打印出当前系统中安装的库及其版本信息
    pip freeze

    # 查看那些库有更新.
    pip list -o

    # 更新库
    pip install -U requests

    # 列出当前已安装库信息
    pip freeze

    # 更新所有
    pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U 

## pip requirments.txt

    @@@ bash
    #
    ####### requirements.txt #######
    #
    ###### 没有指定特定版本信息的第三方库 ######
    nose
    nose-cov
    beautifulsoup4
    #
    ###### 明确指定了要第三方库要使用的版本 ######
    #   See https://www.python.org/dev/peps/pep-0440/#version-specifiers
    docopt == 0.6.1             # Version Matching. Must be version 0.6.1
    keyring >= 4.1.1            # Minimum version 4.1.1
    coverage != 3.5             # Version Exclusion. Anything except version 3.5
    Mopidy-Dirble ~= 1.1        # Compatible release. Same as >= 1.1, == 1.*
    #
    ###### 引用其他 requirements.txt 文件 ######
    -r other-requirements.txt