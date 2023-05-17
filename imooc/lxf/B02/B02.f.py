from functools import reduce  #在 P3 中需添本行
def log(f):
    def fn(*args, **kw):
        print('call ' + f.__name__ + '()...')
        return f(*args, **kw)
    return fn
@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))
@log
def add(x, y):
    return x + y
print(add(10, 2))


