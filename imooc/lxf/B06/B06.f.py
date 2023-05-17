#慕课网 廖雪峰教程 B06.8 任务   __slots__
class Person(object):

    __slots__ = ('name', 'gender')      # 允许的属性例表
    def __init__(self, name, gender):   # 定义构造方法
        self.name = name                # 定义属性
        self.gender = gender

class Student(Person):      # 创建子類

    __slots__ = ('score')   # 子類新增的屬性例表
    def __init__(self,name,gender,score):   # 定義構造方法，繼承父類的屬性
        super(Student, self).__init__(name, gender) # 採用 super 繼承父類的屬性
        self.score = score  # 定義新的屬性。

s = Student('Bob', 'male', 59)  # 創建實例對象，並賦初值
s.name = 'Tim'      # 修改姓名屬性
s.score = 99        # 修改分數屬性
print(s.score)      # 打印輸出分數


