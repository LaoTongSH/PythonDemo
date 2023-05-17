#Python 入门 第13章 第四节练习和任务②③
L = [m + n for m in 'ABC' for n in '123']
print(L)
print("************************************************************")
L1 = [X + Y + Z for X in '123456789' for Y in '0123456789' for Z in '123456789' if X==Z]
print(L1)
print([int(X+Y+Z) for X in '123456789' for Y in '0123456789' for Z in '123456789' if X==Z])