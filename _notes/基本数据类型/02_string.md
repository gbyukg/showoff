# 转义字符, 进度条实现
windows 下使用 `\r\n` 换行, HTTP 头信息中也同样使用 `\r\n`, 类 Unix 系统, 使用一个字符 `\n` 即可

`\r` 需要注意一下.

    @@@ shell
    #!/usr/bin/env bash

    for i in {1..5}; do
        echo -en "${i}%\r"
        sleep 0.5
    done
    echo ''

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

# 切片

![string_com2.png](../_images/datatype/string_slicing.png)

步长为正

    @@@ python
    s = 'he ate camel food'
    s[0:2]    # he
    s[:2]     # he
    s[3:6]    # ate
    s[13:]    # food
    s[7:-5]   # camel
    s[0:-5:3] # ha m o
    s[::]     # he ate camel food
    s[::3]    # ha m d

步长为负

    @@@ python
    s[5:2:-1]  # eta
    s[::-1]    # doof lemac eta eh
    s[-1:2:-2] # do ea t