#慕课网 廖雪峰教程 B06.4 例题   __len__( ) 方法
class Students(object):         # 定义類
    def __init__(self, *args):  # 定義私有的構造方法
        self.names = args

    def __len__(self):          # 定義 __len__( ) 方法
        return len(self.names)  # 返回元素的個數。

ss = Students('Bob', 'Alice', 'Tim','Make')     # 實例化並賦值，共4個元素。
print(ss)
print('Students：',len(ss))



