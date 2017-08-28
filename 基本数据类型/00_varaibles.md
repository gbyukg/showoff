<!SLIDE subsection>

# 变量
Python 中变量的特点:

- Python 属于解释性, 在执行 Python 代码前无需事先编译成机器码文件, 在运行 Python 脚本时 Python 解释器会自动将代买翻译成机器码后在执行.

- Python 属于动态类型语言, Python 解释器在解释变量时会根据变量的值自动分配合适的内存空间给变量, 因此无需在声明变量时指定变量的类型.

- Python 属于强类型语言, 因此在不同类型的变量之间做操作时不会做自动转换处理.

- 在使用一个变量前, 必须先定义好这个变量.

<!SLIDE transition=turnUp>

# 变量命名规则

与大部分其他编程语言类似, 变量名是由一个不包含空格的任意个数的字符序列组成, 包括字母, 数字和下划线, 并且符合以下两个规则:

<ul><li><p>变量名必须以字母`[a-zA-Z]`或下划线(`_`)开头.</p></li></ul>

<ul><li><p>不能使用 Python 中的关键字作为变量的名字.</p></li></ul>
    @@@ python execute
    import keyword
    print(keyword.kwlist)

[Python2 built-in](https://docs.python.org/2/library/functions.html)

[Python3 built-in](https://docs.python.org/3.6/library/functions.html)

.callout.warning Python 中的变量名是区分大小写的, 例如 `city = 'dl'` 和 `City = 'DL'` 是两个变量.

<!SLIDE transition=turnUp>

# 约定俗成

以上两条是定于变量名的硬性规定, 如果不符合以上两条规则中的任意一条, 都会导致语法错误.

但定义一个变量一般还需要遵守以下两点约定俗成的规则, 虽然不符合以下两点的变量名不会有任何错误, 但是为了保证代码的健壮性, 尽量都要符合这两点规则:

<ul><li><p>不要使用 Python 中预定义好的变量名或是方法名做为自己的变量名或方法名.</p></li></ul>
    @@@ python execute
    # 查看 Python 中的内置变量和函数
    print(dir(__builtins__))

<ul><li><p>不要定义以双下划线dunder(`__`)开头和结尾的变量.</p></li></ul>

<!SLIDE transition=turnUp>

# 定义变量

自动被解释成 `字符串`

    @@@ python
    language = 'Python'

自动被解释成 `整数`

    @@@ python
    major_version = 3

自动被解释成 `浮点数`

    @@@ python
    mainor_version = 36.1

自动被解释成 `列表`

    @@@ python
    python_versions = [3, 36, 1]

同时为多个变量赋值

    @@@ python
    a = b = c = 1

同时赋值多个变量

    @@@ python
    val1, val2, val3 = 1, 'str1', 'zzl'

`del` 删除变量

    @@@ python
    del language