def foo(a, b: 'annotating b', c: int) -> float:
    print(a + b +c)

foo('Hello', ',', 'World!')

foo(1, 2, 3)

print(foo.__annotations__)
