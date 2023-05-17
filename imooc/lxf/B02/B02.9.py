#闭包
def fun1():
    x = [5]
    print(x[0])  #5
    def fun2():
        x[0] *= x[0]
        return x[0]
    return fun2()
print(fun1())  #25
print("*******************************")
def count():
    fs = []
    for i in range(1, 4):
        print(i)
        def f():
            print(i*i)
            return i*i
        fs.append(f)
    return fs
f1, f2 ,f3= count()
print(f1(),f2(),f3())
print(count(0))





