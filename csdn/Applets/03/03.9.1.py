# !-- coding:utf-8 --!
# CSDN.Applets  §03.4.1 例題 動畫演示 慢動作和快動作
# !@File:code\Csdn\Applets\03\03.9.1.py
# !@Author:
# !@Time:2020/1/29--9:10

import turtle as screen
from turtle import *

# 1.書寫標題
screen.up()             # 抬筆
screen.goto(-150,250)   # 到指定坐標點
L = ['慢','動','作','和','快','動','作']   # 定義字典
for j in range(7):      # 循環
    screen.down()       # 落筆
    screen.write(L[j], align="center", font=("Courier", 18, "bold"))
    screen.up()         # 抬筆，移動筆不落痕跡
    screen.fd(50)       # 前進

# 2.動畫演示
dist = 2                # 初始化步伐
screen.home()           # 返回原點
screen.down()           # 落筆
for i in range(50):     # 循環
	screen.fd(dist)     # 前進
	screen.rt(90)       # 右轉90度
	dist +=5            # 步伐增加
# 3.關閉了動畫，程序快速走完
screen.pensize(3)		# 設置筆寬
screen.color('red')     # 設置紅筆
screen.tracer(3,25)     # 關閉動畫顯示
for i in range(50):     # 循環
	screen.fd(dist)     # 前進
	screen.rt(90)       # 右轉 90度
	dist +=5            # 步伐增加

done()                  # 結束
