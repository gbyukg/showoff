<!SLIDE center subsection>
# Python 中的异常

<!SLIDE transition=turnUp>
# 捕获异常
基本语法:

    @@@ python
    try:
        try_suite
    except exception_group1 as variable1:
        except_suite1
    ...
    except exception_groupN as variableN:
        except_suiteN
    else:
        else_suite
    finally:
        finally_suite

`else` 当没有异常发生时, `else` 子句将被调用

`finally` 无论是否发生异常, `finall` 子句将总是被调用

<!SLIDE transition=turnUp>
# 抛出异常

在程序中我们可以使用 `raise` 手动抛出一个异常, 语法为:

    @@@ python
    raise exception(args)

其中 `args` 是一个可选的参数, 一个用于描述异常信息的字符串.

.callout.info 当我们在执行 python 脚本时, 如果指定了 `-o` 或 `-oo` 参数, 程序中的断言将不会被执行.

<!SLIDE transition=turnUp>
# 自定义异常

语法:

    @@@ python
    class exceptionName (baseException): pass

其中的 `baseException` 指定自定义异常类的父类, 父类必须是 `Exception` 类, 或是 `Exception` 的某个子类.

<!SLIDE transition=turnUp>
# 异常列表

BaseException

- SystemExit
- KeyboardInterrupt
- GeneratorExit
- Exception
  - StopIteration
  - StandardError
    - BufferError
      - ArithmeticError
        - FloatingPointError
        - OverflowError
        - ZeroDivisionError
      - AssertionError
      - AttributeError
      - EnvironmentError
        - IOError
        - OSError
          - WindowsError (Windows)
          - VMSError (VMS)
        - EOFError
        - ImportError
        - LookupError
          - IndexError
          - KeyError
        - MemoryError
        - NameError
          - UnboundLocalError
        - ReferenceError
        - RuntimeError
          - NotImplementedError
        - SyntaxError
          - IndentationError
            - TabError
        - SystemError
        - TypeError
        - ValueError
          - UnicodeError
            - UnicodeDecodeError
            - UnicodeEncodeError
            - UnicodeTranslateError
- Warning
  - DeprecationWarning
  - PendingDeprecationWarning
  - RuntimeWarning
  - SyntaxWarning
  - UserWarning
    - FutureWarning
  - ImportWarning
  - UnicodeWarning
  - BytesWarning