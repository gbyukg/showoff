# 条件判断
每个条件判断中可以有有0个或多个 `elif`.  
最后的 `else` 也是可选的

# 单行条件表达式

    @@@ python
    # 错误, Python 将会吧 (100 + 10) 作为一个表达式,
    # 当 cus 为 False 时, 结果为 0
    width = 100 + 10 if cus else 0
    # 可以使用括号
    width = 100 + (10 if cus else 0)
    
    # 可以很方便与其他语句一起合用
    print("{0} file{1}".format((count if count != 0 else 'no'), ('s' if count !=1 else '')))

# while

正常退出是指: whild 循环没有被 `break`, `return` 语句打断, 或是没有异常发生.

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    num = 5

    while num:
        # 当遇到 break 时, else 语句将不会被执行
        if num == 3:
            break
        print(num)
        num -= 1
    else:
        print('end loop')

    # elese 为可选语句
    # 如果 while 语句正常退出, else 语句将总是被执行
    # 但是如果在 while 语句中有 break, return,或是有异常抛出
    # else 语句将不会被执行

# for

    @@@ python
    # for
    # for in 循环中的 else 语句与 whil 中的一样
    for i in range(0, 5):
        print(i)
    else:
        print('end for')
