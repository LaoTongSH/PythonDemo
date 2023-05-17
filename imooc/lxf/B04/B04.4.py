class Person(object):
    def __init__(self, name):
        self.name = name
        self._title = 'Mr'          #单下划线
        self.__job = 'Student'      #双下划线

p = Person('Bob')

print(p.name)
print(p._title)
print(p.__job)