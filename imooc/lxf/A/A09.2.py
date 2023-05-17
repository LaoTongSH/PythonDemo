#-*- coding:utf-8 -*-
#用 Python 的 For 循環 遍歷字典
d = {'Adam':15,'Lisa':50,'Bart':80}
print(d)
for key in d.keys():
    print(key,d[key])
for key in d.keys():
    print(key,", ",end="")
print()
for value in d.values():
    print(value,", ",end="")
print()
for key in d.keys():
    print("key = %s, value = %s" %(key, d[key]))
print()
print("*************")
for k , v in d.items():
    print("K = %s , V=%s" %(k ,v ))
print("*************")
#print("k=%s  , v=%s " %(k , v) for k ,v in d.items())
for entry in d.items():
    key , value = entry
    print(" %s, %s"%(key,value))


