# !-- coding:utf-8 --!
# CSDN.Applets  §03.
# !@File:code\Csdn\Applets\03\ 03.a1.py
# !@Author:https://zhidao.baidu.com/question/751055130403603172.html
# !@Time:2020/1/18--10:58

from turtle import Turtle, Screen
MAP = '''
XXXXXXXXOX
XOOOOOOOOX
XOXXXXXXXX
XOOOOXXXXX
XXXXOXXXXX
XXXXOXXXXX
XXXXOOOOOX
XXXXXXXXOX
XOOOOOOOOX
XOXXXXXXXX
'''
MAP_ARRAY = [list(row) for row in MAP.strip().split('\n')]
MAP_ARRAY.reverse()  # put 0, 0 in lower left corner
ADJACENT = [
              (0,  1),
    (-1,  0),          (1,  0),
              (0, -1),
]
SCALE = 3
STAMP_SIZE = 20
WIDTH, HEIGHT = len(MAP_ARRAY[0]), len(MAP_ARRAY)
def any_adjacent(x, y):
    return [(x + dx, y + dy) for dx, dy in ADJACENT if 0 <= x + dx < WIDTH and 0 <= y + dy < HEIGHT and MAP_ARRAY[y + dy][x + dx] == 'O']
def move():  # slowly navigate the MAP, quit when no where new to go
    x, y = turtle.position()
    adjacent_squares = any_adjacent(int(x), int(y))
    # always moves to first valid adjacent square, need to consider
    # how to deal with forks in the road (e.g. shuffle adjacent_squares)
    for adjacent in adjacent_squares:
        if adjacent not in been_there:
            turtle.goto(adjacent)
            been_there.append(adjacent)
            screen.ontimer(move, 1000)  # one second per move, adjust as needed
            break
screen = Screen()  # recast the screen into MAP coordinates
screen.setup(WIDTH * STAMP_SIZE * SCALE, HEIGHT * STAMP_SIZE * SCALE)
screen.setworldcoordinates(-0.5, -0.5, WIDTH - 0.5, HEIGHT - 0.5)
turtle = Turtle('square', visible=False)
turtle.shapesize(SCALE)
turtle.speed('fastest')
turtle.penup()

for y, row in enumerate(MAP_ARRAY):  # draw the MAP
    for x, character in enumerate(row):
        if character == 'X':
            turtle.goto(x, y)
            turtle.stamp()

turtle.color('red')
turtle.shapesize(SCALE / 2)
turtle.goto(1, 0)  # should use unique character in MAP to indicate start & end points
turtle.showturtle()
been_there = []  # prevent doubling back
move()
screen.mainloop()