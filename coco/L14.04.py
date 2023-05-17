# !-- coding:utf-8 --!
# !核桃: L14.枚舉與遞歸
# !@File:code\Coco\ L14.04.py
# !@Author:
# !@Time:2022/2/7--15:40
# !打印圖案

n=6
for i in range(1,n+1):              # 第一層遍歷，為打印空格 正三角形
    print(' ' * (n - i), end='')    # 打印空格
    for j in range(1, 2 * i):       # 第二層遍歷，為打印星星
        print('*', end='')          # 打印 “*”
    print()
for i in range(n-1,0,-1):           # 倒三角形
    print(' ' * (n - i), end='')
    for j in range(1, 2 * i):
        print('*', end='')
    print()