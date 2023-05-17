#慕课网 廖雪峰教程 A08.5 例题   創建 斐波那契数列
def Fibonacci(num):     # 定义函数
    i = 2
    F = [0,1]           # 初始化斐波那契数列
    while i < num:
        F.append(F[i - 2] + F[i - 1])   # 添加新元素
        i += 1
    return F            # 返回斐波那契数列

print(Fibonacci(15))    # 调用并输出斐波那契数列 注：参数需要 >1

