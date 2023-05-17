#慕课网 廖雪峰教程 B06.6 例题   有理数化整数 __int__( ) 方法
class Rational(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
    def __int__(self):
        return self.p // self.q  # 取接近除数的整数，相当于除法后四舍五入。

print(7/2)
print(int(Rational(7, 2)))
print('-'*80)
print(1/3)
print(int(Rational(1, 3)))



