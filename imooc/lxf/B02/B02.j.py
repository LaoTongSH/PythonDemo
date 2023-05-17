import datetime
from functools import reduce  #在 P3 中需添本行

def performance(unit):
    def func_outer(func):
        def func_inner(*args, **kwargs):
            if unit == 'ms':
                print('call ' + func.__name__ + '() in ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
            else:
                print('call ' + func.__name__ + '() in ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
            return func(*args, **kwargs)
        return func_inner
    return func_outer

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))
