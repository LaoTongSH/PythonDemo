#慕课网 廖雪峰教程 B4.6 任务
class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name

p1 = Person('Bob')
Person.count = Person.count+1
print(Person.count)

p2 = Person('Alice')
Person.count = p2.count+1
print(p2.count)

p3 = Person('Tim')
#Person.count = Person.count+1
print(p3.count)
print(Person.count)