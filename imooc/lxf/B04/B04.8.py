#慕课网 廖雪峰教程 B4.7 例题
class Person(object):
    address = '上海'      #賦值類屬性
    def __init__(self, name):
        self.name = name
p1 = Person('Bob')      #創建二個實例。
p2 = Person('Alice')

print('類屬性:',Person.address,'| p1屬性:',p1.address,'| p2屬性:',p2.address)

p2.address = '台湾'       #僅修改實例P2的屬性，為p2綁定了和類同名的屬性。
print('類屬性:',Person.address,'| p1屬性:',p1.address,'| p2屬性:',p2.address)
print("************************************")
del p2.address          #刪除實例的屬性，又顯示類的屬性。
print('類屬性:',Person.address,'| p1屬性:',p1.address,'| p2屬性:',p2.address)

Person.address = '桃園' #修改了類的屬性。
print('類屬性:',Person.address,'| p1屬性:',p1.address,'| p2屬性:',p2.address)
