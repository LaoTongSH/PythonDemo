#高階函數 §02.2 例題  §02.3 任務
import math
def add(x,y,f):
    return f(x)+f(y)
print(add(-5,9,abs))
print(add(25,9,math.sqrt))