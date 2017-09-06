# 定义全局变量
x = 'global x'
l = [1]

def foo():
    global x
    x = x + ' change'
    y = 'local y'
    print(locals())
    #  print(globals())
    print(globals()['x'])
    globals()['name'] = 'test'

foo()
print(globals()['name'])
print(name)
