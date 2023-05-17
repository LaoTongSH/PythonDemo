# !-- coding:utf-8 --!
# CSDN.Applets  §03.2.3 例题  递归方法画树
# !@File:code\Csdn\Applets\03\03.4.py
# !@Author:
# !@Time:2020/1/10--9:49

import turtle
p = turtle.Pen()
p.penup()
p.goto(0, -200)
p.setheading(90)
p.pensize(7)
p.pencolor('green')
p.pendown()

def branch(plist, len):            # 自定义函数，画树枝
    if (len > 15):                 # 递归的退出条件
        list = []                  # 新画笔列表
        for p in plist:            # 遍历旧画笔列表
            p.forward(len)
            q = p.clone()
            p.left(65)
            q.right(65)
            list.append(p)         # 存入新画笔列表
            list.append(q)         # 存入新画笔列表
        branch(list, len * 0.65)   # 递归，list为新画笔列表，树枝长65%

branch([p], 200)
turtle.done()