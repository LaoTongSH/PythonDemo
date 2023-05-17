#-*- coding:utf-8 -*-
#用 Python 的 For 循環 遍歷字典
d = {'Adam':15,'Lisa':50,'Bart':80}
print(key for key in d.items())
print([key for key in d.items()])
print(list(key for key in d.items()))
print("**********************************************************")
print("输出所有的 Key ： %s"%(key for key in d.keys()))
print("输出所有的 Key ： %s"%([key for key in d.keys()]))
print("输出所有的 Key ： %s"%list(key for key in d.keys()))
print("输出所有的 Value ： %s" %list(value for value in d.values()))