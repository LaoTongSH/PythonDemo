#慕课网 廖雪峰教程 B06.5 例题   有理数的四则运算
class Rational(object):
    def __init__(self, p, q):   # 定义构造方法
        self.p = p
        self.q = q

    def __add__(self, r):       # 定义有理数的加法，返回值等于一个新的实例对象
        return Rational(self.p * r.q + self.q * r.p, self.q * r.q)

    def __str__(self):          # 定义了输出的分数结构： p/q
        return '%s/%s' % (self.p, self.q)

    __repr__ = __str__

r1 = Rational(1,8)              # 实例化对象1 = 1/3 ；生成第1个有理数
r2 = Rational(1,2)              # 实例化对象2 = 1/2 ；生成第2个有理数
print(r1+r2)                    # 二个有理数相加。



