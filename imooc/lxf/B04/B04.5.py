class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score    #双下划线

p = Person('Bob', 59)
print(p.name)
try :
    print(p.__score)                #不能访问
except AttributeError:
    print('attributeerror')