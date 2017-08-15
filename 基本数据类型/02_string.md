<!SLIDE center subsection>
# 字符串类型

和数字类型一样, 字符串同样是不可变对象. 为一个变量重新赋值一个新字符串值时, 实际上是创建了一个新的字符串对象, 并将该变量指向这个新创建的字符串对象.

创建字符串内置函数 `str()`

<!SLIDE transition=turnUp>
# 创建字符串对象

使用字符串字面量值

    @@@ python execute
    s1 = 'string1'
    print(s1)

`str()` 内置函数

    @@@ python execute
    print(str('string'))

多行字符串

    @@@ python execute
    s2 = 'this \
    is \
    one \
    line'
    print(s2)

三引号(triple quoted string)

    @@@ python execute
    s3 = """This is a multiple lines string.
    line2
        line3
    """
    print(s3)

括号中的字符串

    @@@ python execute
    s4 = ("This is the nice way to join two long string "
    "togeter; it relies on string literal concatenation.")
    print(s4)

.callout.info 在 Python 中, 单引号与双引号意义完全相同, 因此上面的示例都可以使用双引号来代替

# 字符串相加

我们可以使用 `+` 将多个字符串拼接到一起, 形成一个新的字符串.

    @@@ python execute
    a = 's'
    b = 'tr'
    c = 'ing'
    print(a + b + c)

.callout.warning 字符串对象与数字对象一样, 属于不可变类型, 当使用 `+` 拼接多个字符串时, 每遇到一个 `+` 都将生成一个新的字符串对象, 效率低下.

<!SLIDE transition=turnUp>
# Python2 与 Python3 中的字符串

分别在 Python2 和 Python3 中执行以下代码片段

    @@@ python
    #!/usr/bin/env python

    print("你好, 拍森")

[utf-8 编码查询](http://www.ltg.ed.ac.uk/~richard/utf-8.cgi)

.callout.info Python2 默认使用 ASCII 编码, 而 Python3 中使用 UNICODE 作为默认的编码值.

解决办法:

- `# -*- coding: utf-8 -*-`
- `# encoding: utf-8`

<!SLIDE transition=turnUp>
# 转义字符

| 转义字符   | 说明
| --         |  -- |
| `\newline` | 转义换行
| `\\`       | 转义 \
| `\'`       | 转义 '
| `\"`       | 转义 "
| `\a`       | ASCII 铃音字符
| `\b`       | 回退字符
| `\f`       | 换页* 
| `\v`       | 垂直制表(VT)
| `\r`       | 回车(CR) ，将当前位置移到本行开头(输入的字符会覆盖当前字符)
| `\n`       | 换行(LF) ，将当前位置移到下一行开头
| `\uhhhh`   | 16位的十六进制值 |
| `\Uhhhhhhhh`| 32位的十六进制值 |

引号转义

    @@@ python
    a = "Single 'quotes' are fine; \"doubles\" must be escaped."
    b = 'Single \'quotes\' must be escaped; "doubles" are fine.'
    c = '''both single 'quotes' and double "quotes" are fine.'''

<!SLIDE transition=turnUp>

# 原始字符串(raw)

有时候一个字符串中包含了大量需要转义的字符(正则表达式), 可以通过在字符串前加上 `r` 字符, 来表示这是一个原始字符串, 不要做任何转义.

    @@@ python execute
    print(r"123456\rab")

<!SLIDE transition=turnUp>

# 字符串比较

字符串支持像整数类型那样的比较运算符操作, `<`, `<=`, `==`, `!=`, `>`, 和 `>=`.

对比两个字符串时, 字符串将被拆分成一个一个的字符, 字符会被转正对应的数字, 然后对两个字符串中的每个字符进行对比.

![string_com1.png](../_images/datatype/string_com1.png)
![string_com2.png](../_images/datatype/string_com2.png)

<!SLIDE transition=turnUp>

# 字符串索引

在 Python 中, 我们可以通过下标索引的方式访问字符串中的某个或某一段子字符串(称之为: 切片), 格式为: `s[N]`, 其中 `N` 为字符索引位置, 其取值范围 `0 <= N < len(s)` 或 `-1 <= N <= -(len(s))`.

![string_com2.png](../_images/datatype/string_index.png)

    @@@ python execute
    s = 'Light ray'
    print(s[0])
    print(s[-2])

.callout.info 如果索引超出字符串范围, 将抛出 `IndexError` 异常.

<!SLIDE transition=turnUp>

# 字符切片

切片: 从字符串中提取子字符串片段, 格式为:

`seq[start:stop:step]`, 其中:

  - `start`: 表示字符串起始索引位置, 其值可为正, 也可为负, 忽略不写表示从 0 开始
  - `stop` 字符串终止索引位置, 其值可为正, 也可为负, 忽略不写表示到字符串结尾
  - `step` 步长, 默认为 1

最终截取到的字符串为: `start <= 片段 < stop`

.callout.info `seq` 可以是任何序列对象, 包括后面要讲到的 `tuple`, `list` 等等.

切片操作可以作用到字符串的任意一端:

  - `步长为正`: 从左至右, `start < stop`

  - `步长为负`: 从右至左, `start > stop`

<!SLIDE transition=turnUp>

# 字符切片示例

![string_com2.png](../_images/datatype/string_slicing.png)

步长为正

    @@@ python
    s = 'he ate camel food'
    s[0:2]
    s[:2]
    s[3:6]
    s[13:]
    s[7:-5]
    s[0:-5:3]
    s[::]
    s[::3]

步长为负

    @@@ python
    s[5:2:-1]
    s[::-1]
    s[-1:2:-2]

<!SLIDE transition=turnUp>

# 字符串操作
