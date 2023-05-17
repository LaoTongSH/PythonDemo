import time
from functools import reduce  #在 P3 中需添本行
def performance(f):
    def fn(*args, **kw):
        start = time.time()
#        print('call ' + f.__name__ + '()...')
        f(*args, **kw)
        end = time.time()
        print('用时:{}秒'.format(end-start))
        return f(*args, **kw)
    return fn
@performance
def factorial(n):
    time.sleep(1)
    return reduce(lambda x,y: x*y, range(1, n+1))
print(factorial(10))


# if __name__ == '__main__':
#     factorial(5)