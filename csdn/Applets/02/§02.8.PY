# !-- coding:utf-8 --!
# CSDN.Applets  §02.8 例题  克隆 turtle  回力球
# !@File:code\Csdn\Applets\02\§02.8.py
# !@Author:
# !@Time:2020/1/15--23:10

import sys,pygame
from random import *

class MyDogClass(pygame.sprite.Sprite):     # 设置類
    def __init__(self, image_file, location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = - self.speed[0]

        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]

size = width,height = 640,480           # 设置窗口的宽和高
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])              # 设置窗口的颜色-白色
img_file = "../image/qiu.png"           # 设置角色的图片
dogs = []
for row in range(0,3):
    for column in range(0,3):
        location = [column * 180 + 10,row * 180 + 10]
        speed = [choice([-2,2]), choice([-2,2])]
        dog = MyDogClass(img_file,location,speed)
        dogs.append(dog)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.time.delay(20)
    screen.fill([255,255,255])
    for dog in dogs:
        dog.move()
        screen.blit(dog.image, dog.rect)
    pygame.display.flip()

pygame.quit()



#原文链接：https://blog.csdn.net/qq_37369201/article/details/84065079



# done()                  # 結束
