from functools import reduce  #在 P3 中需添本行
def log(f):
    def fn(x):
        print('call ' + f.__name__ + '()...')
        return f(x)
    return fn

@log
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))



