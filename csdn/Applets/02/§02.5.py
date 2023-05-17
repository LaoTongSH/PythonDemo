# !-- coding:utf-8 --!
# CSDN.Applets  §02.5 例題 隨機畫出千條線
# !@File:§02.5.py
# !@Author:
# !@Time:2020/1/3--13:03
import pygame
import random
import sys
import time
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption("Random Lines")

n = 1

while n < 1000:
    for event in pygame.event.get():
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    # 随机起点和终点，随机颜色r,g,b，線寬的计算
    x = random.randint(0, 600)
    y = random.randint(0, 500)
    x1 = random.randint(0, 600)
    y1 = random.randint(0, 500)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    w = random.randint(1,5)
    color = r, g, b
    pygame.draw.line(screen, color, (x, y), (x1, y1), w)
    pygame.display.update()
    n += 1
    time.sleep(0.05)  # 一次做完延迟0.05秒做下一次，不然会一下子跑完。

