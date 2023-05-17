# !-- coding:utf-8 --!
# CSDN.Applets  §02.3 例題   會移動並彈回的圖形
# !@File:§02.3.py
# !@Author:
# !@Time:2019/12/28--17:36

import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("回力球")
pos_x = 300     # 矩形坐標
pos_y = 250
long = 50       # 長
high = 50       # 寬
vel_x = 0.1     # 设置速度变量
vel_y = 0.1

circlex = 50   # 球心坐標_x
circley = 50
radius = 30     # 半徑
cr_x = 1        # 设置速度变量
cr_y = 1

red = 255, 0, 0 # 設置圖形顏色
color = 255, 255, 0

width = 0       # 圖形線寬為0，填滿圖形

while True:     # 進入死循環
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):   # 退出機制
            exit()
    screen.fill((0, 0, 200))        # 填滿畫布(R,G,B)

    pos_x += vel_x      # 矩形移動
    pos_y += vel_y
    if pos_x > 550 or pos_x < 0:    # 让矩形在窗口范围内移动
        vel_x = -vel_x
    if pos_y > 450 or pos_y < 0:
        vel_y = -vel_y

    circlex += cr_x     # 圓球移動
    circley += cr_y
    if circlex > 550 or circlex < 50:   # 让圓球在窗口范围内移动
        cr_x = -cr_x
    if circley > 450 or circley < 50:
        cr_y = -cr_y
    # 創建新坐標下的矩形和圓球
    pygame.draw.rect(screen, color, (pos_x, pos_y, long, high), width)
    pygame.draw.circle(screen, red, (circlex,circley), radius, width)
    pygame.display.update()
