#慕课网 廖雪峰教程 B06.1 任務   __str__( ) 方法
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student: %s, %s, %s)' % (self.name, self.gender,self.score)

s = Student('Bob', 'male', 88)
print(s)



