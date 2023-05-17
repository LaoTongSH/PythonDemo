#慕课网 廖雪峰教程 B06.7 例题一
class Student:
    def __init__(self, s):  # 设置构造方法
        self.__score = s
        print('调用构造方法；并初始化成绩：',self.__score)

    def setScore(self, s):  # 设置__score的值
        print('调用(set)方法')
        if 0 <= s <= 100:
            self.__score = s

    def getScore(self):     # 得到__score的值
        print('调用(get)方法')
        return self.__score

print('1.创建实例对象')
s = Student(50)             # 创建一个实例对象
print('2.修改实例对象成绩')
s.setScore(100)             # 修改成绩
print('3.获取实例对象成绩')
print(s.getScore())         # 得到成绩  100











