# !-- coding:utf-8 --!
# CSDN.Applets  §01.1.1 例題  關鍵字 yield
# !@File:§01.2.py
# !@Author:
# !@Time:2019/12/26--14:12
L = []                      # 創建最終空例表L
def createGenerator(n):     # 創建發生器函數
    mylist = range(n)       # 生成例表
    print(list(mylist))     # 打印例表
    for i in mylist:        # 迭代此例表
        yield i*i           #返回例表元素的平方值

mygenerator = createGenerator(11)   # 調用發生器函數
print(mygenerator)          # 輸出調用函數的值

for i in mygenerator:       # 遍歷發生器函數所有元素
    L.append(i)             # 把元素加到最終例表
#   print(i,'；',end='')     # 輸出最終例表的元素
print(L)                    # 輸出最終例表

