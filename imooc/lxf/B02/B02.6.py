#自定义排序函数 sorted
print(sorted([-36,5,-12,9,21]))
print(sorted([-36,5,-12,9,21],reverse = True))
print(sorted([-36,5,-12,9,21],key = abs))
print(sorted([-36,5,-12,9,21],key = abs,reverse = True))
