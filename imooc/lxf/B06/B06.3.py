#慕课网 廖雪峰教程 B06.3 例题  P2的 __cmp__( ) 方法 在 P3中已取消，採用新方法排序
from operator import attrgetter                         # 代替 P2 的 __cmp__ 方法
class Student(object):                  # 定義類
    def __init__(self, name, score):    # 構造方法
        self.name = name
        self.score = score
    def __str__(self):                  # 轉字符串方法
        return 'Student(%s: %s)' % (self.name, self.score)     # 返回格式化字符串

#    __repr__=__str__                    # 不能縮進，縮進輸出內存情況

    # def __repr__(self):                 # 定義 __repr__方法
    #     return 'Student({})'.format(self.name,self.score)

L = [Student('Tim', 99), Student('Bob', 99), Student('Alice', 77)]
print(L)

print(sorted(L, key=attrgetter('score','name'),reverse=False))
print(sorted(L, key=attrgetter('score','name'),reverse=True))