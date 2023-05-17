#慕课网 廖雪峰教程 B06.7 任务   特殊属性 @property
class Student(object):

    def __init__(self, name, score):    # 定义构造方法
        self.name = name
        self.__score = score

    @property                       # 定义 get 方法
    def score(self):
        return self.__score

    @score.setter                   # 定义 set 方法
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score

    @property                       # 定义只读的 grade 方法
    def grade(self):
        if self.__score > 80:       # 按条件分类
            grade = 'A'
        elif self.__score < 60:
            grade = 'C'
        else:
            grade = 'B'
        return grade                # 返回分类结果

s = Student('Bob', 59)      # 创建实例对象，赋初值。
print(s.grade)              # 输出

s.score = 60                # 修改分值
print(s.grade)              # 输出

s.score = 99                # 修改分组
print(s.grade)              # 输出
