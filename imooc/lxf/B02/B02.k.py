import time

#import functools
def timeit(func):
   #@functools.wraps(func)
   def wrapper():
      start = time.clock()
      func()
      end =time.clock()
      print("FacName:",func.__name__,"(); used:", (end - start)*100000)
   return wrapper

@timeit
def foo():
   print("in foo()......")

foo()
print("foo name: ", foo.__name__)
