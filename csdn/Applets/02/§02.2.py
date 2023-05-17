# !-- coding:utf-8 --!
# CSDN.Applets  §02.2 例題  畫五角星 ellipse
# !@File:§02.2.py
# !@Time:2019/12/22--21:51
import pygame
from pygame.locals import *
import sys
import math as m

pygame.init()
white = 255,255,255
black = 0,0,0
green = 0,255,0

center_x = 200
center_y = 200
r = 100
myfont = pygame.font.Font(None, 30)

points =[
    # A 點
    (center_x-int(r*m.sin(2*m.pi/5)),center_y-int(r*m.cos(2*m.pi/5))),
    # C 點
    (center_x+int(r*m.sin(2*m.pi/5)),center_y-int(r*m.cos(2*m.pi/5))),
    # E 點
    (center_x-int(r*m.sin(m.pi/5)),center_y+int(r*m.cos(m.pi/5))),
    # B 點
    (center_x,center_y-r),
    # D 點
    (center_x+int(r*m.sin(m.pi/5)),center_y+int(r*m.cos(m.pi/5)))
    ]

size = width,height = 400,400
screen = pygame.display.set_mode((size))                # 初始化和设置窗口大
caption = pygame.display.set_caption("Pygame 作圖")      # 设置窗口标题
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():        #
        if event.type in (QUIT, KEYDOWN):   # 監聽鼠標和鍵盤，按窗口的X、長按鍵盤，退出！
            sys.exit()
    screen.fill((white))                # 窗口背景色填充(R,G,B)
    pygame.draw.polygon(screen, green, points, 0)   # 線寬為零，將形成另外圖形
    A =myfont.render("A", True, black)
    B =myfont.render("B", True, black)
    C =myfont.render("C", True, black)
    D =myfont.render("D", True, black)
    E =myfont.render("E", True, black)
    screen.blit(A, (center_x-int(r*m.sin(2*m.pi/5)),center_y-int(r*m.cos(2*m.pi/5))))
    screen.blit(B, (center_x,center_y-r))
    screen.blit(C, (center_x+int(r*m.sin(2*m.pi/5)),center_y-int(r*m.cos(2*m.pi/5))))
    screen.blit(D, (center_x+int(r*m.sin(m.pi/5)),center_y+int(r*m.cos(m.pi/5))))
    screen.blit(E, (center_x-int(r*m.sin(m.pi/5)),center_y+int(r*m.cos(m.pi/5))))
    pygame.display.update()
