#慕课网 廖雪峰教程 B06.5 任务   有理数的四则运算
class Rational(object):         # 定义有理数类
    def __init__(self, p, q):   # 定义构造方法，二个属性。
        self.p = p
        self.q = q
        for i in range(2,self.q*self.p):       # 以分子、分母积为约分参数
            while(self.p%i==0 and self.q%i==0):
                self.p = self.p//i
                self.q = self.q//i

    def __add__(self, r):       # 定义 +
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __sub__(self, r):       # 定义 -
        return Rational(self.p * r.q - self.q * r.p, self.q * r.q)

    def __mul__(self, r):       # 定义 *
        return Rational(self.p * r.p, self.q * r.q)

    def __div__(self, r):       # 定义 /
        return Rational(self.p * r.q, self.q * r.p)

    def __str__(self):          # 定义了输出的分数结构： p/q
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__          # 在本案可用可不用

r1 = Rational(1, 2)             # 实例化对象1
r2 = Rational(1, 4)             # 实例化对象2
print(r1 + r2)                  # 计算 +
print(r1 - r2)                  # 计算 -
print(r1 * r2)                  # 计算 *
try:                            # 计算 /
    print(r1 / r2)  # 系统不接受这种书写方法
except TypeError:   # 捕捉到错误，执行下面语句。
    print(Rational.__div__(r1,r2))  # 采用这种格式书写有理数的除法。



