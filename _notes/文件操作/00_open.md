# open

在平时工作的时候, 我们想查看一个文件, 一共3个步骤:

- 首先是使用一个文本编辑器打开我们要查看的文件查看内容
- 查看文件内容
- 看完以后关掉这个文件

使用 Python, 或者是任何语言, 都是一样的操作, 打开文件, 读取里面的内容, 使用完以后关闭文件, 只是在 Python 里我们用 open() 方法打开一个文件, 而不是用一个文件编辑器.

## 打开文件

    @@@ python
    # open 至少接受一个参数: 要打开的文件
    # 文件默认是以只读的方式打开的
    f = open('test.txt')
    # 也可以指定文件的打开方式
    # f = open('test.txt', 'r')

    # 获取文件名
    print(f.name)
    # 获取文件访问权限
    print(f.mode)

    # 在文件使用完以后, 我们应该关闭这个文件
    # 因为每打开一个文件, 都会占用一定的系统资源
    # 既然是系统资源, 就一定会有限制
    # 如果系统中打开的文件过多, 超过了系统限制
    # 就会报出 too many open files 错误
    # 所以当使用完一个文件后
    # 我们需要使用 close() 方法来释放这些资源
    f.close()
    # 当然你要是不关闭也行, 当整个程序执行完毕退出以后
    # 所有打开的文件全部都会被自动关掉.

## 读取文件内容
    @@@ python
    from __future__ import print_function

    # Python 还为我们提供了更便捷的方式
    # 使用 with 语句, 当执行完毕以后, 会自动为我们关闭文件
    with open('test.txt', 'r') as f:
        # 我们把打开的文件对象赋给了变量 f
        # 并且变量 f 只能在该代码块中可见
        # 一旦退出代码块, 文件将被自动关闭

        # 文件对象本身是一个可迭代对象
        # 因此我们可以直接循环文件, 获取其中的内容
        # 这种方式获取文件内容时, 使用的是行缓冲模式
        for line in f:
            print(line, end='')

## read()
    @@@ python
    f_contents = f.read()
    print(f_contents)

    # read 还可以接受一个参数, 用于指定读取多少个字节
    f_contents = f.read(100)
    print(f_contents)

    # 再次执行一遍, 会看到输出了后面100个字符
    # 而不是又从头开始读取
    f_contents = f.read(100)
    print(f_contents)

    # 这是因为每个打开的文件都有一个文件指针, 用于指向下一次读取文件时的位置.
    # 打开一个新文件时, 文件指针是0, 表示从第一个字符开始读取
    # 每读取一个字符, 指针就会向后移动一个字节.
    # 我们先读取了100个字符, 指针移动到100处的索引位置
    # 所以在次读取时, 会接着读取内容, 而不是从头开始读

    # 还可以通过 tell 获取当前
    print(f.tell())

    # 当文件内容全部读取完以后, 继续调用 read 读取文件, 会得到一个空的内容
    # 我们可以通过判断读取到内容的长度判断是否达到文件结尾
    f_contents = f.read(10)
    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(10)

## readline()
    @@@ python
    f_contents = f.readline()
    print(f_contents)

## readlines()
    @@@ python
    f_contents = f.readlines()
    # 这是一个列表
    print(f_contents)

# 写文件
向一个以 `r` 打开的文件中写入文件, 提示错误, 文件不可写.

    @@@ python
    with open('test2.txt', 'w') as f:
        # 'w' 自动创建不存在文件

        # 注意, 写入文件时不会自动添加换行符
        # 使用 '\n' 表示换行符, 针对不同的操作系统, Python 会自动为我们转换
        f.write('string1')
        f.write('string2')
        f.write('string3')

        # 尝试在插入其它字符
        # 再次执行, 会发现之前写入的 string 已经没有了
        f.write('another line')

        # 这是因为当我们使用 'w' 打开一个文件时
        # 首先会自动截取文件中的内容, 就是清空
        # 可以使用 pass 语句, 表示打开文件后什么也不干
        pass
        # 执行完以后发现内容已经被清空了

        f.read() # 报错, 该成 `w+`

        # 虽然不报错了, 但是输出的还是为空? 这是为什么?
        # 刚才我们已经说过了, 每个文件里都有一个指针, 指向了当前读取到的文件内容的位置
        # 不只是读取内容会移动该指针, 写文件同样会移动指针
        # 所以如我们直接在下面读取文件内容时, 这个指针已经移动到文件的结尾了
        # 所以获取不到任何内容
        # seek()函数可以帮助我们移动指针的位置.
        f.seek(0)
        print(f.read())

        # 不截取文件
        # 'a+'
        # r+ 打开文件时会将文件指针移动到 0 位置, 写入是回覆盖文件中的内容.

seek

    @@@ python
        f.write('string1\n')
        f.write('string2\n')
        f.write('string3\n')

        f.seek(3)
        print(f.read(5))

## `flush()`

    @@@ python
    import time
    with open('test.txt', 'w', buffering=3) as f:
        for i in range(6):
            f.write("current is: {}\n".format(i))
            #  f.flush()
            time.sleep(1)