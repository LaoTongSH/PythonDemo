#慕课网 廖雪峰教程 B06.7 例题二   特殊属性 @property
class Student:
    def __init__(self, s):      # 设置构造方法
        print('调用构造方法')
        self.__score = s

    @property                   # 调用 get 方法，获得 score
    def score(self):
        print('getter被调用')
        return self.__score

    @score.setter               # 调用 set 方法，赋值 score
    def score(self, s):
        print('setter被调用')
        if 0 <= s <= 100:
            self.__score = s

print('1.创建实例对象')
s = Student(50)         # 创建一个实例对象，赋值成绩：50
print('2.修改实例对象的属性')
try:
    s.setScore(100)     # 修改成绩为：100 这种方法系统会报错！！
except AttributeError:  # 捕捉到错误，执行下面语句。
    s.score = 100       # 修改成绩为：100
print('3.获取实例对象的属性')
score = s.score
print('4.输出实例对象的属性')
print('成绩是{}'.format(score))







