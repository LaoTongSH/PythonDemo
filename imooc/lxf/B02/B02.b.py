#匿名函数
L=lambda x , y : x*y
a=2
b=5
print('长 = ',a, '; 寛 = ',b ,'\n面积是 ：',L(a,b))
print("**********************************************")

print(list(filter(lambda s: s and len(s.strip())>0,['test', None, '', 'str', '  ', 'END'])))