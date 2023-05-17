# !-- coding:utf-8 --!
# CSDN.Applets  §03.3.4 例题  角色被點擊
# !@File:code\Csdn\Applets\03\ 03.8.py
# !@Author:
# !@Time:2020/1/22--21:56

from turtle import *

bgpic('../image/sea.png') # 背景圖片
shape('turtle')         # 設置形狀為海龜
pencolor('red')         # 設置顏色
turtlesize(2,2)         # 設置大小

def move_l(x, y):       # 海龜向左移動函數
    up()                # 抬筆，隱藏海龜移動軌跡
    x -=50              # 向左移動 50
    if x < -250:        # 條件語句，規定 X 移動範圍。
        x = 200         # 設置新坐標
        hideturtle()    # 從右邊界移動到左邊界時，隱藏海龜移動顯示。
    goto(x, y)          # 移動到右邊界
    showturtle()        # 顯示海龜

def move_r(x, y):       # 海龜向右移動函數
    up()                # 抬筆，隱藏海龜移動軌跡
    x +=50              # 向右移動 50
    if x > 250:         # 條件語句，規定 X 移動範圍。
        x = -250        # 設置新坐標
        hideturtle()    # 從左邊界移動到右邊界時，隱藏海龜移動顯示。
    goto(x, y)          # 移動到右邊界
    showturtle()        # 顯示海龜
onclick(move_l)         # 角色(海龜)被 鼠標左鍵 點擊，調用 左 移動函數。
onclick(move_r,3)       # 角色(海龜)被 鼠標右鍵 點擊，調用 右 移動函數
done()