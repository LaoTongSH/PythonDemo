#Python 中的闭包
def count():
    fs = []
    for i in range(1, 4):
        x = i*i
        fs.append(x)
    return fs
print(count())
f1, f2, f3 = count()
print(f1,f2,f3)