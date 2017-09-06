<!SLIDE center subsection>
# 逻辑控制

<!SLIDE transition=turnUp>
# 条件判断

语法:

    @@@ python
    if boolen_expression1:
        suite1
    elif boolen_expression2:
        suite2
    ...
    elif boolen_expressionN:
        suiteN
    else
        else_suit

每个条件判断语句中都可以包含 0 个或多个 `elif` 字句.  
最后的 `else` 是可选的.

最简单的判断语句:

    @@@ python
    if True: pass

.callout.info `pass` 表示什么也不做

<!SLIDE transition=turnUp>
# 单行判断语句

    @@@ python
    expression1 if boolan_expression else expression2

如果表达式 `boolan_expression` 的值为

  - `True` 表达式返回结果为 `expression1`
  - `False`: 表达式返回结果为 `expression2`

示例:

    @@@ python
    print("{0} file{1}".format(
        (count if count != 0 else 'no'),
        ('s' if count !=1 else ''))
    )

<!SLIDE transition=turnUp>
# 循环

Python 提供两种: `for...in` 和 `while`

## `while`

    @@@ python
    while boolen_expression:
        while_suite
    else:
        else_suite

`else` 为可选语句, 当循环正常退出时, `else` 子句将被调用

## `for ... in`

    @@@ python
    for expression in iterable:
        for_suite
    else:
        else_suite

和 while 一样, `else` 为可选语句, 当循环正常退出时, `else` 子句将被调用