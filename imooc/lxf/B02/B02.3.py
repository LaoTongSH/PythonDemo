#從一個列表中挑選出奇數，構成新的列表
def is_odd(x):
    return x % 2 ==1    #除2餘數為1即奇數
print(list(filter(is_odd,[1,4,6,7,9,12,17]))) #調用
a = '  rwmmdcm'
print(a.strip())
