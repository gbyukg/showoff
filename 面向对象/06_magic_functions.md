<!SLIDE>
# 魔术方法

Python 为我们预定义了一系列以双下滑线(`__`)开头和结尾的方法, 当我们对某些对象做特殊操作, 或是通过特定函数调用对象时, 对应的这些方法就会被 Python 自动调用, 我们称这些方法为 魔术方法.  
我们可以通过对自定义的类实现这些魔术方法, 来达到特殊的功能.

## 常用的魔术方法

### `__repr__(self)`, `__str__(self)`:

说明:  
当我们尝试打印某个对象, 或对某个对象调用 `repr()` 或 `str()` 函数时, Python 会尝试调用这两个方法.

返回值:  
返回一个用于对对象进行描述的字符串.

.callout.info 当一个对象中只包含 `__repr__` 方法时, `print(obj)`, `str(obj)` 和 `repr(obj)` 行为全部一样. 当只包含 `__str__` 时, `print(obj)` 和 `str(obj)` 行为一致.

.callout.info `__str__` 主要用于返回对用户友好的字符串, 对一个字符使用 `str()` 将返回字符串本身.  
`__repr__` 则倾向于返回调试信息.

### `__len__(self)`:

说明:  
当对某个对象使用 `len()` 函数时, Python 会尝试调用该方法.

返回值:  
返回一个代表对象长度的数字

### `__getitem__(self, index)`:

说明:  
当尝试通过索引或者键名访问对象中的某个元素时, Python 会尝试调用该方法.  
对象中一旦定义了该方法, 就可以使用 `for in` 来循环获取对象中的元素了.

返回值:  
返回对象中的某个元素.

### `__next__(self)`:

说明:
如果一个对象中存在 `__next__` 方法, 就可以对函数使用 `next()` 方法来依次获取对象中的元素, 当获取完最后一个元素后, 如果继续对这个对象使用 `next()` 方法, 应当抛出 `StopIteration` 异常.  
含有 `__next__` 方法的对象也称作 **迭代器**

返回值:  
返回对象中的下一个元素, 直到没有更多的元素可返回时, 抛出 `StopIteration` 异常.

.callout.warning 在 Python2 中, 应当使用 `next()` 来代替 `__next__()`

### `__iter__(self)`:

说明:  
`__iter__` 用于返回一个迭代器, 用于 `__iter__()` 方法的对象可以被 `for` 循环语句迭代.

返回值:
返回一个迭代器.

### `__getattr__(self, name)`

说明:  
当尝试访问对象中一个不存在的属性时, Python 会自动调用该方法. 可在该方法中尝试捕获属性拼写等错误, 并给出相应的警告信息.

返回值:  
返回属性值, 或是抛出 `AttributeError` 异常.

<!SLIDE transition=turnUp>
# 魔术方法列表

## 二进制运算
|Operator  |  Method|
| --- | --- |
|+ |   object.__add__(self, other)|
|- |   object.__sub__(self, other)|
|* |   object.__mul__(self, other)|
|//|    object.__floordiv__(self, other)|
|/ |   object.__truediv__(self, other)|
|% |   object.__mod__(self, other)|
|**|    object.__pow__(self, other[, modulo])|
|<<|    object.__lshift__(self, other)|
|>>|    object.__rshift__(self, other)|
|& |   object.__and__(self, other)|
|^ |   object.__xor__(self, other)|
|\| |   object.__or__(self, other)|

## 扩展赋值运算
| Operator | Method                                 |
| ---      | ---                                    |
| +=       | object.__iadd__(self, other)           |
| -=       | object.__isub__(self, other)           |
| *=       | object.__imul__(self, other)           |
| /=       | object.__idiv__(self, other)           |
| //=      | object.__ifloordiv__(self, other)      |
| %=       | object.__imod__(self, other)           |
| **=      | object.__ipow__(self, other[, modulo]) |
| <<=      | object.__ilshift__(self, other)        |
| >>=      | object.__irshift__(self, other)        |
| &=       | object.__iand__(self, other)           |
| ^=       | object.__ixor__(self, other)           |
| \|=      | object.__ior__(self, other)            |

## 一元运算符
| Operator  | Method                   |
| ---       | ---                      |
| -         | object.__neg__(self)     |
| +         | object.__pos__(self)     |
| abs()     | object.__abs__(self)     |
| ~         | object.__invert__(self)  |
| complex() | object.__complex__(self) |
| int()     | object.__int__(self)     |
| long()    | object.__long__(self)    |
| float()   | object.__float__(self)   |
| oct()     | object.__oct__(self)     |
| hex()     | object.__hex__(self)     |

## 比较运算符
| Operator | Method                     |
| ---      | ---                        |
| <        | object.__lt__(self, other) |
| <=       | object.__le__(self, other) |
| ==       | object.__eq__(self, other) |
| !=       | object.__ne__(self, other) |
| >=       | object.__ge__(self, other) |
| >        | object.__gt__(self, other) |