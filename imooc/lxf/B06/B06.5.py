#慕课网 廖雪峰教程 B06.4 任務   __len__( ) 方法 創建 斐波那契数列
class Fib(object):

    def __init__(self, num):            # 初始構造方法，參數num
        self.num = num
        self.fibonacci = [0, 1]         # 創建 斐波那契数列 第0,1項
        i = 2
        while i < self.num:             # 用循環創建 斐波那契数列
            # 用 L.append(..) 為 List 添加新的元素。
            self.fibonacci.append(self.fibonacci[i - 2] + self.fibonacci[i - 1])
            i += 1

    def __str__(self):                  # 定義 __str__() 方法
        return str(self.fibonacci)

    def __len__(self):                  # 定義 __len__( ) 方法
        return len(self.fibonacci)      # 返回元素的個數。

f = Fib(10)         # 類的實例化，對象為 List ，
print(f)
print('斐波那契数列中，元素的個數：',len(f))



