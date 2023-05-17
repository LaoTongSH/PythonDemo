# !-- coding:utf-8 --!
# CSDN.Applets  §03.3.2 例题  创建 图片 turtle
# !@File:code\Csdn\Applets\03\03.6.py
# !@Author:
# !@Time:2020/1/18--11:34

import pygame   # 导入pygame模块

pygame.init()   # 初始化pygame
width = 400
height = 150
speed = 0.01    # 设置移动速度

# 创建舞台,利用Pygame中的display模块，来创建窗口
screen = pygame.display.set_mode((width, height),0,32)
# 设置窗口标题
pygame.display.set_caption("Hello PyGame")

# laod函数加载图片
cat = pygame.image.load("../image/cat1.gif")
print(cat)

cat_x, cat_y = 0, 0     # 猫的坐标
h_direction = 1         # 水平方向

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:   # 退出机制
            pygame.quit()
    # blit函数的作用是把加载的图片放到舞台的（cat_x, cat_y）坐标的位置
    screen.blit(cat, (cat_x, cat_y))
    # 这样就实现了会移动的猫
    cat_x += speed * h_direction
    # 如果猫的坐标超出了400-145，145是猫图片的宽度，就让小猫反向
    # 如果猫的坐标小于了0，也让小猫反向，这样就实现了碰到墙壁反弹的效果
    if cat_x > width-145:
        h_direction = -h_direction
    elif cat_x < 0:
        h_direction = -h_direction
    pygame.display.update()     # 重复
