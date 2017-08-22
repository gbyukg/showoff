<!SLIDE bullets incremental>
# 匿名函数

Python 允许我们创建一个没有函数名的函数, 称之为 匿名函数, 匿名函数使用 `lambda` 关键字定义:

    @@@ python
    lambda param1, param2: expression

匿名函数可以接受0至多个参数, 各个参数之间使用逗号(`,`)分隔

expression 中不能包含任何条件判断语句和循环语句, 并且不能包含 `return` 语句, 而函数的返回结果就是 `expression` 执行的结果.
