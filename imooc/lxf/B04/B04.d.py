#慕课网 廖雪峰教程 B4.9 任務
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 90)
print('Name:',p1.name,'; Score:',p1.score)
print('-'*70)
print(p1.get_grade)
print(p1.get_grade())

