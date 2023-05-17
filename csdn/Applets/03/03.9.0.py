# !-- coding:utf-8 --!
# CSDN.Applets  §03.4.0 例题  画表盘
# !@File:code\Csdn\Applets\03\ 03.9.0.py
# !@Author:
# !@Time:2020/1/23--21:49

import turtle

screen = turtle.Screen()    # 实例化一个屏幕对象
screen.bgcolor('yellow')    # 把屏幕的背景颜色设置为黄色

baby = turtle.Turtle()  # 实例化一个小乌龟，命名为baby，这也就是我们的画笔
baby.shape('turtle')    # 把画笔的笔尖形状设置为一只小乌龟，方向 X 正向。
baby.color('green')     # 画笔的颜色设为绿色
baby.speed('slowest')   # 绘画速度设为最慢
baby.penup()            # 抬笔离开屏幕，这样移动画笔只会改变位置，不会在屏幕上留下痕迹

baby.left(60)           # 龜頭轉向 1 點鐘方向。
for _ in range(12):     # 开启一个12次的循环，完成对表盘的绘制
    baby.forward(90)    # 不留痕迹地向前移动90个单位
    baby.pendown()      # 下笔
    baby.forward(20)    # 向前画一条长度为20个单位的线段
    baby.penup()        # 抬笔
    baby.forward(10)    # 不留痕迹地向前移动10个单位
#    baby.stamp()        # 把小乌龟的形象印在屏幕上（此时的小乌龟当成一个印章来用）
    # 寫錶盤的數字，注意函數 write() 的參數。
    baby.write(_+1,align="center", font=("Courier", 14, "bold"))
    baby.backward(120)  # 向后退120个单位，回到了起点
    baby.right(30)      # 顺时针旋转30度（360度的12分之1）

# 下面是画时针、分针和秒針。
baby.color('black')     # 設置黑色的時、分針。
baby.right(60)          # 右轉 2 個字。方向 3 點鐘。
baby.pendown()          # 把笔放下
baby.pensize(6)         # 把笔变粗一点
baby.backward(40)       # 向后移动，画一条长度为40个单位的线段，这就是时针
baby.forward(40)        # 向前移动，回到原点
baby.left(90)           # 逆时针旋转90度，方向 12 點鐘。
baby.pensize(3)         # 畫分針，筆尖細一點
baby.forward(60)        # 向前移动，画一条长度为60个单位的线段，这是分针
baby.backward(60)       # 向後移動，回到原點。

baby.right(60)          # 順时针旋转60度，方向 2 點鐘。
baby.color('red')       # 設置秒針顏色為紅色。
baby.pensize(1)         # 秒針寬度
baby.forward(80)        # 向前移动，画一条长度为80个单位的线段，这是秒针
baby.hideturtle()       # 全部内容都画完了，小乌龟隐身。

# 调用屏幕对象的mainloop方法，这样，在绘图结束之后屏幕不会突然消失，
# 而是静静等待我们手动关闭
screen.mainloop()

#原文链接：https://blog.csdn.net/weixin_44520259/article/details/99727362