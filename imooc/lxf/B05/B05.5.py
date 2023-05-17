#慕课网 廖雪峰教程 B05.4 任务
import json                         # 导入 json

class Students(object):             # 定义类
    def __init__(self, strlist):    # 调用特殊方法 __init__( )
        self.strlist = strlist      # 第2参数，设置成字符串列表

    def read(self):                 # 定義一個 read( )方法
        print('本 read() 方法，自动给 json.load(%s)调用'%s)
        return (self.strlist)       # read 方法的返回值

s = Students('["Tim", "Bob", "Alice"]')     # 实例化对象，并导入字符串例表为属性。

# 调用 json.load()函数，会自动读取任意类的实例对象中的read()方法。
print(json.load(s))


