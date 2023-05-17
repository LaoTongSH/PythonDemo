# !-- coding:utf-8 --!
# CSDN.Applets  §03.4.2 例题     用海龜畫一口鐘
# !@File:code\Csdn\Applets\03\03.9.2.py
# !@Author:
# !@Time:2020/1/10--10:23

import turtle as t      # 導入 turtle 到 t
import datetime as d    # 導入 datetime 到 d
import time             # 導入 time
T = 2

# 3.1 定義畫筆運走函数，抬筆跳到 step 再落筆
def skip(step):
    t.penup()           # 抬笔
    t.forward(step)     # 前进
    t.pendown()         # 落笔

# 3.画表盘函数，参数：半径
def drawClock(radius):  # turtle：T-1
    t.speed(T)          # 設置畫筆的速度
    t.mode("logo")      # 以Logo坐标、角度方式，Y轴正向 0 度，顺时针。
    t.hideturtle()      # 隱藏 turtle 箭頭 / t.showturtle() 显示箭頭
    t.pensize(7)        # 设置笔宽
    t.home()            # 回到原点
    t.tracer(False)     # 關閉 turtle 動畫效果
    for j in range(60): # 畫表盤 60秒 的刻度的循環語句。
        skip(radius)    # 3.1 調畫筆運動函數，到圓周邊上:R1。
        if (j % 5 == 0):    # 画整 5 分钟的刻度。
            t.forward(20)   # 前進 20，畫刻度，線長 20 :R2 = R1+20
            if j == 0:      # 寫 12
                t.write(int(12), align="center", font=("Courier", 18, "bold"))
            elif j == 30:   # 寫 6
                skip(30)    # 抬筆進 30 :R3 = R2+30
                t.write(int(j / 5), align="center", font=("Courier", 18, "bold"))
                skip(-30)   # 回到大圓周 R2
            elif (j == 20 or j == 40):  # 寫 4、8
                skip(20)
                t.write(int(j / 5), align="center", font=("Courier", 18, "bold"))
                skip(-20)
            elif (j == 25 or j == 35):  # 寫 5、7
                skip(30)
                t.write(int(j / 5), align="center", font=("Courier", 18, "bold"))
                skip(-30)
            else:                       # 寫 其他字
                t.write(int(j / 5), align="center", font=("Courier", 18, "bold"))

            skip(-radius - 20)          # 後退半徑+刻度長(回到原點)
        else:
            t.dot(5)        # 画刻度的点
            skip(-radius)   # 從園周上，後退半徑長度回到原點
        t.right(6)          # 右转 6度

# 4.1 把三指针注册成 shape 的函数；参数：名称、指针长
def makePoint(pointName, len):
    t.penup()                   # 抬筆
    t.home()                    # 回原點
    t.begin_poly()              # 开始繪製
    t.back(0.1 * len)           # 指針尾端長
    t.forward(len * 0.35)       # 指針前端長
#    t.pensize(1)
#    t.color('black','White')
    if pointName != "secPoint": # 時、分指針繪製葫蘆
        t.right(90)
        t.circle(6)
        t.left(90)
        t.forward(16)
        t.right(90)
        t.circle(4)
        t.left(90)
        t.forward(12)
        t.right(90)
        t.circle(2)
        t.left(90)
    t.forward(len * 0.45)        # 指針前端長
    t.end_poly()                # 結束繪製
    poly = t.get_poly()         # 獲取繪製
    t.register_shape(pointName, poly)  # 注册为一个shape

# 4.创建画指针、写日期共四个 turtle 的函数
def drawPoint():
    global hourPoint, minPoint, secPoint, fontWriter # 定義4个 turtle 为全局變量
    makePoint("hourPoint", 60)      # 调用 4.1 画指针函数，参数：名称、指针长
    makePoint("minPoint", 110)      # 调用 4.1 画指针函数，参数：名称、指针长
    makePoint("secPoint", 190)      # 调用 4.1 画指针函数，参数：名称、指针长

    hourPoint = t.Pen()             # 啟用 时针 畫筆，注册 turtle-T.2
    hourPoint.shape("hourPoint")    # 改变成时针造型
    hourPoint.shapesize(1,1,6)     # 设置指针形状 参数：宽、长、轮廓线宽度

    minPoint = t.Pen()              # 啟用 分针 畫筆，注册 turtle-T.3
    minPoint.shape("minPoint")      # 改变成分针造型
    minPoint.shapesize(1, 1, 3)     # 设置指针形状 参数：宽、长、轮廓线宽度

    secPoint = t.Pen()              # 啟用 秒针 畫筆，注册 turtle-T.4
    secPoint.shape("secPoint")      # 改变成秒针造型
    secPoint.shapesize(1,1,2)       # 设置指针形状 参数：宽、长、轮廓线宽度
    secPoint.pencolor('red')        # 定义秒針為 紅色

    fontWriter = t.Pen()            # 啟用 寫字 畫筆，创建钟盘日期 turtle-T.5
    fontWriter.pencolor('black')    # 设置钟盘日期的颜色 gray
    fontWriter.hideturtle()         # 隐藏画笔

# 5.1 转换星期表示的函数
def getWeekName(weekday):
    weekName = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return weekName[weekday]

# 5.2 获取年、月、日函数
def getDate(year, month, day):
    return "%s-%s-%s" % (year, month, day)

# 5.读时间函數(動態)，并显示三指针的实时时间
def realTime():
    curr = d.datetime.now()         # 獲取當前時間
    curr_year = curr.year           # 年
    curr_month = curr.month         # 月
    curr_day = curr.day             # 日
    curr_hour = curr.hour           # 小時
    curr_minute = curr.minute       # 分
    curr_second = curr.second       # 秒
    curr_weekday = curr.weekday()   # 计算星期 ?，查例表 weekName

    t.tracer(False)                 # 關閉 turtle 動畫效果，使多個 turtle 一起顯示。
    secPoint.setheading(360 / 60 * curr_second)     # 计算秒针的角度朝向
    minPoint.setheading(360 / 60 * curr_minute)     # 计算分针的角度朝向
    hourPoint.setheading(360 / 12 * curr_hour + 30 / 60 * curr_minute)  # 正点+之间的角度朝向

    fontWriter.clear()              # 清屏 清掉 turtle-D 的痕迹
    fontWriter.home()               # turtle-D 回到中心原点
    fontWriter.penup()              # 抬笔
    fontWriter.forward(90)          # 定义星期 X 文字的 Y 坐标
    # 调用 5.1 转换星期函数，并用 turtle-D 画到钟盘上。
    fontWriter.write(getWeekName(curr_weekday), align="center", font=("Courier", 18, "bold"))
    fontWriter.forward(-180)        # 定义 年-月-日 文字的 Y 坐标
    # 调用 5.2 获取实时日期函数，并用 turtle-D 输出
    fontWriter.write(getDate(curr_year, curr_month, curr_day), align="center", font=("Courier", 18, "bold"))
    t.tracer(True)                  # 開啟 turtle 動畫效果
#    print(curr,'星期',curr_weekday)  # 動態輸出到輸出區
#    print(curr_second)              # 调试用语句，在输出区输出实时时间。
    t.ontimer(realTime, 100)        # 每隔100毫秒调用一次realTime() 形成循环！

# 2.主程序函數
def main():
#    t.bgpic('../image/turtle.png')  # 背景图片
    drawClock(160)      # 调用 3.画表盘函数，参数是半径
    drawPoint()         # 调用 4.画指针、写文字函数
    realTime()          # 调用 5.时间函数
    t.mainloop()        # 调用 mainloop() 方法，等待响应，进入循环。


# 1.程序入口
if __name__ == '__main__':
    main()              # 調用 函數main()

# 参考：https://blog.csdn.net/July__July/article/details/99543992