<!SLIDE center subsection>

# 数字类型
在 Python 中, 数字类型可划分为两类:

- 整型类型
  - 布尔类型
- 浮点数

<!SLIDE transition=turnUp>

# 整型类型

在Python中, 整型大小的限制取决于宿主计算机的内存大小. 当数值过大时, Python 会自动分配一块内存来存放该值, 因此在Python中, 很少能出现整型溢出的情况.

    @@@ Python execute
    print(100 ** 100)

# 定义整型变量

<ul><li><p>使用数字字面量定义整型类型变量</p></li></ul>
    @@@ python
    int1 = 95

<ul><li><p>使用内置函数 int()</p></li></ul>
    @@@ python
    int2 = int(95)

<!SLIDE transition=turnUp>

# 整型运算

| 语法 | 描述  | 简写 | 
| --           | -- | :--: |
| x + y        | 加 | +=
| x - y        | 减 | -=
| x * y        | 乘 | *=
| x / y        | 除(*) |  /=
| x // y       | 地板除 | //=
| x % y        | 模运算 | %=
| x \*\* y     | 幂运算 | \*\*=
| -x           | 负数 |
| +x           | 正数 |
| abs(x)       | 绝对值 |
| divmod(x, y) | 返回一个元组, 包含 x/y 的商和余数 |
| pow(x, y)    | x 的 y 次幂 |

.callout.warning Python2 中的除法运算为 整数除(地板除), Python3 中的除法默认为 小数除

<!SLIDE transition=turnUp>

# Python2 中的 long 整型

在 Python2 中, 除了 `int` 类型之外, 还存在 `long` 类型, 在整数值后面追加 `L` 或 `l`(推荐使用大写L, 显示直观), 即可定义一个 `long int` 类型的变量

    @@@ python
    int_l = 2L
    type(int_l)

使用内置函数 `long()` 创建长整型变量

    @@@ python
    int_l = long()

如果一个 `int` 类型的值大小超出最大限制, 将会被自动转换成 `long` 类型

    @@@ python
    import sys
    type(sys.maxsize)
    type(sys.maxsize + 1)

.callout.info 在 Python3 中, 摒弃了 `long` 类型, 因此在 Python3 中后缀 `L` 将会导致语法错误, 并且内置函数 `long()` 也已经不复存在了. 取而代之, 全部使用 `int` 类型.

<!SLIDE transition=turnUp>

# 整型类型的本质

在 Python 中, **一切皆对象**, 包括一个整数或一个整数变量

    @@@ Python execute
    print(dir(5))

在 Python 中, 数值类型的值为 **只读** 的. 可以通过内置函数 `id()` 可以获取到 Python 对象的唯一ID.

![Alt text](../_images/datatype/val.png)
![Alt text](../_images/datatype/val1-2.png)

<!SLIDE>

# 整型进制转换

Python 同样支持数字的不同进制表示形式:
  - 十进制 `18`, 对应的转换函数 `int(N)`

  - 二进制 `0b10010`, 对应的转换函数 `bin(N)`

  - 八进制 `022`, 对应的转换函数 `oct(N)`

  - 十六进制 `0x12`, 对应的转换函数 `hex(N)`

![Alt text](../_images/datatype/hex.png)

<!SLIDE>

# 位运算

位运算符

| 语法 | 描述 | 简写 |
| --     | -- | :--: |
| i &#124; j| 或: 只要一个为1, 结果即为1 | &#124;= |
| `i ^ j`  | 异或: 相同为0, 不同为1 | `^=` |
| `i & j`  | 并且: 全部为1, 值为1, 否则为0| `&=` |
| `i << j` | 向左移位: | `<<=` |
| `i >> j` | 向右移位: | `>>=` |
| `~i`     | 取反: 1->0, 0->1 | |

<!SLIDE transition=turnUp>

# 位运算使用场景

用途最多就是作为标志位, 如 Linux 权限位.

- `1`: 执行权限
- `2`: 写权限
- `4`: 读权限


![Alt text](../_images/datatype/linux_permission.png)

## 位运算示例

打开/关闭 Linux 权限位

      0 1 0 0              0 1 1 0 
    | 0 0 1 0  = 4 | 2   & 1 1 0 1  = 4 & ~2
    ----------           ----------
      0 1 1 0              0 1 0 0

<!SLIDE subsection>

# bool型

布尔类型属于整数类型的一种, 只存在两个值:

- `True`: 一切非0值和非空值, 转换成整数是为 `1`

- `False`: 0 和 空值, 转换成整数时为 `0`

可以像其它数据类型一样, 调用内置函数 `bool()` 返回一个布尔对象.

    @@@ python
    bool()       # False
    bool(0)      # False
    bool('')     # False
    bool(-4)     # True
    bool('str')  # True

bool 的特殊作用

    @@@ python
    ['DL', 'BJ'][True]
    ['DL', 'BJ'][False]
    ['DL', 'BJ'][1 > 2]
    ['DL', 'BJ'][1 > 2]

.callout.info 在 Python2 中, `True` 和 `False` 是两个内置变量, 可以被手动更改成其他值, 而在 Python3 中, 他们成为了关键字, 不可以在对其进行修改了.

<!SLIDE transition=turnUp>

# 比较关系运算符

运算符 | 描述 | 示例 |
---   | --- | ---
`>`  | 如果左操作数的值大于右操作数的值，则条件成为真.      | `a > b`
`>=` | 如果左操作数的值大于或等于右操作数的值，则条件成为真. | `a >= b`
`<`  | 如果左操作数的值小于右操作数的值，则条件成为真.      | `a < b`
`<=` | 如果左操作数的值小于或等于右操作数的值，则条件成为真. | `a <= b`
`==` | 如果两个操作数的值相等，则条件为真.                | `a == b`
`!=` | 如果两个操作数的值不相等，则条件为真.              | `a != b`
`is`    | 如果是同一个对象, 即对象 id 相同, 则条件为真    | `1 is 1`
`is not`| 如果不是同一个对象, 即对象 id 不相同, 则条件为真 | `1 is not 1`

.callout.info 在 Python2 还支持 `<>` 代表不等于, 在 Python3 中已经取消了这个符号