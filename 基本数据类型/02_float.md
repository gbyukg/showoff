<!SLIDE center subsection>

# 浮点数

在Python中, 浮点数用64位来表示的, 与 C 语言中的 double(双精度) 类型一样.

    @@@ python
    f1 = 1.234

使用 `float()` 内置函数创建浮点数

    @@@ python
    f2 = float(1.234)

    # 使用 int() 函数将一个浮点型数值转换成整型
    int(3.81)    # 3 直接舍掉小数部分
    round(3.81)  # 四舍五入

<!SLIDE transition=turnUp>

# 浮点数的本质

整型在计算机中的存储

![整型在计算中的存储](../_images/datatype/int.png)

浮点数内存结构图(定点数)

![浮点数内存结构图](../_images/datatype/float.png)

十进制小数
<p><code>
123.456 = 1*10<sup>2</sup> + 2*10<sup>1</sup> + 3*10<sup>0</sup> + 4*10<sup>-1</sup> + 5*10<sup>-2</sup> + 6*10<sup>-3</sup> = 1.23456*10<sup>2</sup>
</p>
</code>

二进制小数

<p><code>
1.01101 = 1*2<sup>0</sup> + 0*2<sup>-1</sup> + 1*2<sup>-2</sup> + 1*2<sup>-3</sup> + 0*2<sup>-4</sup> + 1*2<sup>-5</sup> = 0.25 + 0.125 + 0.03125 = 0.40625
</p></code>

---

指数位示意图

![浮点数内存结构图](../_images/datatype/exponent.png)

指数(e)转换规则: `指数 + 基数`<br/>
其中基数(bias)为: <code>2<sup>k-1</sup> - 1</code><br/>
`k` 为指数位的字节长度, 对于32位浮点数是 8 个字节, 对于 64 为浮点数来说, 是 11 位, 这是由 `IEEE` 标准规定的.

浮点数转换规则:
<code>
V = (-1)<sup>s</sup> × M × 2<sup>E</sup>
</code>, 
<code>
E = e - bias
</code>

<!SLIDE>
# match 库

| 语法 | 描述
| -- | --
| math.sin(x)   | x 的正弦值
| math.cos(x)   | x 的余弦值
| math.tan(x)   | x 的正切值
| math.sin(x)   | x 的余切值
| math.pi       | 圆周率 PI
| math.fabs(x)  | 绝对值
| math.floor(x) | 小于 x 的最大整数
| math.ceil(x)  | 大于 x 的最小整数

    @@@ python
    import math
    math.floor(3.81) # 小于3.81的最大整数
    3
    math.ceil(3.81)  # 大于3.81的最小整数
    4