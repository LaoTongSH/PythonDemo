# !-- coding:utf-8 --!
# CSDN.Applets  §03.3.3 例題  克隆
# !@File:code\Csdn\Applets\03\ 03.7.py
# !@Author:
# !@Time:2020/1/22--21:10

from turtle import *

# 默認的箭頭造型
for x in range(5):          # 克隆5次
    goto(x * 20, x * 30)    # 在指定坐標克隆
    t = clone()             # 克隆
    up()                    # 抬筆

shape('turtle')             # 改變造型成海龜
for x in range(5):          # 克隆5次
    goto(x * 20, -50+x * -30)
    t = clone()
    up()

done()
