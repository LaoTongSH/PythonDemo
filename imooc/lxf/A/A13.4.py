#A13章第三小节任务，过滤并输出大写的字符串
def toUppers(L):
    return [Str.upper() for Str in L if isinstance(Str, str)]
print(toUppers(['Hello', 'world', 101]))