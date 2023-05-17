#慕课网 廖雪峰教程 B4.8 例题
class Person(object):
    def __init__(self, name,age):   #定義類的 __init__( ) 方法。
        self.__name = name  #雙下劃線屬性
        self.age = age

    def get_name(self):     #定义实例方法
        return self.__name  #返回雙下劃線屬性

p1 = Person('Bob',50)       #定義實例
print(p1.age)               #訪問類的屬性
try:
    print(p1.name)          #在外部不能訪問雙下劃線屬性，捕捉後報錯。
except AttributeError:
    print('attributeerror')

print(p1.get_name())        #在實例中，調用實例的方法，取得此方法中的屬性-參數。