#慕课网 廖雪峰教程 B4.7 任务
class Person(object):
    __count = 0

    def __init__(self,name):
        self.name = name
        Person.__count += 1         #添加一個實例，計算器+1
        print(Person.__count)       #在類的內部訪問類的雙下劃線屬性

p1 = Person('Bob')
p2 = Person('Alice')
try:
    print(Person.__count)       #在外部不能訪問雙下劃線屬性，捕捉後報錯。
except AttributeError:
    print('attributeerror')



