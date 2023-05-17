# !-- coding:utf-8 --!
# !Imooc.lxf: A.MK.Lxf 入門   同时遍历二个列表
# !@File:code\imooc\lxf\ A.13.6.py
# !@Author:
# !@Time:2020/11/13--12:16
# !platform：Python 3.6.5-64 & PyCharm 2.2 & Mysql 8.0.18 & Navicat 12

# 1.遍历长度相同的列表
L1=[1,3,5,7,9]
L2=[2,4,6,8,0]
sum = 0
for a,b in zip(L1,L2):
    sum = sum + a*b
print(sum)

# 2.遍历长度不同的列表
from itertools import zip_longest
a = ['A','B','C',4,5,'F']
b = ['xyg',12,'ASD']

for i,j in zip_longest(a,b):
    print(i,j)

