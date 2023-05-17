#慕课网 廖雪峰教程 B05.5 任务
class Person(object):       # 定义第1父类
    pass

class Student(Person):      # 定义第1.1子类
    pass

class Teacher(Person):      # 定义第1.2子类
    pass

class SkillMixin(object):           # 定义第2父类
    pass

class BasketballMixin(SkillMixin):  # 定义第2.1子类
    def skill(self):                # 定义第2.1子类的方法
        return 'basketball'

class FootballMixin(SkillMixin):    # 定义第2.2子类
    def skill(self):                # 定义第2.2子类的方法
        return 'football'

class BStudent(Student,BasketballMixin):    # 定义第一多重子类 会打篮球的学生
    pass

class FTeacher(Teacher,FootballMixin):      # 定义第二多重子类 会踢足球的教师
    pass

s = BStudent()              # 第一多重子类实例化
print(s.skill())            # 调用 skill() 方法并打印输出

t = FTeacher()              # 第二多重子类实例化
print(t.skill())            # 调用 skill() 方法并打印输出
