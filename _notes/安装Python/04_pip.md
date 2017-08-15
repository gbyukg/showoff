# pip

至此我们已经安装好 Python 了, 有了基本的开发环境, 但这还不够, 在大部分开发过程中, 我们会使用很多 Python 的第三方库, Python 为我们提供了很好的包管理工具, 这就是 `pip`, 使用它, 我们可以快速地安装或更新 Python 库.

`pip help` 首先, 第一个命令还是如何查看 pip 的帮助文档信息.  
`pip help install` 还可以查看子命令的帮助文档.
=====222222rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr里以 `requests` 库为例来展示如何使用 pip

  - `pip search requests` 在安装一个扩展库之前, 我们可以使用 `search` 子命令来查询该扩展库.
  - `pip install reauests` 在找到该库以后, 就可以使用 install 命令来安装扩展库了
  - `pip list` 安装完以后, 我们可以使用 `pip list` 命令来查看库是否已经被安装好了, 该命名会展示所有当前系统中已经安装好了的库
  - `pip show --verbose requests` 显示当前已经安装库的详细信息
  - `pip uninstall requests` 也可以使用 `uninstall` 来卸载已经安装的库.

刚才我们使用 `pip install requests` 命令直接安装了 request 库, 这默认将安装最新版本的库, 在安装的时候, 我们还可以指定要安装的版本,如: `pip install requests==2.0.0` 表示将安装指定的版本, `pip install requests>=2.0.0`

如果当我们开发的一个项目需要很多依赖库, 一个一个安装这些苦将非常痛苦, 并且为了不出现 "这段代码在我电脑上运行没有问题啊" 这种问题, 所有开发者应该严格使用一直的库版本. 我们可以将所有这些依赖库以及版本信息写入到一个文件中, 在用 `pip install` 时候使用 `-r` 选项指定这个文件, 则该文件中的所有库都将被安装, 并且该文件还可以被放到版本控制中, 方便追中依赖库的更新信息.

pip 为我们提供了 `freeze` 命令, 该命令会将当前系统上安装的所有依赖和版本信息都打印出来, 这些信息就可以作为 `install -r` 选项的输入文件. `pip freeze`, `pip freeze > requirements.txt`, `pip install -r requirements.txt`

刚才我们一直在使用 `pip list` 命令查看当前系统已安装的库信息, 它还有一个比较常用的选项 `-o/----outdated`, 可以使用 `pip help list` 查看帮助文档, 该参数会列出当前系统中可更新的库.  

使用 `pip install` 的 `-U` 参数, 可以让我们更新某个库.  
如果当前系统中存在大量已经过期的库(或者说有更新的库), 想要安装这些库, 如果手动一个一个来更新就比较费时了, 这有一段代码可用来更新当前系统中的所有库. `pip freeze --local | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install -U `