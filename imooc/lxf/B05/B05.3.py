#慕课网 廖雪峰教程 B05.3 任務
class Person(object):       # 定義父類
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):      # 定義子類
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

class Teacher(Person):      # 定義子類
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course

t = Teacher('Alice', 'Female', 'English')   # 創建 Teacher 子類的實例。

print(isinstance(t,Person))
print(isinstance(t,Student))
print(isinstance(t,Teacher))
print(isinstance(t,object))
