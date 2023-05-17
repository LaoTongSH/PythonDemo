#慕课网 廖雪峰教程 B05.6 例题  获取对象的信息
class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):
        return 'I am a Student, my name is %s' % self.name

s = Student('Bob', 'Male', 88)

print(type(s))
print(dir(s))
print(getattr(s,'name'))
print(getattr(s,'Bob','Matt'))
print(getattr(s,'name'))
print('-'*80)
print(getattr(s, 'age', 30))
try:
    print(getattr(s,'age'))
except AttributeError:
    print('Atributeerror')

