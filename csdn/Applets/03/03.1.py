# !-- coding:utf-8 --!
# CSDN.Applets  §03.1 例題  用海龜作圓一
# !@File:code\Csdn\Applets\03\03.1.py
# !@Author:
# !@Time:2020/1/6--19:41

import turtle as t  # 導入模塊
import time

t.color("red", "yellow")
t.setup(840,500)    # 设置主窗口的大小为840*500
t.speed(1)          # 设置画笔速度为10
T = 2               # 设置停顿时间2秒

t.penup()           # 抬筆
t.goto(-350,150)    # 到題字點
t.pendown()         # 落筆
t.write("海龜作圓", font=('Arial', 40, 'normal'))

t.penup()           # 抬筆
t.goto(-350,100)    # 到題字點
t.pendown()         # 落筆
t.write("1.箭頭向下、逆時針", font=('Arial', 20, 'normal'))

t.penup()           # 抬筆
t.goto(-350,50)     # 到題字點
t.pendown()         # 落筆
t.write("2.箭頭向上、順時針", font=('Arial', 20, 'normal'))

t.penup()           # 抬筆
t.goto(-350,0)      # 到題字點
t.pendown()         # 落筆
t.write("3.箭頭向右、逆時針", font=('Arial', 20, 'normal'))

t.penup()           # 抬筆
t.goto(-350,-50)    # 到題字點
t.pendown()         # 落筆
t.write("4.箭頭向左、逆時針", font=('Arial', 20, 'normal'))

t.penup()           # 抬筆
t.goto(150,0)       # 到起點
t.pendown()         # 落筆

# 畫圓 1
t.setheading(270)   # 筆的方向 向下
t.color("Brown")    # 設置棕筆
t.pensize(20)       # 設置筆寬
t.dot(5,"red")      # 畫第一個圓的起點。
time.sleep(T)       # 停頓
t.circle(100)       # 逆時針畫圓。
time.sleep(T)       # 停頓

# 畫圓 2
t.setheading(90)    # 筆的方向 向上
t.color("blue")     # 設置藍筆
time.sleep(T)       # 停頓
t.pensize(5)        # 設置筆寬
t.circle(-100)      # 順時針畫圓。
time.sleep(T)       # 停頓

# 畫圓 3
t.setheading(0)     # 筆的方向 向右
t.color("red")      # 設置紅筆
time.sleep(T)       # 停頓
t.pensize(10)       # 筆寬
t.circle(100)       # 逆時針畫圓。
time.sleep(T)       # 停頓

# 畫圓 4
t.setheading(180)   # 筆的方向 向左
t.color("black")    # 設置黑筆
time.sleep(T)       # 停頓
t.pensize(5)        # 筆寬
t.circle(100)       # 逆時針畫圓。
time.sleep(T)       # 停頓

t.done()            # 結束。
