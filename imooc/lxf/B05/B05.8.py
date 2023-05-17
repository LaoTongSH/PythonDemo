#慕课网 廖雪峰教程 B05.6 任务  修改 __init__
class Person(object):
    # 在 __init__( ) 初始化-構造-私有方法中用可變字符串 **kw 做參數
    def __init__(self, name, gender, **kw):
        self.name = name
        self.gender = gender
        for k, v in kw.items():     # 在P2版本中是 iteritems()函数
            setattr(self, k, v)     # 注意書寫語法格式。

p = Person('Bob', 'Male', age=18, course='Python')  # 實例化對象
print(p.age)
print(p.course,'\n')                # 加一個換行符 \n。
print('My name is:',p.name,'; My gender is:',p.gender,'；')
print('My age  is：',p.age,'；My course is:',p.course,'。')
print(filter(lambda x: x[0]!='_', dir(p)))