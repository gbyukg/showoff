# 字符串类型
    @@@ python
    s1 = 'string'
    s2 = 'this \
    is \
    one \
    line'
    s3 = ''' This is a mutilple lines string.
        Line2
    line3

    s4 = ('this '
    'is '
    'one '
    'line')

    # 注意, 多个字符串相加效率慢
    # 没相加一次, 都会生成一个新的对象
    's' + 'tr' + 'ing'

    '=' * 5

# 转义字符, 进度条实现
    @@@ python
    print('\a') # 铃音
    print('abc\b1') # 回退
    print('123\rabc') # 回车
    print('123\nabc') # 换行

最熟悉的可能就是 `\r` 和 `\n` 了, 因为 Linux 和 Windows 下用这两个字符表示换行符.  
但是仔细看 \r 描述

    @@@ shell
    #!/usr/bin/env bash

    for i in {1..5}; do
        # -n 进制输出换行符
        echo -en "${i}%\r"
        sleep 0.5
    done
    echo ''

Python 实现:

    @@@ python
    #!/usr/bin/env python

    from time import sleep
    import sys

    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('='*i, 5*i))
        sys.stdout.flush()
        sleep(0.25)

# 字符串索引
从上图可以看出, Python 不仅支持正数的索引下标, 同时还支持负数的索引下标: 表示从字符串的右边开始计算.

    @@@ python
    s = 'Light ray'
    s[0]
    s[4]
    s[-1]
    s[15]

# 切片
字符串的切片操作可以让我们获取字符串中的某一段子字符串.

步长为正, 起始位置要小于结束位置, 表示从左到右截取

    @@@ python
    s = 'he ate camel food'
    s[0:2]    # he 步长默认为 1
    s[:2]     # he
    s[13:]    # food
    s[::]     # he ate camel food
    s[-9:14]  # 'amel f'
    s[7:-5]   # camel
    s[0:-5:3] # ha m
    s[::3]    # ha m d

    # 步长为负, 起始位置大于结束位置
    # 表示从右向左截取
    # 注意, 截取的结构是反顺的.
    s[5:2:-1]  # eta
    s[-1:2:-2] # do ea t
    s[::-1]    # doof lemac eta eh 反转

# 字符串方法

    @@@ python
    s = 'strings are represented by the immutable str data type which holds a sequence of Unicode characters'
    s.startswith('string') # True
    s.startswith('are', 8) # True 还可以指定要搜索的起始位置
    s.endswith('characters') # 判断是否以某个特定的字符串结尾
    s.find('data') # 45 查找某个字符串出现的第一个位置
    s.find('datas') # 返回 -1 如果没有找到结果
    # 还可以使用 in 和 not in 来判断某个字符或字符串是否在一个字符串中
    'are' in s
    s.upper() # 返回大写形式
    s.lower() # 返回小写形式
    ' '.join('city') # 'c i t y' 每个字符之间使用空格分割, 这可能不是我们想要的结果
    ' '.join(('city', 'DL')) # 可以传递一个元组, 元组在后面会降到
    s.replace('imutabel', 'mutable') # 替换字符串
    s.split(' ') # 用空格拆分字符串
    ' str   '.strip() # 去除两边的空格

# format
format 是 Python 2.6 引入的, 如果看一些老代码, 或者比较旧的教程, 会看到使用 `%` 来替代 `format` 关键字.

    @@@ python
    f = 'The input is {}'.format
    f(1)

    tu = (12,45,22222,103,6)
    print '{0} {2} {1} {2} {3} {2} {4} {2}'.format(*tu)

基本用法

    @@@ python
    '{} {}'.format('one', 'two')
    # 'one two'
    '{} {}'.format(1, 2)
    # '1 2'

    # 数字
    '{:d}'.format(42)
    # '42'

    # 字符串
    '{:s} {:d}'.format('one', 2)
    # one 2

    # 浮点数
    '{:f}'.format(3.141592653589793)
    # '3.141593'

    # 使用 {{ 输出 一个 {, }} 输出一个 }
    "{{{0}}} {1} ;-}}".format("I'm in braces", "I'm not")
    # "{I'm in braces} I'm not ;-}"

    # 带符号数字 通过前面使用 +, 使输出结果总是打印符号
    '{:+d}'.format(42)
    # '+42'
    '{:+d}'.format(42)
    # '-42'

位置参数

    @@@ python
    '{0} {1} {0}'.format('one', 'two')
    # 'one two one'

    # 同时指定类型
    '{0:s} {1:s} {0:s} {2:d}'.format('one', 'two', 3)
    # 'one two one 3'

字段名

    @@@ python
    '{who} turned {age} this year'.format(who='She', age=88)
    # 'She turned 88 this year'

    'The {who} was {0} last week'.format(12, who='boy')
    # 'The boy was 12 last week'

    # 使用集合数据类型的索引
    # 这里的变量data属于Python中的集合类型之一, 列表, 虽然现在还没有讲到, 但是这里所用到的知识非常简单
    # 可以把它想象成一个数组, 通过索引的方式来获取其中的元素.
    data = [4, 8, 15, 16, 23, 42]
    # 分别使用集合 data 中下标索引为4 和 5 的元素替换
    '{d[4]} {d[5]}'.format(d=data)
    # '23 42'

    # 使用键值
    # person 是另一种 python 的数据类型, 叫做字典, 存在字典中的每个元素都是以键值对的形式出现的
    # 取代前面我们使用的下表索引, 我们可以通过访问字典中的键来获取它对应的值.
    person = {'first': 'Jean-Luc', 'last': 'Picard'}
    '{p[first]} {p[last]}'.format(p=person)
    # 'Jean-Luc Picard'

    # 名称占位符
    data = {'first': 'Hodor', 'last': 'Hodor!'}
    # 在这个例子中, 我们在format的参数前使用了双星号, 它的意思是将字典data中的元素拆分出来, 每个元素的键作为参数名, 值作为参数的值传递给函数, 我们将在后面讲解 函数 的时候在详细讲解.
    '{first} {last}'.format(**data) == '{first} {last}'.format(first='Hodor', last='Hodor!')
    # 'Hodor Hodor!'
    '{first} {last}'.format(first='Hodor', last='Hodor!')
    # 'Hodor Hodor!'

    # 使用对象的属性
    import math # 第一句话, import math 的意思是引入 math 模块, 关于模块的详细信息我们也将在后面讲解.
    # 我们可以通过 对象.属性 的方式来访问一个对象中的属性.
    # 在这里, 我们将访问 math 对象中的 pi 属性.
    # 因为 math 的位置是0, 所以这里我们使用 0.math.
    'math.pi = {0.pi}'.format(math)


    # 这里用到了 python 的 locals() 内置函数, 
    # locals() 中以字典的方式保存了当前所有的局部变量信息, 也就是说这些值将以 键值对 的方式存在.
    # 再在前面使用双星号来解压
    element = 'Silver'
    number = 47
    locals() 返回字典

    "Element {number} is {element}".format(**locals())
    'Element 47 is Silver'

填充

    @@@ python
    # 填充指的是最小长度, 只有字符串的长度小于指定的长时, 才会填充.
    # 左填充
    '{:>10}'.format('test')
    # '      test'

    # 右填充
    '{:10}'.format('test')
    '{:<10}'.format('test')
    # 'test      '