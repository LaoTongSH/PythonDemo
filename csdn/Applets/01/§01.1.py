# CSDN.Applets  §01.1.2 例题  求100之内的素数
def _odd_iter():        # 先构造一个从3 开始的奇数序列
    print('1*')     ### 附加的觀察代碼 ###
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):  # 定义一个符合素數條件的筛选器
    print('2*')     ### 附加的觀察代碼 ###
    return lambda x:x%n>0
def primes():           # 定义生成器，不断返回下一个素数
    print('3*')     ### 附加的觀察代碼 ###
    yield 2             # 關鍵字、返回生成器；下一次迭代從下一行代碼開始執行。
    it = _odd_iter()    # 初始化序列
    while True:
        print('**') ### 附加的觀察代碼 ###
        n = next(it)    # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n),it)   # 造新的序列
for n in primes():      # 定義構造100之內的素數
    print('4*',n)   ### 附加的觀察代碼 ###
    if n < 50:         # 不得超过 100
        print(n,'；',end='')                 # 不換行打印輸出。
    else:
        break

