class Person(object):
    def __init__(self,name,gender,birth,job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job

xiaoming = Person('Xiao Ming', 'Male', '1990-1-1', 'Student')
print(xiaoming.name)
print(xiaoming.job)
