#慕课网 廖雪峰教程 B4.10 任務
class Person(object):
    __count = 0

    def __init__(self, name):   # 創建特殊方法，在實例化時自動調用。
        self.name = name
        Person.__count += 1

    @classmethod                # 創建類方法
    def how_many(cls):
        return cls.__count      # 返回類的私有屬性。

print(Person.how_many())        # 以類調用類方法。
p1 = Person('Bob')              # 創建實例
print(Person.how_many())        # 以類調用類方法。