# !-- coding:utf-8 --!
# CSDN.Applets  帶有秒刻度的複雜鐘的盤面
# !@File:code\Csdn\Applets\03\03.9.2.1.py
# !@Author:
# !@Time:2020/1/11--11:43

import turtle
from datetime import *
import time
def Skip(step):                     # 畫筆運動函數，參數：運動步數
    turtle.penup()                  # 抬筆
    turtle.forward(step)            # 前進
    turtle.pendown()                # 落筆

# 3.1 定义指针函数，参数：指针名称、长度。创建 turtle。
def mkHand(name, length, wh):
    turtle.reset()                  # 清空窗口，重置 turtle 为起始状态
    Skip(-length * 0.1)             # 调用 画笔运动函数
    turtle.begin_poly()             # 开始记录多边形的顶点。当前的乌龟位置是多边形的第一个顶点。
    turtle.pencolor("#ff5500")      # 設置顏色
    turtle.turtlesize(wh)
    turtle.forward(length * 1.1)

    turtle.end_poly()               # 停止记录多边形的顶点。当前的乌龟位置是多边形的最后一个顶点。将与第一个顶点相连。
    handForm = turtle.get_poly()    # 返回最后记录的多边形。
    turtle.register_shape(name, handForm)

# 3.初始化函数
def Init():
    print('@3')
    global secHand, minHand, hurHand, printer   # 定义全局变量
#    turtle.bgpic('../image/cat.gif')            # 背景图片

    turtle.mode("logo")             # 采用 logo 坐标、角度系统 ！！  海龟头朝北 12 点钟方向。
    mkHand("secHand", 135,1)          # 3.1 调用指针函数，參數是 秒針
    mkHand("minHand", 125,2)          # 3.1 调用指针函数，參數是 分針
    mkHand("hurHand", 90,7)           # 3.1 调用指针函数，參數是 時針

    secHand = turtle.Turtle()
    secHand.shape("secHand")        # 用shape 函數定義一個 秒 指針
    minHand = turtle.Turtle()
    minHand.shape("minHand")        # 用shape 函數定義一個 分 指針
    hurHand = turtle.Turtle()
    hurHand.shape("hurHand")        # 用shape 函數定義一個 時 指針

#     for hand in secHand, minHand, hurHand:
#         hand.shapesize(6, 1, 3)     # 返回箭頭的形狀大小：寬度、長度、輪廓
#         hand.speed(0)               # 畫筆的速度

    printer = turtle.Turtle()   # 建立输出文字Turtle

    printer.hideturtle()        # 隐藏画笔的turtle形状
    printer.penup()             # 抬筆

# 4.畫鐘盤函數，參數數是鐘盤直徑
def SetupClock(radius):
    print('@4')
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    turtle.pencolor("#ff5500")
    turtle.fillcolor("green")

    for i in range(60):         # 鐘框的 60 格
        Skip(radius)            # 調用畫筆運動函數
        if i % 5 == 0:
            turtle.forward(20)
            Skip(-radius - 20)

            Skip(radius + 20)
            if i == 0:
                turtle.write(int(12), align="center", font=("Courier", 14, "bold"))
            elif i == 30:
                Skip(25)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-25)
            elif (i == 25 or i == 35):
                Skip(20)
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
                Skip(-20)
            else:
                turtle.write(int(i / 5), align="center", font=("Courier", 14, "bold"))
            Skip(-radius - 20)
        else:
            turtle.dot(5)
            Skip(-radius)
        turtle.right(6)

def Week(t):                        # 計算當前時間的星期 ？ 函數
    week = ["星期一", "星期二", "星期三",
            "星期四", "星期五", "星期六", "星期日"]
    return week[t.weekday()]

def Date(t):                        # 計算日期的函數
    y = t.year
    m = t.month
    d = t.day
    return "%s-%d-%d" % (y, m, d)   # 返回： 年 - 月 - 日

# 5.定義指針、打印文字的函數
def Tick():
    print('@5')
    t = datetime.today()            # 绘制表针的动态显示
    second = t.second + t.microsecond * 0.000001    # 計算 秒
    minute = t.minute + second / 60.0               # 計算 分
    hour = t.hour + minute / 60.0                   # 計算 小時
    secHand.setheading(6 * second)
    minHand.setheading(6 * minute)
    hurHand.setheading(30 * hour)

    printer.forward(65)
    printer.write(Week(t), align="center",
                  font=("Courier", 14, "bold"))     # 畫出文字：星期；調用了星期計算函數
    printer.back(130)
    printer.write(Date(t), align="center",
                  font=("Courier", 14, "bold"))     # 畫出日期 年-月-日；調用計算日期的函數
    printer.home()

    turtle.ontimer(Tick, 100)       # 100ms后继续调用tick  循環，反復

# 2.主程序函數
def main():
    print('@2')
    Init()                  # 調用 3.初始化函數
    turtle.tracer(False)    # 關閉海龜动画，并为更新图纸设置延迟。
    SetupClock(160)         # 調用 4.畫鐘盤函數，參數是鐘的直徑
    turtle.tracer(True)     # 開啟海龜动画，并为更新图纸设置延迟。
    Tick()                  # 調用 5.畫指針函數
    turtle.mainloop()

# 1.程序入口
if __name__ == "__main__":
    main()

#  原文链接：https://blog.csdn.net/qq_32067045/article/details/80243430