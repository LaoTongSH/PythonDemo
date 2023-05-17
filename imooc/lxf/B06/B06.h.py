#慕课网 廖雪峰教程 B06.9 任務  用 __call__( ) 方法 創建斐波那契数列
class Fibonacci(object):        # 創建類

    def __call__(self, num):    # 創建了 __call__( ) 方法，一個屬性參數
        i = 2
        F = [0, 1]  # 初始化斐波那契数列
        while i < num:
            F.append(F[i - 2] + F[i - 1])  # 添加新元素
            i += 1
        return F

fib = Fibonacci()       # 創建實例對象
print(fib(10))          # 调用并输出斐波那契数列 注：参数需要 >1

