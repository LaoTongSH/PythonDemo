#慕课网 廖雪峰教程 B06.1 例题   __str__( ) 方法
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def __str__(self):      # 定义__str__()方法
        return '(Person: %s, %s)' % (self.name, self.gender)
L=[1,2,3,4]                 # 定义List 例表
print(L)
print(L.__str__())
print('-'*80)
print(Person)               # 打印 類
p = Person('Bob', 'male')   # 類的實例對象
print(p)
print(p.__str__())





