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
