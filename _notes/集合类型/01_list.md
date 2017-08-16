# 列表赋值引用

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    L1 = ['a', 'b', 'c']
    L2 = L1

    print(L2)

    L1[1] = 1
    print(L1)
    print(L2)

    L1 = ['a', 'b', 'c']
    L2 = L1[:]
    L1[0] = 1
    print(L1)
    print(L2)

    L2[0] = 'x'
    print(L1)
    print(L2)

# 列表推导式

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 当我们需要创建包含大量元素, 或是需要动态生成列表时, 一般的选择是使用 for 循环语句
    # 使用 for 循环创建列表
    temp = []
    for item in range(0, 100):
        temp.append(item)

    print(temp)

    # 但是使用列表推导式, 只需要一行即可. 注意是中括号 []
    temp2 = [item for item in range(0, 100)]
    print(temp2)

    # 还可以使用条件表达式
    temp3 = [item for item in range(0, 100) if item % 2 == 0]
    print(temp3)

    # 使用多个循环语句
    temp4 = [''.join((s, z, c)) for s in 'MF' for z in 'SMLX' for c in 'BGM' if not (s == 'F' and z == 'X')]
    print(temp4)
