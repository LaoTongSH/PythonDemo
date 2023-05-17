# !-- coding:utf-8 --!
# !核桃: L14.枚舉與遞歸
# !@File:code\Coco\ L14.03.py
# !@Author:
# !@Time:2022/2/7--15:05
# !有1,2,3,4 四個數字，能組成多少個各不相同且無重複數字的三位數？

for x in range(1,5):
    for y in range(1,5):
        for z in range(1,5):
            if (x != y) and (x != z) and (y != z):
                print('%d%d%d' % (x, y, z))
