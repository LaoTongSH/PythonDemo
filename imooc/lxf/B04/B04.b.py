#慕课网 廖雪峰教程 B4.8 任務
class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score  # 雙下劃線屬性

    def get_grade(self):
        return self.__score

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print('A:優秀',p1.get_grade())
print('B:及格',p2.get_grade())
print('C:不及格',p3.get_grade())
