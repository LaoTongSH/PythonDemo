#慕课网 廖雪峰教程 B06.8 例题   __slots__
class Student(object):
    __slots__ = ('name', 'gender', 'score')     # 允许的属性例表

    def __init__(self, name, gender, score):    # 构造方法
        self.name = name
        self.gender = gender
        self.score = score

s = Student('Bob', 'male', 59)      # 创建实例对象，并赋初值。
s.name = 'Tim'      # OK    修改 name。
s.score = 99        # OK    修改分数
try:
    s.grade = 'A'   # 修改 grade(年级)，不在例表中的属性 会报错
except AttributeError:
    s.gender = 'female'     # 能修改 gender
print(s.gender)





