<!SLIDE bullets incremental>
# 匿名函数

Python 允许我们创建一个没有函数名的函数, 称之为 匿名函数, 匿名函数使用 `lambda` 关键字定义:

    @@@ python
    lambda param1, param2: expression

匿名函数可以接受0至多个参数, 各个参数之间使用逗号(`,`)分隔

expression 中不能包含循环语句, 并且不能使用 `return` 语句返回函数体, 而函数的返回结果就是 `expression` 执行的结果.

    @@@ python
    lambda x: "" if x == 1 else "s"

.callout.info lambda 在 Python 中同样也是对象, 这意味着我们可以将 lambda 赋值给一个变量, 或是作为参数传递给一个函数, 或是作为一个函数的返回值返回.

<!SLIDE bullets incremental>
# 内建函数 `map()` 和 `filter()`

函数 | 说明
--- | ---
`map(func, seq1[, seq2...])` | 将序列中的每个元素依次作为参数传递给函数 `func`, 并将结果以列表的形式返回.
`filter(func, seq)`          | 调用一个 `bool` 函数 `func` 来迭代 `seq` 中的每个元素, 返回一个使 `func`返回值为 `true` 的元素序列
