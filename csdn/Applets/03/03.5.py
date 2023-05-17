# !-- coding:utf-8 --!
# CSDN.Applets  §03.3.1 例题  创建 turtle  自定义光标
# !@File:code\Csdn\Applets\03\03.5.py
# !@Author:https://www.cnblogs.com/asworm/p/7045498.html
# !@Time:2020/1/10--22:57

from turtle import *    # 導入
from time import *

t = 0.5                 # 設置停頓時間
up()                    # 抬筆
goto(-75,-75)           # GO
down()                  # 落筆畫畫
w = 1
h = 1
def movitation():           # 定義造型變換函數
    for i in range(1):      # 循環 0，1次
        shape('arrow')      # 設置造型為：箭頭
        sleep(t)            # 停頓
        shape('circle')     # 設置造型為：圓
        sleep(t)
        shape('triangle')   # 設置造型為：三角形
        sleep(t)
        shape('turtle')     # 設置造型為：烏龜
        sleep(t)
        shape('square')     # 設置造型為：方塊
        sleep(t)

for i in range(6):      # 循環 0-5 ，六次。
    turtlesize(w, h)
    movitation()        # 調用造型變換函數
    forward(150)        # 前進100步
    left(60)            # 向左轉 60 度(逆時針)
    w += 1
    h += 1

done()                  # 結束

