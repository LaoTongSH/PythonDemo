# !-- coding:utf-8 --!
# CSDN.Applets  §02.6 例題 碰壁變色的迴力球。
# !@File:§02.6.py
# !@Author:
# !@Time:2020/1/3--13:58

import pygame
from pygame.locals import *
import random
import sys

pygame.init()

screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("回力球")
pos_x = 100     # 矩形坐標
pos_y = 100
long = 80       # 長
high = 80       # 寬
vel_x = 0.3     # 设置速度变量
vel_y = 0.3

color = 255, 0, 0

while True:     # 進入死循環
    for event in pygame.event.get():
        if event.type == pygame.QUIT:       #in (QUIT, KEYDOWN):   # 退出機制
            exit()
    screen.fill((255, 255, 255))        # 填滿畫布(R,G,B)

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    pos_x += vel_x      # 矩形移動
    pos_y += vel_y
    if pos_x > 520 or pos_x < 0:    # 让矩形在窗口范围内移动
        vel_x = -vel_x
        color = r, g, b
    if pos_y > 420 or pos_y < 0:
        vel_y = -vel_y
        color = r, g, b

    # 創建新坐標下的矩形和圓球
    pygame.draw.rect(screen, color, (pos_x, pos_y, long, high), 0)
    pygame.display.update()




