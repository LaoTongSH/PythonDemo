#返回函数
def lazy_sum(*l):
    def sum():
        x = 0
        for n in l:
            x = x+n
        return x
    return sum()
f = lazy_sum(1,2,3,4,5,6,7,8)
print(f)
print("***********************************************")
def calc_prod(*lst):
    def product():
        x = 1
        for n in lst:
            x =x*n
        return x
    return product()
f = calc_prod(1,2,3,4)
print(f)