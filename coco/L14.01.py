# !-- coding:utf-8 --!
# !核桃: L14.枚舉與遞歸
# !@File:code\Coco\ L14.01.py
# !@Author:
# !@Time:2022/2/7--11:14

for i in range(1,100):
    for j in range(1,100):
        if i + j == 100 and i * 3 + j / 3 == 100:
            print('大和尚：',i)
            print('小和尚：',j)

for x  in range(1,100):
    for y in range(1,100):
        for z in range(1,100):
            if x + y + z ==100 and x*5 + y*3 +z*0.5==100:
                print('大和尚:',x,'共得金幣:',x*5)
                print('中和尚:', y, '共得金幣:', y * 3)
                print('小和尚:', z, '共得金幣:', z * 0.5)

for i in range(1,101):
    x = i*3
    y = (100-i)*(1/3)
    if x+y == 100:
        print(i)
        print(100-i)