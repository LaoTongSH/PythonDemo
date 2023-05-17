from functools import reduce
def format_name(s):
    return s[0].upper()+s[1:].lower()
print(list(map(format_name,['adam', 'LISA', 'barT'])))
print("**********************************************")
def prod(x, y):
    return  x*y
print(reduce(prod, [2, 4, 5, 7, 12]))