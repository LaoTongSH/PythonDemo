# !-- coding:utf-8 --!
# CSDN.Applets  §03.2.1 例题 用海龟作圆弧
# !@File:code\Csdn\Applets\03\03.2.py
# !@Author:
# !@Time:2020/1/6--13:51

import turtle as t
import time

t.color("red", "yellow")
t.setup(840,500)    # 设置主窗口的大小为840*500
t.speed(1)          # 设置画笔速度为10
T = 2               # 设置停顿时间2秒
t.shape('turtle')   # 显示海龟

t.penup()           # 抬筆
# 畫圓 1
t.goto(150,150)     # 到第一個圓的起點
t.setheading(270)   # 筆的方向 向下
t.pencolor("red")   # 設置紅筆
t.pendown()         # 落筆
t.dot(10,"red")     # 還第一個圓的起點。
time.sleep(T)       # 停頓
t.circle(50,270)    # 逆時針畫圓。
time.sleep(T)       # 停頓

# 畫圓 2
t.goto(-150,200)    # GO 第二個圓的起點,海龟向左
t.pencolor("black") # 設置黑筆
t.dot(10,"red")     # 畫第二個圓的起點
t.circle(50,270)    # 逆時針畫第二個圓
time.sleep(T)       # 停頓

# 畫圓 3
t.goto(-100,-150)   # GO 第三個圓的起點，海龜方向向上！
time.sleep(T)       # 停頓
t.color("blue")     # 設置藍筆
t.dot(10,"blue")    # 畫第三個圓的起點
t.circle(50,270)    # 逆時針畫第三個圓
time.sleep(T)       # 停頓

# 畫圓 4
t.goto(200,-200)    # GO 第四個元旦起點，海龜方向向右
t.color("Brown")    # 設置棕筆
t.dot(10,"Brown")   # 畫第四個圓的起點
t.circle(50,270)    # 逆時針畫第四個圓
time.sleep(T)       # 停頓

t.goto(150,150)     # GO 第一個圓的起點，海龟方向向下
t.penup()           # 抬筆
t.home()            # 回原点
t.pendown()         # 落筆
for i in range(1,7):
    t.setheading(90)    # 海龟向上
    t.circle(-25,180)   # 順時針畫半個圓
for i in range(1,4):
    t.setheading(270)   # 海龟向下
    t.circle(-50,180)   # 順時針畫半個圓

t.done()            # 結束。
