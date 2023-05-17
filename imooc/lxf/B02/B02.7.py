#自定义排序函数 sorted 对字符串排序
print(sorted(['bob', 'about', 'Zoo', 'Credit']))
print("*************************************************")
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper))
print(sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper,reverse = True))