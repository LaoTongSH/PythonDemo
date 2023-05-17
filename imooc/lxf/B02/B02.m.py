# -- coding:utf-8 --
import datetime, functools
from functools import reduce  #在 P3 中需添本行

def performance(unit):
    def func_outer(func):
        @functools.wraps(func)
        def func_inner(*args, **kwargs):
            print('装饰器函数传递的参数：',unit)
            print('被装饰的原函数名称：' + func.__name__)
            return func(*args, **kwargs)
        return func_inner
    return func_outer

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))
print('函数名称:',factorial.__name__)

