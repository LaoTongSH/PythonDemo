# !-- coding:utf-8 --!
# CSDN.Applets  §02.1 例题 Pygame 基本圖形
# !@File:02.1.py
# !@Author:
# !@Time:2019/12/27--15:59

import pygame
from pygame.locals import *
import sys
import math

red = 255,0,0           # 紅色
white = 255, 255, 255   # 白色
blue = 0, 0, 255        # 藍色
color = 255, 255, 0     # 黃色
green = 0, 255, 0       # 綠色
color1 =0, 255, 255
color2 =255,0, 255

px = 300         # 園心坐標 X
py = 250         # 圓心坐標 Y
radius = 100     # 設置半徑
width = 3        # 設置線寬
position2 = px + radius, py   # 設置第2個坐標中心

pygame.init()                 # 初始化

# 注意，位置和颜色作为数组，都必须括起来作为参数！实际是双层括号
screen = pygame.display.set_mode((600, 500))            # 初始化和设置窗口大小
caption = pygame.display.set_caption("Pygame 作圖")      # 设置窗口标题
myfont = pygame.font.Font(None, 100)                    # 設置字體
textImage = myfont.render("Hello,Pygame", True, white)  # 設置文本內容、文字顏色

while True:
    for event in pygame.event.get():        #
        if event.type in (QUIT, KEYDOWN):   # 監聽鼠標和鍵盤，按窗口的X、長按鍵盤，退出！
            sys.exit()
    screen.fill((0, 0, 200))                # 窗口背景色填充(R,G,B)

    # display text 文本
    screen.blit(textImage, (50, 50))        # 參數：文本內容、坐標

    # draw a line   直線
    linepost1 =50,120   # 直線起點
    linepost2 =500,120  # 直線終點
    pygame.draw.line(screen, red, linepost1, linepost2, width)

    # draw a cycle 繪圓
    pygame.draw.circle(screen, red, (px,py), radius, width)
    # 圓心十字線
    pygame.draw.line(screen, red, (px-5,py), (px+5,py), 1)
    pygame.draw.line(screen, red, (px,py-5), (px, py+5), 1)

    # draw 2 rect   矩形
    position_r1 = 50, 200, 100, 100    # x、y坐標；寬、高
    position_r2 = 400, 200, 100, 100   # 同上
    pygame.draw.rect(screen, white, position_r1, width)     # 矩形
    pygame.draw.rect(screen, color, position_r2, 0)         # 實心矩形

    # 多邊形
    pointlist = [(100,450),(500,450),(300,350)]
    pygame.draw.polygon(screen, color1, pointlist, width)

    # 橢圓--內接矩形的橢圓
    ellpoint = 200, 200, 200 ,100   # 矩形的頂點、長、寬
    pygame.draw.ellipse(screen, color2, ellpoint, 2)

    # draw arc 圓弧
    arcpos = 150, 150, 200, 200     # 矩形的頂點、長、寬
    start_angle = math.radians(90)  # 起始弧度
    end_angle = math.radians(270)   # 結束弧度
    pygame.draw.arc(screen, green, arcpos, start_angle, end_angle, width)

    # 多線段 封閉:1/開口:0
    pygame.draw.lines(screen,color,0,[(40,40),(560,40),(560,460),(40,460)],5)

    # 平滑線
    pygame.draw.aaline(screen,color,(40,190),(160,310),0)

    # 多線段平滑線 封閉:1/開口:0
    pointlist = [(20,20),(580,20),(500,150),(580,480),(20,480),(50,350)]
    pygame.draw.aalines(screen, red, 1, pointlist, 1)

    pygame.display.update()



