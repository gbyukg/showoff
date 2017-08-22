# exception

至少应该存在一个 `except` 语句, 但 `else` 和 `finally` 都是可选的, 当没有异常被捕获到的时候,

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 当我们的程序中出现一些错误的时, Python 默认会打印出错误信息, 并终止程序的运行.
    # 比如我们定义一个字典, 并访问字典中不存在的一个键时
    d = {'a':1, 'b':2}
    #  d[6]
    # 程序直接报错: KeyError: 6 错误, 并终止程序的运行.

    # 但有些时候我们希望能够自己处理这些错误, 当遇到这些错误后,
    # 我们可能希望输出可读性更好的自定义错误信息,
    # 或是在发现这些错误信息后, 做一些相应的操作后, 让程序继续执行,
    # 比如说在这个例子中, 当访问一个不存在的键时,
    # 我们希望打印出一个提示信息, 并将这个键加到字典中
    # 这时我们就需要使用 Pthon 中的异常处理机制
    # 将可能会发生错误的代码放到 try 字句中
    # 在用 except 捕获可能会发生的异常错误.
    # 当有异常发生时, Python 会去 except 语句中查看是否有相应的异常信息
    # 如果找到了, 就会执行except语句,
    # 如果没有在 except 语句中找到对应的异常信息
    # 则异常向上抛出, 抛给调用它的代码, 直到程序的调用出.
    try:
        d[6]
        #  d['a'] / 0
    # 而除数为 0 会抛出 ZeroDivisionError 异常
    except Exception:
        print('Key does not exist in the dictionary d. Adding it.')

    # 在这个例子中, 我们使用了 KeyError 异常.
    # 执行脚本, 与我们的期待一样

    #####################################
    # 我们继续看这个例子, 修改这段代码:
    #  d['a'] / 0
    # 我们知道, 无论什么时候, 任何数除以 0 都是错误的.
    # 所以这段代码会抛出异常,
    # 虽然它能够正确捕获到异常, 但是异常显示的结果明显是不对的.
    # 在所有的编程语言中, 都有各种各样的异常来针对不同的错误, Python 也不例外
    # 所以我们可以通过增加不同的异常来捕获不同的错误.
    # 当访问一个不存在的 键 时, 会抛出 KeyError 异常.
    # 因此增加 KeyError 异常的处理
    #  except KeyError:
        #  print('Key does not exist in the dictionary d. Adding it.')
    # 而除数为 0 会抛出 ZeroDivisionError 异常
    #  except ZeroDivisionError:
        #  print("Error, divisor is 0.")
    # 当有多个 except 字句时, Python 会按照定义except 的顺序, 从上至下依次查找,
    # 直到找到有符合的异常, 如果执行到最后一个 except 语句都没有符合的异常
    # 则向上抛出这个异常直到程序的最顶端后打印出错误信息并终止程序.

    #####################################
    # 我们不仅可以在 except 语句中直接捕获这个异常, 还可以通过捕获发生异常的父异常来捕获到.
    # 在这个例子中, KeyError 异常继承自它的父异常 `LookupError` 异常(从我给出的列表中可以看到),
    # 因此我们还可以通过捕获 `LookupError` 异常来达到我们的目的.
    # except LookupError as e:
    #  except Exception:
        #  print('Error')
    # 这里有一点需要注意一下,
    # 如果有多个 except 语句, 一定要把范围小的异常放在最上面.
    # 如果把 Exception 异常类放到了第一个位置,
    # 因为 Exception 异常类是所有异常类的总父类, 即所有异常都继承自 Exception 异常类.
    # 那么它就会捕获到任何发生的异常, 而下面的 except 也就不会被执行了.
    # 因此通常将 Except 放到最后, 来捕获为捕获到的异常

    # 在这个例子中, KeyError 范围小于 LookupError, 因为 KeyError 是 LookupError 的子类,
    # 而 LookupError 又是 Exception 的子类.
    # 所以通常在最后使用 Exception 来捕获我们没有指定的所有异常.

    #####################################
    # 我们还可以在一个 except 语句中同时获取多个异常,
    # 这些异常以元组的形式出现, 如:
    #  except (KeyError, LookupError):
    # 这样, 当出现 IndexError 异常时, 我们也能在这个 except 语句中捕获到
    # 注意: IndexError 也是 LookupError 的子类

    #####################################
    # 在这个例子中, 我们虽然捕获到了我们需要的异常信息.
    # 但是在提示信息中, 我们希望能过获取到更详细的错误信息
    # 这个时候就可以通过在 except 语句的最后使用 as 语法, 如:
    #  except (KeyError, LookupError) as e:
        #  print('Key [{}] does not exist in the dictionary d. Adding it.'.format(e))

    #####################################
    # else
    # 我们还可以在最后一个 except 语句后面添加 else 子句
    # else 中的子句会在没有发生异常的时候被执行
    #  else:
        #  print("No exception")

    #####################################
    # finally
    # finally 语句则无论是否有异常抛出, 都会被执行
    #  finally:
        #  print("Finally clause")

    try:
        #  d['a']
        d['c']
        #  5/0
    except (KeyError, LookupError) as e:
        print(e)
    except Exception:
        print('Catch an exception')
    else:
        print("No exception")
    finally:
        print("Finally clause")

# 自定义异常

    @@@ python
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-

    # 自定义异常实际上就是一种自定义类型(自定义类), 我们将会在后面讲解类.
    # 但是创建一个类实在很简单, 只需使用 class 关键字即可创建一个类
    # 其中的 `baseException` 指定自定义异常类的父类, 父类必须是 `Exception` 类, 或是 `Exception` 的某个子类.

    # 考虑这样一个例子
    # 查找一个表中某个字段是否含有指定的元素

    table = (
        (('C1B1A1S', 'C1B1A1S-name'),),
        (('E1C1B1A1S', 'E1C1B1A1S-name'),),
        (('C2B1A1S', 'C2B1A1S-name'),),
        (('type4', 'E2C2B1A1S-name'),),
    )

    found = False
    target = 'C2B1A1S-name'
    for row, record in enumerate(table):
        for column, field in enumerate(record):
            for index, item in enumerate(field):
                if item == target:
                    found = True
                    break
            if found:
                break
        if found:
            break
    if found:
        print("found at ({0}, {1}, {2})".format(row, column, index))
    else:
        print("not found")

    # 使用异常实现
    class FoundException(Exception): pass
    try:
        for row, record in enumerate(table):
            for column, field in enumerate(record):
                for index, item in enumerate(field):
                    if item == target:
                        raise FoundException()
    except FoundException:
        print("found at ({0}, {1}, {2})".format(row, column, index))
    else:
        print("not found")