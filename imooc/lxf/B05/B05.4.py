#慕课网 廖雪峰教程 B05.4 例題
class Person(object):                   # 定義父類
    def __init__(self, name, gender):   # 定義構造函數方法
        self.name = name
        self.gender = gender
    def whoAmI(self):                   # 定義一個 whoAmI函數
        return 'I am a Person, my name is %s' % self.name   # whoAmI 函數返回值

class Student(Person):                  # 定義子類
    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score
    def whoAmI(self):                   # 定義一個 whoAmI函數
        return 'I am a Student, my name is %s' % self.name  # whoAmI 函數返回值

class Teacher(Person):                  # 定義子類
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):                   # 定義一個 whoAmI函數
        return 'I am a Teacher, my name is %s' % self.name  # whoAmI 函數返回值

def who_am_i(x):            # 定義函數，參數為 x
    print(x.whoAmI())       # 調用 whoAmI( )函數，並打印結果

p = Person('Tim', 'Male')       # 三個類都實例化
s = Student('Bob', 'Male', 88)
t = Teacher('Alice', 'Female', 'English')

who_am_i(p)     # 都以實例化對象調用函數 who_am_i
who_am_i(s)
who_am_i(t)
