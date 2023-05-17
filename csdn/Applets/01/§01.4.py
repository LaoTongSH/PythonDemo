# CSDN.Applets  §01.2 例题 汉诺塔移动
num = 0
def move(A, C):
    global num        # 用 global 定義成全局變量
    num += 1
    print('第 ',num,' 次 ',A, '--->', C,';')

def hanoi(n, A, B, C):
    if n == 1:
        move(A, C)
    else:
        hanoi(n - 1, A, C, B)
        move(A, C)
        hanoi(n - 1, B, A, C)

hanoi(4, 'A', 'B', 'C')     # 第一個參數是柱子上有幾層盤子。
print('共需要 ',num,' 次，才能完成。')

