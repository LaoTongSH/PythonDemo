#慕课网 廖雪峰教程 B06.9 例題
class Person(object):                   # 創建類
    def __init__(self, name, gender):   # 創建構造方法，含二個屬性。
        self.name = name
        self.gender = gender
        print('My name is %s;\nMy gender is %s。' %(name,gender))

    def __call__(self, friend):         # 創建了 __call__( ) 方法，一個屬性參數
        print('My name is %s...' % self.name)
        print('My friend is %s...' % friend)

p = Person('Bob', 'male')       # 創建實例對象。
print('-'*80)
p('Ti')                         # 實例名( )，即含參數自動調用 __call__( ) 方法。



